# Interaktív használat: IEx és Livebook

## Az IEx

Az Elixir interaktív héja, az `iex` egy REPL (*read-eval-print loop*): beolvas egy kifejezést, kiértékeli, és kiírja az értékét. A promptban zárójelben a kifejezés sorszáma áll.

```iex
$ iex
Erlang/OTP ...
Interactive Elixir ...
  press Ctrl+C to exit
  (type h() ENTER for help)
iex(1)> 3.2 + 2.1 * 2
7.4
iex(2)> :atom
:atom
iex(3)> Atom
Atom
iex(4)> "string"
"string"
iex(5)> {:ennes,:%,A,:':',9.8}
{:ennes, :%, A, :":", 9.8}
iex(6)> [:lista,:%,A,:':',9.8]
[:lista, :%, A, :":", 9.8]
iex(7)> i :':'
...Data type
    Atom...
```

Az `i` segédfüggvény információt ír ki a kapott termről, például a típusát.

Az IEx-ből a **Ctrl+C** lenyomásával léphetünk ki. Ekkor a BEAM megszakítási menüje jelenik meg; egy újabb Ctrl+C kilép a héjból:

```text
iex(8)> Ctrl+C
BREAK: (a)bort (A)bort with dump (c)ontinue
   (p)roc info (i)nfo (l)oaded (v)ersion
   (k)ill (D)b-tables (d)istribution
Ctrl+C
$
```

A **Ctrl+G** a felhasználói parancsmódot (*User switch command*) nyitja meg; a `h` kiírja a parancsait, a `q` kilép:

```text
iex(8)> Ctrl+G
User switch command
--> h
  c [nn]            - connect to job
  i [nn]            - interrupt job
  k [nn]            - kill job
  j                 - list all jobs
  s [shell]         - start local shell
  r [node [shell]]  - start remote shell
  q                 - quit erlang
  ? | h             - this message
  --> q
$
```

### IEx-parancsok

Az IEx segédfüggvényeit (*helpers*) a `h()` listázza:

```iex
iex(1)> h().
Welcome to Interactive Elixir.
...
c/1            - compiles a file
c/2            - compiles a file and writes bytecode to the given path
cd/1           - changes the current directory
clear/0        - clears the screen
exports/1      - shows all exports (functions + macros) in a module
h/1            - prints help for the given module, function or macro
i/0            - prints information about the last value
i/1            - prints information about the given term
ls/0           - lists the contents of the current directory
ls/1           - lists the contents of the specified directory
pwd/0          - prints the current working directory
r/1            - recompiles the given module's source file
v/0            - retrieves the last value from the history
v/1            - retrieves the nth value from the history
...
To learn more about IEx as a whole, type h(IEx).
```

Az IEx-ben érdemes kipróbálni a `Kernel` Elixir-modul és a `:math` Erlang-könyvtár ismert függvényeit, és figyelni a tabulátorral kérhető szövegkiegészítést (*completion*).

## Saját program fordítása, futtatása

Függvényt csak modulban lehet definiálni. Az alábbi `fpea.ex` fájl az `Fpea` modulban definiálja a faktoriális függvényt. A fájlnév konvenció szerint csupa kisbetűs, a szavak között aláhúzással (*snake_case*); a modulnév egybeírt, a szavak nagy kezdőbetűvel (*BumpyCase*, *CamelCase*).

```elixir
defmodule Fpea do
# Fájlnév csupa kisbetűvel, szavak között aláhúzás (snake_case)
# Modulnév egybe, szavak nagy kezdőbetűvel (BumpyCase, CamelCase)
  @spec fac(n::integer) :: f::integer # Típusspecifikáció
  # f = n! (azaz f az n faktoriálisa) # Fejkomment
  def fac(0), do: 1            # ha az n=0 mintaillesztés sikeres
  def fac(n), do: n * fac(n-1) # ha az n=0 mintaillesztés sikertelen
end
```

A fájlt az IEx-ben a `c` paranccsal fordítjuk le; a függvényt a modulnévvel minősítve hívjuk:

```iex
iex(1)> c "fpea.ex"  # fordítás
[Fpea]
iex(2)> Fpea.fac(5)  # futtatás
120
iex(3)> fac(5)         # a modulnevet ki kell írni
** (CompileError) iex:3: undefined function fac/1
iex(4)> Fpea.fac 5   # argumentum körül a zárójel sokszor elhagyható
120
```

Egy már betöltött modul exportált függvényeit az `exports Fpea` írja ki (itt `fac/1`), a módosított forrásfájlt pedig az `r Fpea` fordítja újra.

### Modulok és függvények azonosítása

Az Elixirben egy függvényt három dolog azonosít: a **neve**, az **aritása** (a paramétereinek száma) és annak a **modulnak** a neve, amelyben definiálva van. Például a `String.slice/2` és a `String.slice/3` a `String` modul két azonos nevű függvénye: az egyiknek két, a másiknak három paramétere van. Ha ugyanabban a modulban hivatkozunk egy függvényre, amelyben definiálva van, a modulnév elmaradhat.

A `def` exportált (a modulon kívülről is hívható), a `defp` privát függvényt definiál:

```elixir
defmodule Dummy do

  def dummy0, do: 2024             # exportált, paraméter nélkül

  def dummy1(p), do: dummy2(p)     # exportált fv.

  defp dummy2(p), do: IO.puts (p)  # privát fv.

end

Dummy.dummy0

Dummy.dummy0 |> IO.inspect()

Dummy.dummy1('karakterlánc')    # karakterkódokból álló lácolt lista, nem sztring!

Dummy.dummy1(~c"karakterlista") # a ~c egy ún. szigil, speciális jelölés az Elixirben

Dummy.dummy1("sztring")

# Dummy.dummy2("sztring")
```

Az `IO.puts/1` mindhárom paramétert szövegként írja ki (`karakterlánc`, `karakterlista`, `sztring`). A kikommentezett `Dummy.dummy2("sztring")` hívás `UndefinedFunctionError` hibát adna, mert a privát függvény a modulon kívülről nem látszik. Modulon kívül függvény nem definiálható: a `def dummy, do: "halihó"` önmagában a `cannot invoke def/2 outside module` hibát adja.

## Livebook

A Livebook az Elixir notebookja, a Python Jupyteréhez hasonló. A gyakorlatok feladatsorai Livebook-formátumban (`.livemd`) jelennek meg. Az IEx-szel szemben a Livebookban modul is definiálható egy cellában.

A Livebook Elixir-cellái különálló modulokként fordulnak le. Ha egy cellában egy modulnak nevet adtunk, ugyanazt a nevet egy másik cellában már nem használhatjuk: ha az azonos nevű modult tartalmazó második cellát is kiértékeljük, az Elixir hibát jelez. Ennek előnye, hogy a korábbi cellákban definiált függvényeket a modulnév megadásával a későbbi cellákból is hívhatjuk.

## Kiírás: `IO.inspect`, `inspect`, `IO.puts`

Egy kifejezéssorozat kiértékelésekor az Elixir (a Livebook is) csak az utolsó kifejezés értékét írja ki. A korábbi kifejezések értékét az `IO.inspect/1`-gyel íratjuk ki:

```elixir
[1|[2|[3|[]]]] |> IO.inspect()
[1,2|[3]] # |> IO.inspect()
[1,2,3]
```

Az alábbi cellában az első kifejezés értékével nem kezdünk semmit, ezért nem is jelenik meg sehol; csak a második, utolsó kifejezés értéke (`[1, 2, 3]`) látszik:

```elixir
App3.app([], [])        # E kifejezés értékével nem kezdünk semmit, nem is jelenik meg sehol.
App3.app([], [1, 2, 3])
```

Az `IO.inspect/1`-gyel mindkettő kiíratható (az `App3.app/2` két listát fűz össze, lásd [Típusok](../tipusok.md#típusspecifikáció)):

```elixir
IO.inspect(App3.app([], []))        # Itt sem kezdünk vele semmit, de kiírjuk a már látott
IO.inspect(App3.app([], [1, 2, 3])) #  IO.inspect/1 függvénnyel, direkt paraméterátadással.
```

A `|>` az ún. **pipe** operátor (mint a Linuxban a `|`): a bal oldalán álló kifejezés eredményét a jobb oldalán álló függvénynek adja át, mégpedig az első paramétereként, ha több paramétere is van.

Az `IO.inspect/1` nemcsak kiírja a kapott kifejezés értékét, hanem eredményként változatlanul vissza is adja, ezért a többi `inspect` függvénnyel együtt nagyon hasznos hibakeresési eszköz: bárhová beszúrható egy kifejezésbe.

```elixir
[1 |> IO.inspect(), 2 |> IO.inspect(), 3 |> IO.inspect()] |> IO.inspect()
```

Ez sorban kiírja az `1`, `2`, `3` értéket, majd az `[1, 2, 3]` listát.

Az `IO.inspect/2` és a `Kernel` modulban definiált `inspect/2` (a `Kernel` modulnév elhagyható) között az a különbség, hogy az előbbi kiírja a kapott kifejezést, és az értékét változatlan formában továbbadja, az utóbbi pedig sztringgé konvertálva adja eredményül (a Livebook ezt a sztringet a cella eredményeként jeleníti meg). Az `IO.puts/1` a kapott kifejezést sztringgé alakítva írja ki, és az `:ok` atomot adja vissza. Az `inspect` függvények működése opciókkal befolyásolható; a listák kiírását szabályozó `charlists:` opciót a [Lista és karakterlánc](../tipusok/lista.md) fejezet mutatja be.

<p class="sources">Forrás: dp26a-fp1ea.pdf (35–37. dia), dp26a-fp1gyfel.livemd, dp26a-fp1gy-megoldasok.livemd</p>
