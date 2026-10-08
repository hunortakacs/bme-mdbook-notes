# jegyzet skill: development notes

Context for whoever continues developing the skill in `.claude/skills/jegyzet/` (most likely Claude Code). It records what the user asked for, why the design is the way it is, what has been tested, and what is still open. The skill itself does not read this file.

## What the skill is for

The user is a BME student. His university folder is a git repository with one folder per class, short lowercase names (`dekla` = Deklaratív programozás, `mi` = mesterséges intelligencia, `kvantum` = kvantuminformatika, NLP, ...). Each class folder has a `resources/` folder that he fills week by week: mostly lecture slide PDFs (Beamer and others), plus any text-based files (notebooks, `.livemd`, `.exs`, `.py`, exercise sheets). For each class the skill maintains one mdBook, "Rust Book style", that he reads from start to finish instead of the slides, updated incrementally when new material arrives.

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
- **Homework is learning material.** An earlier version forbade solving or including graded work; the user dropped that rule ("this is learning material"). Homework files are treated like practice exercises: task text and any solution in the resources (his own solved homework included) go into the book; Claude still does not write solutions of its own.
- **UI**: line numbers in code blocks, a thin whole-book reading-progress bar (fattens on hover and shows the percentage; he has ADHD and the scrollbar does not show where he is in the book), no programming ligatures (`|>` and `->` must stay two characters), whole-book search. He asked for official/standard mechanisms over home-grown hacks: mdBook's `additional-css`/`additional-js`, built-in search, built-in print page; third-party mdBook preprocessors (KaTeX, Mermaid) were explicitly OK.
- Book language: the sources' language (Hungarian for his classes). The skill's own instructions are in English.

Things he said he will refine later, once he uses it locally: naming, details of the workflow.

## Layout and data flow

```text
.claude/skills/jegyzet/
  SKILL.md                    the workflow (6 steps); loaded on /jegyzet <class>
  references/transcribe.md    how to turn flagged units into a faithful transcript; formula check
  references/writing.md       structure, style, cuts, errors, gap filling, code, math, figures, homework
  references/mdbook.md        book layout, Markdown/KaTeX/Mermaid specifics
  scripts/doctor.py           checks installed tools
  scripts/prepare.py          hashes resources, triages new/changed sources, carries over transcripts
  scripts/pdf_triage.py       the PDF analysis (also: `page` and `crop` subcommands for Claude)
  scripts/cover.py            records unit -> chapter / cut reason in coverage.tsv
  scripts/check.py            all completeness and build checks; --finalize marks sources done
  scripts/new_book.py         creates book/ (book.toml, SUMMARY, theme); --refresh updates the theme
  scripts/common.py           layout constants, state and coverage I/O, transcript parsing
  assets/theme/               highlight.js bundle, jegyzet.css, jegyzet.js, head.hbs, highlight-languages.json
  assets/katex/               KaTeX 0.16.4 stylesheet and woff2 fonts (math works offline)
```

Per class (`<class>/`): `resources/` (read-only), `book/` (the mdBook), `_work/` (state.json, coverage.tsv, outline.md, findings.md, sources/<slug>/{extract.json, draft.md, transcript.md, pages/, figures/}).

The run: `prepare.py` → Claude transcribes every unit marked `status: TODO view <png>` by reading the PNG (subagents per large source; independent formula-check subagent) → outline, wait for approval → write chapters, record coverage with `cover.py` → `check.py` until no FAIL → `check.py --finalize` → commit.

Why a transcript stage between PDF and book: it makes "nothing lost" checkable. Every unit (logical slide) has a transcript section; `coverage.tsv` maps every unit to a chapter or a cut reason; `check.py` fails on any gap and warns about source code lines that do not appear in the mapped chapter.

### File formats

- `state.json`: `sources[relpath] = {slug, sha256, kind (pdf|office|notebook|image|text|unsupported), status (pending|done|failed|skipped), units}`. Renames are detected by hash. `reviewed_lines`: hashes of the check.py section 5 lines that were missing at the last `--finalize` (judged deliberate then, hidden afterwards).
- `coverage.tsv`: `source  unit  title  disposition`; disposition = chapter path(s) relative to `book/src`, comma separated, or `cut: <reason>`.
- Transcript/draft unit header: `## s12 · p31-33 · Title` (regex in `common.UNIT_HEADER`), then `<!-- status: auto | TODO view pages/p033.png | viewed pages/p033.png | duplicate of <file> <unit> -->` (scripts only test for the `TODO` prefix), `<!-- flags: ... -->`, `<!-- figure: figures/... -->`.
- Unit ids: `sN` = N-th logical slide (matches the printed slide number for Beamer), `sN.k` = variants (animation steps that replaced content), `all` = whole text file.
- `extract.json` meta has `page_hashes` (page text + thumbnail); `prepare.py` marks units whose pages all occur in another source as duplicates (original = done source, else label-grouped, else first by name) and pre-fills `cut: duplicate of …`.
- On a changed PDF, units are matched by `fingerprint` (hash of draft text + thumbnail), finished transcript sections and coverage rows carry over, only changed units become TODO.

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
- highlight.js **10.7.3** custom bundle (mdBook ships 10.1.1 without Elixir/Prolog). Rebuild: in `jegyzet-dev/highlight-bundle/`, `npm i highlight.js@10.7.3 esbuild`, edit `entry.js`, `npx esbuild entry.js --bundle --minify --format=iife --outfile=highlight.js`, copy to `assets/theme/highlight.js`, then `node langs.js > ../../.claude/skills/jegyzet/assets/theme/highlight-languages.json` (check.py uses it to warn about unknown fence languages). Requires must stay static (`require('...')` per language), or esbuild fails. Aliases added: `iex`, `ex`, `exs` → elixir; `pl`, `pro` → prolog (this overrides Perl's `pl`).
- PyMuPDF 1.28 (`import pymupdf`, falls back to `fitz`), numpy.

Install on Fedora: `sudo dnf install cargo git`, `cargo install mdbook mdbook-katex mdbook-mermaid --locked`, `python3 -m pip install --user pymupdf numpy`, `~/.cargo/bin` on PATH. `doctor.py` prints the same.

## Status

Tested, script by script: `pdf_triage.py` on the three dekla PDFs and the synthetic deck; `prepare.py`, `cover.py`, `check.py`, `new_book.py`, `doctor.py` on a dekla class folder; a demo book with KaTeX (inline, display, `\tag`, matrices, formula in a table), Mermaid, callouts, `<details>`, images, footnotes, line numbers and the progress bar, rendered in Chromium in light and navy themes and at phone width.

**End-to-end runs by a fresh Claude (2026-10-08).** Three runs, each a general-purpose subagent following SKILL.md in a scratch git repo, with the developing session answering the outline as the user:

1. `kvantum` (synthetic deck + label-less export): book with 2 chapters, 0 FAIL. Caught the deliberately wrong circuit as a finding; the pasted formula image became LaTeX.
2. `dekla` first run (fp1ea, fp1gy, fp1gyfel, fp1gy-megoldasok, khf1.exs): 13 pages, 0 FAIL. Running the Elixir examples surfaced 5 real errors in the course material (all confirmed); the paradigm tree was redrawn in Mermaid and compared by screenshot.
3. `dekla` update (fp2ea, fp2gy, fp2gy-megoldasok): 6 new pages, 8 chapters extended, file names kept, no seams; a week-2 lecture contradicting the week-1 text became a finding and the old rule was rewritten in place after confirmation.

Every run ended with a SKILL FEEDBACK list; what came out of them is fixed: the duplicate-source detection, the `--force`-on-pending bug, `--only`, the math-flag and URL false alarms, side-by-side REPL detection, `check.py` covering text sources and remembering reviewed lines, `cover.py set-many`, the screenshot recipe, and about twenty instruction clarifications in SKILL.md and the references.

Also untested: `office` sources (pptx/docx via LibreOffice), `.ipynb` flattening, image sources, the CHANGED-source carry-over path on real data, rename detection, scanned PDFs, PowerPoint-exported decks, a run in the main session (all three ran as subagents; a subagent may not Write report-like `.md` files, the dekla agent used a heredoc for `findings.md`).

### Known issues and ideas

- **Partial cuts are not tracked.** A unit (slide or whole text file) is either used or cut. A used slide with one cut sentence, or a notebook with cut cells (Benchee dumps, setup cells), records the partial cut only in the outline. A finer coverage model (sections of text sources, `used + cut:` on one unit) would close this.
- **No formula comparison helper.** Step 5 asks to compare chapter formulas with the transcript; the agents grepped LaTeX strings by hand. A script listing each `math` unit's formulas next to the chapter's would make it reliable.
- **Running examples is laborious** when the lecture's own module file is not in resources (examples retyped from slides) and when IEx output must be captured (`printf … | iex`).
- Automatic figure crops are deliberately tight; transcribe.md asks to check only crops that will be used as images.
- Variants also appear when a later step merely replaces a placeholder (`...` → real code). That costs a view, loses nothing.
- Slides deliberately showing decomposed Unicode (fp2ea s41) extract with spacing accents; the spot check catches it, which is its job.
- The progress-bar label sits over the print icon while shown (only on hover near the top).
- `check.py` section 5 is a substring heuristic: an appended comment still matches, a changed line is reported. Lines judged at `--finalize` are hidden afterwards (`reviewed_lines`).
- Code with `...` placeholders breaks highlighting for the rest of the block; harmless.
- Possible improvements: a `check.py` option to list chapters touched since the last commit for the final report; a contact-sheet helper for the spot checks.

## Testing the skill again

`jegyzet-dev/test/make_test_class.sh <folder>` builds the synthetic `kvantum` class (needs pdflatex with beamer; no `standalone` class needed any more). For a real class, copy a few of the user's dekla files into `<folder>/dekla/resources/`, with `.claude/skills/jegyzet` copied next to them and the folder made a git repo.

Prompt for the fresh agent: "You stand in for Claude Code in a test of a skill. The user typed `/jegyzet <class>`. Setup: the university folder is …; the skill is at … (the value of `${CLAUDE_SKILL_DIR}`), `$ARGUMENTS` is `<class>`. Read `.claude/skills/jegyzet/SKILL.md` and follow it exactly. When it says to wait for the user, end your turn with the message you would show. Every time you end a turn, append a SKILL FEEDBACK section: every unclear instruction, script error, false alarm, wrong flag, guess, and disproportionate effort." Answer the outline via SendMessage, then read the book and the feedback. If two runs share a repo, tell each to commit only its class folder.

Useful next runs: a CHANGED source (edit a lecture PDF that is already done), a removed source, a pptx (needs LibreOffice), an `.ipynb`, and a third dekla week to see how the book holds up as it grows.
