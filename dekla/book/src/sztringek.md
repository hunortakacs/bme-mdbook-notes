# Műveletek sztringeken

A sztringek nem listák az Elixirben – még csak nem is kollekciók –, de mivel kényelmes listaszerűen kezelni őket, a `String` modulban vannak ezt lehetővé tevő függvények.

## Kódpont és graféma

Két fogalmat kell megkülönböztetnünk:

- A **kódpont** (*code point*) egyetlen Unicode-karakter, amelyet egy vagy több bájt ábrázol.

  ```iex
  iex> {byte_size("á"), String.length("á")}
  {2, 1}
  ```

- A **graféma** (*grapheme cluster*, röviden *grapheme*) egy vagy több kódpont, amely egyetlen karakternek látszik. Az alábbi `str` két kódpontból áll: az `e` betűből és az utána álló, az előző betűre ráíródó kalapból (U+0302, *Combining Circumflex Accent*); együtt egyetlen grafémát, az `ê`-t alkotják.

  ```iex
  iex> str = "\u0065\u0302"; {byte_size(str), String.length(str)}
  {3, 1}
  iex> "u\u0302"# U+0302 Combining Circumflex Accent
  "û"
  iex> String.codepoints(str)
  ["e", "̂"] # Két egykarakteres sztring van a listában.
  iex> String.graphemes(str)
  ["ê"] # Egyetlen egykarakteres sztring van a listában.
  ```

A `String.length/1` a grafémákat számolja, a `byte_size/1` a bájtokat.

## A `String` modul függvényei

- `<>` a konkatenálás jele: `"ál"<>"om"`.
- `string` első / utolsó grafémája, grafémáinak száma: `first(string)`, `last(string)`, `length(string)`.
- Graféma a `string` `pos` pozíciójában: `at(string, pos)`.
- Tartalmazza-e `string` a `patts` legalább egy elemét: `contains?(string, patts)`.
- `string` elejéről / végéről / mindkettőről levágja a szóköz-jellegű (*whitespace*) UTF-8 karaktereket: `trim_leading(string)`, `trim_trailing(string)`, `trim(string)`.

```iex
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

Mint a listánál, csak graféma-elemekkel: `slice(string, range)`, `slice(string, start, n)`, `duplicate(string, n)`, `reverse(string)`, `starts_with?(string, prefix)`.

A sztring két darabra vágva adott pozícióban: `split_at(string, pos)` (párt ad eredményül); több darabra szabdalva az UTF-8 whitespace-ek mentén: `split(string)` (listát ad eredményül). A `split/1` a vezető és záró UTF-8 whitespace-eket figyelmen kívül hagyja.

```iex
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

<p class="sources">Forrás: dp26a-fp2ea.pdf (41–43. dia)</p>
