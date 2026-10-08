# Műveletek listákon

## A lista költségei

A lista láncolt lineáris adatstruktúra, ezért olcsó az első elemét (a fejét) és az összes többi elemét (a farkát) megkapni, de drága az utolsó elemét elérni, mert végig kell gyalogolni a listán.

A funkcionális nyelvekben – a többi adatstruktúrához hasonlóan – a lista nem frissíthető, az Elixirben sem. Ha a lista egy elemét le akarjuk cserélni, másolatot kell készítenünk a lecserélendő elem előtti részlistáról. A másolás során a lecserélendő elem előtti összes elemet félre kell raknunk, majd a lecserélendő elem utáni farokrész elé be kell fűznünk az új elemet, ezt követően pedig a félrerakott elemeket egyesével be kell fűznünk az új elemet már tartalmazó listarész elé. A lista adott elem utáni farkáról viszont nem készül másolat: az Elixir **megosztja** a lista farkát a régi és az új elemet tartalmazó lista között.

## Alapműveletek

A `Kernel` modulban definiált alapműveletek:

- Lista feje, farka, hossza: `hd(xs)`, `tl(xs)`, `length(xs)`.
- Két lista összefűzése (konkatenációja): `xs ++ ys`; eredménye `xs` összes eleme `ys` elé fűzve, az eredeti sorrendben.
- Két lista különbsége: `xs -- ys`; eredménye `xs` azon elemeinek listája az eredeti sorrendben, amelyek nincsenek benne `ys`-ben. Az `ys` minden eleme `xs`-ből legfeljebb egy előfordulást töröl, balról az elsőt.
- Tagsági vizsgálat: `x in xs` eredménye `true`, ha `x` eleme `xs`-nek.

```iex
iex> [:a, 'a', [65]] ++ [1+2, 2/1, 'a'] # 65 == ?A
[:a, ~c"a", ~c"A", 3, 2.0, ~c"a"]
iex> Enum.to_list(1..100000) ++ [100001] # rossz hatékonyságú!
[1, 2, 3, 4, 5, 6, 7, 8, ...100001]
iex> [:a, 'a', [65], 'a'] -- ["A", 2/1, 'a']
[:a, ~c"A", ~c"a"]
iex> [:a, 'a', [65], 'a'] -- ["A", 2/1, 'a', :a, :a, :a]
[~c"A", ~c"a"]
iex> [1, 2, 3] -- [1.0, 2] # szigorú egyenlőség: 1 !== 1.0
[1, 3]
iex> "A" in ["A", 2/1, 'a', :a, :a, :a]
true
```

A `++` az első listát lemásolja, ezért egy hosszú lista végére egyetlen elemet fűzni rossz hatékonyságú. A `--` szigorú egyenlőséggel hasonlít, ezért az `1.0` nem törli az `1`-et.

## A `List` modul függvényei

- Lista első / utolsó eleme; ha nincs, `default` vagy `nil`: `first(list, default \\ nil)`, `last(list, default \\ nil)`.
- Egy elem első előfordulásának törlésével kapott lista: `delete(list, elem)`.
- Adott pozíciójú elem törlésével / beszúrásával / cseréjével kapott lista: `delete_at(list, index)`, `insert_at(list, index, value)`, `replace_at(list, index, value)`, `update_at(list, index, fun)`. Az indexelés 0-tól indul, a negatív index a lista végéről. Az `update_at/3` a `fun` függvényt alkalmazza az adott pozíciójú elemre.
- Lista kilapításával / kilapítása után a `tail` elé fűzésével kapott lista: `flatten(list)`, `flatten(list, tail)`.
- Elem többszörözésével kapott lista: `duplicate(elem, n)`.
- Listák listájából ennesek listája: `zip(list_of_lists)`; a hosszabb listák végét levágja.
- Konverziós függvények, pl. `List.to_string`, `Tuple.to_list`.
- Három tesztelő függvény:
  - `improper?(list)` igaz, ha `list` *nem valódi* lista, azaz egy listakonstruktorban a farok *nem* lista, pl. `[1,2|3]`, `[:a,:b|nil]`;
  - `starts_with?(list, prefix)` igaz, ha `list` `prefix`-szel kezdődik;
  - `ascii_printable?(list, n \\ :infinity)` igaz, ha `list` első `n` karaktere 7 bites ASCII-kódolású és nyomtatható, beleértve a vezérlő karaktereket is (`\a`, `\b`, `\t`, `\n`, `\v`, `\f`, `\r`, `\e`).

```iex
iex> List.zip([[:a, :b, :c], [:d, :e, :f, :g, :h], [:i, :j, :k, :l]])
[{:a, :d, :i}, {:b, :e, :j}, {:c, :f, :k}] # Listák vége levágva
iex> List.flatten(['abc', [['defgh']], ['ijkl']], 'zzz')
~c"abcdefghijklzzz"
iex> List.starts_with? 'almafa', [?a, ?l]
true
```

## Az `Enum` modul függvényei

Az `Enum` modul függvényei is alkalmazhatók listákra:

- Lista megfordításával / megfordítása után a `tail` elé fűzésével kapott lista: `reverse(list)`, `reverse(list, tail)`.
- Lista adott indexű eleme, ha nincs ilyen, `default` vagy `nil`: `at(list, index, default \\ nil)`.
- Lista legkisebb / legnagyobb eleme: `min(list, sorter \\ &<=/2, empty_fallback \\ fn -> raise(Enum.EmptyError) end)`. A `max/3` paraméterezése hasonló, `&<=/2` helyett `&>=/2`-vel. Ha `list` üres, a harmadik paraméterként átadott függvény aktivizálódik.
- Lista `n` elemű eleje, `n` elem utáni farka: `take(list, n)`, `drop(list, n)`. Ha `n` negatív, az elemeket a lista végéről kezdve emeli le / dobja el.
- Lista részlistája: `slice(list, range)` a `range` tartományba eső indexű elemek listája, `slice(list, start, n)` a `start` indextől kezdődő `n` elemű részlista. Ha `range`, illetve `start` negatív, az indexelés a lista végéről indul.
- Lista kettévágva: `split(list, n)`, ugyanaz, csak rövidebben, mint `{(take list, n), (drop list, n)}`.
- Lista rendezve alapértelmezés / `fun` függvény szerint: `sort(list)`, `sort(list, fun)`.
- Lista többszörös értékek nélkül: `uniq(list)`.

```iex
iex> Enum.reverse 'almafa'
~c"afamla"
iex> Enum.at 'almafa', 2
109
iex> {(Enum.max 'mióta') === ?ó, (Enum.min [], fn -> 0 end)}
{true, 0}
iex> xs='indulakutyasatyukaludni'; {(Enum.take xs,-5), (Enum.drop xs,5)}
{~c"ludni", ~c"akutyasatyukaludni"}
iex> {(Enum.slice xs, 6..10), (Enum.slice xs, -10..-7)}
{~c"kutya", ~c"tyuk"}
iex> xs='indulakutyasatyukaludni'; [(Enum.split xs,5),(Enum.split xs,-5)]
[{~c"indul", ~c"akutyasatyukaludni"}, {~c"indulakutyasatyuka", ~c"ludni"}]
iex> Enum.sort xs
~c"aaaaddiikkllnnsttuuuuyy"
iex> Enum.sort xs, &>=/2
~c"yyuuuuttsnnllkkiiddaaaa"
iex> Enum.uniq xs
~c"indulaktys"
```

Az `Enum.at 'almafa', 2` eredménye a `?m` karakterkód, azaz 109.

Az `Enum` modul függvényei – mind **mohó** kiértékelésűek – egyéb korlátos, felsorolható (*enumerable*) adatstruktúrákra is alkalmazhatók. Nem korlátos adatstruktúrákra a `Stream` modul **lusta** kiértékelésű függvényeit lehet használni.

## Rövid példák

Mintaillesztés, változók kötése és újrakötése listákkal:

```iex
iex> xs = [10,20,30] # mintaillesztés és változó kötése értékhez
[10, 20, 30]
iex> x = hd xs       # hd: lista feje
10
iex> rs = tl xs      # tl: lista farka
[20, 30]
iex> {zs,xs} = {xs,[5,6]} # mintaillesztés és változó újrakötése
{[10, 20, 30], [5, 6]}
iex> xs              # xs-hez új értéket kötöttünk
[5, 6]
iex> zs              # xs változott, zs nem!
[10, 20, 30]
iex> ^xs = [7,8,9]   # ^: változó 'fixálása', csak mintaillesztés, kötés nélkül
** (MatchError) no match of right hand side value: ~c"\a\b\t"
iex> hd tl xs       # összetett kifejezés is kiértékelhető
6
iex> tl []           # mi az üres lista farka?
** (ArgumentError) errors were found at the given arguments:
  * 1st argument: not a nonempty list
    :erlang.tl([])
```

A `[7,8,9]` lista vezérlő karakterek kódjaiból áll, ezért a hibaüzenet karakterláncként írja ki.

A nyomtatható karakterkódok (7..13, 27, 32..126) egyelemű listái:

```iex
iex> for i <- 7..13, do: [i]
[~c"\a", ~c"\b", ~c"\t", ~c"\n", ~c"\v", ~c"\f", ~c"\r"]
iex> for i <- 27..27, do: [i]
[~c"\e"]
iex> for i <- 32..126, do: [i]
[~c" ", ~c"!", ~c"\"", ~c"#", ~c"$", ~c"%", ~c"&", ~c"'", ~c"(", ~c")", ~c"*",
 ~c"+", ~c",", ~c"-", ~c".", ~c"/", ~c"0", ~c"1", ~c"2", ~c"3", ~c"4", ~c"5",
 ~c"6", ~c"7", ~c"8", ~c"9", ~c":", ~c";", ~c"<", ~c"=", ~c">", ~c"?", ~c"@",
 ~c"A", ~c"B", ~c"C", ~c"D", ~c"E", ~c"F", ~c"G", ~c"H", ~c"I", ~c"J", ~c"K",
 ~c"L", ~c"M", ~c"N", ~c"O", ~c"P", ~c"Q", ...]
iex> IO.puts (for i <- 35..126, do: [i])
#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
:ok
iex> IO.inspect (for i <- 32..126, do: [i]), limit: :infinity
[~c" ", ~c"!", ~c"\"", ~c"#", ~c"$", ~c"%", ~c"&", ~c"'", ~c"(", ~c")", ~c"*",
 ~c"+", ~c",", ~c"-", ~c".", ~c"/", ~c"0", ~c"1", ~c"2", ~c"3", ~c"4", ~c"5",
 ~c"6", ~c"7", ~c"8", ~c"9", ~c":", ~c";", ~c"<", ~c"=", ~c">", ~c"?", ~c"@",
 ~c"A", ~c"B", ~c"C", ~c"D", ~c"E", ~c"F", ~c"G", ~c"H", ~c"I", ~c"J", ~c"K",
 ~c"L", ~c"M", ~c"N", ~c"O", ~c"P", ~c"Q", ~c"R", ~c"S", ~c"T", ~c"U", ~c"V",
 ~c"W", ~c"X", ~c"Y", ~c"Z", ~c"[", ~c"\\", ~c"]", ~c"^", ~c"_", ~c"`", ~c"a",
 ~c"b", ~c"c", ~c"d", ~c"e", ~c"f", ~c"g", ~c"h", ~c"i", ~c"j", ~c"k", ~c"l",
 ~c"m", ~c"n", ~c"o", ~c"p", ~c"q", ~c"r", ~c"s", ~c"t", ~c"u", ~c"v", ~c"w",
 ~c"x", ~c"y", ~c"z", ~c"{", ~c"|", ~c"}", ~c"~"]
[~c" ", ~c"!", ~c"\"", ~c"#", ~c"$", ~c"%", ~c"&", ~c"'", ~c"(", ~c")", ~c"*",
 ~c"+", ~c",", ~c"-", ~c".", ~c"/", ~c"0", ~c"1", ~c"2", ~c"3", ~c"4", ~c"5",
 ~c"6", ~c"7", ~c"8", ~c"9", ~c":", ~c";", ~c"<", ~c"=", ~c">", ~c"?", ~c"@",
 ~c"A", ~c"B", ~c"C", ~c"D", ~c"E", ~c"F", ~c"G", ~c"H", ~c"I", ~c"J", ~c"K",
 ~c"L", ~c"M", ~c"N", ~c"O", ~c"P", ~c"Q", ...]
```

Az alapértelmezett kiírás az 50. elem után levágja a listát (`...`); a `limit: :infinity` opcióval az `IO.inspect` a teljes listát kiírja, majd az IEx a visszaadott értéket ismét, alapértelmezett módon.

### Számlista összege

Az `fpea.ex` fájlba írt `sum/1` a lista fejét és farkát a `hd` és `tl` függvénnyel kéri el. A `, do:` jelölés többsoros változata a `do ... end`; egy sorban a `;` választja el a kifejezéseket:

```elixir
@spec sum(xs::[integer]) :: s::integer
# Az xs számlista összege s
def sum([]), do: 0 # a ", do:" jelölés többsoros változata a "do ... end"
def sum(xs)  do x = hd xs; rs = tl xs; x + sum rs end # újsor helyett ;
```

```iex
iex> c "fpea.ex"
[Fpea]
iex> xs = [10, 20.5, 30.5]
[10, 20.5, 30.5]
iex> Fpea.sum xs
61.0
iex> Fpea.sum tl xs
51.0
iex> Fpea.sum(tl(tl(tl xs)))
0
iex> Fpea.sum "abc" # "abc" !== [97, 98, 99]: "abc" sztring, nem lista
** (ArgumentError) errors were found at the given arguments:
  * 1st argument: not a nonempty list
    :erlang.hd("abc")
    fpea.ex:13: Fpea.sum/1
iex> Fpea.sum 'abc' # 'abc' === [97, 98, 99]: 'abc' karakterkódok listája
294
```

### Két lista összefűzése, megfordítva összefűzése

Az `append/2` két listát fűz össze, a `revapp/2` az első listát megfordítva fűzi a második elé. Az utóbbi jobbrekurzív: a fejet az akkumulátorként használt `ys` elé teszi.

```elixir
@spec append(xs::[any], ys::[any]) :: rs::[any]
# rs az xs lista ys elé fűzésével kapott lista
def append([], ys), do: ys
def append(xs, ys), do: [(hd xs) | (append (tl xs), ys)]
@spec revapp(xs::[any], ys::[any]) :: rs::[any]
# rs a megfordított xs lista ys elé fűzésével kapott lista
def revapp([], ys), do: ys
def revapp(xs, ys), do: revapp (tl xs), [(hd xs) | ys]
```

```iex
iex> c "fpea.ex"
[Fpea]
iex> xs
[10, 20.5, 30.5]
iex> Fpea.append(xs, [:a,:b,:c,:d])
[10, 20.5, 30.5, :a, :b, :c, :d]
iex> Fpea.revapp xs, [:a,:b,:c,:d]
[30.5, 20.5, 10, :a, :b, :c, :d]
```

## Gyakorló feladatok

Írjon többféle megoldást a feladatokra: saját rekurzív függvényekkel, különféle könyvtári függvények – minél több magasabb rendű függvény (`Enum.map/2`, `Enum.filter/2`, `Enum.reduce/3`, `List.foldr/3`, `List.foldl/3` stb.) – felhasználásával, valamint `for`-komprehenzióval ([For-jelölés](for.md)). Hasonlítsa össze a megoldások futási idejét a `benchee`-vel, próbáljon hatékonyabb kódot írni, pl. jobbrekurzióval. A specifikációk típus- és függvényspecifikációinak helyességét a dialyzerrel ellenőrizheti ([Típusellenőrzés: dialyzer](elixir/mix.md#típusellenőrzés-dialyzer)).

### Lista kettévágása

Írjon függvényt egy lista kettévágására! Írhat segédfüggvényt, használhat akkumulátort és jobbrekurziót, használhatja a `for`-jelölést. Ne használja az `Enum.split*`, `Enum.take*` és `Enum.drop*` függvények semelyik változatát a `split/2` függvény megvalósítására (de bármilyen könyvtári függvényt használhat az eredmény ellenőrzésére)!

```elixir
defmodule Split do
  @spec split(xs :: [any()], n :: integer()) :: {ps :: [any()], ss :: [any()]}
  # Az xs lista n hosszú prefixuma (első n eleme) ps, length(xs)-n
  # hosszú szuffixuma (első n eleme utáni része) pedig ss
  def split(xs, n) do
  ...
  end
end
IO.puts(Split.split([10, 20, 30, 40, 50], 3) === {[10, 20, 30], [40, 50]})
IO.puts(IO.inspect(Split.split(~c"egyedem-begyedem", 8)) === Enum.split(~c"egyedem-begyedem", 8))
IO.puts(IO.inspect(Split.split(~c"papás-mamás", 6)) === Enum.split(~c"papás-mamás", 6))
IO.puts(Split.split(~c"nem_vágom", 0) === Enum.split(~c"nem_vágom", 0))
IO.puts(Split.split(~c"", 10) === Enum.split(~c"", 10))
IO.puts(Split.split(~c"", 0) === Enum.split(~c"", 0))
```

<details>
<summary>Megoldás</summary>

Törzsrekurzív változat: a rekurzív hívás eredményét mintaillesztéssel bontja szét, és a fejet az első rész elé teszi.

```elixir
defmodule Split1 do
  @spec split(xs :: [any()], n :: integer()) :: {ps :: [any()], ss :: [any()]}
  # Az xs lista n hosszú prefixuma (első n eleme) ps, length(xs)-n
  # hosszú szuffixuma (első n eleme utáni része) pedig ss
  def split(xs, 0), do: { [], xs }
  def split([x|xs], n) do
    { ps, ss } = split(xs, n-1)
    { [x|ps], ss }
  end
  def split([], _), do: { [], [] }
end
```

Jobbrekurzív változat akkumulátorral; az akkumulátorban fordított sorrendben gyűlnek az elemek, ezért a végén meg kell fordítani:

```elixir
defmodule Split2 do
  @spec split(xs :: [any()], n :: integer()) :: {ps :: [any()], ss :: [any()]}
  # Az xs lista n hosszú prefixuma (első n eleme) ps, length(xs)-n
  # hosszú szuffixuma (első n eleme utáni része) pedig ss
  def split(xs, n), do: split(xs, n, [])
  defp split([x|xs], n, ps) when n > 0, do: split(xs, n-1, [x|ps])
  defp split(xs, 0, ps), do: { Enum.reverse(ps), xs }
  defp split([], _, ps), do: { Enum.reverse(ps), [] }
end
```

Mindkét változattal minden teszt `true`-t ír ki. Az `IO.inspect` a `{~c"egyedem-", ~c"begyedem"}` és a `{[112, 97, 112, 225, 115, 45], [109, 97, 109, 225, 115]}` párt is kiírja (az `á` kódja, 225, nem nyomtatható ASCII-kód, ezért a második pár számokkal jelenik meg). A mérés:

```elixir
ls = Range.to_list(0..100_000)
n = 70_000
Benchee.run(%{
    "split1" => fn -> Split1.split(ls, n) end,
    "split2" => fn -> Split2.split(ls, n) end,
    "enumSplit" => fn -> Enum.split(ls, n) end
})
```

</details>

### Lista adott feltételt kielégítő elemeiből álló prefixuma

Írjon függvényt egy lista adott feltételt kielégítő prefixumának előállítására! Írhat segédfüggvényt, használhat akkumulátort és jobbrekurziót, használhatja a for-jelölést. Ne használja az `Enum.split*`, `Enum.take*` és `Enum.drop*` függvények semelyik változatát a `takewhile/2` függvény megvalósítására (de bármilyen könyvtári függvényt használhat az eredmény ellenőrzésére)!

```elixir
defmodule Take do
  @spec takewhile(xs :: [any()], f :: (any() -> boolean())) :: rs :: [any()]
  def takewhile(xs, f) do
  ...
  end
end
IO.puts(Take.takewhile(~c"álom12" ++ [:a] ++ ~c"34brigád", &is_integer/1) === ~c"álom12")
IO.puts(Take.takewhile(~c"abcdefghijkl", fn x -> x < ?f end) === ~c"abcde")
```

<details>
<summary>Megoldás</summary>

```elixir
defmodule Take1 do
  @spec takewhile(xs :: [any()], f :: (any() -> boolean())) :: rs :: [any()]
  def takewhile([x|xs], f) do
    if f.(x) do
      [x|takewhile(xs, f)]
    else
      []
    end
  end
  def takewhile([], _f), do: []
end
```

```elixir
defmodule Take2 do
  @spec takewhile(xs :: [any()], f :: (any() -> boolean())) :: rs :: [any()]
  def takewhile(xs, f), do: takewhile(xs, f, [])
  defp takewhile([x|xs], f, acc) do
    if f.(x) do
      takewhile(xs, f, [x|acc])
    else
      Enum.reverse(acc)
    end
  end
  defp takewhile([], _f, acc), do: Enum.reverse(acc)
end
```

Mindkét változattal mindkét teszt `true`-t ír ki. A mérés:

```elixir
ls = Range.to_list(0..100_000)
f = fn x -> x < 70_000 end
Benchee.run(%{
    "take1" => fn -> Take1.takewhile(ls, f) end,
    "take2" => fn -> Take2.takewhile(ls, f) end,
    "enumTake" => fn -> Enum.take_while(ls, f) end
})
```

</details>

### Lista minden n-edik elemének kihagyásával létrejövő lista

Írjon függvényt egy olyan lista létrehozására, amelyből a paraméterként átadott lista minden n-edik eleme, a nulladiktól kezdve, ki van hagyva! (A listák indexelése 0-val kezdődik.) Ne használja az `Enum.split*`, `Enum.take*` és `Enum.drop*` függvények semelyik változatát a `dropevery/2` függvény megvalósítására (de bármilyen könyvtári függvényt használhat az eredmény ellenőrzésére)! Tipp: ha nem ír segédfüggvényt, és nincs más ötlete, használhatja a `for`-jelölést, generátoraként a `../2`, szűrőjeként a `rem/2` függvényt, a listaelemek elérésére pedig az `Enum.at/2` függvényt.

```elixir
defmodule Drop do
  @spec dropevery(xs :: [any()], n :: integer()) :: rs :: [any()]
  def dropevery(xs, n) do
    ...
  end
end
ls = ~c"álom" ++ [:a] ++ ~c"egybrigád"
IO.inspect(Drop.dropevery(ls, 4) === ~c"lomegyrigd")
ls = ~c"abcdefghijkl"
IO.inspect(Drop.dropevery(ls, 5) === ~c"bcdeghijl")
ls = ~c"1234567"
IO.inspect(Drop.dropevery(ls, 2) === ~c"246")
ls = []
IO.inspect(Drop.dropevery(ls, 3) === [])
ls = [:a, :b, :c, :d, :e, :f, :g, :h, :i, :j, :k, :l, :m]
IO.inspect(Drop.dropevery(ls, 3) === [:b, :c, :e, :f, :h, :i, :k, :l])
```

### Lista egyre rövidülő szuffixumainak listája

Írjon olyan függvényt, amely egy `xs` lista elemeiből álló részlistákat ad eredményül: az első részlista maga az `xs` legyen, a második az `xs` második, azaz 1 indexű elemétől a végéig tartson, a harmadik az `xs` harmadik, azaz 2 indexű elemétől a végéig, és így tovább; az utolsó részlista az üres lista legyen. Tipp: a `tails` függvény eredménye listák listája, így üres listára alkalmazva olyan lista a visszatérési értéke, amelynek egyetlen eleme van, az üres lista.

```elixir
defmodule Tails do
  @spec tails(xs :: [any()]) :: zss :: [[any()]]
  # Az xs lista egyre rövidülő szuffixumainak listája zss
  def tails(xs) do
  ...
  end
end
IO.puts(Tails.tails([1, 4, 2]) === [[1, 4, 2], [4, 2], [2], []])
IO.puts(Tails.tails([:a, :b, :c, :d]) === [[:a, :b, :c, :d], [:b, :c, :d], [:c, :d], [:d], []])
IO.puts(Tails.tails([:z]) === [[:z], []])
IO.puts(Tails.tails([]) === [[]])
```

### Lista egymást követő két-két eleméből képzett párok listája

Írjon olyan rekurzív függvényt, amely egy lista 1. és 2., 3. és 4., 5. és 6. stb. elemeiből képzett párok listáját adja eredményül! Ha a listának kettőnél kevesebb eleme van, az eredmény az üres lista legyen. Ha a listának páratlan számú eleme van, az utolsót dobja el.

```elixir
defmodule Pairs do
  @spec pairs(xs::[any()]) :: zs :: [any()]
  def pairs(xs), do: ...
end
zs = [{1,2}, {3,4}, {5,6}, {7,8}, {9,10}, {11,12}, {13,14}, {15,16}, {17,18}, {19,20}]
(1..20 |> Range.to_list() |> Pairs.pairs() == zs) |> IO.puts
zs = [{1,2}, {3,4}, {5,6}, {7,8}, {9,10}]
(1..11 |> Range.to_list() |> Pairs.pairs() == zs) |> IO.puts
([1] |> Pairs.pairs() == []) |> IO.puts
```

### Listában párosával előforduló elemek listája

Írjon olyan rekurzív függvényt, amely egy lista elemei közül az összes olyat visszaadja az eredménylistában, amelyet vele azonos értékű elem követ: például két egymást követő, azonos értékű elemből egyet, három egymást követőből kettőt stb. Írhat

1. segédfüggvényt és akkumulátort nem használó, valamint
2. akkumulátoros segédfüggvényt használó változatot.

Próbáljon meg egyéb változatokat is írni, pl.

3. a `for`-jelöléssel és az `Enum.zip/1` függvény alkalmazásával.

```elixir
defmodule Parosan do
  @spec parosan(xs :: [any()]) :: rs :: [any()]
  # Az xs lista összes olyan elemének listája rs, amely
  # után vele azonos értékű elem áll
  def parosan xs do
  ...
  end
end
IO.puts(Parosan.parosan([:a, :a, :a, 2, 3, 3, :a, 2, :b, :b, 4, 4]) === [:a, :a, 3, :b, 4])
IO.puts(Parosan.parosan([:a, 2, 3, :a, 2, :b, 4]) === [])
IO.puts(Parosan.parosan([:a]) === [])
IO.puts(Parosan.parosan([]) === [])
```

### Lista elején azonos értékű elemekből álló részlisták listája

Írjon függvényt olyan nem üres, folytonos részlisták előállítására, amelyek egy lista elejétől indulnak, és velük azonos értékű és elemszámú részlisták követik őket! Példák:

- `[1,1]` ⟶ `[[1]]`: a lista elején kezdődő `[1]` részlistát az `[1]` részlista követi.
- `[1,1,1]` ⟶ `[[1]]`: a lista elején kezdődő `[1]` részlistát az `[1]` részlista követi, de a lista elején kezdődő `[1,1]` részlistát már nem követi azonos értékű részlista.
- `[1,1,0,0]` ⟶ `[[1]]`: a lista elején kezdődő `[1]` részlistát az `[1]` részlista követi, de a `[0]` részlista már nem a lista elején kezdődik.
- `[1,1,1,1]` ⟶ `[[1], [1, 1]]`: a lista elején kezdődő `[1]` és `[1, 1]` részlistákat azonos értékű részlisták követik.
- `[1,1,1,1,1]` ⟶ `[[1], [1, 1]]`: a lista elején kezdődő `[1]` és `[1, 1]` részlistákat azonos értékű részlisták követik, de a lista elején kezdődő `[1, 1, 1]` részlistát már nem követi azonos értékű részlista.
- `[1,1,0,1,1]` ⟶ `[[1]]`: a lista elején kezdődő `[1]` részlistát az `[1]` részlista követi, de nincs több olyan ismétlődő részlista, amely a lista elején kezdődne.
- `[1,1,1,1,1,1]` ⟶ `[[1], [1, 1], [1, 1, 1]]`: a lista elején kezdődő `[1]`, `[1, 1]` és `[1, 1, 1]` részlistákat azonos értékű részlisták követik.

Lehetőleg írjon többféle változatot, pl. akkumulátort használó és nem használó, könyvtári függvényeket alkalmazó és nem alkalmazó változatot. Tipp: ha nincs jobb ötlete, használja az `Enum.take/2` és `Enum.drop/2` függvényt egy segédfüggvényben.

```elixir
defmodule Repeated1 do
  @spec repeated(xs :: [any()]) :: rs :: [any()]
  def repeated(xs) do
  ...
  end
end
(Repeated1.repeated([1,1]) == [[1]]) |> IO.inspect
(Repeated1.repeated([1,1,1]) == [[1]]) |> IO.inspect
(Repeated1.repeated([1,1,0,0]) == [[1]]) |> IO.inspect
(Repeated1.repeated([1,1,1,1]) == [[1], [1, 1]]) |> IO.inspect
(Repeated1.repeated([1,1,1,1,1]) == [[1], [1, 1]]) |> IO.inspect
(Repeated1.repeated([1,1,0,1,1]) == [[1]]) |> IO.inspect
(Repeated1.repeated([1,1,1,1,1,1]) == [[1], [1, 1], [1, 1, 1]]) |> IO.inspect

(Repeated1.repeated([:a, :a, :a, 2, 3, 3, :a, :b, :b, :b, :b]) === [[:a]]) |> IO.inspect
(Repeated1.repeated([:a, :b, :b, :b, :b]) === []) |> IO.inspect
(Repeated1.repeated([:b, :b, :b, :b]) === [[:b], [:b, :b]]) |> IO.inspect
(Repeated1.repeated([]) === []) |> IO.inspect
```

### Listában párosával előforduló részlisták listája

Írjon függvényt egy lista összes olyan nem üres, folytonos részlistájának előállítására, amelyet vele azonos értékű részlista követ! Lehetőleg írjon többféle változatot. Tipp: használja a `Tails.tails/1` függvényt; felhasználhatja a `Repeated1.repeated/1` vagy egy `Repeated2.repeated/1` függvényt is.

```elixir
defmodule Stammering do
  @spec stammering(xs :: [any()]) :: zss :: [[any()]]
  # zss az xs lista összes olyan nemüres, folytonos részlistájából
  # álló lista, amelyet vele azonos értékű részlista követ
  def stammering(xs) do
    ...
  end
end
(Stammering.stammering([:a, :a, :a, 2, 3, 3, :a, :b, :b, :b, :b]) ===
  [[:a], [:a], [3], [:b], [:b, :b], [:b], [:b]]) |> IO.puts()
IO.puts(Stammering.stammering([]) === [])
IO.puts(Stammering.stammering([:a]) === [])
IO.puts(Stammering.stammering([:a, :a]) === [[:a]])
IO.puts(Stammering.stammering([:a, :b]) === [])
```

<p class="sources">Forrás: dp26a-fp2ea.pdf (28–38. dia), dp26a-fp2gy-megoldasok.livemd, dp26a-fp3gy.livemd</p>
