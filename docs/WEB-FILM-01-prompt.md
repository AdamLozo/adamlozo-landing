# WEB-FILM-01 — Add "Lady Eleanore's Mantle" to adamlozo.com (YouTube embed)

- **Run ID:** `WEB-FILM-01`
- **Site:** the adamlozo.com landing site, deployed on Render as the service **`adamlozo-landing`**.
- **Video:** https://youtu.be/sk1RsAPlbY0 (video ID `sk1RsAPlbY0`), public on YouTube.
- This run is outside the Province-House repo. The Province-House boilerplate does not apply, except the rules that this prompt states.

## Director's decisions this prompt assumes — do not run it otherwise

1. The film is shown on adamlozo.com as a **YouTube embed**. The video file is not hosted on Render (director, chat 2026-10-12).
2. Use the privacy-enhanced embed host `https://www.youtube-nocookie.com/embed/sk1RsAPlbY0`.
3. **Nothing is published without the director's yes.** A push to the branch that Render deploys publishes the site, so it waits for his answer in Step 3.
4. Do not change any other part of the site, except the link to the film page (Step 2).
5. **STOP and ask** on any blocker or tool failure. No workarounds.

## Step 0 — Find the site

1. Find the local repo of the site. Search `C:\Claude\Projects\` for a git repo whose remote, `render.yaml`, package name or README names `adamlozo-landing` or adamlozo.com. Report its path and its git remote.
2. **STOP** if you find none or more than one. Report what you found.
3. `cd` to that repo. Check that the working tree is clean and that the local branch equals its remote. **STOP** if not; report the state.
4. Save this prompt with the **Write tool** to `docs/WEB-FILM-01-prompt.md` in that repo. Check first that the path is free.

## Step 1 — Inventory (read-only)

Report:
1. The framework and the build (plain HTML, React, Next.js, or other), the build command, and the publish folder.
2. Which branch Render deploys (from `render.yaml` or the repo docs; if no record, state UNKNOWN).
3. The pages and the routes. The home page sections, in order, with their headings.
4. The shared styles: the fonts, the colours (as tokens if there are any), and the dark mode, if any.
5. Any existing section for projects or films.

## Step 2 — PAUSE: where the film goes

Show the director these choices, labelled "Option 1" and "Option 2", one plain line each:
- **Option 1 (chat's recommendation):** a new page `/films/lady-eleanores-mantle` with the embed and a short text, plus one card on the home page that links to it.
- **Option 2:** a section on the home page with the embed in it.

Wait for his answer. Do not edit any file before it.

## Step 3 — Build the change

After the director's answer:

1. **The embed:**
   - an `<iframe>` with `src="https://www.youtube-nocookie.com/embed/sk1RsAPlbY0"`, `title="Lady Eleanore's Mantle"`, `loading="lazy"`, `allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share"`, `allowfullscreen`, `referrerpolicy="strict-origin-when-cross-origin"`;
   - full width of its column, with the aspect ratio 2656 / 1600 (CSS `aspect-ratio`), no fixed height;
   - it works at phone width (375 px) with no horizontal scroll.
2. **The text** (use it word for word):
   - Heading: **Lady Eleanore's Mantle**
   - Line under it: *A 21-minute AI film after Nathaniel Hawthorne's "Legends of the Province House" (1838).*
   - Paragraph: In 1721, Lady Eleanore Rochcliffe arrives at the Province House in Boston, wrapped in a gold-embroidered mantle. Her pride is matched only by the beauty of the mantle, and by what it carries. Every image and voice was made with AI tools on one home PC, and directed, cut and finished by hand.
   - A link under the embed: "Watch on YouTube" → https://youtu.be/sk1RsAPlbY0
3. **For Option 1 only:** the page gets a `<title>`, a meta description (the line under the heading), and Open Graph tags (`og:title`, `og:description`, `og:type` = `video.other`, `og:url`, `og:image` = `https://i.ytimg.com/vi/sk1RsAPlbY0/maxresdefault.jpg`). The home card uses the same title, the line, and the same image.
4. Use the site's own styles, fonts and colours. Do not add a new library.
5. Build the site locally and run it. Check the page at 1280 px and at 375 px wide. Report what you see, and any console error.
6. Commit on a new branch `web-film-01`. Do not push it yet.
7. **PAUSE:** tell the director the local address to look at, and ask: "Publish to adamlozo.com?" Do not merge or push to the deploy branch before his yes.

## Step 4 — Publish (only after the director's yes)

1. Merge `web-film-01` into the deploy branch, and push.
2. Report the Render deploy status, if you can read it. If you cannot, say so; do not guess.
3. Open the live page and check that the video plays. Report the result.

## Report

Paste back:
- the repo path and remote; the inventory;
- the director's placement choice;
- the files changed, with a one-line summary each;
- the local checks at 1280 px and 375 px;
- the director's publish answer, the commit and push, and the live check;
- any problem, with no workaround.
