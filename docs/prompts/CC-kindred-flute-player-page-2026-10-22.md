# Claude Code prompt — Kindred person page: the Flute Player

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Person folder: `C:\Claude\Projects\Gallery\Series\Ancestors\people\flute-player\`
Person log: `C:\Claude\Projects\Gallery\Series\Ancestors\people\flute-player\flute-player-log.md`
Series log: `C:\Claude\Projects\Gallery\Series\Ancestors\ancestors-prompt-log.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-kindred-flute-player-page-2026-10-22.md`

Goal: publish the fourth Kindred person, the Flute Player, with the existing `tools/build_people.py`. He belongs to the group "Ice Age Europe", with the Grandmother.

Rules:
- Use the existing scripts and template. Do not change page code unless a script fails, and then stop and report.
- Do not change the other three people's entries or pages, the series images, `series.json`, `gallery.json`, `Midjourney-Prompt-Index.md`, or `prompt-log.md`.
- Do not publish the character sheet.
- Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Check the inputs and retouch

1. Confirm that the person folder holds the six facet images `Ancestors-P4-FlutePlayer-01-Portrait.jpg` to `Ancestors-P4-FlutePlayer-06-Legacy.jpg`.
2. Confirm that the person log has the same format as the other person logs.
3. 01 Portrait has a known signature-like scribble at the lower right. Retouch it with Photoshop Generative Remove on a copy in `C:\Claude\Projects\Gallery\Retouched\`, with the same method as the Grandmother's 05 Bond: move the original into `people\flute-player\originals\`, put the retouched copy in the person folder under the same name, and add one line about it to the person log under the ANC-70 entry. If a trace stays after 2 attempts, stop and report.
4. Check all four corners of all six images for a signature, a logo, or a model mark, most closely at the lower right. Retouch any other mark the same way, and record it in the log.

## Step 2 — Build

1. Run: `py tools/build_people.py ancestors "C:\Claude\Projects\Gallery\Series\Ancestors\people\flute-player" --seen-in 02`
2. Confirm that `people.json` now has four people, with the other three unchanged.
3. Report the display and full size of each image. Do not crop any image.

## Step 3 — Test, publish, and record

1. Test locally:
   - `/kindred/the-flute-player/` shows six facets in order, with correct captions and alt text, and a working lightbox.
   - `/kindred/` shows "Africa" (the Storyteller, the Bead-Maker) and "Ice Age Europe" (the Grandmother, the Flute Player). The Flute Player's card shows six thumbnails and the button.
   - A "Meet the Flute Player →" link appears under 02 The Flute and opens his page. The other "Meet" links are unchanged.
   - The next and previous order on all person pages is: the Storyteller → the Bead-Maker → the Grandmother → the Flute Player → the Storyteller.
   - The other three person pages show no change except their next and previous links.
   - No page scrolls sideways at 390 px. The main gallery still has 180 entries.
2. Copy this prompt into the repo as `docs/prompts/CC-kindred-flute-player-page-2026-10-22.md`.
3. Commit and push to `main`.
4. Wait for the Render deploy. Poll `/kindred/` until it loads `people.json` with the new `?v=` hash, then do the same checks on the live site.
5. In the person log, change `- **Status:** all six facets final (approved 2026-10-22). Page not built yet.` to `- **Status:** published at adamlozo.com/kindred/the-flute-player/, commit <hash>, 2026-10-22.`
6. In the series log, change `(ANC-68 to ANC-78; all six facets approved 2026-10-22; page not built yet)` to `(ANC-68 to ANC-78; published 2026-10-22, commit <hash>)`.
7. Change no other text in either log, except the retouch lines from Step 1.

## Report back

- The input checks, the retouch of 01, and any other marks found.
- The script output and the display and full size of each image.
- The new and changed files.
- Main gallery entry count before and after (it must be 180).
- Local test results, including the next and previous order and the "Meet" links.
- Commit hash.
- Live check results.
- The changes in the two logs.
