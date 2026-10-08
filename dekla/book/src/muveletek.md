# Műveletek és beépített függvények

## Aritmetikai és bitműveletek

Aritmetikai műveletek (a `Kernel` modulban), a precedencia szerint csoportosítva (kisebb szám: erősebb kötés):

- előjel: `+`, `-` (precedencia: 1);
- multiplikatív műveletek: `*`, `/`, `div`, `rem` (precedencia: 2);
- additív műveletek: `+`, `-` (precedencia: 3).

Bitműveletek (a `Bitwise` modulban):

- `bnot` vagy `~~~`, `band` vagy `&&&` (precedencia: 2);
- `bor` vagy `|||`, `bxor`, `bsl` vagy `<<<`, `bsr` vagy `>>>` (precedencia: 3).

Szabályok:

- `+`, `-`, `*` és `/` egész és lebegőpontos operandusokra is alkalmazhatók;
- `+`, `-` és `*` eredménye egész, ha mindkét operandusuk egész, egyébként lebegőpontos;
- `/` eredménye mindig lebegőpontos;
- `div` (egészosztás) és `rem` (maradék) prefix helyzetűek, például `div(7, 2)`; eredményük egész;
- `div`, `rem` és a bitműveletek operandusai csak egészek lehetnek;
- `~~~`, `&&&`, `|||`, `<<<`, `>>>` infix, a többi bitművelet prefix helyzetű.

A bitműveleteket használat előtt importálni kell:

```elixir
import Bitwise
```

Ekkor például `5 &&& 3` értéke `1`, `bnot(5)` értéke `-6`, `1 <<< 4` értéke `16`. A régebbi anyagokban szereplő `use Bitwise[, (only_operators | skip_operators): true]` alak az újabb Elixir-verziókban elavult, figyelmeztetést ad.

## Összehasonlító műveletek (relációk)

Egy reláció (összehasonlítás) eredménye a `true` vagy a `false` atom.

- Kisebb, kisebb-egyenlő, nagyobb-egyenlő, nagyobb: `<`, `<=`, `>=`, `>`.
- *Érték szerinti* egyenlőség (`integer` és `float` lehet egyenlő): `==`, `!=`.
- *Szigorú egyenlőség* (`integer` és `float` nem lehet egyenlő): `===`, `!==`.

Például `5.0 == 5` értéke `true`, `5.0 === 5` értéke `false`.

Különböző típusú termek is összehasonlíthatók. A típusok sorrendje (vö. [Típusok](tipusok.md)):

```text
number < atom < reference < function < port < pid < tuple < map < list < binary
```

### Lebegőpontos értékek összehasonlítása

Elrettentő példák: a lebegőpontos számok kettes számrendszerben csak közelítőleg ábrázolhatók, ezért az egyenlőségvizsgálat meglepő eredményt adhat.

```iex
iex> 10.1 - 9.9 == 0.2
false
iex> (10.1 - 9.9) * 10
1.999999999999993
iex> 0.000000000000001 + 1 == 1
false
iex> 0.0000000000000001 + 1 == 1
true
```

> [!WARNING]
> Lebegőpontos értékek egyenlőségének vizsgálata helyett vizsgáljuk a különbségüket a `<=` vagy `>=` relációval: ε-nál kisebb-e a különbségük?

## Logikai műveletek

- Prefix helyzetű operátor: `not` és `!`. A `not` operandusa csak `boolean` lehet, a `!`-é tetszőleges típusú kifejezés.
- Infix helyzetű operátorok: `and` és `&&`, `or` és `||`.
  - `not`, `and` és `or` használható őrkifejezésben (lásd [Mintaillesztés](mintaillesztes.md#őr)), `!`, `&&` és `||` nem.
  - `and` és `or` első operandusa csak `boolean` lehet, `&&` és `||` első operandusa tetszőleges típusú kifejezés.
  - A `false` és `nil` értékű kifejezéseket kivéve *minden más* érték `true`-nak számít.
  - A második operandusuk tetszőleges típusú kifejezés lehet.
  - Eredményük típusa a két operandus típusának uniója.
  - Lusta kiértékelésű, ún. *short-circuit* műveletek: ha az első operandus kiértékelése eldönti az eredményt, a másodikra nem kerül sor.

```iex
iex> !:atom && div(3,0) === 2
false
iex> :atom && div(3,0) === 2
** ...bad argument in ...: div(3, 0)
iex> :atom and rem(3,2) === 1
** ...expected a boolean on left-side of "and"
iex> true and rem(3,2)
1
iex> false and rem(3,2)
false
iex> nil && rem(3,2)
nil
```

Az első példában a `!:atom` értéke `false`, ezért a `&&` a második operandust, a nullával való osztást ki sem értékeli. A másodikban `:atom` igaznak számít, így az osztásra sor kerül, és hibát ad. A harmadikban az `and` első operandusa nem `boolean`, ez hiba. A `true and rem(3,2)` eredménye a második operandus értéke, `1`, tehát nem feltétlenül `boolean`.

## Beépített függvények (Built-In Functions, BIFs)

A **BIF**-ek a BEAM-be beépített, rendszerint C-ben írt függvények. Többségük az *erts* Erlang-könyvtár `erlang` moduljának része; az Elixir-specifikációjuk az Elixir `Kernel` moduljában található. A csak az Erlang `erlang` moduljában definiált BIF-ek az `:erlang` modulnévvel hívhatók.

Az alaptípusokon alkalmazható leggyakoribb BIF-ek:

- Számok: `abs(num)`, `trunc(num)`, `ceil(num)`, `floor(num)`, `round(num)`, `:erlang.float(num)`. Az `:erlang.float` helyett 1-gyel is oszthatjuk az egész számot, pl. `5/1`.
- Sztring, bináris: `bit_size(string)`, `byte_size(string)`.
- Szótár: `map_size(map)`.
- Ennes: `tuple_size(tuple)`, `elem(tuple, index)`, `put_elem(tuple, index, value)`, ahol `0` ≤ `index` ≤ `tuple_size(tuple)-1`.
- Lista: `length(list)`, `hd(list)`, `tl(list)`.

Az operátorok is BIF-ek a `Kernel`-ben, például `Kernel.*(3,4)`.

## Típusvizsgálat és típuskonverzió

Típusvizsgálat (BIF-ek a `Kernel`-ben):

- `is_integer(term)`, `is_float(term)`, `is_number(term)`,
- `is_atom(term)`, `is_boolean(term)`, `is_nil(term)`,
- `is_binary(term)`, `is_bitstring(term)`,
- `is_tuple(term)`, `is_list(term)`, `is_map(term)`,
- `is_function(term)`, `is_function(term, arity)`.

Típuskonverzió (az egyes típusokhoz tartozó modulokban, pl. `Atom.to_string/1`):

- Atom: `to_charlist(atom)`, `to_string(atom)`;
- Float: `to_charlist(float)`, `to_string(float)`;
- Integer: `to_charlist(integer)`, `to_string(integer)`;
- List: `to_atom(list)`, `to_charlist(list)`, `to_float(list)`, `to_integer(list)`, `to_integer(list, base)`, `to_string(list)`, `to_tuple(list)`;
- String: `to_atom(string)`, `to_charlist(string)`, `to_float(string)`, `to_integer(string)`, `to_integer(string, base)`;
- Tuple: `to_list(tuple)`;
- Map: `to_list(map)`.

<p class="sources">Forrás: dp26a-fp3ea.pdf (17–21. dia)</p>
