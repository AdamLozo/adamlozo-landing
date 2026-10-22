# Claude Code prompt — Kindred person pages (first person: the Storyteller)

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Person folder: `C:\Claude\Projects\Gallery\Series\Ancestors\people\storyteller\`
Person log (captions and alt text): `C:\Claude\Projects\Gallery\Series\Ancestors\people\storyteller\storyteller-log.md`
Series log: `C:\Claude\Projects\Gallery\Series\Ancestors\ancestors-prompt-log.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-kindred-people-pages-2026-10-22.md`

Goal: build the structure for Kindred person pages, and publish the first person, the Storyteller. Each person has six images (facets) in a fixed order. Later people will be added with new data and images only, with no new page code.

Rules:
- Do not change `gallery/gallery.json`, the main gallery, `Midjourney-Prompt-Index.md`, or `prompt-log.md`.
- Do not change the nine series images or `gallery/series/ancestors/series.json`.
- Do not publish the character sheet (`...-00-Sheet.jpg`). It is a working reference only.
- Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Read

1. Read `kindred/index.html`, `tools/build_series.py`, and `gallery/series/ancestors/series.json`.
2. Read the person log. Use it as the only source for the page introduction, the home card text, the six facet titles, both caption paragraphs, and the alt text. Use the text exactly as written.
3. Confirm that the person folder holds the six facet images `Ancestors-P1-Storyteller-01-Portrait.jpg` to `Ancestors-P1-Storyteller-06-Legacy.jpg`. If one is missing, stop and report.

## Step 2 — Check the images

1. Check all four corners of the six facet images for a signature, a logo, or a model mark.
2. Image 05 Bond may have a faint mark at the lower right. Look at it closely.
3. Do not retouch any image. If you find a mark, stop and report the image and the corner.

## Step 3 — Build the web images

1. Extend `tools/build_series.py`, or add a small `tools/build_people.py` that imports from it. Use the same size and quality rules as the series images.
2. Put the web images in `gallery/series/ancestors/people/storyteller/images/display/` and `.../full/`.
3. Do not crop any image. Report the display and full size of each image.

## Step 4 — Create the people data file

1. Create `gallery/series/ancestors/people.json`.
2. It holds a list of people. The first and only entry for now is the Storyteller, with:
   - `slug`: `the-storyteller`
   - `name`: `The Storyteller`
   - `group`: `Africa`
   - `summary`: the home card text line from the log ("The elder who holds the band's memory.")
   - `intro`: the page introduction
   - `seen_in`: the series numbers `["01", "05"]`
   - `facets`: six entries in order, each with number, facet name, paragraph 1, paragraph 2, alt text, prompt ID, source file name, and the display and full image paths.
3. Generate this file with a script that reads the person log, so the text is exact. Do not type the captions by hand.

## Step 5 — Create the person page

1. Create one page template that reads `people.json` and serves at `/kindred/<slug>/`. For now, create `kindred/the-storyteller/index.html`.
2. Use the same header, footer, fonts, styles, and lightbox as `kindred/index.html`.
3. At the top: the name, the group, and the introduction.
4. Show the six facets in order. Under each image: the facet name, paragraph 1, and paragraph 2 (in the same lighter style as on the series page).
5. The lightbox shows the facet name and both paragraphs, and its arrows move in facet order.
6. Under the six facets, add "Seen in the series:" with links to the series images 01 The Hearth and 05 Care on `/kindred/`. If the series page has no anchors for single images, add them.
7. Add a link back to `/kindred/`.
8. The page must work at phone width with no horizontal scroll.

## Step 6 — Add "The People" to the Kindred page

1. On `kindred/index.html`, add a section "The People" under the nine series images.
2. The section reads `people.json` and shows one card per person, grouped by group (Africa, Ice Age Europe).
3. Each card shows the display image of the person's 01 Portrait, the name, the summary line, and a link to `/kindred/<slug>/`.
4. Do not change the nine series images or their captions.

## Step 7 — Test, publish, and record

1. Test locally:
   - `/kindred/the-storyteller/` shows six facets in order, with correct captions and alt text, and a working lightbox.
   - `/kindred/` shows "The People" with the Storyteller card under an "Africa" heading, and the nine series images are unchanged.
   - The "Seen in the series" links open the correct series images.
   - Both pages have no horizontal scroll at 390 px.
   - The main gallery still has 180 entries.
2. Copy this prompt into the repo as `docs/prompts/CC-kindred-people-pages-2026-10-22.md`.
3. Commit and push to `main`.
4. Wait for the Render deploy. Do the same checks on the live site.
5. In the person log, change `- **Status:** all six facets final (approved 2026-10-22). Page not built yet.` to `- **Status:** published at adamlozo.com/kindred/the-storyteller/, commit <hash>, 2026-10-22.` Change no other text.
6. In the series log, change `all six facets approved 2026-10-22; page not built yet)` to `published 2026-10-22, commit <hash>)`. Change no other text.

## Report back

- How you built the people data and the page template, and what a later person needs (files and data only).
- The result of the corner checks.
- The display and full size of each image.
- The new and changed files.
- Main gallery entry count before and after (it must be 180).
- Local test results.
- Commit hash.
- Live check results.
- The changes in the two logs.
