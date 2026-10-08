# For-jelölés

Gyűjtemények (kollekciók) kezelésére a **for-jelölést** használjuk; az angol elnevezést teljesen átvéve **for-komprehenziónak** (*for-comprehension*) is nevezik. A komprehenzió ma már sokféle programozási nyelvben megtalálható (<https://en.wikipedia.org/wiki/List_comprehension>); a for-jelölés részletes összefoglalója: <https://www.mitchellhanberg.com/the-comprehensive-guide-to-elixirs-for-comprehension/>.

## Alakja és jelentése

Az alábbiakban a szögletes zárójelek jelentése: *opcionális*.

`for` q₁[, q₂, ..., qₙ][, `into:` coll], `do:` exp

ahol

- a qᵢ
  1. `pattern <- list` alakú *generátor*, vagy
  2. *predikátum* (igazságérték-eredményű függvény, feltétel);
- legalább egy qᵢ-nek *generátornak* kell lennie;
- a `pattern` mintának illeszkednie kell a `list` lista kiválasztandó elemeire, és ki kell elégítenie az adott `pattern <- list` generátortól jobbra álló összes qᵢ predikátumot;
- az `exp` tetszőleges, a `pattern` mintától függő vagy nem függő kifejezés;
- a generátorban a minta előállítására lista helyett más felsorolható kollekciót, leggyakrabban tartomány típusú értéket is megadhatunk;
- az opcionális `into:` után álló `coll`-lal megadhatjuk, hogy milyen típusú felsorolható kollekciót hozzon létre a for-jelölés; ha elhagyjuk, alapértelmezés szerint lista jön létre. `coll`-ként üres kollekciót kell megadni: `""` (sztring), `%{}` (szótár), `[]` (lista), `<<>>` (bináris);
- a for-jelölésben definiált változók lokálisak.

A for-jelölés értéke az összes olyan `exp` kifejezés kollekciója, amelyre a **mintaillesztés sikerült** és a **predikátumok teljesültek**. Az eddig bemutatott változat tehát egy vagy több kollekció elemein műveletek elvégzésére és/vagy bizonyos elemek szűrésére használható (vö. `Enum.map/2`, `Enum.filter/2`).

Ha a generátor mintája egy elemre nem illeszkedik, az az elem egyszerűen kimarad az eredményből, és a kiértékelés a következő elemmel folytatódik; a mintaillesztés így külön szűrőfeltétel nélkül is szűr.

Több generátor esetén a jobbra álló generátor fut gyorsabban: a bal oldali generátor minden eleméhez végigmegy a jobb oldali összes elemén (keresztszorzat).

### A `uniq:` opció

`for` q₁[, q₂, ..., qₙ][, `into:` coll], `uniq: true|false`, `do:` exp

A `uniq: true` opció hatására az előállított gyűjteménybe csak egymástól különböző értékek kerülnek be. Csak lista, sztring és bináris esetén van értelme használni, hiszen a szótárban a kulcsok sohasem ismétlődhetnek.

### A `reduce:` opció

`for` q₁[, q₂, ..., qₙ], `reduce:` acc₀ `do` acc -> fun(pat, acc) `end`

- A `reduce:` opcióval a for-jelölés nem az `Enum.map/2`-t, hanem az `Enum.reduce/3`-at váltja ki.
- Az acc₀ az eredményt gyűjtő akkumulátor kezdőértéke.
- A `do ... end` között egy névtelen függvényt kell megadni (az `fn` és a hozzá tartozó `end` nélkül!), amelynek egyetlen argumentuma az acc akkumulátor (a neve bármi lehet). A törzsében olyan kétargumentumú függvényt vagy operátort kell használni, amelynek egyik argumentuma a generátorban használt pat minta, a másik pedig ugyancsak az acc akkumulátor. Az argumentumok sorrendjének hatása lehet az eredményre!

## Kis példák

A kommentek az egyes for-kifejezéseknek megfelelő matematikai halmazjelölést mutatják:

```iex
iex> for x <- 1..6 // 2, do: x     # { x | x ∈{1, 3, 5} }
[1, 3, 5]
iex> for x <- [1,2,3], do: 2*x+1   # { 2 · x + 1 | x ∈{1, 2, 3} }
[3, 5, 7]
iex> for x <- 1..9, rem(x, 2) === 0, x > 2, do: 2*x
[8, 12, 16]
iex> for {k,v} <- [egy: 1, két: 2, há: 3], into: %{}, do: {k,v}
%{egy: 1, két: 2, há: 3}
iex> for {k,v} <- %{egy: 1, két: 2, há: 3}, into: [], do: {k,v}
[egy: 1, két: 2, há: 3]
iex> for c <- [?c, ?s, ?ó, ?k, ?a], into: "", do: <<c>>
<<99, 115, 243, 107, 97>>
iex> for c <- [?c, ?s, ?o, ?k, ?a], into: "", do: <<c>>
"csoka"
iex> for x <- 0..-2 // -2, y <- 1..x, do: {x,y}
[{0, 1}, {0, 0}, {-2, 1}, {-2, 0}, {-2, -1}, {-2, -2}]
iex> for x <- 0..-2 // -2, y <- 1..x, xy = {x,y}, do: xy
[{0, 1}, {0, 0}, {-2, 1}, {-2, 0}, {-2, -1}, {-2, -2}]
iex> for x <- 2..4, rem(x,3) !== 0, y <- 1..3, x > y, do: {x,y}
[{2, 1}, {4, 1}, {4, 2}, {4, 3}]
```

Néhány megjegyzés a példákhoz:

- A `<<c>>` egyetlen bájtot állít elő. Az `ó` kódja (243) egy bájton nem érvényes UTF-8 karakter, ezért az eredmény nem írható ki sztringként, csak bájtokként; ékezet nélkül `"csoka"` lesz az eredmény.
- A `0..-2 // -2` tartomány elemei 0 és -2; az `1..x` tartomány a függő generátorban `x` értékétől függ (`1..0`, illetve `1..-2`, csökkenő tartományok).
- Az `xy = {x,y}` qᵢ-ként mintaillesztéssel köt változót, amely a `do:` utáni kifejezésben használható.
- Az utolsó példában a `rem(x,3) !== 0` szűrő az első generátorhoz, az `x > y` a másodikhoz tartozik.

További példák:

```iex
iex> for i <- 1..3, j <- 2..1//-1, do: {i,j} # keresztszorzatok listája
[{1, 2}, {1, 1}, {2, 2}, {2, 1}, {3, 2}, {3, 1}]
iex> for i <- 1..3, do: (for j <- 2..1//-1, do: {i,j}) # listák listája
[[{1, 2}, {1, 1}], [{2, 2}, {2, 1}], [{3, 2}, {3, 1}]]
iex> for i <- 1..3, j <- 2..1//-1, into: %{}, do: {i,j} # ismétlődő kulcs felülír!
%{1 => 1, 2 => 1, 3 => 1}
iex> for i <- 1..3, j <- 2..1//-1, into: %{}, do: {i+j*4,j} # így a kulcsok egyediek
%{5 => 1, 6 => 1, 7 => 1, 9 => 2, 10 => 2, 11 => 2}
iex> for _i <- 1..5, into: "", do: "1" # többszörözve
"11111"
iex> for _i <- 1..5, into: "", uniq: true, do: "1" # azonosak csak egyszer
"1"
iex> for _i <- 1..5, into: <<>>, do: <<1::size 1>> # 5 bit (0b11111), 1 byte
<<31::size(5)>>
iex> for _i <- 1..5, into: <<>>, uniq: true, do: <<1::size 1>> # 1 bit (0b1), 1 byte
<<1::size(1)>>
iex> for _i <- 1..5, into: <<>>, do: <<1::size 2>> # 10 bit (0b01010101, 0b01), 2 byte
<<85, 1::size(2)>>
iex> for _i <- 1..5, into: <<>>, uniq: true, do: <<1::size 2>> # 2 bit (0b01), 1 byte
<<1::size(2)>>
```

## Gyakorló feladatok

### Listában kulcs-érték párokban előforduló értékek listája

Egy listában többféle típusú és szerkezetű elem fordul elő, köztük `{:v, v}` párok is, ahol a párok első tagja a `:v` atom, második tagja az itt `v`-vel jelölt, tetszőleges érték. Írjon olyan rekurzív függvényt, amely a lista elemei közül az összes `{:v, v}` párban található `v` értéket visszaadja az eredménylistában! Írhat segédfüggvényt és akkumulátort nem használó, valamint akkumulátoros segédfüggvényt használó változatot. Feltétlenül írjon egyéb változatot is `for`-jelöléssel (meg fog lepődni!).

<details>
<summary>Megoldás</summary>

A `for`-jelöléses változat a feladatlapon szerepel. Ha a generátorban a mintaillesztés sikertelen, az adott érték nem kerül be az eredménylistába, és a kiértékelés a következő listaelemmel folytatódik; ezért külön szűrőfeltétel nélkül, nagyon egyszerűen megvalósítható az elvárt működés.

```elixir
defmodule Ertekek do
  @spec ertekek(xs :: [{:v::atom(), v::any()} | any()]) :: vs :: [any()]
  # Az xs lista elemei közül a {:v, v} mintára illeszkedő
  # párok 2. tagjából képzett lista vs
  def ertekek(xs), do: for({:v, v} <- xs, do: v)
end
Ertekek.ertekek([:alma, {:s, 3}, {:v, 1}, 3, {:v, 2}]) === [1, 2]
```

</details>

### Természetes szám valódi osztói

Egy természetes szám **valódi osztóinak** nevezzük az 1-en és önmagán kívüli pozitív osztóit. Írjon olyan kifejezést vagy függvényt a `for`-jelölés felhasználásával, amely egy listában visszaadja a paraméterként átadott természetes szám valódi osztóit! Írjon többféle megoldást, használjon magasabb rendű függvényeket, definiálhatja a függvényt a `def` kulcsszóval is.

Tipp: egy $k$ természetes szám valódi osztóit a legegyszerűbben úgy találhatja meg, hogy a $k$-t rendre elosztja a $2$ és $k/2$ közötti egészekkel, és ha az egészosztásnak nincs maradéka, akkor az adott szám osztója $k$-nak.

```elixir
# @spec proper_divisors(i :: integer()) :: ds :: [integer()]
# Az i természetes szám valódi osztóinak listája ds
proper_divisors = ...
(proper_divisors.(10) === [2, 5]) |> IO.inspect(charlists: :as_list)
(proper_divisors.(23) === []) |> IO.inspect(charlists: :as_list)
(proper_divisors.(48) === [2, 3, 4, 6, 8, 12, 16, 24]) \
 |> IO.inspect(charlists: :as_list)
(proper_divisors.(128) === [2, 4, 8, 16, 32, 64]) \
 |> IO.inspect(charlists: :as_list)
```

### Összetett számok

**Összetett számnak** nevezzük azt a természetes számot, amelynek van valódi osztója. A legkisebb összetett szám a 4. Írjon olyan kifejezést vagy függvényt a `for`-jelölés felhasználásával, amely egy listában visszaadja a paraméterként átadott természetes számnál nem nagyobb összes összetett számot, 4-től kezdve! Felhasználhatja a valódi osztókat előállító függvényt, amelyet az előbb írt meg. Írjon többféle megoldást, használjon magasabb rendű függvényeket, definiálhatja a függvényt a `def` kulcsszóval is.

```elixir
# @spec composite_numbers(i :: integer()) :: ns :: [integer()]
# Az i-nél nem nagyobb összetett számok listája ns
composite_numbers =
(composite_numbers.(11) === [4, 6, 8, 9, 10]) |> IO.inspect(charlists: :as_list)
(composite_numbers.(17) === [4, 6, 8, 9, 10, 12, 14, 15, 16]) \
 |> IO.inspect(charlists: :as_list)
```

**Hatékonyabb megoldás.** Írjon olyan megoldást az előző feladatra, amely nem állítja elő a valódi osztók listáját! Az $n$ természetes szám összetett, ha osztható

1. a $2$ és $\sqrt n$ közötti prímszámok bármelyikével;
2. $2$-vel vagy a $3$ és $\sqrt n$ közötti páratlan egészek bármelyikével.

Az első módszer gyorsabb, de ha a prímszámok előállítása nem triviális, a második módszer is elég hatékony. További hatékonyságnövelő lehetőségekről olvashat pl. itt: <https://en.wikipedia.org/wiki/Primality_test>.

```elixir
composite_numbers_faster = &for i <- 4..&1, composite?.(i), do: i
(composite_numbers_faster.(11) === [4, 6, 8, 9, 10] ) \
 |> IO.inspect(charlists: :as_list)
(composite_numbers_faster.(21) === [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21])\
 |> IO.inspect(charlists: :as_list)
```

Tipp: bontsa a megoldást lépésekre: állítsa elő a szám összetett voltának vizsgálatához használandó osztókat; állapítsa meg, hogy a szám összetett-e; állítsa elő az összetett számok listáját a kért tartományban. Fontolja meg az alábbi függvények használatát:

- A `Kernel` modulban definiált `..///3` operátor operandusainak egész számoknak kell lenniük, ezért ha a felső határ beállítására a `:math.sqrt/1` függvényt használja, egész számmá kell konvertálni (vö. `round/1`, `floor/1`, `ceil/1`).
- Az `Enum.to_list/1` tetszőleges felsorolható sorozatot listává alakít, így tartomány típusú értéksorozatot is.
- Az `Enum.reduce/3` egy lista összes elemére alkalmaz egy kétoperandusú függvényt. Ha pl. egy szám összetett voltát akarjuk vele vizsgálni, olyan függvényt kell átadnunk paraméterként, amely az adott számnak a sorozat egy elemével való oszthatósága esetén igaz, egyébként hamis értékkel tér vissza.

```elixir
# @spec probes(i :: integer()) :: ps :: [integer()]
# A 2-t, továbbá a 3 és a :math.sqrt(i) közé eső egészeket tartalmazó lista ps
probes = ...
# @spec composite?(i :: integer()) :: b :: boolean()
# b igaz, ha i összetett szám
composite? = ...
# @spec composite_numbers_faster(i :: integer()) :: ns :: [integer()]
# Az i-nél nem nagyobb összetett számok listája ns
composite_numbers_faster = ...
```

Ha a javaslatot megfogadta, a megoldást három kis – esetleg több – lépésre bontotta, mindegyikre egy-egy névtelen (de változóhoz kötött) függvényt írt, így ezeket könnyebb volt megérteni, és a helyességüket könnyebb volt belátni. Mivel a funkcionális nyelvekben a függvényhívás nagyon hatékonyan van megoldva, ez a jó és követendő gyakorlat: minden kicsit is összetett függvényt több egyszerűbb függvényből rakjunk össze, és ahol csak lehet, használjuk a hatékonyan megvalósított és sokat tesztelt könyvtári függvényeket.

<p class="sources">Forrás: dp26a-fp3ea.pdf (10–14. dia), dp26a-fp3gy.livemd</p>
