"""Build web images for a gallery series. Never reads or writes gallery/gallery.json.

Usage:
    py tools/build_series.py <series slug> "<source folder>" [--page-dir kindred] [--force]

Example:
    py tools/build_series.py ancestors "C:\\Claude\\Projects\\Gallery\\Series\\Ancestors\\images"

Writes:
    gallery/series/<slug>/images/display/<id>.webp  (long edge 1600 px, quality 82)
    gallery/series/<slug>/images/full/<id>.jpg      (long edge max 3000 px, quality 90, progressive)

Uses the same colour conversion and size rules as tools/build_gallery.py (to_srgb, fit).
No crop and no retouch. The id is the lower-case source file stem.

If gallery/series/<slug>/series.json exists, the script refreshes only the generated fields
("display", "full", "width", "height") of each entry whose "source_name" matches a source file.
It never changes caption text and never adds or removes entries.

After it writes series.json, it stamps a short content hash of series.json and people.json into
every page that loads them (<page dir>/index.html and <page dir>/*/index.html), as
series.json?v=<hash> and people.json?v=<hash>. A new hash is a new edge-cache key, so a page
never gets an old data file from the cache after a deploy.
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_gallery import DISPLAY_EDGE, EXTENSIONS, FULL_EDGE, GALLERY, REPO, fit, is_current, to_srgb  # noqa: E402

DATA_FILES = ("series.json", "people.json")


def data_version(path):
    """Short content hash of one data file, used as its ?v= query. CRLF counts as LF, so a
    checkout with core.autocrlf gives the same hash as the committed file."""
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()[:8]


def stamp_versions(slug, page_dir):
    """Write the current ?v=<hash> of each data file into every page that loads it."""
    base = GALLERY / "series" / slug
    versions = {n: data_version(base / n) for n in DATA_FILES if (base / n).exists()}
    root = REPO / page_dir
    pages = [root / "index.html"] + sorted(root.glob("*/index.html"))
    for page in pages:
        if not page.is_file():
            continue
        text = page.read_text(encoding="utf-8")
        new = text
        for name, v in versions.items():
            url = re.escape(f"/gallery/series/{slug}/{name}")
            new = re.sub(rf"({url})(?:\?v=[0-9a-f]*)?(?=['\"])", rf"\g<1>?v={v}", new)
        if new != text:
            page.write_text(new, encoding="utf-8", newline="\n")
            print(f"stamped  /{page.relative_to(REPO).as_posix()}")
    print("versions: " + ", ".join(f"{n}?v={v}" for n, v in versions.items()))


def build_image(src, display_dir, full_dir, web, force=False):
    """Write the display WebP and full JPEG for one source image. Return (state, info)."""
    sid = src.stem.lower()
    display = display_dir / f"{sid}.webp"
    full = full_dir / f"{sid}.jpg"
    if not force and is_current(src, (display, full)):
        state = "current"
    else:
        with Image.open(src) as img:
            img = to_srgb(ImageOps.exif_transpose(img))
            fit(img, DISPLAY_EDGE).save(display, "WEBP", quality=82, method=6)
            fit(img, FULL_EDGE).save(full, "JPEG", quality=90, progressive=True, optimize=True)
        state = "built"
    with Image.open(display) as d, Image.open(full) as f:
        info = {
            "display": f"{web}/display/{sid}.webp",
            "full": f"{web}/full/{sid}.jpg",
            "width": d.width,
            "height": d.height,
            "full_size": f.size,
        }
    dw, dh = info["width"], info["height"]
    fw, fh = info["full_size"]
    print(f"{state:8} {src.name}  display {dw}x{dh}  full {fw}x{fh}")
    return state, info


def main():
    parser = argparse.ArgumentParser(description="Build web images for a gallery series.")
    parser.add_argument("slug", help="series slug, for example ancestors")
    parser.add_argument("source", help="source image folder")
    parser.add_argument("--page-dir", default="kindred", help="site folder of the series page")
    parser.add_argument("--force", action="store_true", help="rebuild all images")
    args = parser.parse_args()

    source = Path(args.source)
    if not source.is_dir():
        sys.exit(f"Source folder not found: {source}")

    base = GALLERY / "series" / args.slug
    display_dir = base / "images" / "display"
    full_dir = base / "images" / "full"
    display_dir.mkdir(parents=True, exist_ok=True)
    full_dir.mkdir(parents=True, exist_ok=True)
    web = f"/gallery/series/{args.slug}/images"

    files = sorted(
        (p for p in source.iterdir() if p.is_file() and p.suffix.lower() in EXTENSIONS),
        key=lambda p: p.name.lower(),
    )
    if not files:
        sys.exit(f"No images in {source}")

    info = {}
    for src in files:
        _, info[src.name] = build_image(src, display_dir, full_dir, web, args.force)

    json_path = base / "series.json"
    if json_path.exists():
        data = json.loads(json_path.read_text(encoding="utf-8"))
        updated = 0
        for e in data.get("images", []):
            i = info.get(e.get("source_name"))
            if i:
                e.update({k: i[k] for k in ("display", "full", "width", "height")})
                updated += 1
        json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        print(f"series.json: {updated} of {len(data.get('images', []))} entries refreshed")
        stamp_versions(args.slug, args.page_dir)
    print(f"Images: {len(files)}")


if __name__ == "__main__":
    main()
