# Findings

## F1 · confirmed · dp26a-fp2ea s48, dp26a-fp2ea-fibonacci s2
Source says: tree-recursive `fib/1`: "O(2^n) futási idő, O(2^n) tárhely".
Problem: the space need is O(n): at any moment only one path of the call tree is on the stack, and
its depth is at most n. The notebook's own prose says the partial results are kept "az egyre mélyülő
veremben", which fits O(n).
Proposal: write O(2^n) time, O(n) space (stack depth n).
Decision: user chose the proposal (2026-10-08): O(2^n) time, O(n) space (stack depth n).

## F2 · confirmed · dp26a-fp1gy-megoldasok s5, dp26a-fp1ea s47/s50, dp26a-fp1ea-sum-benchee s2
Source says: putting the more frequently matching clause (non-empty list) first makes the function
more efficient; the slide's annotated Benchee table (sum2 1.83x, sum1 1.97x slower than sum3) is
presented in that light.
Problem: the course's own measurements do not agree with each other: in the benchee notebook sum1
(empty-list clause first) is faster than sum2 (7.54 K vs 6.73 K ips), and the nth benchmark in 1gy
shows no difference (firstElemEmptyFirst vs EmptyLast within 1–3 %). Only the tail-recursive sum3 is
consistently faster.
Proposal: keep the recommendation as the course states it, show both measurements, and add one
sentence: the measured differences between the two clause orders are small and not consistent; the
clear gain comes from tail recursion.
Decision: user chose the proposal (2026-10-08): keep the advice, show both measurements, add the one-sentence caveat.

## F3 · confirmed · dp26a-fp1gy-megoldasok s5 (task 8)
Source says: `Prime.prime?/1` solution, head comment "b == true, ha x prím".
Problem: `Prime.prime?(1)` returns `true` (1 is not prime), `prime?(0)` raises FunctionClauseError.
The tests do not cover these cases.
Proposal: keep the solution as is and add one sentence that it is correct for x ≥ 2.
Decision: user chose the proposal (2026-10-08): keep the code, add that it is correct for x ≥ 2.

## F4 · confirmed · dp26a-fp3ea s18
Source says: term order `number < atom < reference < function < port < pid < tuple < list < binary`.
Problem: `map` is missing; the real order puts it between tuple and list (verified with `Enum.sort`).
Proposal: write `... < tuple < map < list < binary` (bitstring).
Decision: user chose the proposal (2026-10-08): add map between tuple and list.

## F5 · confirmed · dp26a-fp3ea s17
Source says: bitwise operators must be enabled with `use Bitwise` (or `use Bitwise, only_operators: true`).
Problem: in current Elixir (1.14+) `use Bitwise` is deprecated and prints a warning; the current form is
`import Bitwise` (`only:`/`except:` options of import).
Proposal: write `import Bitwise` and mention once that older material writes `use Bitwise`.
Decision: user chose the proposal (2026-10-08): write import Bitwise, mention use Bitwise once as the older form.

## F6 · confirmed · dp26a-fp1gyfel s3
Source says: "Ha nem fedünk le minden esetet, azt az Elixir dialyzer eszköze az elemzés során jelzi."
Problem: dialyzer does not report non-exhaustive clause sets; a function that handles only some
cases is valid and fails at run time with FunctionClauseError (which the same notebook shows with
App0). Dialyzer's success typing is optimistic: it warns when a call can never succeed, a clause can
never match, or a @spec contradicts the code.
Proposal: replace the sentence with: missing cases are not a compile error; a call that matches no
clause stops with FunctionClauseError at run time; dialyzer warns only if it can prove that a call
can never succeed.
Decision: user chose the proposal (2026-10-08): missing cases fail at run time with FunctionClauseError; dialyzer warns only when it can prove a call can never succeed.
