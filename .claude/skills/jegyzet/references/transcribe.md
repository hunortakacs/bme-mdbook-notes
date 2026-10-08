# Transcribing flagged units

The transcript of a source (`_work/sources/<slug>/transcript.md`) is the complete, faithful text version of that source. The book is written from transcripts, not from the PDF, so whatever is missing from a transcript is missing from the book. Transcribing is copying, not writing: no summarising, no rephrasing, no translating, no fixing.

## The file

```markdown
## s14 · p31-33 · Mintaillesztés
<!-- status: TODO view pages/p033.png -->
<!-- flags: math, graphic -->
<!-- figure: figures/p033-f1.png -->

(text extracted by the script)
```

- The `## sN · pages · title` line identifies the unit. Never edit, reorder, add or delete these lines; `check.py` compares them with the source.
- `status: auto` means the script found only plain text and code on the slide. Leave these units as they are.
- `status: duplicate of <file> <unit>` means every page of the unit also appears in another source, which is transcribed instead. Leave these units as they are.
- `status: TODO view <png>` means you have to look. Paths are relative to the source's folder in `_work/sources/<slug>/`.
- `draft.md` next to the transcript is the script's raw extraction, kept so that a later change of the source can be compared with it. Never edit it.
- Flags say why: `math` (formula fonts or symbols), `graphic` (drawing or picture), `image` (embedded picture), `table`, `layout` (columns or rotated text; reading order may be wrong), `stacked` (pictures on top of each other, see below), `encoding` (the text layer is unreliable), `no-text` (slide is a picture), `annot` (PDF comments), `variant` (see below).

## For each TODO unit

1. Read the page image with the Read tool. Look at the whole slide, not only at the part the flag names.
2. Rewrite the unit's body so that it holds everything a student would get from the slide, in reading order. The extracted text is a starting point; where it disagrees with the image, the image is right.
3. Change `TODO view` to `viewed` in the status line and keep the image path (`<!-- status: viewed pages/p033.png -->`); the formula check uses it. Keep the flags and figure lines. If you transcribed a formula on a unit without the `math` flag (a formula pasted as a picture, handwriting), add `math` to its flags line, so the formula check covers it. If a unit flagged `math` turns out to hold no formula (a symbol in code, a footnote mark), remove the flag (and the flags line, if nothing is left on it), so the check skips it.

Remarks of your own that are not slide content go in `<!-- note: ... -->` comments, never into the body.

What the body must contain:

- **Text**: all of it, in the source language, as written. Keep emphasis that carries meaning (defined terms, warnings). Lists stay lists with their nesting.
- **Code**: fenced, with the language (`iex` for IEx sessions, `console` for shell sessions, the other names in `mdbook.md`), character for character, indentation included. Typos in code are copied as they are; the writing step fixes them. Syntax colouring is not content; comments are.
- **Formulas**: LaTeX, inline as `$...$`, displayed as `$$...$$` on their own lines. Reproduce the formula exactly as shown: the same symbols, indices, limits, accents, brackets and order. This holds for formulas that are pasted pictures and for handwriting too. Use KaTeX-compatible commands (`\begin{pmatrix}`, `\begin{aligned}`, `\begin{cases}`, `\langle \rangle`, `\ket{}`, `\bra{}`). If you cannot read a symbol with certainty, do not guess silently: write your best reading and add `<!-- unclear: what and where -->`.
- **Tables**: Markdown tables, every cell.
- **Figures**: one `Figure:` paragraph per figure, complete enough that someone could redraw it without the image: what kind of figure it is, every node, edge, label, axis, value and arrow direction. Then one line with the recommendation:
  - `Use: image <path>` when it is a photo, plot, screenshot, a drawing too intricate to redraw exactly, or a figure where positions carry meaning (circuits, memory layouts, geometry, timelines);
  - `Use: redraw` when it is a simple tree, flowchart, state machine or sequence whose every element you listed;
  - `Use: table` or `Use: text` when the figure is really a table or a list in disguise;
  - `Use: none (decorative)` for logos, clip art and stock photos that say nothing.
- **Links** and PDF annotations already listed by the script: keep them.

For every figure you recommend as `Use: image`, check the automatic crop named in the `figure:` line by reading it (crops of formulas, tables and decorations do not matter; they are not used as images). If it cuts something off or includes surrounding text, make a better one, replace the path in the `figure:` line, and delete the automatic crop:

```bash
python3 <skill>/scripts/pdf_triage.py crop <source.pdf> <physical page> X0 Y0 X1 Y1 -o <source folder>/figures/<name>.png
```

`X0 Y0 X1 Y1` are fractions of the page from its top left corner (`0 0.35 1 0.9` is the full width between 35% and 90% of the height). Read the new crop to confirm. `pdf_triage.py page <pdf> <page> -o out.png` renders any whole page, also ones that were not flagged.

## Special cases

- **Variants** (`s14.1`, `s14.2`): animation steps of one slide where a later step replaced something instead of adding to it. Each variant holds content the other lacks. Transcribe each fully and start the later ones with a line `Differs from s14.1: ...`, so the writer sees at once what changed.
- **Stacked pictures** (`stacked`): several pictures lie on top of each other on one page, usually an animation exported to a single page. Only the top one is visible in the render. The script saved every layer as its own file (`figures/pNNN-x*.png`); read each one and describe them in order. A layer file is a better image than the crop of the page, so a `Use: image` line names the layer.
- **`encoding`**: the text layer has wrong or missing characters. Take all text from the image.
- **`layout`**: decide the real reading order from the image. Side-by-side columns become consecutive blocks; say what was beside what when the pairing carries meaning (a term next to its definition, code next to its output).
- **Suspected errors in the source**: copy what the slide says and add `<!-- suspect: what looks wrong and why -->`. Do not correct it here; the writing step decides. Output in an older version's format (a charlist printed as `'abc'` instead of `~c"abc"`) is not suspect; the writing step updates it anyway.
- **Unreadable** content (too small, blurred, cut off): try `pdf_triage.py page ... --width 2400` for a sharper render. If it stays unreadable, transcribe what you can, add `<!-- unclear: ... -->`, and mention it in your report.

## Spot checks on `auto` units

Extraction can be wrong on a slide that was not flagged. For each source, pick three `auto` units spread across the deck, render them with `pdf_triage.py page` into the source's `pages/` folder, and compare with their text. If one of them is missing something or is out of order, do not trust the rest: run `prepare.py <class> --force --view-all --only <slug>`, which turns every `auto` unit of that source into a TODO unit (other sources stay as they are), and transcribe them all.

When the script merged animation steps by content instead of by page labels (the prepare report says "merged by content"), also render the first and the last page of two merged groups and confirm that the last page contains everything the first one has.

## When you are done with a source

Every unit is `auto`, `viewed` or `duplicate`; none is TODO. Report: how many units you viewed, every `suspect` and `unclear` note with its unit, the figures you recommend keeping, and any crop you replaced.

## Independent formula check

Run this for every source that has `math` units, as soon as those units are transcribed (the others need not be finished), with a fresh subagent that did not write the transcript (a reader who knows what the formula "should" say reads it less carefully).

Give the subagent the transcript path and this instruction: for each unit flagged `math`, read the page image named in its status line (`pages/pNNN.png`), then compare every formula in the transcript with the image symbol by symbol: indices and exponents, signs, limits of sums and integrals, hats, bars, daggers and primes, bracket types, the order of factors, matrix entries. Report each difference as `unit: transcript has X, image shows Y`. Report nothing else and change nothing.

For every reported difference, look at the image again yourself and correct the transcript where the report is right.
