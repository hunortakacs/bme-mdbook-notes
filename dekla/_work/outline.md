# Outline: Deklaratív programozás (dekla)

First run, 2026-10-08. Sources: three FP lectures (dp26a-fp1ea/fp2ea/fp3ea.pdf), their notebooks
(fp1ea-sum-benchee, fp2ea-fibonacci, fp3ea-reszlistak-kihagy_bevesz_rek), the fp1 intro notebook
(fp1gyfel) and the practice sheets fp1gy-megoldasok, fp2gy-megoldasok, fp3gy.

Title: **Deklaratív programozás**. Language: hu. The Prolog half of the course will extend the book later
(new top-level chapters after the Elixir part).

Abbreviations below: 1ea = dp26a-fp1ea.pdf, 2ea, 3ea likewise; bench = dp26a-fp1ea-sum-benchee,
fib = dp26a-fp2ea-fibonacci, 3nb = dp26a-fp3ea-reszlistak-kihagy-bevesz-rek, fel = dp26a-fp1gyfel,
1gy = dp26a-fp1gy-megoldasok, 2gy = dp26a-fp2gy-megoldasok, 3gy = dp26a-fp3gy.

## Chapter tree (all NEW)

- `bevezetes.md` **Bevezetés**: what the course is (FP in Elixir, LP in Prolog). 1ea s3.
- `deklarativ.md` **Deklaratív programozás**: declarative vs imperative, MIT és nem HOGYAN, the variable
  as in mathematics, C factorial example, FP–functions / LP–relations, paradigm tree, `app/2` in
  Elixir vs `app/3` in Prolog, the Prolog procedure used in several directions. 1ea s14–s18.
- `elixir.md` **Az Elixir nyelv**: main features, Erlang/OTP, BEAM, Elixir (analogies JVM/Kotlin,
  Jupyter/Livebook), processes and messages (spawn/send/receive). 1ea s21, s26, s27.
  - `elixir/iex.md` **Interaktív használat: IEx és Livebook**: REPL session, Ctrl+C / Ctrl+G menus,
    IEx helpers (h, c, r, i, exports…), compiling and calling own module (`fpea.ex`, `Fpea.fac`),
    module/function identity (name/arity/module), def/defp, modules only in files or Livebook cells,
    Livebook cell = module, `IO.inspect` vs `inspect`, the pipe `|>`. 1ea s35–s37; fel s2, s5 (Livebook
    module note); 1gy s3 (practice hint: Kernel and :math in iex, completion).
  - `elixir/mix.md` **Projektek, mérés, típusellenőrzés: mix, benchee, dialyzer**: mix new project
    layout, mix.exs, deps, `mix do deps.get + deps.compile`, `mix compile`, `iex -S mix`, `r`,
    Benchee.run with `profile_after`, reading the result table, dialyxir in deps, `mix dialyzer`, PLT,
    the invalid_contract example, why dialyzer cannot run inside Livebook. 1ea s41–s49, s50 (table
    only), 3ea s29, s30; 3gy s2 (dialyzer-in-mix paragraph); 2gy s4 (same, commented out).
- `tipusok.md` **Típusok**: strongly typed, dynamically checked; the type table; type specifications
  (`@spec`) and the declarative head comment. 2ea s4; 1ea s25; fel s5 (@spec + fejkomment paragraph).
  - `tipusok/atom-szam.md` **Atom, szám, igazságérték**: 2ea s5, s6, s25 (boolean part).
  - `tipusok/fuggveny.md` **Függvény**: function as value, capture `&`, anonymous fn and `.()` call,
    def/defp, function type, default parameters `\\`, higher-order functions (`L.map`, `T.map` for a
    binary tree, Java/C# analogues). 2ea s7–s9; 1ea s24.
  - `tipusok/ennes-tartomany.md` **Ennes és tartomány**: 2ea s10.
  - `tipusok/lista.md` **Lista és karakterlánc**: linked list, head/tail, `[x|xs]` notations,
    charlists `'erl'`/`~c"erl"`, which code lists print as charlists, `charlists:` inspect options.
    2ea s11, s12; fel s2 (list notation), s5 (printing charlists, 0..127 table).
  - `tipusok/sztring-binaris.md` **Sztring és bináris**: UTF-8 bytes, escapes, interpolation, `<<>>`,
    size. 2ea s13–s15.
  - `tipusok/szotar.md` **Kulcs-érték lista és szótár**: 2ea s16–s18.
  - `tipusok/regex.md` **Reguláris kifejezés**: sigil, PCRE, run/scan/split/replace, option table.
    2ea s19, s20.
- `valtozok.md` **Termek, azonosítók, változók**: term, identifier conventions (`?`, `!`, snake_case),
  free/bound variable, rebinding, pin `^`, lexical scope, `with`, comments. 2ea s22–s25.
- `muveletek.md` **Műveletek és beépített függvények**: arithmetic and bitwise operators with
  precedence, comparisons and term order, float pitfalls, `not/and/or` vs `!/&&/||` (guards,
  short-circuit, truthiness), BIFs, type tests and conversions. 3ea s17–s21.
- `mintaillesztes.md` **Mintaillesztés**: pattern, free variable, `_`, repeated variables, `=` is
  matching not assignment, MatchError, what cannot be a pattern (expressions), layered patterns,
  partial map match, pin, `case` with guards, `when` guards in function heads, clauses and mutually
  exclusive patterns (`[x|xs]` vs `[x]` vs `[x1,x2|xs]`), the examples from 3ea. 1ea s22; 3ea s23–s26;
  fel s4; 2gy s2 (guard intro); 1gy s5 (mutually exclusive patterns, layered pattern note).
- `rekurzio.md` **Rekurzió**: linear / branching recursion, recursive data structures, designing a
  recursive function (`app/2` walk-through: termination and correctness), body vs tail recursion
  (`fac`, `FacJobbrek`, accumulator), left recursion (print before/after: `upto_by_3`), clause order
  and efficiency with the measurements (sum1/sum2/sum3, nth), error signalling Erlang style
  `{:ok, v} | :error` vs Elixir style `v | nil`. Exercises: 1gy tasks 1–8 with solutions + "További
  gyakorló feladatok" (revapp, rev, diff; no solution); 2gy upto_by_3 (both, with solutions).
  1ea s23, s47, s50; bench s2; fel s3, s5, s6, s7; 1gy s4, s5, s6; 2gy s2.
- `listak.md` **Műveletek listákon**: cost of list access, sharing the tail, `hd/tl/length/++/--/in`,
  List and Enum functions, eager Enum vs lazy Stream, short examples (`sum`, `append`, `revapp`).
  Exercises: 2gy L1 split, L2 takewhile (with solutions); 3gy L1–L6 (dropevery, tails, pairs, parosan,
  repeated, stammering; no solutions; 2gy L3–L6 are the same tasks, taken once from 3gy). 2ea s28–s38;
  2gy s4; 3gy s2 (L1–L6).
- `sztringek.md` **Műveletek sztringeken**: code point vs grapheme, String functions. 2ea s41–s43.
- `for.md` **For-jelölés**: generators, filters, `into:`, `uniq:`, `reduce:`, examples.
  Exercises: 3gy L7 (ertekek, solution in the sheet), T1 proper divisors, T2 composite numbers
  (+ faster variant). 3ea s10–s14; 3gy s2 (L7), s3 (T1, T2).
- `technikak.md` **Problémamegoldási technikák**: short parent page.
  - `technikak/dinamikus.md` **Dinamikus programozás: Fibonacci**: what DP is, the six Fibonacci
    variants (tree recursion with call-tree figure, memoization, tabulation with Map / :array / list,
    two-variable iteration), complexities, benchmark table, memo trace (FibMm), `dbg` (FibTdbg).
    Exercise: 2gy "Maximális összegű intervallum" (both functions, solutions). 2ea s46–s48; fib s1, s2;
    2gy s3.
  - `technikak/csuszoablak.md` **Csúszóablakos technika**: max-sum contiguous sublists, variants
    11/12/12x/13, 21/22a/22b/23, benchmark comparison. 3ea s4; 3nb s1–s5.
  - `technikak/kihagy-bevesz.md` **Kihagy-bevesz rekurzió**: `komb/1`, `eloszt/1` (CEOI'95 coin
    split). Exercise: 3gy "Összeg testvéries elosztása" (improve eloszt; no solution) + 3nb closing
    exercise. 3ea s6; 3nb s6; 3gy s3 (elosztás part).

## Cut list

- Title slides, part dividers, tables of contents: 1ea s1, s2, s4, s13, s19, s20, s28, s34, s40;
  2ea s1–s3, s21, s26, s27, s34, s39, s40, s44, s45; 3ea s1–s3, s5, s8, s9, s15, s16, s22, s27, s28.
- Administration (website, ETS, requirements, grading, IMSc, practice times): 1ea s5–s12, s52;
  2ea s49; 3ea s31.
- Installation, editors, Docker: 1ea s29–s32, s38, s39; 1gy s3 (install advice part); `Mix.install`
  cells of all notebooks.
- Pointers to the notebooks / downloads: 1ea s33, s51; 2ea s47 (link part; the list of six variants
  is kept); 3ea s4/s6 (link lines only).
- Link list: 3ea s7 (DP reading list).
- Notebook conventions (cell colours) and headers: 1gy s1, s2; 2gy s1; 3gy s1; fel s1; bench s1;
  3nb s1 heading only.
- Raw tool output: `mix --help` full text (1ea s42; usage lines kept), Benchee warnings, system info
  and `%Benchee.Suite{}` dumps, profiler listing (1gy s5); only the result tables are kept.
- Livebook UI widgets: fib s2 Kino.Input / Explorer.DataFrame cells.
- Trivia: 2ea s46 "named for better saleability" sentence about Bellman (the DP definition stays).

## Figures

- 1ea s16 paradigm/language tree: redraw (Mermaid).
- 2ea s48 call tree of `fib 5`: redraw (Mermaid tree), traversal-order curve described in text.
- 2ea s46 pasted slide from another course: text.
- 3ea s18 bomb clip art, 3ea s10 bullet icons: dropped (decorative).

## Verified by running (Elixir 1.19.6)

Every IEx example of 2ea and 3ea and the 3nb `komb`/`eloszt` calls, the charlist printing claims of
fel/2ea, `Prime.prime?` edge cases, `use Bitwise`. Results match the slides except the items below.
Map/keyword printing order and `~c` charlist format follow the real 1.19 output.

Trivial fixes applied silently: keyword list output in 2ea s16 (`{:név, ...}` tuples, stray quote);
`{y, ys, yys}` → `{y, ys, yss}` with real output `{1, [2, 3], [1, 2, 3]}` (3ea s26); eloszt result key
`[2, 1, 4]` (3ea s6); printable code ranges in fel s5 ("7..13, 27, 32..126", 127 is not printable);
`sum_of_sqrs_a6b5` name (2ea s9); `to_atom(string)` (3ea s21); `def fac(n), do:` (1ea s23); iex prompts
(1ea s35); "pause" leftover (2ea s14); "BEAM platformra" (1ea s27); `Repeated` module name in 3gy L5;
`EnumS.` → `ElosztS.` type references (3gy/3nb); `Enum.at 'almafa', 2` prints `109` (= `?m`).

## Findings (need a decision)

See findings.md F1–F6 (all confirmed by the user on 2026-10-08; F6 was found while writing).
