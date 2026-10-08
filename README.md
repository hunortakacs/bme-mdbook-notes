# notes

Study books for university classes, generated from lecture material with Claude Code. One mdBook per class, updated as new material arrives.

## Layout

```text
<class>/res/     lecture slides, notebooks, exercise sheets (input, never modified)
<class>/book/    the class's mdBook
<class>/_work/   pipeline state: transcripts, coverage, outline, findings, class profile and checks
hub/             the start page that lists every book
scripts/         serve and build the site (no Claude Code needed)
.claude/skills/notes/   the skill that writes and updates the books
.claude/notes-dev/      development notes and regression tests of the skill
```

## Use

- Put new files into `<class>/res/`, then run `/notes <class>` in Claude Code (`/notes` alone updates every class with new material). It shows an outline and asks about anything doubtful before writing, and commits when done.
- Read locally: `python3 scripts/hub.py . serve` → <http://127.0.0.1:3000/>. `python3 scripts/hub.py . install-service` runs it as the systemd user service `notes`. Needs mdbook, mdbook-katex, mdbook-mermaid and Python's Pygments.

## Deploy

Cloudflare Pages, connected to this repository:

- build command: `python3 scripts/build_site.py . site --install .tools`
- output directory: `site`

Every push rebuilds the hub and all books.
