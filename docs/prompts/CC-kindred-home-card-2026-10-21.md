# Claude Code prompt — Kindred as its own home-page item

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
Series log: `C:\Claude\Projects\Gallery\Series\Ancestors\ancestors-prompt-log.md`
This prompt: `C:\Claude\Projects\Gallery\docs\CC-kindred-home-card-2026-10-21.md`

Goal: Kindred is its own item on the adamlozo.com home page, with its own address `/kindred/`. It is no longer part of the main Gallery. This prompt also includes the gallery header change from `CC-gallery-header-tools-2026-10-21.md`. Do not run that prompt separately.

Adam's decisions:
- New address: `https://adamlozo.com/kindred/`. The old address `/gallery/ancestors/` forwards to it.
- Remove the Kindred series card from the main Gallery page.
- Add a Kindred card to the home page.

Rules:
- Do not change `gallery/gallery.json`, the main grid, or any image caption.
- Do not move or rebuild the series images.
- Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Read

1. Read the home page file and find how its project cards are built (HTML, data file, or script).
2. Find the header text "12 projects live" and "Selected work 001 — 012". Find how these numbers are made. The home page has 13 cards now, so the numbers are already wrong.
3. Read `gallery/ancestors/index.html` and `gallery/index.html`.
4. Record what you found before you change anything.

## Step 2 — Move the series page to /kindred/

1. Create `kindred/index.html` from `gallery/ancestors/index.html`.
2. Keep the images and `series.json` where they are, in `gallery/series/ancestors/`. Make sure that every path in the new page is absolute (it starts with `/`), so that it works from `/kindred/`.
3. Change the link back to the main gallery. It now links to the home page `/`, with the text "Back to home".
4. Set the canonical URL of the page to `https://adamlozo.com/kindred/`.

## Step 3 — Forward the old address

1. Replace `gallery/ancestors/index.html` with a small forwarding page to `/kindred/`.
2. Use a `<meta http-equiv="refresh" content="0; url=/kindred/">`, a `<link rel="canonical" href="https://adamlozo.com/kindred/">`, and a plain link to `/kindred/` for browsers that block the refresh.
3. If the repo already has a redirect file for Render (for example a `_redirects` file or a `render.yaml` route), stop and report it. Do not add a second method.

## Step 4 — Remove the series card from the Gallery

1. In `gallery/index.html`, remove the Kindred series card and its CSS (the 50 lines added in commit `b3be51b`).
2. Do not change the hero, the grid, or the grid script.

## Step 5 — Gallery header (from the header prompt)

1. In `gallery/index.html`, change `All images made with Midjourney.` to `All images made with Midjourney and Nano Banana.`
2. If the line already says this, record it and make no change.
3. Search the `<title>`, the meta description, and the Open Graph and Twitter tags of `gallery/index.html` for the same sentence. Make the same change there.
4. Report any other text that names only Midjourney for the whole gallery. Do not change it.

## Step 6 — Home page cards

1. On the home page Gallery card, change `All images made with Midjourney.` to `All images made with Midjourney and Nano Banana.` if that sentence is on the card.
2. Add a new card for Kindred, directly after the Gallery card. Use the same format as the other cards:
   - Title: `Kindred`
   - Type word: `Series`
   - Text: `Nine paintings of our earliest ancestors, and the qualities that kept them alive: love, family, care, art, music, friendship, teamwork, and endurance.`
   - Link: `https://adamlozo.com/kindred/`
   - Image: if the other cards have an image, use the display image of 01 The Hearth (`/gallery/series/ancestors/images/display/`). If the cards have no image, add none.
3. Make the header numbers agree with the real card count (14 after this change). If the numbers are typed by hand, change them to 14 and 001 — 014. If a script makes them, fix the script so that it counts the cards.

## Step 7 — Test and publish

1. Test locally:
   - `/kindred/` shows all nine images in order, with captions and a working lightbox.
   - `/gallery/ancestors/` forwards to `/kindred/`.
   - `/gallery/` shows the new header line, no series card, and an unchanged grid (180 entries).
   - The home page shows the Kindred card after the Gallery card, and the header shows 14.
   - `/kindred/` and the home page have no horizontal scroll at 390 px.
2. Copy this prompt into the repo as `docs/prompts/CC-kindred-home-card-2026-10-21.md`.
3. Commit and push to `main`.
4. Wait for the Render deploy. Do the same checks on the live site.

## Step 8 — Update the series log

1. In the series log, change the line `Page: \`adamlozo.com/gallery/ancestors/\`` to `Page: \`adamlozo.com/kindred/\` (moved 2026-10-21; the old address forwards)`.
2. Add one line under it: `Home page card added: commit <hash>, 2026-10-21.`
3. Change no other text.

## Report back

- What you found in Step 1, including how the home page numbers are made.
- The new and changed files.
- The forwarding method used.
- The header and card text, before and after.
- Any other Midjourney-only text that you found but did not change.
- Gallery entry count before and after (it must be 180).
- Local test results.
- Commit hash.
- Live check results.
