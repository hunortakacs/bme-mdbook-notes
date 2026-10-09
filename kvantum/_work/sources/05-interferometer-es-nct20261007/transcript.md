# 05_INterferometer_es_NCT20261007.pdf

<!-- 50 pages, 50 units, grouping: heuristic -->

## s1 · p1 · (no title)
<!-- status: viewed pages/p001.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p001-f1.png -->
<!-- figure: figures/p001-f2.png -->

**A kvantuminterferométer működése és a No cloning tétel**

Kvantuminformatikai alkalmazások (BMEVIHIAD00)

2026/27. őszi félév

**Dr. Imre Sándor, Dr. Bacsárdi László**

BME Hálózati Rendszerek és Szolgáltatások Tanszék

imre@hit.bme.hu

Figure: title-slide decoration: the HIT logo ("HÁLÓZATI RENDSZEREK ÉS SZOLGÁLTATÁSOK TANSZÉK") over a grey network-graph background, and the Műegyetem 1782 building logo in the bottom right corner.
Use: none (decorative)

## s2 · p2 · ISMÉTLÉS
<!-- status: auto -->

## s3 · p3 · A KVANTUMMECHANIKA POSZTULÁTUMAI
<!-- status: viewed pages/p003.png -->
<!-- flags: math, graphic, image, table -->
<!-- figure: figures/p003-f1.png -->

- **1. Posztulátum:** *kvantum bit*
  - Hilbert-tér
- 2. Posztulátum: *logikai kapuk*
  - Unitér transzformáció
  - Elemi kvantum logikai kapuk
- 3. Posztulátum: *Q/C átalakítás*
  - Mérési statisztika
  - Mérés utáni állapot
- **4. Posztulátum:** *regiszterek*
  - Tenzor szorzás

To the right of the list, one boxed formula (pasted picture) beside each postulate:

- beside 1. Posztulátum (red box):

  $$|\varphi\rangle = \sum_{i=0}^{2^n-1} \varphi_i |i\rangle$$

- beside 2. Posztulátum (blue box):

  $$U^\dagger \equiv U^{-1}$$

- beside 3. Posztulátum (orange box), first beside "Mérési statisztika", then beside "Mérés utáni állapot":

  $$P(m \mid |\varphi\rangle) = \langle\varphi|M_m^\dagger M_m|\varphi\rangle$$

  $$|\varphi'\rangle = \frac{M_m|\varphi\rangle}{\sqrt{\langle\varphi|M_m^\dagger M_m|\varphi\rangle}}$$

- beside 4. Posztulátum (green box):

  $$|\varphi\rangle = |0\rangle \otimes \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$

<!-- note: there is no table on the slide; the table flag comes from the formula boxes -->

## s4 · p4 · (no title)
<!-- status: viewed pages/p004.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p004-f1.png -->

**Projektív mérés (Neumann-mérés)**

“Projective geometry has opened up for us with the greatest facility new territories in our science, and has rightly been called the royal road to our particular field of knowledge.”

Felix Klein

Figure: section-divider decoration: grey network-graph background at the top of the slide.
Use: none (decorative)

## s5 · p5 · MÉRÉS FIZIKAILAG
<!-- status: viewed pages/p005.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p005-setup.png -->
<!-- figure: figures/p005-f2.png -->

Figure: optical setup for measuring polarization. From the left, a wide hollow red arrow (the beam) carries a mix of photons drawn as small double arrows: vertical (↕), horizontal (↔), vertical, vertical, horizontal. It enters a blue square cube with a diagonal line from top left to bottom right, labelled "Polarizáló nyalábosztó". To the right of the cube a hollow arrow with a horizontal double arrow (↔) inside leads to a black D-shaped detector marked "0", labelled "Egyfoton detektor 0", with a cable leaving it; above this path, in italics: "*Vízszintesen polarizált fotonokat átengedi →*". Below the cube a downward hollow arrow with a vertical double arrow (↕) inside leads to a black detector marked "1", labelled "Egyfoton detektor 1", with a cable; to the left of this path, in italics: "*Függőlegesen polarizált fotonokat letükrözi ↓*".
Use: image figures/p005-setup.png

To the right of detector 0:

$$|\leftrightarrow\rangle = |0\rangle$$

Below detector 1:

$$|\updownarrow\rangle = |1\rangle$$

## s6 · p6 · PROJEKTÍV MÉRÉS KONSTRUÁLÁSA
<!-- status: viewed pages/p006.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p006-f1.png -->
<!-- figure: figures/p006-f2.png -->
<!-- figure: figures/p006-f3.png -->
<!-- figure: figures/p006-f4.png -->
<!-- figure: figures/p006-f5.png -->
<!-- figure: figures/p006-f6.png -->

Ellenőrizzük a teljességi relációt

$$\sum_m \mathbf{M}_m^\dagger \mathbf{M}_m = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \mathbf{I}$$

Dirac-jelöléssel

$$M_0 = |0\rangle\langle 0| \text{ and } M_1 = |1\rangle\langle 1|$$

Végkövetkeztetés

Thus we reached a very simple and practical rule of thumb: *In case we have a set of orthonormal states $\{|\varphi_m\rangle\}$ then the corresponding measurement operators which provide exact differentiation among them can be produced by $M_m = |\varphi_m\rangle\langle\varphi_m|$.*

<!-- note: the quoted paragraph is a pasted book excerpt in English; "orthonormal states {|φm⟩}" and "Mm = |φm⟩⟨φm|" are underlined in red on the slide -->

## s7 · p7 · PROJEKTOROK TULAJDONSÁGAI
<!-- status: viewed pages/p007.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p007-f1.png -->
<!-- figure: figures/p007-f2.png -->

$$M_m \;\longrightarrow\; P_m = |\varphi_m\rangle\langle\varphi_m|$$

<!-- note: the arrow is a blue block arrow from M_m to P_m -->

1. Obviously they are self-adjoint operators $P_m^\dagger \equiv P_m$ since $(|\varphi_m\rangle\langle\varphi_m|)^\dagger = \langle\varphi_m|^\dagger|\varphi_m\rangle^\dagger = |\varphi_m\rangle\langle\varphi_m|$.
2. Furthermore $P_m P_m = |\varphi_m\rangle \underbrace{\langle\varphi_m||\varphi_m\rangle}_{\equiv 1} \langle\varphi_m| = P_m$.
3. Finally they are orthogonal which means $P_m P_n = |\varphi_m\rangle \underbrace{\langle\varphi_m||\varphi_n\rangle}_{\equiv 1 \mathrm{or} 0} \langle\varphi_n| = \delta(m-n)P_m$.

## s8 · p8 · MÉRÉS PROJEKTOROKKAL
<!-- status: viewed pages/p008.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p008-f1.png -->
<!-- figure: figures/p008-f2.png -->
<!-- figure: figures/p008-f3.png -->
<!-- figure: figures/p008-f4.png -->

$$P(m \mid |\varphi\rangle) = \langle\varphi|P_m|\varphi\rangle$$

$$|\varphi'\rangle = \frac{P_m|\varphi\rangle}{\sqrt{\langle\varphi|P_m|\varphi\rangle}}$$

$$\sum_m P_m \equiv I$$

**Exercise 3.1.** Construct the measurement operators providing sure success in case of the following set $|\varphi_0\rangle = \frac{|0\rangle+|1\rangle}{\sqrt{2}}$ and $|\varphi_1\rangle = \frac{|0\rangle-|1\rangle}{\sqrt{2}}$!

## s9 · p9 · MÉRÉS A BÁZISÁLLAPOTOK SZERINT
<!-- status: viewed pages/p009.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p009-f1.png -->
<!-- figure: figures/p009-x95.png (raw layer) -->
<!-- figure: figures/p009-x96.png (raw layer) -->
<!-- figure: figures/p009-x97.png (raw layer) -->
<!-- figure: figures/p009-x99.png (raw layer) -->
<!-- figure: figures/p009-x100.jpeg (raw layer) -->

- Let us check what we have learned by means of a simple example

  $$|\varphi\rangle = a|0\rangle + b|1\rangle$$

- Basis vectors $|0\rangle$ and $|1\rangle$

  $$\begin{array}{rcc} & & \begin{bmatrix} a \\ b \end{bmatrix} \\ P(0 \mid |\varphi\rangle) = \langle\varphi|P_0|\varphi\rangle = & \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} & \begin{bmatrix} a \\ 0 \end{bmatrix} \\ & \begin{bmatrix} a^* & b^* \end{bmatrix} & |a|^2 \end{array}$$

  A blue block arrow below this formula points up at it.

- Measurement statistic

  A blue block arrow below this bullet points down at the next formula.

  $$\begin{array}{rcc} & & \begin{bmatrix} a \\ b \end{bmatrix} \\ P(1 \mid |\varphi\rangle) = \langle\varphi|P_0|\varphi\rangle = & \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} & \begin{bmatrix} 0 \\ b \end{bmatrix} \\ & \begin{bmatrix} a^* & b^* \end{bmatrix} & |b|^2 \end{array}$$

<!-- note: both P(·|φ) formulas are pasted pictures laid out as a multiplication scheme: the input column [a; b] stands above the product column, the row vector [a* b*] under the matrix, the result under the product column -->
<!-- suspect: the second formula reads P(1 | |φ⟩) = ⟨φ|P_0|φ⟩ although the matrix used is P_1 = [[0,0],[0,1]]; should be ⟨φ|P_1|φ⟩ -->

Handwritten photo (red marker on paper) at the top right, beside the first two bullets, in the same multiplication scheme (the row vector stands above the result matrix):

$$\begin{array}{rcc} & & \begin{bmatrix} 1 & 0 \end{bmatrix} \\ P_0 = |0\rangle\langle 0| = & \begin{bmatrix} 1 \\ 0 \end{bmatrix} & \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \end{array}$$

$$\begin{array}{rcc} & & \begin{bmatrix} 0 & 1 \end{bmatrix} \\ P_1 = |1\rangle\langle 1| = & \begin{bmatrix} 0 \\ 1 \end{bmatrix} & \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \end{array}$$

## s10 · p10 · ÁLTALÁNOS ÉS PROJEKTÍV MÉRÉS KAPCSOLATA
<!-- status: viewed pages/p010.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p010-f1.png -->
<!-- figure: figures/p010-f2.png -->

Figure: quantum circuit in a framed box. Two groups of wires (each a bundle of horizontal lines with a vertical "⋮" marking further lines) enter from the left: the upper group labelled $|\varphi_k\rangle$, the lower group labelled $|\gamma\rangle$. Both groups enter one large box labelled $U$. Between $U$ and the next box all wires continue (with "⋮" marks); above them the label $|\psi_k\rangle$. The wires then enter a box drawn as a meter: a dial arc with points labelled 0, 1, 2, 3, 4 and a needle pointing at 3, with the word "Projective" under it. All wires leave the meter box on the right (with "⋮" marks).
Use: image figures/p010-f1.png

Copyright © 2005 John Wiley & Sons Ltd.

**Neumark-kiterjesztés**: bármely általános mérést végre tudjuk hajtani projektív mérésként + kiegészítő kvantumbitek + unitér transzformáció

- Mérhetőség (megkülönböztethetőség)

  ↕ (a blue two-headed vertical block arrow connects the two bullets)

- Másolhatóság (következő előadáson!)

## s11 · p11 · (no title)
<!-- status: viewed pages/p011.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p011-f1.png -->

**Pozitív Operátor Értékű Mérés (POVM Operator Valued Measurements)**

**KITEKINTÉS**

Figure: section-divider decoration: grey network-graph background at the top of the slide.
Use: none (decorative)

## s12 · p12 · POVM
<!-- status: auto -->

- Mit tegyünk ha a megkülönböztetetendő állapotok nem
merőlegesek?
- No cloning tétel (következő óra): ilyen állapotokat nem
lehet egyértelműen/biztonságosan megkülönböztetni!
- De mégis van olyan mérés konstrukció, ami kezelhetővé
teszi az ilyen eseteket. Ez a POVM konstrukció.

## s13 · p13 · PROJEKTÍV PÉLDA
<!-- status: viewed pages/p013.png -->
<!-- flags: math, graphic, image, stacked, table, layout -->
<!-- figure: figures/p013-f1.png -->
<!-- figure: figures/p013-f2.png -->
<!-- figure: figures/p013-f3.png -->
<!-- figure: figures/p013-x112.jpeg (raw layer) -->
<!-- figure: figures/p013-x113.png (raw layer) -->
<!-- figure: figures/p013-x114.png (raw layer) -->
<!-- figure: figures/p013-x115.jpeg (raw layer) -->
<!-- figure: figures/p013-x116.jpeg (raw layer) -->
<!-- figure: figures/p013-x117.png (raw layer) -->
<!-- figure: figures/p013-x119.png (raw layer) -->
<!-- figure: figures/p013-x121.png (raw layer) -->

- Ortogonális állapotok megkülönböztetése.
- Állatkert: madarak és emlősök
- Mérődoboz konstruálása – direkt megközelítés:
  - $D_0 =$ Ha tojás pottyan ki belőle, akkor madár
  - $D_1 =$ Ha szőrös, akkor emlős

Boxed note (red frame, left, between the two sub-items):

> Skálaérték: emlős, madár
>
> Mért fizikai tulajdonság: szőrős, tojást pottyant

Figure: two clip-art groups illustrating the classes: a sheet of cartoon birds (layer x116) stands beside the box, next to the $D_0$ item (madár); six cartoon mammal heads (beaver, fox, rabbit, deer, wolf, another fox; layer x115) stand under the $D_1$ item (emlős). The Budapest Zoo logo (green elephant on an orange arch, "BUDAPEST ZOO"; layer x112) is at the top right.
Use: none (decorative)

Figure: vector diagram at the right: a red arrow pointing straight up, labelled "szőrös" at its tip, and a green arrow pointing to the right, labelled "tojást pottyant" below its tip; the two arrows start from the same point and are perpendicular. A black quarter-circle arc joins the tip of the red arrow to the tip of the green arrow.
Use: redraw

<!-- note: layers x113 and x114 are the formula pictures "D_1 =" and "D_0 ="; layers x117, x119, x121 are plain black rectangles (masks of the arrows), no content. There is no table on the slide; the table flag comes from the boxed note -->

## s14 · p14 · POVM PÉLDA
<!-- status: viewed pages/p014.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p014-f1.png -->
<!-- figure: figures/p014-f2.png -->

- Nem ortogonális állapotok megkülönböztetése.
- Megérkezik egy rakás kacsacsőrű emlős az állatkertbe, a madarak pedig délre költöznek.
- A projektív mérés eredményéből nem következtethetünk biztosan, mert a “szőrős” válasz nem igazít el bennünket

Figure: left, the six cartoon mammal heads and the sheet of cartoon birds (as on the previous slide) joined by a blue two-headed horizontal block arrow (↔).
Use: none (decorative)

Figure: vector diagram at the right: black axes, the vertical one labelled "szőrös" at its tip, the horizontal one labelled "tojást pottyant" below its tip, both arrows. A red arrow starts at the origin and points up and to the right at 45°, between the two axes. At the tip of the red arrow is a photo of two baby platypuses (kacsacsőrű emlős) held in hands.
Use: redraw

## s15 · p15 · POVM PÉLDA
<!-- status: viewed pages/p015.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p015-f1.png -->
<!-- figure: figures/p015-f2.png -->
<!-- figure: figures/p015-f3.png -->

- Mérődoboz konstruálása – indirekt megközelítés (a mérőoperátorok merőlegesek a lehetséges állapotra):
  - $D_0 =$ Vagy nem szőrös vagy nem tojás potyog belője (merőleges a „szőrös és tojás potyog belőle”-re), akkor emlős
  - $D_1 =$ Ha tojás pottyan ki belőle (merőleges a szőrősre), akkor kacsacsőrű emlős
  - $D_2 = I - D_0 - D_1$

<!-- suspect: "belője" in the D_0 item looks like a typo of "belőle" (the same item later says "belőle") -->

Figure: photo of two baby platypuses held in two hands, watermark "vicces-kepek.blogspot.com", at the bottom right.
Use: none (decorative)

## s16 · p16 · (no title)
<!-- status: viewed pages/p016.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p016-f1.png -->
<!-- figure: figures/p016-f2.png -->

**A kvantuminterferométer működése**

**Dr. Imre Sándor, Dr. Bacsárdi László**

BME Hálózati Rendszerek és Szolgáltatások Tanszék

imre@hit.bme.hu

Figure: section title-slide decoration: the HIT logo over a grey network-graph background, and the Műegyetem 1782 building logo in the bottom right corner.
Use: none (decorative)

## s17 · p17 · EGY EGYSZERŰ KÍSÉRLET
<!-- status: viewed pages/p017.png -->
<!-- flags: graphic, image, stacked, layout -->
<!-- figure: figures/p017-f1.png -->
<!-- figure: figures/p017-f2.png -->
<!-- figure: figures/p017-x138.jpeg (raw layer) -->
<!-- figure: figures/p017-x140.jpeg (raw layer) -->
<!-- figure: figures/p017-x143.jpeg (raw layer) -->

Figure: a probabilistic two-input, two-output box. Two horizontal lines (wires) run from left to right through a beige rounded box; the upper wire is labelled "0" on both the left and the right end, the lower wire "1" on both ends. Inside the box each wire has a light-blue node at its entry and at its exit. Four edges join the entry nodes to the exit nodes: the straight upper edge (entry 0 to exit 0) labelled $p_{00}$ above it; the straight lower edge (entry 1 to exit 1) labelled $p_{11}$ below it; two crossing diagonals, entry 0 to exit 1 and entry 1 to exit 0, with the label $p_{10}$ at the lower left (beside the rising diagonal from entry 1) and $p_{01}$ at the right (beside the falling diagonal towards exit 1). On the left, a blue smiley stands at input 0 and another blue smiley at input 1. A cartoon boy lies on top of the box.
Use: redraw

Figure: photo at the right edge of the slide: a hand flipping a coin, the coin shown in several positions in the air on a black background (a coin toss).
Use: none (decorative)

<!-- note: the cartoon boy (layer x138), the beige paper texture of the box (layer x140) and the coin-toss photo (layer x143) are the stacked layers -->

## s18 · p18 · EGY EGYSZERŰ KÍSÉRLET
<!-- status: viewed pages/p018.png -->
<!-- flags: math, graphic, image, stacked, table, layout, encoding -->
<!-- figure: figures/p018-f1.png -->
<!-- figure: figures/p018-x138.jpeg (raw layer) -->
<!-- figure: figures/p018-x138.jpeg (raw layer) -->
<!-- figure: figures/p018-x147.jpeg (raw layer) -->
<!-- figure: figures/p018-x140.jpeg (raw layer) -->
<!-- figure: figures/p018-x140.jpeg (raw layer) -->

Formula in a grey marble-textured box at the top:

$$P_{00} = p_{00} \cdot p_{00} + p_{01} \cdot p_{10} = 0.5 \neq 0$$

Figure: two of the probabilistic boxes of the previous slide connected in series. The wires "0" (upper) and "1" (lower) run through the first box and continue into the second; the labels 0/1 stand at the input, between the boxes, and at the output. Each box has the same four edges as before: $p_{00}$ (upper straight), $p_{11}$ (lower straight), and the crossing diagonals labelled $p_{10}$ (lower left) and $p_{01}$ (right). A cartoon boy lies on top of each box. A single blue smiley stands on the left, at input 0.
Use: redraw

<!-- note: layers: cartoon boy (x138, twice), marble texture of the formula box (x147), paper texture of the boxes (x140, twice) -->

## s19 · p19 · EGY EGYSZERŰ KÍSÉRLET
<!-- status: viewed pages/p019.png -->
<!-- flags: graphic, image, stacked, layout -->
<!-- figure: figures/p019-beamsplitter.png -->
<!-- figure: figures/p019-x157.jpeg (raw layer) -->
<!-- figure: figures/p019-x159.jpeg (raw layer) -->
<!-- figure: figures/p019-x147.jpeg (raw layer) -->
<!-- figure: figures/p019-x147.jpeg (raw layer) -->
<!-- figure: figures/p019-x147.jpeg (raw layer) -->
<!-- figure: figures/p019-x147.jpeg (raw layer) -->
<!-- figure: figures/p019-x162.jpeg (raw layer) -->
<!-- figure: figures/p019-x164.png (raw layer) -->
<!-- figure: figures/p019-x157.jpeg (raw layer) -->
<!-- figure: figures/p019-x162.jpeg (raw layer) -->
<!-- figure: figures/p019-x164.png (raw layer) -->
<!-- figure: figures/p019-x159.jpeg (raw layer) -->
<!-- figure: figures/p019-x169.png (raw layer) -->
<!-- figure: figures/p019-x171.png (raw layer) -->
<!-- figure: figures/p019-x138.jpeg (raw layer) -->
<!-- figure: figures/p019-x140.jpeg (raw layer) -->

Figure: a half-silvered mirror as a random switch. A light-blue smiley on the left sends a pink block arrow labelled "0" to the right; a second pink block arrow labelled "1" points up from below. Both arrows point at a grey marble-textured slab placed diagonally (from lower left to upper right), the beam splitter. Above the slab is a measuring instrument (photo of an electronic instrument) with a box labelled "0" on top of it, and beside it "$p$ = 0.5" in red. To the right of the slab is a second instrument with a box labelled "1" on top, and "$p$ = 0.5" in red under it. At the top right, a parchment scroll shows the probabilistic box of the previous slides (crossing edges, no labels) with the cartoon boy on top.
Use: image figures/p019-beamsplitter.png

<!-- note: layers: instrument photo (x157), texture fills of the smiley, arrows, slab and scroll (x159, x162, x164, x169, x171), marble (x147), cartoon boy (x138), paper (x140) -->

## s20 · p20 · EGY EGYSZERŰ KÍSÉRLET
<!-- status: viewed pages/p020.png -->
<!-- flags: graphic, image, stacked, table -->
<!-- figure: figures/p020-interferometer.png -->
<!-- figure: figures/p020-x159.jpeg (raw layer) -->
<!-- figure: figures/p020-x157.jpeg (raw layer) -->
<!-- figure: figures/p020-x147.jpeg (raw layer) -->
<!-- figure: figures/p020-x147.jpeg (raw layer) -->
<!-- figure: figures/p020-x147.jpeg (raw layer) -->
<!-- figure: figures/p020-x147.jpeg (raw layer) -->
<!-- figure: figures/p020-x162.jpeg (raw layer) -->
<!-- figure: figures/p020-x164.png (raw layer) -->
<!-- figure: figures/p020-x157.jpeg (raw layer) -->
<!-- figure: figures/p020-x147.jpeg (raw layer) -->
<!-- figure: figures/p020-x147.jpeg (raw layer) -->
<!-- figure: figures/p020-x147.jpeg (raw layer) -->
<!-- figure: figures/p020-x147.jpeg (raw layer) -->
<!-- figure: figures/p020-x159.jpeg (raw layer) -->
<!-- figure: figures/p020-x162.jpeg (raw layer) -->
<!-- figure: figures/p020-x164.png (raw layer) -->
<!-- figure: figures/p020-x169.png (raw layer) -->
<!-- figure: figures/p020-x171.png (raw layer) -->
<!-- figure: figures/p020-x138.jpeg (raw layer) -->
<!-- figure: figures/p020-x138.jpeg (raw layer) -->
<!-- figure: figures/p020-x140.jpeg (raw layer) -->
<!-- figure: figures/p020-x140.jpeg (raw layer) -->

Figure: a Mach–Zehnder interferometer built from two half-silvered mirrors. Bottom left: a light-blue smiley sends a pink block arrow "0" to the right, and a pink block arrow "1" points up from below; both hit a grey diagonal half-silvered mirror (lower left corner of a rectangle). The light paths form a rectangle drawn with thin lines: from the lower-left mirror one path goes up to a black full mirror at the upper left corner, the other goes right to a black full mirror at the lower right corner; both paths meet at a second grey half-silvered mirror at the upper right corner. Beyond it are two measuring instruments: one above it labelled "0", one to its right labelled "1". Inside the rectangle: "Mit várunk?". At the top left, a parchment scroll shows two probabilistic boxes in series (each with crossing edges and a cartoon boy on top).
Use: image figures/p020-interferometer.png

<!-- note: layers are the same instrument photo, textures, cartoon boy and paper as on the previous slides -->

## s21 · p21 · EGY EGYSZERŰ KÍSÉRLET
<!-- status: viewed pages/p021.png -->
<!-- flags: math, graphic, image, stacked, table -->
<!-- figure: figures/p021-interferometer.png -->
<!-- figure: figures/p021-x159.jpeg (raw layer) -->
<!-- figure: figures/p021-x157.jpeg (raw layer) -->
<!-- figure: figures/p021-x147.jpeg (raw layer) -->
<!-- figure: figures/p021-x147.jpeg (raw layer) -->
<!-- figure: figures/p021-x147.jpeg (raw layer) -->
<!-- figure: figures/p021-x147.jpeg (raw layer) -->
<!-- figure: figures/p021-x157.jpeg (raw layer) -->
<!-- figure: figures/p021-x147.jpeg (raw layer) -->
<!-- figure: figures/p021-x147.jpeg (raw layer) -->
<!-- figure: figures/p021-x147.jpeg (raw layer) -->
<!-- figure: figures/p021-x147.jpeg (raw layer) -->
<!-- figure: figures/p021-x159.jpeg (raw layer) -->
<!-- figure: figures/p021-x162.jpeg (raw layer) -->
<!-- figure: figures/p021-x164.png (raw layer) -->
<!-- figure: figures/p021-x162.jpeg (raw layer) -->
<!-- figure: figures/p021-x164.png (raw layer) -->
<!-- figure: figures/p021-x169.png (raw layer) -->
<!-- figure: figures/p021-x171.png (raw layer) -->
<!-- figure: figures/p021-x138.jpeg (raw layer) -->
<!-- figure: figures/p021-x138.jpeg (raw layer) -->
<!-- figure: figures/p021-x140.jpeg (raw layer) -->
<!-- figure: figures/p021-x140.jpeg (raw layer) -->
<!-- figure: figures/p021-x147.jpeg (raw layer) -->

Figure: the same Mach–Zehnder interferometer as on the previous slide (smiley with input arrows "0" and "1", lower-left and upper-right half-silvered mirrors, black full mirrors at the upper left and lower right, the scroll with two boxes in series at the top left). Changes: a light-blue smiley sits on the upper-right half-silvered mirror; the instrument labelled "0" has a bright green frame; the instrument labelled "1" is crossed out with a big dark-blue X. Inside the rectangle, in a grey marble-textured box, the formula:

$$P_{00} = p_{00} \cdot p_{00} + p_{01} \cdot p_{10} = 0!$$

Use: image figures/p021-interferometer.png

<!-- note: the text layer also holds "Mit történik?", which is not visible on the slide (covered by the formula box) -->
<!-- suspect: the formula says the probability of output 0 is 0, but the figure highlights detector 0 in green and crosses out detector 1; either the formula or the highlighting seems reversed -->

## s22 · p22 · (no title)
<!-- status: viewed pages/p022.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p022-f1.png -->

***Az interferométer általános leírása***

*"An idea is always a generalization, and generalization is a property of thinking. To generalize means to think."*

Georg Hegel

Figure: section-divider decoration: grey network-graph background at the top of the slide.
Use: none (decorative)

## s23 · p23 · FÉLIGÁTERESZTŐ TÜKÖR (HALFSILVERED MIRROR,
<!-- status: viewed pages/p023.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p023-beamsplitter.png -->

<!-- note: the full slide title is "FÉLIGÁTERESZTŐ TÜKÖR (HALFSILVERED MIRROR, BEAMSPLITTER)" -->

Figure: a single beam splitter (framed drawing). A grey textured slab, the beam splitter, stands diagonally (lower left to upper right) inside a dash-dotted square. An input $|0\rangle$ comes from the left (solid arrow pointing right into the slab) and an input $|1\rangle$ comes from below (solid arrow pointing up into the slab). Two dashed outputs leave the square: one going up, labelled $|0\rangle$, ending in an arrow at a detector "D" at the top; one going right, labelled $|1\rangle$, ending in an arrow at a detector "D" on the right. A legend box at the upper right: "Legend", a grey textured bar = "Beam splitter", an octagon with "D" = "Detector".
Use: image figures/p023-beamsplitter.png

Copyright © 2005 John Wiley & Sons Ltd.

## s24 · p24 · 2 FÉLIGÁTERSZTŐ TÜKÖR MINT AZONOSSÁG TRANSZFORMÁCIÓ
<!-- status: viewed pages/p024.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p024-two-beamsplitters.png -->

<!-- suspect: the title reads "FÉLIGÁTERSZTŐ" (an E missing; slide 23 has "FÉLIGÁTERESZTŐ") -->

Figure: two beam splitters forming an interferometer (framed drawing). Lower left: a beam splitter in a dash-dotted square; input $|0\rangle$ from the left (solid arrow), $|1\rangle$ written below the square. From it a dashed path labelled $|0\rangle$ goes up to a white mirror at the upper left, which reflects it to the right; a dashed path labelled $|1\rangle$ goes right to a white mirror at the lower right, which reflects it up. Both paths meet at a second beam splitter in a dash-dotted square at the upper right. From there a solid arrow goes up to a detector "D" labelled $|0\rangle$. A second detector "D" labelled $|1\rangle$ stands to the right of the upper beam splitter, with no line reaching it. Legend box at the bottom: grey textured bar = "Beam splitter", white bar = "Mirror", octagon "D" = "Detector".
Use: image figures/p024-two-beamsplitters.png

Copyright © 2005 John Wiley & Sons Ltd.

## s25 · p25 · 2 FÉLIGÁTERSZTŐ TÜKÖR MINT AZONOSSÁG TRANSZFORMÁCIÓ
<!-- status: viewed pages/p025.png -->
<!-- flags: graphic -->
<!-- figure: figures/p025-f1.png -->

<!-- suspect: the title reads "FÉLIGÁTERSZTŐ" (an E missing) -->

- A két tükör közé elhelyezett extra detektorok ismét véletlenszerűvé teszik az eredményt.

  ⇓ (a light-blue block arrow points down to the next item)

- Megjegyzés: A mérések jellemzően befolyásolják a megfigyelt rendszert, és így magukat a mérési eredményeket is.
- Az „elektromágneses hullámokkal történő megfigyelés (mérés)” paradoxona: Kis részlétek kis hullámhosszal figyelhetők meg. Minél kisebb a hullámhossz, annál nagyobb a frekvencia és így a foton energiája, tehát a egyre nagyobb a foton hatása a megfigyelt objektumra.

<!-- suspect: "Kis részlétek" looks like a typo of "részletek"; "tehát a egyre nagyobb" has a stray "a" -->

Copyright © 2005 John Wiley & Sons Ltd.

## s26 · p26 · ÁLTALÁNOSÍTOTT INTERFEROMÉTER
<!-- status: viewed pages/p026.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p026-f1.png -->

Figure: generalized interferometer (framed drawing). Lower left: a beam splitter labelled $H$ in a dash-dotted square; inputs $|0\rangle$ from the left and $|1\rangle$ from below (solid arrows). Its output $|0\rangle$ goes up (dashed) to a white mirror at the upper left, then right along the upper path; its output $|1\rangle$ goes right (dashed) along the lower path to a white mirror at the lower right, then up. A dashed rectangle labelled $P$ in the middle spans both paths: on the upper path a sheet of glass $\alpha_0$, on the lower path a sheet of glass $\alpha_1$. Both paths meet at a second beam splitter labelled $H$ in a dash-dotted square at the upper right; from it a solid arrow goes up to a detector "D" labelled $|0\rangle$, and a solid arrow goes right to a detector "D" labelled $|1\rangle$. Legend box at the bottom: grey textured bar = "Beam splitter", white bar = "Mirror", octagon "D" = "Detector", rounded square $\alpha$ = "Sheet of glass".
Use: image figures/p026-f1.png

Copyright © 2005 John Wiley & Sons Ltd.

<!-- note: from this page on, the slide footer number is one higher than the PDF page (27 here) -->

## s27 · p27 · ÁRAMKÖRI LEÍRÁS
<!-- status: viewed pages/p027.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p027-f1.png -->
<!-- figure: figures/p027-f2.png -->
<!-- figure: figures/p027-f3.png -->
<!-- figure: figures/p027-f4.png -->

Figure: quantum circuit in a framed box: a single wire starting with $|0\rangle$ on the left, passing through three boxes in order $H$, $P$, $H$, and ending on the right. Under the wire four upward arrows mark the states: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

$$\mathbf{H} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \qquad \mathbf{P} = \begin{bmatrix} e^{j\alpha_0} & 0 \\ 0 & e^{j\alpha_1} \end{bmatrix}$$

## s28 · p28 · ELEMZÉS (1)
<!-- status: viewed pages/p028.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p028-f1.png -->

Figure: quantum circuit in a framed box: a single wire starting with $|0\rangle$ on the left, passing through three boxes in order $H$, $P$, $H$, and ending on the right. Under the wire four upward arrows mark the states: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.
A vertical red line crosses the circuit at $|\varphi_0\rangle$ (before the first $H$).
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

$$|\varphi_0\rangle = |0\rangle$$

## s29 · p29 · ELEMZÉS (2)
<!-- status: viewed pages/p029.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p029-f1.png -->

Figure: quantum circuit in a framed box: a single wire starting with $|0\rangle$ on the left, passing through three boxes in order $H$, $P$, $H$, and ending on the right. Under the wire four upward arrows mark the states: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.
A vertical red line crosses the circuit at $|\varphi_1\rangle$ (between $H$ and $P$).
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

$$\begin{array}{rcc} & & \begin{bmatrix} 1 \\ 0 \end{bmatrix} \\ |\varphi_1\rangle = H|\varphi_0\rangle = & \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} & \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix} \end{array}$$

<!-- note: multiplication scheme as on slide 9: the input column [1; 0] stands above the result column -->

## s30 · p30 · ELEMZÉS (3)
<!-- status: viewed pages/p030.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p030-f1.png -->

Figure: quantum circuit in a framed box: a single wire starting with $|0\rangle$ on the left, passing through three boxes in order $H$, $P$, $H$, and ending on the right. Under the wire four upward arrows mark the states: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.
A vertical red line crosses the circuit at $|\varphi_2\rangle$ (between $P$ and the second $H$).
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

$$\begin{array}{rcc} & & \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix} \\ |\varphi_2\rangle = P|\varphi_1\rangle = & \begin{bmatrix} e^{j\alpha_0} & 0 \\ 0 & e^{j\alpha_1} \end{bmatrix} & \begin{bmatrix} \frac{e^{j\alpha_0}}{\sqrt{2}} \\ \frac{e^{j\alpha_1}}{\sqrt{2}} \end{bmatrix} \end{array}$$

<!-- note: multiplication scheme: the input column stands above the result column -->

## s31 · p31 · ELEMZÉS (4)
<!-- status: viewed pages/p031.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p031-f1.png -->

Figure: quantum circuit in a framed box: a single wire starting with $|0\rangle$ on the left, passing through three boxes in order $H$, $P$, $H$, and ending on the right. Under the wire four upward arrows mark the states: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.
A vertical red line crosses the circuit at $|\varphi_3\rangle$ (after the second $H$).
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

$$\begin{array}{rcc} & & \begin{bmatrix} \frac{e^{j\alpha_0}}{\sqrt{2}} \\ \frac{e^{j\alpha_1}}{\sqrt{2}} \end{bmatrix} \\ |\varphi_3\rangle = H|\varphi_2\rangle = & \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} & \begin{bmatrix} \frac{e^{j\alpha_0}+e^{j\alpha_1}}{2} \\ \frac{e^{j\alpha_0}-e^{j\alpha_1}}{2} \end{bmatrix} \end{array}$$

<!-- note: multiplication scheme: the input column stands above the result column -->

## s32 · p32 · ELEMZÉS (5)
<!-- status: viewed pages/p032.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p032-f1.png -->

$$\begin{aligned} |\varphi_3\rangle &= \frac{e^{j\alpha_0} + e^{j\alpha_1}}{2}|0\rangle + \frac{e^{j\alpha_0} - e^{j\alpha_1}}{2}|1\rangle \\ &= e^{j\frac{\alpha_0+\alpha_1}{2}} \left( \frac{e^{j\frac{\alpha_0-\alpha_1}{2}} + e^{-j\frac{\alpha_0-\alpha_1}{2}}}{2}|0\rangle + \frac{e^{j\frac{\alpha_0-\alpha_1}{2}} - e^{-j\frac{\alpha_0-\alpha_1}{2}}}{2}|1\rangle \right) \end{aligned}$$

$$\Delta\alpha \triangleq \alpha_0 - \alpha_1$$

$$\frac{e^{j\Delta\alpha}+e^{-j\Delta\alpha}}{2} = \cos(\Delta\alpha) \qquad \frac{e^{j\Delta\alpha}-e^{-j\Delta\alpha}}{2j} = \sin(\Delta\alpha)$$

$$P_0 = \cos^2\left(\frac{\Delta\alpha}{2}\right) = (1+\cos(\Delta\alpha))\frac{1}{2}, \qquad \Delta\alpha = 0$$

: ideális eset

$$P_1 = \sin^2\left(\frac{\Delta\alpha}{2}\right) = (1-\cos(\Delta\alpha))\frac{1}{2}. \qquad \Delta\alpha = \frac{\pi}{2}$$

: teljesen véletlen működés

<!-- note: ": ideális eset" stands right of "Δα = 0" in the P_0 line, ": teljesen véletlen működés" right of "Δα = π/2" in the P_1 line. The formula pictures carry small stray marks (dots under ≜, a dash over the second minus and over "=" of the sin identity); they are crop artefacts, not symbols -->
## s33 · p33 · LINEÁRIS RENDSZEREKRE VONATKOZÓ ISMERETEINKET
<!-- status: viewed pages/p033.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p033-f1.png -->

<!-- note: the full slide title is "LINEÁRIS RENDSZEREKRE VONATKOZÓ ISMERETEINKET KIHASZNÁLVA"; "ELEMZÉS (1)" is a subtitle at the right, beside the formula -->

**ELEMZÉS (1)**

Figure: quantum circuit in a framed box: a single wire starting with $|0\rangle$ on the left, passing through three boxes in order $H$, $P$, $H$, and ending on the right. Under the wire four upward arrows mark the states: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.
A vertical red line crosses the circuit at $|\varphi_0\rangle$ (before the first $H$).
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

$$|\varphi_0\rangle = |0\rangle$$

## s34 · p34 · ELEMZÉS (2)
<!-- status: viewed pages/p034.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p034-f1.png -->
<!-- figure: figures/p034-f2.png -->
<!-- figure: figures/p034-x219.png (raw layer) -->
<!-- figure: figures/p034-x230.png (raw layer) -->
<!-- figure: figures/p034-x251.png (raw layer) -->
<!-- figure: figures/p034-x253.png (raw layer) -->

Figure: quantum circuit in a framed box: a single wire starting with $|0\rangle$ on the left, passing through three boxes in order $H$, $P$, $H$, and ending on the right. Under the wire four upward arrows mark the states: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.
A vertical red line crosses the circuit at $|\varphi_1\rangle$ (between $H$ and $P$).
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

In a red box:

$$H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \qquad H|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}.$$

(the two equations stand one under the other)

A blue block arrow points right from the red box to the result:

$$\begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}$$

<!-- note: layers: x219 is the circuit, x253 the red-box formulas, x251 a black rectangle (mask, no content). Layer x230 holds the matrix calculation of slide 29 (|φ1⟩ = H|φ0⟩ = 1/√2 [[1,1],[1,-1]] with [1;0] above [1/√2; 1/√2]); it is not visible on the rendered slide -->

## s35 · p35 · ELEMZÉS (3)
<!-- status: viewed pages/p035.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p035-f1.png -->
<!-- figure: figures/p035-f2.png -->
<!-- figure: figures/p035-f3.png -->
<!-- figure: figures/p035-f4.png -->
<!-- figure: figures/p035-x219.png (raw layer) -->
<!-- figure: figures/p035-x233.png (raw layer) -->
<!-- figure: figures/p035-x221.png (raw layer) -->
<!-- figure: figures/p035-x256.png (raw layer) -->

Figure: quantum circuit in a framed box: a single wire starting with $|0\rangle$ on the left, passing through three boxes in order $H$, $P$, $H$, and ending on the right. Under the wire four upward arrows mark the states: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.
A vertical red line crosses the circuit at $|\varphi_2\rangle$ (between $P$ and the second $H$).
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

$$\mathbf{P} = \begin{bmatrix} e^{j\alpha_0} & 0 \\ 0 & e^{j\alpha_1} \end{bmatrix}$$

A blue block arrow points right from the matrix to the result:

$$\begin{bmatrix} \frac{e^{j\alpha_0}}{\sqrt{2}} \\ \frac{e^{j\alpha_1}}{\sqrt{2}} \end{bmatrix}$$

<!-- note: layers: x219 is the circuit, x221 the P matrix, x256 a black rectangle (mask). Layer x233 holds the matrix calculation of slide 30 (|φ2⟩ = P|φ1⟩ ...); it is not visible on the rendered slide -->

## s36 · p36 · ELEMZÉS (4)
<!-- status: viewed pages/p036.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p036-f1.png -->
<!-- figure: figures/p036-f2.png -->
<!-- figure: figures/p036-x219.png (raw layer) -->
<!-- figure: figures/p036-x236.png (raw layer) -->
<!-- figure: figures/p036-x260.png (raw layer) -->
<!-- figure: figures/p036-x253.png (raw layer) -->

Figure: quantum circuit in a framed box: a single wire starting with $|0\rangle$ on the left, passing through three boxes in order $H$, $P$, $H$, and ending on the right. Under the wire four upward arrows mark the states: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.
A vertical red line crosses the circuit at $|\varphi_3\rangle$ (after the second $H$).
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

In a red box:

$$H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \qquad H|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}.$$

(the two equations stand one under the other)

A blue block arrow points right from the red box to the result:

$$\begin{bmatrix} \frac{e^{j\alpha_0}+e^{j\alpha_1}}{2} \\ \frac{e^{j\alpha_0}-e^{j\alpha_1}}{2} \end{bmatrix}$$

<!-- note: layers: x219 is the circuit, x253 the red-box formulas, x260 a black rectangle (mask). Layer x236 holds the matrix calculation of slide 31 (|φ3⟩ = H|φ2⟩ ...); it is not visible on the rendered slide. The copyright line is partly covered by the red box -->

## s37 · p37 · INTERFEROMÉTER AHOGY EGY FIZIKUS LÁTJA
<!-- status: viewed pages/p037.png -->
<!-- flags: graphic, image, stacked -->
<!-- figure: figures/p037-f1.png -->
<!-- figure: figures/p037-f2.png -->
<!-- figure: figures/p037-x264.png (raw layer) -->
<!-- figure: figures/p037-x265.jpeg (raw layer) -->
<!-- figure: figures/p037-x267.jpeg (raw layer) -->

Figure: top left, the generalized interferometer drawing of slide 26 (two beam splitters $H$, two mirrors, the sheets of glass $\alpha_0$ and $\alpha_1$ in the block $P$, detectors $|0\rangle$ and $|1\rangle$, legend), with a photo of a butterfly (cream wings with black spots) sitting on top of the $P$ block.
Use: image figures/p037-x264.png

Figure: large photo at the right: a real Mach–Zehnder interferometer on a black optical breadboard with a grid of mounting holes, seen from above. Green laser beams are drawn along the light paths: from a fibre-coupled source at the lower left, the beam goes right to a beam splitter, splits into two paths forming a quadrilateral (via mirrors in kinematic mounts at the upper left and lower right), and the paths recombine at a second beam splitter near the upper right; from there one beam goes up to a white screen at the top and one goes right to a white screen at the right edge. A hand at the upper right adjusts a mount in the upward beam.
Use: image figures/p037-x267.jpeg

<!-- note: layers: x264 the interferometer drawing, x265 the butterfly photo (on black), x267 the lab photo -->

## s38 · p38 · INTERFEROMÉTER AHOGY EGY VILLAMOSMÉRNÖK LÁTJA
<!-- status: viewed pages/p038.png -->
<!-- flags: graphic, image, stacked -->
<!-- figure: figures/p038-f1.png -->
<!-- figure: figures/p038-x264.png (raw layer) -->
<!-- figure: figures/p038-x265.jpeg (raw layer) -->
<!-- figure: figures/p038-x219.png (raw layer) -->
<!-- figure: figures/p038-x270.png (raw layer) -->
<!-- figure: figures/p038-x271.png (raw layer) -->
<!-- figure: figures/p038-x273.png (raw layer) -->

Figure: three pictures joined by blue block arrows. Bottom left: the generalized interferometer drawing of slide 26 (two beam splitters $H$, two mirrors, the sheets of glass $\alpha_0$ and $\alpha_1$ in the block $P$, detectors $|0\rangle$ and $|1\rangle$, legend), with a photo of a butterfly (cream wings with black spots) sitting on top of the $P$ block. A blue arrow points right from it to the bottom right picture: the circuit drawing of slide 27 (a single wire starting with $|0\rangle$, passing through the boxes $H$, $P$, $H$, with upward arrows marking $|\varphi_0\rangle$ (before the first $H$), $|\varphi_1\rangle$ (between $H$ and $P$), $|\varphi_2\rangle$ (between $P$ and the second $H$) and $|\varphi_3\rangle$ (after the second $H$)). A blue arrow points up from that circuit to the top picture.
Use: text

Figure: top, a Qiskit circuit drawing (matplotlib style): qubit wires $q_0$ and $q_1$ and a classical register "c" (double line, marked "2" with a slash). On $q_0$: gates H, S, H (blue squares), then a barrier (grey band with a dashed line) across $q_0$ and $q_1$, then a measurement (black box with a meter symbol) on $q_0$ whose double-line arrow goes down to bit 0 of c. On $q_1$ after the barrier: a measurement whose arrow goes down to bit 1 of c.
Use: image figures/p038-x270.png

<!-- note: layers: x264 interferometer drawing, x265 butterfly, x219 the H–P–H circuit, x270 the Qiskit circuit, x271 and x273 black rectangles (masks, no content) -->

## s39 · p39 · INTERFEROMÉTER AHOGY EGY INFORMATIKUS LÁTJA
<!-- status: viewed pages/p039.png -->
<!-- flags: graphic, image, stacked, layout -->
<!-- figure: figures/p039-f1.png -->
<!-- figure: figures/p039-x264.png (raw layer) -->
<!-- figure: figures/p039-x265.jpeg (raw layer) -->

Figure: block diagram of a quantum algorithm in a large rounded frame. "Klasszikus bemenet" above the frame, with a blue arrow pointing down into the first block. Blocks in a row from left to right, joined by blue arrows: "Inicializálás" → "Kvantum-párhuzamosság" → "Amplitúdó erősítés" → "Mérés". A red dashed line leaves the bottom of "Amplitúdó erősítés", runs down, left and back up, and ends with a red arrowhead pointing into "Kvantum-párhuzamosság" (a loop back). From "Mérés" a blue arrow points down to "Utó-feldolgozás", and from that a blue arrow points down out of the frame to "Klasszikus kimenet".
Use: redraw

Figure: bottom left, partly over the frame: the generalized interferometer drawing of slide 26 (two beam splitters $H$, two mirrors, the sheets of glass $\alpha_0$ and $\alpha_1$ in the block $P$, detectors $|0\rangle$ and $|1\rangle$, legend), with a photo of a butterfly (cream wings with black spots) sitting on top of the $P$ block.
Use: image figures/p037-x264.png

Code in a black box at the bottom middle:

```python
qc = QuantumCircuit(1,2)
qc.h(0)
qc.p(Dalpha)
qc.h(0)
qc.measure(0,1)
qc.draw("mpl")
backend = Aer.get_backend("aer_simulator")
result = backend.run(qc, shots=10000).result()
counts = result.get_counts()
print(counts)
```

<!-- suspect: qc.p(Dalpha) has no qubit argument; Qiskit's QuantumCircuit.p takes (theta, qubit), so it should be qc.p(Dalpha, 0) -->
<!-- note: layers: x264 interferometer drawing, x265 butterfly -->

## s40 · p40 · INTERFEROMÉTER AHOGY EGY INFORMATIKUS LÁTJA
<!-- status: viewed pages/p040.png -->
<!-- flags: graphic, image, stacked -->
<!-- figure: figures/p040-f1.png -->
<!-- figure: figures/p040-x280.png (raw layer) -->
<!-- figure: figures/p040-x219.png (raw layer) -->

Figure: the block diagram of the previous slide ("Klasszikus bemenet" → "Inicializálás" → "Kvantum-párhuzamosság" → "Amplitúdó erősítés" → "Mérés" → "Utó-feldolgozás" → "Klasszikus kimenet", with the red dashed loop from "Amplitúdó erősítés" back to "Kvantum-párhuzamosság"; here "Klasszikus bemenet" stands left of the frame with a blue arrow pointing right into "Inicializálás"). Over its lower part lies a large copy of the circuit of slide 27 (a single wire starting with $|0\rangle$, passing through the boxes $H$, $P$, $H$, with upward arrows marking $|\varphi_0\rangle$ (before the first $H$), $|\varphi_1\rangle$ (between $H$ and $P$), $|\varphi_2\rangle$ (between $P$ and the second $H$) and $|\varphi_3\rangle$ (after the second $H$)), covering the left edges of "Utó-feldolgozás" and "Klasszikus kimenet".
Use: redraw

<!-- note: layers: x280 the block diagram, x219 the H–P–H circuit -->

## s41 · p41 · DEKOHERENCIA – ÖSSZEFONÓDÁS A KÖRNYEZETTEL
<!-- status: viewed pages/p041.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p041-f1.png -->
<!-- figure: figures/p041-f2.png -->

- Az első két posztulátum csak *zárt* rendszerekre érvényes, ezért a környezettel való összefonódás nagyon veszélyes lehet!
- Ennek bemutatására a jól ismert kvantuminterferométert használjuk, és feltételezzük, hogy az interferométeren áthaladó foton a laboratóriumon (azaz a környezeten) kívül egy pillangóval összefonódik.
- A környezet: $|\Omega\rangle$
- A pillangó repülési szabálya:

  $$|0\rangle|\Omega\rangle \rightarrow |0\rangle|\Omega_0\rangle, |1\rangle|\Omega\rangle \rightarrow |1\rangle|\Omega_1\rangle$$

  (in a framed box)

<!-- note: "zárt" is in red on the slide -->

## s42 · p42 · DEKOHERENCIA – ÖSSZEFONÓDÁS A KÜLVILÁGGAL
<!-- status: viewed pages/p042.png -->
<!-- flags: graphic, image, stacked -->
<!-- figure: figures/p042-f1.png -->
<!-- figure: figures/p042-x216.png (raw layer) -->
<!-- figure: figures/p042-x219.png (raw layer) -->
<!-- figure: figures/p042-x265.jpeg (raw layer) -->

Figure: top left, the generalized interferometer drawing of slide 26 (two beam splitters $H$, two mirrors, the sheets of glass $\alpha_0$ and $\alpha_1$ in the block $P$, detectors $|0\rangle$ and $|1\rangle$, legend), with a photo of a butterfly (cream wings with black spots) sitting on top of the $P$ block (here the butterfly sits on the upper edge of the frame, overlapping the header). Below it: "Copyright © 2005 John Wiley & Sons Ltd."
Use: image figures/p042-x216.png

Figure: bottom right, the circuit of slide 27 (a single wire starting with $|0\rangle$, passing through the boxes $H$, $P$, $H$, with upward arrows marking $|\varphi_0\rangle$ (before the first $H$), $|\varphi_1\rangle$ (between $H$ and $P$), $|\varphi_2\rangle$ (between $P$ and the second $H$) and $|\varphi_3\rangle$ (after the second $H$)), with "Copyright © 2005 John Wiley & Sons Ltd." inside its frame. A vertical red line crosses the circuit at $|\varphi_2\rangle$ (between $P$ and the second $H$).
Use: redraw

Copyright © 2005 John Wiley & Sons Ltd.

<!-- note: layers: x216 interferometer drawing, x265 butterfly, x219 circuit. The footer shows page number 44 on this page 42 -->

## s43 · p43 · ELEMZÉS (1)
<!-- status: viewed pages/p043.png -->
<!-- flags: math, graphic, image, no-text -->
<!-- figure: figures/p043-f1.png -->

- Pillangóhatás előtt

  $$|\varphi_2\rangle = \frac{e^{j\alpha_0}|0\rangle + e^{j\alpha_1}|1\rangle}{\sqrt{2}}|\Omega\rangle = |\varphi_2\rangle = \frac{e^{j\alpha_0}|0\rangle|\Omega\rangle + e^{j\alpha_1}|1\rangle|\Omega\rangle}{\sqrt{2}}$$

- Pillangóhatás után

  $$|\varphi_2'\rangle = |\varphi_2\rangle = \frac{e^{j\alpha_0}|0\rangle|\Omega_0\rangle + e^{j\alpha_1}|1\rangle|\Omega_1\rangle}{\sqrt{2}}$$

- Ezzel a Hadamard kapu után:

$$\begin{aligned} |\varphi_3\rangle &= \frac{e^{j\alpha_0}\frac{|0\rangle+|1\rangle}{\sqrt{2}}|\Omega_0\rangle + e^{j\alpha_1}\frac{|0\rangle-|1\rangle}{\sqrt{2}}|\Omega_1\rangle}{\sqrt{2}} \\ &= |0\rangle\frac{e^{j\alpha_0}|\Omega_0\rangle + e^{j\alpha_1}|\Omega_1\rangle}{2} + |1\rangle\frac{e^{j\alpha_0}|\Omega_0\rangle - e^{j\alpha_1}|\Omega_1\rangle}{2} \\ &= e^{j\frac{\alpha_0+\alpha_1}{2}}\left(|0\rangle\frac{e^{j\frac{\alpha_0-\alpha_1}{2}}|\Omega_0\rangle + e^{-j\frac{\alpha_0-\alpha_1}{2}}|\Omega_1\rangle}{2} + |1\rangle\frac{e^{j\frac{\alpha_0-\alpha_1}{2}}|\Omega_0\rangle - e^{-j\frac{\alpha_0-\alpha_1}{2}}|\Omega_1\rangle}{2}\right) \end{aligned}$$

<!-- note: colour highlights in the formulas (pasted pictures): terms with $|\Omega_0\rangle$ on pink, with $|\Omega_1\rangle$ on light blue, $|0\rangle$ on lilac, $|1\rangle$ on light green (in the "után" line the whole $e^{j\alpha_0}|0\rangle|\Omega_0\rangle$ is pink and $e^{j\alpha_1}|1\rangle|\Omega_1\rangle$ light blue) -->
<!-- suspect: both lines write "= |φ2⟩ =" in the middle: in the first line |φ2⟩ is repeated after the first "=", in the second |φ2'⟩ = |φ2⟩ equates the state after the butterfly with the state before it; probably meant as a single definition each -->

## s44 · p44 · ELEMZÉS (2)
<!-- status: viewed pages/p044.png -->
<!-- flags: math, graphic, image, no-text -->
<!-- figure: figures/p044-omega-circle.png -->

$$\Delta\alpha \triangleq \alpha_0 - \alpha_1$$

$$|\varphi_3\rangle = |0\rangle\frac{e^{j\frac{\Delta\alpha}{2}}|\Omega_0\rangle + e^{-j\frac{\Delta\alpha}{2}}|\Omega_1\rangle}{2} + |1\rangle\frac{e^{j\frac{\Delta\alpha}{2}}|\Omega_0\rangle - e^{-j\frac{\Delta\alpha}{2}}|\Omega_1\rangle}{2}$$

- Figyelem! $|\Omega_0\rangle$ és $|\Omega_1\rangle$ nem feltétlenül ortogonálisak
- Feltételezve, hogy $\langle\Omega_0|\Omega_1\rangle \neq 0$ valós

$$|\Omega_1\rangle = \boxed{\langle\Omega_0|\Omega_1\rangle}|\Omega_0\rangle + \boxed{\sqrt{1-|\langle\Omega_0|\Omega_1\rangle|^2}}|\Omega_0^\perp\rangle$$

$$\begin{aligned} |\varphi_3\rangle = {} & \frac{e^{j\frac{\Delta\alpha}{2}} + \boxed{\langle\Omega_0|\Omega_1\rangle}e^{-j\frac{\Delta\alpha}{2}}}{2}|0\rangle|\Omega_0\rangle + \frac{e^{-j\frac{\Delta\alpha}{2}}}{2}\boxed{\sqrt{1-|\langle\Omega_0|\Omega_1\rangle|^2}}|0\rangle|\Omega_0^\perp\rangle + {} \\ & \frac{e^{j\frac{\Delta\alpha}{2}} - \boxed{\langle\Omega_0|\Omega_1\rangle}e^{-j\frac{\Delta\alpha}{2}}}{2}|1\rangle|\Omega_0\rangle - \frac{e^{-j\frac{\Delta\alpha}{2}}}{2}\boxed{\sqrt{1-|\langle\Omega_0|\Omega_1\rangle|^2}}|1\rangle|\Omega_0^\perp\rangle \end{aligned}$$

<!-- note: colour highlights in the formulas (pasted pictures): terms with $|\Omega_0\rangle$ on pink, with $|\Omega_1\rangle$ on light blue, $|0\rangle$ on lilac, $|1\rangle$ on light green, $|\Omega_0^\perp\rangle$ on light orange. The boxes are coloured frames: $\langle\Omega_0|\Omega_1\rangle$ in a red frame, $\sqrt{1-|\langle\Omega_0|\Omega_1\rangle|^2}$ in an orange frame -->

Figure: vector diagram at the right, beside the two bullets: a unit circle with a horizontal axis (arrow to the right) and a vertical axis (arrow up). A red arrow along the horizontal axis from the centre to the circle, labelled $|\Omega_0\rangle$ (on pink); the vertical axis labelled $|\Omega_0^\perp\rangle$ (on light orange) at its top. A blue arrow from the centre into the upper right quadrant to the circle, labelled $|\Omega_1\rangle$ (on light blue). Dashed lines drop from the tip of the blue arrow to both axes; a brace under the horizontal axis marks the projection $\langle\Omega_0|\Omega_1\rangle$, a brace left of the vertical axis marks the height $\sqrt{1-|\langle\Omega_0|\Omega_1\rangle|^2}$.
Use: image figures/p044-omega-circle.png

## s45 · p45 · ELEMZÉS (3)
<!-- status: viewed pages/p045.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p045-f1.png -->

$$P_0 = \left|\frac{e^{j\frac{\Delta\alpha}{2}} + \langle\Omega_0|\Omega_1\rangle e^{-j\frac{\Delta\alpha}{2}}}{2}\right|^2 + \left|\frac{e^{-j\frac{\Delta\alpha}{2}}}{2}\sqrt{1-|\langle\Omega_0|\Omega_1\rangle|^2}\right|^2$$

$$z \in \mathbb{C} : |z|^2 = zz^* \qquad \frac{e^{j\Delta\alpha}+e^{-j\Delta\alpha}}{2} = \cos(\Delta\alpha)$$

(a light-blue block arrow points down from each of these two formulas to the result below)

$$P_0 = (1 + \langle\Omega_0|\Omega_1\rangle\cos(\Delta\alpha))\frac{1}{2}$$

$$P_1 = (1 - \langle\Omega_0|\Omega_1\rangle\cos(\Delta\alpha))\frac{1}{2}$$

A red-outlined two-headed horizontal arrow (↔) joins these to a framed box at the right (the result without the butterfly, slide 32):

$$P_0 = \cos^2\left(\frac{\Delta\alpha}{2}\right) = (1+\cos(\Delta\alpha))\frac{1}{2}, \qquad P_1 = \sin^2\left(\frac{\Delta\alpha}{2}\right) = (1-\cos(\Delta\alpha))\frac{1}{2}.$$

- Ha $\langle\Omega_0|\Omega_1\rangle = 1$ akkor az összefonódás eltűnik.
- Azonban ha $\langle\Omega_0|\Omega_1\rangle = 0$ akkor a működés teljesen véletlenné válik és a megfigyelőt alaposan becsapjuk.

<!-- note: in the framed box the P_0 and P_1 lines stand one under the other; the "=" of the cos identity is green (pasted) -->

## s46 · p46 · (no title)
<!-- status: viewed pages/p046.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p046-f1.png -->

***A No Cloning (Copy) tétel***

*"Knowledge is what we get when an observer, preferably a scientifically trained observer, provides us with a copy of reality that we can all recognize. "*

Christopher Lasch

Figure: section-divider decoration: grey network-graph background at the top of the slide.
Use: none (decorative)

## s47 · p47 · AZ UNIVERZÁLIS KVANTUMMÁSOLÓ
<!-- status: viewed pages/p047.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p047-f1.png -->

Figure: circuit of the universal quantum copier (framed). Three input wires enter from the left: $|\varphi\rangle$ (top), $|\mathbf{0}\rangle$ (middle, bold 0), $|\Omega\rangle$ (bottom). A large box $U$ spans all three wires; inside it, a smaller box $Q$ spans only the top two wires. Outputs on the right: $|\varphi\rangle$ (top), $|\varphi\rangle$ (middle), $|\Omega_\varphi\rangle$ (bottom).
Use: image figures/p047-f1.png

- Első vezeték: másolandó kvantumállapot.
- Középső vezeték : segéd qubitek.
- Alsó vezeték: környezet.
- Létezik-e egyáltalán ilyen *U* transzformáció? Ha igen, akkor meghatározzuk belőle *Q*-t.

## s48 · p48 · AZ UNIVERZÁLIS KVANTUMMÁSOLÓ
<!-- status: viewed pages/p048.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p048-f1.png -->
<!-- figure: figures/p048-f2.png -->
<!-- figure: figures/p048-x311.png (raw layer) -->
<!-- figure: figures/p048-x312.png (raw layer) -->
<!-- figure: figures/p048-x313.png (raw layer) -->
<!-- figure: figures/p048-x314.png (raw layer) -->
<!-- figure: figures/p048-x315.png (raw layer) -->
<!-- figure: figures/p048-x317.png (raw layer) -->

A másolás azt jelenti, hogy:

$$\begin{aligned} U &: |\varphi\rangle|\mathbf{0}\rangle|\Omega\rangle \rightarrow |\varphi\rangle|\varphi\rangle|\Omega_\varphi\rangle \\ U &: |\psi\rangle|\mathbf{0}\rangle|\Omega\rangle \rightarrow |\psi\rangle|\psi\rangle|\Omega_\psi\rangle \end{aligned}$$

*U*-nak unitérnek kell Lennie, azaz megőrzi a belső szprzatot

- For input

  $$\langle\Omega,\mathbf{0},\psi|\varphi,\mathbf{0},\Omega\rangle = \langle\psi|\varphi\rangle\langle\mathbf{0}|\mathbf{0}\rangle\langle\Omega|\Omega\rangle = \langle\psi|\varphi\rangle$$

- For output

  $$\langle\Omega_\psi,\psi,\psi|\varphi,\varphi,\Omega_\varphi\rangle = \langle\psi|\varphi\rangle\langle\psi|\varphi\rangle\langle\Omega_\psi|\Omega_\varphi\rangle = \langle\psi|\varphi\rangle^2\langle\Omega_\psi|\Omega_\varphi\rangle$$

A két belső szorzat akkor egyenlő ha

- $\langle\psi|\varphi\rangle = \pm 1$ which is equivalent to $|\varphi\rangle = |\psi\rangle$ or
- $\langle\psi|\varphi\rangle = 0$ which represents the orthogonality between $|\varphi\rangle$ and $|\psi\rangle$

<!-- note: "For input" is red, "For output" green; the final ⟨ψ|φ⟩ of the input line is circled in red, the final ⟨ψ|φ⟩²⟨Ω_ψ|Ω_φ⟩ of the output line is circled in green. Layers: x311 the two U lines, x314 the input line, x312 the output line, x313 the two final bullets, x315 and x317 black rectangles (masks of the circles) -->
<!-- suspect: "Lennie" (capital L, should be "lennie") and "szprzatot" (should be "szorzatot") are typos -->

## s49 · p49 · A NO CLONING TÉTEL
<!-- status: auto -->

- Nem készíthető olyan unitér kvantumkapu, amivel
tetszőleges kvantumállapot-halmaz hibamentesen másolható.
- De
    - Ortogonális állapotok halmaza másolható!
    - Ismert állapot másolható!
- Hogyan?

## s50 · p50 · (no title)
<!-- status: viewed pages/p050.png -->
<!-- flags: graphic, image, no-text -->
<!-- figure: figures/p050-f1.png -->

Figure: black-and-white cartoon (watermark "CARTOONSTOCK.com", signature "MIKE SHAPIRO"): two angels with haloes and wings on clouds; one stands in front of a desk labelled "INFORMATION" with a computer monitor, behind which the other angel sits. Caption: "I still don't understand quantum theory." Vertical side texts: "© Original Artist / Search ID: mshn197" (left) and "Rights Available from CartoonStock.com" (right).
Use: none (decorative)
