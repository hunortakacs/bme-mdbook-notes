# Atom, szám, igazságérték

## Atom

Az **atom** olyan konstans, amelynek az értéke maga a neve.

- Kettősponttal (`:`) kezdődik.
- Kezdődhet az angol ábécé nagybetűjével is, kettőspont nélkül, de ez konvenció szerint a modulnevekre van fenntartva.
- A `:` után UTF-8 kódolású karaktersorozat, Elixir-operátor vagy sztring állhat.
- Az UTF-8 kódolású karaktersorozatban betűk, számjegyek és kétféle írásjel (`_`, `@`) lehetnek; a karaktersorozat végén általában kérdőjel (`?`) vagy felkiáltójel (`!`) is állhat.
- Saját magát jelöli, nem sztring: egy atom értéke maga a neve.
- Két azonos nevű atom mindig egyenlő, akárhol is vannak definiálva.
- Hasonló a Prolog névkonstanshoz (atomhoz).

Példák: `:jános`, `:is_bin?`, `:vált@2`, `:<>`, `:"fun/3"`, `:"éljen soká!"`, `:Éljen_soká!`, `:"Őrült Űrőr tűrjön"`, `Dp`, `Gy1`.

## Szám

**Egész** (integer):

- decimális, pl. `1234`;
- hexadecimális, pl. `0xcafe`;
- oktális, pl. `0o765`;
- bináris, pl. `0b1010`;
- tagolható, pl. `123_456_789`;
- korlátlan pontosságú, pl. `123456789012345678901234567890`;
- karakterkód (Unicode codepoint): ha nyomtatható, `?z`, ha vezérlő, `?\n`. A `?z` tehát egész szám, a `z` karakter kódja (122).

**Lebegőpontos** (float):

- pl. `3.14159`;
- vezető nullával, pl. `0.14159` (a tizedespont előtt mindig kell számjegy);
- exponenssel, pl. `0.2e-22`;
- IEEE 754 szerinti, dupla pontosságú (64 bit, kb. 16 számjegy, max. exponens kb. $10^{308}$).

## Igazságérték

**Igazságérték**, másnéven logikai érték (boolean):

- Három atomot tekintünk igazságértéknek: `:true`, `:false`, `:nil`.
- Mindhárom írható kettőspont nélkül is: `true`, `false`, `nil`.
- A `false` és a `nil` hamis, minden más érték (nemcsak a `true`) igaz.
- Angolul szokás megkülönböztetni a *true*-t a *truthy*-tól (igaznak számító érték), a *false*-t a *falsy*-tól (hamisnak számító érték), pl. a JavaScriptben, a Javában, az Elixirben.

A logikai műveleteket a [Műveletek és beépített függvények](../muveletek.md#logikai-műveletek) fejezet tárgyalja.

<p class="sources">Forrás: dp26a-fp2ea.pdf (5–6., 25. dia)</p>
