# dp26a-fp3ea.pdf

<!-- 90 pages, 31 units, grouping: labels -->

## s1 · p1 · (no title)
<!-- status: auto -->
<!-- header: Deklaratív programozás 3. előadás | 1 / 31 -->

Deklaratív programozás 3. előadás

Kabódi László^(1) Marussy Kristóf^(2)

BME Számítástudományi és Információelméleti Tanszék Mesterséges Intelligencia és Rendszertervezés Tanszék

1`kabodi.laszlo@vik.bme.hu`

2`marussy@mit.bme.hu`

2026. ősz

## s2 · p2 · I. rész
<!-- status: auto -->

Problémamegoldási technikák

1 Problémamegoldási technikák

2 For-jelölés (for-comprehension)

3 Műveletek, BIFek, típusvizsgálat/konverzió, mintaillesztés

4 Hasznos segédeszköz: dialyzer

## s3 · p3 · Tartalom
<!-- status: auto -->
<!-- header: Problémamegoldási technikák | FPE-3 – Problémamegoldási technikák: csúszóablak használata | 3 / 31 -->

1 Problémamegoldási technikák
- FPE-3 – Problémamegoldási technikák: csúszóablak használata
- FPE-3 – Problémamegoldási technikák: kihagy-bevesz rekurzió

## s4 · p4 · Csúszóablakos technika: maximális összegű folytonos részlisták
<!-- status: auto -->
<!-- header: Problémamegoldási technikák | FPE-3 – Problémamegoldási technikák: csúszóablak használata | 4 / 31 -->

Egy lista különféle szempontok szerint kiválasztott folytonos részlistáit csúszóablakos módszerrel állíthatjuk elő, egymásba ágyazott ismétlésekkel. Mivel a funkcionális nyelvekben nincs ciklus, az ismétlést rekurzióval valósítjuk meg, a részeredményeket egy, esetleg több akkumulátorban gyűjtjük. Mivel a gyűjtéshez plusz paraméter(ek)re van szükség, általában segédfüggvényeket is definiálunk. A lista maximális összegű folytonos részlistáinak előállítására többféle megoldást is bemutat a harmadik előadás segédanyaga. Az egyes megoldások futási idejét is megmérjük a `benchee`-vel. Egy példa:
- Bemenet (egészlista): `[1, 2, 3, 4, -10, 4, 3, 2, 1]`
- Eredmény (egy pár, első eleme a részlisták összege, második eleme ezen maximális összegű részlisták listája):

```
{10, [[1, 2, 3, 4], [1, 2, 3, 4, -10, 4, 3, 2, 1], [4, 3, 2, 1]]}
```

A harmadik előadás segédanyaga a honlapról letölthető:
- dp26a-fp3ea-reszlistak-kihagy_bevesz_rek.livemd

## s5 · p5 · Tartalom
<!-- status: auto -->
<!-- header: Problémamegoldási technikák | FPE-3 – Problémamegoldási technikák: kihagy-bevesz rekurzió | 5 / 31 -->

1 Problémamegoldási technikák
- FPE-3 – Problémamegoldási technikák: csúszóablak használata
- FPE-3 – Problémamegoldási technikák: kihagy-bevesz rekurzió

## s6 · p6 · Kihagy-bevesz rekurzió: elemek kombinációja, kétfelé válogatása
<!-- status: auto -->
<!-- header: Problémamegoldási technikák | FPE-3 – Problémamegoldási technikák: kihagy-bevesz rekurzió | 6 / 31 -->

A harmadik előadás segédanyagában két példa is van a kihagy-bevesz (inclusion-exclusion) rekurzióra. Az első, `komb/1` egy lista elemeinek összes kombinációját adja eredményül, a második, `eloszt/1` pedig megmutatja, hogy listaelemeket hányféleképpen lehet úgy kétfelé válogatni, hogy a részösszegek különbségének abszolút értéke a lehető legkisebb legyen. Példák a függvényhívásokra és az eredményekre:

1 `komb([1,2,3]) == [[], [1], [2], [2,1], [3], [3,1], [3,2], [3,2,1]]`

2 `eloszt([28, 7, 11, 8, 9, 7, 27]) == %{[9, 11, 28] => 48}`

3 `eloszt([4,1,2,5,3]) == %{[4, 2, 1] => 7, [4, 3] => 7, [5, 2] => 7}`

Az `eloszt/1` eredménye egy szótár (map), melynek kulcsai az összegfeltételt kielégítő részlisták, elemei pedig az összegfeltételt kielégítő kisebbik összeg. A második példában tehát a fennmaradó `[7,7,8,27]` elemekből áll az eredményben nem szereplő másik rész, melynek összege `49`. A harmadik előadás segédanyaga, mint már írtuk, a honlapról letölthető:
- dp26a-fp3ea-reszlistak-kihagy_bevesz_rek.livemd

## s7 · p7 · Dinamikus programozás: olvasnivalók, feladatok gyakorlásra
<!-- status: auto -->
<!-- header: Problémamegoldási technikák | FPE-3 – Problémamegoldási technikák: kihagy-bevesz rekurzió | 7 / 31 -->

- Az Algoritmuselmélet (VISZAA08) tantárgy dinamikus programozásról szóló és
- más prezentációi: <https://www.cs.bme.hu/algel/>
- Horváth Gyula (ELTE) összefoglalója és feladatgyűjteménye a dinamikus programozásról: <https://people.inf.elte.hu/szlavi/VersenyFeladatok/DinaProg/dinprog.pdf>
- A Közép-európai Informatikai Diákolimpia (Central-European Olympiad in Informatics, CEOI) versenyfeladatai: <http://ceoi.inf.elte.hu/tasks-archive/>
- A Nemzetközi Informatikai Diákolimpia (International Olympiad in Informatics, IOI) versenyfeladatai: <https://ioi.contest.codeforces.com/> (regisztráció szükséges)
- DSA Tutorial – Learn Data Structures and Algorithms: <https://www.geeksforgeeks.org/dsa/>

```
dsa-tutorial-learn-data-structures-and-algorithms/ (sok példával és
```

gyakorló feladattal), többek között a dinamikus programozásról: <https://www.geeksforgeeks.org/competitive-programming/dynamic-programming/>

Links: <http://ceoi.inf.elte.hu/tasks-archive/>, <https://ioi.contest.codeforces.com/>, <https://people.inf.elte.hu/szlavi/VersenyFeladatok/DinaProg/dinprog.pdf>, <https://www.cs.bme.hu/algel/>, <https://www.geeksforgeeks.org/competitive-programming/dynamic-programming/>, <https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/>

## s8 · p8 · II. rész
<!-- status: auto -->

For-jelölés (for-comprehension)

1 Problémamegoldási technikák

2 For-jelölés (for-comprehension)

3 Műveletek, BIFek, típusvizsgálat/konverzió, mintaillesztés

4 Hasznos segédeszköz: dialyzer

## s9 · p9 · Tartalom
<!-- status: auto -->
<!-- header: For-jelölés (for-comprehension) | FPE-3 – For-jelölés (for-komprehenzió, for-comprehension) | 9 / 31 -->

2 For-jelölés (for-comprehension)
- FPE-3 – For-jelölés (for-komprehenzió, for-comprehension)

## s10 · p10-13 · For-jelölés 1
<!-- status: TODO view pages/p013.png -->
<!-- flags: graphic -->
<!-- figure: figures/p013-f1.png -->
<!-- header: For-jelölés (for-comprehension) | FPE-3 – For-jelölés (for-komprehenzió, for-comprehension) -->

Gyűjtemények (kollekciók) kezelésére használjuk a for-jelölést, vagy az angol elnevezést teljesen átvéve: a for-komprehenziót). Most vegyünk sorra mindent, amit a for-jelölésről tudni kell (a szögletes zárójelek jelentése itt: opcionális). A for-jelölés: `for` q1[, q2, ..., qn][, `into:` coll], `do:` exp*, ahol*
- a `q`i
1 `pattern <- list` alakú generátor, vagy 2 predikátum (igazságérték-eredményű függvény, feltétel);
- legalább egy `q`i-nak generátornak kell lennie;
- a `pattern` mintának illeszkednie kell a `list` lista kiválasztandó elemeire, és ki kell elégítenie az adott `pattern <- list` generátortól jobbra álló összes `q`i predikátumot;
- az `exp` tetszőleges, a `pattern` mintától függő vagy nem függő kifejezés;
- a generátorban a minta előállítására lista helyett más felsorolható kollekciót, leggyakrabban tartomány-típusú értéket is megadhatunk.
(Folytatás a következő dián.)

## s11 · p14-17 · For-jelölés 2
<!-- status: auto -->
<!-- header: For-jelölés (for-comprehension) | FPE-3 – For-jelölés (for-komprehenzió, for-comprehension) -->

A for-jelölés (folyt.): `for` q1[, q2, ..., qn][, `into:` coll], `do:` exp*, ahol*
- az opcionális `into:` opció után álló `coll`-lal megadhatjuk, hogy milyen
- típusú felsorolható kollekciót hozzon létre a for-jelölés, ha elhagyjuk,
- alapértelmezés szerint lista jön létre;
- `coll`-ként üres kollekciót kell megadni: `""` (sztring), `%{}` (szótár), `[]` (lista), `<<>>` (bináris);
- a for-jelölésben definiált változók lokálisak;
- a for-jelölés értéke az összes olyan `exp`j kifejezés kollekciója, amelyre a **mintaillesztés sikerült** és a **predikátumok teljesültek;**
- a for-jelölés eddig bemutatott változata tehát egy vagy több kollekció elemein műveletek elvégzésére és/vagy bizonyos elemek szűrésére használható (vö. `Enum.map/2`, `Enum.filter/2`).
- Összefoglaló a for-jelölésről: <https://www.mitchellhanberg.com/the-comprehensive-guide-to-elixirs-for-comprehension/>
- A komprehenzió ma már sokféle programozási nyelvben megtalálható, lásd: <https://en.wikipedia.org/wiki/List_comprehension>

Links: <https://en.wikipedia.org/wiki/List_comprehension>, <https://www.mitchellhanberg.com/the-comprehensive-guide-to-elixirs-for-comprehension/>

## s12 · p18-19 · For-jelölés 3
<!-- status: auto -->
<!-- header: For-jelölés (for-comprehension) | FPE-3 – For-jelölés (for-komprehenzió, for-comprehension) -->

A for-jelölés `uniq:` opcióval: `for` q1[, q2, ..., qn][, `into:` coll], `uniq: true|false`, `do:` exp*, ahol*
- a `uniq: true` opció hatására az előállított gyűjteménybe csak egymástól
- különböző értékek kerülnek be;
- csak lista, sztring és bináris esetén van értelme használni, hiszen a szótárban a kulcsok sohasem ismétlődhetnek.
A for-jelölés `reduce:` opcióval: `for` q1[, q2, ..., qn], `reduce:` acc0 `do` acc -> fun(pat, acc) `end`*, ahol*
- a `reduce:` opcióval a for-jelölés nem az `Enum.map/2`-et, hanem az `Enum.reduce/3`-t váltja ki,
- az acc0 az eredményt gyűjtő akkumulátor kezdőértéke,
- a `do` . . . `end` között egy névtelen függvényt kell megadni (az `fn` és a hozzá tartozó `end` nélkül!), amelynek egyetlen argumentuma az acc akkumulátor (a neve bármi lehet), a törzsében pedig egy olyan kétargumentumú függvényt vagy operátort kell használni, amelynek két argumentuma közül az egyik a generátorban használt pat minta, a másik pedig ugyancsak az acc akkumulátor (az argumentumok sorrendjének hatása lehet az eredményre!).

## s13 · p20-24 · For-jelölés: kis példák 1
<!-- status: auto -->
<!-- header: For-jelölés (for-comprehension) | FPE-3 – For-jelölés (for-komprehenzió, for-comprehension) -->

```
iex> for x <- 1..6 // 2, do: x     # { x | x ∈{1, 3, 5} }
[1, 3, 5]
iex> for x <- [1,2,3], do: 2*x+1   # { 2 · x + 1 | x ∈{1, 2, 3} }
[3, 5, 7]
iex> for x <- 1..9, rem(x, 2) === 0, x > 2, do: 2*x
[8, 12, 16]
iex> for {k,v} <- [egy: 1, két: 2, há: 3], into: %{}, do: {k,v}
%{egy: 1, há: 3, két: 2}
iex> for {k,v} <- %{egy: 1, két: 2, há: 3}, into: [], do: {k,v}
[egy: 1, há: 3, két: 2]
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

## s14 · p25-30 · For-jelölés: kis példák 2
<!-- status: auto -->
<!-- header: For-jelölés (for-comprehension) | FPE-3 – For-jelölés (for-komprehenzió, for-comprehension) -->

```
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
<31::size(5)>>
iex> for _i <- 1..5, into: <<>>, uniq: true, do: <<1::size 1>> # 1 bit (0b1), 1 byte
<<1::size(1)>>
iex> for _i <- 1..5, into: <<>>, do: <<1::size 2>> # 10 bit (0b01010101, 0b01), 2 byte
<85, 1::size(2)>>
iex> for _i <- 1..5, into: <<>>, uniq: true, do: <<1::size 2>> # 2 bit (0b01), 1 byte
<1::size(2)>>
```

## s15 · p31 · III. rész
<!-- status: auto -->

Műveletek, BIFek,

típusvizsgálat/konverzió, mintaillesztés

1 Problémamegoldási technikák

2 For-jelölés (for-comprehension)

3 Műveletek, BIFek, típusvizsgálat/konverzió, mintaillesztés

4 Hasznos segédeszköz: dialyzer

## s16 · p32 · Tartalom
<!-- status: auto -->
<!-- header: FPE-3 – Alapműveletek, beépített függvények -->

3 Műveletek, BIFek, típusvizsgálat/konverzió, mintaillesztés
- FPE-3 – Alapműveletek, beépített függvények
- FPE-3 – Mintaillesztés

## s17 · p33-34 · Aritmetikai és bitműveletek
<!-- status: auto -->
<!-- header: FPE-3 – Alapműveletek, beépített függvények -->

- Aritmetikai műveletek (Kernel modul)
  - Előjel: `+`, `-` (precedencia: 1)
  - Multiplikatív műveletek: `*`, `/`, `div`, `rem` (precedencia: 2)
  - Additív műveletek: `+`, `-` (precedencia: 3)
- Bitműveletek (Bitwise modul)
  - `bnot` vagy `~~~`, `band` vagy `&&&` (precedencia: 2)
  - `bor` vagy `|||`, `bxor`, `bsl` vagy `<<<`, `bsr` vagy `>>>` (precedencia: 3)
Megjegyzések
- `+`, `-`, `*` és `/` egész és lebegőpontos operandusokra is alkalmazhatók
- `+`, `-` és `*` eredménye egész, ha mindkét operandusuk egész, egyébként lebegőpontos
- `/` eredménye mindig lebegőpontos
- `div` és `rem` prefix helyzetűek, ereményük egész
- `div`, `rem` és a bitműveletek operandusai csak egészek lehetnek
- `~~~`, `&&&`, `|||`, `<<<`, `>>>` infix, a többi bitművelet prefix helyzetű
- A bitműveleteket engedélyezni kell: `use Bitwise` vagy

```
use Bitwise[, (only_operators | skip_operators): true]
```

## s18 · p35-37 · Összehasonlító műveletek (relációk)
<!-- status: TODO view pages/p037.png -->
<!-- flags: graphic, image, layout -->
<!-- figure: figures/p037-f1.png -->
<!-- header: FPE-3 – Alapműveletek, beépített függvények -->

- Egy reláció (összehasonlítás) eredménye a `true` vagy `false` atom
- Termek összehasonlítási sorrendje (vö. típusok):

```
number < atom < reference < function < port < pid < tuple < list < binary
```

- Kisebb, kisebb-egyenlő, nagyobb-egyenlő, nagyobb: `<`, `<=`, `>=`, `>`
- Érték szerinti egyenlőség (`integer` és `float` lehet egyenlő): `==`, `!=`
- Szigorú egyenlőség (`integer` és `float` nem lehet egyenlő): `===`, `!==`
- Példák: `5.0 == 5 == true`, `5.0 === 5 == false`
Elrettentő példák:

```
10.1 - 9.9 == 0.2 ; false
(10.1 - 9.9) * 10 ;
1.999999999999993
0.000000000000001 + 1 == 1 ; false
0.0000000000000001 + 1 == 1 ; true
```

Lebegőpontos értékek összehasonlítása helyett vizsgáljuk a különbségüket a `<=` vagy `>=` relációval (ε-nál kisebb-e a különbségük?)

## s19 · p38-40 · Logikai műveletek
<!-- status: TODO view pages/p040.png -->
<!-- flags: layout -->
<!-- header: FPE-3 – Alapműveletek, beépített függvények -->

- Prefix helyzetű operátor: `not` és `!`; `not` operandusa csak `boolean`, `!`-é
  - `not`, `and` és `or` használható őrkifejezésben, `!`, `&&` és `||` nem.
  - `and` és `or` első operandusa csak `boolean`, `&&` és `||` első operandusa
  - A `false` és `nil` értékű kifejezéseket kivéve minden más érték
  - Második operandusuk tetszőleges típusú kifejezés lehet
  - Eredményük típusa a két operandus típusának uniója
  - Lusta kiértékelésű, ún. short-circuit műveletek: ha az első operandus kiértékelése eldönti eredményt, a másodikra nem kerül sor
tetszőleges típusú kifejezés lehet
- Infix helyzetű operátorok: `and` és `&&`, `or` és `||`
tetszőleges típusú kifejezés lehet

`true`-nak számít.
- Példák:

```
iex> !:atom && div(3,0) === 2
false
iex> :atom && div(3,0) === 2
** ...bad argument in ...: div(3, 0)
iex> :atom and rem(3,2) === 1
```

```
                                                 iex> true and rem(3,2)
                                                 1
                                                 iex> false and rem(3,2)
                                                 false
                                                 iex> nil && rem(3,2)
** ...expected a boolean on left-side of "and"   nil
```

## s20 · p41-42 · Beépített függvények (Built-In Functions, BIFs)
<!-- status: TODO view pages/p042.png -->
<!-- flags: math -->
<!-- header: FPE-3 – Alapműveletek, beépített függvények -->

- A BEAM-be beépített, rendszerint C-ben írt függvények
- Többségük az erts Erlang-könyvtár `erlang` moduljának része
- Elixir-specifikációjuk az Elixir Kernel moduljában található
- A csak az Erlang `erlang` moduljában definiált BIF-ek az `:erlang` modulnévvel hívhatók
- Az alaptípusokon alkalmazható leggyakoribb BIF-ek:
  - Számok: `abs(num)`, `trunc(num)`, `ceil(num)`, `floor(num)`,

```
round(num), :erlang.float(num)
```

  - `:erlang.float` helyett 1-gyel oszthatjuk az egész számot, pl. `5/1`
  - Sztring, bináris: `bit_size(string)`, `byte_size(string)`
  - Szótár: `map_size(map)`
  - Ennes: `tuple_size(tuple)`, `elem(tuple, index)`,

```
put_elem(tuple, index, value)1
```

  - Lista: `length(list)`, `hd(list)`, `tl(list)`
- Az operátorok is BIF-ek a `Kernel`-ben, pl. `Kernel.*(3,4)`
1Megjegyzés: `0` ≤`index` ≤`tuple_size(tuple)-1`

## s21 · p43-44 · Egyéb alapfügvények (típusvizsgálat és típuskonverzió)
<!-- status: auto -->
<!-- header: FPE-3 – Alapműveletek, beépített függvények -->

- Típusvizsgálat (BIF-ek a Kernelben)
  - `is_integer(term)`, `is_float(term)`, `is_number(term)`,
  - `is_atom(term)`, `is_boolean(term)`, `is_nil(term)`,
  - `is_binary(term)`, `is_bitstring(term)`,
  - `is_tuple(term)`, `is_list(term)`„ `is_map(term)`
  - `is_function(term)`, `is_function(term, arity)`
- Típuskonverzió (az egyes típusokhoz tartozó modulokban)
  - Atom: `to_charlist(atom)`, `to_string(atom)`,
  - Float: `to_charlist(float)`, `to_string(float)`,
  - Integer: `to_charlist(integer)`, `to_string(integer)`,
  - List: `to_atom(list)`, `to_charlist(list)`, `to_float(list)`,

```
to_integer(list), to_integer(list, base), to_string(list),
to_tuple(list)
```

  - String: `to_atom(list)`, `to_charlist(string)`, `to_float(string)`,

```
to_integer(string), to_integer(string, base),
```

  - Tuple: `to_list(tuple)`,
  - Map: `to_list(map)`,

## s22 · p45 · Tartalom
<!-- status: auto -->

3 Műveletek, BIFek, típusvizsgálat/konverzió, mintaillesztés
- FPE-3 – Alapműveletek, beépített függvények
- FPE-3 – Mintaillesztés

## s23 · p46-49 · Mintakifejezés, minta, mintaillesztés (pattern matching)
<!-- status: auto -->

- Mintakifejezés, röviden minta: termhez hasonló olyan kifejezés, amelyben nincs függvénykifejezés, de lehet benne szabad változó
- Egy szabad változó mindenre illeszkedik, és lehet rá hivatkozni
- Az aláhúzásjel (_) és a vele kezdődő változónév mindenre illeszkedik; az előbbire nem lehet, az utóbbira nem szokás hivatkozni
- Egy mintában ugyanaz a változó többször is előfordulhat, ha mindenütt azonos értékre kell illeszkednie
- A mintaillesztés műveleti jele az `=`, bal oldalán a mintával, jobb oldalán egy tömör kifejezéssel (a mintaillesztés egyirányú)
- A mintaillesztés a minta nem fixált (vö. ^ operátor) változóit értékhez köti
- A kötés **nem** értékadás!
- Függvényhíváskor az aktuális paramétereket illesztjük a formális paraméterekre
- Ha egy változót értékhez kötünk, de nem használjuk, az Elixir figyelmeztet rá, kivéve akkor, ha a változónév _-sal kezdődik
- Figyelem: a Prologban a funkcionális nyelvekkel ellentétben kétirányú mintaillesztés van, egyesítés a neve

## s24 · p50-60 · (no title)
<!-- status: auto -->

```
iex> [x, &+/2] = [5, &+/2]
** (CompileError) ... & is not allowed in matches
iex> [x, f] = [5, &+/2]
[5, &:erlang.+/2]
iex> [x, f] = [5, f]
[5, &:erlang.+/2]
iex> a = fn(x) -> x+1 end
#Function<44.40011524/1 in :erl_eval.expr/5>
iex> {a, b} = {fn(x) -> x+1 end, 23}
#Function<44.40011524/1 in :erl_eval.expr/5>, 23
iex> fn(x) -> x+1 end = a
** (CompileError) ... fn is not allowed in matches
iex> 3 = szabad
** (CompileError) iex:505: undefined function szabad/0
iex> [z | zs] = [0,1,2,3]
[0, 1, 2, 3]
iex> [z1 | [z2 | [z3 | [z4 | zs]]]] = [0,1,2,3]
[0, 1, 2, 3]
iex> [z1, z2, z3 | [3]] = [0,1,2,3]
[0, 1, 2, 3]
```

## s25 · p61-72 · (no title)
<!-- status: auto -->

```
iex> [z1, z2, z3 | 3] = [0,1,2,3]
** (MatchError) no match of right hand side value: [0, 1, 2, 3]
iex> [z1, z2 | [3]] = [0,1,2,3]
** (MatchError) no match of right hand side value: [0, 1, 2, 3]
iex> {{a, b}, {a, b}} = {{:a, :b}, {:a, :b}}
{{:a, :b}, {:a, :b}}
iex> {{a, b, a}} = {{:a, :b, :b}}
** (MatchError) no match of right hand side value: {{:a, :b, :b}}
iex> {a, b, _b, _} = {:a, :b, :b, :a}
{:a, :b, :b, :a}
iex> {a, b}
{:a, :b}
iex> _b
warning: the underscored variable "_b" is used after being set...
please rename the variable to remove the underscore
:b
iex> x = %{b: "barna", z: "zöld"}
%{b: "barna", z: "zöld"}
iex> %{k1: v1, k2: v2} = x
** (MatchError) no match of right hand side value: %{b: "barna", z: "zöld"}
```

## s26 · p73-85 · (no title)
<!-- status: auto -->

```
iex> %{k1 => v1, k2 => v2} = x
** (CompileError) iex:3: cannot use variable k1 as map key inside a pattern...
iex> %{b: v1, z: v2} = x
%{b: "barna", z: "zöld"}
iex> {v1, v2}
"barna", "zöld"
iex> %{z: ^v1, b: v2} = x
** (MatchError) no match of right hand side value: %{b: "barna", z: "zöld"}
iex> %{z: v1, b: v2} = x
%{b: "barna", z: "zöld"}
iex> {v1, v2}
"zöld", "barna"
iex> %{b: v} = x # részleges mintaillesztés
%{b: "barna", z: "zöld"}
iex> v
"barna"
iex> ([y|ys] = yss) = [1, 2, 3] # réteges minta (layered pattern)
[1,2,3]
iex> {y, ys, yys}
{[1], [2, 3], [1,2,3]}
```

## s27 · p86 · IV. rész
<!-- status: auto -->

Hasznos segédeszköz: dialyzer

1 Problémamegoldási technikák

2 For-jelölés (for-comprehension)

3 Műveletek, BIFek, típusvizsgálat/konverzió, mintaillesztés

4 Hasznos segédeszköz: dialyzer

## s28 · p87 · Tartalom
<!-- status: auto -->
<!-- header: Hasznos segédeszköz: dialyzer | FPE-3 – Programok statikus analízise: dialyzer -->

4 Hasznos segédeszköz: dialyzer
- FPE-3 – Programok statikus analízise: dialyzer

## s29 · p88 · dialyxir telepítése
<!-- status: auto -->
<!-- header: Hasznos segédeszköz: dialyzer | FPE-3 – Programok statikus analízise: dialyzer -->

```
 # Run "mix help deps" to learn about dependencies.
 defp deps do
  [
   {:dialyxir, "~> 1.4", only: [:dev, :test], runtime: false},
   # {:dep_from_hexpm, "~> 0.3.0"},
   # {:dep_from_git, git: "https://github.com/elixir-lang/my_dep.git", tag: ...}
  ]
 end

Telepítsük és fordítsuk le az új modulokat!2

~/tmp/fp$ mix do deps.get, deps.compile
Resolving Hex dependencies...
Resolution completed in 0.051s
New:
  dialyxir 1.4.6
  erlex 0.2.7
...
Compiling ...
```

2Az új modulok az adott projekt részei lesznek, lokálisak, nem globálisak.

## s30 · p89 · Szignatúravizsgálat: mix dialyzer
<!-- status: auto -->
<!-- header: Hasznos segédeszköz: dialyzer | FPE-3 – Programok statikus analízise: dialyzer -->

- A projekt forrásfájljainak a `lib` mappában kell lenniük: rakjunk be ide egy
- Elixir programot, pl. az egyik kisházit, rontsunk el egy-két specifikációt, és
- dializáljuk.
- A dializálás a `lib` mappában lévő **összes** `.ex` fájlt vizsgálja.
- Az első futtatás soká tart, mert a dialyzer rengeteg ún. PLT-fájlt telepít a modulokhoz tartozó típusszignatúrákkal (PLT = Persistent Lookup Table).
- A dializálás a `.beam` fájlokat elemzi, ezért ha változott valamelyik forrásfájl, az elemzés előtt fordítás készül belőle.

```
@spec sum(xs::[integer()]) :: s::[integer()]
# Az xs számlista összege s
def sum([x|xs]), do: x + sum(xs)
def sum([]), do: 0
~/tmp/fp$ mix dialyzer
lib/sum.ex:2:invalid_contract
The @spec for the function does not match the success typing ...
Function: Sum.sum/1
Success typing: ([number()]) -> number()
But the spec is: (xs::[integer()]) -> s::[integer()]
```

## s31 · p90 · 3. gyakorlat
<!-- status: auto -->
<!-- header: Hasznos segédeszköz: dialyzer | FPE-3 – Programok statikus analízise: dialyzer -->

- Alapvetően *otthoni munka*, a gyakorlaton megbeszéljük a feladatok megoldásait
- Gyakorlat anyaga: <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp3gy.livemd>
- Felkészüléshez ajánlott: <https://dp.iit.bme.hu/dp26a/ea/dp26a-fp3ea-reszlistak-kihagy_bevesz_rek.livemd>

Links: <https://dp.iit.bme.hu/dp26a/ea/dp26a-fp3ea-reszlistak-kihagy_bevesz_rek.livemd>, <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp3gy.livemd>
