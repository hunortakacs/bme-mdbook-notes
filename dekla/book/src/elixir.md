# Az Elixir nyelv

## Fő jellemzők

Az Elixir

- funkcionális nyelv;
- a nyelvben minden kifejezés: nincs utasítás (*statement*) és kifejezés (*expression*) megkülönböztetés;
- a különféle esetek felismerésére és szétválasztására **mintaillesztést** használ ([Mintaillesztés](mintaillesztes.md));
- ciklusok helyett **rekurziót** és **magasabb rendű függvényeket** használ ([Rekurzió](rekurzio.md), [Függvény](tipusok/fuggveny.md));
- dinamikusan típusos ([Típusok](tipusok.md));
- nincs semmi megosztva: a processzek üzenetekkel kommunikálnak;
- Erlang-függvények hívhatók Elixirből, Elixir-függvények Erlangból.

## Erlang, BEAM és Elixir

Az **Erlang Open Telecom Platform** (OTP) az Ericsson által fejlesztett nyílt forráskódú rendszer masszívan párhuzamos, elosztott, megbízható alkalmazások fejlesztésére. Kihasználja az üzenetküldést és azt, hogy nincs megosztott memória és nincs változómódosítás; akár függvények is átküldhetők a szerverek között.

- **Erlang**: az OTP platform eredeti funkcionális programozási nyelve, a Prologhoz hasonló szintaxissal.
- **BEAM**: az Erlang/OTP virtuális gépe.
- **Elixir**: funkcionális programozási nyelv a BEAM platformra, modern (a Rubyra hasonlító) szintaxissal.

A viszonyuk olyan, mint a Java-világban: BEAM : Erlang : Elixir ≈ JVM : Java : Kotlin. A Livebook pedig az Elixir számára az, ami a Jupyter a Pythonnak: notebook.

## Folyamatok üzenetekkel kommunikálnak

A folyamatok (processzek) között nincs megosztott memória; egymással üzenetküldéssel kommunikálnak (*aktor modell*). Az alábbi példában a `spawn/1` új folyamatot indít, amely a `receive` blokkban üzenetre vár. A főfolyamat a `send/2`-vel küld neki egy üzenetet, benne a saját azonosítójával (`self()`) mint válaszcímmel, majd maga is a válaszra vár; a beérkező üzenetet mintaillesztéssel fogadja:

```elixir
worker = spawn(fn -> # Új folyamat indítása
  receive do # Várakozás üzenetre
    {:hello, from} -> # Válasz küldése from felé
      send(from, {:reply, "Hello from the worker process!"})
  end
end)
send(worker, {:hello, self()}) # Üzenet küldése válaszcímmel
receive do # Várakozás a worker folyamat válaszára
  {:reply, message} -> # Üzenet fogadása mintaillesztéssel
    IO.puts(message)
end
```

Az egymás utáni üzenetekre rekurzív függvényekkel lehet válaszolni: a függvény fogad egy üzenetet, válaszol rá, majd jobbrekurzívan újra meghívja önmagát, és várja a következőt.

<p class="sources">Forrás: dp26a-fp1ea.pdf (21., 26–27. dia)</p>
