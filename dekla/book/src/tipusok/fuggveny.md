# Függvény

## A függvény is érték

A függvény is érték: változóhoz köthető, adatstruktúra eleme lehet, függvény eredménye lehet, paraméterként átadható stb. Azaz a függvény is ún. *first class citizen*, teljes jogú polgár.

Egy modulban definiált függvényt a `&` operátorral (*capture operator*) tehetünk értékké: `&Modul.név/aritás`. Az így kapott függvényértéket ponttal és zárójelpárral hívjuk. Az infix operátorok is függvények, és prefix helyzetben is alkalmazhatók; az `:math` Erlang-modul függvényei ugyanígy elérhetők:

```iex
iex> fac = &Fpea.fac/1 # &: capture operator
&Fpea.fac/1
iex> fac.(5) # pont és zárójelpár kell, szóközökkel tagolható
120
iex> Kernel.+(3,2) # infix operátor alkalmazása prefix helyzetben
5
iex> fs = [&Kernel.+/2, &*/2, &:math.sin/1] # :math Erlang modul!
[&:erlang.+/2, &:erlang.*/2, &:math.sin/1]
iex> (hd fs).(3,2)
5
iex> (hd tl fs).(3,2)
6
iex> (hd tl tl fs).(:math.pi * 90 / 180)
1.0
```

A `fs` lista elemei függvények; a `hd fs` a lista feje (az összeadás), a `hd tl fs` a második eleme (a szorzás), a `hd tl tl fs` a harmadik (a szinusz). Az eredmény kiírásából látszik, hogy az Elixir `Kernel.+/2` és `*/2` operátora valójában az `:erlang` modul függvénye.

## Névtelen függvény

Névtelen (anonim) függvényt az `fn paraméterek -> törzs end` kifejezéssel definiálunk. Közvetlenül is meghívható, és névhez is köthető; a hívásnál itt is kell a pont:

```iex
iex> fn ki -> "Szia, " <> ki <> "!" end # <>: konkatenálás
#Function<44.40011524/1 in :erl_eval.expr/5>
iex> fn ki -> "Szia, "<>ki<>"!" end.("Péter") # pont, zárójel!
"Szia, Péter!"
iex> szia = fn ki -> "Szia, " <> ki <> "!" end
#Function<44.40011524/1 in :erl_eval.expr/5>
iex> szia
#Function<44.40011524/1 in :erl_eval.expr/5>
iex> szia.("Bea")
"Szia, Bea!"
```

A `#Function<...>` a függvényérték kiírt alakja; a számok verziónként és futásonként mások.

## Függvénydefiníció modulban

Modulban a `def` publikus, a `defp` privát, azaz a modulon belül lokális függvényt definiál. A modulban definiált függvény hívásakor a pont nem kell, és az argumentumok körüli zárójel sokszor elhagyható:

```elixir
def sum_of_squares(a,b), do: sqr(a) + sqr(b)
defp sqr(a), do: a*a # p[rivát], azaz lokális a modulon belül
```

```iex
iex> Fpea.sum_of_squares 3, 4.5
29.25
```

A függvény típusa: `(arg1 típusa, arg2 típusa, ...) :: eredmény típusa`. Például a `sum_of_squares/2` függvényé: `(number, number) :: number`.

## Paraméter alapértelmezett értéke

Egy függvény egy vagy több paraméterének a `\\` jelöléssel alapértelmezett (*default*) értéket adhatunk. Az ilyen paraméter opcionális, a többi elvárt. Ha egy függvényt

- a kötelezően (default argumentumok nélkül) elvártnál kevesebb paraméterrel hívunk meg, a hívás meghiúsul;
- az elvárt számú paraméterrel hívunk meg, az összes opcionális paraméter az alapértelmezett értékét veszi fel;
- az elvártnál több paraméterrel hívunk meg, az aktuális paraméterek értékét balról jobbra haladva veszik fel az opcionális paraméterek.

```elixir
def sum_of_sqrs_b5(a, b \\ 5), do: sqr(a) + sqr(b)
```

```iex
iex> Fpea.sum_of_sqrs_b5 3, 4.5
29.25
iex> Fpea.sum_of_sqrs_b5 3
34
```

```elixir
def sum_of_sqrs_a6b5(a \\ 6, b \\ 5), do: sqr(a) + sqr(b)
```

```iex
iex> Fpea.sum_of_sqrs_a6b5 3
34
iex> Fpea.sum_of_sqrs_a6b5
61
```

A `sum_of_sqrs_a6b5 3` hívásban az egyetlen aktuális paraméter az első opcionális paraméterhez, `a`-hoz kerül, `b` az alapértelmezett 5 lesz: $3^2 + 5^2 = 34$. Paraméter nélkül mindkettő az alapértelmezett: $6^2 + 5^2 = 61$.

## Magasabb rendű függvények

Mivel a függvény is érték, átadható egy másik függvénynek. Azt a függvényt, amelynek paramétere vagy eredménye függvény, **magasabb rendű függvénynek** nevezzük. A ciklusok helyett ezekkel szétválaszthatjuk az adatszerkezet rekurzív bejárását az elemeken elvégzendő műveletektől. Az alábbi `L.map/2` egy egyszeresen láncolt listát jár be, a `T.map/2` egy bináris fát; mindkettő az `f` paraméterként kapott függvényt alkalmazza minden elemre:

```elixir
defmodule L do # Egyszeresen láncolt lista bejárás
  def map([], _f), do: []
  def map([hd|tl], f), do: [f.(hd)|map(tl, f)]
end
defmodule T do # Bináris fa bejárás
  def map(nil, _f), do: nil
  def map({x, left, right}, f), do: {f.(x), map(left, f), map(right, f)}
end
```

A fát itt `{x, left, right}` hármasok ábrázolják, az üres fát a `nil`. Egy alkalmazás:

```iex
iex> L.map [1, 2, 3], fn(x) -> 2 * x end
[2, 4, 6]
```

A magasabb rendű függvények egyre gyakoribbak az objektumorientált nyelvekben is:

- Java: `List.of(1, 2, 3).stream().map(x -> 2 * x).toList()`
- C#: `new List<int>{1, 2, 3}.Select(x => 2 * x)`

<p class="sources">Forrás: dp26a-fp2ea.pdf (7–9. dia), dp26a-fp1ea.pdf (24. dia)</p>
