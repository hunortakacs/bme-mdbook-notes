# notes

Study books for university classes, generated from lecture material with Claude Code. One mdBook per class, updated as new material arrives.

## Layout

```text
<class>/res/     lecture slides, notebooks, exercise sheets (input, never modified)
<class>/book/    the class's mdBook
<class>/_work/   pipeline state: transcripts, coverage, outline, findings, class profile and checks
hub/             the start page that lists every book
.claude/skills/notes/   the skill that does the work
notes-dev/       development notes and regression tests of the skill
```

## Use

- Put new files into `<class>/res/`, then run `/notes <class>` in Claude Code (`/notes` alone updates every class with new material). It shows an outline and asks about anything doubtful before writing, and commits when done.
- Read locally at <http://127.0.0.1:3000/> (systemd user service `notes`).

## Deploy

Cloudflare Pages, connected to this repository:

- build command: `python3 .claude/skills/notes/scripts/build_site.py . site --install .tools`
- output directory: `site`

Every push rebuilds the hub and all books.
