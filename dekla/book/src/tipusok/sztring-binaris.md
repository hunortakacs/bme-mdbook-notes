# Sztring és bináris

## Sztring (String, double quoted)

Az idézőjelek közé írt **sztring** UTF-8 kódolású karakterek ábrázolása bájtok sorozataként, azaz bináris típusú érték. Ennek két következménye van:

- az UTF-8 kódolás miatt a sztring (karakterekben mért) hossza kisebb lehet az őt ábrázoló bináris (bájtokban mért) hosszánál;
- a lista- és a sztringműveletek különbözőek.

```iex
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

A `δ` két bájton tárolódik, ezért az öt karakterből álló sztring hét bájt. A `String` modul függvényeit a [Műveletek sztringeken](../sztringek.md) fejezet tárgyalja.

## Ami közös a karakterláncban és a sztringben

A karakterlánc és a sztring is UTF-8 kódolású karakterekből áll, és mindkettőben lehetnek ún. **escape-szekvenciák**:

| | | | | | |
|---|---|---|---|---|---|
| `\a` | BEL (0x07) | `\b` | BS (0x08) | `\d` | DEL (0x7f) |
| `\e` | ESC (0x1b) | `\f` | FF (0x0c) | `\n` | NL (0x0a) |
| `\r` | CR (0x0d) | `\s` | SP (0x20) | `\t` | TAB (0x09) |
| `\v` | VT (0x0b) | `\uhhhh` | Unicode codepoint in hexadecimal | | |
| `\xhh` | single byte in hexadecimal | | | | |

Néhány karakter speciális jelentését az elé írt `\` megszünteti, pl. `\\` maga a visszaper-jel.

Mindkettő megengedi az ún. **interpolációt**, azaz egy kifejezés helyettesítését az értékével: `"...#{<expr>}..."`.

```iex
iex> name = "dávid" # Sztring
"dávid"
iex> "Helló, #{String.capitalize name}!"
"Helló, Dávid!"
iex> bubo = 'Bubo' # Karakterlánc
~c"Bubo"
iex> "Helló, #{List.to_string [bubo, ? , "Réka"]}!"
"Helló, Bubo Réka!"
```

Az utolsó példában a `? ` (kérdőjel és szóköz) a szóköz karakter kódja; a `List.to_string/1` a karakterláncból, a kódból és a sztringből álló listát egyetlen sztringgé alakítja.

## Bináris (Binary)

A **bináris** típusba tartozó értékek bitsorozatok. Egy bináris érték jelölése `<< kif, ... >>` alakú. A legegyszerűbb `kif` a [0,255] tartományba eső egész szám; a számokat bájtként tároljuk a binárisban:

```iex
iex> b = << 1, 2, 3 >>
<<1, 2, 3>>
iex> {byte_size(b), bit_size b}
{3, 24}
```

A tárolásra használt bitek száma a `::size(n)` módosítóval megszabható. Az alábbi példában az 1 két biten (`01`), a második 1 három biten (`001`) tárolódik, együtt az öt bites `01001`, ami decimálisan 9:

```iex
iex> b = << 1::size(2), 1::size(3) >> # 01 001
<<9::size(5)>> # = 9 (decimálisként)
iex> {byte_size(b), bit_size b}
{1, 5}
```

Egész és lebegőpontos számok és más értékek is tárolhatók binárisan. Itt a `<<2.5>>` a 2.5 lebegőpontos szám 64 bites ábrázolása:

```iex
iex> << <<1>> :: binary, <<2.5>> :: binary >>
<<1, 64, 4, 0, 0, 0, 0, 0, 0>>
```

A bináris tárolás hasznos médiafájlok és UTF-8 karakterek tárolására, processzek közötti kommunikációban stb.

<p class="sources">Forrás: dp26a-fp2ea.pdf (13–15. dia)</p>
