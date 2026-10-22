"""Build one person of a gallery series: web images, the people.json entry, and the person page.
Never reads or writes gallery/gallery.json or series.json.

Usage:
    py tools/build_people.py <series slug> "<person folder>" --seen-in <nn> [<nn> ...] [--page-dir kindred] [--force]

Example:
    py tools/build_people.py ancestors "C:\\Claude\\Projects\\Gallery\\Series\\Ancestors\\people\\storyteller" --seen-in 01 05

The person folder holds the six facet images <prefix>-01-<Facet>.jpg to <prefix>-06-<Facet>.jpg
(the -00-Sheet image is a working reference and is never published) and one *-log.md file.
The log is the only source of text. The script reads, exactly as written:
    ## P<n> <Name> — ...                                  person heading
    - **Home card text:** <Name> · <Group> · <Summary>
    ### Page introduction ...                             the next paragraph is the intro
    | 01 | Portrait | `<file>` | ANC-31 |                 one table row per facet
    #### 01. Portrait                                     one section per facet, with
    - **Paragraph 1 (the story):** ...
    - **Paragraph 2 (the evidence):** ...
    - **Alt:** ...

Writes:
    gallery/series/<slug>/people/<folder name>/images/display/<id>.webp  (same rules as build_series.py)
    gallery/series/<slug>/people/<folder name>/images/full/<id>.jpg
    gallery/series/<slug>/people.json     entry replaced by slug, or appended in build order
    <page dir>/<person slug>/index.html   from tools/templates/person.html

The person page copies the <style> block of <page dir>/index.html, so both pages share one set of
styles. Run this script again for each person after a style change on <page dir>/index.html.

Last, it stamps a short content hash of people.json and series.json into <page dir>/index.html and
every person page, as people.json?v=<hash> (see stamp_versions in build_series.py). The person
pages build their previous and next links from people.json, so a new person needs no page rebuild.
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_gallery import GALLERY, REPO  # noqa: E402
from build_series import build_image, stamp_versions  # noqa: E402

FACETS = ["Portrait", "Responsibility", "Challenge", "Joy", "Bond", "Legacy"]
TEMPLATE = Path(__file__).resolve().parent / "templates" / "person.html"


def fail(msg):
    sys.exit(f"ERROR: {msg}")


def one(pattern, text, what):
    found = re.findall(pattern, text, re.M)
    if len(found) != 1:
        fail(f"log: expected one {what}, found {len(found)}")
    return found[0]


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def parse_log(text):
    heading = one(r"^## P\d+ (.+?) — ", text, "person heading")
    card = one(r"^- \*\*Home card text:\*\* (.+)$", text, "home card text")
    parts = card.split(" · ")
    if len(parts) != 3:
        fail(f"log: home card text must be 'Name · Group · Summary': {card}")
    name, group, summary = (p.strip() for p in parts)
    if name != heading:
        fail(f"log: home card name '{name}' does not match heading '{heading}'")

    m = re.search(r"^### Page introduction.*\n+((?:(?!#).+\n?)+)", text, re.M)
    if not m:
        fail("log: no page introduction")
    intro_lines = [ln.strip() for ln in m.group(1).splitlines() if ln.strip()]
    if len(intro_lines) != 1:
        fail(f"log: the page introduction must be one paragraph, found {len(intro_lines)}")

    rows = {n: (facet.strip(), file, pid)
            for n, facet, file, pid in re.findall(r"^\| (\d\d) \| (.+?) \| `(.+?)` \| (ANC-\d+) \|$", text, re.M)}

    facets = []
    for i, facet_name in enumerate(FACETS, start=1):
        num = f"{i:02d}"
        sec = re.search(rf"^#### {num}\. (.+)\n((?:- .+\n?)+)", text, re.M)
        if not sec:
            fail(f"log: no section '#### {num}. {facet_name}'")
        if sec.group(1).strip() != facet_name:
            fail(f"log: section {num} is '{sec.group(1).strip()}', expected '{facet_name}'")
        body = sec.group(2)
        fields = {}
        for key, label in (("description_1", r"Paragraph 1 \(the story\)"),
                           ("description_2", r"Paragraph 2 \(the evidence\)"),
                           ("alt", r"Alt")):
            fm = re.findall(rf"^- \*\*{label}:\*\* (.+)$", body, re.M)
            if len(fm) != 1:
                fail(f"log: facet {num} needs one '{label}' line, found {len(fm)}")
            fields[key] = fm[0].strip()
        if num not in rows:
            fail(f"log: no table row for facet {num}")
        row_facet, file, pid = rows[num]
        if row_facet != facet_name:
            fail(f"log: table row {num} is '{row_facet}', expected '{facet_name}'")
        facets.append({"number": num, "facet": facet_name, **fields, "prompt_id": pid, "source_name": file})

    return {"name": name, "group": group, "summary": summary, "intro": intro_lines[0], "facets": facets}


def main():
    parser = argparse.ArgumentParser(description="Build one person of a gallery series.")
    parser.add_argument("slug", help="series slug, for example ancestors")
    parser.add_argument("folder", help="person folder with the facet images and the person log")
    parser.add_argument("--seen-in", nargs="+", required=True, help="series image numbers, for example 01 05")
    parser.add_argument("--page-dir", default="kindred", help="site folder of the series page")
    parser.add_argument("--force", action="store_true", help="rebuild all images")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        fail(f"person folder not found: {folder}")
    logs = list(folder.glob("*-log.md"))
    if len(logs) != 1:
        fail(f"expected one *-log.md in {folder}, found {len(logs)}")
    person = parse_log(logs[0].read_text(encoding="utf-8"))

    series_base = GALLERY / "series" / args.slug
    series = json.loads((series_base / "series.json").read_text(encoding="utf-8"))
    groups = {e["group"] for e in series["images"]}
    numbers = {e["number"] for e in series["images"]}
    if person["group"] not in groups:
        fail(f"group '{person['group']}' is not a group in series.json: {sorted(groups)}")
    for n in args.seen_in:
        if n not in numbers:
            fail(f"--seen-in {n} is not an image number in series.json")

    key = folder.name.lower()
    base = series_base / "people" / key / "images"
    display_dir, full_dir = base / "display", base / "full"
    display_dir.mkdir(parents=True, exist_ok=True)
    full_dir.mkdir(parents=True, exist_ok=True)
    web = f"/gallery/series/{args.slug}/people/{key}/images"

    for f in person["facets"]:
        src = folder / f["source_name"]
        if not src.is_file():
            fail(f"facet image not found: {src}")
        _, info = build_image(src, display_dir, full_dir, web, args.force)
        f.update({k: info[k] for k in ("display", "full", "width", "height")})

    slug = slugify(person["name"])
    entry = {
        "slug": slug,
        "name": person["name"],
        "group": person["group"],
        "summary": person["summary"],
        "intro": person["intro"],
        "seen_in": args.seen_in,
        "facets": person["facets"],
    }

    json_path = series_base / "people.json"
    data = json.loads(json_path.read_text(encoding="utf-8")) if json_path.exists() else {"people": []}
    people = data["people"]
    idx = next((i for i, p in enumerate(people) if p["slug"] == slug), None)
    if idx is None:
        people.append(entry)
    else:
        people[idx] = entry
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"people.json: {slug} {'appended' if idx is None else 'replaced'}, {len(people)} people")

    series_page = (REPO / args.page_dir / "index.html").read_text(encoding="utf-8")
    style = re.search(r"<style>.*?</style>", series_page, re.S)
    if not style:
        fail(f"no <style> block in {args.page_dir}/index.html")
    page = TEMPLATE.read_text(encoding="utf-8")
    values = {
        "STYLE": style.group(0),
        "NAME": html.escape(person["name"]),
        "SUMMARY": html.escape(person["summary"]),
        "SLUG": slug,
        "SERIES": args.slug,
        "PAGE": args.page_dir,
    }
    for k, v in values.items():
        page = page.replace("{{" + k + "}}", v)
    left = re.findall(r"\{\{[A-Z]+\}\}", page)
    if left:
        fail(f"template placeholders not filled: {left}")
    out = REPO / args.page_dir / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8", newline="\n")
    print(f"page: /{args.page_dir}/{slug}/")
    stamp_versions(args.slug, args.page_dir)


if __name__ == "__main__":
    main()
