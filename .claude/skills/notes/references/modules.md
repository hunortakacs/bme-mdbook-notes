# Class modules: the profile and the verifiers

The skill is general. Everything that is specific to one class lives in that class's `_work/` folder, is versioned with it, and is created and improved by that class's agent as the semester goes on. Two kinds of module exist.

## `_work/profile.md`: what this class's book has to stay consistent with

Every agent working on the class reads it first (class agent, writers, auditors). It holds only what a fresh agent could not see from one chapter and would otherwise get wrong or inconsistent:

- **Course**: full name, language of the sources and the book, what the course covers (two or three lines).
- **Terminology**: the course's terms as the book uses them, one per line: term, English term if the course gives one, how it is used, and a note where the course coins or translates unusually (`jobbrekurzió (tail recursion): also called terminális/farokrekurzió; the book uses jobbrekurzió`).
- **Notation and code conventions**: formula notation, code language names, the runtime version used for verification, how outputs are shown (which version's format), what is fixed silently (old syntax the slides use).
- **Recurring decisions**: rules that follow from the user's answers and apply again next week (each with the finding id), and standing preferences for this class.
- **Verifiers**: one line per verifier in `verify/`: what it checks, what it does not.

Keep it short (a page or two) and current: when a run adds a term, a convention or a decision, update the profile in the same run. Remove what stopped being true. It is a working file, not part of the book.

## `_work/verify/`: checks that run on every `check.py`

A verifier is an executable file that checks the book mechanically for something specific to this class: code examples that show an output (run them and compare), code that must compile, queries with answers, numeric results of formulas, cross-references the course uses. `check.py` runs every executable file in `verify/` whose name does not start with `.` or `_` (section 7), so a verifier protects the book in every later run, also against mistakes made while editing old chapters.

Create one when two things hold: the class has such checkable content that keeps coming (not a one-off), and the tool it needs is installed on this machine. If the tool is missing, do not install anything: name it and the install line in the final report.

### Contract

- Called as `verify/<name> <class folder>` with the class folder as working directory. Any language; a short shell or Python wrapper is fine. Helper files and data that are not to be run start with `_` or are not executable.
- Reads `book/src` (and anything in `_work/`). Writes nothing in `book/`; a cache, if needed, goes to `verify/.cache/` (not in git).
- Prints one line per finding: `FAIL <chapter>: <what>` for something wrong in the book, `WARN <chapter>: <what>` for something to judge, and at the end `OK <summary>` (what was checked, how many items). Exit code 0, unless the verifier itself cannot work (then non-zero, with the reason).
- No network, no randomness, deterministic; finishes within a few minutes.
- A difference that was judged fine (an abbreviated error message on a slide, an output that depends on the machine) is recorded in a data file next to the verifier, `verify/_<name>.accepted`, one line per item: a key that changes whenever the checked code or the expected output changes (a short hash of both), a tab, and the reason. Accepted items are not reported again. Never accept a difference in substance: that is a finding for the user.

### Lifecycle

1. Write it in the run where the need appears, and run it on the whole current book.
2. Judge every report: fix the book, or accept the item with a reason. A verifier that floods the report with false alarms is fixed, not ignored.
3. Note it in the profile.
4. When it misses an error or raises a false alarm in a later run, improve it in that run.

A verifier is specific to its class. If another class needs something similar, its agent writes its own (it may start from a copy); nothing class-specific moves into the skill.
