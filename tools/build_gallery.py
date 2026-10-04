"""Build gallery images and maintain gallery/gallery.json.

Usage:
    python tools/build_gallery.py ["<source folder>"]

Writes:
    gallery/images/display/<slug>.webp  (long edge 1600 px, quality 82)
    gallery/images/full/<slug>.jpg      (long edge max 3000 px, quality 90, progressive)
    gallery/gallery.json                (caption text in existing entries is never changed)
"""

import io
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageCms, ImageOps

DEFAULT_SOURCE = r"C:\Users\adam\OneDrive\Pictures\Website Images"
EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}
DISPLAY_EDGE = 1600
FULL_EDGE = 3000
SLUG_MAX = 60

REPO = Path(__file__).resolve().parent.parent
GALLERY = REPO / "gallery"
DISPLAY_DIR = GALLERY / "images" / "display"
FULL_DIR = GALLERY / "images" / "full"
JSON_PATH = GALLERY / "gallery.json"

TEXT_FIELDS = ("title", "style", "description", "alt")

# Trailing Midjourney ID: _<uuid> with an optional _<index>.
MJ_ID = re.compile(r"_+[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}(_\d+)?$", re.I)
# Midjourney short links and parameters that the file name copies from the prompt.
# Link IDs are 11 characters, but a truncated file name can cut them short.
MJ_LINK = re.compile(r"https?s?\.mj\.run[A-Za-z0-9_-]{1,11}", re.I)
# A parameter and its value, for example "--ar 16:9" or "--raw". Runs after "_" becomes " ".
MJ_PARAM = re.compile(r"--[a-z]+(\s+(?!--)\S+)?", re.I)
# A link cut off at the end of the file name, for example "ht" or "https".
MJ_LINK_STUB = re.compile(r"\s+h(t(t(p(s(s)?)?)?)?)?\s*$", re.I)


def make_slug(stem):
    """Return a URL-safe slug, without the creator handle and the Midjourney ID."""
    text = stem
    if MJ_ID.search(text):
        text = MJ_ID.sub("", text)
        text = text.split("_", 1)[1] if "_" in text else text
    text = MJ_LINK.sub(" ", text)
    text = MJ_PARAM.sub(" ", text.replace("_", " "))
    text = MJ_LINK_STUB.sub("", " " + text)
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(text) > SLUG_MAX:
        text = text[:SLUG_MAX].rsplit("-", 1)[0] or text[:SLUG_MAX]
    return text.strip("-") or "image"


def unique_slug(base, used):
    slug, n = base, 2
    while slug in used:
        suffix = f"-{n}"
        slug = base[: SLUG_MAX - len(suffix)].rstrip("-") + suffix
        n += 1
    used.add(slug)
    return slug


def to_srgb(img):
    """Return an RGB image in sRGB, converting from an embedded ICC profile if present."""
    icc = img.info.get("icc_profile")
    if img.mode in ("RGBA", "LA", "PA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGBA")
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[-1])
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")
    if icc:
        try:
            src = ImageCms.ImageCmsProfile(io.BytesIO(icc))
            dst = ImageCms.createProfile("sRGB")
            img = ImageCms.profileToProfile(img, src, dst, outputMode="RGB")
        except (ImageCms.PyCMSError, OSError):
            pass  # Unreadable profile: treat the pixels as sRGB.
    return img


def fit(img, edge):
    """Scale down so the long edge is at most `edge`. Never upscale."""
    w, h = img.size
    scale = edge / max(w, h)
    if scale >= 1:
        return img.copy()
    return img.resize((round(w * scale), round(h * scale)), Image.LANCZOS)


def is_current(src, outputs):
    mtime = src.stat().st_mtime
    return all(p.exists() and p.stat().st_mtime > mtime for p in outputs)


def folder_size(path):
    return sum(f.stat().st_size for f in path.glob("*") if f.is_file())


def mb(n):
    return f"{n / 1_048_576:.1f} MB"


def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DEFAULT_SOURCE)
    if not source.is_dir():
        sys.exit(f"Source folder not found: {source}")

    DISPLAY_DIR.mkdir(parents=True, exist_ok=True)
    FULL_DIR.mkdir(parents=True, exist_ok=True)

    entries = json.loads(JSON_PATH.read_text(encoding="utf-8")) if JSON_PATH.exists() else []
    by_source = {e["source_name"]: e for e in entries}
    used = {e["id"] for e in entries}

    files = sorted(
        (p for p in source.iterdir() if p.is_file() and p.suffix.lower() in EXTENSIONS),
        key=lambda p: p.name.lower(),
    )
    ignored = sorted(
        p.name for p in source.iterdir() if p.is_file() and p.suffix.lower() not in EXTENSIONS
    )

    new, built, skipped = [], [], []
    for src in files:
        entry = by_source.get(src.name)
        slug = entry["id"] if entry else unique_slug(make_slug(src.stem), used)
        display = DISPLAY_DIR / f"{slug}.webp"
        full = FULL_DIR / f"{slug}.jpg"

        if is_current(src, (display, full)):
            skipped.append(src.name)
            if entry is None:  # Outputs exist but the entry is gone: rebuild the entry.
                with Image.open(display) as d:
                    dw, dh = d.size
        else:
            with Image.open(src) as img:
                img = to_srgb(ImageOps.exif_transpose(img))
                d = fit(img, DISPLAY_EDGE)
                d.save(display, "WEBP", quality=82, method=6)
                f = fit(img, FULL_EDGE)
                f.save(full, "JPEG", quality=90, progressive=True, optimize=True)
                dw, dh = d.size
            built.append(src.name)

        if entry is None:
            entry = {
                "id": slug,
                "display": f"/gallery/images/display/{slug}.webp",
                "full": f"/gallery/images/full/{slug}.jpg",
                "width": dw,
                "height": dh,
                **{k: "" for k in TEXT_FIELDS},
                "source_name": src.name,
            }
            entries.append(entry)
            by_source[src.name] = entry
            new.append(slug)
        else:
            # Refresh only the generated fields. Never touch caption text.
            if src.name in built:
                entry["width"], entry["height"] = dw, dh

    present = {p.name for p in files}
    missing = [e["source_name"] for e in entries if e["source_name"] not in present]

    JSON_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Source folder:   {source}")
    print(f"Images found:    {len(files)}")
    print(f"New entries:     {len(new)}")
    print(f"Built:           {len(built)}")
    print(f"Skipped (current): {len(skipped)}")
    print(f"Ignored files:   {len(ignored)}" + (f" ({', '.join(ignored)})" if ignored else ""))
    print(f"Missing sources: {len(missing)}")
    for name in missing:
        print(f"  - {name}")
    print(f"Total entries:   {len(entries)}")
    print(f"display size:    {mb(folder_size(DISPLAY_DIR))}")
    print(f"full size:       {mb(folder_size(FULL_DIR))}")


if __name__ == "__main__":
    main()
