# Claude Code prompt — Kindred series page (Ancestors)

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Series folder: `C:\Claude\Projects\Gallery\Series\Ancestors\`
Series log (captions and prompts): `C:\Claude\Projects\Gallery\Series\Ancestors\ancestors-prompt-log.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-kindred-series-page-2026-10-21.md`

Goal: publish the nine Ancestors images as their own page at `adamlozo.com/gallery/ancestors/`, titled "Kindred". The main gallery gets one card that links to the page. The series images do not go into the main gallery grid.

Rules:
- Do not change any existing main gallery entry, image, or caption.
- Do not add the series images to `gallery/gallery.json`.
- Do not change `Midjourney-Prompt-Index.md` or `prompt-log.md`.
- Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Read

1. Read `docs/ADD-GALLERY-IMAGES.md` and `tools/gallery_config.json` in the repo.
2. Read the files that build and show the main gallery page (the HTML, CSS, JS, and the web-image build tool). Find how the main gallery makes display and full images, and how the lightbox shows the title, style, and description.
3. Read the series log. Use the section "Series order and captions" as the only source for titles, descriptions, alt text, the introduction, and the style line.
4. Adam approved all captions, the introduction, and the style line on 2026-10-21. Each image has a description in two paragraphs: paragraph 1 (the story) and paragraph 2 (the evidence). Use the text exactly as written.

## Step 2 — Organize the source images

1. The nine images are in the series folder: `Ancestors-01-Africa-The-Hearth.jpg` to `Ancestors-09-IceAge-Endurance.jpg`.
2. Create the folder `C:\Claude\Projects\Gallery\Series\Ancestors\images\`.
3. Move the nine images into that folder. Do not rename them.
4. Confirm that exactly nine `.jpg` files are in `images\`. If the count is different, stop and report.

## Step 3 — Check the images

1. Check all four corners of each image for a signature, a logo, or a model mark.
2. Do not retouch any image in this run. If you find a mark, stop and report the image and the corner.

## Step 4 — Build the web images

1. Build display and full web images for the nine images with the same tool and the same size rules as the main gallery.
2. Put them in `gallery/series/ancestors/images/display/` and `gallery/series/ancestors/images/full/`.
3. Images 01, 02, and 09 are very wide (about 21:9). Do not crop any image.
4. Report the display and full size of each image.

## Step 5 — Create the series data file

1. Create `gallery/series/ancestors/series.json`.
2. Include the series title "Kindred", the introduction, and the style line `In the spirit of Joseph Wright of Derby`.
3. Include nine entries in the order 01 to 09. Each entry has: number, title, group (`Africa` or `Ice Age Europe`), description paragraph 1, description paragraph 2, alt text, prompt ID (the "Final ID" column), source file name, and the display and full image paths.

## Step 6 — Create the series page

1. Create the page so that it serves at `/gallery/ancestors/`. Use the same site header, footer, fonts, and styles as the main gallery.
2. At the top: the title "Kindred", the introduction, and the style line.
3. Show the nine images in series order, 01 to 09. Do not sort by date.
4. Under each image, show the number, the title, the group, and both description paragraphs. Show paragraph 2 in a slightly smaller or lighter style, so the story reads first and the evidence second.
5. Use the same lightbox as the main gallery. The lightbox shows the title, the group, and both description paragraphs. The lightbox arrows move in series order.
6. Add a link back to the main gallery.
7. The page must work at phone width with no horizontal scroll.

## Step 7 — Add the series card to the main gallery

1. On the main gallery page, add one card for the series, above the main grid.
2. The card shows the display image of 01 The Hearth, the title "Kindred", the text "A series in nine images", and a link to `/gallery/ancestors/`.
3. Do not change the main grid, its count, or its order.

## Step 8 — Test, publish, and record

1. Test locally. Confirm that the series page shows all nine images in order, with correct captions, and that the lightbox works.
2. Confirm that the main gallery shows the series card, and that the main grid is unchanged (same entry count as before).
3. Confirm that the series page works at a phone width of 390 px.
4. Copy this prompt into the repo as `docs/prompts/CC-kindred-series-page-2026-10-21.md`.
5. Commit and push to `main`.
6. Wait for the Render deploy. Check `https://adamlozo.com/gallery/ancestors/` and the series card on `https://adamlozo.com/gallery/`.
7. In the series log, change each `- **Status:** final` to `- **Status:** published`. Add one line under "Page:" at the top with the commit hash. Change no other text.

## Report back

- The files that build the main gallery, and how you reused them.
- The nine files moved into `images\`.
- The result of the corner checks.
- The display and full size of each image.
- The new files and the changed files in the repo.
- Main gallery entry count before and after (it must be the same).
- Local test result, including the phone-width check.
- Commit hash.
- Live check result for both pages.
- The changes in the series log.
