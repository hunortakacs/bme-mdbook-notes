# Profile: dekla

## Course

Deklaratív programozás (BME VIK, 2026 ősz; lecturers Kabódi László, Marussy Kristóf). Sources and book in Hungarian. First half: functional programming in Elixir (FP lectures `dp26a-fpNea.pdf`, notebooks `*.livemd`, practice sheets `dp26a-fpNgy*.livemd`); second half: logic programming in Prolog (not yet in `res/`; it becomes a new part "Logikai programozás" in SUMMARY.md after the Elixir chapters).

## Terminology (as the book uses it)

- ennes (tuple), szótár (map), kulcs-érték lista (keyword list), tartomány (range), bináris (binary), sztring (string, double quoted), karakterlánc / karakterlista (charlist, single quoted) — a karakterlánc NEM sztring
- term, tömör (ground, no free variable), szabad / kötött változó; kötés (binding) — never "értékadás"
- minta, mintaillesztés (pattern matching), réteges minta (layered pattern), őr / őrkifejezés (guard), klóz (clause)
- törzsrekurzió (body recursion), jobbrekurzió = terminális rekurzió = farokrekurzió (tail recursion), balrekurzió = fejrekurzió (head recursion), elágazó rekurzió (tree recursion), akkumulátor
- fejkomment (declarative head comment under `@spec`), típusspecifikáció
- for-jelölés = for-komprehenzió (for-comprehension), generátor, predikátum/szűrő
- kihagy-bevesz rekurzió (include-exclude), csúszóablakos technika, memoizálás, táblázatos (tabulation)
- hibajelzés Erlang-stílusban (`{:ok, v} | :error`) és Elixir-stílusban (`v | nil`)
- BIF (beépített függvény), egyesítés (Prolog's two-way matching)
- KHF = kis házi feladat, NHF = nagy házi feladat, gyakorlat; exercise headings "Gyakorló feladatok", solutions in `<details><summary>Megoldás</summary>`

## Notation and code conventions

- Fence languages: `elixir` for code, `iex` for IEx sessions (`iex>` prompts, results under each input), `text` for program and Benchee output, `console` for shell sessions, `prolog`.
- Outputs are shown as Elixir 1.19 prints them (verified with the installed 1.19.6): charlists as `~c"..."`, maps in key order, `Enum.at 'almafa', 2` prints `109`. Inputs keep the slides' spelling (`'erl'` stays); the book mentions once that `'...'` is the older notation (tipusok/lista.md).
- Abbreviated error messages of the slides (`** ...bad argument in ...`) may stay; `#Function<...>` numbers are not meaningful.
- Fixed silently: slide typos, misnamed functions (`sum_of_sqrs_a6b5`), wrong module references in types (`EnumS.` → `ElosztS.`), old-format outputs.
- Benchmark tables are quoted as measured, with machine and versions in one sentence; Benchee warnings and system dumps are cut.

## Recurring decisions (findings.md)

- F1: tree recursion is O(2^n) time, O(n) space.
- F2: the course's clause-order advice is kept, the measurements are shown, plus one sentence that they are small and inconsistent; tail recursion is the clear gain.
- F4: term order includes `map` between tuple and list.
- F5: `import Bitwise` (old form `use Bitwise` mentioned once).
- F6: missing clauses fail at run time with FunctionClauseError; dialyzer does not report missing cases.

## Verifiers

- `verify/iex`: runs every `iex` block of the book in Elixir (each chapter in its own session, the chapter's compilable `defmodule` blocks and `verify/_prelude.exs` loaded first) and compares each result with the output the book shows; also compiles every complete `defmodule` of an `elixir` block. Does not check `text` output blocks after `elixir` cells, IEx helpers (`c`, `r`, `h`, `i`, `exports`), shell sessions, or Benchee runs. Accepted differences: `verify/_iex.accepted`.
