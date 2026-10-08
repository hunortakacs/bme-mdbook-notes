# Kulcs-érték lista és szótár

## Kulcs-érték lista (Keyword list)

Egy kulcs-érték pár kételemű ennesként írható le: `{:key, value}`, ahol a kulcs csak atom, az érték tetszőleges típusú lehet. Az ilyen párokból álló listára gyakran van szükség, ezért az Elixir többféle jelölést, rövidítést, bizonyos esetekben zárójelelhagyást is megenged: `[{:név, "Szöszi"}]` helyett írható `[név: "Szöszi"]`, és ha a kulcs-érték lista egy függvényhívás vagy egy ennes utolsó eleme, a szögletes zárójel is elhagyható.

```iex
iex> [{:név,"Szöszi"},{:szerelme,"jazz-zongorista"},{:város,"Prága"}]
[név: "Szöszi", szerelme: "jazz-zongorista", város: "Prága"]
iex> [név: "Szöszi", szerelme: "jazz-zongorista", város: "Prága"]
[név: "Szöszi", szerelme: "jazz-zongorista", város: "Prága"]
iex> inspect név: "Szöszi", szerelme: "jazz-zongorista", város: "Prága"
"[név: \"Szöszi\", szerelme: \"jazz-zongorista\", város: \"Prága\"]"
iex> [:cseh_film, név: "Szöszi", város: "Prága", szerelme: "zongorista"]
[:cseh_film, {:név, "Szöszi"}, {:város, "Prága"}, {:szerelme, "zongorista"}]
iex> {:cseh_film, név: "Szöszi", szerelme: "zongorista", város: "Prága"}
{:cseh_film, [név: "Szöszi", szerelme: "zongorista", város: "Prága"]}
```

A negyedik példában a lista első eleme atom, nem pár, ezért ez már nem kulcs-érték lista, és az Elixir a párokat ennesként írja ki. Az ötödikben a zárójel nélküli kulcs-érték lista az ennes második eleme lesz.

A kulcs-érték párokat leginkább függvényopciók megadására használjuk, pl. `limit: :infinity`, `charlists: :as_lists`.

## Szótár (Map)

A **szótár** kulcs-érték párok rendezett kollekciója.

- Jelölése (*map literal*): `%{ key1 => value1, key2 => value2, ...}`.
- Ha a kulcs atom, alternatív jelölés: `%{atom1: value1, atom2: value2}`.
- A kulcsok és az értékek típusa tetszőleges, lehet kifejezés is; egy szótáron belül a kulcsok különböző típusúak lehetnek.

```iex
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

Az utolsó példában a `(&+/2).(3,2)` kulcskifejezés értéke 5. Ha a kulcsok vegyesen atomok és más értékek, az atom kulcsú párokat is ki lehet írni rövid alakban, de csak a lista végén (`fütty: ...`).

A szótárt elsősorban asszociatív tömbként szokás használni. Értéket a kulccsal, szögletes zárójeles jelöléssel nyerünk ki belőle; ha nincs ilyen kulcs, az eredmény `nil`. Ha a kulcs atom, a rövidebb pontos jelölés is használható:

```iex
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

További részletek a `Map` modul dokumentációjában találhatók.

<p class="sources">Forrás: dp26a-fp2ea.pdf (16–18. dia)</p>
