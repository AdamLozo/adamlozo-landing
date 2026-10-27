# Claude Code prompt — Add gallery batch 2026-10-26 (continue from Step 3)

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
First prompt: `C:\Claude\Projects\Gallery\docs\CC-gallery-add-2026-10-26.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-gallery-add-2026-10-26b.md`

Do not change any existing gallery entry. Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Step 2 of the first prompt is resolved

Adam confirms these facts (2026-10-26):

1. The index numbering is the gallery numbering. Gallery numbers exist only in the cumulative index.
2. `gallery/gallery.json` has no number field. This is correct. Do not add one.
3. The highest gallery number is 137, from the index.
4. The 195 entries in `gallery.json` include images that have no index entry. This is normal.
5. The three index titles with no gallery match (1, 2, and 25) are out of scope. Do not investigate or change them.

## Step 2 — Copy this prompt

1. Copy this prompt into the repo as `docs/prompts/CC-gallery-add-2026-10-26b.md`.

## Step 3 — Continue the first prompt

1. Open the first prompt.
2. Do Steps 3 to 10 of the first prompt, in order.
3. Apply these two clarifications:
   - Step 8.1 of the first prompt: "numbers 138 to 158" are the index headings. In `gallery.json`, append the 21 new entries in the same order, 138 first and 158 last, with the same fields as the existing entries.
   - Step 9.4 of the first prompt: the live page must show 216 images (195 + 21). If the count is different, report it.

## Report back

- The report items of the first prompt, for Steps 3 to 10.
- Confirm that `gallery.json` has 216 entries and that the 21 new entries are at the end, in order.
