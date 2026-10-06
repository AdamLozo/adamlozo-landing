# Claude Code prompt — Add gallery batch 2026-10-06

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Source folder: `C:\Claude\Projects\Gallery`
Batch index file: `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index-2026-10-06.md`
Cumulative index file: `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index.md`

Save a copy of this prompt as `docs/prompts/CC-gallery-add-2026-10-06.md` in the repo.

## Step 1 — Read the procedure

1. Read `docs/ADD-GALLERY-IMAGES.md`. Follow it for all steps below.
2. Read `tools/gallery_config.json`.
3. If the procedure conflicts with this prompt, stop and report the conflict.

## Step 2 — Find the new images

1. List the image files in the source folder.
2. Compare the list with the images that the gallery already contains.
3. Record each image that is not in the gallery and not excluded in `tools/gallery_config.json`. These are the new images.
4. Read the "Not mine" list in the cumulative index and in the batch index. Do not add an image whose file name is on either list.
5. Match each new image to its prompt in the batch index file.
6. If a new image has no prompt, or a prompt has no image, stop. Report the file names.

## Step 3 — Merge the prompts into the cumulative index

1. Add the entries from the batch index to the end of `Midjourney-Prompt-Index.md`.
2. Do not add an entry that is already in the cumulative index.
3. Do not change or remove the existing entries.
4. If the batch file has "Not mine" names, add them to the "Not mine" list in the cumulative index.
5. Do not change, move, or delete the batch index file.

## Step 4 — Examine each new image

### Exception: the Starship image

1. Find the new image with "Starship" in its file name or in its prompt.
2. If you find zero matches or more than one match, stop and report.
3. This image has illegible text in many areas. Adam approved this text.
4. Do not retouch, crop, or change this image.
5. Do not remove marks that look like a signature.
6. If you see a real logo or a real masthead, do not exclude the image. Stop and report.

### All other new images

Look at each new image. For each image, do these checks:

1. Real artist signature: remove it with a retouch. Do not crop. Examine the result. If a trace stays visible, exclude the image.
2. Real logo or real masthead: exclude the image.
3. Scribbles or generic fake lettering: keep the image.
4. Record each exclusion and its reason in `tools/gallery_config.json`.

## Step 5 — Write the captions

1. Title: 2 to 5 words.
2. Use "After <Artist>" only when the prompt names an artist.
3. Description: 1 or 2 sentences, max 35 words.
4. Base each caption on the image and its prompt.

## Step 6 — Test locally

1. Build the gallery with the procedure in `docs/ADD-GALLERY-IMAGES.md`.
2. Serve the site locally and open `/gallery/`.
3. Make sure each new image shows, has its caption, and opens at full size.
4. Make sure the existing images did not change.
5. If a test fails, stop and report. Do not push.

## Step 7 — Push and check the live page

1. Commit with the message `Gallery: add batch 2026-10-06`.
2. Push to `main`.
3. Wait for the Render deploy to complete.
4. Open https://adamlozo.com/gallery/. Make sure the new images show.

## Step 8 — Report

Give a report with:

1. The number of new images added.
2. A table: file name, title, description.
3. Images retouched, with the retouch location.
4. Images excluded, with the reason.
5. The commit hash and the live check result.
6. Any problem or recommendation.

## Rules

- Never crop an image. Do not add crop entries to `tools/gallery_config.json`. If the build crops images by default, stop and report.
- Stop and report on any blocker or tool failure. Do not use a workaround.
- Do not change images that are already in the gallery.
- Use targeted reads. Do not read full large files when a search is sufficient.
