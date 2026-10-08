# Writing the book

## Who reads it and why

A student who was not at the lecture, reading the book from the first page to the last to learn the subject well enough to solve the exercises and pass the exam on his own. Slides are prompts for a lecturer; without the lecturer they are fragments. The book supplies the connecting explanation the lecturer would have given, and nothing beyond what the course teaches.

The measure: after reading a chapter, the student knows everything the corresponding slides contain, and understood it on the first read.

## Contents

- Structure
- Style
- What to cut
- Errors in the sources
- Filling gaps
- Code
- Math
- Figures
- Exercises and homework
- Sources line
- Updating an existing book

## Structure

Order the book by topic, in the order a learner needs the topics, which is often not the order of the lectures. Lectures revisit topics, introduce something in passing and define it two weeks later, and repeat material as recap. In the book each topic appears once, at one place, complete: gather everything the sources say about it from all lectures, notebooks and exercise sheets.

- A concept is explained before it is used. If the sources use something early and define it late, move the definition forward.
- Chapters follow the Rust Book pattern: a chapter per major topic, sub-chapters for its parts, each a page of its own that can be read in one sitting. Titles are plain names of the topic in the source language ("Mintaillesztés", not "A mintaillesztés rejtelmei").
- No chapters about the book itself and no extra study aids: no "how to use this book", no "start here", no cheat sheet, no recap chapter, no glossary, unless the user asks. They repeat content and he reads in order anyway.
- An introduction page holds only what orients the reader in the subject (what the course is about, in a few sentences), not a preview of the chapters; the sidebar shows those. It may be very short.

## Style

Write an explanation, in full sentences and paragraphs, the way a good textbook does. Carry the same information as the slides; do not carry their form.

- Do not copy slide text bullet by bullet, and do not paraphrase it bullet by bullet either. Work out what the slide is saying and say that. Where the source's own wording is already a clear sentence or a precise definition, keep it.
- Keep the course's terminology exactly, including the terms the lecturer coined or translated in an unusual way. Those are the words on the exam. Give the English term once in parentheses when the source does.
- Definitions and rules stay precise. Readable does not mean loose.
- Use a list when the content is a list (steps, alternatives, properties), a table when it is a comparison along the same attributes, and prose for everything that has a "because" in it.
- Lead with the point. One idea per paragraph. Short sentences where the material is hard.
- Explain an example before or right after showing it: what to look at and what it demonstrates. Never refer to a place in an example by counting ("the fourth line", "the second expression"): name the thing ("the `fac/1` clause with the guard", "the call to `Enum.map/2`"). Line numbers are displayed in the book and positions shift when text is edited.

What to leave out of the prose, because it adds length and no information:

- announcements of what a chapter will do and summaries of what it just did;
- motivation speeches, praise of the topic, rhetorical questions;
- hedges and fillers ("fontos megjegyezni, hogy", "érdemes tudni", "it is worth noting");
- remarks about the slides or the lecture ("ahogy az előadáson láttuk", "a dián szereplő");
- emphasis on everything. Bold is for a term at the point where it is defined.

## What to cut

Leave out, and record each on the cut list with its reason:

- course administration: grading, deadlines, schedules, requirements, contact details, room numbers;
- installation and environment setup, editor recommendations, tool version notes;
- raw tool output with no teaching content (help screens, project generator logs, long listings);
- link collections and reading lists (a link that the text needs stays, where it is needed);
- history and trivia asides, quotes, jokes, title slides, tables of contents, "questions?" slides;
- recaps of earlier lectures and summary slides (the content is already in the book; check that every statement really is, and keep any that appears only there).

Everything else stays. When unsure whether something is content, it is content. A cut is a decision the user sees in the outline; an omission nobody decided is a defect.

## Errors in the sources

Slides contain mistakes. Handle them by weight:

- **Trivial**: typos, a missing bracket, a wrong character in code, a syntax error, a compiler warning caused by such a slip (missing parentheses), an obviously mis-numbered item, an output that does not match the code because of a slip. Fix it in place and say nothing. Never write "the slide has a typo here" or show the wrong version; the book simply has the right one.
- **Serious**: a wrong statement, a definition that contradicts another part of the material, a formula that does not hold, code that cannot do what is claimed, an example whose result differs from what running it gives in a way that changes the point. Do not decide alone. Put it in the outline as a finding and in `_work/findings.md`:

  ```markdown
  ## F3 · open · dp26a-fp2ea s31
  Source says: ...
  Problem: ...
  Proposal: ... (name any concept the fix needs that the sources do not define)
  ```

  Until the user answers, the book follows the source at that spot, so that nothing he has not approved overrides the lecturer. When he answers, apply it, change `open` to `confirmed` or `rejected`, and add a line `Decision: ...` with what he said. Mention still-open findings at the start of the next run.

When in doubt whether an error is trivial, treat it as serious.

When a new source contradicts what the book already says (a later lecture corrects or sharpens an earlier one), that is a finding too. Until the user answers, the book keeps its current text.

## Filling gaps

Add an explanation of your own only where a reader who has just the book would otherwise be stuck: a term used but never defined, a step skipped in a derivation, an example shown without saying what it shows, a concept the lecturer clearly explained aloud and the slide only names.

- Keep additions as short as the gap. One sentence is often enough.
- Additions are not marked; they are part of the text.
- Add only what is standard and certain. Never invent course-specific facts: what will be on the exam, how the lecturer defines something, which variant of a theorem the course uses. If the material is ambiguous about such a thing, that is a finding.
- No enrichment. Do not add related topics, extra examples, best practices, background or alternative approaches the course does not teach. A longer book is a worse book for someone who has to learn all of it.

## Code

- Every code block has a language (`elixir`, `python`, `c`, `prolog`, `bash`, `text` for plain output). Without it there is no highlighting and `check.py` fails.
- Keep every example from the sources unless it is an exact duplicate. When two sources (often two lectures) show versions of the same example, show it once, in the fuller version, and keep what only the other one has. Keep code exactly, apart from trivial fixes. Keep comments that explain; translate nothing.
- Interactive sessions show input and output together the way the REPL prints them. Program output goes in its own `text` block, introduced by a sentence.
- Consecutive one-line notebook cells that demonstrate the same point become one block, an `iex` session with each result under its expression, not a row of separate blocks.
- Refer to functions and constructs by name in the text, in backticks.

Whether to run an example is decided per example. To capture what a REPL really prints, pipe the input into it (`printf 'x = 5\nx + 1\n' | iex`); a script run (`elixir f.exs`, `python f.py`) does not print return values. Run it when the source shows or claims an output, the runtime is installed on this machine, and running is quick and has no side effects. Then the book shows the real output; a difference that is only formatting or a newer version's wording is a trivial fix, a difference in substance is a finding. Do not run code that needs network access, credentials, long computation, or that the text only uses to illustrate syntax or structure. In the final report say which examples were verified by running; never imply it for those that were not. Deprecation and version warnings that running prints but the source does not show are left out, unless the course talks about them.

## Math

- Every formula is LaTeX, rendered by KaTeX: `$...$` inline, `$$...$$` displayed on lines of their own. Never an image of a formula.
- Notation is the course's notation, symbol for symbol. Do not "improve" it or switch conventions.
- Every symbol is introduced in words where it first appears.
- Derivations keep all the steps the source has. Where the source jumps, add the missing step (see Filling gaps).
- Number a displayed formula with `\tag{n}` only if the text refers back to it.
- Details of syntax and KaTeX limits are in `mdbook.md`.

## Figures

A figure that carries information must be in the book. Describing it in words instead is not a substitute. The transcript says for each figure what it shows and recommends a form; you decide:

- **Image**: copy the crop into `book/src/img/` and include it with alt text and, when useful, a caption. The right choice for plots, photos, screenshots and any drawing that cannot be reproduced exactly.
- **Redraw as Mermaid**: only for simple trees, flowcharts, state machines and sequence diagrams, and only when every node, edge and label of the original is reproduced. After building, compare with the original. If anything does not match or the layout misleads, use the image.
- **Table or text**: when the figure is a table or list drawn as a picture.
- **Formula image**: always LaTeX.
- **Figure corrected by a confirmed finding**: the crop shows the wrong version, so redraw it (Mermaid, or for circuits and layouts a monospaced drawing in a `text` block) or, if it cannot be drawn faithfully that way, describe it in words and say so in the report.

Decorative pictures are cut. Refer to a figure from the text and say what to see in it.

## Exercises and homework

- Exercises from the course, practice and homework alike (házi feladat, KHF, NHF, beadandó), belong at the end of the chapter whose topic they train, under a heading such as "Gyakorló feladatok", with the task text as given.
- When the resources hold the same sheet twice, once with and once without solutions, take the task text from the version without, and the solutions from the other. When they hold only a solution (a solved homework without its task sheet), state the task from what the file itself says (header comment, specification) and mention in the report that the task sheet is missing.
- Solutions appear only if the resources contain one (official, or the user's own solved homework). Put each inside `<details><summary>Megoldás</summary> ... </details>` so it is not seen by accident. Do not write solutions of your own; a one-line hint that points to the relevant section is allowed.

## Sources line

Every chapter written from sources ends with one line naming them, with the exact file names and the slide numbers (the number in the unit id, which matches the number printed on the slide):

```html
<p class="sources">Forrás: dp26a-fp1ea.pdf (21–27. dia), dp26a-fp1gy.livemd</p>
```

`check.py` requires the file name of every source that feeds the chapter to appear in it.

## Updating an existing book

The reader has read the earlier version and will read the new one from wherever the changes are. So:

- Integrate. New material about an existing topic is worked into that topic's chapter at the place it belongs. Revise the neighbouring paragraphs so there are no seams, no repeated definitions, and no "as mentioned later" left pointing the wrong way.
- If new material changes how an old topic should be explained (a later lecture generalises or corrects an earlier one), rewrite the old explanation; do not stack the new one on top.
- Split a chapter that has grown past one sitting into sub-chapters; keep the original file as the parent.
- Keep file names. Reordering happens in `SUMMARY.md`. A new chapter goes where the reading order needs it, before existing chapters if they build on it. A link forward is fine for a passing mention; if an earlier chapter needs a later topic to be understood, move one of them in `SUMMARY.md`.
- When a changed source drops or alters content, the report from `prepare.py` names the affected units and chapters. Alter the book to match changed content. For dropped content, ask the user in the outline whether it stays.
- Update the sources lines of every chapter you touch.
- In the final report list each changed chapter with what changed in it, so the user knows what to reread.
