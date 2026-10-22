# Claude Code prompt — Kindred person page: the Child

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Person folder: `C:\Claude\Projects\Gallery\Series\Ancestors\people\child\`
Person log: `C:\Claude\Projects\Gallery\Series\Ancestors\people\child\child-log.md`
Series log: `C:\Claude\Projects\Gallery\Series\Ancestors\ancestors-prompt-log.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-kindred-child-page-2026-10-22.md`

Goal: publish the eighth Kindred person, the Child, with the existing `tools/build_people.py`. She belongs to the group "Africa", after the Storyteller, the Bead-Maker, and the Friend. She is the eighth and last person, and the only child.

Rules:
- Use the existing scripts and template. Do not change page code unless a script fails, and then stop and report.
- Do not change the other seven people's entries or pages, the series images, `series.json`, `gallery.json`, `Midjourney-Prompt-Index.md`, or `prompt-log.md`.
- Do not publish the character sheet.
- Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Check the inputs and retouch

Adobe limited Generative Remove after the last run. If a remove fails once, stop and ask Adam. Do not retry repeatedly.

If Photoshop stops answering for about 5 minutes, stop and ask Adam.


1. Confirm that the person folder holds the six facet images `Ancestors-P8-Child-01-Portrait.jpg` to `Ancestors-P8-Child-06-Legacy.jpg`.
2. Confirm that the person log has the same format as the other person logs.
3. 02 Responsibility ("Joseph Wright") and 05 Bond have known signatures at the lower right. Every earlier person had marks at the lower right of most images, so expect more.
4. Check all four corners of all six images, most closely at the lower right.
5. Retouch every mark you find with Photoshop Generative Remove on a copy in `C:\Claude\Projects\Gallery\Retouched\`, with the same method as before: move each original into `people\child\originals\`, put the retouched copy in the person folder under the same name, and add one line about it to the person log under that facet's prompt entry. If a trace stays after 2 attempts, stop and report.

## Step 2 — Build

1. Run: `py tools/build_people.py ancestors "C:\Claude\Projects\Gallery\Series\Ancestors\people\child" --seen-in 01 05`
2. Confirm that `people.json` now has eight people, with the other seven unchanged, and that the Child's `seen_in` is ["01", "05"].
3. Report the display and full size of each image. Do not crop any image.

## Step 3 — Test, publish, and record

1. Test locally:
   - `/kindred/the-child/` shows six facets in order, with correct captions and alt text, and a working lightbox.
   - `/kindred/` shows "Africa" (the Storyteller, the Bead-Maker, the Friend, the Child) and "Ice Age Europe" (the Grandmother, the Flute Player, the Painter, the Fire-Carrier). The Child's card shows six thumbnails and the button.
   - A "Meet the Child →" link appears under 01 The Hearth and under 05 Care, and each opens her page. Under 01 The Hearth, "Meet the Storyteller" and "Meet the Child" show. Under 05 Care, "Meet the Storyteller", "Meet the Friend", and "Meet the Child" show. The other "Meet" links are unchanged.
   - The next and previous order on all person pages is: the Storyteller → the Bead-Maker → the Friend → the Child → the Grandmother → the Flute Player → the Painter → the Fire-Carrier → the Storyteller.
   - The other seven person pages show no change except their next and previous links.
   - No page scrolls sideways at 390 px. The main gallery still has 180 entries.
2. Copy this prompt into the repo as `docs/prompts/CC-kindred-child-page-2026-10-22.md`.
3. Commit and push to `main`.
4. Wait for the Render deploy. Poll `/kindred/` until it loads `people.json` with the new `?v=` hash, then do the same checks on the live site.
5. In the person log, change `- **Status:** all six facets final (approved 2026-10-22). Page not built yet.` to `- **Status:** published at adamlozo.com/kindred/the-child/, commit <hash>, 2026-10-22.`
6. In the series log, change `(ANC-110 to ANC-116; all six facets approved 2026-10-22; page not built yet)` to `(ANC-110 to ANC-116; published 2026-10-22, commit <hash>)`.
7. Change no other text in either log, except the retouch lines from Step 1.

## Report back

- The input checks, each retouch, and any other marks found.
- The script output and the display and full size of each image.
- The new and changed files.
- Main gallery entry count before and after (it must be 180).
- Local test results, including the next and previous order and the "Meet" links.
- Commit hash.
- Live check results.
- The changes in the two logs.
