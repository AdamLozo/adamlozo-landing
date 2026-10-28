# LAND-LG-01 — Add The Lost Ghost to adamlozo.com

`cd C:\Claude\Projects\adamlozo-landing` and obey the repo's own instructions, if it has a `CLAUDE.md`.

## Decisions this prompt assumes — do not run it otherwise

1. **New film page:** `films/the-lost-ghost/index.html`. Copy the structure, styles and markup of `films/lady-eleanores-mantle/index.html` exactly. Change only the content of decision 2.
2. **Content of the new page:**
   - YouTube ID: `CEqOjUfjpfo`. Embed: `https://www.youtube-nocookie.com/embed/CEqOjUfjpfo`. Watch link: `https://youtu.be/CEqOjUfjpfo`.
   - Page title: `The Lost Ghost — Adam Lozo`.
   - H1: `The Lost Ghost`.
   - Sub line, meta description, `og:description` and `twitter:description`: `A 20-minute AI film after Mary E. Wilkins Freeman's ghost story "The Lost Ghost" (1903).` Escape the quotes in the meta tags as `&quot;`, as the Mantle page does.
   - `og:url`: `https://adamlozo.com/films/the-lost-ghost/`.
   - `og:image` and `twitter:image`: `https://i.ytimg.com/vi/CEqOjUfjpfo/maxresdefault.jpg` (1280×720).
   - Player frame: `aspect-ratio: 1920 / 1152;` (the film is 1920×1152).
   - About paragraph (use this text exactly):
     `One winter, a young schoolteacher boards with two sisters in a quiet New England house. At night, a small child comes to the doors, looking for her mother. Years later, by the parlour window, the teacher tells the story for the first time. Every image and voice was made with AI tools on one home PC, and directed, cut and finished by hand.`
   - Add a second paragraph with the same `about` style, directly after the first:
     `Dedicated to Christine (@WICKED_Queen12), the most Halloween person I've ever known. The Lost Ghost is yours.`
     Link `@WICKED_Queen12` to `https://x.com/WICKED_Queen12`, with `rel="noopener"`.
3. **Main page list (`index.html`):** find the list item for Lady Eleanore's Mantle. Add a new item for The Lost Ghost in the same markup and style, **above** the Mantle item, because it is the newest film. Link it to `/films/the-lost-ghost/`. Use the same type of label, short text and any badge or tag that the Mantle item has. Its short text: `A 20-minute AI ghost film after Mary E. Wilkins Freeman (1903).` If the Mantle item shows an image, use `https://i.ytimg.com/vi/CEqOjUfjpfo/maxresdefault.jpg` in the same way.
4. **Do not change** any other page, style or file. Do not change the Mantle page or the Mantle list item.

## Step 0 — checks

1. Check that the repo is at `C:\Claude\Projects\adamlozo-landing` and that its remote is `AdamLozo/adamlozo-landing`. STOP if not.
2. Check that the branch is `main`, that HEAD = `origin/main` after `git fetch`, and that the tree is clean. STOP if not.
3. Check that `films/the-lost-ghost/` does not exist. STOP if it does.
4. Save this prompt to `docs/LAND-LG-01-prompt.md` with the Write tool.

## Step 1 — build

1. Make the new page by decisions 1 and 2.
2. Add the list item by decision 3.

## Step 2 — check

1. Serve the site locally (for example `python -m http.server`). Open `/` and `/films/the-lost-ghost/`.
2. Check: the new list item shows above Mantle and its link opens the new page; the player loads the video ID `CEqOjUfjpfo`; the back links work; the X link opens the right profile; there are no console errors.
3. Check the page at a phone width (390 px): no horizontal scroll, and the player fits.
4. Validate that both HTML files have no unclosed tags (for example with `python -m html.parser` or a small script).

## Step 3 — push and live check

1. Commit with `git commit -F <msgfile>`: "Add The Lost Ghost film page and list item". Push, and check that `git ls-remote origin main` = HEAD.
2. Render publishes the site from the push. Wait up to 5 minutes. Then check that `https://adamlozo.com/films/the-lost-ghost/` returns 200 and contains `CEqOjUfjpfo`, and that `https://adamlozo.com/` contains `/films/the-lost-ghost/`. If the site is not updated after 5 minutes, report it. Do not trigger a deploy by other means.

## Stop rules

- STOP and ask on any blocker or tool failure. No workarounds without guidance.
- If the main page has no clear Mantle list item to copy, STOP and report the structure you found.

## Report

Keep it short: Step 0 results, the files changed with their line ranges, the local check results, the live check results, and HEAD after the push.
