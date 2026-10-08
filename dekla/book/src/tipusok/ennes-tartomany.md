# Ennes és tartomány

## Ennes (Tuple)

Az **ennes** rögzített számú, tetszőleges kifejezésből álló, fix sorrendű kollekció. Jelölése kapcsos zárójel, az elemek vesszővel elválasztva. Ennesként tudunk két vagy több értéket paraméterként átadni vagy eredményként visszakapni.

```iex
iex> {0x1ff, :erlang, Armstrong, 'Joe'++[0], [], {}}
{511, :erlang, Armstrong, [74, 111, 101, 0], [], {}}
iex> {plus, per, sin} = # mintaillesztések kötésekkel
  {&Kernel.+/2, &//2, &:math.sin/1}
{&:erlang.+/2, &:erlang.//2, &:math.sin/1}
iex> {plus.(3,4), per.(3,4)} # infix volt, prefix lett
{7, 0.75}
iex> sin.(90*:math.pi/180)
1.0
```

Az első példában a `0x1ff` értéke 511, a `'Joe'++[0]` pedig a `'Joe'` karakterkód-lista és a `[0]` összefűzése; mivel a 0 nem nyomtatható karakter kódja, a lista számokként jelenik meg (lásd [Lista és karakterlánc](lista.md)). A második példa mintaillesztéssel köti a három függvényt a `plus`, `per` és `sin` változóhoz (lásd [Mintaillesztés](../mintaillesztes.md)).

## Tartomány (Range)

A **tartomány** egész számok sorozata a [start, end] tartományban, `start..end` vagy lépésközzel `start..end//lépés` alakban:

```iex
iex> {18..23, 18..10}
{18..23, 18..10//-1}
iex> for i <- 18..10 // -3, do: i
[18, 15, 12]
```

A `18..10` csökkenő tartomány, az Elixir ki is írja a `-1` lépésközt. A második példa a [for-jelöléssel](../for.md) sorolja fel a `18..10//-3` tartomány elemeit.

<p class="sources">Forrás: dp26a-fp2ea.pdf (10. dia)</p>
