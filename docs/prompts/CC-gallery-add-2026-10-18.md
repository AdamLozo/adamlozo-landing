# Claude Code prompt — Add gallery batch 2026-10-18

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Source folder: `C:\Claude\Projects\Gallery\Images`
Batch file: `C:\Claude\Projects\Gallery\index-entries-2026-10-17.md`
Cumulative index: `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index.md`

This prompt is saved in the repo as `docs/prompts/CC-gallery-add-2026-10-18.md`.

## Step 1 — Read the procedure

1. Read `docs/ADD-GALLERY-IMAGES.md`. Follow it for all steps below.
2. Read `tools/gallery_config.json`.
3. If the procedure conflicts with this prompt, stop and report the conflict.

## Step 2 — Find the new images

1. List the image files in the source folder.
2. Compare the list with the `source_name` values in `gallery/gallery.json`.
3. Record each image that is not in the gallery and not in `exclude`.
4. The result must be the 10 files in the "Source files" list in the Notes of the batch file.
5. Three older files (from 9 October and 1 October) are already in `exclude`. Do not change them.
6. If the count or the file names are different, stop and report.

## Step 3 — Merge the prompts into the cumulative index

1. Copy the cumulative index to `C:\Claude\Projects\Gallery\backups\` with the date in the file name.
2. Count the `### ` entries in the cumulative index. Record the count.
3. Add the 10 gallery entries from the batch file to the end of the cumulative index. Use the same format as the earlier entries.
4. Do not add an entry that is already in the index.
5. Do not change or remove the existing entries.
6. Count the entries again. The new count must be the old count plus 10. If not, stop and restore the backup.

## Step 4 — Build the web images

1. Run `python tools/build_gallery.py`.
2. Make sure that the script made 10 new entries in `gallery/gallery.json`.
3. If the script crops an image, stop and report.

## Step 5 — Examine each new image

Make a 512 px preview of each new image. Do the checks in the "Checks" line of each batch entry. These checks are the most important:

1. **Concord, Late October:** a faint signature is at the bottom centre. Remove it with a retouch box. Do not crop.
2. **The Endless Hall:** look beside the base of the right-hand column. A stamp was removed there. Make sure that no trace stays.
3. **Rain on Beacon Hill:** look at the lower-left corner for a red seal stamp, and at the small shop sign for garbled letters.
4. **Unravelling:** look in all corners for a signature or a social-media handle.
5. **Every Prayer:** look at the upper left for a logo badge.

For all 10 images, obey these rules:

- A signature, stamp or handle: remove it with a retouch box. Examine the result.
- If a trace stays after the retouch, stop and report. Do not exclude the image.
- A real logo or a real masthead: stop and report. Do not exclude the image.
- Scribbles or generic fake lettering: keep the image.

Delete the previews when you finish.

## Step 6 — Write the captions

1. Use the batch file text exactly. Copy each title, description and alt text from its batch entry.
2. The batch descriptions are longer than 35 words. Adam approved this length. Do not shorten them.
3. `style` is an empty string for 9 images.
4. `style` for **The Endless Hall** is `In the spirit of M.C. Escher`. Adam approved this wording.
5. Do not use the words "AI" or "Midjourney" in a caption.

The alt text for each image is in the "Alt" text that follows. Use it in the `alt` field:

| Title | Alt |
|---|---|
| Every Prayer | Mixed-media painting of a woman in a long crimson coat beside a small stone chapel on a stormy hill, with a lightning bolt and a flock of black birds. |
| Blocks of Christmas Light | Mixed-media painting of a smiling dark-haired woman in a red sweater in a white armchair, beside a Christmas tree made of blue and gold blocks. |
| The Last Gold Light | Palette-knife impasto painting of a woman in a hat and grey coat in golden dune grass, facing a grey sea under a small yellow sun and a flock of birds. |
| Be It Done unto Me | Silver-white and crimson painting of a winged angel with lilies above a kneeling woman in a red gown and white veil, with a white dove in the upper right. |
| Concord, Late October | Photorealistic close-up of a woman with silver hair and dry leaves in it, wearing a grey knit sweater and silver rings, holding a cluster of dark blue grapes to her face. |
| Unbreathed | Dark fantasy painting of a woman's upturned face with closed eyes, framed by teal and violet ribbon-like hair with gold edges and purple coral. |
| Slow Descents | Fashion photograph of a red-haired woman in profile in a midnight-blue velvet blazer, eyes closed, with glossy dark blue liquid spheres dripping beside her. |
| Rain on Beacon Hill | Illustrated cityscape of colourful stacked Boston rowhouses on a hill, with shopfronts and street lamps below and a gold dome at the top, under a pale misty sky. |
| Unravelling | Sketchy pencil-and-crayon illustration of a tabby kitten walking on its hind legs with a pink yarn ball, a trailing pink strand, a white butterfly above and coral flowers at the sides, on a blurred city street. |
| The Endless Hall | Black-and-white op-art illustration of an ornate arched hall with a checkerboard floor, a central staircase, a seated figure seen from behind and a flock of birds rising from a patterned wall. |

## Step 7 — Test locally

1. Do the local test in `docs/ADD-GALLERY-IMAGES.md`.
2. Make sure that each new image shows, has its caption, and opens at full size.
3. Make sure that the existing images did not change.
4. If a test fails, stop and report. Do not push.

## Step 8 — Push and check the live page

1. Commit with the message `Gallery: add batch 2026-10-18`.
2. Push to `main`.
3. Wait for the Render deploy to complete.
4. Open https://adamlozo.com/gallery/. Make sure that the new images show.

## Step 9 — Move the batch file

1. Move `index-entries-2026-10-17.md` to `C:\Claude\Projects\Gallery\backups\processed\`.
2. Do this step only after the live check passes.

## Step 10 — Report

Give a report with:

1. The number of new images added. It must be 10.
2. A table: file name, title.
3. Images retouched, with the retouch location.
4. Any change to `tools/gallery_config.json`.
5. The index entry count before and after.
6. The commit hash and the live check result.
7. Any problem or recommendation.

## Rules

- Never crop an image. Do not add crop entries to `tools/gallery_config.json`.
- Stop and report on any blocker or tool failure. Do not use a workaround.
- Do not change images or captions that are already in the gallery.
- Use targeted reads. Do not read full large files when a search is sufficient.
