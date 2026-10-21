# Claude Code prompt — Add gallery batch 2026-10-21

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Source folder: `C:\Claude\Projects\Gallery\Images`
Batch file: `C:\Claude\Projects\Gallery\index-entries-2026-10-21.md`
Cumulative index: `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-gallery-add-2026-10-21.md`

Do not change any existing gallery entry. Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Read the procedure

1. Read `docs/ADD-GALLERY-IMAGES.md` in the repo. Follow it for all steps below.
2. Read `tools/gallery_config.json`.
3. Copy this prompt into the repo as `docs/prompts/CC-gallery-add-2026-10-21.md`.
4. If the procedure conflicts with this prompt, stop and report the conflict.

## Step 2 — Find the new images

1. List the image files in the source folder.
2. Compare the list with the `source_name` values in `gallery/gallery.json`.
3. Record each image that is not in the gallery and not in `exclude`.
4. The list must be exactly these six files: `NB-010.jpg`, `NB-011.jpg`, `NB-012.jpg`, `MJ-003.png`, `MJ-004.png`, `MJ-005.png`.
5. If the list is different, stop and report the list.

## Step 3 — Read the batch file

1. Read the batch file. It has six entries, numbered 117 to 122.
2. Confirm that the highest gallery number in `gallery/gallery.json` is 116. If it is not 116, stop and report it.
3. For each entry, use the title, description, alt text, and style line exactly as written. The descriptions are longer than 35 words. Adam approved them, so do not shorten them.
4. Only image 121 (Swivels of Bone and Faith) has a style line: `In the spirit of Ernie Barnes`. The other five have an empty style.

## Step 4 — Signature and mark checks

Do the checks that each batch entry lists in its **Checks** field:

1. `MJ-003.png` and `MJ-004.png`: retouch the signature scribble at the lower right. Confirm that no trace stays. Then check the other three corners.
2. `MJ-005.png`: check all four corners for a signature.
3. `NB-010.jpg`, `NB-011.jpg`, `NB-012.jpg`: check all four corners for a mark.
4. `NB-010.jpg`: confirm that the envelopes and the bunting show no readable text.
5. `NB-012.jpg`: confirm that the sky shows no constellation chart lines and no text.
6. If a retouch leaves a visible trace after 2 attempts, stop and report. Do not exclude the image.

## Step 5 — Size check

1. `NB-010.jpg` is 1200 x 896 pixels. This is smaller than the other images.
2. Build its web image with the normal procedure. Do not upscale it.
3. Report the web build size of each of the six images.

## Step 6 — Add to the gallery

1. Add the six images to the gallery with their captions, as numbers 117 to 122.
2. Back up the cumulative index to `C:\Claude\Projects\Gallery\backups\` before you change it.
3. Append the batch file to the cumulative index. Start at the line `# Prompt Index — 21 October 2026` and continue to the end of the file. Do not append the top section.
4. Never replace the cumulative index. Only append.

## Step 7 — Test and publish

1. Test the gallery page locally. Confirm that the six images and captions show.
2. Commit and push to `main`.
3. Wait for the Render deploy.
4. Check https://adamlozo.com/gallery/ for all six images and captions.
5. Move the batch file to `C:\Claude\Projects\Gallery\backups\processed\`.

## Step 8 — Update the prompt log

1. Open `C:\Claude\Projects\Gallery\prompt-log.md`.
2. In the entries for NB-010, NB-011, NB-012, MJ-003, MJ-004, and MJ-005, change `- **Status:** final` to `- **Status:** published`.
3. Add the extension to each `- **File:**` line. Example: `NB-010` (extension not recorded) becomes `NB-010.jpg`.
4. In the "Pending" section, change the line that starts with `- Batch 2026-10-21` to say that the batch is live, with the commit hash.
5. Do not change other text in the prompt log.

## Report back

- The list of new images from Step 2.
- The result of each check in Step 4, and each retouch done.
- The web build size of each image.
- Any image that you could not add, and why.
- Index entry count before and after.
- Local test result.
- Commit hash.
- Live page check result.
- The prompt-log changes from Step 8.
