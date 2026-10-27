# Claude Code prompt — Add gallery batch 2026-10-26

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Source folder: `C:\Claude\Projects\Gallery\Images`
Batch file: `C:\Claude\Projects\Gallery\index-entries-2026-10-26.md`
Cumulative index: `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-gallery-add-2026-10-26.md`

Do not change any existing gallery entry. Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Read the procedure

1. Read `docs/ADD-GALLERY-IMAGES.md` in the repo. Follow it for all steps below.
2. Read `tools/gallery_config.json`.
3. Copy this prompt into the repo as `docs/prompts/CC-gallery-add-2026-10-26.md`.
4. If the procedure conflicts with this prompt, stop and report the conflict.

## Step 2 — Check the gallery count and numbering

Adam reports that the live gallery shows 195 images before this batch. The cumulative index ends at gallery number 137. Check this before you change anything.

1. In `gallery/gallery.json`, count the entries.
2. Find the highest gallery number.
3. Count the entries in the cumulative index (`### <number>.` headings).
4. Report the three values.
5. If the highest gallery number is 137, continue. The batch uses numbers 138 to 158.
6. If the highest gallery number is not 137, stop. Report the count, the highest number, and how the numbers and the 195 count relate (for example, entries without a number, or a different numbering). Do not renumber anything.

## Step 3 — Rename one source file

1. In the source folder, rename `MJ-033.mp4.png` to `MJ-033.png`. It is a PNG still image, 1920 x 2400. It is not a video.
2. If `MJ-033.png` already exists, stop and report.
3. Do not rename or move any other file. Do not add any file from `C:\Claude\Projects\Gallery\Video\`.

## Step 4 — Find the new images

1. List the image files in the source folder.
2. Compare the list with the `source_name` values in `gallery/gallery.json`.
3. Record each image that is not in the gallery and not in `exclude`.
4. The list must be exactly these 21 files: `NB-021.jpg`, `MJ-020.png`, `MJ-021.png`, `NB-022.jpg`, `MJ-022.png`, `MJ-023.png`, `MJ-024.png`, `MJ-025.png`, `MJ-026.png`, `MJ-027.jpg`, `MJ-028.png`, `MJ-029.png`, `MJ-030.png`, `MJ-031.png`, `MJ-032.png`, `NB-024.jpg`, `MJ-033.png`, `NB-025.jpg`, `MJ-035.png`, `MJ-036.jpg`, `MJ-037.png`.
5. If the list is different, stop and report the list. These IDs are not for the gallery: MJ-014, MJ-016, MJ-034, NB-014, NB-015, NB-016, NB-017, NB-023.

## Step 5 — Read the batch file

1. Read the batch file. It has 21 entries, numbered 138 to 158.
2. For each entry, use the title, description, alt text, and style line exactly as written. Most descriptions are longer than 35 words. Adam approved them, so do not shorten them.
3. Three entries have a style line. Use each one exactly as written:
   - 138 The New Orrery: `In the spirit of Joseph Wright of Derby`
   - 139 The Golden Shell: `In the spirit of Salvador Dalí`
   - 156 Hold the Line: `In the spirit of Winslow Homer`
4. The other 18 entries have an empty style.

## Step 6 — Signature and mark checks

Do the checks that each batch entry lists in its **Checks** field:

1. All Midjourney images: check all four corners for a signature or a mark.
2. `MJ-032.png` (The Last Pile): check carefully for a "Norman Rockwell" signature. An earlier run had one.
3. `MJ-030.png` (Morning Incense): check the lower-right corner for small signature letters.
4. `MJ-028.png` (Lantern Stars): confirm that the tiles show no invented script.
5. The six Nano Banana images and finishes (`NB-021.jpg`, `NB-022.jpg`, `NB-024.jpg`, `NB-025.jpg`, `MJ-027.jpg`, `MJ-036.jpg`): check all four corners. Keep the visible Gemini mark if one shows. It is a provenance label, not a signature.
6. `NB-022.jpg`: confirm that the plaque reads exactly `LORD BARTHOLOMEW BOLOGNA III` and `Of the House of Deli`.
7. `NB-024.jpg`: confirm that the list reads exactly `WHEN PIGS FLY:`, `Fix the porch step`, `Paint the barn`, `Take me dancing`, `Clean the gutters`. Report any spelling error. Do not fix spelling.
8. If you find a signature or unwanted text, retouch it. If a retouch leaves a visible trace after 2 attempts, stop and report. Do not exclude the image.

## Step 7 — Size check

1. Build the web image of each file with the normal procedure. Do not upscale any image.
2. Report the source size and the web build size of each of the 21 images.

## Step 8 — Add to the gallery

1. Add the 21 images to the gallery with their captions, as numbers 138 to 158.
2. Back up the cumulative index to `C:\Claude\Projects\Gallery\backups\` before you change it.
3. Append the batch file to the cumulative index. Start at the line `# Prompt Index — 26 October 2026` and continue to the end of the file. Do not append the top section.
4. Never replace the cumulative index. Only append.

## Step 9 — Test and publish

1. Test the gallery page locally. Confirm that the 21 images and captions show.
2. Commit and push to `main`.
3. Wait for the Render deploy.
4. Check https://adamlozo.com/gallery/ for all 21 images and captions. Report the total image count on the live page.
5. Move the batch file to `C:\Claude\Projects\Gallery\backups\processed\`.

## Step 10 — Update the prompt log

1. Back up `C:\Claude\Projects\Gallery\prompt-log.md` to `C:\Claude\Projects\Gallery\backups\` before you change it.
2. In the entries for the 21 IDs in Step 4, change the status line to `- **Status:** published`. For MJ-033, the status line currently ends with a note; replace the whole line.
3. In the "Pending" section, change the line that starts with `- Batch 2026-10-26` to say that the batch is live, with the commit hash.
4. Do not change other text in the prompt log. Do not change the entries for MJ-014, MJ-016, MJ-034, or NB-023.

## Report back

- The three values from Step 2, and how they relate to the 195 count.
- The rename from Step 3.
- The list of new images from Step 4.
- The result of each check in Step 6, and each retouch done.
- The source size and web build size of each image.
- Any image that you could not add, and why.
- Index entry count before and after.
- Local test result.
- Commit hash.
- Live page check result and the total image count.
- The prompt-log changes from Step 10.
