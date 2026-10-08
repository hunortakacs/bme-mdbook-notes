# notes skill: development notes

Context for whoever continues developing the skill in `.claude/skills/notes/` (most likely Claude Code). It records what the user asked for, why the design is the way it is, what has been tested, and what is still open. The skill itself does not read this file.

## What the skill is for

The user is a BME student. His university folder is a git repository with one folder per class, short lowercase names (`dekla` = Deklaratív programozás, `mi` = mesterséges intelligencia, `kvantum` = kvantuminformatika, NLP, ...). Each class folder has a `res/` folder that he fills week by week: mostly lecture slide PDFs (Beamer and others), plus any text-based files (notebooks, `.livemd`, `.exs`, `.py`, exercise sheets). For each class the skill maintains one mdBook, "Rust Book style", that he reads from start to finish instead of the slides, updated incrementally when new material arrives.

### Requirements, as agreed with the user

- **Reliability first: no information gets lost.** Preprocessing must notice pictures, diagrams, overlapping animated pictures, animation-step duplicate pages, tables and formulas, because Claude cannot look at every page of several large PDFs.
- **Math**: formulas, whether real text/LaTeX in the PDF or pasted LaTeX images, must end up as proper LaTeX in the book, not images.
- **Figures**: important diagrams must be in the book: copied (cropped) or recreated, recreated only if that can be done reliably.
- **Incremental, merge by topic**: new material is merged into the existing chapters where it belongs; report what changed.
- **Outline first**: on a new class and on every update, show the planned structure and the cut list, wait for OK, then write.
- **Writing**: same information content as the sources but readable: topic-based reading order, each topic once, flowing explanation instead of slide fragments, course terminology kept, in the language of the sources. Where the source wording is already good it may stay. No meta chapters ("start here", cheat sheets).
- **Cut**: admin and grading, installation, tool output dumps, link lists, history asides. The cut list is shown in the outline.
- **Errors in the slides**: simple typos and syntax errors are fixed in place without comment (he explicitly hates "the slide says X but the correct one is Y" notes). Serious errors are brought to him to confirm.
- **Gap filling**: allowed, unmarked, only when needed. "Avoid AI slop, do this when needed, not just for the love of the game."
- **Code**: syntax highlighting everywhere (he needs it). Decide per example whether running it is useful; don't run everything.
- **Refer to code by content, never by position** ("the fourth line" broke once when line numbers were added).
- **Homework is learning material.** An earlier version forbade solving or including graded work; the user dropped that rule ("this is learning material"). Homework files are treated like practice exercises: task text and any solution in `res/` (his own solved homework included) go into the book; Claude still does not write solutions of its own.
- **UI**: line numbers in code blocks, a thin whole-book reading-progress bar (fattens on hover and shows the percentage; he has ADHD and the scrollbar does not show where he is in the book), no programming ligatures (`|>` and `->` must stay two characters), whole-book search. He asked for official/standard mechanisms over home-grown hacks: mdBook's `additional-css`/`additional-js`, built-in search, built-in print page; third-party mdBook preprocessors (KaTeX, Mermaid) were explicitly OK.
- **One entry point for all books**: a hub mdBook that lists the class books, served with all of them by one always-on systemd user service (standard setup, no per-class `mdbook serve`).
- **Repository**: the repo root holds the class folders directly. Everything outside the repository is the user's and is never touched. Nothing may hardcode where the repository or the user's folders are: the skill derives `ROOT` from `${CLAUDE_SKILL_DIR}`, scripts take it as an argument.
- Book language: the sources' language (Hungarian for his classes). The skill's own instructions are in English.

Things he said he will refine later, once he uses it locally: naming, details of the workflow.

## Layout and data flow

```text
.claude/skills/notes/
  SKILL.md                    the coordinator: finds work, runs one class agent per class, asks the user,
                              starts fresh agents, commits; loaded on /notes [class ...]
  references/class-agent.md   the class agent's phases A-D and their report formats
  references/modules.md       class modules: _work/profile.md and executable checks in _work/verify/
  references/audit.md         the chapter audit by a fresh agent
  references/transcribe.md    how to turn flagged units into a faithful transcript; formula check
  references/writing.md       structure, style, cuts, errors, gap filling, code, math, figures, homework
  references/mdbook.md        book layout, Markdown/KaTeX/Mermaid specifics
  scripts/doctor.py           checks installed tools
  scripts/status.py           for the coordinator: which classes have work (hashes only, reads no material)
  scripts/bookmap.py          for planning an update: a map of the book generated from the chapters
  scripts/prepare.py          hashes res/, triages new/changed sources, carries over transcripts
  scripts/pdf_triage.py       the PDF analysis (also: `page` and `crop` subcommands for Claude)
  scripts/cover.py            records unit -> chapter / cut reason in coverage.tsv
  scripts/check.py            all completeness and build checks; --finalize marks sources done
  scripts/new_book.py         creates book/ (book.toml, SUMMARY, theme); --refresh updates the theme;
                              both also copy notes.css into hub/theme/
  scripts/common.py           layout constants, state and coverage I/O, transcript parsing
  assets/theme/               highlight.js bundle, notes.css, notes.js, head.hbs, highlight-languages.json
  assets/katex/               KaTeX 0.16.4 stylesheet and woff2 fonts (math works offline)

scripts/                      in the repository, not the skill: the repo must work without .claude/
  hub.py                      the hub: keeps hub/ (an mdBook listing all books) current, serves / and /<class>/,
                              rebuilds on change, installs the systemd user unit; owns hub/theme/hub.css
  build_site.py               static site for hosting: hub at the root, books under /<class>/
```

Everything a reader or the deploy needs (the books with their copied theme, hub/, scripts/) is outside `.claude/`, so deleting the skill leaves a working repository. The skill only generates and maintains; nothing outside it may import from or read files in `.claude/`.

Per class (`<class>/`): `res/` (the user's input, read-only), `book/` (the mdBook), `_work/` (state.json, coverage.tsv, outline.md, findings.md, profile.md, verify/, sources/<slug>/{extract.json, draft.md, transcript.md, pages/, figures/}, audit/).

The run (since 2026-10-08, see "Scaling" below): the coordinator (the session that got `/notes`) runs `status.py`, then starts one class agent per class with work. Phase A: `prepare.py`, the class agent transcribes small sources itself and lists large ones (`TRANSCRIBE`) and math sources (`FORMULA CHECK`); the coordinator starts fresh agents for those. Phase B: the class agent reads, runs what can be run, writes the outline and returns it with questions; the coordinator asks the user (AskUserQuestion, one question per finding). Phase C: write chapters, `cover.py`, `check.py` (sections 1-7), module upkeep, chapter excerpts for the audit (`AUDIT`); the coordinator starts one auditor per chapter. Phase D: apply the audit, `check.py --finalize`, final report; the coordinator runs `hub.py update` and commits class + hub.

Why a transcript stage between PDF and book: it makes "nothing lost" checkable. Every unit (logical slide) has a transcript section; `coverage.tsv` maps every unit to a chapter or a cut reason; `check.py` fails on any gap and warns about source code lines that do not appear in the mapped chapter.

### File formats

- `state.json`: `sources[relpath] = {slug, sha256, kind (pdf|office|notebook|image|text|unsupported), status (pending|done|failed|skipped), units}`. Renames are detected by hash. `reviewed_lines`: hashes of the check.py section 5 lines that were missing at the last `--finalize` (judged deliberate then, hidden afterwards).
- `coverage.tsv`: `source  unit  title  disposition`; disposition = chapter path(s) relative to `book/src`, comma separated, or `cut: <reason>`, or `a.md,b.md; cut: <what>` for a unit that is used with a part left out (`common.chapters_of`, `common.partial_cut`).
- Text sources: Markdown-like files (`common.MARKDOWN_EXT`: .md, .livemd, .qmd, ...) are split at `#`/`##` headings outside fences into units `s1..sN` (text before the first heading joins s1); fewer than two headings, or a code file, is one unit `all`. `state.json` keeps `sections` (id, title, fingerprint) per text source; a changed file is matched by fingerprint, then by title. An entry without `sections` (prepared before this existed) stays one `all` unit. `.ipynb` notebooks are flattened and split the same way.
- Transcript/draft unit header: `## s12 · p31-33 · Title` (regex in `common.UNIT_HEADER`), then `<!-- status: auto | TODO view pages/p033.png | viewed pages/p033.png | duplicate of <file> <unit> -->` (scripts only test for the `TODO` prefix), `<!-- flags: ... -->`, `<!-- figure: figures/... -->`.
- Unit ids: `sN` = N-th logical slide (matches the printed slide number for Beamer), `sN.k` = variants (animation steps that replaced content), `all` = whole text file.
- `extract.json` meta has `page_hashes` (page text + thumbnail); `prepare.py` marks units whose pages all occur in another source as duplicates (original = done source, else label-grouped, else first by name) and pre-fills `cut: duplicate of …`.
- On a changed PDF, units are matched by `fingerprint` (hash of draft text + thumbnail), finished transcript sections and coverage rows carry over, only changed units become TODO.

## Scaling: contexts, class modules, audit (2026-10-08)

The user asked for the pipeline to keep its quality all semester, for several classes of different sizes, weekly updates, without classes ever mixing in one context. Decisions:

- **One context per class.** The coordinator never reads class material; each class has its own agent, so a run for several classes is several independent contexts, and the coordinator's context grows only by reports. Subagents cannot ask the user (and are not relied on to start agents), so the class agent works in phases A-D and returns fixed-format reports (`PHASE X DONE`, `TRANSCRIBE:`, `FORMULA CHECK:`, `OUTLINE`/`QUESTIONS`, `AUDIT:`, `FINAL REPORT`); the coordinator continues it with SendMessage. The coordinator does all commits, one class at a time (no git index races).
- **Findings go to the user through AskUserQuestion** (the user's explicit preference), one question per finding, recommended option first.
- **The skill stays general; classes grow their own modules** (the user's direction): `_work/profile.md` (terminology, notation, conventions, recurring decisions; read by every agent of that class) and executable checks in `_work/verify/` that `check.py` runs as section 7 under a small contract (`FAIL`/`WARN`/`OK` lines, `_<name>.accepted` for judged differences, files starting with `_` are helpers). Nothing class-specific goes into the skill, not even a reusable runner: another class's agent writes or copies its own. First module: `dekla/_work/verify/iex` (compiles every complete `defmodule`, runs every `iex` block chapter by chapter and compares outputs; 210 inputs, 55 modules, 4 accepted differences; catches a changed output and a syntax error, tested by tampering).
- **Audit by a fresh agent per changed chapter**, against `cover.py excerpt` (only the units that feed the chapter; `--pending` for an extended chapter: only this run's units), so its cost stays at about one chapter plus its new sources however large the book grows. It closes the gap that section 5 checks only code lines and formulas, not prose.
- **Book map instead of chapter digests.** Planning an update should not need the whole book once it is long. Hand-written digests were rejected (they go stale and can mislead, the user's concern); `bookmap.py` generates the map from the chapters every time instead: per chapter the sections, bold (defined) terms, code languages, exercises, feeding units. It is internal (never in the book). On dekla after three lectures: 13 000 words of book, a 10 KB map. The class agent plans with it and then reads the chosen chapters in full.

Not yet tested end to end: a full run through the coordinator and class agents (phases A-D with real agents). The scripts behind it are covered by the regression suite (`Coordination`). Do the next real update (dekla week 4) as that test, and fix what the reports show.

## Hosting (2026-10-08)

The user wants the hub and all books online for free, deployed automatically on push (the user pushes; runs end at the commit). Chosen: **Cloudflare Pages** (free plan, private GitHub repositories, no ads, the user's domain and DNS are already on Cloudflare). Read the Docs was considered: its free tier is for public projects and shows ads. The site is static; nothing runs on a server.

`build_site.py ROOT OUT --install DIR` is the whole build: it downloads static (musl) release binaries of mdbook 0.5.4, mdbook-katex and mdbook-mermaid 0.17.1 into DIR, builds `hub/` into OUT and each `<class>/book` into `OUT/<class>/` exactly as committed (no checks, nothing written to the repo). All links are relative (hub list `dekla/`, the books' home button `../` from the book root, computed in notes.js), so the site also works under a path prefix; `--base` (or `$READTHEDOCS_CANONICAL_URL`) only sets mdBook's 404 page.

Cloudflare Pages project settings (dashboard, Git integration, no config file): framework preset None, build command `python3 scripts/build_site.py . site --install .tools`, output directory `site`, root directory empty. Tested in a clean `ubuntu:22.04` container with only python3 and ca-certificates.

mdbook-katex 0.10.0 has no binary release, and compiling it needs `patch` and a C compiler (a quickjs dependency patches its sources), which a build image may lack. Its `0.10.0-alpha-binaries` release has a static binary; the whole site built with it is byte-identical to the one built with the locally compiled 0.10.0. When mdbook-katex publishes binaries for a release, switch `KATEX` in build_site.py.

## How pdf_triage.py decides

1. **Animation steps**: PDF page labels group pages (Beamer overlays share a label). Labels are used only if consecutive pages share one; otherwise a content heuristic merges page i into i+1 when i's words and ink are contained in i+1. Within a group a step is dropped only if both its words and its ink are contained in a kept later step, so replaced content survives as a variant.
2. **Template**: per-pixel median of up to 48 pages at 800 px width = background, logo, header, footer. Fallback for < 8 pages: dominant colour.
3. **Non-text ink** = differs from template and is outside text-line boxes. Connected components on a 6 px grid, classified as marker (≤ 20 pt: bullets), box/rule (only straight edges: block backgrounds, frames) or figure (textured: drawings, images, arrows). `graphic` flag if any figure component.
4. **Flags**: `math` (math fonts CMMI/CMSY/…, ≥ 2 math Unicode symbols outside monospace spans, superscripts other than footnote/affiliation markers, i.e. a short digit or `*†‡§` that also starts a line further down), `image`, `table` (≥ 2 thin horizontal rules outside images), `layout` (two-column gutter, rotated text), `stacked` (overlapping images; every layer extracted), `encoding` (U+FFFD, private-use chars, Type 3 fonts), `no-text`, `annot`, `variant`.
5. **Text draft**: rows rebuilt from PyMuPDF lines; monospace URLs (matched against the page's link annotations) are joined across line wraps and written as `<url>`, not fenced as code; code detected by font name or by measuring fixed glyph advance; comment lines in a non-mono font are pulled into code blocks; indentation rebuilt from x positions; Beamer's split accents (`˝o` → `ő`) composed; bullets from marker components.

Calibration constants are at the top of `pdf_triage.py` and in `analyse_page` (marker ≤ 20 pt, texture threshold, rule length 0.2·width). They were tuned on the dekla decks and the synthetic deck only.

### Measured results

| Source | Pages | Units | To view | Notes |
|---|---|---|---|---|
| dp26a-fp1ea.pdf (dekla, Beamer) | 136 | 55 | 12 | 52 slides + 3 with replaced-content variants (17 before the math-flag fix) |
| dp26a-fp2ea.pdf | 118 | 49 | 9 | image-only slide (p115) flagged `no-text`; the regex option table flagged `table` |
| dp26a-fp3ea.pdf | 90 | 31 | 5 | |
| synthetic kvantum-ea03.pdf | 14 | 10 | 7 | animated figure kept as s4.1/s4.2 |
| same without page labels + stacked page | 15 | 11 | 8 | heuristic grouping matched the labelled result |

During tuning, the unflagged slides of fp1ea were checked visually on contact sheets: all were plain text or code.

## Versions and third-party parts

- mdBook **0.5.x** (tested 0.5.4). mdBook 0.4 is not supported: mdbook-katex 0.10 needs the 0.5 preprocessor API.
- mdbook-katex **0.10.0**. Its injected CSS link points at KaTeX **0.16.4**; we set `no-css = true` and serve `assets/katex` (0.16.4) via `theme/head.hbs`. If mdbook-katex is upgraded and uses another KaTeX version, update `assets/katex` from `npm pack katex@<version>` (dist/katex.min.css + dist/fonts/*.woff2).
- mdbook-mermaid **0.17.1** (built against mdBook 0.5.0; prints a harmless version warning that check.py filters).
- highlight.js **10.7.3** custom bundle (mdBook ships 10.1.1 without Elixir/Prolog). Rebuild: in `.claude/notes-dev/highlight-bundle/`, `npm i highlight.js@10.7.3 esbuild`, edit `entry.js`, `npx esbuild entry.js --bundle --minify --format=iife --outfile=highlight.js`, copy to `assets/theme/highlight.js`, then `node langs.js > ../../skills/notes/assets/theme/highlight-languages.json` (check.py uses it to warn about unknown fence languages). Requires must stay static (`require('...')` per language), or esbuild fails. Aliases added: `iex`, `ex`, `exs` → elixir; `pl`, `pro` → prolog (this overrides Perl's `pl`).
- PyMuPDF 1.28 (`import pymupdf`, falls back to `fitz`), numpy.

Install on Fedora: `sudo dnf install cargo git`, `cargo install mdbook mdbook-katex mdbook-mermaid --locked`, `python3 -m pip install --user pymupdf numpy`, `~/.cargo/bin` on PATH. `doctor.py` prints the same.

## Status

**Ready to use.** The git repository is the root: the skill in `.claude/skills/notes/`, this folder, and one folder per class created by the user (`<class>/res/`). The hub runs as the systemd user service `notes` on http://127.0.0.1:3000/. The hub is part of the repository: `hub/` holds its mdBook (book.toml, src/, theme/; the user may edit the page outside the `notes:books` markers, whose content hub.py regenerates without dates so it only changes when a book does). The systemd unit is machine-specific, so `install-service` writes it into `~/.config/systemd/user/` with this checkout's absolute paths; it is not in git. Only `hub/book/` is ignored. A run commits `C` and `hub` together after `hub.py update`.

How it was tested:

- **Regression suite** `.claude/notes-dev/test/test_scripts.py` (11 tests, ~12 s, no Claude, no LaTeX): PDF new → changed (only changed units are new work, transcripts and coverage carry over) → renamed → removed; duplicate sources and `--force --view-all --only`; unsupported and image sources; `.pptx` through a stand-in `soffice` and the failure without one; text sources split into sections, partial cuts, `set-many`, missing code reported per section, reviewed lines hidden after `--finalize`, changed and removed sections reported with their chapters; `.ipynb` sections with image outputs; formulas missing from a chapter; `cover.py changed`; the hub (list, routing, redirect, rebuild on change, relative links); `status.py`, `bookmap.py`, `cover.py excerpt` (also `--pending`), the class-verifier hook in check.py section 7, `build_site.py` (layout, base path). Run it after every change to the scripts.
- **End-to-end runs by a fresh Claude** (2026-10-08), each a general-purpose subagent following SKILL.md in a scratch repo, the developing session answering as the user: `kvantum` (synthetic deck + export), `dekla` week 1 (fp1ea, three fp1 notebooks, khf1.exs), `dekla` week 2 as an update (fp2ea, fp2gy, fp2gy-megoldasok). All ended with 0 FAIL and good books; the merge put new material into the existing chapters without seams, and contradictions between weeks became findings. Every SKILL FEEDBACK item from those runs is fixed (see git history of this file for the list).
- **Real decks**: `pdf_triage.py` flags on dp26a-fp1ea/fp2ea/fp3ea and the synthetic deck (table above) were rechecked after each heuristic change.

Not covered by a real file: a real `.pptx`/`.docx` (LibreOffice is not installed here; the conversion path is tested with a stand-in), scanned PDFs, PowerPoint-exported decks.

### Limitations by design

- Automatic figure crops are deliberately tight; transcribe.md has the transcriber check every crop that will be used as an image and re-crop with `pdf_triage.py crop`.
- A variant also appears when a later animation step merely replaces a placeholder (`...` → code): one extra view, nothing lost.
- Slides that show decomposed Unicode on purpose (fp2ea s41) extract with spacing accents; the spot check catches it.
- `check.py` section 5 is a substring check: a changed line is reported, an appended comment is not. Charlist spelling (`'a'`/`~c"a"`) and `#Function<…>` numbers are normalised, formula spacing and `\mathrm`/`\operatorname` too.
- Code with `...` placeholders confuses the highlighter for the rest of the block; harmless.
- Running examples costs effort when the lecture's own module is not in `res/` (examples are retyped from slides); IEx output is captured with `printf … | iex`.
- The hub has no live reload in the browser; a reload shows the rebuilt book (pages are sent with `Cache-Control: no-cache`).

## Testing the skill again

After a change to a script: `python3 .claude/notes-dev/test/test_scripts.py`. After a change to SKILL.md or a reference: an end-to-end run.

End-to-end: make a scratch git repo with `.claude/skills/notes` and `scripts/` copied in and one class folder. For a synthetic class run `.claude/notes-dev/test/make_test_class.sh <folder>` (pdflatex with beamer); for a real one put copies of course files into `<folder>/<class>/res/` (copies only: the user's folders outside the repository are never touched). Prompt for the fresh agent: "You stand in for Claude Code in a test of a skill. The user typed `/notes <class>`. Setup: the university folder is …; the skill is at … (the value of `${CLAUDE_SKILL_DIR}`), `$ARGUMENTS` is `<class>`. Read `.claude/skills/notes/SKILL.md` and follow it exactly. When it says to wait for the user, end your turn with the message you would show. Every time you end a turn, append a SKILL FEEDBACK section: every unclear instruction, script error, false alarm, wrong flag, guess, and disproportionate effort." Answer the outline with SendMessage, then read the book and the feedback. If two runs share a repo, tell each to commit only its class folder.
