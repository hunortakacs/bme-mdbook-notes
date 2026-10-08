# Típusok

Az Elixir **erősen típusos** nyelv, **dinamikus típusellenőrzéssel**:

- erősen típusos: minden értéknek pontosan egy futásidejű típusa van;
- dinamikus típusellenőrzésű: a típusokat nem kötelező megadni a kódban, és egy változóhoz nem feltétlenül csak egy típus tartozik.

A fontosabb típusok (a felsorolás nem teljes; a dőlt betűs típusok más alaptípusokra épülnek):

| **Értéktípusok** | **Value types** |
|---|---|
| Atom | Atom |
| Tetszőleges hosszú egész szám | Arbitrary-sized integer (integer) |
| Lebegőpontos szám | Floating-point number (float) |
| Függvény | Function |
| *Tartomány* | *Range* |
| *Reguláris kifejezés* | *Regular expression (regex)* |
| *Sztring* | *String* |

| **Kollekció-típusok** | **Collection types** |
|---|---|
| Ennes | Tuple |
| Lista | List |
| Bináris | Binary |
| Szótár | Map |
| Struktúra | Struct |

A következő alfejezetek sorra veszik őket.

## Típusspecifikáció

Bár a típusokat nem kötelező megadni, dokumentációs céllal **típusspecifikáció** írható a függvényekhez a `@spec` attribútummal. Ez javítja a függvény dokumentáltságát és ezáltal az olvashatóságát, továbbá lehetővé teszi, hogy a *dialyzer* segédprogrammal ellenőrizzük a függvény típushelyességét (lásd [Projektek, mérés, típusellenőrzés](elixir/mix.md#típusellenőrzés-dialyzer)). Két példa:

- `@spec tl(xs :: [any()]) :: ts :: [any()] | nil`: „A `tl` függvény argumentuma egy `xs` tetszőleges elemű lista, visszatérési értéke (`ts`) egy szintén tetszőleges elemű lista vagy `nil`.”
- `@spec nth(xs :: [any()], n :: integer()) :: r :: any() | nil`: „Az `nth` függvény argumentumai egy `xs` tetszőleges elemű lista és egy `n` egész szám, visszatérési értéke (`r`) vagy egy tetszőleges típusú érték vagy `nil`.”

A paramétereknek és az eredménynek nevet is adhatunk (`xs ::`, `ts ::`); a `|` két típus unióját jelöli.

A specifikáció mellé a kurzus a `#`-tel kezdődő **deklaratív fejkommentet** is elvárja. A fejkomment a bemenő paraméter(ek) és a függvény visszatérési értéke közötti kapcsolatot fejezi ki deklaratív módon, azaz lehetőleg a *mi*-re, és nem a *hogyan*-ra ad választ. A specifikációban adott nevekre hivatkozik:

```elixir
defmodule App3 do
  @spec app(xs :: [integer()], ys :: [integer()]) :: zs :: [integer()]
  # xs és ys listák összefűzöttje zs
  def app([x|xs], ys), do: [x|app(xs, ys)]
  def app([], ys),     do: ys
end
```

<p class="sources">Forrás: dp26a-fp2ea.pdf (4. dia), dp26a-fp1ea.pdf (25. dia), dp26a-fp1gyfel.livemd</p>
