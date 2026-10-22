# Claude Code prompt — Kindred person page: the Bead-Maker

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Person folder: `C:\Claude\Projects\Gallery\Series\Ancestors\people\bead-maker\`
Person log: `C:\Claude\Projects\Gallery\Series\Ancestors\people\bead-maker\bead-maker-log.md`
Series log: `C:\Claude\Projects\Gallery\Series\Ancestors\ancestors-prompt-log.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-kindred-bead-maker-page-2026-10-22.md`

Goal: publish the third Kindred person, the Bead-Maker, with the existing `tools/build_people.py`. She belongs to the group "Africa", with the Storyteller.

Rules:
- Use the existing script and template. Do not change page code unless the script fails, and then stop and report.
- Do not change the Storyteller's or the Grandmother's entries or pages, the series images, `series.json`, `gallery.json`, `Midjourney-Prompt-Index.md`, or `prompt-log.md`.
- Do not publish the character sheet.
- Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Check the inputs

1. Confirm that the person folder holds the six facet images `Ancestors-P3-BeadMaker-01-Portrait.jpg` to `Ancestors-P3-BeadMaker-06-Legacy.jpg`.
2. Confirm that the person log has the same format as `people\storyteller\storyteller-log.md`: the home card text, the page introduction, and six facets, each with paragraph 1, paragraph 2, and alt text.
3. Check all four corners of the six images for a signature, a logo, or a model mark.
4. If you find a mark, retouch it with Photoshop Generative Remove on a copy in `C:\Claude\Projects\Gallery\Retouched\`, as you did for the Grandmother's 05 Bond: move the original into `people\bead-maker\originals\`, put the retouched copy in the person folder under the same name, and add one line about it to the person log under that facet's prompt entry. If a trace stays after 2 attempts, stop and report. Look most closely at the lower right corners, where Nano Banana marks usually appear.

## Step 2 — Build

1. Run the script with the series numbers from the log:
   `py tools/build_people.py ancestors "C:\Claude\Projects\Gallery\Series\Ancestors\people\bead-maker" --seen-in 03`
2. Confirm that `people.json` now has three people, with the Storyteller and the Grandmother unchanged.
3. Report the display and full size of each image. Do not crop any image.

## Step 3 — Test, publish, and record

1. Test locally:
   - `/kindred/the-bead-maker/` shows six facets in order, with correct captions and alt text, and a working lightbox.
   - `/kindred/` shows "The People" with "Africa" (the Storyteller, then the Bead-Maker) and "Ice Age Europe" (the Grandmother).
   - The "Seen in the series" link opens 03 Love.
   - `/kindred/the-storyteller/` and `/kindred/the-grandmother/` are unchanged.
   - No horizontal scroll at 390 px. The main gallery still has 180 entries.
2. Copy this prompt into the repo as `docs/prompts/CC-kindred-bead-maker-page-2026-10-22.md`.
3. Commit and push to `main`.
4. Wait for the Render deploy. Do the same checks on the live site.
5. In the person log, change `- **Status:** all six facets final (approved 2026-10-22). Page not built yet.` to `- **Status:** published at adamlozo.com/kindred/the-bead-maker/, commit <hash>, 2026-10-22.`
6. In the series log, change `(ANC-57 to ANC-67; all six facets approved 2026-10-22; page not built yet)` to `(ANC-57 to ANC-67; published 2026-10-22, commit <hash>)`.
7. Change no other text in either log.

## Report back

- The result of the input and corner checks.
- The script output and the display and full size of each image.
- The new and changed files.
- Main gallery entry count before and after (it must be 180).
- Local test results.
- Commit hash.
- Live check results.
- The changes in the two logs.
