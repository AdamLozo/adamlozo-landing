# Claude Code prompt — Add gallery batch 2026-10-24

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Source folder: `C:\Claude\Projects\Gallery\Images`
Batch file: `C:\Claude\Projects\Gallery\index-entries-2026-10-24.md`
Cumulative index: `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-gallery-add-2026-10-24.md`

Do not change any existing gallery entry. Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Read the procedure

1. Read `docs/ADD-GALLERY-IMAGES.md` in the repo. Follow it for all steps below.
2. Read `tools/gallery_config.json`.
3. Copy this prompt into the repo as `docs/prompts/CC-gallery-add-2026-10-24.md`.
4. If the procedure conflicts with this prompt, stop and report the conflict.

## Step 2 — Rename four source files

Four source files still have their Midjourney names. Rename them in the source folder:

| Current name | New name |
|---|---|
| `ozolmada_Backlit_layered_cut-paper_shadow-box_diorama_flat_stac_66f70a3d-180f-4fde-a62f-830b1ca6ace3.png` | `MJ-006.png` |
| `ozolmada_radiant_golden_bird_with_wide_open_wings_rising_out_of_7923e6f9-ff9b-474f-b237-485c9d1854c2.png` | `MJ-007.png` |
| `ozolmada_white_sea_foam_rising_in_the_shape_of_an_open_hand_wit_a33184b0-3df2-4c9f-a5ae-b942d37a1380.png` | `MJ-008.png` |
| `ozolmada_Contemporary_narrative_oil_painting_warm_painterly_rea_14e12e88-94be-4746-9c5a-8a4b1f66afbc.png` | `MJ-009.png` |

1. Before you rename `MJ-009`, look at the image. It must be a close-up of a shy couple a little apart on a wet brownstone stoop at night, with a tabby cat in a lit window. If it is a wide street view, stop and report.
2. If a target name already exists, stop and report.
3. Do not rename or move any other file.

## Step 3 — Find the new images

1. List the image files in the source folder.
2. Compare the list with the `source_name` values in `gallery/gallery.json`.
3. Record each image that is not in the gallery and not in `exclude`.
4. The list must be exactly these 15 files: `MJ-006.png`, `MJ-007.png`, `MJ-008.png`, `MJ-009.png`, `MJ-010.png`, `MJ-011.png`, `MJ-012.png`, `MJ-013.png`, `MJ-015.png`, `NB-018.jpg`, `NB-019.jpg`, `MJ-017.png`, `MJ-018.png`, `NB-020.jpg`, `MJ-019.png`.
5. If the list is different, stop and report the list. Do not add `MJ-014` (Her Chair). It is not for the gallery.

## Step 4 — Read the batch file

1. Read the batch file. It has 15 entries, numbered 123 to 137.
2. Confirm that the highest gallery number in `gallery/gallery.json` is 122. If it is not 122, stop and report it.
3. For each entry, use the title, description, alt text, and style line exactly as written. Most descriptions are longer than 35 words. Adam approved them, so do not shorten them.
4. Nine entries have a style line. Use each one exactly as written:
   - 124 After the Fall: `In the spirit of Pieter Bruegel the Elder`
   - 125 The Sea Catches Icarus: `In the spirit of Katsushika Hokusai`
   - 127 The Gold at Her Hem: `In the spirit of Gustav Klimt`
   - 128 The Keeper: `In the spirit of Edward Hopper`
   - 129 Hostage: `In the spirit of Henry Fuseli`
   - 131 The Circle: `In the spirit of Caravaggio`
   - 132 The Empty Glass: `In the spirit of John Singer Sargent`
   - 134 First Snow: `In the spirit of Mary Blair`
   - 135 Room for One More: `In the spirit of Sonia Delaunay`
5. The other six entries have an empty style.
6. Image 129 (Hostage) comes from a poem whose poet is unknown. Do not add a credit line.

## Step 5 — Signature and mark checks

Do the checks that each batch entry lists in its **Checks** field:

1. All eleven Midjourney images: check all four corners for a signature or a mark.
2. `MJ-008.png`: also check for a seal or a stamp, because the style is a woodblock print.
3. `MJ-018.png`: confirm that no canvas edge, frame, or wall shows.
4. `MJ-017.png`: confirm that street signs and car plates show no readable text.
5. `NB-018.jpg`, `NB-019.jpg`, `NB-020.jpg`: check all four corners. Keep the visible Gemini mark. It is a provenance label, not a signature.
6. `NB-018.jpg`: confirm that the dance card on the vanity shows no readable text.
7. `NB-019.jpg`: confirm that the glass shows no lettering, badge, or patch.
8. `NB-020.jpg`: confirm that the window and the jukebox show no readable text.
9. If you find a signature or text, retouch it. If a retouch leaves a visible trace after 2 attempts, stop and report. Do not exclude the image.

## Step 6 — Size check

1. Build the web image of each file with the normal procedure. Do not upscale any image.
2. Report the source size and the web build size of each of the 15 images.

## Step 7 — Add to the gallery

1. Add the 15 images to the gallery with their captions, as numbers 123 to 137.
2. Back up the cumulative index to `C:\Claude\Projects\Gallery\backups\` before you change it.
3. Append the batch file to the cumulative index. Start at the line `# Prompt Index — 24 October 2026` and continue to the end of the file. Do not append the top section.
4. Never replace the cumulative index. Only append.

## Step 8 — Test and publish

1. Test the gallery page locally. Confirm that the 15 images and captions show.
2. Commit and push to `main`.
3. Wait for the Render deploy.
4. Check https://adamlozo.com/gallery/ for all 15 images and captions.
5. Move the batch file to `C:\Claude\Projects\Gallery\backups\processed\`.

## Step 9 — Update the prompt log

1. Open `C:\Claude\Projects\Gallery\prompt-log.md`.
2. Back it up to `C:\Claude\Projects\Gallery\backups\` before you change it.
3. In the entries for the 15 IDs in Step 3, change `- **Status:** final` to `- **Status:** published`.
4. In the entries for MJ-006 and MJ-007, change the `- **File:**` line to only `` `MJ-006.png` `` and `` `MJ-007.png` ``.
5. In the "Pending" section, change the line that starts with `- Batch 2026-10-24` to say that the batch is live, with the commit hash.
6. Do not change other text in the prompt log. Do not change the entries for MJ-014 or MJ-016.

## Report back

- The four renames from Step 2, and the result of the MJ-009 image check.
- The list of new images from Step 3.
- The result of each check in Step 5, and each retouch done.
- The source size and web build size of each image.
- Any image that you could not add, and why.
- Index entry count before and after.
- Local test result.
- Commit hash.
- Live page check result.
- The prompt-log changes from Step 9.
