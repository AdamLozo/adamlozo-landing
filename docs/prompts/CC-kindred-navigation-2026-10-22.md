# Claude Code prompt — Kindred navigation

Repo: `C:\Claude\Projects\adamlozo-landing` (branch `main`)
This prompt: `C:\Claude\Projects\Gallery\docs\CC-kindred-navigation-2026-10-22.md`

Goal: make the person pages easy to find, and let visitors move from one person to the next. Adam approved this design. Put every change in the shared template and the build scripts, so every future person gets it with no extra work.

Rules:
- Do not change any caption, alt text, image, or the order of the nine series images.
- Do not change `gallery/gallery.json` or the main gallery.
- Do not change the person logs or the series log.
- Stop and report on any failure or ambiguity. Do not use a workaround.

## Step 1 — Read

1. Read `kindred/index.html`, `tools/build_people.py`, `tools/templates/person.html`, `tools/build_series.py`, and `gallery/series/ancestors/people.json`.
2. Record how the Kindred page and the person pages load `series.json` and `people.json`.

## Step 2 — Kindred page: show that the people exist

1. Under the title "Kindred" and its subtitle, add one line: `Nine images tell the story of two bands. Then meet the people, each in six portraits.`
2. Under that line, add two jump links: `The Story` (to the nine series images) and `The People` (to the people section). Give the two sections the anchors `#the-story` and `#the-people`.
3. Under the heading "The People", add one line: `Each person's life in six portraits: who they are, their work, a hardship, a joy, a bond, and what they pass on.`

## Step 3 — Kindred page: person cards

Change each person card so that it clearly opens more images:
1. Keep the portrait image, the name, the group, and the summary line.
2. Add a row of six small thumbnails, one for each facet in order, from the person's display images. On a phone, the six thumbnails may wrap to two rows of three.
3. Add a clear button at the bottom of the card: `See the six portraits →`.
4. Make the whole card one link to the person page, with a visible hover and focus state.
5. Keep the cards grouped as now: "Africa", then "Ice Age Europe", with the people in `people.json` order inside each group.

## Step 4 — Kindred page: links from the story to the people

1. For each series image, find every person whose `seen_in` list contains that image number.
2. Under that image's caption, add a small link for each such person: `Meet the Storyteller →` (use the person's `name`).
3. Build these links from `people.json` when the page loads, so new people add their links automatically.
4. Expected now: 01 The Hearth and 05 Care link to the Storyteller; 03 Love links to the Bead-Maker; 04 Family and 08 Collaboration link to the Grandmother.

## Step 5 — Person pages: trail, next and previous, and return link

1. At the top of each person page, add a trail: `Kindred › The People › <name>`. "Kindred" links to `/kindred/`, and "The People" links to `/kindred/#the-people`.
2. After the "Seen in the series" links, add a block with two links, each with the small display image of that person's 01 Portrait and their name:
   - `← <previous person>` and `<next person> →`.
   - The order is the same as the order of the cards on the Kindred page: all "Africa" people, then all "Ice Age Europe" people. The list wraps around at both ends.
   - Expected now: the Storyteller → the Bead-Maker → the Grandmother → the Storyteller.
3. Change every "Back" link on the person pages to `All the people`, linking to `/kindred/#the-people`.
4. Build the next and previous links from `people.json` when the page loads, so a new person changes the order automatically.
5. Run `tools/build_people.py` again for all three people, so all three pages use the new template. Confirm that the text in `people.json` does not change.

## Step 6 — Fix the cache delay after a deploy

1. After a deploy, the edge cache can serve the old `people.json` for up to 300 seconds, and a new person page then shows no facets.
2. Fix this with a version query on the data files: when a build script writes `people.json` or `series.json`, it also writes a short content hash of that file into the pages that load it, and the pages fetch `people.json?v=<hash>` and `series.json?v=<hash>`.
3. If the HTML pages themselves are also cached for 300 seconds, report it. Do not change any cache setting on Render or Cloudflare.

## Step 7 — Test and publish

1. Test locally:
   - The Kindred page shows the intro line and the two jump links, and both links jump to the correct section.
   - Each person card shows six thumbnails and the button, and the whole card opens the person page.
   - The "Meet …" links appear under exactly the five series images in Step 4, and each opens the correct person page.
   - Each person page shows the trail, the previous and next links in the expected order with wrap-around, and "All the people" goes to the people section, not to the top of the page.
   - The lightbox on every page still works.
   - No page scrolls sideways at 390 px. Keyboard focus is visible on the cards and links.
   - The main gallery still has 180 entries.
2. Copy this prompt into the repo as `docs/prompts/CC-kindred-navigation-2026-10-22.md`.
3. Commit and push to `main`.
4. Wait for the Render deploy. Do the same checks on the live site. Confirm that the pages fetch the data files with the version query.

## Report back

- How the pages load the data, before and after the change.
- The new and changed files.
- The order of the next and previous links, as tested.
- The five "Meet …" links, as tested.
- Whether the HTML pages are cached, and how long.
- Local test results.
- Commit hash.
- Live check results.
