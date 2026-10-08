---
name: notes
description: Builds and incrementally updates an mdBook study book (notes, jegyzet) for a university class from the files in the class's res folder (lecture slide PDFs, notebooks, code, exercise sheets). Use when the user wants to create, update, extend or rebuild the notes or book of a class, says new material arrived for a class, or names a class folder such as dekla, mi or kvantum together with notes, jegyzet or mdBook.
argument-hint: "[class-folder ...]"
---

# Notes: one study book per class, updated as material arrives

The user is a university student. Each class has a folder; its `res/` folder fills up week by week with lecture slides and other material. This skill turns that material into one mdBook per class that the user reads from start to finish instead of the slides, and keeps that book current when files are added to `res/` or changed, all semester long, for several classes.

Two things matter above all:

- **Nothing in the sources gets lost.** Every slide and every file ends up either in a chapter or on a cut list with a reason. Scripts track this, so it does not depend on memory.
- **The book is worth reading.** Same information as the sources, reorganised by topic and written as an explanation a student who missed the lecture can follow. No slide fragments, no filler.

Requested classes: `$ARGUMENTS` (empty: every class that has work).

## Who does what

Quality must not depend on how much material has piled up or how many classes there are, so the work is split by context:

- **You are the coordinator.** You never read class material: no transcripts, sources, chapters or page images. Your context holds only short reports, outlines and the user's answers. You talk to the user, start agents, and make every git commit.
- **One class agent per class** does that class's work, in a context of its own, so classes never mix. Its instructions are [references/class-agent.md](references/class-agent.md). It works in phases and stops at each phase boundary with a fixed-format report, because only you can ask the user and start fresh agents. You continue it with SendMessage (its context stays intact).
- **Fresh single-purpose agents** do work that needs a clean context or an independent eye: transcribing a large source, checking formulas against the page images, auditing a written chapter against its sources. You start them from the class agent's report; they work on one class only and report back to you, and you pass the report on to that class's agent.
- **The class's own modules** carry what is specific to a class: `_work/profile.md` (terminology, notation, conventions, recurring decisions) and executable checks in `_work/verify/`. The class agent creates and improves them over the semester; `check.py` runs the checks. See [references/modules.md](references/modules.md). The skill itself stays general.

The scripts live in `/home/hunor/bme/notes/.claude/skills/notes/scripts` (`S` below); each prints its usage with `--help`. The repository root is `/home/hunor/bme/notes` (`ROOT`).

## The run

### 1. Find the work

```bash
python3 S/doctor.py               # tools present? If something required is missing, tell the user the install line and stop.
python3 S/status.py ROOT [CLASS ...]
```

`status.py` hashes `res/` only and reads nothing else. A class marked `WORK` has new, changed, removed or unfinished sources. If a requested class is current, say so. If nothing has work, say so and stop. If a class shows `uncommitted changes` from before this run, commit them first (`git add C && git commit -m "C: state before update"`), so the run's changes can be reviewed and undone as one diff. Uncommitted changes outside class folders are not this run's business: never add them to a commit.

### 2. Start one class agent per class with work

Start them in parallel (general-purpose agents, in the background), one per class, named `notes-<class>`, with this prompt:

> You are the class agent for the class `<class>` in `ROOT/<class>`. Read `S/../references/class-agent.md` and follow it exactly, starting with phase A. Work only inside `ROOT/<class>`. Do not commit, and do not start agents of your own. End every phase with the report the instructions define.

### 3. Run the phases

Each class agent ends a phase with a report that starts `PHASE <X> DONE <class>` (or `NOTHING TO DO <class>`). React per class, and keep each class's reports, questions and agents separate: never pass one class's material to another class's agent.

- **`TRANSCRIBE` and `FORMULA CHECK` lines** (phase A): start one fresh agent per `TRANSCRIBE` line with the transcription prompt below, in parallel. When all transcriptions of the class are back, start one fresh agent per `FORMULA CHECK` line with the formula-check prompt. Then continue the class agent with `Phase B.` followed by every report verbatim.
- **`OUTLINE` and `QUESTIONS`** (phase B, sometimes C): show the user the condensed outline as text, labelled with the class. Then ask with the AskUserQuestion tool: one question per finding (`Q` line), up to four per call, the recommended option first, and, after phase B, a last question whether the outline is approved. Never ask questions of two classes in the same call. Continue the class agent with `Phase C.` (or the phase it asked for) and the answers verbatim, including any free text. If the user said in this conversation to proceed without asking, answer with the recommended options and say so in the final report.
- **`AUDIT` lines** (phase C): start one fresh agent per line with the audit prompt below, in parallel. Continue the class agent with `Phase D.` and every audit report verbatim.
- **`FINAL REPORT`** (phase D): the class is done. Commit it (step 4).

Transcription prompt (one source):

> Transcribe the flagged units of one source so the transcript is complete and faithful. Transcript: `<transcript path>`. Source (read-only): `<source path>`. Rules: `S/../references/transcribe.md`; read it in full first, follow it exactly, including the spot check. Do not run the formula check, and do not touch any other file. Report back: units viewed, every `suspect` and `unclear` note with its unit, figures you recommend keeping as images, crops you replaced, the spot-check result.

Formula-check prompt (one transcript): the instruction in the last section of [references/transcribe.md](references/transcribe.md), with the transcript path.

Audit prompt (one chapter): the instruction in [references/audit.md](references/audit.md), with the paths from the `AUDIT` line.

### 4. Commit and report

When a class agent has sent its `FINAL REPORT`, refresh the list of books and commit that class and the hub together, one class at a time:

```bash
python3 S/hub.py ROOT update
git add <class> hub && git commit -m "<class>: <what was added>"     # message in English; do not push
```

When every class is done, give the user each class's final report, shortened to what the user needs: what is new or changed and where to reread, what was cut (one line), open findings, unsupported files, which code was verified by running, how to read it (`http://127.0.0.1:3000/<class>/`; search with `s`, the whole book on one page under the print icon).

## Reading the books

All books are served together by the hub: `http://127.0.0.1:3000/` lists them, `/<class>/` is a book, and every book has a home button back to the list. It runs as the systemd user service `notes` and rebuilds a book within seconds of any change. Check it with `systemctl --user is-active notes`; if it is not installed, install it once with `python3 S/hub.py ROOT install-service` and tell the user the address. The hub is an ordinary mdBook in `ROOT/hub/`, kept in git with its unit file `hub/notes.service`; `hub.py` only rewrites the list between the `notes:books` markers in `hub/src/index.md`.

## Folder layout

```text
ROOT/                        git repository, one folder per class
  hub/                       the entry page listing all books (an mdBook, in git) and notes.service
  <class>/
    res/                     the user's files (lecture slides, notebooks, code); never modified
    book/                    the mdBook: book.toml, src/, theme/   (book/book/ is build output)
    _work/
      state.json             which sources were processed, with their SHA-256
      coverage.tsv           one row per unit: which chapter it went to, or why it was cut
      outline.md             the approved structure of the book, one section per run
      findings.md            suspected serious errors in the sources and the user's decisions
      profile.md             the class's terminology, conventions and recurring decisions
      verify/                the class's own executable checks, run by check.py
      sources/<slug>/        per source: draft.md, transcript.md, extract.json, pages/, figures/
      audit/                 chapter excerpts for the auditors (not in git)
```

A *unit* is one logical slide of a PDF (`s12`; `s12.1`, `s12.2` when animation steps replace each other's content), one `#`/`##` section of a Markdown-like text file or notebook (`s1`, `s2`, ...), or a whole file without such headings (`all`). A *slug* is the source's file name in lowercase ASCII.

## Rules that hold everywhere

- **Sources are read-only.** Work happens in `book/` and `_work/`.
- **One class per context.** No agent ever works on two classes, and no report of one class is shown to another class's agent.
- **The user decides what is serious.** Every finding and every change of direction goes to the user through AskUserQuestion.
- **Do not mark anything done that was not done.** A unit is `viewed` only after its page image was read; a code example is "verified" only if it ran.
- **The skill stays general.** Anything specific to one class (a language runtime, a notation, a term) belongs in that class's profile or verifiers, never in the skill's files.
