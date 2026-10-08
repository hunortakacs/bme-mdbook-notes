# dp26a-fp2ea.pdf

<!-- 118 pages, 49 units, grouping: labels -->

## s1 · p1 · (no title)
<!-- status: auto -->
<!-- header: Deklaratív programozás 2. előadás | 1 / 49 -->

Deklaratív programozás 2. előadás

Kabódi László^(1) Marussy Kristóf^(2)

BME Számítástudományi és Információelméleti Tanszék Mesterséges Intelligencia és Rendszertervezés Tanszék

1`kabodi.laszlo@vik.bme.hu`

2`marussy@mit.bme.hu`

2026. ősz

## s2 · p2 · I. rész
<!-- status: auto -->

Típusok, termek, azonosítók, változók

1 Típusok, termek, azonosítók, változók

2 Műveletek listákon

3 Műveletek sztringeken

4 Problémamegoldási technikák

## s3 · p3 · Tartalom
<!-- status: auto -->
<!-- header: 3 / 49 -->

1 Típusok, termek, azonosítók, változók
- FPE-2 – Típusok: atom, szám, függvény, ennes, tartomány, lista
- FPE-2 – Termek, azonosítók, változók

## s4 · p4 · Típusok1
<!-- status: TODO view pages/p004.png -->
<!-- flags: table -->
<!-- header: 4 / 49 -->

Az Elixir erősen típusos nyelv, dinamikus típusellenőrzéssel.

**Értéktípusok**

**Value types**

Atom

Atom

Tetszőleges hosszú egész szám Arbitrary-sized integer (integer) Lebegőpontos szám

Floating-point number (float)

Függvény

Function

Tartomány

Range

Reguláris kifejezés

Regular expression (regex)

Sztring

String

**Kollekció-típusok** **Collection types** Ennes

Tuple

Lista

List

Bináris

Binary

Szótár

Map

Struktúra

Struct

1A felsorolás nem teljes. A dőlt betűs típusok más alaptípusokra épülnek.

## s5 · p5 · Atom
<!-- status: auto -->
<!-- header: 5 / 49 -->

- Kettősponttal (:) kezdődik
- Kezdődhet az angol ábécé nagybetűjével is, kettőspont nélkül, de ez konvenció szerint a modulnevekre van fenntartva
- A : után UTF-8 kódolású karaktersorozat, Elixir operátor vagy sztring állhat
- Az UTF-8 kódolású karaktersorozatban betűk, számjegyek és kétféle írásjel (_, @) lehetnek
- A karaktersorozat végén általában kérdőjel (?) vagy felkiáltójel (!) is lehet
- Saját magát jelöli, nem sztring: egy atom értéke maga a neve
- Két azonos nevű atom mindig egyenlő, akárhol is vannak definiálva
- Hasonló a Prolog névkonstanshoz (atomhoz)
- Példák: `:jános`, `:is_bin?`, `:vált@2`, `:<>`, `:"fun/3"`, `:"éljen soká!"`,

```
:Éljen_soká!, :"Őrült Űrőr tűrjön", Dp, Gy1
```

## s6 · p6-7 · Szám
<!-- status: TODO view pages/p007.png -->
<!-- flags: math -->
<!-- header: 6 / 49 -->

- Egész (integer)
  - Decimális, pl. 1234
  - Hexadecimális, pl. 0xcafe
  - Oktális, pl. 0o765
  - Bináris, pl. 0b1010
  - Tagolható, pl. `123_456_789`
  - Korlátlan pontosságú, pl. `123456789012345678901234567890`
  - Karakterkód (Unicode codepoint)
    - Ha nyomtatható: `?z`
    - Ha vezérlő: `?\n`
- Lebegőpontos (float)
  - Pl. `3.14159`,
  - Vezető nullával, pl. `0.14159`
  - Exponenssel pl. `0.2e-22`
  - IEEE 754 szerinti, dupla pontosságú (64 bit, kb. 16 számjegy, max. exponens kb. 10^(308))

## s7 · p8-11 · Függvény (Function) 1
<!-- status: auto -->
<!-- header: 7 / 49 -->

- A függvény is érték: változóhoz köthető, adatstruktúra eleme lehet, függvény eredménye lehet, paraméterként átadható stb. Azaz: a függvény is ún. first class citizen, teljes jogú polgár
- Példák:

```
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

## s8 · p12-16 · Függvény (Function) 2
<!-- status: auto -->
<!-- header: 8 / 49 -->

- További példák: anonim függvény definiálása, hívása, névhez kötése

```
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

- További példa: függvénydefiníció `def`-fel, `defp`-vel

```
def sum_of_squares(a,b), do: sqr(a) + sqr(b)
defp sqr(a), do: a*a # p[rivát], azaz lokális a modulon belül
iex> Fpea.sum_of_squares 3, 4.5
29.25
```

- Függvény típusa: `(`arg1 típusa`,` arg2 típusa`,` . . . `) ::` eredmény típusa Pl. a `sum_of_squares/2` függvényé: `(number, number) :: number`

## s9 · p17-19 · Paraméter alapértelmezett (default) értéke
<!-- status: auto -->
<!-- header: 9 / 49 -->

- Egy függvény egy vagy több paraméterének adhatunk alapértelmezett értéket a `\\` jelöléssel. Az ilyen paraméter opcionális, a többi elvárt.
- Ha egy függvényt
  - a kötelezően (default argumentumok nélkül) elvártnál kevesebb paraméterrel hívunk meg, a hívás meghiúsul;
  - az elvárt számú paraméterrel hívunk meg, az összes opcionális paraméter az alapértelmezett értékét veszi fel;
  - az elvártnál több paraméterrel hívunk meg, az aktuális paraméterek értékét balról jobbra haladva veszik fel az opcionális paraméterek.
- Példák alapértelmezett értékekkel

```
def sum_of_sqrs_b5(a, b \\ 5), do: sqr(a) + sqr(b)
iex> Fpea.sum_of_sqrs_b5 3, 4.5
29.25
iex> Fpea.sum_of_sqrs_b5 3
34
def sum_of_sqrs_b5(a \\ 6, b \\ 5), do: sqr(a) + sqr(b)
iex> Fpea.sum_of_sqrs_a6b5 3
34
iex> Fpea.sum_of_sqrs_a6b5
61
```

## s10 · p20-21 · Ennes (Tuple), tartomány (Range)
<!-- status: auto -->

Ennes (Tuple)
- Rögzített számú, tetszőleges kifejezésből álló, fix sorrendű kollekció“
- Példák:

```
iex> {0x1ff, :erlang, Armstrong, 'Joe'++[0], [], {}}
{511, :erlang, Armstrong, [74, 111, 101, 0], [], {}}
iex> {plus, per, sin} = # mintaillesztések kötésekkel
  {&Kernel.+/2, &//2, &:math.sin/1}
{&:erlang.+/2, &:erlang.//2, &:math.sin/1}
iex> {plus.(3,4), per.(3,4)} # infix volt, prefix lett
{7, 0.75}
iex> sin.(90*:math.pi/180)
1.0
```

Tartomány (Range)
- Egész számok sorozata a [start, end] tartományban
- Példa tartomány és lépésköz definiálására, használatára:

```
iex> {18..23, 18..10}
{18..23, 18..10//-1}
iex> for i <- 18..10 // -3, do: i
[18, 15, 12]
```

## s11 · p22-23 · Lista (List)
<!-- status: auto -->

- Korlátlan számú, tetszőleges kifejezésből álló, egyszeresen láncolt sorozat
- Lineáris rekurzív adatstruktúra:
  - vagy üres (`[]` jellel jelöljük),
  - vagy egy elemből áll, amelyet egy lista követ: `[x|xs]`
- Első eleme, ha van, a lista feje
- Első eleme utáni, esetleg üres része a lista farka

```
iex> [:elem] # egyelemű lista
[:elem]
iex> [:elem|[]] # fejből és üres farokból létrehozott lista
[:elem]
iex> [:elem1|[:elem2]] # fejből-farokból létrehozott lista
[:elem1, :elem2]
iex> [:elem,123,3.14,'elem'] # több elemű listák
[:elem, 123, 3.14, 'elem']
iex> [:elem,123|[3.14,'elem']]
[:elem, 123, 3.14, 'elem']
iex> [:egy|[:két]] ++ [:elem,123|[3.14,'elem']] # ++: konkatenáció
[:egy, :két, :elem, 123, 3.14, 'elem']
```

## s12 · p24 · Karakterlánc (single-quoted)
<!-- status: TODO view pages/p024.png -->
<!-- flags: math -->

- Rövidítés, karakterkódok listája: `'erl'` ≡`[?e,?r,?l]` ≡`[101,114,108]`
- Az Elixir/Erlang shell a nyomtatható karakterkódok (7..13, 27, 32..126) listáját karakterláncként írja ki
- Ha ezektől különböző érték is van a listában, listaként írja ki
- Példák:

```
iex> [101,114,108]
~c"erl"
iex> [31,101,114,108]
[31, 101, 114, 108]
iex> 'erl' ++ 'ang' # konkatenálható
~c"erlang"
```

- A karakterlánc NEM sztring!

## s13 · p25-30 · Sztring (String, double quoted)
<!-- status: auto -->

- UTF-8 kódolású karakterek ábrázolása bájtok sorozataként (bináris típus)
- Következmények:
  - Az UTF-8 kódolás miatt a sztring rövidebb lehet az őt ábrázoló binárisnál
  - A lista- és a sztringműveletek különbözőek
- Példák:

```
iex> dxdy = "δx/δy"
"δx/δy"
iex> {String.length(dxdy), byte_size(dxdy)}
{5, 7}
iex> {String.at(dxdy,0), String.codepoints(dxdy)}
{"δ", ["δ", "x", "/", "δ", "y"]}
iex> [dx, dy] = String.split(dxdy, "/")
["δx", "δy"]
iex> dx <> "/" <> dy # <>: konkatenálás
"δx/δy"
```

- Sztringműveletekről, a String modul függvényeiről hamarosan lesz szó

## s14 · p31-32 · Ami közös a karakterláncban és a sztringben
<!-- status: TODO view pages/p032.png -->
<!-- flags: layout -->

- UTF-8 kódolású karakterekből állnak
- pause Lehetnek bennük ún. escape-szekvenciák:
\a BEL (0x07) \b \e ESC (0x1b) \f \r CR (0x0d) \s

```
iex> name = "dávid" # Sztring
"dávid"
"Helló, Dávid!"
~c"Bubo"
"Helló, Bubo Réka!"
```

BS (0x08) \d DEL (0x7f) FF (0x0c) \n NL (0x0a) SP (0x20) \t TAB (0x09)

\v VT (0x0b) \uhhhh Unicode codepoint in hexadecimal \xhh single byte in hexadecimal
- Néhány karakter speciális jelentését az elé írt `\` megszünteti, pl. `\\`
- Megengedik az ún. interpolációt, azaz változó helyettesítését az értékével (`"...#{<expr>}..."`) sztringben, illetve karakterláncban:

```
iex> "Helló, #{String.capitalize name}!"
iex> bubo = 'Bubo' # Karakterlánc
iex> "Helló, #{List.to_string [bubo, ? , "Réka"]}!"
```

## s15 · p33-35 · Bináris (Binary)
<!-- status: auto -->

- A bináris típusba tartozó értékek bitsorozatok
- Egy bináris érték jelölése `<< kif, ...` `>>` alakú
- A legegyszerűbb `kif` a [0,255] tartományba eső egész szám
- A számokat bájtként tároljuk a binárisban

```
iex> b = << 1, 2, 3 >>
<<1, 2, 3>>
iex> {byte_size(b), bit_size b}
{3, 24}
```

- A tárolásra használt bitek száma megszabható

```
iex> b = << 1::size(2), 1::size(3) >> # 01 001
<<9::size(5)>> # = 9 (decimálisként)
iex> {byte_size(b), bit_size b}
{1, 5}
```

- Egész és lebegőpontos számok és más értékek is tárolhatók binárisan

```
iex> << <<1>> :: binary, <<2.5>> :: binary >>
<<1, 64, 4, 0, 0, 0, 0, 0, 0>>
```

- A bináris tárolás hasznos médiafájlok és UTF-8 karakterek tárolására, processzek közötti kommunikációban stb.

## s16 · p36-40 · Kulcs-érték lista (Keyword lists)
<!-- status: auto -->

- Egy kulcs-érték párt kételemű ennesként írhatunk le: `{:key, value}`, ahol a kulcs csak atom, az érték tetszőleges típusú lehet
- Gyakran van szükség ilyen listákra, ezért az Elixir többféle jelölést, rövidítést, bizonyos esetekben zárójelelhagyást is megenged
- Példák

```
iex> [{:név,"Szöszi"},{:szerelme,"jazz-zongorista"},{:város,"Prága"}]
[név: "Szöszi", szerelme: "jazz-zongorista", város: "Prága"]
iex> [név: "Szöszi", szerelme: "jazz-zongorista", város: "Prága"]
[név: "Szöszi", szerelme: "jazz-zongorista", "város: "Prága"]
iex> inspect név: "Szöszi", szerelme: "jazz-zongorista", város: "Prága"
"[név: \"Szöszi\", szerelme: \"jazz-zongorista\", város: \"Prága\"]"
iex> [:cseh_film, név: "Szöszi", város: "Prága", szerelme: "zongorista"]
[:cseh_film, {név: "Szöszi", város: "Prága", szerelme: "zongorista"}]
iex> {:cseh_film, név: "Szöszi", szerelme: "zongorista", város: "Prága"}
{:cseh_film, [név: "Szöszi", szerelme: "zongorista", város: "Prága"]}
```

- A kulcs-érték párokat leginkább függvényopciók megadására használjuk, pl. `limit: :infinity`, `charlists: :as_lists`

## s17 · p41-44 · Szótár (Map) 1
<!-- status: auto -->

- A szótár kulcs-érték párok rendezett kollekciója
- Jelölés (map literal): `%{ key1 => value1, key2 => value2, ...}`
- Ha a kulcs atom, alternatív jelölés: `%{atom1: value1, atom2: value2}`
- A kulcsok és az értékek típusa tetszőleges; lehet kifejezés is
- Egy szótáron belül a kulcsok különböző típusúak lehetnek
- Példák:

```
iex> states = %{"UA"=>"Ukraine", "SK"=>"Slovakia", "AT"=>"Austria"}
%{"AT" => "Austria", "SK" => "Slovakia", "UA" => "Ukraine"}
iex> msgs = %{{:error,:enoent} => :fatal, {:error,:busy} => :retry}
%{{:error, :busy} => :retry, {:error, :enoent} => :fatal}
iex> colors = %{:red=>0xff0000, :green=>0x00ff00, :blue=>0x0000ff}
%{green: 65280, red: 16711680, blue: 255}
iex> colors = %{red: 0xff0000, green: 0x00ff00, blue: 0x0000ff}
%{green: 65280, red: 16711680, blue: 255}
iex> mix = %{(&+/2).(3,2) => "három+kettő", fütty: "dal"<>"olka"}
%{5 => "három+kettő", :fütty => "dalolka"}
```

## s18 · p45-50 · Szótár (Map) 2
<!-- status: auto -->

- A szótár típust elsősorban asszociatív tömbként szokás használni
- Szótárból értéket a kulccsal lehet kinyerni szögletes zárójeles jelöléssel
- Ha a kulcs atom, a rövidebb pontos jelölés is használható
- Példák:

```
iex> states["UA"]
"Ukraine"
iex> states["HU"]
nil
iex> msgs[{:error, :busy}]
:retry
iex> colors[:green]
65280
iex> colors.red
16711680
iex> mix[(&Kernel.*/2).(1,5)]
"három+kettő"
iex> mix.fütty
"dalolka"
```

- További részletek a Map modul dokumentációjában

## s19 · p51-55 · Reguláris kifejezés (Regex) 1
<!-- status: auto -->

- Az Elixirben a reguláris kifejezés is önálló típus
- Jelölés: `~r{regexp}`^(2) vagy `~r{regexp}options`
- A reguláris kifejezés szintaxisa a PCRE^(3) szerinti.
- Példák:

```
iex> Regex.run ~r{[cdr]}, "madárcsicsergés"
["d"]
iex> Regex.scan ~r{[cdr]}, "madárcsicsergés"
[["d"], ["r"], ["c"], ["c"], ["r"]]
iex> Regex.split ~r{[cdr]}, "madárcsicsergés"
["ma", "á", "", "si", "se", "gés"]
iex> Regex.replace ~r{[cdr]}, "madárcsicsergés", "."
"ma.á..si.se.gés"
```

- További részletek a Regex modul dokumentációjában
2A `~r{...}` jelölés is egy szigil, azaz bűvös jelölés. A szigilekről részletek a Kernel dokumentációjában

találhatók.

3Perl Compatible Regular Expressions, <http://www.pcre.org>

Links: <http://www.pcre.org>

## s20 · p56-57 · Reguláris kifejezés (Regex) 2
<!-- status: TODO view pages/p057.png -->
<!-- flags: table -->

- A regexp után egy vagy több egykarakteres opció állhat
**Jel** **Jelentés**

Többsoros sztring első sorában kezdődjön az illesztés

f i

Az illesztés ne különböztesse meg a kis- és nagybetűket

m Többsoros sztring esetén a ^ és a $ az egyes sorok elejét és végét jelentse (a

\A és \z jelentése változatlanul a sztring eleje és vége)

s A . illeszkedjen az újsor-karakterekre is U Az egyébként mohó * és + módosítók legyenek lusták, azaz a minta a lehető

leghosszabb karaktersorozat helyett a lehető legrövidebbre illeszkedjen

u Engedje meg Unicode-specifikus minták, pl. \p használatát x Engedje meg a bővített mód használatát: ignorálja a szóköz-jellegű (ún.

whitespace) karaktereket és a kommenteket (a # jeltől a sor végéig)
- Példák:

```
iex> Regex.run ~r{cs.*s}, "Madarak Csicsergése"
["csergés"]
iex> Regex.run ~r{cs.*s}i, "Madarak Csicsergése"
["Csicsergés"]
iex> Regex.run ~r{cs.*s}iU, "Madarak Csicsergése"
["Csics"]
```

## s21 · p58 · Tartalom
<!-- status: auto -->
<!-- header: FPE-2 – Termek, azonosítók, változók -->

1 Típusok, termek, azonosítók, változók
- FPE-2 – Típusok: atom, szám, függvény, ennes, tartomány, lista
- FPE-2 – Termek, azonosítók, változók

## s22 · p59-61 · Term
<!-- status: auto -->
<!-- header: FPE-2 – Termek, azonosítók, változók -->

- A term tetszőleges adatstruktúra
- Minden termnek van értéke és típusa
- A term maga is kifejezés
- Közelítő rekurzív definíciója: Szám-, atom-, függvény- és más értékekből, ill. termekből konstruktorokkal felépített, tovább nem egyszerűsíthető kifejezés
- Példák
  - `kötött = 2021`
  - Term: tovább nem egyszerűsíthető, tömör, ha kiértékelhető, azaz nincs benne szabad változó

```
123456789
{'Diák Detti', [{:khf, [:prolog, :elixir, :prolog]}]}
[&:erlang.+/2, kötött, fn(x,y) -> x*y end]
```

  - Nem term (tovább egyszerűsíthető vagy nem tömör)

```
5+6                   # műveletet tartalmaz
(&:erlang.+/2).(5,6) # függvényalkalmazást tartalmaz
szabad                # szabad változó
```

## s23 · p62-63 · Azonosító (identifier)
<!-- status: auto -->
<!-- header: FPE-2 – Termek, azonosítók, változók -->

- Kisbetűvel vagy aláhúzásjellel (_) kezdődő, betűket, számjegyeket^(4) és aláhúzásjeleket tartalmazó, opcionálisan kérdő- vagy felkiáltójellel végződő karaktersorozat
- Konvenció szerint a ?-lel végződő azonosító kiértékelése igazságértéket ad eredményül, a !-lel végződő kiértékelése pedig kivételt dob, ha meghiúsul
- Konvenció szerint az azonosító részeit aláhúzásjellel tagoljuk (ún. megengedő snake_case), vö. atom szintaxisa
- Példák:

```
what_s_in_a_name   name?   exec!
_unused   rómeó_és_Júlia   year_2021
```

- Az azonosító változót vagy függvénynevet jelöl
4UTF-8 kódolású betű, ill. decimális számjegy; lásd <https://hexdocs.pm/elixir/unicode-syntax.html>

Links: <https://hexdocs.pm/elixir/unicode-syntax.html>

## s24 · p64-68 · Változó
<!-- status: auto -->
<!-- header: FPE-2 – Termek, azonosítók, változók -->

- Egy változó lehet szabad vagy kötött
- A szabad változónak nincs értéke, típusa
- A kötött változó valamely konkrét term szinonimája
- A változóhoz köthető új érték, de ez korábbi felhasználását nem módosítja
- A ^ (pin) operátor a kötött változó értékét fixálja: nem köthető új értékhez
- Példák

```
iex> x = fn(x) -> 2*x end # a külső és a belső x nem ugyanaz!
#Function<44.40011524/1 in :erl_eval.expr/5>
iex> y = x
#Function<44.40011524/1 in :erl_eval.expr/5>
iex> ^x = y.(2)
** (MatchError) no match of right hand side value: 4
iex> x = y.(2)
4
iex> y
#Function<44.40011524/1 in :erl_eval.expr/5>
```

## s25 · p69-73 · Változó hatásköre, komment, igazságérték
<!-- status: auto -->
<!-- header: FPE-2 – Termek, azonosítók, változók -->

- Változó hatásköre: lexikális
  - A függvény törzsében és fejében definiált változók (utóbbiak másnéven: formális paraméterek) lokálisak a függvényre nézve
  - Modulban is lehet változót definiálni, ami csak modulszinten látható, a modulban definiált függvényekből nem
  - `with` kifejezéssel is definiálhatunk lokális változót, például

```
iex> with a = 5, b = 7, do: a*a + 2*a*b + b*b
144
iex> a = 11; with a = 5, b = 7, do: a*a + 2*a*b + b*b; a
11
```

- Komment: # jellel keződik, a sor végéig tart
- Igazságérték, másnéven logikai érték (boolean)
  - Három atomot tekintünk igazságértéknek: `:true`, `:false`, `:nil`
  - Mindhárom írható kettőspont nélkül is: `true`, `false`, `nil`
  - A `false` és `nil` hamis, minden más érték (nemcsak a `true`) igaz
  - Angolul szokás megkülönböztetni a true-t a truthy-tól, a false-t a falsy-tól, pl. JavaScript, Java, Elixir.

## s26 · p74 · II. rész
<!-- status: auto -->

Műveletek listákon

1 Típusok, termek, azonosítók, változók

2 Műveletek listákon

3 Műveletek sztringeken

4 Problémamegoldási technikák

## s27 · p75 · Tartalom
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Műveletek listákon -->

2 Műveletek listákon
- FPE-2 – Műveletek listákon
- FPE-2 – Kis példák listák használatára

## s28 · p76-78 · Műveletek listákon 1
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Műveletek listákon -->

- A lista láncolt lineáris adatstruktúra, ezért olcsó az első elemét (a fejét) és az összes többi elemét (a farkát) megkapni, de drága az utolsó elemét elérni, mert végig kell gyalogolni a listán
- A funkcionális nyelvekben, a többi adatstruktúrával egyezően, a lista nem frissíthető, az Elixirben sem: amikor a lista egy elemét le akarjuk cserélni, akkor másolatot kell készítenünk a lecserélendő elem előtti részlistáról
- A másolás során a lecserélendő elem előtti összes elemet félre kell raknunk, majd a lecserélendő elem utáni megosztott farokrész elé be kell fűznünk az új elemet, ezt követően pedig a félrerakott elemeket egyesével be kell fűznünk az új elemet már tartalmazó listarész elé
- Vagyis a lista adott elemi utáni farkáról nem készül másolat, mert az Elixir megosztja a lista farkát a régi és az új elemet tartalmazó listák között
- A lista annyira megkerülhetetlen adatstruktúra a funkcionális nyelvekben, hogy már eddig is sok példát láttunk a használatára. A következő dián összefoglaljuk a leggyakoribb listaműveleteket
- A sztring ugyan nem listaként van ábrázolva az Elixirben, de a használata hasonló, ezért a leggyakoribb sztringműveleteket is összefoglaljuk később egy dián

## s29 · p79-83 · Műveletek listákon 2
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Műveletek listákon -->

- Lista feje, farka, hossza: `hd(xs)`, `tl(xs)`, `length(xs)`^(5)
- Két lista összefűzése (konkatenációja): `xs ++ ys`, eredménye `xs` összes eleme `ys` elé fűzve az eredeti sorrendben
- Két lista különbsége: `xs -- ys`, eredménye `xs` azon elemeinek listája az eredeti sorrendben, amelyek nincsenek benne `ys`-ben
- Tagsági vizsgálat: `x in xs` eredménye `true`, ha `x` eleme `xs`-nek
- Példák

```
iex> [:a, 'a', [65]] ++ [1+2, 2/1, 'a'] # 65 == ?A
[:a, 'a', 'A', 3, 2.0, 'a']
iex> Enum.to_list(1..100000) ++ [100001] # rossz hatékonyságú!
[1, 2, 3, 4, 5, 6, 7, 8, ...100001]
iex> [:a, 'a', [65], 'a'] -- ["A", 2/1, 'a']
[:a, 'A', 'a']
iex> [:a, 'a', [65], 'a'] -- ["A", 2/1, 'a', :a, :a, :a]
['A', 'a']
iex> [1, 2, 3] -- [1.0, 2] # szigorú egyenlőség: 1̸ ≡1.0
[1, 3]
iex> "A" in ["A", 2/1, 'a', :a, :a, :a]
true
```

5`hd/1`, `tl/1`, `length/1`, `++/2`, `--/2`, `in/2` a Kernel modulban vannak definiálva

## s30 · p84-86 · Műveletek listákon 3
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Műveletek listákon -->

- Lista első / utolsó eleme; ha nincs, `default` vagy `nil`:

```
first(list, default \\ nil), last(list, default \\ nil)
```

- Egy elem első előfordulásának törlésével kapott lista:

```
delete(list, elem)
```

- Adott pozíciójú elem törlésével / beszúrásával / cseréjével kapott lista:

```
delete_at(list, index), insert_at(list, index, value),
replace_at(list, index, value), update_at(list, index, fun)
```

Indexelés 0-tól, negatív index a lista végéről indul. `update_at/3` a `fun` függvényt alkalmazza az adott pozíciójú elemre.
- Lista kilapításával / kilapítása után a `tail` elé fűzésével kapott lista:

```
flatten(list), flatten(list, tail)
```

- Elem többszörözésével kapott lista: `duplicate(elem, n)`
- Listák listájából ennesek listája: `zip(list_of_lists)`
- Példák:

```
iex> List.zip([[:a, :b, :c], [:d, :e, :f, :g, :h], [:i, :j, :k, :l]])
[{:a, :d, :i}, {:b, :e, :j}, {:c, :f, :k}] # Listák vége levágva
iex> List.flatten(['abc', [['defgh']], ['ijkl']], 'zzz')
  'abcdefghijklzzz'
```

## s31 · p87-89 · Műveletek listákon 4
<!-- status: TODO view pages/p089.png -->
<!-- flags: layout -->
<!-- header: Műveletek listákon | FPE-2 – Műveletek listákon -->

- Konverziós függvények, pl. `List.to_string`, `Tuple.to_list`
- Van három tesztelő függvény is:
  - `improper?(list)` igaz, ha `list` nem valódi lista, azaz egy listakonstruktorban a farok nem lista, pl. `[1,2|3]`, `[:a,:b|nil]`
  - `starts_with?(list, prefix)` igaz, ha `list prefix`-szel kezdődik
  - `ascii_printable?(list, n \\ :infinity)` igaz, ha `list` első `n` karaktere 7-bites ASCII-kódolású és nyomtatható, beleértve a vezérlő karaktereket is (`\a`, `\b`, `\t`, `\n`, `\v`, `\f`, `\r`, `\e`)
Az `Enum` modul függvényei is alkalmazhatók listákra:
- Lista megfordításával / megfordítása után a `tail` elé fűzésével kapott lista: `reverse(list)`, `reverse(list, tail)`
- Lista adott indexű eleme, ha nincs ilyen, `default` vagy `nil`:

```
    at(list, index, default \\ nil)
iex> List.starts_with? 'almafa', [?a, ?l]   iex> Enum.reverse 'almafa'
true                                        'afamla'
                                            iex> Enum.at 'almafa', 2
                                            ?m
```

## s32 · p90-91 · Műveletek listákon 5
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Műveletek listákon -->

További függvények az `Enum` modulból:
- Lista legkisebb / legnagyobb eleme:

```
min(list, sorter \\ &<=/2,
          empty_fallback \\ fn -> raise(Enum.EmptyError) end)
```

`max/3` paraméterezése hasonló, `&<=/2` helyett `&>=/2`-vel. Ha `list` üres, a 3. paraméterként átadott függvény aktivizálódik.
- Lista `n` elemű eleje, `n` elem utáni farka: `take(list, n)`, `drop(list, n)` Ha `n` negatív, az elemeket a lista végéről kezdve emeli le / dobja el.
- Lista részlistája: `slice(list, range)` a `range` tartományba eső indexű elemek listája / `slice(list, start, n)` a `start` indextől kezdődő `n` elemű részlista. Ha `range`, ill. `start` negatív, indexelés a lista végéről.
Példák

```
iex> {(Enum.max 'mióta') === ?ó, (Enum.min [], fn -> 0 end)}
{true, 0}
iex> xs='indulakutyasatyukaludni'; {(Enum.take xs,-5), (Enum.drop xs,5)}
{'ludni', 'akutyasatyukaludni'}
iex> {(Enum.slice xs, 6..10), (Enum.slice xs, -10..-7)}
{'kutya', 'tyuk'}
```

## s33 · p92-94 · Műveletek listákon 6
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Műveletek listákon -->

És még néhány függvény az `Enum` modulból:
- Lista kettévágva: `split(list, n)` ugyanaz, csak rövidebben mint

```
{(take list, n), (drop list, n)}
```

- Lista rendezve alapértelmezés / `fun` függény szerint: `sort(list)`,

```
sort(list, fun)
```

- Lista többszörös értékek nélkül: `uniq(list)`
Példák

```
iex> xs='indulakutyasatyukaludni'; [(Enum.split xs,5),(Enum.split xs,-5)]
[{'indul', 'akutyasatyukaludni'}, {'indulakutyasatyuka', 'ludni'}]
iex> Enum.sort xs
'aaaaddiikkllnnsttuuuuyy'
iex> Enum.sort xs, &>=/2
'yyuuuuttsnnllkkiiddaaaa'
iex> Enum.uniq xs
'indulaktys'
```

Az `Enum` modul függvényei – mind mohó kiértékelésű – egyéb korlátos, felsorolható (enumerable) adatstruktúrákra is alkalmazhatók. Nem korlátos adatstruktúrákra a `Stream` modul függvényeit – ezek lusta kiértékelésűek – lehet használni

## s34 · p95 · Tartalom
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Kis példák listák használatára -->

2 Műveletek listákon
- FPE-2 – Műveletek listákon
- FPE-2 – Kis példák listák használatára

## s35 · p96 · Listakezelés – rövid példák 1
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Kis példák listák használatára -->

```
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

## s36 · p97 · Listakezelés – rövid példák 2
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Kis példák listák használatára -->

```
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
 ~c"W", ~c"X", ~c"Y", ~c"Z", ~c"[", ~c"\", ~c"]", ~c"^", ~c"_", ~c"`", ~c"a",
 ~c"b", ~c"c", ~c"d", ~c"e", ~c"f", ~c"g", ~c"h", ~c"i", ~c"j", ~c"k", ~c"l",
 ~c"m", ~c"n", ~c"o", ~c"p", ~c"q", ~c"r", ~c"s", ~c"t", ~c"u", ~c"v", ~c"w",
 ~c"x", ~c"y", ~c"z", ~c"{", ~c"|", ~c"}", ~c"~"]
 [~c" ", ~c"!", ~c"\"", ~c"#", ~c"$", ~c"%", ~c"&", ~c"'", ~c"(", ~c")", ~c"*",
  ~c"+", ~c",", ~c"-", ~c".", ~c"/", ~c"0", ~c"1", ~c"2", ~c"3", ~c"4", ~c"5",
  ~c"6", ~c"7", ~c"8", ~c"9", ~c":", ~c";", ~c"<", ~c"=", ~c">", ~c"?", ~c"@",
  ~c"A", ~c"B", ~c"C", ~c"D", ~c"E", ~c"F", ~c"G", ~c"H", ~c"I", ~c"J", ~c"K",
  ~c"L", ~c"M", ~c"N", ~c"O", ~c"P", ~c"Q", ...]
```

## s37 · p98-101 · Listakezelés – rövid példák 3
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Kis példák listák használatára -->

`fpea.ex` – Számlista összege @spec sum(xs::[integer]) :: s::integer

```
# Az xs számlista összege s
def sum([]), do: 0 # a ", do:" jelölés többsoros változata a "do ... end"
def sum(xs)  do x = hd xs; rs = tl xs; x + sum rs end # újsor helyett ;

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

## s38 · p102-103 · Listakezelés – rövid példák 4
<!-- status: auto -->
<!-- header: Műveletek listákon | FPE-2 – Kis példák listák használatára -->

`fpea.ex` – Két lista összefűzése @spec append(xs::[any], ys::[any]) :: rs::[any]

```
# rs az xs lista ys elé fűzésével kapott lista
def append([], ys), do: ys
def append(xs, ys), do: [(hd xs) | (append (tl xs), ys)]
@spec revapp(xs::[any], ys::[any]) :: rs::[any]
# rs a megfordított xs lista ys elé fűzésével kapott lista
def revapp([], ys), do: ys
def revapp(xs, ys), do: revapp (tl xs), [(hd xs) | ys]

iex(22)> c "fpea.ex"
[Fpea]
iex(23)> xs
[10, 20.5, 30.5]
iex(24)> Fpea.append(xs, [:a,:b,:c,:d])
[10, 20.5, 30.5, :a, :b, :c, :d]
iex(25)> Fpea.revapp xs, [:a,:b,:c,:d]
[30.5, 20.5, 10, :a, :b, :c, :d]
```

## s39 · p104 · III. rész
<!-- status: auto -->

Műveletek sztringeken

1 Típusok, termek, azonosítók, változók

2 Műveletek listákon

3 Műveletek sztringeken

4 Problémamegoldási technikák

## s40 · p105 · Tartalom
<!-- status: auto -->
<!-- header: Műveletek sztringeken | FPE-2 – Műveletek sztringeken -->

3 Műveletek sztringeken
- FPE-2 – Műveletek sztringeken

## s41 · p106-108 · Műveletek sztringeken 1
<!-- status: auto -->
<!-- header: Műveletek sztringeken | FPE-2 – Műveletek sztringeken -->

A sztringek nem listák az Elixirben – mégcsak nem is kollekciók –, de mivel kényelmes listaszerűen kezelni őket, a `String` modulban vannak ezt lehetővé tevő függvények. Két fogalmat kell megkülönböztetnünk: a kódpontot (code point) és a grafémát (grapheme cluster, röviden grapheme).
- A **kódpont** egyetlen Unicode karakter, egy vagy több bájt ábrázolja

```
iex> {byte_size("á"), String.length("á")}
{2, 1}
```

- A **graféma** egy vagy több kódpont, ami egyetlen karakternek látszik

```
iex> str = "\u0065\u0302"; {byte_size(str), String.length(str)}
{3, 1}
iex> "u\u0302"# U+0302 Combining Circumflex Accent
"ˆu"
iex> String.codepoints(str)
["e", "^"] # Két egykarakteres sztring van a listában.
iex> String.graphemes(str)
```

`["`ˆ`e"]` # Egyetlen egykarakteres sztring van a listában.

## s42 · p109-110 · Műveletek sztringeken 2
<!-- status: auto -->
<!-- header: Műveletek sztringeken | FPE-2 – Műveletek sztringeken -->

- `<>` a konkatenálás jele: `"ál"<>"om"`
- `string` első / utolsó grafémája, grafémáinak száma:

```
first(string), last(string), length(string)
```

- Graféma `string pos` pozíciójában: `at(string, pos)`
- Tartalmazza-e `string patts` legalább egy elemét:

```
contains?(string, patts)
```

- `string` elejéről / végéről / mindkettőről levágja a szóköz-jellegű (whitespace) UTF-8 karaktereket: `trim_leading(string)`,

```
trim_trailing(string), trim(string)
```

- Példák

```
iex> str = " "<>" "<>"kutyafüle"<>" "; String.at(str, 8)
"ü"
iex> String.contains?(str, "ü")
true
iex> String.contains?(str, ["ü","ty","n"])
true
iex> String.contains?(str, ["n"])
false
iex> {String.trim_leading(str), String.trim(str)}
{"kutyafüle ", "kutyafüle"}
```

## s43 · p111-112 · Műveletek sztringeken 3
<!-- status: auto -->
<!-- header: Műveletek sztringeken | FPE-2 – Műveletek sztringeken -->

- Mint a listánál, csak graféma-elemekkel: `slice(string, range)`,

```
slice(string, start, n), duplicate(string, n), reverse(string),
starts_with?(string, prefix)
```

- Sztring két darabra vágva adott pozícióban: `split_at(string, pos)`; több darabra szabdalva UTF-8 whitespace-ek mentén: `split(string)`
  - A vezető és záró UTF-8 whitespace-eket ignorálja
- Példák

```
iex> str = "indulakutyasatyukaludni"; String.reverse(str)
"indulakuytasaytukaludni"
iex> String.starts_with?(str, "indula")
true
iex> {String.slice(str, 6..10), String.slice(str, -10..-7)}
{"kutya", "tyuk"}
iex> String.duplicate("indul ", 3)
"indul indul indul "
iex> String.split_at(" "<>" "<>"kutya füle macska farka"<>" ", 12)
{"  kutya füle", " macska farka "} # párt ad eredményül
iex> String.split(" "<>" "<>"kutya füle macska farka"<>" ")
["kutya", "füle", "macska", "farka"] # listát ad eredményül
```

## s44 · p113 · IV. rész
<!-- status: auto -->

Problémamegoldási technikák

1 Típusok, termek, azonosítók, változók

2 Műveletek listákon

3 Műveletek sztringeken

4 Problémamegoldási technikák

## s45 · p114 · Tartalom
<!-- status: auto -->
<!-- header: Problémamegoldási technikák | FPE-2 – Fibonacci-számok rekurzióval és dinamikus programozással -->

4 Problémamegoldási technikák
- FPE-2 – Fibonacci-számok rekurzióval és dinamikus programozással

## s46 · p115 · (no title)
<!-- status: TODO view pages/p115.png -->
<!-- flags: graphic, image, no-text -->
<!-- figure: figures/p115-f1.png -->
<!-- header: Problémamegoldási technikák | FPE-2 – Fibonacci-számok rekurzióval és dinamikus programozással -->

## s47 · p116 · Dinamikus programozás: Fibonacci. Benchmarking és debugging
<!-- status: auto -->
<!-- header: Problémamegoldási technikák | FPE-2 – Fibonacci-számok rekurzióval és dinamikus programozással -->

A Fibonacci-számok kiszámítására hatféle algoritmust mutat be a második előadás segédanyaga:
- Elágazó rekurzióval
- Memoizálással (dinamikus programozás felülről lefelé haladva), Elixir Map-pel
- Táblázattal (dinamikus programozás alulról felfelé haladva), Elixir Map-pel
- Táblázattal (dinamikus programozás alulról felfelé haladva), Erlang :array-jel
- Táblázattal (dinamikus programozás alulról felfelé haladva), Elixir List-tel
- Az (n-2)-edik (prev) és az (n-1)-edik (curr) Fibonacci-szám nyilvántartásával
A második előadás segédanyaga a honlapról letölthető:
- <https://dp.iit.bme.hu/dp26a/ea/dp26a-fp2ea-fibonacci.livemd>
A segédanyag a `Benchee` és a `KinoExplorer` modulok használatára is mutat példákat.

Links: <https://dp.iit.bme.hu/dp26a/ea/dp26a-fp2ea-fibonacci.livemd>

## s48 · p117 · Fibonacci elágazó rekurzióval
<!-- status: TODO view pages/p117.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p117-f1.png -->
<!-- header: Problémamegoldási technikák | FPE-2 – Fibonacci-számok rekurzióval és dinamikus programozással -->

# O(2^n) futási idő, O(2^n) tárhely @spec fib(i :: integer()) :: n :: integer()

```
# n az i-edik Fibonacci-szám
def fib(0), do: 0
def fib(1), do: 1
def fib(i), do: fib(i-1) + fib(i-2)
```

## s49 · p118 · 2. gyakorlat
<!-- status: auto -->
<!-- header: Problémamegoldási technikák | FPE-2 – Fibonacci-számok rekurzióval és dinamikus programozással -->

- Ezen a héten a dékáni szünet miatt nem találkozunk a gyakorlaton
- **2026. szeptember 22.** 10:15 az IB027 és IE007 termekben
- Alapvetően *otthoni munka*, a gyakorlaton megbeszéljük a feladatok megoldásait
- Gyakorlat anyaga: <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp2gy.livemd>
- Felkészüléshez ajánlott: <https://dp.iit.bme.hu/dp26a/ea/dp26a-fp2ea-fibonacci.livemd>

Links: <https://dp.iit.bme.hu/dp26a/ea/dp26a-fp2ea-fibonacci.livemd>, <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp2gy.livemd>
