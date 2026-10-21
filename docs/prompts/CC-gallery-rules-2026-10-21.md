# Claude Code prompt — Gallery rule update and MJ-003 record fix

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Procedure: `docs/ADD-GALLERY-IMAGES.md` in the repo
Cumulative index: `C:\Claude\Projects\Gallery\Midjourney-Prompt-Index.md`
Prompt log: `C:\Claude\Projects\Gallery\prompt-log.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-gallery-rules-2026-10-21.md`

Make only the changes in this prompt. Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Update the signature-scribble rule

1. Open `docs/ADD-GALLERY-IMAGES.md`.
2. Change line 66 from `- Keep images with scribbles or generic fake lettering. Do not crop or retouch them.` to `- Keep images with generic fake lettering. Do not crop or retouch them.`
3. Directly after that line, add this new bullet:

   `- Retouch Midjourney signature scribbles with Photoshop Generative Remove, on a copy in C:\Claude\Projects\Gallery\Retouched. Do not change the source file. If Photoshop is not available, use the retouch-box fallback in this document. If a trace stays after 2 attempts, stop and report.`

4. Keep the retouch-box fallback (lines 78 to 96) as it is.
5. Change no other text in the document.

(Revised 2026-10-21 after Claude Code stopped at Step 1: Adam chose option B and kept the fallback.)

## Step 2 — Update the batch-number rule

1. In `docs/ADD-GALLERY-IMAGES.md`, find each place that gets the next gallery number from `gallery/gallery.json`.
2. Change it to get the number from the highest `### N.` entry in the cumulative index.
3. If the document has no such place, record this in the report and make no change.

## Step 3 — Correct the MJ-003 corner in the cumulative index

Adam approved this one edit to an existing index entry. It is an exception to the append-only rule.

1. Back up the cumulative index to `C:\Claude\Projects\Gallery\backups\Midjourney-Prompt-Index_2026-10-21_before-MJ-003-fix.md`.
2. Find entry `### 120. Moving Day`.
3. In its `- **Checks:**` line (line 2787 only, not line 2806), change `the lower right corner` to `the lower left corner`.
4. Change nothing else in the index.
5. Confirm that the index has the same line count before and after the change.

## Step 4 — Correct the MJ-003 corner in the prompt log

1. Open the prompt log.
2. In the "Pending" line that starts with `- MJ-003 (Moving Day)`, change `at lower right` to `at lower left`.
3. In the `## MJ-003 — Moving Day` entry, change the line `- **Gallery note:** retouch the signature scribble at lower right.` to `- **Gallery note:** retouch the signature scribble at lower left (corrected 2026-10-21).`
4. Do not change line 802 (the v2 history note). It records what was seen at that time.
5. Change nothing else in the prompt log.

## Step 5 — Commit

1. Copy this prompt into the repo as `docs/prompts/CC-gallery-rules-2026-10-21.md`.
2. Commit `docs/ADD-GALLERY-IMAGES.md` and the prompt copy to `main`, then push.
3. The index and the prompt log are outside the repo. Do not commit them.

## Report back

- The diff of `docs/ADD-GALLERY-IMAGES.md`.
- The result of Step 2, with the old and the new text.
- The index line count before and after, and the changed line.
- The two changed lines in the prompt log.
- The commit hash.
