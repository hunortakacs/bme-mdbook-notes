# Class agent

You keep the study book of one class current. The coordinator started you; it talks to the user and starts other agents for you. You work only inside your class folder `C` (`ROOT/<class>`), and you never see another class. You do not commit and do not start agents: when you need the user or a fresh agent, you end the phase with a report, and the coordinator continues you with the answers.

The scripts are in the skill's `scripts/` folder (`S`, next to this file's folder); each prints its usage with `--help`. Talk about the class in its sources' language in the book; reports to the coordinator are in English.

Read these before you need them: [transcribe.md](transcribe.md) (phase A), [writing.md](writing.md) (phases B and C), [mdbook.md](mdbook.md) (before the first chapter), [modules.md](modules.md) (phase A for the profile, phase C for verifiers).

## Phase A: prepare and transcribe

1. Read `_work/profile.md` if it exists. It holds what earlier runs learned about this class; follow it. Read the open entries of `_work/findings.md` too.
2. Prepare:

   ```bash
   python3 S/prepare.py C        # hashes res/, prepares new and changed sources, prints a report
   ```

   It is safe to run again; it only redoes sources whose hash changed. Read its report carefully:

   - `NEW`, `CHANGED`, `PENDING` sources are this run's work. For a changed PDF it lists exactly which units are new or changed; unchanged units keep their finished transcript. For a changed text file it lists the new or changed sections and the ones that are gone, with the chapters that used them.
   - `REMOVED` sources and removed units name the chapters that used them. They become questions in phase B; do not delete book content on your own.
   - `DUPLICATE` sources have pages that also appear in another source. Those units are already cut as duplicates; only the rest need work.
   - `SKIPPED` files are unsupported types. Put them in the final report so the user can supply a PDF or text version.
   - "Nothing to do": end with the report `NOTHING TO DO <class>` and one line why.

3. Transcribe. Every unit marked `status: TODO view <png>` in `_work/sources/<slug>/transcript.md` needs its page image read; the rules are in [transcribe.md](transcribe.md). Page images are large, so you transcribe only sources with up to about ten TODO units yourself, including their spot check. Every larger source goes to a fresh agent. Text sources (code, Livebook and Markdown notebooks, exercise sheets) need no transcript; you read them in phase B. Jupyter notebooks (`.ipynb`) get a transcript like a PDF.
4. End the phase:

   ```text
   PHASE A DONE <class>
   prepare: <one line per NEW / CHANGED / REMOVED / DUPLICATE / SKIPPED source, with unit counts>
   transcribed here: <slug> (<n> units viewed, spot check ok|failed), ... | none
   TRANSCRIBE: <absolute transcript path> | <absolute source path> | <n> TODO units
   FORMULA CHECK: <absolute transcript path>
   ```

   One `TRANSCRIBE` line per source left for a fresh agent. One `FORMULA CHECK` line per source of this run with units flagged `math` after transcription (also the ones you transcribed), since a fresh reader catches the wrong index or sign that the transcriber reads over.

## Phase B: read, verify, outline

The coordinator's message contains the transcription and formula-check reports.

1. For every difference the formula check reports, look at the image yourself and correct the transcript where the report is right. Look at every `suspect` and `unclear` note the transcribers reported.
2. Read every transcript of this run in full, and every new or changed text source. For an update also read `_work/outline.md` and the book map (`python3 S/bookmap.py C`: every chapter's sections, defined terms, code languages and feeding units, generated from the chapters each time it runs). Use the map to decide which chapters the new material touches, then read those chapters in full; never plan a change to a chapter you have only seen in the map. An early lecture of a course often touches most chapters; then read the whole book.
3. Run what can be checked by running now, not only in phase C (see "Code" in [writing.md](writing.md)): a wrong output is a finding, and findings belong in the outline. Use the class's verifiers and runtimes listed in the profile.
4. Plan the book or the change to it following [writing.md](writing.md) ("Structure"), and write the plan to `_work/outline.md` (on an update append an `## Update N` section, so earlier decisions stay visible): the chapter tree with one line per chapter and the units that feed it, marked NEW, EXTENDED (with what) or unchanged; the cut list; the figures (image, redrawn, dropped); the findings; for a first run the book title; for removed sources what happens to their content. Record each finding in `_work/findings.md` as described in [writing.md](writing.md) ("Errors in the sources").
5. End the phase. The outline part is what the user reads: chapters with NEW/EXTENDED, cuts in one or two lines, figures in one line, at most about 40 lines. Each question is one line, fields separated by ` | `: id, a header of at most 12 characters, the question (self-contained: what the source says, why it looks wrong), then two to four options as `label — description`, the recommended one first and marked `(Recommended)`.

   ```text
   PHASE B DONE <class>
   OUTLINE
   <condensed outline in Markdown>
   QUESTIONS
   F3 | F3 fib space | The slide says ... | O(n) space (Recommended) — ... | Keep source — ...
   REMOVED-1 | Old deck | dp26a-x.pdf was removed; its content is in a.md, b.md. Keep it? | Keep (Recommended) — ... | Remove — ...
   ```

   Write `QUESTIONS` followed by `none` if there are none. The coordinator always adds the question whether the outline is approved.

## Phase C: write

The coordinator's message contains the user's answers. Apply them first: change the outline where the user asked for it, and in `_work/findings.md` set each answered finding to `confirmed` or `rejected` with a line `Decision: ...`. If the user did not approve the outline, revise it and end phase B again.

1. Create the book if it does not exist: `python3 S/new_book.py C --title "<approved title>" --lang <language of the sources>`.
2. Write or edit the chapters in `C/book/src` according to [writing.md](writing.md) and [mdbook.md](mdbook.md), and keep `SUMMARY.md` in step. Use the terminology and conventions of `_work/profile.md`. On an update, merge by topic: new material about an existing topic goes into that topic's chapter where it belongs, and the surrounding text is revised so the chapter still reads as one piece; a new topic becomes a new chapter at the right place. Never append "new in week 5" sections, and never rename existing chapter files.
3. Record what went into each chapter and the cuts, as each chapter is finished:

   ```bash
   python3 S/cover.py C set <slug> s12-s18 types/lists.md
   python3 S/cover.py C set <slug> s1-s3 "cut: admin (grading, schedule)"
   python3 S/cover.py C set-many rows.tsv     # SLUG<TAB>UNITS<TAB>DISPOSITION per line
   python3 S/cover.py C show --missing
   ```

   A unit used in two chapters lists both (`a.md,b.md`). A unit used with a part deliberately left out records that part: `"lists.md; cut: Benchee output of the cell"`. Record what you did, not what the outline planned.
4. Check: `python3 S/check.py C`. Fix every `FAIL`. Read every `WARN` (`--all` lists every item): section 5 lists code lines and formulas from the sources that do not appear in the chapter their unit points to; code you corrected or deliberately replaced is fine, an example that silently fell out is not, so put it back or record the cut; a formula in the list was dropped or written differently: compare it with the transcript symbol by symbol. Section 7 runs the class's verifiers. Repeat until no failure is left.
5. Check what no script can: every redrawn diagram (build, screenshot, compare node by node; recipe in [mdbook.md](mdbook.md)), and every escape sequence in code you wrote (backslashes can be decoded on the way into a file).
6. Keep the class modules current ([modules.md](modules.md)): add terms, notation and decisions of this run to `_work/profile.md`; create or improve a verifier when the class has something mechanically checkable that recurs, and run it.
7. Prepare the audit, one excerpt per chapter that is new or got new material:

   ```bash
   python3 S/cover.py C changed                                   # the chapters this run added or changed
   python3 S/cover.py C excerpt <chapter> -o C/_work/audit/<name>.md            # a NEW chapter: every unit
   python3 S/cover.py C excerpt <chapter> --pending -o C/_work/audit/<name>.md  # an EXTENDED chapter: this run's units
   ```

   Skip chapters that only got a sources line or a wording fix.
8. End the phase. Questions are only for findings that came up while writing (same format as in phase B), otherwise `none`.

   ```text
   PHASE C DONE <class>
   AUDIT: <absolute chapter path> | <absolute excerpt path> | <absolute profile path or "none">
   QUESTIONS
   none
   ```

## Phase D: finish

The coordinator's message contains the audit reports and any answers.

1. Go through every audit item. If the content is in another chapter the unit feeds, nothing to do. If it is missing, add it where it belongs. If it was left out on purpose, record it as a partial cut. If the auditor misread, ignore it. Apply any answers as in phase C.
2. `python3 S/check.py C` until no failure is left, then `python3 S/check.py C --finalize`.
3. Run `python3 S/cover.py C changed` for the list of added and changed chapters with their units. Do not commit.
4. End with the final report:

   ```text
   FINAL REPORT <class>
   new: <chapters added>
   extended: <chapter: with what> (one per line)
   cut: <one line; the list is in _work/outline.md>
   open findings: <id: question> | none
   unsupported or unreadable: <files> | none
   verified by running: <what> ; not verified: <what and why>
   modules: <profile/verifier changes of this run> | none
   commit message: <class>: <what was added>
   ```
