# Reguláris kifejezés

Az Elixirben a **reguláris kifejezés** (Regex) is önálló típus. Jelölése `~r{regexp}` vagy `~r{regexp}options`. A `~r{...}` jelölés is szigil, azaz bűvös jelölés; a szigilekről részletek a `Kernel` dokumentációjában találhatók. A reguláris kifejezés szintaxisa a PCRE (*Perl Compatible Regular Expressions*, <http://www.pcre.org>) szerinti.

A `Regex.run/2` az első illeszkedést adja vissza, a `Regex.scan/2` az összeset, a `Regex.split/2` az illeszkedések mentén darabolja a sztringet, a `Regex.replace/3` pedig lecseréli az illeszkedő részeket:

```iex
iex> Regex.run ~r{[cdr]}, "madárcsicsergés"
["d"]
iex> Regex.scan ~r{[cdr]}, "madárcsicsergés"
[["d"], ["r"], ["c"], ["c"], ["r"]]
iex> Regex.split ~r{[cdr]}, "madárcsicsergés"
["ma", "á", "", "si", "se", "gés"]
iex> Regex.replace ~r{[cdr]}, "madárcsicsergés", "."
"ma.á..si.se.gés"
```

A regexp után egy vagy több egykarakteres opció állhat:

| **Jel** | **Jelentés** |
|---|---|
| f | Többsoros sztring első sorában kezdődjön az illesztés |
| i | Az illesztés ne különböztesse meg a kis- és nagybetűket |
| m | Többsoros sztring esetén a `^` és a `$` az egyes sorok elejét és végét jelentse (a `\A` és `\z` jelentése változatlanul a sztring eleje és vége) |
| s | A `.` illeszkedjen az újsor-karakterekre is |
| U | Az egyébként mohó `*` és `+` módosítók legyenek lusták, azaz a minta a lehető leghosszabb karaktersorozat helyett a lehető legrövidebbre illeszkedjen |
| u | Engedje meg Unicode-specifikus minták, pl. `\p` használatát |
| x | Engedje meg a bővített mód használatát: ignorálja a szóköz-jellegű (ún. whitespace) karaktereket és a kommenteket (a `#` jeltől a sor végéig) |

Az alábbi példákban a `cs.*s` minta `cs`-vel kezdődő, `s`-re végződő részt keres. Opció nélkül csak a kisbetűs `cs`-re illeszkedik, és a mohó `.*` a lehető leghosszabb részt veszi; az `i` opcióval a nagybetűs `Cs` is illeszkedik; az `U` opcióval a `.*` lusta lesz, így a legrövidebb illeszkedést kapjuk:

```iex
iex> Regex.run ~r{cs.*s}, "Madarak Csicsergése"
["csergés"]
iex> Regex.run ~r{cs.*s}i, "Madarak Csicsergése"
["Csicsergés"]
iex> Regex.run ~r{cs.*s}iU, "Madarak Csicsergése"
["Csics"]
```

További részletek a `Regex` modul dokumentációjában találhatók.

<p class="sources">Forrás: dp26a-fp2ea.pdf (19–20. dia)</p>
