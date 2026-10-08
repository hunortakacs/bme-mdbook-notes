# Termek, azonosítók, változók

## Term

A **term** tetszőleges adatstruktúra. Minden termnek van értéke és típusa, és a term maga is kifejezés. Közelítő rekurzív definíciója: szám-, atom-, függvény- és más értékekből, illetve termekből konstruktorokkal felépített, tovább nem egyszerűsíthető kifejezés.

A term tehát tovább nem egyszerűsíthető és **tömör**: kiértékelhető, azaz nincs benne szabad változó. Ha a `kötött` változó értéke már `kötött = 2021`, akkor az alábbiak termek:

```elixir
123456789
{'Diák Detti', [{:khf, [:prolog, :elixir, :prolog]}]}
[&:erlang.+/2, kötött, fn(x,y) -> x*y end]
```

Nem termek viszont azok a kifejezések, amelyek tovább egyszerűsíthetők vagy nem tömörek:

```elixir
5+6                   # műveletet tartalmaz
(&:erlang.+/2).(5,6) # függvényalkalmazást tartalmaz
szabad                # szabad változó
```

## Azonosító (identifier)

Az **azonosító** kisbetűvel vagy aláhúzásjellel (`_`) kezdődő, betűket, számjegyeket és aláhúzásjeleket tartalmazó, opcionálisan kérdő- vagy felkiáltójellel végződő karaktersorozat. A betű és a számjegy UTF-8 kódolású betű, illetve decimális számjegy lehet (lásd <https://hexdocs.pm/elixir/unicode-syntax.html>). Az azonosító változót vagy függvénynevet jelöl.

Konvenciók:

- a `?`-lel végződő azonosító kiértékelése igazságértéket ad eredményül;
- a `!`-lel végződő azonosító kiértékelése kivételt dob, ha meghiúsul;
- az azonosító részeit aláhúzásjellel tagoljuk (ún. megengedő *snake_case*; vö. az [atom](tipusok/atom-szam.md) szintaxisával).

```text
what_s_in_a_name   name?   exec!
_unused   rómeó_és_Júlia   year_2021
```

## Változó

Egy változó lehet **szabad** vagy **kötött**. A szabad változónak nincs értéke és típusa; a kötött változó valamely konkrét term szinonimája.

A változóhoz új érték köthető, de ez a korábbi felhasználását nem módosítja: a korábban kiértékelt kifejezések a régi értéket használták. A `^` (*pin*) operátor a kötött változó értékét fixálja: így a változó nem köthető új értékhez, hanem a mintaillesztésben a meglévő értékével vesz részt.

```iex
iex> x = fn(x) -> 2*x end # a külső és a belső x nem ugyanaz!
#Function<44.40011524/1 in :erl_eval.expr/5>
iex> y = x
#Function<44.40011524/1 in :erl_eval.expr/5>
iex> ^x = y.(2)
** (MatchError) no match of right hand side value: 4
iex> x = y.(2)
4
iex> y
#Function<44.40011524/1 in :erl_eval.expr/5>
```

A `^x = y.(2)` meghiúsul, mert `x` értéke itt a függvény, nem a 4. Az `x = y.(2)` után `x` új értéke 4, de `y` továbbra is a függvényt jelöli, mert a kötésekor `x` még a függvény volt.

## Változó hatásköre

A változók hatásköre **lexikális**:

- A függvény törzsében és fejében definiált változók (az utóbbiak másnéven a formális paraméterek) lokálisak a függvényre nézve.
- Modulban is lehet változót definiálni, de az csak modulszinten látható, a modulban definiált függvényekből nem.
- A `with` kifejezéssel is definiálhatunk lokális változót: a `with` után kötött változók csak a `do:` utáni kifejezésben látszanak.

```iex
iex> with a = 5, b = 7, do: a*a + 2*a*b + b*b
144
iex> a = 11; with a = 5, b = 7, do: a*a + 2*a*b + b*b; a
11
```

A második példában a `with`-en belüli `a = 5` nem változtatja meg a külső `a` értékét, amely 11 marad. A `;` egy sorban választ el kifejezéseket.

## Komment

A komment `#` jellel kezdődik, és a sor végéig tart.

<p class="sources">Forrás: dp26a-fp2ea.pdf (22–25. dia)</p>
