# WEB-FILM-02 — Link-preview tags, the home description, and the merged branch

- **Run ID:** `WEB-FILM-02`
- **Repo:** `C:\Claude\Projects\adamlozo-landing` (remote `https://github.com/AdamLozo/adamlozo-landing`, Render deploys `main`).
- **Parent run:** `WEB-FILM-01` (commit `4197d9b`, live).

## Director's decisions this prompt assumes — do not run it otherwise

1. **Add X card tags to the film page** `films/lady-eleanores-mantle/index.html`, so that a shared link shows a large preview (director, chat 2026-10-13).
2. **Add the film to the home page description.**
3. **Delete the merged branch `web-film-01`.**
4. **Publishing is approved** for exactly these changes (director, chat 2026-10-13). Change nothing else on the site.
5. **STOP and ask** on any blocker or tool failure. No workarounds. Call Python with `py -3.11` (the plain `python` is the Store alias). Use a free port other than 8765 and 8000 for the local server.

## Step 0

1. `cd C:\Claude\Projects\adamlozo-landing`. Check that the working tree is clean and that `main` equals `origin/main` (`4197d9b`). **STOP** if not; report the state.
2. Save this prompt with the **Write tool** to `docs/WEB-FILM-02-prompt.md`. Check first that the path is free.

## Step 1 — The film page tags

In the `<head>` of `films/lady-eleanores-mantle/index.html`, after the Open Graph tags, add:

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Lady Eleanore's Mantle">
<meta name="twitter:description" content="A 21-minute AI film after Nathaniel Hawthorne's &quot;Legends of the Province House&quot; (1838).">
<meta name="twitter:image" content="https://i.ytimg.com/vi/sk1RsAPlbY0/maxresdefault.jpg">
```

Also add `og:image:width` = `1280` and `og:image:height` = `720`. Change no other line.

## Step 2 — The home page description

1. In `index.html`, find `<meta name="description" ...>`. Its current text ends with "…Delayed, Pickman's Model, Xenophysik."
2. Change it to add the film after Pickman's Model: "…Delayed, Pickman's Model, Lady Eleanore's Mantle, Xenophysik."
3. If the home page also has `og:description` or `twitter:description` with the same project list, make the same change there. Report each line before and after.
4. Change no other line.

## Step 3 — Check, commit, publish

1. Check that `maxresdefault.jpg` exists: request `https://i.ytimg.com/vi/sk1RsAPlbY0/maxresdefault.jpg` and report the HTTP status and the image size. **STOP** if it is not 200; report it.
2. Run the site locally. Check that both pages load, with no new console error.
3. Commit on `main` with the message "WEB-FILM-02: X card tags on the film page; film in the home description". Push. Check that `main` equals `origin/main`.
4. Report the Render deploy status, if you can read it. If you cannot, say so; do not guess. Then fetch the live film page and the live home page, and report that the new tags are in the HTML.

## Step 4 — The merged branch

1. Check that `web-film-01` is fully merged into `main` (`git branch --merged main`). **STOP** if it is not.
2. Delete the local branch. If `origin/web-film-01` exists, delete it too. Report what you deleted.
3. Stop the local server.

## Report

Paste back:
- the Step 0 checks;
- the lines added on the film page; the home description before and after;
- the image check; the local checks;
- the commit, the push, the deploy status, the live check;
- the branches deleted;
- any problem, with no workaround.
