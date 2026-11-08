# Claude Code prompt — Add gallery batch 2026-11-08

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Source folder: `C:\Claude\Projects\Gallery\Images`
Batch file: `C:\Claude\Projects\Gallery\index-entries-2026-11-08.md`
Cumulative index: `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-gallery-add-2026-11-08.md`

Do not change any existing gallery entry. Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Read the procedure

1. Read `docs/ADD-GALLERY-IMAGES.md` in the repo. Follow it for all steps below.
2. Read `tools/gallery_config.json`.
3. Copy this prompt into the repo as `docs/prompts/CC-gallery-add-2026-11-08.md`.
4. If the procedure conflicts with this prompt, stop and report the conflict.

## Step 2 — Check the gallery count and numbering

The live gallery showed 216 images after the 2026-10-26 batch. The cumulative index ends at gallery number 158. Check this before you change anything.

1. In `gallery/gallery.json`, count the entries.
2. Find the highest gallery number.
3. Count the entries in the cumulative index (`### <number>.` headings).
4. Report the three values.
5. If the highest gallery number is 158, continue. The batch uses numbers 159 to 171.
6. If the highest gallery number is not 158, stop. Report the count, the highest number, and how they relate. Do not renumber anything.

## Step 3 — Rename one source file

1. In the source folder, rename `last-house-of-the-day.png` to `MJ-044.png`. It is a PNG still image.
2. If `MJ-044.png` already exists, stop and report.
3. Do not rename or move any other file.

## Step 4 — Find the new images

1. List the image files in the source folder.
2. Compare the list with the `source_name` values in `gallery/gallery.json`.
3. Record each image that is not in the gallery and not in `exclude`.
4. The list must be exactly these 13 files: `MJ-038.png`, `MJ-039.png`, `MJ-040.png`, `MJ-041.png`, `MJ-042.png`, `MJ-043.jpg`, `MJ-044.png`, `MJ-045.jpg`, `MJ-046.jpg`, `MJ-047.jpg`, `MJ-048.jpg`, `MJ-049.jpg`, `MJ-050.jpg`.
5. If the list is different, stop and report the list. Do not add any file from `C:\Claude\Projects\Gallery\Video\`.

## Step 5 — Read the batch file

1. Read the batch file. It has 13 entries, numbered 159 to 171.
2. For each entry, use the title, description, alt text, and style line exactly as written. Some descriptions are longer than 35 words. Adam approved them, so do not shorten them.
3. Four entries have a style line. Use each one exactly as written:
   - 160 The Lamps Come On: `In the spirit of Edgar Degas`
   - 164 Where the Roads Split: `In the spirit of Andrew Wyeth`
   - 165 Last House of the Day: `In the spirit of Norman Rockwell`
   - 171 Refill: `In the spirit of Andy Warhol`
4. The other 9 entries have an empty style.

## Step 6 — Signature and mark checks

Do the checks that each batch entry lists in its **Checks** field:

1. All images: check all four corners for a signature or a mark.
2. The seven Nano Banana finishes (`MJ-043.jpg`, `MJ-045.jpg`, `MJ-046.jpg`, `MJ-047.jpg`, `MJ-048.jpg`, `MJ-049.jpg`, `MJ-050.jpg`): keep the visible Gemini mark if one shows. It is a provenance label, not a signature.
3. `MJ-038.png` (The Longest Night): the canvas edges and the wall are part of the image. Do not crop them.
4. `MJ-041.png` (Two Places Set): check the lower right, between the paint drips, for faint marks that look like lettering.
5. `MJ-042.png` (Just Before Grace): check the small picture on the wall, to the left of the young man, for invented lettering.
6. `MJ-044.png` (Last House of the Day): check carefully for a "Norman Rockwell" signature. Examine the paper list on her lap. If any handwritten word looks like a name or a signature, do not retouch it. Stop and report, with the position of the word. Adam will fix it with a region edit.
7. `MJ-045.jpg`, `MJ-048.jpg`: check the lower-right corner with special care. A signature appeared there before and was removed.
8. `MJ-046.jpg`: check the lower-left corner with special care, for the same reason.
9. `MJ-050.jpg` (Refill): check the bottom margin for pencil signatures or numbers.
10. If you find a signature or unwanted text (except on the MJ-044 list), retouch it. If a retouch leaves a visible trace after 2 attempts, stop and report. Do not exclude the image.

## Step 7 — Size check

1. Build the web image of each file with the normal procedure. Do not upscale any image.
2. Report the source size and the web build size of each of the 13 images.

## Step 8 — Add to the gallery

1. Add the 13 images to the gallery with their captions, as numbers 159 to 171.
2. Back up the cumulative index to `C:\Claude\Projects\Gallery\backups\` before you change it.
3. Append the batch file to the cumulative index. Start at the line `# Prompt Index — 8 November 2026` and continue to the end of the file. Do not append the top section.
4. Never replace the cumulative index. Only append.

## Step 9 — Test and publish

1. Test the gallery page locally. Confirm that the 13 images and captions show.
2. Commit and push to `main`.
3. Wait for the Render deploy.
4. Check https://adamlozo.com/gallery/ for all 13 images and captions. The live page must show 229 images. Report the total image count on the live page.
5. Move the batch file to `C:\Claude\Projects\Gallery\backups\processed\`.

## Step 10 — Update the prompt log

1. Back up `C:\Claude\Projects\Gallery\prompt-log.md` to `C:\Claude\Projects\Gallery\backups\` before you change it.
2. In the entries for the 13 IDs in Step 4 (MJ-038 to MJ-050), change the status line to `- **Status:** published`.
3. In the MJ-044 entry, change the File line to ``- **File:** `MJ-044.png` (renamed from `last-house-of-the-day.png`)``.
4. In the "Pending" section, change the line that starts with `- Batch 2026-11-08` to say that the batch is live, with the commit hash.
5. Do not change other text in the prompt log.

## Report back

- The three values from Step 2.
- The rename from Step 3.
- The list of new images from Step 4.
- The result of each check in Step 6, and each retouch done. Report any MJ-044 list word that looks like a name or a signature.
- The source size and web build size of each image.
- Any image that you could not add, and why.
- Index entry count before and after.
- Local test result.
- Commit hash.
- Live page check result and the total image count.
- The prompt-log changes from Step 10.
