# bloch_gyak.pdf

<!-- 14 pages, 14 units, grouping: heuristic -->

## s1 · p1 · (no title)
<!-- status: viewed pages/p001.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p001-f1.png -->
<!-- figure: figures/p001-f2.png -->

**Műveletek a Bloch-gömbön**

Kvantuminformatikai alkalmazások – Gyakorlat

**Dr. Solymos Balázs, Dr. Bacsárdi László, Dr. Imre Sándor**

BME Hálózati Rendszerek és Szolgáltatások Tanszék

solymosb@hit.bme.hu

Figure: title banner with the department logo "HiT" and the text "HÁLÓZATI RENDSZEREK ÉS SZOLGÁLTATÁSOK TANSZÉK" in front of a light grey network graph (circles joined by lines).
Use: none (decorative)

Figure: small BME logo at the bottom right: line drawing of the main university building with "MŰEGYETEM 1782" under it.
Use: none (decorative)

## s2 · p2 · A KVANTUMMECHANIKA POSZTULÁTUMAI
<!-- status: viewed pages/p002.png -->
<!-- flags: math, graphic, image, table -->
<!-- figure: figures/p002-f1.png -->

<!-- note: layout: the list is on the left; each formula sits in a coloured box to the right of its postulate (red box next to 1., blue next to 2., orange next to 3., green below 4.). The formulas are placed here under the postulate they belong to. -->

- 1. posztulátum: *kvantumbit*
  - Hilbert-tér

  $$|\varphi\rangle = \sum_{i=0}^{2^n-1} \varphi_i |i\rangle$$

- 2. posztulátum: *logikai kapuk*
  - Unitér transzformáció
  - Elemi kvantum logikai kapuk

  $$U^\dagger \equiv U^{-1}$$

- 3. posztulátum: *Q/C átalakítás*
  - Mérési statisztika
  - Mérés utáni állapot

  $$P(m \mid |\varphi\rangle) = \langle\varphi| M_m^\dagger M_m |\varphi\rangle$$

  $$|\varphi'\rangle = \frac{M_m|\varphi\rangle}{\sqrt{\langle\varphi| M_m^\dagger M_m |\varphi\rangle}}$$

- 4. posztulátum: *regiszterek*
  - Tenzorszorzás

  $$|\varphi\rangle = |0\rangle \otimes \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$

<!-- note: the fraction bar of the |φ'⟩ formula is drawn as a double line in the picture; taken as a rendering artefact of a single fraction bar. -->

## s3 · p3 · 1ST POSTULATE (STATE SPACE)
<!-- status: auto -->

The actual state of any closed physical system can be described by means of a so called state vector **v** having complex coefficients and unit length in a Hilbert space V i.e. a complex linear vector space (state space) equipped with inner product.

**1.** **Állapotleírás**

**Zárt** fizikai rendszer aktuális állapota egy olyan állapotvektorral írható le, amely komplex együtthatókkal rendelkezik, egységnyi hosszú a H Hilbert-térben (egy komplex lineáris vektortérben, amelyben értelmezve van a belső szorzat).

## s4 · p4 · KVANTUMBIT (QUBIT)
<!-- status: viewed pages/p004.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p004-f1.png -->
<!-- figure: figures/p004-f2.png -->
<!-- figure: figures/p004-f3.png -->
<!-- figure: figures/p004-f4.png -->
<!-- figure: figures/p004-f5.png -->

- Dirac ‘*ket*’ és ‘*bra*’ jelölés $\quad |\varphi\rangle = (\langle\varphi|)^\dagger$
- Kvantumbit: mindkét klasszikus állapotot (bázisállapotot) tartalmazza egyidőben: szuperpozíció

  $$|\varphi\rangle = a|0\rangle + b|1\rangle = a\begin{bmatrix} 1 \\ 0 \end{bmatrix} + b\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} a \\ b \end{bmatrix}$$

- ahol *a* és *b* <u>komplex</u> valószínűségi amplitúdók. Abszolút érték négyzetük adja meg a mérés eredményét (a klasszikus bázisban): $\quad |a|^2 + |b|^2 = 1$
- Műveletek: belső és külső szorzat

## s5 · p5 · BLOCH-GÖMB (1)
<!-- status: viewed pages/p005.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p005-f1.png -->

Egy kvantumbitet jelenít meg

$$|\varphi\rangle = e^{j\gamma}\left[\cos\left(\frac{\alpha}{2}\right)|0\rangle + e^{j\beta}\sin\left(\frac{\alpha}{2}\right)|1\rangle\right] \quad \alpha, \beta, \gamma \in \mathbb{R}$$

$$|\varphi\rangle = [x, y, z]^T = [\cos(\beta)\sin(\alpha), \sin(\beta)\sin(\alpha), \cos(\alpha)]^T$$

<!-- suspect: the second line equates the ket |φ⟩ with the real 3-vector [x, y, z]^T; what is meant is the Bloch vector (point on the sphere) of |φ⟩, not the state vector itself. -->

## s6 · p6 · BLOCH-GÖMB (2)
<!-- status: viewed pages/p006.png -->
<!-- flags: math, graphic, image, table, layout, encoding -->
<!-- figure: figures/p006-f1.png -->
<!-- figure: figures/p006-f2.png -->

<!-- note: layout: the Bloch sphere figure fills the left half of the slide; the formulas stand to its right, top to bottom. -->

Figure: Bloch sphere, line drawing in a rounded frame. A circle (the sphere) with a horizontal ellipse through its centre (the equator, the xy plane). Three axes start at the centre: z points straight up to the north pole, x points to the lower left (towards the viewer), y points to the right; each axis ends in an arrowhead and is labelled with its letter in italics (z just below the north pole, x at the lower left end, y at the right end). The north pole carries a small grey ball and the label |0⟩ above it; the south pole carries a small grey ball and the label |1⟩ below it, with a vertical line running from the centre down to it. A state vector runs from the centre up and to the right to a point on the sphere's surface, labelled |j⟩ (see the suspect note); around its tip two pairs of short crossing arcs (pieces of a latitude and a longitude line) mark the point on the surface. The angle α is drawn as an arc between the z axis and the state vector. From the tip of the state vector a dashed vertical line drops to the equatorial plane, and a dashed line joins that foot point with the centre (the projection of the vector onto the xy plane). The angle β is drawn as an arc in the equatorial plane between the x axis and this dashed projection. Bottom left inside the frame: "Copyright © 2005 John Wiley & Sons Ltd."
Use: image figures/p006-f2.png

<!-- suspect: the state on the sphere is labelled |j⟩; this is almost certainly |φ⟩ set in a Symbol font that did not survive (φ shown as j), matching the |φ⟩ of the formulas beside it. -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

$$|\varphi\rangle = e^{j\gamma}\left[\cos\left(\frac{\alpha}{2}\right)|0\rangle + e^{j\beta}\sin\left(\frac{\alpha}{2}\right)|1\rangle\right]$$

$$\alpha, \beta, \gamma \in \mathbb{R}$$

$$|\varphi\rangle = [x, y, z]^T = [\cos(\beta)\sin(\alpha), \sin(\beta)\sin(\alpha), \cos(\alpha)]^T$$

<!-- suspect: as on s5, the last line equates the ket |φ⟩ with the real Bloch vector [x, y, z]^T. -->

## s7 · p7 · PAULI-KAPUK
<!-- status: viewed pages/p007.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p007-f1.png -->
<!-- figure: figures/p007-f2.png -->
<!-- figure: figures/p007-f3.png -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

Pauli-X (bit-flip) kapu:

$$\begin{bmatrix} a \\ b \end{bmatrix}$$

$$|\psi\rangle = X|\varphi\rangle = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} b \\ a \end{bmatrix} = b|0\rangle + a|1\rangle$$

<!-- note: the column vector [a; b] stands directly above the column vector [b; a] that follows the matrix, i.e. it shows the input |φ⟩ that the matrix acts on, while [b; a] below it is the result. The slide writes it this way (matrix followed by the result vector); it is copied as shown. -->
<!-- note: two tiny dots under |φ⟩ = a|0⟩ + b|1⟩ are remnants of a cropped-off line of the picture; nothing readable. Same on s8–s12. -->

## s8 · p8 · PAULI-KAPUK
<!-- status: viewed pages/p008.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p008-f1.png -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

- Pauli X (bit-flip) gate:

  $$\begin{bmatrix} a \\ b \end{bmatrix}$$

  $$|\psi\rangle = X|\varphi\rangle = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} b \\ a \end{bmatrix} = b|0\rangle + a|1\rangle$$

- Pauli *Z* (phase-flip) gate:

  $$\begin{bmatrix} a \\ b \end{bmatrix}$$

  $$|\psi\rangle = Z|\varphi\rangle = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\begin{bmatrix} a \\ -b \end{bmatrix} = a|0\rangle - b|1\rangle$$

<!-- note: as on s7, each [a; b] stands directly above the result vector that follows the matrix ([b; a] and [a; -b]). -->

## s9 · p9 · PAULI-KAPUK
<!-- status: viewed pages/p009.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p009-f1.png -->
<!-- figure: figures/p009-f2.png -->
<!-- figure: figures/p009-f3.png -->
<!-- figure: figures/p009-f4.png -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

- Pauli *Y* (???-flip) gate:

  $$\begin{bmatrix} a \\ b \end{bmatrix}$$

  $$|\psi\rangle = Y|\varphi\rangle = \begin{bmatrix} 0 & -j \\ j & 0 \end{bmatrix}\begin{bmatrix} -jb \\ ja \end{bmatrix} = -jb|0\rangle + ja|1\rangle$$

- Geometrical interpretation of Pauli *X* gate: rotation around axis *x* in the Bloch sphere

  $$e^{-j\frac{\alpha}{2}X} = \cos\left(\frac{\alpha}{2}\right)I - j\sin\left(\frac{\alpha}{2}\right)X$$

<!-- note: as on s7, [a; b] stands directly above the result vector [-jb; ja] that follows the matrix. "???-flip" is literally on the slide (a question to the class). -->

## s10 · p10 · FÁZIS-KAPU
<!-- status: viewed pages/p010.png -->
<!-- flags: math, graphic, image, no-text -->
<!-- figure: figures/p010-f1.png -->
<!-- figure: figures/p010-f2.png -->
<!-- figure: figures/p010-f3.png -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

$$\begin{bmatrix} a \\ b \end{bmatrix}$$

$$|\psi\rangle = P(\alpha)|\varphi\rangle = \begin{bmatrix} 1 & 0 \\ 0 & e^{j\alpha} \end{bmatrix}\begin{bmatrix} a \\ e^{j\alpha}b \end{bmatrix} = a|0\rangle + e^{j\alpha}b|1\rangle$$

<!-- note: as on s7, [a; b] stands directly above the result vector [a; e^{jα}b] that follows the matrix. -->

## s11 · p11 · HADAMARD-KAPU
<!-- status: viewed pages/p011.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p011-f1.png -->
<!-- figure: figures/p011-f2.png -->
<!-- figure: figures/p011-f3.png -->
<!-- figure: figures/p011-f4.png -->
<!-- figure: figures/p011-x91.png (raw layer) -->
<!-- figure: figures/p011-x92.png (raw layer) -->
<!-- figure: figures/p011-x93.png (raw layer) -->
<!-- figure: figures/p011-x78.png (raw layer) -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

$$\begin{bmatrix} a \\ b \end{bmatrix}$$

$$|\psi\rangle = H|\varphi\rangle = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}\begin{bmatrix} \frac{a+b}{\sqrt{2}} \\ \frac{a-b}{\sqrt{2}} \end{bmatrix} = \frac{a+b}{\sqrt{2}}|0\rangle + \frac{a-b}{\sqrt{2}}|1\rangle$$

- Hadamard-kapu hermitikus: $\quad H^\dagger = H$
- továbbá: $\quad HH = I$

<!-- note: as on s7, [a; b] stands directly above the result vector that follows the matrix. -->
<!-- note: stacked layers, in order: x91 = the H|φ⟩ equation with [a; b] above it, x92 = H† = H, x93 = HH = I, x78 = |φ⟩ = a|0⟩ + b|1⟩. They are formula pictures that do not hide each other; all are transcribed above. -->

## s12 · p12 · HADAMARD-KAPU
<!-- status: viewed pages/p012.png -->
<!-- flags: math, graphic, image, stacked, table -->
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

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

$$\begin{bmatrix} a \\ b \end{bmatrix}$$

$$|\psi\rangle = H|\varphi\rangle = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}\begin{bmatrix} \frac{a+b}{\sqrt{2}} \\ \frac{a-b}{\sqrt{2}} \end{bmatrix} = \frac{a+b}{\sqrt{2}}|0\rangle + \frac{a-b}{\sqrt{2}}|1\rangle$$

- Hadamard-kapu hermitikus: $\quad H^\dagger = H$
- továbbá: $\quad HH = I$
- Érdemes megjegyezni:

  $$H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}},$$

  $$H|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}.$$

<!-- note: differs from s11 only by the last bullet; its two formulas stand in a red box to the right of it. As on s7, [a; b] stands directly above the result vector that follows the matrix. -->
<!-- note: stacked layers, in order: x91 = the H|φ⟩ equation with [a; b] above it, x92 = H† = H, x93 = HH = I, x96 = H|0⟩ and H|1⟩, x78 = |φ⟩ = a|0⟩ + b|1⟩. Formula pictures that do not hide each other; all are transcribed above. -->

## s13 · p13 · HADAMARD-KAPU ÉS A SZUPERPOZÍCIÓ ELVE
<!-- status: viewed pages/p013.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p013-circuit.png -->

<!-- note: layout: top left the two H formulas, top middle |φ⟩; a light blue arrow points down from each of them to the long equation at the bottom; the circuit in a red frame is at the top right. -->

$$H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}},$$

$$H|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}.$$

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

Figure: two thick light blue arrows pointing down: the left one from the H|0⟩, H|1⟩ formulas, the right one from |φ⟩ = a|0⟩ + b|1⟩, both to the equation below.
Use: text

$$|\psi\rangle = H|\varphi\rangle = a\frac{|0\rangle + |1\rangle}{\sqrt{2}} + b\frac{|0\rangle - |1\rangle}{\sqrt{2}} = \frac{a+b}{\sqrt{2}}|0\rangle + \frac{a-b}{\sqrt{2}}|1\rangle$$

Figure: circuit diagram in a red frame, with no caption. One closed loop: along the top wire three resistors R₁, R₂, R₃ in series, left to right; above each resistor a voltmeter (circle labelled U₁, U₂, U₃) connected in parallel with it. The right end of the top wire goes down the right side to the bottom wire. On the bottom wire, a DC source (battery: thin long plate on the left marked "+", thick short plate on the right); a voltmeter U below it is connected in parallel with the battery. Left of the battery on the bottom wire an arrow labelled I points left (current direction). The left side of the loop goes up through an ammeter (circle labelled I) back to the top wire before R₁.
Use: image figures/p013-circuit.png

## s14 · p14 · BLOCH GÖMB FELADATOK
<!-- status: auto -->

Vizsgáljuk meg hol helyezkednek el az egyes bázisállapotok a gömbön!

Milyen régió tartozik a gömbön egy mérési eloszláshoz?

Milyen operációnak feleltethetőek meg a gömbön az egyes Pauli kapuk?

Vizsgáljuk meg, és lássuk be a következő egyenlőségeket: HH=I, XX=I, ZZ=I, HXH=Z, HZH=X
