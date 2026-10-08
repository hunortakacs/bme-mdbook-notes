# Lista és karakterlánc

## Lista (List)

A **lista** korlátlan számú, tetszőleges kifejezésből álló, egyszeresen láncolt sorozat, a deklaratív nyelvek talán legalapvetőbb adatstruktúrája. Lineáris rekurzív adatstruktúra:

- vagy üres (jele `[]`),
- vagy egy elemből áll, amelyet egy lista követ: `[x|xs]`.

A lista első eleme, ha van, a lista **feje**; az első eleme utáni, esetleg üres része a lista **farka**. Mivel a lista láncolt, csak az első elemét érjük el közvetlenül; az utolsó és bármely közbülső elemét csak úgy, ha előbb az összes előtte álló elemet eltávolítjuk.

Ugyanaz a lista többféleképpen is leírható; a tömörebb változatok könnyebben írhatók és olvashatók. Az 1, 2, 3 egészekből álló lista például `[1|[2|[3|[]]]]`, `[1,2|[3]]` vagy `[1,2,3]`. A `|` előtt több elem is állhat, vesszővel elválasztva:

```iex
iex> [:elem] # egyelemű lista
[:elem]
iex> [:elem|[]] # fejből és üres farokból létrehozott lista
[:elem]
iex> [:elem1|[:elem2]] # fejből-farokból létrehozott lista
[:elem1, :elem2]
iex> [:elem,123,3.14,'elem'] # több elemű listák
[:elem, 123, 3.14, ~c"elem"]
iex> [:elem,123|[3.14,'elem']]
[:elem, 123, 3.14, ~c"elem"]
iex> [:egy|[:két]] ++ [:elem,123|[3.14,'elem']] # ++: konkatenáció
[:egy, :két, :elem, 123, 3.14, ~c"elem"]
```

A listaműveleteket a [Műveletek listákon](../listak.md) fejezet tárgyalja.

## Karakterlánc (single-quoted)

Az aposztrófok közé írt **karakterlánc** (karakterlista) rövidítés: karakterkódok listája.

`'erl'` ≡ `[?e,?r,?l]` ≡ `[101,114,108]`

Ugyanez a `~c` szigillel is írható: `~c"erl"`. A szigil speciális, „bűvös” jelölés az Elixirben. Az újabb Elixir-verziók a `'...'` jelölésre figyelmeztetnek, és a karakterlistát maguk is `~c"..."` alakban írják ki.

Az Elixir/Erlang-héj a nyomtatható karakterkódokból (7..13, 27, 32..126) álló listát karakterláncként írja ki. Ha ezektől különböző érték is van a listában, listaként, számokkal írja ki:

```iex
iex> [101,114,108]
~c"erl"
iex> [31,101,114,108]
[31, 101, 114, 108]
iex> 'erl' ++ 'ang' # konkatenálható
~c"erlang"
```

> [!IMPORTANT]
> A karakterlánc NEM sztring! A `'abc'` egy lista, a `"abc"` sztring (bináris); a lista- és a sztringműveletek különbözőek (lásd [Sztring és bináris](sztring-binaris.md)).

A kiírás tehát csak megjelenítés: a lista mindkét esetben számokból áll. Például a `[0 | ~c"abc"]` kifejezés eredménye `[0, 97, 98, 99]`, mert a 0 nem nyomtatható karakter kódja, ezért az egész lista számokként jelenik meg. Egy mintaillesztés után a farka, `~c"bc"`, már megint karakterláncként látszik:

```elixir
[_,_|xs] = [0 | ~c"abc"] |> IO.inspect
xs
```

```text
[0, 97, 98, 99]
~c"bc"
```

Az `Á` kódja 193, ami kívül esik a 32..126 tartományon, ezért a `~c"Ábc"` is számokkal jelenik meg (`[193, 98, 99]`), a farka (`~c"bc"`) viszont nem.

### A karakterlisták kiírása

Az `inspect` függvények kiírása a `charlists:` opcióval szabályozható: a `charlists: :as_lists` a lista elemeit számként, a `charlists: :as_charlists` karakterként jeleníti meg. Az alábbi példák az `App3.app/2` listaösszefűző függvényt használják ([Típusok](../tipusok.md#típusspecifikáció)):

```elixir
IO.inspect(App3.app([], []))
IO.inspect(App3.app([5, 6, 7], [1, 2, 3]))
IO.inspect(App3.app([7, 10, 12], [97, 98, 99])) # Ha kiírható a karakterkód, akkor úgy is látjuk
```

```text
[]
[5, 6, 7, 1, 2, 3]
~c"\a\n\fabc"
```

```elixir
IO.inspect(App3.app([7, 10, 12], [97, 98, 99]), charlists: :as_lists) # Ha számként szeretnénk látni
```

```text
[7, 10, 12, 97, 98, 99]
```

Az `IO.inspect/2` kiírja és változatlanul továbbadja az értéket, az `inspect/2` sztringgé alakítja, az `IO.puts/1` pedig a sztringet idézőjelek nélkül írja ki:

```elixir
App3.app([7, 10, 12], [97, 98, 99]) |> IO.inspect(charlists: :as_lists)
App3.app([7, 10, 12], [97, 98, 99]) |> inspect(charlists: :as_lists)
App3.app([7, 10, 12], [97, 98, 99]) |> inspect(charlists: :as_charlists)
App3.app([7, 10, 12], [97, 98, 99]) |> inspect(charlists: :as_charlists) |> IO.puts()
```

A négy kifejezés eredménye rendre a `[7, 10, 12, 97, 98, 99]` lista, a `"[7, 10, 12, 97, 98, 99]"` sztring, a `"~c\"\\a\\n\\fabc\""` sztring, végül az `IO.puts/1` kiírja a `~c"\a\n\fabc"` szöveget, és `:ok`-t ad vissza.

A 0..127 tartományba eső ASCII-kódú karakterek megjelenési formáját így nézhetjük meg:

```elixir
(for code <- 0..127, do: code) |> IO.inspect(charlists: :as_charlists)
[127] |> IO.inspect(charlists: :as_charlists)
```

```text
~c"\0\x01\x02\x03\x04\x05\x06\a\b\t\n\v\f\r\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\e\x1C\x1D\x1E\x1F !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\d"
~c"\d"
```

A 7..13, 27 és 32..126 tartományon kívül eső kódú karakterek hexadecimális kódjukkal (`\x01`) vagy saját escape-szekvenciájukkal (`\0`, `\d`) jelennek meg. A nyomtatható karakterek teljes listáját a [Műveletek listákon](../listak.md#rövid-példák) fejezet is bemutatja.

<p class="sources">Forrás: dp26a-fp2ea.pdf (11–12. dia), dp26a-fp1gyfel.livemd</p>
