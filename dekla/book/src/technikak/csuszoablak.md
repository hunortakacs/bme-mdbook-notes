# Csúszóablakos technika

Egy sorozat (lista) különféle szempontok szerint kiválasztott folytonos részsorozatait **csúszóablakos** módszerrel állíthatjuk elő, egymásba ágyazott ismétlésekkel. Mivel a funkcionális nyelvekben nincs ciklus, az ismétlést rekurzióval valósítjuk meg, a részeredményeket egy, esetleg több akkumulátorban gyűjtjük. Mivel a gyűjtéshez plusz paraméter(ek)re van szükség, rendszerint segédfüggvényeket is definiálunk.

A példafeladat egy számlista **maximális összegű folytonos részlistáinak** előállítása. Például az `[1, 2, 3, 4, -10, 4, 3, 2, 1]` lista maximális összegű folytonos részlistái: `[1, 2, 3, 4]`, `[1, 2, 3, 4, -10, 4, 3, 2, 1]` és `[4, 3, 2, 1]`, összegük `10`. A függvény visszatérési értéke olyan pár legyen, amelynek első eleme a részlisták összege, második eleme ezen maximális összegű részlisták listája; a fenti példában:

```elixir
{10, [[1, 2, 3, 4], [1, 2, 3, 4, -10, 4, 3, 2, 1], [4, 3, 2, 1]]}
```

A `reszlistak/1` függvény specifikációja:

```elixir
  @spec reszlistak(xs::[integer()]) :: {max::integer(), rss::[[integer()]]}
  # rss az xs max összegű részlistáinak listája
```

Két megközelítést nézünk meg: az elsőben előállítjuk az összes folytonos részlistát, és a maximumot a legvégén keressük meg; a másodikban már a részlisták gyűjtése közben csak a maximális összegűeket tartjuk meg.

## 1. Maximumkeresés a legvégén

### 11. A lista elejétől kezdődő összes folytonos részlista

Az ablak bal széle a lista eleje, a jobb széle elemenként halad előre. Az `ss` akkumulátor fordított sorrendben tartalmazza az eddig bevett elemeket (így az új elemet olcsón elé lehet fűzni), a `zss` akkumulátor gyűjti az eddigi részlistákat, helyes sorrendre fordítva:

```elixir
defmodule Reszlistak11 do
  def reszlistak([x|xs]), do: reszlistak(xs, [x], [[x]])
  def reszlistak([]), do: []

  def reszlistak([y|ys], ss, zss) do
    ss_uj = [y|ss]
    reszlistak(ys, ss_uj, [Enum.reverse(ss_uj) | zss])
  end
  def reszlistak([], _ss, zss), do: zss
end
```

```elixir
Reszlistak11.reszlistak([1,2,3,4,5]) |> Enum.reverse()
```

```text
[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
```

### 12. A lista összes folytonos részlistája

Az ablak bal szélét is léptetni kell: a lista minden szuffixumára (a lista egyre rövidülő farkára) előállítjuk az elejétől kezdődő részlistákat:

```elixir
defmodule Reszlistak12 do
  def reszlistak(xxs), do: reszlistak(xxs, [])

  def reszlistak([_x|xs]=xxs, zss) do
    reszlistak(xs, Reszlistak11.reszlistak(xxs) ++ zss)
  end

  def reszlistak([], zss), do: zss
end
```

```elixir
Reszlistak12.reszlistak([1,2,3,4,5]) |> Enum.reverse()
```

```text
[
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 2, 3, 4],
  [1, 2, 3, 4, 5],
  [2],
  [2, 3],
  [2, 3, 4],
  [2, 3, 4, 5],
  [3],
  [3, 4],
  [3, 4, 5],
  [4],
  [4, 5],
  [5]
]
```

### 12x. Az összes folytonos részlista és az összegük

Kitérőként lássuk a részösszegeket is:

```elixir
defmodule Reszlistak12x do
  def reszlistak(xs), do: reszlistak(Reszlistak12.reszlistak(xs), [])

  def reszlistak([xs|xss], zss), do: reszlistak(xss, [{Enum.sum(xs), xs} | zss])
  def reszlistak([], zss), do: zss
end
```

```elixir
Reszlistak12x.reszlistak([1,2,-3,-4,5]) |> Enum.reverse()
```

```text
[
  {5, [5]},
  {1, [-4, 5]},
  {-4, [-4]},
  {-2, [-3, -4, 5]},
  {-7, [-3, -4]},
  {-3, [-3]},
  {0, [2, -3, -4, 5]},
  {-5, [2, -3, -4]},
  {-1, [2, -3]},
  {2, [2]},
  {1, [1, 2, -3, -4, 5]},
  {-4, [1, 2, -3, -4]},
  {0, [1, 2, -3]},
  {3, [1, 2]},
  {1, [1]}
]
```

### 13. A maximális összegű folytonos részlisták

Az összes részlista közül a maximális összegűeket egy újabb bejárással választjuk ki. A `max` akkumulátor az eddigi legnagyobb összeg, a `zss` az ilyen összegű részlisták listája. Ha egy részlista összege nagyobb az eddigi maximumnál, új maximumot és új gyűjtést kezdünk; ha egyenlő vele, hozzávesszük; ha kisebb, eldobjuk:

```elixir
defmodule Reszlistak13 do
  @spec reszlistak(xs::[integer()]) :: {max::integer(), rss::[[integer()]]}
  # rss az xs max összegű részlistáinak listája
  def reszlistak([_|_]=xs) do
    [rs|rss] = Reszlistak12.reszlistak(xs)
    reszlistak(rss, Enum.sum(rs), [rs])
  end
  def reszlistak([]), do: []

  @spec reszlistak(xs::[integer()], max::integer(), zss::[[integer()]]) :: rss::[[integer()]]
  # rss az xs max összegű részlistáinak listája; a részlistákat zss-ben gyűjtjük
  def reszlistak([xs|xss], max, zss) do
    sum = Enum.sum(xs)
    cond do
      sum > max -> reszlistak(xss, sum, [xs])
      sum == max -> reszlistak(xss, max, [xs | zss])
      true -> reszlistak(xss, max, zss)
    end
  end
  def reszlistak([], max, zss), do: {max, zss}
end
```

A `cond` kifejezés sorban kiértékeli a feltételeket, és az első igaz feltételhez tartozó kifejezés értékét adja; a `true` ág a „minden más” eset.

```elixir
Reszlistak13.reszlistak([1,2,13,4,5]) |> IO.inspect()
Reszlistak13.reszlistak([1,2,13,4,-10,4,13,2,1]) |> IO.inspect()
Reszlistak13.reszlistak([-13,-13,-13]) |> IO.inspect()
Reszlistak13.reszlistak([0,0,0]) |> IO.inspect()
Reszlistak13.reszlistak([-13]) |> IO.inspect()
Reszlistak13.reszlistak([]) |> IO.inspect()
```

```text
{25, [[1, 2, 13, 4, 5]]}
{30, [[1, 2, 13, 4, -10, 4, 13, 2, 1]]}
{-13, [[-13], [-13], [-13]]}
{0, [[0], [0, 0], [0, 0, 0], [0], [0, 0], [0]]}
{-13, [[-13]]}
[]
```

## 2. Maximumkiválasztás a részlisták gyűjtésekor

### 21. A lista elejétől kezdődő folytonos részlisták és összegük

```elixir
defmodule Reszlistak21 do
  def reszlistak([x|xs]), do: reszlistak(xs, [x], [{x, [x]}])
  def reszlistak([]), do: []

  def reszlistak([y|ys], ss, zss) do
    ss_uj = [y|ss]
    reszlistak(ys, ss_uj, [{Enum.sum(ss_uj), Enum.reverse(ss_uj)} | zss])
  end
  def reszlistak([], _ss, zss), do: zss
end
```

```elixir
Reszlistak21.reszlistak([1,2,3,4,5]) |> Enum.reverse() |> IO.inspect()
Reszlistak21.reszlistak([1,2,3,-3,-2,5]) |> Enum.reverse() |> IO.inspect()
```

```text
[
  {1, [1]},
  {3, [1, 2]},
  {6, [1, 2, 3]},
  {10, [1, 2, 3, 4]},
  {15, [1, 2, 3, 4, 5]}
]
[
  {1, [1]},
  {3, [1, 2]},
  {6, [1, 2, 3]},
  {3, [1, 2, 3, -3]},
  {1, [1, 2, 3, -3, -2]},
  {6, [1, 2, 3, -3, -2, 5]}
]
```

### 22a. A lista elejétől kezdődő, maximális összegű folytonos részlisták

Most már gyűjtés közben csak a maximális összegű részlistákat tartjuk meg:

```elixir
defmodule Reszlistak22a do
  def reszlistak([x|xs]), do: reszlistak(xs, [x], x, [[x]])
  def reszlistak([]), do: []

  def reszlistak([y|ys], ss, max, zss) do
    ss_uj = [y|ss]
    ss_uj_rev = Enum.reverse(ss_uj) # |> IO.inspect(label: "ss_uj_rev")
    sum = Enum.sum(ss_uj_rev) # |> IO.inspect(label: "sum")
    cond do
      sum > max -> reszlistak(ys, ss_uj, sum, [ss_uj_rev])
      sum == max -> reszlistak(ys, ss_uj, max, [ss_uj_rev | zss])
      true -> reszlistak(ys, ss_uj, max, zss)
    end
  end
  def reszlistak([], _ss, max, zss), do: {max, Enum.reverse(zss)}
end
```

```elixir
Reszlistak22a.reszlistak([1,2,3,-3,-2,5]) |> IO.inspect()
Reszlistak22a.reszlistak([6,-6,1,2,3,-3,-2,5]) |> IO.inspect()
```

```text
{6, [[1, 2, 3], [1, 2, 3, -3, -2, 5]]}
{6, [[6], [6, -6, 1, 2, 3], [6, -6, 1, 2, 3, -3, -2, 5]]}
```

### 22b. Ugyanez `Enum.take`-kel

Ez a változat a teljes listából indul, és a részlistákat az `Enum.take/2`-vel egyre rövidebb prefixumként állítja elő:

```elixir
defmodule Reszlistak22b do
  def reszlistak(xs), do: reszlistak(xs, length(xs)-1, Enum.sum(xs), [xs])

  def reszlistak(_xs, 0, max, zss), do: {max, zss}
  def reszlistak(xs, len, max, zss) do
    ss = Enum.take(xs, len)
    sum = Enum.sum(ss)
    cond do
      sum > max -> reszlistak(xs, len-1, sum, [ss])
      sum == max -> reszlistak(xs, len-1, max, [ss | zss])
      true -> reszlistak(xs, len-1, max, zss)
    end
  end
end
```

```elixir
Reszlistak22b.reszlistak([1,2,3,-3,-2,5]) |> IO.inspect()
Reszlistak22b.reszlistak([6,-6,1,2,3,-3,-2,5]) |> IO.inspect()
```

```text
{6, [[1, 2, 3], [1, 2, 3, -3, -2, 5]]}
{6, [[6], [6, -6, 1, 2, 3], [6, -6, 1, 2, 3, -3, -2, 5]]}
```

### 23. A maximális összegű folytonos részlisták

A lista minden szuffixumára meghívjuk a 22a vagy a 22b változatot, és az eredményekből csak a maximális összegűeket tartjuk meg. Az elejétől kezdődő maximális részlistákat előállító függvényt paraméterként (`mxrls`) adjuk át, így a két változat ugyanazzal a kerettel használható:

```elixir
defmodule Reszlistak23 do
  @type mxrls() :: ([integer()] -> [[integer()]])
  @spec reszlistak(f::mxrls(), xs::[integer()]) :: {max::integer(), rss::[[integer()]]}
  # rss az xs max összegű részlistáinak listája
  # f egy számlista elejétől kezdődő, folytonos, max. összegű részlistákat adja eredményül
  def reszlistak(mxrls, [_x|xs]=xxs), do: reszlistak(mxrls, xs, mxrls.(xxs))
  def reszlistak(_mxrls, []), do: {}

  def reszlistak(mxrls, [_y|ys]=yys, {maxsum, zss}) do
    {max, mss} = mxrls.(yys)
    cond do
      max > maxsum -> reszlistak(mxrls, ys, {max, mss})
      max == maxsum -> reszlistak(mxrls, ys, {maxsum, zss ++ mss}) # hatékonyság vs. sorrend!
      true -> reszlistak(mxrls, ys, {maxsum, zss})
    end
  end
  def reszlistak(_mxrls, [], maxlists), do: maxlists
end
```

A `zss ++ mss` megőrzi a részlisták sorrendjét, de a `++` az első listát lemásolja; a `mss ++ zss` olcsóbb lenne, de felcserélné a sorrendet.

```elixir
(&Reszlistak22a.reszlistak/1) |> Reszlistak23.reszlistak([1,2,3,4,5]) |> IO.inspect()
(&Reszlistak22a.reszlistak/1) |> Reszlistak23.reszlistak([1,2,3,4,-10,4,3,2,1]) |> IO.inspect()
(&Reszlistak22b.reszlistak/1) |> Reszlistak23.reszlistak([1,2,3,4,5]) |> IO.inspect()
(&Reszlistak22b.reszlistak/1) |> Reszlistak23.reszlistak([1,2,3,4,-10,4,3,2,1]) |> IO.inspect()
```

```text
{15, [[1, 2, 3, 4, 5]]}
{10, [[1, 2, 3, 4], [1, 2, 3, 4, -10, 4, 3, 2, 1], [4, 3, 2, 1]]}
{15, [[1, 2, 3, 4, 5]]}
{10, [[1, 2, 3, 4], [1, 2, 3, 4, -10, 4, 3, 2, 1], [4, 3, 2, 1]]}
```

## Futási idők összehasonlítása

A futási idők mérésére véletlenszerű számok listáját használjuk. Egy 10 hosszúságú, a -5..5 tartományba eső számokat tartalmazó sorozatot például így állíthatunk elő (az eredmény minden futtatáskor más):

```elixir
for _ <- 1..10, do: Enum.random(-5..5)
```

```text
[-5, 4, -2, -2, -5, 0, 2, 1, 4, -3]
```

A mérés egy 1000 elemű véletlen listán:

```elixir
xs = for _ <- 1..1000, do: Enum.random(-5..5)
Benchee.run(
  %{
    "utolag keres"  =>
      fn -> Reszlistak13.reszlistak(xs) end,
    "menet kozben, sajat fv"  =>
      fn -> Reszlistak23.reszlistak(&Reszlistak22a.reszlistak/1, xs) end,
    "menet kozben, Enum.take"  =>
      fn -> Reszlistak23.reszlistak(&Reszlistak22b.reszlistak/1, xs) end
  }# , profile_after: true
)
:ok
```

Az eredmény (Elixir 1.20.2, Erlang 29.0.6, AMD Ryzen AI 9 HX 370):

```text
Name                              ips        average  deviation         median         99th %
menet kozben, sajat fv           2.26      442.21 ms     ±2.22%      438.00 ms      465.67 ms
menet kozben, Enum.take          1.42      702.56 ms     ±1.30%      702.25 ms      720.61 ms
utolag keres                     0.33     3016.53 ms    ±44.34%     3169.76 ms     4270.77 ms

Comparison: 
menet kozben, sajat fv           2.26
menet kozben, Enum.take          1.42 - 1.59x slower +260.35 ms
utolag keres                     0.33 - 6.82x slower +2574.31 ms
```

A menet közbeni maximumkiválasztás több mint hatszor gyorsabb, mert nem kell az összes (1000 elemű listánál félmilliónál több) részlistát egyszerre tárolni és utólag újra bejárni.

<p class="sources">Forrás: dp26a-fp3ea.pdf (4. dia), dp26a-fp3ea-reszlistak-kihagy_bevesz_rek.livemd</p>
