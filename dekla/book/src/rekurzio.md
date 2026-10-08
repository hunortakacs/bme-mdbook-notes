# Rekurzió

## Lineáris és elágazó rekurzió

A deklaratív programozás alappillére a rekurzió. A deklaratív nyelvekben nincs ciklus, ezért ismétlést, iterációt is rekurzív algoritmussal valósítunk meg. A rekurzió kétféle lehet: **lineáris** és **elágazó** (angolul *linear recursion* és *tree recursion*).

- **Lineáris rekurzió**: egy *rekurzív hívás* van a függvényben.

  ```elixir
  def fac(0), do: 1 # 1. klóz: Alapeset
  def fac(n), do: n * fac(n - 1) # 2. klóz: Rekurzív eset
  ```

- **Jobbrekurzió** (farokrekurzió, *tail recursion*): a rekurzív hívás *visszatérési pozícióban* van, ezért hatékonyabb gépi kód készül belőle, nem kell hozzá verem.

  ```elixir
  def fac(n), do: fac(n, 1) # Segédfüggvény meghívása akkumulátor paraméterrel
  def fac(0, a), do: a
  def fac(n, a), do: fac(n - 1, n * a)
  ```

- **Elágazó rekurzió**: több *rekurzív hívás* van a függvényben; sokszor nem hatékony (lásd [Dinamikus programozás](technikak/dinamikus.md)).

  ```elixir
  def fib(n) when n <= 1, do: n # 1. klóz őrfeltétellel: Alapeset
  def fib(n), do: fib(n - 1) + fib(n - 2) # 2. klóz: Rekurzív eset
  ```

Az adatszerkezetek is lehetnek rekurzívak:

- **Lineárisan rekurzív adatszerkezet** pl. az egyszeresen láncolt lista (`[...]`, nem egydimenziós tömb!). Alapesete az `[]` üres lista, *rekurzív esete* a legalább egyelemű `[H|T]`, ahol `T` is egy lista (`[]` vagy legalább egyelemű).
- **Elágazóan rekurzív adatszerkezet** pl. a (bináris vagy többágú) fa.

Rekurzív adatszerkezetek feldolgozásának természetes módja a rekurzív algoritmus. Lineáris adatszerkezetek, pl. listák feldolgozására imperatív nyelveken még lehet ciklust írni, de elágazóan rekurzív adatszerkezeteket, pl. fákat ciklusokkal bejárni már nagy kihívás. Ez az **algebrai módszer**: a *rekurzív adatszerkezeteket* *mintaillesztéssel* dolgozzuk fel rekurzív függvényekkel, minden esetre egy-egy klózt írva.

## Rekurzív függvény írása: két lista összefűzése

A deklaratív stílus érzékeltetésére írjuk meg lépésről lépésre két lista összefűzését `app/2` néven! Az `xs` és `ys` listák összefűzése azt jelenti, hogy az `xs` lista összes elemét az `ys` *elé* fűzzük az elemek eredeti sorrendjének megőrzésével: `xs⊕ys`.

Mivel a lista láncolt adatszerkezet, csak az első elemét érjük el közvetlenül. Egyszerű a dolgunk, ha az első lista, `xs`, üres: ekkor a második listát, `ys`-t kell változtatás nélkül visszaadnunk. Ezt az esetet már láttuk (`App0`, [Mintaillesztés](mintaillesztes.md#klózok)).

Ugyanez a rövidített (`, do:`) függvénydefiníció helyett a teljes, `do ... end` alakú definícióval:

```elixir
defmodule App0 do
  # app(xs, ys): xs és ys listák összefűzöttje zs == (xs ⊕ ys)
  # [] ⊕ ys == ys
  def app([], ys) do
    ys
  end
end
```

Ha `xs` nem üres, akkor ahhoz, hogy az `ys` elé fűzzük, rendre le kell emelni és félre kell rakni az elemeit, amíg csak üressé nem válik. Hová tegyük ezeket az elemeket? Ha a függvény *rekurzív módon* hívja meg saját magát, akkor átmenetileg automatikusan a hívási verembe kerülnek.

Amikor rekurzív függvényt írunk, abból indulunk ki, hogy a függvény valamilyen egyszerűbb adatszerkezetre – pl. egy paraméterként kapott lista farkára – elvégzi, amit elvárunk tőle, és ezután már csak a lista fejével kell valamit kezdenie, pl. a rekurzív hívás eredményeként kapott lista elé fűznie. A mintaillesztéssel az előforduló eseteket világosan elkülöníthetjük. Két lista összefűzésénél az első paraméter, `xs`, értéke szerint két esetet érdemes megkülönböztetni (lehetne többet is, de felesleges lenne): 1. `xs` nem üres, 2. `xs` üres.

```elixir
defmodule App1 do
  # app(xs, ys): xs és ys listák összefűzöttje zs == (xs ⊕ ys)

  # [z | zs] ⊕ ys = [z | zs ⊕ ys]
  def app([z | zs] = zzs, ys) do
    [z | app(zs, ys)]
  end

  # [] ⊕ ys == ys
  def app([], ys) do
    ys
  end

end
```

A `[z | zs] = zzs` réteges minta (lásd [Mintaillesztés](mintaillesztes.md#réteges-minta)) csak a magyarázat kedvéért szerepel, hogy a teljes paraméterre is utalni tudjunk, ne csak a komponenseire. Mivel a törzsben nem használjuk, a fordító figyelmeztetésének elkerülésére aláhúzásjellel kezdjük:

```elixir
defmodule App2 do
  # app(xs, ys): xs és ys listák összefűzöttje zs == (xs ⊕ ys)
  def app([z | zs] = _zzs, ys) do
    [z | app(zs, ys)]
  end

  def app([], ys) do
    ys
  end
end
```

Ha az `app/2` hívásakor az első paraméter üres lista, az Elixir a második klózt értékeli ki, ha nem üres, az elsőt. Az első klóz rekurzív hívásában az `app/2`-t a kapott `_zzs` lista farkára, `zs`-re alkalmazzuk, feltételezve, hogy képes a `zs` listát az `ys` elé fűzni. Amikor ebből a hívásból visszatér, már csak a verembe félretett `z`-t kell a kapott lista elé fűznie (`[z | app(zs, ys)]`).

Két dolgot kell még belátnunk.

- **A rekurzió nem végtelen.** A listák véges hosszúságúak, és a rekurzív hívás az `app/2`-t mindig a kapott `_zzs`-nél eggyel rövidebb `zs`-re alkalmazza. A lista tehát egyre rövidül, és amikor üressé válik, a második klóz kiértékelésére kerül sor: ennek törzsében nincs rekurzív hívás, a függvény a rekurzív hívások során változás nélkül továbbadott `ys`-sel tér vissza.
- **A függvény azt csinálja, amit elvárunk tőle.** Amikor a lista már üressé vált, a rekurzív hívás az `ys` listával tér vissza; ez elé fűzi az első klóz az eredeti lista utolsó elemét, amelyet a veremből vesz elő. A következő visszatéréskor az így kibővített lista elé fűzi az utolsó előtti elemet, majd a hátulról harmadikat, és így tovább, amíg ki nem ürül a verem. A végeredmény valóban az, amit várunk.

```iex
iex> App2.app([1,2,3], [4,5])
[1, 2, 3, 4, 5]
```

Ha a klóz törzse egyetlen kifejezésből áll, célszerű a rövidített `, do:` függvényjelölést alkalmazni; a típusspecifikációval és a fejkommenttel kiegészített tömör változat az `App3` ([Típusok](tipusok.md#típusspecifikáció)). Ellenőrizzük, hogy lefedtünk-e minden lehetséges esetet! Az első paraméter a két klózban kétféle mintára illeszkedhet, `[]`-ra vagy `[x|xs]`-re, azaz üres vagy legalább egyelemű listára: ez lefedi az első paraméter összes lehetséges (lista) értékét. A második paraméter mindkét klózban az `ys` kötetlen változó, ami mindenre illeszkedik. A két klózzal tehát valóban minden esetet lefedtünk.

## Törzsrekurzió és jobbrekurzió

A rekurzió szokásos iskolapéldája az $n!$ kiszámítása. Matematikai definíciója:

$$
0! = 1, \qquad n! = n \cdot (n-1)!, \text{ ha } n > 0
$$

Az első változat a matematikai definíciót másoló rekurzív függvény:

```elixir
defmodule Fac do
  @spec fac(n :: integer()) :: f :: integer() # Típusspecifikáció
  # f = n! (azaz f az n faktoriálisa) # Fejkomment

  # ha az n=0 mintaillesztés sikeres
  def fac(0), do: 1

  # ha az n=0 mintaillesztés sikertelen
  def fac(n), do: n * fac(n - 1)
end
```

A második klózban alkalmazott rekurziót angolul *body recursion*-nek, magyarul **törzsrekurziónak** mondhatjuk, ha hangsúlyozni akarjuk, hogy a rekurzív hívás eredményével a függvény törzsében még további műveletet (itt szorzást) kell végezni.

A **jobbrekurzív** (*tail recursive*) változat kevésbé szigorúan követi a matematikai definíciót, ezért nehezebb megérteni, és nehezebb hozzá kifejező, pontos fejkommentet írni. A jobbrekurziót magyarul **terminális rekurziónak**, ritkábban **farokrekurziónak** is nevezik, mert a rekurzív hívás az adott klózban az utolsó – befejező, lezáró – hívás: az eredményét változatlanul vissza kell adni, már semmilyen műveletet nem végzünk vele.

A jobbrekurzív változathoz egy plusz paraméterre van szükség. Ezt **akkumulátornak** szokták nevezni, mert a részeredményeket gyűjtjük benne – ahelyett, hogy a még elvégzendő műveleteket az argumentumaikkal együtt a verembe tennénk. Itt a részletszorzatokat adjuk át benne a rekurzív hívásban.

Az akkumulátornak az első híváskor adunk értéket: a `fac/1` hívja meg az `1` kezdőértékkel a `fac/2`-t. Ha a `fac/1`-et $0$-val hívjuk, az eredménynek $1$-nek kell lennie, ezért a `fac/2` első klózának $0$ esetén az akkumulátort kell visszaadnia, rekurzív hívás nélkül. Ha az első paraméter, $n$, nem $0$, a második klózra kerül sor: a rekurzív hívásban az első paramétert eggyel csökkentjük ($n-1$), a másodikban pedig $n$-nel megszorozzuk az eddig összegyűjtött részletszorzatot ($n*a$). Így alakul ki az $n\cdot(n-1)\cdot\ldots\cdot1$ eredmény.

```elixir
defmodule FacJobbrek do
  # Típusspecifikáció
  @spec fac(n :: integer()) :: f :: integer()
  # f = n! (azaz f az n faktoriálisa)
  def fac(n), do: fac(n, 1)

  @spec fac(n :: integer(), a :: integer()) :: f :: integer()
  defp fac(0, a), do: a
  defp fac(n, a), do: fac(n - 1, n * a)
end
```

Mindkét változatot kipróbálhatjuk ugyanazokkal a hívásokkal:

```elixir
Fac.fac(5)
Fac.fac(0)
Fac.fac(1)
Fac.fac(100_000)
FacJobbrek.fac(5)
FacJobbrek.fac(0)
FacJobbrek.fac(1)
FacJobbrek.fac(100_000)
```

Az eredmény mindkét függvénnyel 120, 1, 1, illetve egy több mint 450 000 jegyű szám (az egész számok pontossága korlátlan). Érdemes kipróbálni, tapasztalható-e lényeges különbség a két függvény futási ideje között.

A jobbrekurzív kódot a modern értelmező- és fordítóprogramok nagyon hatékonyan, **iteratív processzként** valósítják meg: a hívás nem foglal újabb veremhelyet. A jobbrekurzió manapság főleg olyan esetekben indokolt, amikor két vagy több processz üzenetet küld egymásnak, és végtelen jobbrekurzív hívásban várnak a válaszüzenetre (lásd [Az Elixir nyelv](elixir.md#folyamatok-üzenetekkel-kommunikálnak)).

### Balrekurzió

**Balrekurziónak** (fejrekurziónak, angolul *head recursion*) nevezzük, ha a rekurzív hívás egy klóz első és egyetlen rekurzív hívása, azaz a rekurzív hívás *előtt* nem végzünk semmilyen műveletet. A különbség jól látszik, ha egy függvény a rekurzív hívás előtt vagy után ír ki valamit: a jobbrekurzív változat a hívás előtt írja ki a soron következő számot, a balrekurzív a hívás után, a visszatérés során. A két változatot a fejezet végi `upto_by_3` feladat mutatja be.

## Klózsorrend és hatékonyság

Egy rekurzív adatszerkezet feldolgozására legalább két, esetleg több klózt írunk. Közöttük vannak olyanok, amelyekre az adatszerkezet jellegzetessége miatt csak egyszer vagy csak nagyon ritkán kerül sor, másokra gyakrabban. Ilyen például az üres és a nem üres lista esete: az üres listát feldolgozó klóz kiértékelésére csak egyszer kerül sor, a nem üres listát feldolgozó klózt a lista hosszától függően akár nagyon sokszor hívjuk.

A kurzus ajánlása: az algoritmus hatékonyságát javítja, ha

- egy függvény klózai *kölcsönösen kizárják* egymást, és
- közülük a gyakrabban hívott(ak) megelőzi(k) a ritkábban hívott(ak)at:

```elixir
def fun([x|xs])...
def fun([])...
```

Az `App3.app/2` második klóza illeszkedik az üres listára; a rekurzió során erre csak egyszer kerül sor, ezért ez észszerű döntésnek tűnik. Az `App4.app/2` a két klózt fordított sorrendben tartalmazza. Érdemes megmérni, van-e észrevehető különbség a futási időben egy 25 millió elemű listán:

```elixir
defmodule App4 do
  @spec app(xs :: [integer()], ys :: [integer()]) :: zs :: [integer()]
  # xs és ys listák összefűzöttje zs
  def app([], ys),     do: ys
  def app([x|xs], ys), do: [x|app(xs, ys)]
end
```

```elixir
App4.app(Range.to_list(1..25_000_000), [])
:ok
```

```elixir
App3.app(Range.to_list(1..25_000_000), [])
:ok
```

### Mérések: egészlista összege háromféleképpen

Az egészlista összegét kiszámoló `Sum` modulnak (lásd [Projektek, mérés, típusellenőrzés](elixir/mix.md#fordítás-és-futtatás-mix-szel)) három változata van: a `sum1` első, a `sum2` második klóza illeszkedik az üres listára, a `sum3` pedig egy jobbrekurzív segédfüggvényt hív meg. Van-e különbség a hatékonyságukban?

```elixir
defmodule Sum do

  @spec sum1(xs::[integer()]) :: sum::integer()
  # xs elemeinek összege sum
  # üres listára az első klóz illeszkedik
  def sum1([]), do: 0
  def sum1([x|xs]), do: x + sum1(xs)

  # üres listára a második klóz illeszkedik
  def sum2([x|xs]), do: x + sum2(xs)
  def sum2([]), do: 0

  # jobbrekurzív
  def sum3(xs), do: sumi(xs, 0)

  defp sumi([x|xs], sum), do: sumi(xs, sum+x)
  defp sumi([], sum), do: sum

end

1..1000 |> Range.to_list() |> Sum.sum1() |> IO.inspect()
1..1000 |> Range.to_list() |> Sum.sum2() |> IO.inspect()
1..1000 |> Range.to_list() |> Sum.sum3() |> IO.inspect()
```

Mindhárom `500500`-at ír ki. A gyakorló notebook mindhármat egy 90 millió elemű listára is lefuttatja:

```elixir
1..90_000_000 |> Range.to_list() |> Sum.sum1() |> IO.inspect()
1..90_000_000 |> Range.to_list() |> Sum.sum2() |> IO.inspect()
1..90_000_000 |> Range.to_list() |> Sum.sum3() |> IO.inspect()
```

A Benchee-mérés egy 10 000 elemű listán (`1..10_000 |> Enum.to_list |> Sum.sum1()` stb.):

```elixir
Benchee.run(
  %{
    "sum1 ([] az 1. klozban)"  => fn -> 1..10_000 |> Enum.to_list |> Sum.sum1() end,
    "sum2 ([] a 2. klozban)"  => fn -> 1..10_000 |> Enum.to_list |> Sum.sum2() end,
    "sum3 (iterativ, [] a 2. klozban)"  => fn -> 1..10_000 |> Enum.to_list |> Sum.sum3() end
  }# , profile_after: true
)
:ok
```

Az előadás diáján közölt eredmény (`mix run`-nal, Elixir 1.18.4, Erlang 28.0.1, Intel i5-8365U; a zárójeles megjegyzések az előadó kiegészítései):

```text
Name           ips        average  deviation         median         99th %
sum3       16.26 K       61.50 µs    ±16.25%       63.65 µs       79.93 µs
sum2        8.87 K      112.80 µs    ±18.45%       97.88 µs      175.92 µs
sum1        8.26 K      121.01 µs    ±18.40%      105.16 µs      187.74 µs

Comparison:
sum3       16.26 K (2. klóz illeszkedik az üres listára a jobbrekurzív segédfüggvényben)
sum2        8.87 K - 1.83x slower +51.30 µs (2. klóz illeszkedik az üres listára)
sum1        8.26 K - 1.97x slower +59.52 µs (1. klóz illeszkedik az üres listára)
```

Az első előadás segédanyagában (Livebookban, ugyanazon a gépen) mért eredmény:

```text
Name                                       ips        average  deviation         median         99th %
sum3 (iterativ, [] a 2. klozban)       11.60 K       86.22 μs    ±16.11%       82.37 μs      150.53 μs
sum1 ([] az 1. klozban)                 7.54 K      132.56 μs    ±22.29%      126.42 μs      230.17 μs
sum2 ([] a 2. klozban)                  6.73 K      148.58 μs    ±15.46%      136.23 μs      204.25 μs

Comparison: 
sum3 (iterativ, [] a 2. klozban)       11.60 K
sum1 ([] az 1. klozban)                 7.54 K - 1.54x slower +46.33 μs
sum2 ([] a 2. klozban)                  6.73 K - 1.72x slower +62.36 μs
```

Az első gyakorlat `nth` feladatánál (lásd lent) egy 100 001 elemű lista első, középső és utolsó elemét kérjük el, egyszer az üres listát utolsóként (`EmptyLast`), egyszer elsőként (`EmptyFirst`) kezelő klózsorrenddel:

```text
Name                           ips        average  deviation         median         99th %
firstElemEmptyFirst      1745.97 K        0.57 μs    ±98.93%        1.02 μs        2.05 μs
firstElemEmptyLast       1724.38 K        0.58 μs   ±100.87%        1.02 μs        2.05 μs
middleElemEmptyLast         6.32 K      158.12 μs    ±41.63%      102.40 μs      307.20 μs
middleElemEmptyFirst        6.28 K      159.34 μs    ±50.58%      102.40 μs      307.20 μs
lastElemEmptyLast           3.16 K      316.78 μs    ±30.90%      307.20 μs      614.40 μs
lastElemEmptyFirst          3.08 K      324.93 μs    ±31.75%      307.20 μs      614.40 μs
```

A két klózsorrend között mért különbségek kicsik és nem következetesek: a diáin a `sum2` a gyorsabb, a segédanyagban a `sum1`, az `nth`-nél pedig 1–3% az eltérés. Egyértelmű nyereséget a jobbrekurzió hoz: a `sum3` mindkét mérésben másfél-kétszer gyorsabb. A futási idő a lista hosszával arányosan nő: az utolsó elem elérése kétszer annyi ideig tart, mint a középsőé.

## Hibajelzés: Erlang- és Elixir-stílus

Gyakran előfordul, hogy bizonyos listákon bizonyos műveleteket nem lehet elvégezni. Egy üres listának például egyetlen eleme sincs, bármelyik elemét is kérjük, nincs mit eredményül adni.

Ilyenkor dönthetünk úgy, hogy az adott műveletet üres listára nem értelmezzük, és a hiba jelzését a rendszerre bízzuk (a hívás például `FunctionClauseError` hibával leáll). Ha úgy döntünk, hogy a helyes eredmény mellett a hibát is jelezzük, ezt hagyományosan kétféle stílusban tehetjük meg:

- **Erlang-stílusban** a visszatérési érték típusa `{:ok, any()} | :error`: siker esetén a visszatérési érték egy `{:ok, value}` pár, ahol `value` a visszaadott, `any()` típusú érték, meghiúsulás esetén pedig az `:error` atom.
- **Elixir-stílusban** a visszatérési érték típusa `any() | nil`: siker esetén maga az `any()` típusú `value`, meghiúsulás esetén a `nil` atom.

Mindhárom változatra példa a lenti 5. feladat (`Last`, `LastEx`, `LastEr`).

## Gyakorló feladatok

Az alábbi feladatok megoldására **ne** használja az azonos vagy hasonló feladatokat megoldó könyvtári függvényeket a `Kernel`, `List`, `Enum` és más modulokból, pl. `hd`, `tl`, `first`, `last`, `at`, `length`, `split`, `slice`! Gyakorlásképpen *saját*, ahol kell, rekurzív függvénydefiníciókat írjon. A specifikációs kódrészletek a megírandó függvény keretét (modul, típusspecifikáció, fejkomment) és néhány teszthívást tartalmaznak; a `...` helyére kell a megoldást írni.

### 1. Lista feje

Írjon függvényt egy lista fejének (első elemének) visszaadására! Ha a lista üres, Elixir-stílusban jelezze, azaz a `nil` atomot adja eredményül. Tipp: az első klóz a legalább egyelemű listára, a második az üres listára illeszkedjen.

```elixir
defmodule Head do
  @spec hd(xs :: [any()]) :: r :: any() | nil
  # Ha xs nem üres, x az xs lista feje, egyébként nil
  def hd(...), do:
  ...
end
IO.puts(Head.hd([]) == nil)
IO.puts(Head.hd(Range.to_list(1..5)) == 1)
IO.puts(Head.hd(~c"almárium") == ?a)
```

<details>
<summary>Megoldás</summary>

```elixir
defmodule Head do
  @spec hd(xs :: [any()]) :: r :: any() | nil
  # Ha xs nem üres, x az xs lista feje, egyébként nil
  def hd([x|_]), do: x
  def hd([]), do: nil
end
```

Mindhárom teszt `true`-t ír ki.

</details>

### 2. Lista farka

Írjon függvényt egy lista farkának (az első eleme utáni részlistájának) visszaadására! Ha a lista üres, Elixir-stílusban jelezze, azaz a `nil` atomot adja eredményül. Tipp: az első klóz a legalább egyelemű listára, a második az üres listára illeszkedjen.

```elixir
defmodule Tail do
  @spec tl(xs: [any()]) :: ts :: [any()] | nil
  # Az xs lista farka ts
  def tl(...), do:
  ...
end
IO.puts(Tail.tl([]) == nil)
IO.puts(Tail.tl(Range.to_list(1..5)) == [2,3,4,5])
IO.puts(Tail.tl(~c"almárium") == ~c"lmárium")
```

<details>
<summary>Megoldás</summary>

```elixir
defmodule Tail do
  @spec tl(xs: [any()]) :: ts :: [any()] | nil
  # Az xs lista farka ts
  def tl([_|xs]), do: xs
  def tl([]), do: nil
end
```

Mindhárom teszt `true`-t ír ki.

</details>

### 3. Lista n-edik eleme

Írjon rekurzív függvényt egy lista n-edik elemének visszaadására! (A lista indexelése 0-tól indul.) Ha a lista n-nél rövidebb, Elixir-stílusban jelezze, azaz a `nil` atomot adja eredményül. Tipp: három klózt kell írnia: egyet az üres listára, egyet a megtalált elem visszaadására, egyet pedig arra, hogy rekurzív hívással folytassa a keresést.

```elixir
defmodule Nth do
  @spec nth(xs :: [any()], n :: integer()) :: r :: any() | nil
  # Ha xs elég hosszú, r az xs n-edik eleme; egyébként nil (indexelés 0-tól)
  def nth(..., n), do:
  ...
end
IO.puts(Nth.nth([], 5) == nil)
IO.puts(Nth.nth(Range.to_list(1..5), 4) == 5)
IO.puts(Nth.nth(Range.to_list(1..5), 5) == nil)
IO.puts(Nth.nth(~c"almárium", 3) == ?á)
IO.puts(Nth.nth(~c"almárium", -3) == nil)
```

A `benchee` modul segítségével hasonlítsa össze a futási időket egy hosszú lista első, középső és utolsó elemének elérése esetén, olyan klózsorrendekkel, amikor az első, illetve amikor az utolsó klóz illeszkedik az üres listára!

<details>
<summary>Megoldás</summary>

```elixir
defmodule Nth do
  @spec nth(xs :: [any()], n :: integer()) :: r :: any() | nil
  # Ha xs elég hosszú, r az xs n-edik eleme; egyébként nil (indexelés 0-tól)
  def nth([x|_], 0), do: x
  def nth([_|xs], n), do: nth(xs, n-1)
  def nth([], _), do: nil
end
```

Mind az öt teszt `true`-t ír ki. A mérés:

```elixir
defmodule NthEmptyFirst do
  @spec nth(xs :: [any()], n :: integer()) :: r :: any() | nil
  # Ha xs elég hosszú, r az xs n-edik eleme; egyébként nil (indexelés 0-tól)
  def nth([], _), do: nil
  def nth([x|_], 0), do: x
  def nth([_|xs], n), do: nth(xs, n-1)
end
IO.puts(NthEmptyFirst.nth([], 5) == nil)
IO.puts(NthEmptyFirst.nth(Range.to_list(1..5), 4) == 5)
IO.puts(NthEmptyFirst.nth(Range.to_list(1..5), 5) == nil)
IO.puts(NthEmptyFirst.nth(~c"almárium", 3) == ?á)
IO.puts(NthEmptyFirst.nth(~c"almárium", -3) == nil)

l = Range.to_list(0..100_000)
Benchee.run(%{
        "firstElemEmptyLast" => fn -> Nth.nth(l, 0) end,
        "middleElemEmptyLast" => fn -> Nth.nth(l, 50_000) end,
        "lastElemEmptyLast" => fn -> Nth.nth(l, 100_000) end,
        "firstElemEmptyFirst" => fn -> NthEmptyFirst.nth(l, 0) end,
        "middleElemEmptyFirst" => fn -> NthEmptyFirst.nth(l, 50_000) end,
        "lastElemEmptyFirst" => fn -> NthEmptyFirst.nth(l, 100_000) end
    }
)
```

Az eredmény a [Mérések](#mérések-egészlista-összege-háromféleképpen) szakaszban látható. Ha egy mérendő függvény nagyon gyors (itt az első elem elérése), a Benchee figyelmeztet, hogy a mérés megbízhatatlanabb.

</details>

### 4. Lista hossza

Írjon rekurzív függvényt egy lista hosszának meghatározására! Ne használjon segédfüggvényt! Tipp: az első klóz a legalább egyelemű listákra, a második az üres listára illeszkedjen.

```elixir
defmodule Length do
  @spec len(xs :: [any()]) :: n :: integer()
  # Az xs lista hossza n
  def len(...), do:
  ...
end
IO.puts(Length.len([]) == 0)
IO.puts(Length.len(Range.to_list(1..5)) == 5)
IO.puts(Length.len(~c"kőszerű") == 7)
```

<details>
<summary>Megoldás</summary>

```elixir
defmodule Length do
  @spec len(xs :: [any()]) :: n :: integer()
  # Az xs lista hossza n
  def len([_|xs]), do: 1 + len(xs)
  def len([]), do: 0
end
```

Mindhárom teszt `true`-t ír ki.

</details>

Most akkumulátort és segédfüggvényt használó *jobbrekurzív* függvényt írjon a lista hosszának megállapítására! Tipp: az akkumulátorban gyűjtse a listaelemek számát: amikor leszedi a soron következő elemet a lista elejéről, a rekurzív hívásban az akkumulátor korábbi értékéhez adjon 1-et.

```elixir
defmodule Length2 do
  @spec len(xs :: [any()]) :: n :: integer()
  # Az xs lista hossza n
  def len(....), do: ...

  @spec len(xs :: [any()], count :: integer()) :: n :: integer()
  # Az xs lista hossza és count összege n
  def len(..., count), do:
    ...
end

IO.puts(Length2.len([]) == 0)
IO.puts(Length2.len(Range.to_list(1..5)) == 5)
IO.puts(Length2.len(~c"kőszerű") == 7)
```

<details>
<summary>Megoldás</summary>

```elixir
defmodule Length2 do
  @spec len(xs :: [any()]) :: n :: integer()
  # Az xs lista hossza n
  def len(xs), do: len(xs, 0)

  @spec len(xs :: [any()], count :: integer()) :: n :: integer()
  # Az xs lista hossza és count összege n
  defp len([_|xs], count), do: len(xs, count + 1)
  defp len([], count), do: count
end
```

Mindhárom teszt `true`-t ír ki.

</details>

### 5. Lista utolsó eleme

Írjon rekurzív függvényt egy lista utolsó elemének visszaadására! Ne használjon segédfüggvényt! (A klózok mintáinak megválasztásához lásd [Egymást kölcsönösen kizáró minták](mintaillesztes.md#egymást-kölcsönösen-kizáró-minták).)

Először olyan függvényt írjon, amely visszaadja egy lista utolsó elemét, de a hibajelzést a rendszerre bízza.

```elixir
defmodule Last do
  @spec last(xs :: [any()]) :: x :: any()
  # Ha xs nem üres, az utolsó eleme x
  def last(...), do:
  ...
end
IO.puts(Last.last(~c"Itt vagy?") == ??)
IO.puts(Last.last([]))
```

<details>
<summary>Megoldás</summary>

```elixir
defmodule Last do
  @spec last(xs :: [any()]) :: x :: any()
  # Ha xs nem üres, az utolsó eleme x
  def last([_a | xs=[_b|_cs]]), do: last(xs)
  def last([x]), do: x
end
```

Az első teszt `true`-t ír ki, a második hibával leáll:

```text
** (FunctionClauseError) no function clause matching in Last.last/1
```

</details>

Most írja meg a függvényt Elixir-stílusú hibakezeléssel!

```elixir
defmodule LastEx do
  @spec last(xs :: [any()]) :: r :: (x :: any()) | nil
  # Ha xs nem üres, r == x, ahol az xs utolsó eleme x, egyébként r == nil
  def last(...), do:
  ...
end
IO.puts(LastEx.last(~c"Itt vagy?") == ??)
IO.puts(LastEx.last([]) == nil)
```

<details>
<summary>Megoldás</summary>

```elixir
defmodule LastEx do
  @spec last(xs :: [any()]) :: r :: (x :: any()) | nil
  # Ha xs nem üres, r == x, ahol az xs utolsó eleme x, egyébként r == nil
  def last([_a | xs=[_b|_cs]]), do: last(xs)
  def last([x]), do: x
  def last([]), do: nil
end
```

Mindkét teszt `true`-t ír ki.

</details>

Végül írja meg újra a függvényt Erlang-stílusú hibakezeléssel!

```elixir
defmodule LastEr do
  @spec last(xs :: [any()]) :: r :: {:ok, x :: any()} | :error
  # Ha xs nem üres, r == {:ok, x}, ahol az xs utolsó eleme x, egyébként r == :error
  def last(...), do:
  ...
end
IO.puts(LastEr.last(~c"Itt vagy?") == {:ok, ??})
IO.puts(LastEr.last([]) == :error)
```

<details>
<summary>Megoldás</summary>

```elixir
defmodule LastEr do
  @spec last(xs :: [any()]) :: r :: {:ok, x :: any()} | :error
  # Ha xs nem üres, r == {:ok, x}, ahol az xs utolsó eleme x, egyébként r == :error
  def last([_a | xs=[_b|_cs]]), do: last(xs)
  def last([x]), do: {:ok, x}
  def last([]), do: :error
end
```

Mindkét teszt `true`-t ír ki.

</details>

### 6. Lista k-adik elemétől induló, n hosszú részlistája

Írjon rekurzív függvényt egy lista olyan $n$ hosszú részlistájának visszaadására, amely a $k$-adik elemtől kezdődik (a lista indexelése 0-tól indul)! Ha nincs ilyen hosszú részlistája, Elixir-stílusú hibajelzéssel térjen vissza. Ne használjon segédfüggvényt! A klózok sorrendjének megválasztásával törekedjen hatékony megoldásra. Gondolja át, hányféle esetet kell megkülönböztetnie!

Tipp, a megkülönböztetendő esetek:

1. Kiszedtük a lista $k$-adik elemével kezdődő, $n$ hosszú részlistát.
2. Elhagytuk a lista első $k-1$ elemét, kigyűjthetjük a következő $n$ darab elemet.
3. Elhagyjuk a lista első $k-1$ elemét.
4. Elfogytak az elemek a listából, mielőtt kiszedtük volna az $n$ hosszú részlistát.

```elixir
defmodule Slice do
  @spec slice(xs :: [any()], k :: integer(), n :: integer()) :: r :: [any()] | nil
  # Ha xs elég hosszú, r az xs k-tól induló, n hosszú részlistája; egyébként nil
  # Indexelés 0-tól
  def slice(..., k, n), do:
  ...
end
IO.puts(Slice.slice([], 0, 5) == nil)
IO.puts(Slice.slice(Range.to_list(1..5), 1, 3) == [2,3,4])
IO.puts(Slice.slice(Range.to_list(1..5), 4, 1) == [5])
IO.puts(Slice.slice(~c"almárium", 3, 3) == ~c"ári")
IO.puts(Slice.slice(~c"almárium", -3, 3) == nil)
```

A `benchee` segítségével mérje meg a futási időket különféle paraméterezések mellett, továbbá profilozással nézze meg, melyik klóz, illetve hívott függvény használja el a legtöbb futási időt! Hasonlítsa össze a saját `Slice.slice/3` függvénye futási idejét az `Enum.slice/3` függvényével különféle szélsőséges paraméterezések mellett!

<details>
<summary>Megoldás</summary>

```elixir
defmodule Slice do
  @spec slice(xs :: [any()], k :: integer(), n :: integer()) :: r :: [any()] | nil
  # Ha xs elég hosszú, r az xs k-tól induló, n hosszú részlistája; egyébként nil
  # Indexelés 0-tól
  def slice(_xs, 0, 0), do: []
  def slice([x|xs], 0, n) do
    case slice(xs, 0, n-1) do
      nil -> nil
      t -> [x|t]
    end
  end
  def slice([_x|xs], k, n), do: slice(xs, k-1, n)
  def slice([], _, _), do: nil
end
```

A tesztek mellé a megoldás egy hatodikat is ad, amely szintén `true`-t ír ki:

```elixir
IO.puts(Slice.slice(~c"almárium", 3, 9) == nil)
```

A mérés:

```elixir
l = Range.to_list(0..100_000)
Benchee.run(%{
        "begin" => fn -> Slice.slice(l, 0, 1_000) end,
        "middle" => fn -> Slice.slice(l, 50_000, 1_000) end,
        "end" => fn -> Slice.slice(l, 99_000, 1_000) end,
        "all" => fn -> Slice.slice(l, 0, 100_000) end,
        "beginEnum" => fn -> Enum.slice(l, 0, 1_000) end,
        "middleEnum" => fn -> Enum.slice(l, 50_000, 1_000) end,
        "endEnum" => fn -> Enum.slice(l, 99_000, 1_000) end,
        "allEnum" => fn -> Enum.slice(l, 0, 100_000) end
    },
    profile_after: true
)
```

A profilozás szerint a teljes lista kivágásakor (`all`) a futási idő 99,72%-át maga a `Slice.slice/3` használja el, 100 001 hívással.

</details>

### 7. Tagsági vizsgálat

Írjon rekurzív függvényt annak eldöntésére, hogy egy érték benne van-e egy listában! Ne használjon segédfüggvényt, ügyeljen a hatékonyságra.

```elixir
  defmodule Member do
    @spec member?(xs :: [any()], e :: any()) :: b :: boolean()
    # b == true, ha e benne van xs-ben, egyénként false
    def member?(..., e), do:
    ...
  end
  (Member.member?(~c"A szó elszáll", ?ó) == true) |> IO.inspect()
  (Member.member?([~c"A szó", ~c"elszáll", ~c"az írás", ~c"megmarad."], ~c"elszáll")
    == true) |> IO.inspect()
  (Member.member?([1.2, ?v, "str", false], false) == true) |> IO.inspect()
  (Member.member?([1.2, ?v, "str", false], "str") == true) |> IO.inspect()
  (Member.member?([1.2, ?v, "str", false], ~c"str") == false) |> IO.inspect()
  (Member.member?([], []) == false) |> IO.inspect()
```

<details>
<summary>Megoldás</summary>

Az első klóz mintájában az `e` változó kétszer szerepel, így csak akkor illeszkedik, ha a lista feje egyenlő a keresett értékkel:

```elixir
defmodule Member do
  @spec member?(xs :: [any()], e :: any()) :: b :: boolean()
  # b == true, ha e benne van xs-ben, egyénként false
  def member?([e|_], e), do: true
  def member?([_|xs], e), do: member?(xs, e)
  def member?([], _), do: false
end
```

Mind a hat teszt `true`-t ír ki.

</details>

### 8. Prímvizsgálat

Írjon rekurzív programot annak eldöntésére, hogy egy egész szám prím-e! Feltételezheti, hogy a függvényt egészszám-paraméterrel hívjuk. Segédfüggvényt használhat. Ügyeljen a hatékonyságra.

```elixir
  defmodule Prime do
    @spec prime?(x :: integer()) :: b :: boolean()
    # b == true, ha x prím
    def prime?(x), do:
    ...
  end
  (Prime.prime?(17) == true) |> IO.inspect()
  (Prime.prime?(18) == false) |> IO.inspect()
  (Prime.prime?(197_628) == false) |> IO.inspect()
  (Prime.prime?(1_000_003) == true) |> IO.inspect()
  (Prime.prime?(1_213_457) == false) |> IO.inspect()
  (Prime.prime?(179_424_691) == true) |> IO.inspect()
```

<details>
<summary>Megoldás</summary>

A segédfüggvény $\lfloor\sqrt{x}\rfloor$-től lefelé haladva próbálja az osztókat; ha 1-ig nem talált osztót, a szám prím. Az őrök a mintaillesztést egészítik ki az oszthatóság vizsgálatával:

```elixir
defmodule Prime do
  @spec prime?(x :: integer()) :: b :: boolean()
  # b == true, ha x prím
  def prime?(x), do: prime?(x, floor(:math.sqrt(x)))
  defp prime?(_x, 1), do: true
  defp prime?(x, y) when rem(x, y) == 0, do: false
  defp prime?(x, y) when rem(x, y) != 0, do: prime?(x, y-1)
end
```

Mind a hat teszt `true`-t ír ki. A megoldás $x \ge 2$ esetén helyes: `Prime.prime?(1)` is `true`-t ad, `Prime.prime?(0)` pedig `FunctionClauseError` hibát.

</details>

### További gyakorló feladatok

```elixir
defmodule Fp1Gy do
  @spec revapp(xs :: [integer()], ys :: [integer()]) :: zs :: [integer()]
  # zs == xs fordítottja ys elé fűzve
  def revapp(...) do
    ...
  end

  @spec rev(xs :: [integer()]) :: zs :: [integer()]
  # zs == xs fordítottja
  def rev(...) do
    ...
  end

  @spec diff(xs :: [integer()], ys :: [integer()]) :: zs :: [integer()]
  # zs == xs és ys különbsége, azaz xs azon elemei, melyek nincsenek benne ys-ben
  # a listában az azonos értékű elemeket külön elemeknek tekintjük,
  # azaz az ilyen lista zsák (bag), nem halmaz (set)
  def diff(...) do
    ...
  end
end
```

### Kiírás a rekurzív hívás előtt és után

Írjon lineárisan rekurzív függvényeket az alábbi feladatok megoldására direkt rekurzióval! Törekedjen elegáns, tömör, érthető és hatékony függvények írására.

**Kiírás a rekurzív hívás előtt.** Írjon olyan rekurzív függvényt `upto_by_3` néven, amely növekvő sorrendben kiírja az $1$ és $n$ közé eső, $n$-nél nem nagyobb, 3-mal osztható természetes számokat! Az $n$-et paraméterként adja át a függvénynek. A rekurzív hívás az adott klóz utolsó hívása, eredménye az adott klóz eredménye legyen, azaz a rekurzív hívás eredményével már ne végezzen semmilyen műveletet: a soron következő számot tehát a rekurzív hívás **előtt** írja ki. Segédfüggvényt definiálhat. Használjon őrt a minta szerinti feltétel kiegészítésére.

```elixir
defmodule UptoBy3TailR do
  @spec upto_by_3(n :: integer()) :: :ok
  def upto_by_3(n) do
    IO.puts(i)
    ...
  end
end
UptoBy3TailR.upto_by_3(20)
```

<details>
<summary>Megoldás</summary>

```elixir
defmodule UptoBy3TailR do
  @spec upto_by_3(n :: integer()) :: :ok
  def upto_by_3(n), do: upto_by_3(3, n)
  defp upto_by_3(i, n) when i <= n do
    IO.puts(i)
    upto_by_3(i+3, n)
  end
  defp upto_by_3(i, n) when i > n, do: :ok
end
UptoBy3TailR.upto_by_3(20)
```

</details>

**Kiírás a rekurzív hívás után.** Írja át előző megoldását úgy, hogy a rekurzív hívás az adott klóz első hívása legyen, azaz a rekurzív hívás *előtt* ne végezzen semmilyen műveletet: a soron következő számot tehát a rekurzív hívás **után** írja ki. Az eredményt továbbra is növekvő sorrendben írja ki. Segédfüggvényt definiálhat.

```elixir
defmodule UptoBy3HeadR do
  @spec upto_by_3(n :: integer()) :: :ok
  def upto_by_3(n) do
    ...
    IO.puts(i)
  end
end
UptoBy3HeadR.upto_by_3(20)
```

Vesse össze a két függvényalkalmazás által kiírt számsorozatot! Miben különbözik a kétféle megoldás veremhasználata?

Tipp: előfordulhat, hogy a második változata nem teljesíti a specifikációt, hogy ti. növekvő sorrendben kell kiírni a számokat. Ezen úgy segíthet, hogy nem 1-től felfelé halad a generáláskor, hanem $n$-től lefelé. Ennek az a járulékos előnye itt és hasonló esetekben, hogy a végállomás a 0 (esetleg más, előre tudható konstans) lesz, így elég a mintaillesztés, ami hatékonyabb, mintha őrt is használnánk. Ha tehát most is őrt használt volna, cserélje le pusztán mintaillesztésre. Használjon segédfüggvényt.

<details>
<summary>Megoldás</summary>

```elixir
defmodule UptoBy3HeadR do
  @spec upto_by_3(n :: integer()) :: :ok
  def upto_by_3(n), do: downto_by_3(n - rem(n, 3))
  defp downto_by_3(0), do: :ok
  defp downto_by_3(i) do
    downto_by_3(i - 3)
    IO.puts(i)
  end
end
UptoBy3HeadR.upto_by_3(20)
```

Mindkét változat a 3, 6, 9, 12, 15, 18 számokat írja ki, soronként. A balrekurzív változat előbb lemegy a 0-ig, és a számokat a visszatérés során írja ki; ehhez minden szám a verembe kerül.

</details>

<p class="sources">Forrás: dp26a-fp1ea.pdf (23., 47., 50. dia), dp26a-fp1ea-sum-benchee.livemd, dp26a-fp1gyfel.livemd, dp26a-fp1gy-megoldasok.livemd, dp26a-fp2gy-megoldasok.livemd</p>
