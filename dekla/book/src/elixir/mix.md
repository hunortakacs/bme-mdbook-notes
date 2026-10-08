# Projektek, mérés, típusellenőrzés: mix, benchee, dialyzer

## Miért kell projektszervezés?

- Az Elixirhez sokféle modul van. A gyakran használtak (pl. `Kernel`, `Enum`, `List`, `String`) az Elixir-alapcsomag részei, a többit (pl. `Benchee`) utólag kell telepíteni, ha és amikor szükség van rájuk.
- Magának a fordítónak (`elixir`, `elixirc`, `iex`) is, a moduloknak is több verziója van, és az újabb verziók nem mindig kompatibilisek a korábbiakkal: a függőségeket kezelni kell.
- Egy saját projekt általában több modulból áll, plusz a teszteléshez használt adatokból és segédprogramokból; ezeket célszerű áttekinthetően, rendben tartani.
- Az Elixirhez kidolgozott segédeszközök csak akkor használhatók, ha betartjuk a konvenciókat, nemcsak a névadásra, hanem például a fájlokat tároló mappák szerkezetére vonatkozóakat is.

Elixir-projektek kezelésére készült a **`mix`**, amely az Elixir-csomag része (<https://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html>). A legfontosabb hívási formái a `mix --help` szerint:

```text
mix             - Invokes the default task (mix run) in a project
mix new PATH    - Creates a new Elixir project at the given path
mix help        - Lists all available tasks
mix help TASK   - Prints documentation for a given task
```

## Új projekt

Hozzunk létre egy `fp` nevű projektet egy új, ugyancsak `fp` nevű mappában! Az `fp/lib` mappában létrejön az `fp.ex` fájl, benne az `Fp` modul sablonjával; ez lenne a modul neve a `--module` opció nélkül is.

```console
# mix new fp --module Fp
* creating README.md
* creating .formatter.exs
* creating .gitignore
* creating mix.exs
* creating lib
* creating lib/fp.ex
* creating test
* creating test/test_helper.exs
* creating test/fp_test.exs

Your Mix project was created successfully.
You can use "mix" to compile it, test it, and more:
    cd fp
    mix test
Run "mix help" for more commands.

# ls -F fp
lib/  mix.exs  README.md  test/
```

A projekt leírása a `mix.exs` fájlban van, és ez – mi más is lehetne – Elixir-kód:

```elixir
defmodule Fp.MixProject do
  use Mix.Project
  def project do
    [
      app: :fp,
      version: "0.1.0",
      elixir: "~> 1.18",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end
  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:logger]
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  defp deps do
   [
    # {:dep_from_hexpm, "~> 0.3.0"},
    # {:dep_from_git, git: "https://github.com/elixir-lang/my_dep.git", tag: ...}
   ]
  end
end
```

A `mix.exs` két publikus (`def`) és egy privát (`defp`) függvényt definiál. A `project` a projekt konfigurációjáról tárol adatokat, az `application`-nel egy applikációs fájlt lehet generálni; ezek részleteibe nem megyünk bele. A `deps` privát függvény törzsében kell leírni a **függőségeket**: a kívánt modulok nevét és paramétereit.

## Függőség felvétele: benchee

Új függőségként a `Benchee` modult vesszük fel, amely – ahogy a neve is sugallja – benchmarkingra, futási idők mérésére használható (<https://github.com/bencheeorg/benchee>). A `mix.exs` vége ezzel így néz ki:

```elixir
 # Run "mix help deps" to learn about dependencies.
 defp deps do
  [
   {:benchee, "~> 1.0", only: :dev},
   # {:dep_from_hexpm, "~> 0.3.0"},
   # {:dep_from_git, git: "https://github.com/elixir-lang/my_dep.git", tag: ...}
  ]
 end
```

Ezután letöltjük és lefordítjuk az új modult és a függőségeit. Az új modulok az adott projekt részei lesznek: lokálisak, nem globálisak.

```console
~/tmp/fp$ mix do deps.get + deps.compile
Resolving Hex dependencies...
Resolution completed in 0.051s
New:
  benchee 1.4.0
  deep_merge 1.0.0
  statistex 1.1.0
...
Compiling ...
```

## Fordítás és futtatás mix-szel

Tegyük a `lib/sum.ex` fájlba egy egészlista összegét kiszámoló függvény három változatát (a különbségüket a [Rekurzió](../rekurzio.md#klózsorrend-és-hatékonyság) fejezet tárgyalja):

```elixir
defmodule Sum do
  def sum1([]), do: 0
  def sum1([x|xs]), do: x + sum1(xs)

  def sum2([x|xs]), do: x + sum2(xs)
  def sum2([]), do: 0

  def sum3(xs), do: sumi(xs, 0)

  defp sumi([x|xs], sum), do: sumi(xs, sum+x)
  defp sumi([], sum), do: sum
end

# A fájl végére írt kifejezéseket az iex automatikusan ki fogja értékelni
1..1000 |> Range.to_list() |> Sum.sum1() |> IO.inspect()
1..1000 |> Range.to_list() |> Sum.sum2() |> IO.inspect()
1..1000 |> Range.to_list() |> Sum.sum3() |> IO.inspect()
```

- Fordítani a `mix compile`-lal lehet. A lefordított fájl a `_build/dev/lib/fp/ebin/` mappába kerül, a `sum.ex` esetében `Elixir.Sum.beam` néven.
- Az `iex`-et a `mix`-projekt konfigurációjával és függőségeivel így indítjuk (lásd `mix help`, `elixir --help`):

  ```console
  iex -S mix # Starts IEx and runs the default task
  ```

- A programot az `r` paranccsal (pontosabban az `r` segédfüggvénnyel) lehet betölteni, újratölteni:

  ```iex
  iex> r Sum
  ```

- A `Sum` modulban definiált függvények ezután hívhatók:

  ```iex
  iex> Sum.sum1 [1,2,3,4,5]
  15
  ```

A modult záró `end` után álló függvényhívásokat az `iex` betöltéskor kiértékeli; az `IO.inspect` ezek eredményét ki is írja. Ha újratöltjük a programot az `r` segédfüggvénnyel, az eredmény megjelenik a képernyőn:

```iex
iex> r Sum
...
500500
{:reloaded, [Sum]}
```

## Mérés és profilozás: benchee

A méréshez a `Benchee.run/1` függvényt kell meghívni egy fájlban, például a `benchee_sum.exs`-ben. A paramétere egy szótár: a kulcsok a mérések nevei, az értékek névtelen függvények, amelyek törzsében a mérendő hívás áll.

```elixir
Benchee.run(%{"sum1" => fn -> 1..10_000 |> Enum.to_list() |> Sum.sum1() end,
              ...
              }
           )
```

Az elemzést a `mix run lib/benchee_sum.exs` paranccsal indítjuk. Ha azt is tudni szeretnénk, hogy a függvényeink által meghívott függvények milyen gyakran és mennyi ideig futnak, a `profile_after` opciót is meg kell adni:

```elixir
Benchee.run(%{"sum1" => fn -> 1..10_000 |> Enum.to_list() |> Sum.sum1() end,
              ...
             },
             profile_after: true
           )
```

A Benchee először kiírja a gép és a futtatás adatait (operációs rendszer, processzor, Elixir- és Erlang-verzió, a bemelegítés és a mérés ideje), majd egy táblázatot. Az `ips` a másodpercenkénti végrehajtások száma (*iterations per second*, `K` = ezer), az `average`, a `median` és a `99th %` a futási idő átlaga, mediánja és 99. percentilise, a `deviation` a szórás az átlag százalékában. A `Comparison` rész a leggyorsabbhoz viszonyítja a többit (`1.83x slower +51.30 µs`). A három `sum` változat eredményei a [Rekurzió](../rekurzio.md#klózsorrend-és-hatékonyság) fejezetben láthatók.

Livebookban a függőségeket a notebook első cellájában a `Mix.install/1` tölti be, például `Mix.install([{:benchee, "~> 1.3"}])`. Livebook-cellából futtatott mérésnél a Benchee figyelmeztet, hogy a mért függvények kiértékelt (*evaluated*) és nem lefordított függvények, ezért lassabbak; pontosabb méréshez a hívást modulbeli függvénybe vagy `mix run`-nal futtatott `.exs` fájlba érdemes tenni.

## Típusellenőrzés: dialyzer

A **dialyzer** az Erlang/Elixir programok statikus elemzője: a lefordított kódból kikövetkezteti a függvények típusát (*success typing*), és összeveti a típusspecifikációkkal (`@spec`, lásd [Típusok](../tipusok.md#típusspecifikáció)). Jelzi például, ha egy specifikáció nem felel meg a függvénynek. Elixir-projektben a `dialyxir` modullal használjuk, amelyet a `benchee`-hez hasonlóan a függőségek közé kell felvenni:

```elixir
 # Run "mix help deps" to learn about dependencies.
 defp deps do
  [
   {:dialyxir, "~> 1.4", only: [:dev, :test], runtime: false},
   # {:dep_from_hexpm, "~> 0.3.0"},
   # {:dep_from_git, git: "https://github.com/elixir-lang/my_dep.git", tag: ...}
  ]
 end
```

```console
~/tmp/fp$ mix do deps.get, deps.compile
Resolving Hex dependencies...
Resolution completed in 0.051s
New:
  dialyxir 1.4.6
  erlex 0.2.7
...
Compiling ...
```

A projekt forrásfájljainak a `lib` mappában kell lenniük. Rakjunk ide egy Elixir-programot, például az egyik kisházit, rontsunk el egy-két specifikációt, és dializáljuk!

- A dializálás a `lib` mappában lévő **összes** `.ex` fájlt vizsgálja.
- Az első futtatás sokáig tart, mert a dialyzer rengeteg ún. PLT-fájlt (*Persistent Lookup Table*) telepít a modulokhoz tartozó típusszignatúrákkal.
- A dializálás a `.beam` fájlokat elemzi, ezért ha valamelyik forrásfájl megváltozott, az elemzés előtt lefordítja.

Az alábbi `sum/1` specifikációja szerint a függvény egészlistát adna vissza, pedig egy számot ad. A dialyzer ezt `invalid_contract` hibaként jelzi, és megmutatja a kikövetkeztetett típust (*success typing*) a specifikáció mellett:

```elixir
@spec sum(xs::[integer()]) :: s::[integer()]
# Az xs számlista összege s
def sum([x|xs]), do: x + sum(xs)
def sum([]), do: 0
```

```console
~/tmp/fp$ mix dialyzer
lib/sum.ex:2:invalid_contract
The @spec for the function does not match the success typing ...
Function: Sum.sum/1
Success typing: ([number()]) -> number()
But the spec is: (xs::[integer()]) -> s::[integer()]
```

A dialyzert Livebook-cellában nem lehet futtatni, mert a dialyzer a lefordított BEAM-kódot elemzi, a Livebook pedig nem menti el a BEAM-kódot a háttértárba. Ezért hozzunk létre egy `mix`-projektet, másoljuk ki az elemzendő programrészeket a Livebook-cellá(k)ból, és mentsük el a projekt `lib` mappájába egy `.ex` kiterjesztésű fájlba. Ezután, a `dialyxir` függőség letöltése és a modulok lefordítása után, futtatható a `mix dialyzer` (lásd még <https://hexdocs.pm/dialyxir/readme.html>). A `mix` parancssoros használatához az Elixirt telepíteni kell a saját gépre, vagy Dockerből kell tudni futtatni.

<p class="sources">Forrás: dp26a-fp1ea.pdf (41–49. dia), dp26a-fp3ea.pdf (29–30. dia), dp26a-fp1ea-sum-benchee.livemd, dp26a-fp3gy.livemd, dp26a-fp2gy-megoldasok.livemd</p>
