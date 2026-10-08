# Mintaillesztés

Az Elixir – más funkcionális, illetve deklaratív nyelvekhez hasonlóan – **mintaillesztést** (*pattern matching*) használ a különféle esetek felismerésére és szétválasztására, valamint változók értékhez kötésére.

## Minta és mintaillesztés

A **mintakifejezés**, röviden **minta**, termhez hasonló olyan kifejezés, amelyben nincs függvénykifejezés, de lehet benne szabad változó (a term és a szabad változó fogalmát lásd: [Termek, azonosítók, változók](valtozok.md)).

- A konstansok csak velük azonos értékre illeszkednek, pl. `123`, `[]`, `[1,2,3]`, `~c"abc"`, `"abc"`, `:eof`, `nil`, `true`.
- A kötött, azaz értékkel rendelkező változók csak velük azonos értékre illeszkednek.
- Egy szabad (kötetlen), azaz értékkel nem rendelkező változó mindenre illeszkedik, és sikeres illesztéskor az illeszkedő kifejezés megfelelő részéhez *kötjük*; ezután hivatkozhatunk rá.
- Az aláhúzásjel (`_`, a *névtelen változó*) és az aláhúzásjellel kezdődő változónév is mindenre illeszkedik. Az előbbire nem lehet, az utóbbira nem szokás hivatkozni.
- Egy mintában ugyanaz a változó többször is előfordulhat, ha mindenütt azonos értékre kell illeszkednie.
- Kifejezés **nem lehet** minta, pl. `1+x`, `1+2`, `round(x)`, `round(5.3)`.

A mintaillesztés műveleti jele az `=`, a bal oldalán a mintával, a jobb oldalán egy tömör kifejezéssel: a mintaillesztés egyirányú. A mintaillesztés a minta nem fixált (vö. `^` operátor) változóit értékhez köti.

> [!IMPORTANT]
> A kötés **nem** értékadás! Az `=` nem írja felül a változó értékét egy tárolóban, hanem a bal oldali mintát illeszti a jobb oldali értékre, és a minta szabad változóit a megfelelő részekhez köti.

Változóhoz kétféleképpen köthetünk értéket:

- az `=` mintaillesztés- vagy kötésoperátorral,
- paraméterátadással függvényhíváskor: az aktuális paramétereket illesztjük a formális paraméterekre az egyes *klózokban*.

Ha egy változót értékhez kötünk, de nem használjuk, az Elixir figyelmeztet rá, kivéve akkor, ha a változónév `_`-sal kezdődik.

A Prologban – a funkcionális nyelvekkel ellentétben – kétirányú mintaillesztés van, ennek **egyesítés** a neve.

Néhány egyszerű eset:

- `x = 5` az `x` mintát illeszti az 5 kifejezésre, `x` értéke 5 lesz.
- `[hd|tl] = valami()` a `hd` és `tl` változókat a `valami()` által visszaadott lista fejéhez és farkához köti. Ha a `valami()` üres listával (vagy bármi mással) tér vissza, a kiértékelés hibával leáll: `(MatchError) no match of right hand side value`.
- Az `[x | xs]` minta a legalább egyelemű listákra illeszkedik: `x` a lista fejének, `xs` a farkának az értékét veszi fel; az utóbbi lehet üres is.
- Az `[x1, x2 | xs]` minta a legalább kételemű listákra illeszkedik: `x1` a lista első, `x2` a második elemének, `xs` a farkának az értékét veszi fel.
- Az `[_|xs]` minta is a legalább egyelemű listákra illeszkedik, de a lista fejét a névtelen változóhoz köti, azaz eldobja.
- Az `[_,_|_]` minta a legalább kételemű listákra illeszkedik, de az elemek értékével nem kezd semmit.

```iex
iex> 123 = 123
123
iex> 123 = 321
** (MatchError) no match of right hand side value: 321
iex> ~c"abc" = [97, 98, 99]
~c"abc"
iex> :eof = :eof
:eof
iex> nil = nil
nil
```

Listamintákkal:

```elixir
[x|xs] = ~c"abc" |> IO.inspect
{x, xs}
```

```text
~c"abc"
{97, ~c"bc"}
```

```elixir
[_,_|xs] = ~c"abc" |> IO.inspect
xs
```

```text
~c"abc"
~c"c"
```

```elixir
[_|xs] = ~c"Ábc" |> IO.inspect
xs
```

```text
[193, 98, 99]
~c"bc"
```

(Hogy miért jelenik meg az egyik lista karakterekkel, a másik számokkal, azt a [Lista és karakterlánc](tipusok/lista.md#karakterlánc-single-quoted) fejezet magyarázza.)

Kifejezést tartalmazó minta fordítási hibát ad:

```elixir
defmodule BadPattern do
  def fun(x < 0), do: x
end
```

```elixir
defmodule BadPattern do
  def fun(round(x)), do: x
end
```

```elixir
1+2 = 1+2
```

Mindhárom esetben a hibaüzenet: `cannot invoke remote function ... inside a match` (az `:erlang.</2`, az `:erlang.round/1`, illetve az `:erlang.+/2` függvényre).

## Példák mintaillesztésre

Függvényérték nem lehet minta, és a `&` sem állhat mintában; szabad változó viszont illeszkedhet függvényértékre. Szabad változó a jobb oldalon nem állhat:

```iex
iex> [x, &+/2] = [5, &+/2]
** (CompileError) ... & is not allowed in matches
iex> [x, f] = [5, &+/2]
[5, &:erlang.+/2]
iex> [x, f] = [5, f]
[5, &:erlang.+/2]
iex> a = fn(x) -> x+1 end
#Function<44.40011524/1 in :erl_eval.expr/5>
iex> {a, b} = {fn(x) -> x+1 end, 23}
{#Function<44.40011524/1 in :erl_eval.expr/5>, 23}
iex> fn(x) -> x+1 end = a
** (CompileError) ... fn is not allowed in matches
iex> 3 = szabad
** (CompileError) iex:505: undefined function szabad/0
```

A `[x, f] = [5, f]` sikerül, mert a jobb oldalon `f` már kötött, az értéke a függvény. Listamintákkal:

```iex
iex> [z | zs] = [0,1,2,3]
[0, 1, 2, 3]
iex> [z1 | [z2 | [z3 | [z4 | zs]]]] = [0,1,2,3]
[0, 1, 2, 3]
iex> [z1, z2, z3 | [3]] = [0,1,2,3]
[0, 1, 2, 3]
iex> [z1, z2, z3 | 3] = [0,1,2,3]
** (MatchError) no match of right hand side value: [0, 1, 2, 3]
iex> [z1, z2 | [3]] = [0,1,2,3]
** (MatchError) no match of right hand side value: [0, 1, 2, 3]
```

A `[z1, z2, z3 | 3]` minta azért nem illeszkedik, mert a negyedik elem utáni farok nem a `3` szám, hanem a `[3]` lista; a `[z1, z2 | [3]]` pedig csak háromelemű listára illeszkedhetne.

Ennesmintákkal; ugyanaz a változó többször is előfordulhat a mintában:

```iex
iex> {{a, b}, {a, b}} = {{:a, :b}, {:a, :b}}
{{:a, :b}, {:a, :b}}
iex> {{a, b, a}} = {{:a, :b, :b}}
** (MatchError) no match of right hand side value: {{:a, :b, :b}}
iex> {a, b, _b, _} = {:a, :b, :b, :a}
{:a, :b, :b, :a}
iex> {a, b}
{:a, :b}
iex> _b
warning: the underscored variable "_b" is used after being set...
please rename the variable to remove the underscore
:b
```

Az `_b` kötött ugyan, de mivel aláhúzásjellel kezdődik, a rá való hivatkozásra az Elixir figyelmeztet.

Szótármintákkal. A szótárminta **részleges**: elég, ha a mintában szereplő kulcsok megvannak a szótárban. Kulcs helyén szabad változó nem állhat. A `^` fixálja a változó értékét:

```iex
iex> x = %{b: "barna", z: "zöld"}
%{b: "barna", z: "zöld"}
iex> %{k1: v1, k2: v2} = x
** (MatchError) no match of right hand side value: %{b: "barna", z: "zöld"}
iex> %{k1 => v1, k2 => v2} = x
** (CompileError) iex:3: cannot use variable k1 as map key inside a pattern...
iex> %{b: v1, z: v2} = x
%{b: "barna", z: "zöld"}
iex> {v1, v2}
{"barna", "zöld"}
iex> %{z: ^v1, b: v2} = x
** (MatchError) no match of right hand side value: %{b: "barna", z: "zöld"}
iex> %{z: v1, b: v2} = x
%{b: "barna", z: "zöld"}
iex> {v1, v2}
{"zöld", "barna"}
iex> %{b: v} = x # részleges mintaillesztés
%{b: "barna", z: "zöld"}
iex> v
"barna"
```

A `%{z: ^v1, b: v2} = x` azért hiúsul meg, mert `v1` értéke ekkor `"barna"`, a `:z` kulcshoz tartozó érték pedig `"zöld"`.

## Réteges minta

A **réteges minta** (*layered pattern*) `minta = változó` alakú: a változó a teljes illesztett értékhez kötődik, a minta pedig a részeihez. Így egyszerre hivatkozhatunk az egészre és a komponenseire:

```iex
iex> ([y|ys] = yss) = [1, 2, 3] # réteges minta (layered pattern)
[1, 2, 3]
iex> {y, ys, yss}
{1, [2, 3], [1, 2, 3]}
```

Függvény paraméterében is használható. Az alábbi `[z | zs] = zzs` mintával a klóz törzsében a teljes listára `zzs`-sel, a fejére `z`-vel, a farkára `zs`-sel hivatkozhatunk:

```elixir
  def app([z | zs] = zzs, ys) do
    [z | app(zs, ys)]
  end
```

A réteges minta további haszna a [Klózok](#egymást-kölcsönösen-kizáró-minták) szakaszban látható.

## Mintaillesztés `case` kifejezéssel

A `case` kifejezés a kapott értéket sorban illeszti az ágak mintáira, és az első illeszkedő ág kifejezését értékeli ki:

```elixir
case valami() do
  [hd|tl] -> ... # Ha nem üres lista
  [] -> ... # Ha üres lista
  _ -> ... # Bármi más
end
```

## Őr

A mintában csak tömör, azaz kiértékelhető kifejezés lehet, változót tartalmazó kifejezés nem. Ilyesmit tehát nem írhatunk le:

```elixir
def fac(n >= 0), do: ...
```

Az ilyen esetek gyakoriak, ezért a minta ún. **őrrel** (*guard*) egészíthető ki. Az őrt a függvényfejben a paraméter(eke)t követő `when` kulcsszó vezeti be, utána **őrkifejezés** áll:

```elixir
  def fac(n) when n >= 0, do: ...
```

Az őrkifejezésben csak őrként (*guard*) definiált, garantáltan mellékhatás nélküli könyvtári függvényeket hívhatunk, más függvényeket, így saját függvényeket sem. Ilyenek például a típusvizsgáló `is_...` függvények és a `not`, `and`, `or` műveletek (lásd [Műveletek és beépített függvények](muveletek.md)).

Őr a `case` ágaiban is állhat. Az alábbi `case` kifejezés egészekkel kezdődő nem üres listára a fej kétszeresét, üres listára 0-t, bármi másra `nil`-t (hibajelzést) ad:

```elixir
case valami() do
  [hd|tl] when is_integer(hd) -> hd * 2 # Ha nem üres lista
  [] -> 0 # Ha üres lista
  _ -> nil # Bármi más: hibajelzés
end
```

## Klózok

Egy függvényt több **klózzal** definiálhatunk: minden előforduló esetre egy-egy klózt írunk, és a függvény hívásakor az első olyan klóz törzse értékelődik ki, amelynek mintájára (és őrére) az aktuális paraméterek illeszkednek. Minden klóz független a többitől: a paramétereik neve lehet azonos, de különböző is; egy klóz törzsében csak a saját paramétereire lehet hivatkozni.

Ha egyik klóz sem illeszkedik, a hívás `FunctionClauseError` hibával leáll. Például ha az összefűzés első változata csak az üres listát kezeli:

```elixir
defmodule App0 do
  # app(xs, ys): xs és ys listák összefűzöttje zs == (xs ⊕ ys)
  # [] ⊕ ys == ys
  def app([], ys), do: ys
end
```

akkor az `App0.app([], ~c"abc")` eredménye `~c"abc"`, az `App0.app([1,2,3], ~c"abc")` viszont `FunctionClauseError` hibát ad. A hiányzó eset tehát nem fordítási hiba, hanem futás közben derül ki. A *dialyzer* ([Típusellenőrzés: dialyzer](elixir/mix.md#típusellenőrzés-dialyzer)) sem jelzi a hiányzó eseteket; csak akkor figyelmeztet, ha be tudja bizonyítani, hogy egy hívás soha nem lehet sikeres.

### Egymást kölcsönösen kizáró minták

Egy függvény klózainak mintái lehetőleg **zárják ki kölcsönösen** egymást. Tegyük fel például, hogy egy függvénynek – az üres listát nem kezelve – azt kell megkülönböztetnie, amikor a listának *pontosan* egy eleme van, attól, amikor *legalább* egy eleme van:

```elixir
def fun([x|xs])...
def fun([x])...
```

Ezzel az a gond, hogy az első klóz ***minden*** olyan listára illeszkedik, amelynek van feje, a farka pedig tetszőleges elemszámú, azaz üres is lehet. Ezért az első klóz az egyelemű listára is illeszkedik, a második klózra soha nem kerül sor: a minták nem zárják ki kölcsönösen egymást (erre az Elixir-fordító figyelmeztet is). A két klóz sorrendjének megfordításával a mintaillesztés már meg tudja különböztetni a két esetet, ám ennek hatékonyságromlás az ára:

```elixir
def fun([x])...
def fun([x|xs])...
```

Írhatunk azonban olyan mintát is, amely a legalább kételemű listákra illeszkedik, és így kölcsönösen kizárja a pontosan egyelemű listára illeszkedő mintát:

```elixir
def fun([x1,x2|xs])...
def fun([x])...
```

Az első klóz törzsében a lista fejére az `x1` változóval, a farkára az `[x2|xs]` kifejezéssel hivatkozhatunk. Ez utóbbi hivatkozást egyszerűbbé (és olcsóbbá) teszi a réteges minta; a lista farkára ekkor az `xxs` változóval hivatkozunk:

```elixir
def fun([x1 | xxs = [x2|xs]])...
def fun([x])...
```

Ha az `x2` és `xs` változókat nem használjuk a klóz törzsében, az Elixir-fordító figyelmeztet. A figyelmeztetést úgy kerülhetjük el, hogy a változó nevét aláhúzásjellel kezdjük, vagy elég csak aláhúzásjelet írni:

```elixir
def fun([x1 | xxs = [_x2|_xs]])...
def fun([x1 | xxs = [_|_]])...
```

A beszédes nevek azonban segítik a megértést, utalnak a változó szerepére. Ha a lista második elemére vagy a harmadik elemtől kezdődő farkára hivatkozni akarunk a klóz törzsében, akkor ne aláhúzásjellel kezdődő változóneveket használjunk.

<p class="sources">Forrás: dp26a-fp1ea.pdf (22. dia), dp26a-fp3ea.pdf (23–26. dia), dp26a-fp1gyfel.livemd, dp26a-fp2gy-megoldasok.livemd, dp26a-fp1gy-megoldasok.livemd</p>
