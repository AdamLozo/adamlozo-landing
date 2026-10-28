# LAND-LG-02 — The Lost Ghost page: link style and main-page meta description

`cd C:\Claude\Projects\adamlozo-landing`

## Decisions this prompt assumes — do not run it otherwise

1. **Link style on the film page:** in `films/the-lost-ghost/index.html`, add a link style for `.about a`, using the site's own tokens:
   - `color: var(--text);`, `text-decoration: none;`, `border-bottom: 1px solid var(--line);`, `padding-bottom: 1px;`, and `transition: color 0.25s ease, border-color 0.25s ease;`
   - On `:hover` and `:focus-visible`: `color: var(--accent);`, `border-color: var(--accent);`, `outline: none;`
   - Change no other style. Do not change the Mantle page.
2. **Main-page meta description:** in `index.html`, add `The Lost Ghost` to the meta description, in the same pattern as the other project names. If the page also has `og:description` and `twitter:description` with the same project list, add it there too. Keep each description under 160 characters if it was under 160 before; if it is then too long, report the text and do not cut other names.
3. Change no other file.

## Step 0 — checks

1. Check that the remote is `AdamLozo/adamlozo-landing`, the branch is `main`, HEAD = `origin/main` (expected `318306a`), and the tree is clean. STOP if not.
2. Save this prompt to `docs/LAND-LG-02-prompt.md` with the Write tool.

## Step 1 — change and check

1. Make the changes of decisions 1 and 2.
2. Serve the site locally. Check that the X link on the film page uses the new style, and that hover changes it to the accent color. Check at 390 px width. Check that there are no console errors.
3. Check both files for unclosed tags.

## Step 2 — push and live check

1. Commit with `git commit -F <msgfile>`. Push, and check that `git ls-remote origin main` = HEAD.
2. Wait up to 5 minutes. Check that the live film page contains the `.about a` style and the live main page contains `The Lost Ghost` in its meta description.

## Stop rules

- STOP and ask on any blocker or tool failure.

## Report

Keep it short: Step 0 results, the changed lines, the new meta description text, the local and live check results, and HEAD after the push.
