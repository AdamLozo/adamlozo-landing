# Claude Code prompt — Add gallery batch 2026-10-19

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Source folder: `C:\Claude\Projects\Gallery\Images`
Batch file: `C:\Claude\Projects\Gallery\index-entries-2026-10-19.md`
Cumulative index: `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index.md`

This prompt is saved in the repo as `docs/prompts/CC-gallery-add-2026-10-19.md`.

## Step 1 — Read the procedure

1. Read `docs/ADD-GALLERY-IMAGES.md`. Follow it for all steps below.
2. Read `tools/gallery_config.json`.
3. If the procedure conflicts with this prompt, stop and report the conflict.

## Step 2 — Update the procedure document

Adam approved three rule changes in the 2026-10-18 batch. They are not in `docs/ADD-GALLERY-IMAGES.md` yet. Make these three changes, and do not change other text:

1. In "3. Write the captions", change the `description` rule to: `description`: 1 to 2 sentences, 35 words maximum. When Adam approves longer text in the batch file, use that text as written.
2. In "3. Write the captions", change the `style` rule to: `style`: `After <Artist Name>` or `In the spirit of <Artist Name>`, only when the prompt names an artist. Otherwise, use an empty string.
3. In "4. Signatures, logos, and mastheads", the image must not be excluded when a retouch fails. Change these two sentences:
   - "If the retouch leaves a visible trace, exclude the image." becomes "If the retouch leaves a visible trace, stop and report. Do not exclude the image."
   - "If the retouch does not pass after 2 attempts, exclude the image." becomes "If the retouch does not pass after 2 attempts, stop and report. Do not exclude the image."

Show the diff of the document in the report.

## Step 3 — Find the new images

1. List the image files in the source folder.
2. Compare the list with the `source_name` values in `gallery/gallery.json`.
3. Record each image that is not in the gallery and not in `exclude`.
4. The result must be the 10 files in the "Source files" table at the end of the batch file.
5. If the count or the file names are different, stop and report.

## Step 4 — Merge the prompts into the cumulative index

1. Copy the cumulative index to `C:\Claude\Projects\Gallery\backups\` with the date in the file name.
2. Count the `### ` entries in the cumulative index. The count must be 106. If it is different, stop and report.
3. In the batch file, find the line `# Prompt Index — 19 October 2026`.
4. Append that line and all text after it to the end of the cumulative index. Do not append the text above that line.
5. Do not change or remove the existing entries.
6. Count the entries again. The new count must be 116. If not, stop and restore the backup.

## Step 5 — Build the web images

1. Run `python tools/build_gallery.py`.
2. Make sure that the script made 10 new entries in `gallery/gallery.json`.
3. Record the `id` of the new entry for `MJ-002.png`. You need it in Step 7.

## Step 6 — Examine each new image

Make a 512 px preview of each new image. Do the check in the "Checks" line of each batch entry. These checks are the most important:

1. **Made of Stardust:** look at the lower-right corner. A gold lotus emblem was replaced there. Make sure that no trace stays.
2. **Warm Tubes, Loud Night:** look at the amplifier and the guitar for a real brand logo.
3. **Painted Into Being:** look at the wall graffiti for readable words.

For all 10 images, obey these rules:

- A signature, stamp, or handle: remove it with a retouch. Examine the result.
- If a trace stays after the retouch, stop and report. Do not exclude the image.
- A real logo or a real masthead: stop and report. Do not exclude the image.
- Scribbles or generic fake lettering: keep the image.
- A small Gemini sparkle mark in a corner is a provenance label, not an artist signature or a logo. Keep it. Do not retouch it, and do not exclude the image. Record it in the report.

Delete the previews when you finish.

## Step 7 — Crop the canvas edge of The Lantern Leaves

`MJ-002.png` has a thin dark canvas edge at the top and at the left. Adam approved a crop of this edge only. This is the only crop in this batch.

1. Measure the width of the dark edge on each side of the source image, in pixels.
2. Convert each width to a fraction of the image width or height. Add a small margin of 0.002.
3. Add a `crops` entry for the `id` from Step 5 in `tools/gallery_config.json`. Include only the sides that have a dark edge.
4. Run `python tools/build_gallery.py --force <id>`.
5. Make a 512 px preview. Make sure that no dark edge stays and that no part of the painting is lost except the edge.
6. If an edge is wider than 2 percent of the image, stop and report. Do not crop.

## Step 8 — Write the captions

1. Use the batch file text exactly. Copy each title, description, and alt text from its batch entry. The title is the `### ` heading without the number. The description is the paragraph after the "Alt" line.
2. The batch descriptions are longer than 35 words. Adam approved this length. Do not shorten them.
3. The description of **Karen on Christmas Eve** ends with the dedication "In loving memory of Karen." Keep it exactly.
4. `style` is an empty string for 9 images.
5. `style` for **The Simple Beauty** is `In the spirit of Gustav Klimt`. Adam approved this wording.
6. Do not use the words "AI", "Midjourney", "Nano Banana", or "Gemini" in a caption.

## Step 9 — Test locally

1. Do the local test in `docs/ADD-GALLERY-IMAGES.md`.
2. Make sure that each new image shows, has its caption, and opens at full size.
3. Make sure that the existing images did not change.
4. If a test fails, stop and report. Do not push.

## Step 10 — Push and check the live page

1. Commit with the message `Gallery: add batch 2026-10-19`. Include `docs/ADD-GALLERY-IMAGES.md` and this prompt file.
2. Push to `main`.
3. Wait for the Render deploy to complete.
4. Open https://adamlozo.com/gallery/. Make sure that the new images show.

## Step 11 — Move the batch file

1. Move `index-entries-2026-10-19.md` to `C:\Claude\Projects\Gallery\backups\processed\`.
2. Do this step only after the live check passes.

## Step 12 — Report

Give a report with:

1. The number of new images added. It must be 10.
2. A table: file name, `id`, title.
3. Images retouched, with the retouch location.
4. Gemini marks found, with the image and the corner.
5. The crop values for The Lantern Leaves.
6. The diff of `docs/ADD-GALLERY-IMAGES.md`.
7. Any other change to `tools/gallery_config.json`.
8. The index entry count before and after.
9. The commit hash and the live check result.
10. Any problem or recommendation.

## Rules

- Do not crop any image except The Lantern Leaves in Step 7.
- Stop and report on any blocker or tool failure. Do not use a workaround.
- Do not change images or captions that are already in the gallery.
- Use targeted reads. Do not read full large files when a search is sufficient.
