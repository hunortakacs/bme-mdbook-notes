# Kihagy-bevesz rekurzió

A **kihagy-bevesz** (*include-exclude*, *inclusion-exclusion*) rekurzió a lista minden eleménél két ágra bontja a feladatot: az egyik ágban az elemet bevesszük a készülő megoldásba, a másikban kihagyjuk. Így a lista elemeinek összes részhalmazát bejárja: $n$ elemű listánál $2^n$ esetet.

## Kombinációk

A `komb/1` egy lista elemeinek összes kombinációját (részhalmazát) adja eredményül. Az `acc` akkumulátor a már bevett elemeket gyűjti. Minden elemnél két rekurzív hívás van: a `komb(ns, acc)` kihagyja az `n` elemet, a `komb(ns, [n | acc])` beveszi; a két ág eredményét összefűzzük. Ha elfogytak az elemek, az akkumulátor egy kész kombináció:

```elixir
defmodule Kombinaciok do
  def komb(ns), do: komb(ns, [])

  defp komb([n | ns], acc) do
    komb(ns, acc) ++ komb(ns, [n | acc])
  end
  defp komb([], acc), do: [acc]
end
```

```elixir
Kombinaciok.komb([1,2,3]) |> Enum.sort
```

```text
[[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
```

Mivel a bevett elemeket az akkumulátor elé fűzzük, a kombinációk elemei fordított sorrendben állnak (`[3, 2, 1]`).

## Összeg testvéries elosztása

Adott pénzérméket úgy kell elosztani két ember között, hogy a két összeg különbségének abszolút értéke a lehető legkisebb legyen (CEOI'1995 versenyfeladat; CEOI: Közép-európai Informatikai Diákolimpia, *Central European Olympiad in Informatics*).

Ha az érmék értékét tartalmazó lista `[28, 7, 11, 8, 9, 7, 27]`, akkor egyikük a `[9, 11, 28]` érméket kapja, amelyek összege `48`, másikuk a többit (`[7, 7, 8, 27]`), amelyek összege `49`.

Az `eloszt/1` először kiszámítja a teljes összeget (`tot`), és ennek felét egész osztással (`tgt`, a célösszeg). Ezután kihagy-bevesz rekurzióval kigyűjti az összes olyan részlistát, amelynek összege nem nagyobb a célösszegnél, végül ezek közül kiválogatja a maximális összegűeket. Az eredmény egy szótár, amelynek kulcsai az összegfeltételt kielégítő részlisták, értékei pedig e részlisták összege, azaz az elosztás kisebbik összege.

```elixir
defmodule ElosztS do

  def sort(ls), do: Enum.sort(ls, fn (a,b) -> b < a end)

  @type p_int() :: integer()
  @type my_map() :: %{[p_int()] => p_int()}
  @spec max_osszegek(map :: my_map()) :: resmap :: my_map()
  def max_osszegek(map) do
    maxval = Enum.max(Map.values(map))
    for {k,v} <- map, v == maxval, into: %{}, do: {k, v}
  end
end
```

Az `ElosztS.max_osszegek/1` a for-jelöléssel azokat a párokat válogatja ki a szótárból, amelyek értéke a legnagyobb.

```elixir
defmodule Eloszt do

  @spec eloszt(vals :: [ElosztS.p_int()]) :: map :: ElosztS.my_map
    # Legyen halfsum a vals pozitív egészlista összegének a fele (egész osztással).
    # A map kulcs-érték párjaiban a kulcsok vals olyan max. összegű részlistái,
    # melyek összege nem nagyobb halfsum-nál, az értékek pedig e részlisták összege.

  def eloszt([_,_|_] = vals) do
    tot = Enum.sum(vals)
    |> IO.inspect(label: "Listaösszeg")
    tgt = div(tot, 2)
    |> IO.inspect(label: "Célérték")

    # vals = vals #Enum.sort(vals) #my_sort(vals) # rendezzük az értéklistát csökkenő sorrendben
    # |> IO.inspect()
    eloszt(Map.new(), vals, tgt, [], 0) # Map.new() === %{} # 0 jó-e?
    # |> IO.inspect()
    |> ElosztS.max_osszegek()
  end
  def eloszt(_), do: "A listának legalább kételeműnek kell lennie."

  @spec eloszt(map  :: ElosztS.my_map(),  # map-be gyűjtjük a részlistákat és összegüket
               vals :: [ElosztS.p_int()], # a még feldolgozandó érmelista
               tgt  :: ElosztS.p_int(),   # a célösszeg (nem változik)
               curr :: [ElosztS.p_int()], # a már összegyűjtött részlista
               sum  :: ElosztS.p_int())   # a már összegyűjtött részlista összege
          :: resmap :: ElosztS.my_map()   # a bővített map, a fv. eredménye

  defp eloszt(map, [val|vals], tgt, curr, sum) do
    curr_new = [val | curr] # az aktuális érmével bővített részlista
    sum_new = sum + val     # az aktuális érmével megnövelt összeg

    # ha az új összeg nem nagyobb a célösszegnél, berakjuk a map-be, ha kisebb, nem
    # figyeljük meg, hogyan használjuk a pipe-ot az esetleg bővített map továbbadására
    (if sum_new <= tgt, do: Map.put(map, curr_new, sum_new), else: map)
    |> eloszt(vals, tgt, curr_new, sum_new) # 1. ág: val-t bevesszük # feltételesen kihagyható
    |> eloszt(vals, tgt, curr, sum) # 2. ág: val-t kihagyjuk
  end
  defp eloszt(map, [], _tgt, _curr, _sum), do: map
end
```

Az `eloszt/5` a szótárt (`map`) a pipe-pal adja tovább: az első rekurzív hívás (a bevevő ág) a bővített szótárral tér vissza, és ezt kapja meg első paraméterként a második rekurzív hívás (a kihagyó ág). Így a két ág eredménye egyetlen szótárban gyűlik.

```elixir
Eloszt.eloszt([1, 2, 3, 4])
```

```text
Listaösszeg: 10
Célérték: 5
%{[3, 2] => 5, [4, 1] => 5}
```

További példák (a `Listaösszeg` és `Célérték` sorok nélkül):

```elixir
Eloszt.eloszt([28, 7, 11, 8, 9, 7, 27]) |> IO.inspect()
Eloszt.eloszt([1,2,3,4,5]) |> IO.inspect()
Eloszt.eloszt([4,1,2,5,3]) |> IO.inspect()
Eloszt.eloszt([4,1,2,5,6,3,7]) |> IO.inspect()
```

```text
%{[9, 11, 28] => 48}
%{[4, 2, 1] => 7, [4, 3] => 7, [5, 2] => 7}
%{[2, 1, 4] => 7, [3, 4] => 7, [5, 2] => 7}
%{
  [3, 5, 2, 4] => 14,
  [3, 6, 1, 4] => 14,
  [3, 6, 5] => 14,
  [6, 5, 2, 1] => 14,
  [7, 2, 1, 4] => 14,
  [7, 3, 4] => 14,
  [7, 5, 2] => 14,
  [7, 6, 1] => 14
}
```

A kulcsokban az érmék a bevétel fordított sorrendjében állnak. Egyelemű vagy üres listára a függvény a `"A listának legalább kételeműnek kell lennie."` sztringet adja.

## Gyakorló feladatok

- A bemutatott megoldás először kigyűjti az összes olyan részlistát, amelynek összege nem nagyobb a teljes listaösszeg felénél, és csak ezután válogatja ki közülük a maximális összegűeket. Írjon egy vagy több olyan változatot, amely nem tartja meg az összes részlistát, hanem már menet közben eldobja az aktuális maximumnál kisebb összegűeket!
- Ezután próbáljon olyan megoldást írni, amely az egyszer már kiszámolt összegű részlisták összegét nem számolja ki újra!
- Hasonlítsa össze az egyes változatok futási idejét a `benchee` segítségével, és becsülje meg a tárigényüket!

<p class="sources">Forrás: dp26a-fp3ea.pdf (6. dia), dp26a-fp3ea-reszlistak-kihagy_bevesz_rek.livemd, dp26a-fp3gy.livemd</p>
