# bloch_gyak.pdf

<!-- 14 pages, 14 units, grouping: heuristic -->

## s1 · p1 · (no title)
<!-- status: TODO view pages/p001.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p001-f1.png -->
<!-- figure: figures/p001-f2.png -->

**Műveletek a Bloch-gömbön**

Kvantuminformatikai alkalmazások – Gyakorlat

**Dr. Solymos Balázs, Dr. Bacsárdi László, Dr. Imre Sándor** BME Hálózati Rendszerek és Szolgáltatások Tanszék solymosb@hit.bme.hu

## s2 · p2 · A KVANTUMMECHANIKA POSZTULÁTUMAI
<!-- status: TODO view pages/p002.png -->
<!-- flags: graphic, image, table -->
<!-- figure: figures/p002-f1.png -->

- 1. posztulátum: *kvantumbit*
  - Hilbert-tér
- 2. posztulátum: *logikai kapuk*
  - Unitér transzformáció
  - Elemi kvantum logikai kapuk
- 3. posztulátum: *Q/C átalakítás*
  - Mérési statisztika
  - Mérés utáni állapot
- 4. posztulátum: *regiszterek*
  - Tenzorszorzás

## s3 · p3 · 1ST POSTULATE (STATE SPACE)
<!-- status: auto -->

The actual state of any closed physical system can be described by means of a so called state vector **v** having complex coefficients and unit length in a Hilbert space V i.e. a complex linear vector space (state space) equipped with inner product.

**1.** **Állapotleírás**

**Zárt** fizikai rendszer aktuális állapota egy olyan állapotvektorral írható le, amely komplex együtthatókkal rendelkezik, egységnyi hosszú a H Hilbert-térben (egy komplex lineáris vektortérben, amelyben értelmezve van a belső szorzat).

## s4 · p4 · KVANTUMBIT (QUBIT)
<!-- status: TODO view pages/p004.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p004-f1.png -->
<!-- figure: figures/p004-f2.png -->
<!-- figure: figures/p004-f3.png -->
<!-- figure: figures/p004-f4.png -->
<!-- figure: figures/p004-f5.png -->

- Dirac ‘*ket*’ és ‘*bra*’ jelölés
- Kvantumbit: mindkét klasszikus állapotot (bázisállapotot)
tartalmazza egyidőben: szuperpozíció
- ahol a és b komplex valószínűségi amplitúdók. Abszolút érték
négyzetük adja meg a mérés eredményét (a klasszikus bázisban):
- Műveletek: belső és külső szorzat

## s5 · p5 · BLOCH-GÖMB (1)
<!-- status: TODO view pages/p005.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p005-f1.png -->

Egy kvantumbitet jelenít meg

## s6 · p6 · BLOCH-GÖMB (2)
<!-- status: TODO view pages/p006.png -->
<!-- flags: math, graphic, image, table, layout, encoding -->
<!-- figure: figures/p006-f1.png -->
<!-- figure: figures/p006-f2.png -->

- 0
z

a

𝛼

b 𝛽

x

1

Copyright © 2005 John Wiley & Sons Ltd.

 = a 0 + b 1

j

y

## s7 · p7 · PAULI-KAPUK
<!-- status: TODO view pages/p007.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p007-f1.png -->
<!-- figure: figures/p007-f2.png -->
<!-- figure: figures/p007-f3.png -->

Pauli-X (bit-flip) kapu:

## s8 · p8 · PAULI-KAPUK
<!-- status: TODO view pages/p008.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p008-f1.png -->

- Pauli X (bit-flip) gate:
- Pauli Z (phase-flip) gate:

## s9 · p9 · PAULI-KAPUK
<!-- status: TODO view pages/p009.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p009-f1.png -->
<!-- figure: figures/p009-f2.png -->
<!-- figure: figures/p009-f3.png -->
<!-- figure: figures/p009-f4.png -->

- Pauli Y (???-flip) gate:
- Geometrical interpretation of Pauli X gate: rotation
around axis x in the Bloch sphere

## s10 · p10 · FÁZIS-KAPU
<!-- status: TODO view pages/p010.png -->
<!-- flags: graphic, image, no-text -->
<!-- figure: figures/p010-f1.png -->
<!-- figure: figures/p010-f2.png -->
<!-- figure: figures/p010-f3.png -->

## s11 · p11 · HADAMARD-KAPU
<!-- status: TODO view pages/p011.png -->
<!-- flags: graphic, image, stacked -->
<!-- figure: figures/p011-f1.png -->
<!-- figure: figures/p011-f2.png -->
<!-- figure: figures/p011-f3.png -->
<!-- figure: figures/p011-f4.png -->
<!-- figure: figures/p011-x91.png (raw layer) -->
<!-- figure: figures/p011-x92.png (raw layer) -->
<!-- figure: figures/p011-x93.png (raw layer) -->
<!-- figure: figures/p011-x78.png (raw layer) -->

- Hadamard-kapu hermitikus:
,
- továbbá:

## s12 · p12 · HADAMARD-KAPU
<!-- status: TODO view pages/p012.png -->
<!-- flags: graphic, image, stacked, table -->
<!-- figure: figures/p012-f1.png -->
<!-- figure: figures/p012-f2.png -->
<!-- figure: figures/p012-f3.png -->
<!-- figure: figures/p012-f4.png -->
<!-- figure: figures/p012-f5.png -->
<!-- figure: figures/p012-x91.png (raw layer) -->
<!-- figure: figures/p012-x92.png (raw layer) -->
<!-- figure: figures/p012-x93.png (raw layer) -->
<!-- figure: figures/p012-x96.png (raw layer) -->
<!-- figure: figures/p012-x78.png (raw layer) -->

- Hadamard-kapu hermitikus:
,
- továbbá:
- Érdemes megjegyezni:

## s13 · p13 · HADAMARD-KAPU ÉS A SZUPERPOZÍCIÓ ELVE
<!-- status: TODO view pages/p013.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p013-f1.png -->

## s14 · p14 · BLOCH GÖMB FELADATOK
<!-- status: auto -->

Vizsgáljuk meg hol helyezkednek el az egyes bázisállapotok a gömbön!

Milyen régió tartozik a gömbön egy mérési eloszláshoz?

Milyen operációnak feleltethetőek meg a gömbön az egyes Pauli kapuk?

Vizsgáljuk meg, és lássuk be a következő egyenlőségeket: HH=I, XX=I, ZZ=I, HXH=Z, HZH=X
