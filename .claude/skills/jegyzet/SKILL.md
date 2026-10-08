---
name: jegyzet
description: Builds and incrementally updates an mdBook study book (jegyzet) for a university class from the files in the class's resources folder (lecture slide PDFs, notebooks, code, exercise sheets). Use when the user wants to create, update, extend or rebuild the notes or book of a class, says new material arrived for a class, or names a class folder such as dekla, mi or kvantum together with notes, jegyzet or mdBook.
argument-hint: "[class-folder]"
---

# Jegyzet: one study book per class, updated as material arrives

The user is a university student. Each class has a folder; its `resources/` folder fills up week by week with lecture slides and other material. This skill turns those resources into one mdBook per class that he reads from start to finish instead of the slides, and keeps that book current when resources are added or changed.

Two things matter above all, and every step below serves one of them:

- **Nothing in the sources gets lost.** Every slide and every file ends up either in a chapter or on a cut list with a reason. Scripts track this, so it does not depend on memory.
- **The book is worth reading.** Same information as the sources, reorganised by topic and written as an explanation a student who missed the lecture can follow. No slide fragments, no filler.

Requested class: `$ARGUMENTS`

## Folder layout

```text
<root>/                      git repository (the user's is ~/bme/jegyzet), one folder per class
  hub/                       the entry page listing all books (an mdBook, in git) and jegyzet.service
  dekla/
    resources/               the user's files; never modify these
    book/                    the mdBook: book.toml, src/, theme/   (book/book/ is build output)
    _work/
      state.json             which sources were processed, with their SHA-256
      coverage.tsv           one row per unit: which chapter it went to, or why it was cut
      outline.md             the approved structure of the book
      findings.md            suspected serious errors in the sources, awaiting the user
      sources/<slug>/        per source: draft.md, transcript.md, extract.json, pages/, figures/
      .gitignore             written by prepare.py: pages/ and figures/ stay out of git
```

A *unit* is one logical slide of a PDF (`s12`; `s12.1`, `s12.2` when animation steps replace each other's content), one `#`/`##` section of a Markdown-like text file or notebook (`s1`, `s2`, ... in file order), or a whole file without such headings, such as a code file (`all`). A *slug* is the source's file name in lowercase ASCII.

The scripts live in `${CLAUDE_SKILL_DIR}/scripts`. Each prints its usage with `--help`. Below, `S` stands for that path and `C` for the class folder.

## The run

Work through these steps in order. Steps 3 and 6 are the points where the user decides something; everywhere else, keep going. Talk to the user in the language he uses with you; the book is in the language of the sources.

### 1. Find out what changed

First, if the folder is a git repository and the class folder has uncommitted changes from before this run, commit them before running anything (`git add C && git commit -m "C: állapot frissítés előtt"`), so the run's changes can be reviewed and undone as one diff. Uncommitted changes outside the class folder are not this run's business: leave them alone and never add them to a commit.

```bash
python3 S/doctor.py              # tools present? If something required is missing, tell the user the install line and stop.
python3 S/prepare.py C           # hashes resources, prepares new and changed sources, prints a report
```

If no class was named, look for folders that contain a resources folder, run `prepare.py` on each, and continue with those that report pending work (ask which first if there are several).

`prepare.py` is safe to run again at any time; it only redoes sources whose hash changed. Read its report carefully:

- `NEW`, `CHANGED`, `PENDING` sources are this run's work. For a changed PDF it lists exactly which units are new or changed; unchanged units keep their finished transcript. For a changed text file it lists the new or changed sections and the ones that are gone, with the chapters that used them.
- `REMOVED` sources and removed units name the chapters that used them. Bring these to the user in step 3; do not delete book content on your own.
- `DUPLICATE` sources have pages that also appear in another source (a re-export, a combined deck). Those units are already marked and cut as duplicates; only the remaining units need work.
- `SKIPPED` files are unsupported types. Tell the user in the final report so he can supply a PDF or text version.
- "Nothing to do" means the book is current: say so and stop.

### 2. Transcribe: make every unit readable as text

Slides carry information that text extraction misses: formulas, diagrams, tables, pictures, multi-column layouts, pasted formula images. `prepare.py` flags every unit where that can be the case and marks it `status: TODO view <png>` in `_work/sources/<slug>/transcript.md`. Units marked `auto` are plain text or code: their text is complete, but its form is raw (code fences have no language, line breaks follow the slide), which the writing step tidies.

Turn every TODO unit into a complete transcript by looking at its rendered page. The rules are in [references/transcribe.md](references/transcribe.md); read it before the first unit.

Page images are large, so protect the main context: give each source with more than about ten TODO units to its own subagent (general-purpose), several in parallel when there are several sources. The subagent prompt must give the absolute paths of the transcript, the source file and `references/transcribe.md`, and tell it to follow that file and report back counts, suspected errors and unclear spots. Smaller sources you do yourself.

When a source has units flagged `math`, run the independent formula check described at the end of `transcribe.md` after transcription. A wrong index or sign in a formula is the most damaging kind of error this pipeline can make, and the one a second look reliably catches.

Text sources (code, Livebook and Markdown notebooks, exercise sheets) need no transcript. You read them directly in the next step. Jupyter notebooks (`.ipynb`) get a transcript like a PDF; only their sections with image outputs are TODO.

### 3. Outline, then wait for approval

Read every transcript of this run in full, and every text source. Run the code examples that show or claim an output now (see "Code" in `writing.md`), not only in step 5: a wrong output is a finding, and findings belong in the outline. For an update also read `_work/outline.md`, `book/src/SUMMARY.md`, open entries in `_work/findings.md`, and the chapters the new material touches (`cover.py C chapter <file>` shows what already feeds a chapter). An early lecture of a course often touches most chapters; then read the whole book.

Then plan the book, or the change to it, following [references/writing.md](references/writing.md) (section "Structure"), and write the plan to `_work/outline.md` (on an update, append an `## Update N` section, so earlier decisions stay visible):

- the chapter tree, each chapter with one line on its content and the units that feed it, marked NEW, EXTENDED (say with what) or unchanged;
- the cut list: what is left out and why;
- figures: which are kept as images, which are redrawn, which are dropped;
- findings: anything in the sources that looks seriously wrong (see "Errors in the sources" in `writing.md`), each with what the source says, why it looks wrong, and what you propose;
- for a first run, the book title; for removed sources, what happens to the content they fed.

Show the user a condensed version of this outline in the conversation (chapters, cuts, figures, findings as yes/no questions; the full plan stays in the file) and ask for approval or changes. This is the cheap moment to change direction, so do not write chapters before he answers. If he has said in this conversation to proceed without asking, or nobody is there to answer, proceed with your best plan and say so in the final report.

### 4. Write

Create the book if it does not exist:

```bash
python3 S/new_book.py C --title "<approved title>" --lang hu     # language of the sources
```

Write or edit the chapters in `C/book/src` according to [references/writing.md](references/writing.md), and keep `SUMMARY.md` in step. Markdown features, file naming, math, diagrams and images are in [references/mdbook.md](references/mdbook.md).

On an update, merge by topic. New material about an existing topic goes into that topic's chapter, at the place where it belongs, and the surrounding text is revised so the chapter still reads as one piece. A new topic becomes a new chapter at the right position in the reading order. Never append "new in week 5" sections, and never rename existing chapter files (links, coverage and git history depend on the names).

As each chapter is finished, record what went into it, and record the cuts:

```bash
python3 S/cover.py C set <slug> s12-s18 types/lists.md
python3 S/cover.py C set <slug> s1-s3 "cut: admin (grading, schedule)"
python3 S/cover.py C set-many rows.tsv     # many at once: SLUG<TAB>UNITS<TAB>DISPOSITION per line
python3 S/cover.py C show --missing        # what is still unassigned
```

A unit used in two chapters lists both (`a.md,b.md`). A unit that is used but has a part deliberately left out records that part: `"lists.md; cut: Benchee output of the cell"`. Record what you actually did, not what the outline planned.

### 5. Verify

```bash
python3 S/check.py C
```

Fix every `FAIL`. Read every `WARN` (`--all` lists every item instead of the first 20): section 5 lists code lines and formulas from the sources that do not appear in the chapter their unit points to. Code you corrected or deliberately replaced is fine; an example that silently fell out is not, so put it back or record the cut. A formula in the list was dropped or written differently: compare it with the transcript symbol by symbol, and fix the chapter unless the difference is notation only. What is still listed at `--finalize` counts as judged and is not shown again. Repeat until no failure is left.

Then check what the script cannot:

- Code examples you decided to run (see "Code" in `writing.md`): run them and make the book show the real output.
- Every redrawn diagram: build, take a screenshot of the page (recipe in `mdbook.md`, "Diagrams"), and compare it with the original node by node.

When everything holds:

```bash
python3 S/check.py C --finalize      # marks the sources as done in state.json
```

### 6. Report and commit

Refresh the list of books on the entry page (`python3 S/hub.py <root> update`), then commit the class folder and the hub together (`git add C hub && git commit`), message in the form `C: <what was added>`, in the language of the book. Do not push.

Tell the user, briefly:

- what is new: chapters added, chapters extended and with what (`cover.py C changed`, run before the commit, lists every added or changed chapter with the units that feed it);
- what was cut (one line, pointing to the outline for the list);
- findings that need his decision, each as a question he can answer with yes or no;
- unsupported or unreadable material;
- which code examples were verified by running and which were not;
- how to read it: `http://127.0.0.1:3000/C/` (see "Reading the books"; search with `s`, the whole book on one page under the print icon).

## Reading the books

All books are served together by the hub: `http://127.0.0.1:3000/` lists them, `/<class>/` is a book, and every book has a home button back to the list. It runs as the systemd user service `jegyzet` and rebuilds a book within seconds of any change, so a finished run needs no extra step. Check it with `systemctl --user is-active jegyzet`. If it is not installed, install it once with `python3 S/hub.py <root> install-service` (the user asked for this setup; tell him the address afterwards). The hub is an ordinary mdBook in `<root>/hub/`, kept in git with its unit file `hub/jegyzet.service`; `hub.py` only rewrites the list between the `jegyzet:books` markers in `hub/src/index.md`, everything else there is the user's. `mdbook serve C/book --open` still works for a single book.

## Rules that hold in every step

- **Sources are read-only.** Work happens in `book/` and `_work/`.
- **Write in the language of the sources**, with the course's own terminology.
- **Verify claims against the sources' own worked examples.** If a rule you are about to write contradicts an example in the material, the example usually wins; look again.
- **Do not mark anything done that was not done.** A unit is `viewed` only after its page image was read; a code example is "verified" only if it ran.

## Reference files

- [references/transcribe.md](references/transcribe.md): how to transcribe flagged units, handle figures and formulas, and run the formula check. Read in step 2.
- [references/writing.md](references/writing.md): structure, style, cuts, errors, gap filling, code, exercises. Read in step 3 and keep to it in step 4.
- [references/mdbook.md](references/mdbook.md): file layout, SUMMARY, Markdown, KaTeX and Mermaid specifics, images, theme. Read before writing the first chapter.
