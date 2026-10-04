"""Build gallery images and maintain gallery/gallery.json.

Usage:
    python tools/build_gallery.py ["<source folder>"] [--force <id>]

Reads:
    tools/gallery_config.json           ("exclude": source file names to drop,
                                         "crops": {id: {left, top, right, bottom}} as fractions to remove,
                                         "retouch": {id: [{left, top, right, bottom}, ...]} boxes to
                                         inpaint, as fractions of the source: left/top are the start,
                                         right/bottom are the end)

Writes:
    gallery/images/display/<slug>.webp  (long edge 1600 px, quality 82)
    gallery/images/full/<slug>.jpg      (long edge max 3000 px, quality 90, progressive)
    gallery/gallery.json                (caption text in existing entries is never changed)
    gallery/version.txt                 (short hash of gallery.json, for cache busting)

An excluded source loses its gallery.json entry and its outputs. This is the only case
where the script deletes an entry. An image is rebuilt when its source is newer than its
outputs, when its crop or retouch boxes in the config differ from the "crop" or "retouch"
stored in its entry, or when --force names its id. Retouch runs on the source pixels
(cv2.inpaint, Telea) before the crop and the resize. Source files are never changed.

Retouched copies: if <source folder>\..\Retouched\<source file name> exists (for example a
signature removed in Photoshop), the script reads its pixels instead of the source and
stores "retouched": true in the entry. Adding or removing a copy rebuilds the image.
"""

import argparse
import hashlib
import io
import json
import re
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageCms, ImageOps

DEFAULT_SOURCE = r"C:\Claude\Projects\Gallery\Images"
RETOUCHED_FOLDER = "Retouched"  # sibling of the source folder; same file names as the sources
EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}
DISPLAY_EDGE = 1600
FULL_EDGE = 3000
SLUG_MAX = 60

REPO = Path(__file__).resolve().parent.parent
GALLERY = REPO / "gallery"
DISPLAY_DIR = GALLERY / "images" / "display"
FULL_DIR = GALLERY / "images" / "full"
JSON_PATH = GALLERY / "gallery.json"
VERSION_PATH = GALLERY / "version.txt"
CONFIG_PATH = REPO / "tools" / "gallery_config.json"

SIDES = ("left", "top", "right", "bottom")
TEXT_FIELDS = ("title", "style", "description", "alt")
RETOUCH_PAD = 6     # px added on each side of a retouch box before inpainting
RETOUCH_RADIUS = 7  # cv2.inpaint neighbourhood radius in px

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


def load_config():
    if not CONFIG_PATH.exists():
        return set(), {}, {}
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return set(cfg.get("exclude", [])), cfg.get("crops", {}), cfg.get("retouch", {})


def norm_crop(crop):
    """Return the crop as {side: fraction} for all four sides, or None if it removes nothing."""
    if not crop:
        return None
    out = {s: round(float(crop.get(s, 0.0)), 4) for s in SIDES}
    for s, v in out.items():
        if not 0 <= v < 0.5:
            sys.exit(f"Crop value out of range: {s}={v}")
    return out if any(out.values()) else None


def apply_crop(img, crop):
    if not crop:
        return img
    w, h = img.size
    box = (
        round(w * crop["left"]),
        round(h * crop["top"]),
        w - round(w * crop["right"]),
        h - round(h * crop["bottom"]),
    )
    return img.crop(box)


def norm_retouch(boxes):
    """Return the retouch boxes as a list of {side: fraction}, or None if there are none."""
    if not boxes:
        return None
    out = []
    for b in boxes:
        box = {s: round(float(b[s]), 4) for s in SIDES}
        if not (0 <= box["left"] < box["right"] <= 1 and 0 <= box["top"] < box["bottom"] <= 1):
            sys.exit(f"Retouch box out of range: {box}")
        out.append(box)
    return out


def apply_retouch(img, boxes):
    """Inpaint the boxes (fractions of the image) with cv2.INPAINT_TELEA."""
    if not boxes:
        return img
    w, h = img.size
    mask = np.zeros((h, w), np.uint8)
    for b in boxes:
        x0 = max(0, round(w * b["left"]) - RETOUCH_PAD)
        y0 = max(0, round(h * b["top"]) - RETOUCH_PAD)
        x1 = min(w, round(w * b["right"]) + RETOUCH_PAD)
        y1 = min(h, round(h * b["bottom"]) + RETOUCH_PAD)
        mask[y0:y1, x0:x1] = 255
    bgr = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    out = cv2.inpaint(bgr, mask, RETOUCH_RADIUS, cv2.INPAINT_TELEA)
    return Image.fromarray(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))


def is_current(src, outputs):
    mtime = src.stat().st_mtime
    return all(p.exists() and p.stat().st_mtime > mtime for p in outputs)


def folder_size(path):
    return sum(f.stat().st_size for f in path.glob("*") if f.is_file())


def mb(n):
    return f"{n / 1_048_576:.1f} MB"


def main():
    parser = argparse.ArgumentParser(description="Build gallery images and gallery.json.")
    parser.add_argument("source", nargs="?", default=DEFAULT_SOURCE, help="source image folder")
    parser.add_argument("--force", metavar="ID", help="rebuild the image with this id")
    args = parser.parse_args()

    source = Path(args.source)
    if not source.is_dir():
        sys.exit(f"Source folder not found: {source}")
    retouched_dir = source.parent / RETOUCHED_FOLDER

    DISPLAY_DIR.mkdir(parents=True, exist_ok=True)
    FULL_DIR.mkdir(parents=True, exist_ok=True)

    excluded_names, crops, retouches = load_config()

    entries = json.loads(JSON_PATH.read_text(encoding="utf-8")) if JSON_PATH.exists() else []

    # Drop excluded images: the entry and its outputs.
    removed = []
    for e in [e for e in entries if e["source_name"] in excluded_names]:
        for p in (DISPLAY_DIR / f"{e['id']}.webp", FULL_DIR / f"{e['id']}.jpg"):
            p.unlink(missing_ok=True)
        entries.remove(e)
        removed.append(e["id"])

    by_source = {e["source_name"]: e for e in entries}
    used = {e["id"] for e in entries}
    if args.force and args.force not in used:
        sys.exit(f"--force: no entry with id {args.force}")

    files = sorted(
        (
            p
            for p in source.iterdir()
            if p.is_file() and p.suffix.lower() in EXTENSIONS and p.name not in excluded_names
        ),
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
        crop = norm_crop(crops.get(slug))
        stored_crop = entry.get("crop") if entry else None
        retouch = norm_retouch(retouches.get(slug))
        stored_retouch = entry.get("retouch") if entry else None
        # A retouched copy (for example from Photoshop) replaces the source pixels.
        copy = retouched_dir / src.name
        pixels = copy if copy.is_file() else src
        is_copy = pixels is copy
        stored_copy = bool(entry.get("retouched")) if entry else False

        if (
            is_current(pixels, (display, full))
            and crop == stored_crop
            and retouch == stored_retouch
            and is_copy == stored_copy
            and slug != args.force
            and not (entry is None and (crop or retouch or is_copy))
        ):
            skipped.append(src.name)
            if entry is None:  # Outputs exist but the entry is gone: rebuild the entry.
                with Image.open(display) as d:
                    dw, dh = d.size
        else:
            with Image.open(pixels) as img:
                img = to_srgb(ImageOps.exif_transpose(img))
                img = apply_retouch(img, retouch)
                img = apply_crop(img, crop)
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
            if crop:
                entry["crop"] = crop
            if retouch:
                entry["retouch"] = retouch
            if is_copy:
                entry["retouched"] = True
            entries.append(entry)
            by_source[src.name] = entry
            new.append(slug)
        else:
            # Refresh only the generated fields. Never touch caption text.
            if src.name in built:
                entry["width"], entry["height"] = dw, dh
                if crop:
                    entry["crop"] = crop
                else:
                    entry.pop("crop", None)
                if retouch:
                    entry["retouch"] = retouch
                else:
                    entry.pop("retouch", None)
                if is_copy:
                    entry["retouched"] = True
                else:
                    entry.pop("retouched", None)

    present = {p.name for p in files}
    missing = [e["source_name"] for e in entries if e["source_name"] not in present]

    text = json.dumps(entries, indent=2, ensure_ascii=False) + "\n"
    JSON_PATH.write_text(text, encoding="utf-8")
    version = hashlib.sha256(text.encode("utf-8")).hexdigest()[:10]
    VERSION_PATH.write_text(version + "\n", encoding="utf-8")

    print(f"Source folder:   {source}")
    print(f"Images found:    {len(files)}")
    print(f"New entries:     {len(new)}")
    print(f"Built:           {len(built)}")
    print(f"Skipped (current): {len(skipped)}")
    print(f"Excluded:        {len(excluded_names)} in config, {len(removed)} entries removed now")
    for slug in removed:
        print(f"  - {slug}")
    print(f"Ignored files:   {len(ignored)}" + (f" ({', '.join(ignored)})" if ignored else ""))
    print(f"Missing sources: {len(missing)}")
    for name in missing:
        print(f"  - {name}")
    print(f"Total entries:   {len(entries)}")
    print(f"Version:         {version}")
    print(f"display size:    {mb(folder_size(DISPLAY_DIR))}")
    print(f"full size:       {mb(folder_size(FULL_DIR))}")


if __name__ == "__main__":
    main()
