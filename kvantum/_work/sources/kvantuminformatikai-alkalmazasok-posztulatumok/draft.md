# Kvantuminformatikai alkalmazások_posztulátumok.pdf

<!-- 20 pages, 20 units, grouping: heuristic -->

## s1 · p1 · (no title)
<!-- status: TODO view pages/p001.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p001-f1.png -->
<!-- figure: figures/p001-f2.png -->

**Kvantummechanikai posztulátumok** **és alkalmazásuk**

Kvantuminformatikai alkalmazások BMEVIHIAD00

Budapest,

**Oláh Kitti**

2026. 09. 21.

BME Hálózati Rendszerek és Szolgáltatások Tanszék olah.kitti@edu.bme.hu

## s2 · p2 · MOTIVÁCIÓ
<!-- status: auto -->

„Nem szeretem, és sajnálom, hogy valaha is közöm volt hozzá.” – **Erwin Schrödinger**

„Azok, akiket nem sokkol, amikor először találkoznak a kvantummechanikával valószínűleg nem értették meg.” – **Niels Bohr**

„Azt hiszem kijelenthetem, hogy senki sem érti a kvantummechanikát.” – **Richard Feynman**

## s3 · p3 · TARTALOM
<!-- status: auto -->

- Mit nevezünk posztulátumnak? Mérnöki és fizikusi
aspektusból?
- Mi a kvantumkommunikáció alapköve?
- Két állapotú rendszerek bemutatása, Hilbert-tér és
a kvantummechanika kapcsolata
- Mit jelent az unitér transzformáció? Kvantumkapuk
bemutatása Bloch-gömb segítségével
- Méréstechnika kvantumosan
- Ha van egy kvantumbitünk, miért ne lehetne
egyszerre több is…

## s4 · p4 · POSZTULÁTUM
<!-- status: auto -->

- Valamely gondolati rendszer alapját képező, szükségképp
igaznak tekintett állítások egyike.
- Bizonyítás nélkül elfogadott, a gondolkodás szempontjából
nélkülözhetetlen feltevés, tétel.
- Egy bizonyos gondolati rendszer vagy tudományág számára a
posztulátum az a minimális feltétel, amely alapján további következtetéseket lehet levonni, pl. a béke a jövő fejlődésének posztulátuma.
- Geometriai posztulátum: Euklideszi geometria
- Axióma: egy, az adott tudományágon belül bizonyíthatatlan, ám
magától értetődőnek tekintett állítás („**Ez triviális kolléga**”)

## s5 · p5 · (no title)
<!-- status: TODO view pages/p005.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p005-f1.png -->

**Elválasztó fólia címmel**

**Kvantummechanikai posztulátumok mérnöki**

**interpretációban**

## s6 · p6 · I. POSZTULÁTUM
<!-- status: TODO view pages/p006.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p006-f1.png -->

**Állapotleírás**

**Zárt** fizikai rendszer aktuális állapota egy olyan állapotvektorral írható le, amely komplex együtthatókkal rendelkezik, egységnyi hosszú a Hilbert-térben (egy komplex lineáris vektortérben, amelyben értelmezve van a belső szorzat).
- 𝛼^(2) + 𝛽^(2) = 1
𝛼, 𝛽∈ℂ

Links: <https://www.shutterstock.com/hu/search/quantum-vacuum-state>

## s7 · p7 · KVANTUMBIT (QUBIT)
<!-- status: TODO view pages/p007.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p007-f1.png -->

𝜑^(†)

ȁۧ𝜑=ۦȁ
- Dirac ‘*ket*’ és ‘*bra*’ jelölés
- Kvantumbit: mindkét klasszikus állapotot (bázisállapotot)
tartalmazza egyidőben: szuperpozíció

1 ^(=) ^(𝛼)

ȁۧ𝜑= 𝛼หۧ0 + 𝛽ȁۧ1 = 𝛼^(1)
        - 0 ^(+ 𝛽0)
𝛽
- ahol a és b komplex valószínűségi amplitúdók. Abszolút érték
négyzetük adja meg a mérés eredményét (a klasszikus bázisban): 𝛼^(2) + 𝛽^(2) = 1
- Műveletek: belső és külső szorzat

## s8 · p8 · HILBERT-TÉR
<!-- status: TODO view pages/p008.png -->
<!-- flags: table, layout -->

- Végtelen dimenziójú euklideszi vektorterek
általánosítása
- Teljes
- Metrikus
**Kvantum interpretáció** Állapot leírás Megfigyelhető Mérés eredménye Mérés valószínűsége Időbeni változása

**Hilbert-térben** Vektor Hermitikus operátor Operátor sajátértéke Belső szorzat négyzete Unitér transzformáció (Schrödinger-egyenlet)

## s9 · p9 · II. POSZTULÁTUM
<!-- status: TODO view pages/p009.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p009-f1.png -->
<!-- figure: figures/p009-f2.png -->
<!-- figure: figures/p009-f3.png -->
<!-- figure: figures/p009-f4.png -->

**Rendszer időbeli fejlődése**

A zárt rendszer időbeli fejlődése **unitér**

transzformációval írható le, amely csak a kezdő és végállapottól függ. Adjungáltja megegyezik az inverzével. Sorok/oszlopok ortonormált bázist alkotnak. Kölcsönösen egyértelmű, hossztartó leképezés, ami megőrzi a belső szorzatot.

## s10 · p10 · PAULI-KAPUK
<!-- status: TODO view pages/p010.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p010-f1.png -->
<!-- figure: figures/p010-f2.png -->
<!-- figure: figures/p010-f3.png -->
<!-- figure: figures/p010-f4.png -->
<!-- figure: figures/p010-f5.png -->

Pauli X-kapu (bit-flip) :

Pauli Z-kapu (phase-flip) :

## s11 · p11 · PAULI-KAPUK
<!-- status: TODO view pages/p011.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p011-f1.png -->
<!-- figure: figures/p011-f2.png -->
<!-- figure: figures/p011-f3.png -->
<!-- figure: figures/p011-f4.png -->
<!-- figure: figures/p011-f5.png -->

Pauli Y-kapu:

Fázis-kapu:

## s12 · p12 · HADAMARD-KAPU
<!-- status: TODO view pages/p012.png -->
<!-- flags: math, graphic, image, stacked, table -->
<!-- figure: figures/p012-f1.png -->
<!-- figure: figures/p012-f2.png -->
<!-- figure: figures/p012-f3.png -->
<!-- figure: figures/p012-f4.png -->
<!-- figure: figures/p012-x82.png (raw layer) -->
<!-- figure: figures/p012-x83.png (raw layer) -->
<!-- figure: figures/p012-x84.png (raw layer) -->

Hadamard-kapu **unitér transzformáció** és **hermitikus** is, emiatt:

𝐻^(†) = 𝐻

𝐻^(−1) = 𝐻 𝐻^(†)𝐻= 𝐼

## s13 · p13 · BLOCH-GÖMB
<!-- status: TODO view pages/p013.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p013-f1.png -->
<!-- figure: figures/p013-f2.png -->

- https://bloch.kherb.io/
- https://www.justqlabs.com/simulator
𝜃

𝜃

2 ^(ȁۧ0) ^(+ 𝑒𝑖𝜙𝑠𝑖𝑛) 2 ^(ȁۧ1)
- ȁۧ𝜓= 𝑐𝑜𝑠

Links: <https://bloch.kherb.io/>, <https://www.justqlabs.com/simulator>

## s14 · p14 · III. POSZTULÁTUM
<!-- status: TODO view pages/p014.png -->
<!-- flags: math, graphic, image, table -->
<!-- figure: figures/p014-f1.png -->
<!-- figure: figures/p014-f2.png -->
<!-- figure: figures/p014-f3.png -->

**Mérés**

Legyen {𝑚} a mérés lehetséges eredményeinek a

halmaza. Egy mérés a mérési operátorok halmazával adható meg: {𝑀𝑚}. Ha a megmérendő rendszer állapota ȁۧφ akkor annak a valószínűsége, hogy a mérés az m eredményt adja:

Klasszikus világ

mérődoboz

Kvantumvilág

A mérés után a rendszer állapota az alábbi lesz:

## s15 · p15 · IV. POSZTULÁTUM
<!-- status: TODO view pages/p015.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p015-f1.png -->

**Összetett rendszer**

Ha V és Y a két kvantumrendszerhez rendelt Hilbert-tér, akkor az

ebből a két rendszerből álló összetett rendszerhez a 𝑊= 𝑉⨂𝑌Hilbert-tér rendelhető. Mire használható? Példa két kvantumbitből álló regiszterre:

ȁۧφ1 = ȁۧ0

ȁۧφ2 = ^(หۧ0) ^(+ ȁۧ1)
- 2
หۧφ = ȁۧ0 ⨂^(ȁۧ0) ^(+ ȁۧ1) = ^(หۧ00) ^(+ ȁۧ01)
  - 2
    - 2

## s16 · p16 · KVANTUMREGISZTER
<!-- status: TODO view pages/p016.png -->
<!-- flags: math, graphic, encoding -->
<!-- figure: figures/p016-f1.png -->
<!-- figure: figures/p016-f2.png -->
<!-- figure: figures/p016-f3.png -->
<!-- figure: figures/p016-f4.png -->
<!-- figure: figures/p016-f5.png -->
<!-- figure: figures/p016-f6.png -->
<!-- figure: figures/p016-f7.png -->
<!-- figure: figures/p016-f8.png -->
<!-- figure: figures/p016-f9.png -->
<!-- figure: figures/p016-f10.png -->

 = a 0 + b 1

 2

 = a 00 + b 01 + c 10 + d 11

 4

 = a 0000 + b 0001 + ... + o 1110 + p 1111

## s17 · p17 · SZÁMOLJUNK!
<!-- status: TODO view pages/p017.png -->
<!-- flags: math, graphic, layout -->
<!-- figure: figures/p017-f1.png -->
<!-- figure: figures/p017-f2.png -->
<!-- figure: figures/p017-f3.png -->
<!-- figure: figures/p017-f4.png -->
<!-- figure: figures/p017-f5.png -->
<!-- figure: figures/p017-f6.png -->

ȁۧ0 +ۧȁ1 ȁۧ𝟎𝟎+ۧȁ𝟎𝟏

ȁ0 ⊗

=

2

𝟐

ȁۧ1 +ۧȁ0 ȁۧ𝟎𝟏+ۧȁ𝟎𝟎

ȁ0 ⊗

=

2

𝟐

ȁۧ0 +ۧȁ1

ȁۧ𝟎𝟎+ۧȁ𝟏𝟎

⊗ȁ0 =
- 2ۧ
𝟐ۧ

ȁۧ0 +ۧȁ1 ȁ𝟏𝟎+ۧ ȁ𝟏𝟏

ȁ1 ⊗

=ۧ

2

𝟐

ȁۧ0 +ۧȁ1

ȁۧ𝟎𝟏+ۧȁ𝟏𝟏

⊗ȁ1 =

2ۧ

𝟐

ȁۧ0 +ۧȁ1 ȁۧ0 +ۧȁ1 ȁۧ𝟎𝟎+ۧȁ𝟎𝟏+ ȁۧ𝟏𝟎+ۧȁ𝟏𝟏

⊗

=

𝟐

2

2

(𝛼หۧ0 + 𝛽ȁۧ1 ) ⊗ȁۧ0 =𝜶หۧ𝟎𝟎+ 𝜷ȁۧ𝟏𝟎

ȁۧ0 ⊗𝛼หۧ0 + 𝛽ȁۧ1 = 𝜶หۧ𝟎𝟎+ 𝜷ȁۧ𝟎𝟏ۧ

## s18 · p18 · (no title)
<!-- status: TODO view pages/p018.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p018-f1.png -->

**Elválasztó fólia címmel**

**Kvantummechanikai posztulátumok**

**fizikusi interpretációja**

## s19 · p19 · A KVANTUMMECHANIKA POSZTULÁTUMAI FIZIKUS INTERPRETÁCIÓBAN
<!-- status: auto -->

**I.** **Posztulátum:** Minden kvantumrendszert egy hullámfüggvény, **Ψ(r,t)** ír

le, amely függ a térbeli koordinátáktól (r) és az időtől (t). Ez a függvény tartalmazza a rendszer összes mérhető információját.

**II.** **Posztulátum:** Minden fizikailag megfigyelhető (mint például az

energia, impulzus, pozíció) tulajdonságot egy hermitikus operátorral ábrázolunk. Ezek az operátorok a hullámfüggvényre hatva adják meg a megfigyelhető értékeit.

**III.** **Posztulátum:** Amikor egy kvantumrendszeren mérést végzünk, az

eredmény a megfelelő operátor egyik sajátértéke lesz. Egy adott sajátérték megfigyelésének valószínűségét a hullámfüggvénynek a megfelelő sajátállapotra vetített nagyságának négyzete határozza meg.

**IV.** **Posztulátum:** Méréskor a rendszer hullámfüggvénye „összeomlik” a

megfigyelt sajátértéknek megfelelő sajátállapotok egyikébe.

**V.** **Posztulátum:** A hullámfüggvény időbeli alakulását az időfüggő

Schrödinger-egyenlettel lehet leírni.

## s20 · p20 · (no title)
<!-- status: TODO view pages/p020.png -->
<!-- flags: graphic, image, no-text -->
<!-- figure: figures/p020-f1.png -->
<!-- figure: figures/p020-f2.png -->
<!-- figure: figures/p020-f3.png -->
