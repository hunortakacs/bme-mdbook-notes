# 03_osszefonodasalapjai_20260923.pdf

<!-- 32 pages, 30 units, grouping: heuristic -->

## s1 · p1 · (no title)
<!-- status: viewed pages/p001.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p001-f1.png -->
<!-- figure: figures/p001-f2.png -->

**Összefonódás**

Kvantuminformatikai alkalmazások, 2026. ősz
2026. szeptember 23.

**Dr. Bacsárdi László, Dr. Imre Sándor**

BME Villamosmérnöki és Informatikai Kar
bacsardi@hit.bme.hu

Figure: title slide decoration. Top: the HIT logo ("HÁLÓZATI RENDSZEREK ÉS SZOLGÁLTATÁSOK TANSZÉK") over a light grey network-graph background (nodes and edges), a dark red bar at the right edge. Bottom right: a QR code and below it the drawing of the Műegyetem building with the text "MŰEGYETEM 1782".
Use: none (decorative)

## s2 · p2 · FONTOS INFORMÁCIÓ
<!-- status: auto -->

A 2026/2027-es tanévben az előadásról felvétel készül. Minden információ (dátumok, évvel kapcsolatos referencia) a 2026/2027-es tanév őszi félévére vonatkozik.

Az előadás során a diasor minimálisan módosulhat (pl. elgépelések javítása, bizonyos fogalmak pontosítása.) A tárgy számonkért anyaga a félév során folyamatosan közzétett diasor. Ha az előadás felvétele és az utólag közzétett diasor között valamilyen különbség van, akkor az utólag közzétett diasor tartalma a mérvadó.

## s3 · p3 · ÖSSZEFOGLALÁS A KORÁBBI ÓRÁKRÓL
<!-- status: auto -->

## s4 · p4 · MI AZ A KVANTUM?
<!-- status: viewed pages/p004.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p004-f1.png -->

**Egy rendszerre akkor aggasztjuk rá a „kvantum” jelzőt, ha a kvantummechanika törvényei szerint működik.**
<!-- suspect: "aggasztjuk" (= worry) is probably a typo for "aggatjuk" (= hang on, attach) -->

A kvantum alapú rendszereknek speciális jellegzetességei:

- kvantáltság
- hullám-részecske kettősség
- alagúteffektus
- szuperpozíció
- kvantum interferencia
- …

A kvantum alapú jelenségek alapvetően a nanométer tartományban jelennek meg

***de***

a kvantummechanika törvénye jelentik az alapjait sok makroszkopikus rendszernek is.
<!-- suspect: "törvénye jelentik" — singular noun with plural verb; probably "törvényei jelentik" -->

<!-- note: the text above sits in a light grey box on the right half of the slide; the picture is on the left -->

Figure: stock photo of a printed circuit board in purple/pink light, with a glowing chip in the middle and traces running out from it in all directions.
Use: none (decorative)

## s5 · p5 · „We never experiment with just one electron or atom or (small) molecule.
<!-- status: duplicate of 01_bevezetes_20260909.pdf s10 -->
<!-- flags: graphic, image -->
<!-- figure: figures/p005-f1.png -->

In thought-experiments we sometimes assume that we do; this invariably entails ridiculous consequences... **we are not** **experimenting with single particles**, any more than we can raise Ichthyosauria in the zoo"

Erwin Schrödinger [Brit. J. Phil. Sci. 3, 233 (1952)]

## s6 · p6 · A KVANTUMMECHANIKA POSZTULÁTUMAI
<!-- status: viewed pages/p006.png -->
<!-- flags: math, graphic, image, table -->
<!-- figure: figures/p006-f1.png -->

- 1. Posztulátum: *kvantumbit*
  - Hilbert-tér
- 2. Posztulátum: *logikai kapuk*
  - Unitér transzformáció
  - Elemi kvantum logikai kapuk
- 3. Posztulátum: *Q/C átalakítás*
  - Mérési statisztika
  - Mérés utáni állapot
- 4. Posztulátum: *regiszterek*
  - Tenzorszorzás

<!-- note: right of the list, four framed formulas, one per postulate (the frame colours pair them with the list: red = 1., blue = 2., orange = 3., green = 4., the last one below the list) -->

<!-- note: red frame, belongs to 1. Posztulátum -->

$$|\varphi\rangle = \sum_{i=0}^{2^n-1} \varphi_i |i\rangle$$

<!-- note: blue frame, belongs to 2. Posztulátum -->

$$U^\dagger \equiv U^{-1}$$

<!-- note: orange frame, belongs to 3. Posztulátum -->

$$P(m \mid |\varphi\rangle) = \langle\varphi|M_m^\dagger M_m|\varphi\rangle$$

$$|\varphi'\rangle = \frac{M_m|\varphi\rangle}{\sqrt{\langle\varphi|M_m^\dagger M_m|\varphi\rangle}}$$

<!-- note: green frame, belongs to 4. Posztulátum; it stands below the list -->

$$|\varphi\rangle = |0\rangle \otimes \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$

## s7 · p7 · POSZTULÁTUMOK (1)
<!-- status: viewed pages/p007.png -->
<!-- flags: math, graphic, image, encoding -->
<!-- figure: figures/p007-f1.png -->

**1. Állapotleírás**

**Zárt** fizikai rendszer aktuális állapota egy olyan állapotvektorral írható le, amely komplex együtthatókkal rendelkezik, egységnyi hosszú a *H* Hilbert-térben (egy komplex lineáris vektortérben, amelyben értelmezve van a belső szorzat).

**2. Zárt rendszer időbeli fejlődése**

A **zárt** rendszer időbeli fejlődése **unitér** transzformációval írható le, amely csak a kezdő és végállapottól függ.

$$U^\dagger \equiv U^{-1}$$

<!-- note: the formula is in a red frame below the text of point 2 -->

**4. Összetett rendszer**

Ha V és Y a két kvantumrendszerhez rendelt Hilbert-tér, akkor az ebből a két rendszerből álló összetett rendszerhez a $\mathrm{W} = \mathrm{V} \otimes \mathrm{Y}$ Hilbert-tér rendelhető.

<!-- note: point 3 is not on this slide; it is the next slide (s8) -->

## s8 · p8 · 3. POSZTULÁTUM
<!-- status: viewed pages/p008.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p008-f1.png -->
<!-- figure: figures/p008-elefant.png -->
<!-- figure: figures/p008-cickany.png -->

**3. A mérés**

Legyen $\{m\}$ a mérés lehetséges eredményeinek a halmaza. Egy mérés a mérési operátorok halmazával adható meg:

$$\{M_m\}$$

Ha a megmérendő rendszer állapota $|\varphi\rangle$ akkor annak a valószínűsége, hogy a mérés az *m* eredményt adja:

$$P(m \mid |\varphi\rangle) = \langle\varphi|M_m^\dagger M_m|\varphi\rangle$$

A mérés után a rendszer állapota az alábbi lesz:

$$|\varphi'\rangle = \frac{M_m|\varphi\rangle}{\sqrt{\langle\varphi|M_m^\dagger M_m|\varphi\rangle}}$$

Ez miért érdekes?

<!-- note: "Ez miért érdekes?" stands at the right, under the elephant photo; a big red arrow points from there at the post-measurement formula |φ'⟩ -->

Figure: photo of an elephant leaning on / sitting down onto a small silver car on a dirt road (the car is pushed in under its weight). It stands right of the probability formula, above the question "Ez miért érdekes?".
Use: image figures/p008-elefant.png

Figure: photo of a tiny shrew sitting on the fingers of a human hand (watermark "Wikipedia.org"). It stands bottom left, next to the post-measurement formula.
Use: image figures/p008-cickany.png

<!-- note: the two photos are a visual metaphor for the question "Ez miért érdekes?": a measurement (a big apparatus acting on a small system) changes the measured state -->

## s9 · p9 · KVANTUMBIT (QUBIT)
<!-- status: viewed pages/p009.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p009-f1.png -->
<!-- figure: figures/p009-f2.png -->
<!-- figure: figures/p009-f3.png -->
<!-- figure: figures/p009-f4.png -->
<!-- figure: figures/p009-f5.png -->

- Dirac ‘*ket*’ és ‘*bra*’ jelölés $\qquad |\varphi\rangle = (\langle\varphi|)^\dagger$
- Kvantumbit: mindkét klasszikus állapotot (bázisállapotot) tartalmazza egyidőben: szuperpozíció

  $$|\varphi\rangle = a|0\rangle + b|1\rangle = a\begin{bmatrix} 1 \\ 0 \end{bmatrix} + b\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} a \\ b \end{bmatrix}$$

- ahol *a* és *b* <u>komplex</u> valószínűségi amplitúdók. Abszolút érték négyzetük adja meg a mérés eredményét (a klasszikus bázisban):

  $$|a|^2 + |b|^2 = 1$$

- Műveletek: belső és külső szorzat

<!-- note: "ket", "bra", "a" and "b" are red on the slide; "komplex" is underlined -->

## s10 · p10 · BLOCH-GÖMB (1)
<!-- status: viewed pages/p010.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p010-f1.png -->

Egy kvantumbitet jelenít meg

$$|\varphi\rangle = e^{j\gamma}\left[\cos\left(\frac{\alpha}{2}\right)|0\rangle + e^{j\beta}\sin\left(\frac{\alpha}{2}\right)|1\rangle\right] \qquad \alpha, \beta, \gamma \in \mathbb{R}$$

$$|\varphi\rangle = [x, y, z]^T = [\cos(\beta)\sin(\alpha), \sin(\beta)\sin(\alpha), \cos(\alpha)]^T$$

<!-- suspect: the second line equates the ket |φ⟩ with the real 3-vector [x, y, z]^T; that vector is the point of the Bloch sphere that represents |φ⟩, not the state vector itself -->

## s11 · p11 · BLOCH-GÖMB (2)
<!-- status: viewed pages/p011.png -->
<!-- flags: math, graphic, image, layout, encoding -->
<!-- figure: figures/p011-f1.png -->
<!-- figure: figures/p011-f2.png -->

Figure: Bloch sphere (line drawing, framed, "Copyright © 2005 John Wiley & Sons Ltd." at the bottom). A sphere with its equator drawn as an ellipse. Vertical axis from the centre up to the north pole, labelled $z$; the north pole is a dot labelled $|0\rangle$, the south pole a dot labelled $|1\rangle$. In the equatorial plane: the $x$ axis points from the centre towards the viewer and to the lower left, the $y$ axis to the right. A state vector (arrow) goes from the centre to a point on the upper right part of the sphere, labelled $|j\rangle$, with a few short curved strokes around its tip. The angle $\alpha$ is marked between the $z$ axis and the state vector. A dashed line drops vertically from the tip of the state vector to the equatorial plane, and a dashed line joins that foot point to the centre; the angle $\beta$ is marked in the equatorial plane between the $x$ axis and this dashed projection.
Use: image figures/p011-f2.png

<!-- suspect: the state on the sphere is labelled |j⟩ while both formulas name it |φ⟩; probably a φ in a symbol font that renders as j -->

<!-- note: the two formulas stand right of the figure -->

$$|\varphi\rangle = e^{j\gamma}\left[\cos\left(\frac{\alpha}{2}\right)|0\rangle + e^{j\beta}\sin\left(\frac{\alpha}{2}\right)|1\rangle\right]$$

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

## s12 · p12 · EGYBITES KVANTUMKAPUK
<!-- status: viewed pages/p012.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p012-f1.png -->
<!-- figure: figures/p012-f2.png -->
<!-- figure: figures/p012-f3.png -->
<!-- figure: figures/p012-f4.png -->
<!-- figure: figures/p012-f5.png -->
<!-- figure: figures/p012-x114.png (raw layer) -->
<!-- figure: figures/p012-x115.png (raw layer) -->
<!-- figure: figures/p012-x116.jpeg (raw layer) -->
<!-- figure: figures/p012-x117.png (raw layer) -->

- Megismerkedtünk különböző kvantumkapukkal
  - Pauli-X, Y, Z kapuk
  - Fázisforgató kapu
  - Valamint a Hadamard-kapuval (H-kapu)

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

$$|\psi\rangle = H|\varphi\rangle = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} \frac{a+b}{\sqrt{2}} \\ \frac{a-b}{\sqrt{2}} \end{bmatrix} = \frac{a+b}{\sqrt{2}}|0\rangle + \frac{a-b}{\sqrt{2}}|1\rangle$$

<!-- note: animation exported to one page. Layers: x115 = the line |φ⟩ = a|0⟩ + b|1⟩; x114 = the whole H|φ⟩ chain, with a column vector [a; b] drawn above the gap after the matrix and the result column already in that gap; x117 = a white box that covers the gap; x116 = the result part "= [(a+b)/√2; (a−b)/√2] = (a+b)/√2 |0⟩ + (a−b)/√2 |1⟩". In the render the [a; b] column floats above the gap after the Hadamard matrix (it moves into place in the animation); the formula above is the intended chain -->

## s13 · p13 · ELEMI KVANTUMKAPUK (1)
<!-- status: viewed pages/p013.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p013-f1.png -->
<!-- figure: figures/p013-x120.png (raw layer) -->
<!-- figure: figures/p013-x121.png (raw layer) -->
<!-- figure: figures/p013-x115.png (raw layer) -->
<!-- figure: figures/p013-x122.jpeg (raw layer) -->
<!-- figure: figures/p013-x124.png (raw layer) -->
<!-- figure: figures/p013-x123.png (raw layer) -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

Pauli-X (bit-flip) kapu:

$$|\psi\rangle = X|\varphi\rangle = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} b \\ a \end{bmatrix} = b|0\rangle + a|1\rangle$$

Pauli-Z (fázis-flip) kapu

$$|\psi\rangle = Z|\varphi\rangle = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} a \\ -b \end{bmatrix} = a|0\rangle - b|1\rangle$$

<!-- note: animation exported to one page, same build as s12. Layers: x115 = |φ⟩ line; x121 = whole X chain and x120 = whole Z chain, each with the [a; b] column drawn above the gap after the matrix and the result column sitting in that gap; x123 = white box covering the gap; x122 = "[b; a] = b|0⟩ + a|1⟩"; x124 = "[a; −b] = a|0⟩ − b|1⟩". In the render [a; b] floats above the gap after each matrix; the formulas above are the intended chains -->

## s14 · p14 · ELEMI KVANTUMKAPUK (2)
<!-- status: viewed pages/p014.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p014-f1.png -->
<!-- figure: figures/p014-f2.png -->
<!-- figure: figures/p014-f3.png -->
<!-- figure: figures/p014-f4.png -->
<!-- figure: figures/p014-f5.png -->
<!-- figure: figures/p014-f6.png -->
<!-- figure: figures/p014-x127.png (raw layer) -->
<!-- figure: figures/p014-x128.jpeg (raw layer) -->
<!-- figure: figures/p014-x129.png (raw layer) -->
<!-- figure: figures/p014-x130.jpeg (raw layer) -->
<!-- figure: figures/p014-x123.png (raw layer) -->

Pauli-*Y* (???-flip) kapu:

$$|\psi\rangle = Y|\varphi\rangle = \begin{bmatrix} 0 & -j \\ j & 0 \end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} -jb \\ ja \end{bmatrix} = -jb|0\rangle + ja|1\rangle$$

Fázisforgató kapu

$$|\psi\rangle = P(\alpha)|\varphi\rangle = \begin{bmatrix} 1 & 0 \\ 0 & e^{j\alpha} \end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} a \\ e^{j\alpha}b \end{bmatrix} = a|0\rangle + e^{j\alpha}b|1\rangle$$

<!-- note: "???" is on the slide as written (an open question to the audience) -->
<!-- note: animation exported to one page, same build as s12. Layers: x127 = whole Y chain, x129 = whole P(α) chain, each with [a; b] drawn above the gap after the matrix; x123 = white box covering the gap; x128 = "[−jb; ja] = −jb|0⟩ + ja|1⟩"; x130 = "[a; e^{jα}b] = a|0⟩ + e^{jα}b|1⟩". In the render [a; b] floats above the gap after each matrix; the formulas above are the intended chains -->

## s15 · p15 · HADAMARD-KAPU HATÁSA A BÁZISÁLLAPOTOKRA
<!-- status: viewed pages/p015.png -->
<!-- flags: math, graphic, image, table -->
<!-- figure: figures/p015-f1.png -->

- Érdemes megjegyezni

$$\begin{aligned} H|0\rangle &= \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \\ H|1\rangle &= \frac{|0\rangle - |1\rangle}{\sqrt{2}}. \end{aligned}$$

<!-- note: the two formulas are in a red frame -->

## s16 · p16-17 · SZÁMONKÉRÉS
<!-- status: auto -->

Féléves feladat
- Egyénileg és csapatban is megoldható
- Mérnöki ábrándozós és programozós feladat egyaránt van
- Beadási forma: videó vagy dokumentum
Ha valaki a NHF alapján TDK-ázna, bátran szóljon!

## s17 · p18 · (no title)
<!-- status: auto -->

**Bármilyen kérdés az eddigiekhez?**

## s18 · p19 · (no title)
<!-- status: viewed pages/p019.png -->
<!-- flags: graphic, image, stacked -->
<!-- figure: figures/p019-f1.png -->
<!-- figure: figures/p019-f2.png -->
<!-- figure: figures/p019-f3.png -->
<!-- figure: figures/p019-f4.png -->
<!-- figure: figures/p019-x17.jpeg (raw layer) -->
<!-- figure: figures/p019-x147.jpeg (raw layer) -->
<!-- figure: figures/p019-x148.jpeg (raw layer) -->
<!-- figure: figures/p019-x149.jpeg (raw layer) -->
<!-- figure: figures/p019-x150.jpeg (raw layer) -->

***Összefonódás***

***(Entanglement)***

*"Wonder is from surprise, and surprise stops with experience."*

Bishop Robert South

<!-- note: section title slide; the title and the quote are in the middle, four photos around them -->

Figure (layer x17): light grey network-graph background (nodes and edges) across the top of the slide.
Use: none (decorative)

Figure (layer x147, top left): photo of a man in a flat cap and a woman with long brown hair hugging.
Use: none (decorative)

Figure (layer x149, top right): photo of football players in white kits piled on top of each other in a goal celebration on the pitch, crowd in the background (watermark "www.tenir.hu" or similar).
Use: none (decorative)

Figure (layer x150, bottom left): black-and-white photo of Albert Einstein laughing. Caption under it: "Einstein, amikor először hallott az összefonódásról".
Use: none (decorative)

Figure (layer x148, bottom right): photo of two small children hugging, the girl with a pink flower in her hair; a strip at the bottom with a globe logo ("BIPOLÁRIS VILÁG") and the text "Az ölelés megnyugtat, csökkenti a félelmeket, a szorongást, és a magányosság érzését."
Use: none (decorative)

## s19 · p20-21 · SCHRÖDINGER MACSKÁJA
<!-- status: viewed pages/p021.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p021-f1.png -->

Figure: the Schrödinger's cat thought experiment, a colour drawing of a closed room (corner of two walls and the floor). On the wall at the right: a blue box with a radioactivity symbol on its black front face; a red dashed line runs from it to a yellow box (the detector) that is mounted on the side wall. From the yellow box a hinged arm and a string lead down to a hammer. The hammer has fallen and smashed a glass flask on the floor; green liquid (poison) is spilled around the broken flask. On the left, a grey cat drawn twice, semi-transparent and overlapping: once standing/walking (alive) and once lying on its side (dead), i.e. the two states superposed. No text in the figure.
Use: image figures/p021-f1.png

<!-- note: page 20 is an empty slide (header and footer only), so the unit holds only page 21 -->

## s20 · p22 · SZUPERPOZÍCIÓ
<!-- status: viewed pages/p022.png -->
<!-- flags: math, graphic -->
<!-- figure: figures/p022-f1.png -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

## s21 · p23 · MEGLEPŐ ÁLLAPOT
<!-- status: viewed pages/p023.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p023-f1.png -->

- A 4. posztulátum alapján bontsuk fel az alábbi állapotot!

  $$|\varphi\rangle = a|00\rangle + b|11\rangle$$

  $$|\varphi\rangle = |\varphi_1\rangle \otimes |\varphi_2\rangle \;\Rightarrow\; |\varphi_1\rangle = \text{?} \qquad |\varphi_2\rangle = \text{?}$$

- Nincs ilyen felbontás!
- Kvantumállapotok két típusa
  - szorzat (product)
  - összefonódott (entangled)

<!-- note: in the second formula line the implication is a thick blue block arrow pointing right, and the two question marks are red -->

## s22 · p24 · ÖSSZEFONÓDÁS
<!-- status: viewed pages/p024.png -->
<!-- flags: math, graphic, image, stacked -->
<!-- figure: figures/p024-collage.png -->
<!-- figure: figures/p024-x168.jpeg (raw layer) -->
<!-- figure: figures/p024-x169.jpeg (raw layer) -->
<!-- figure: figures/p024-x170.jpeg (raw layer) -->
<!-- figure: figures/p024-x171.jpeg (raw layer) -->
<!-- figure: figures/p024-x172.jpeg (raw layer) -->
<!-- figure: figures/p024-x173.jpeg (raw layer) -->
<!-- figure: figures/p024-x179.jpeg (raw layer) -->

Gyakorlatilag (szinte) minden hatékony kvantumalgoritmusban és kommunikációs protokollban megjelenik

$$|\psi\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle$$

Figure: photo collage illustrating an entangled pair as two travellers who start from the same place and end up far apart. Middle right (layer x168): photo of a modern building with two red-brick wings and a curved metallic middle section; a small blue square is drawn on the middle section as the common starting point. From the blue square two curved lines go out:
- a green line goes left/up through a photo of a JAL passenger jet flying above clouds (layer x179) and ends with an arrowhead on the Sydney Opera House in a Google Earth satellite image of Sydney harbour (top left, layer x169, label "…ney Cove, Australia", "© 2007 Europa Technologies, Image © 2007 DigitalGlobe", "Google"); overlapping that image at its lower left, a photo of the Sydney Opera House from the water with a green-and-yellow ferry in front (layer x172).
- a red line goes down through a photo of a small red-and-white propeller plane in flight (registration "PH-MB…", layer x173) and ends with an arrowhead on a building in a Google Earth satellite image of a city block (bottom middle, layer x170, "Pointer 40°46'20.63" N 73°59'01.13" W", "Image © 2007 Sanborn", "Google", i.e. Lincoln Center, New York); overlapping it at its left, a photo of the interior of a large opera house auditorium with tiers of balconies, full audience and the orchestra in front (layer x171).
The formula $|\psi\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle$ stands bottom right of the collage.
Use: image figures/p024-collage.png

Links: <http://www.jal.co.jp/aircraft/aircraft/dl/group_05_1024_768.jpg>

<!-- note: the link is attached to the JAL airplane photo (its link text "group_05_1024_768" appeared in the extracted text) -->

## s23 · p25 · (no title)
<!-- status: viewed pages/p025.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p025-f1.png -->

***Hogyan állítsunk elő összefonódott párt?***

Figure: light grey network-graph background across the top of the slide.
Use: none (decorative)

## s24 · p26 · VEZÉRELT NEM KAPU (CNOT GATE)
<!-- status: viewed pages/p026.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p026-f1.png -->

Figure: circuit diagram of the CNOT gate, inside a rounded frame. Two horizontal wires, both running left to right through a rounded rectangle labelled $CNOT$ below it. Top wire: input label $|C\rangle_{IN}$ at the left end, output label $|C\rangle_{OUT}$ at the right end; inside the rectangle a filled dot (control) in the middle, with the value $x$ written under the wire left of the dot and $x$ right of the dot. Bottom wire: input label $|D\rangle_{IN}$, output label $|D\rangle_{OUT}$; inside the rectangle a circle with a plus ($\oplus$, target) directly below the control dot, with $y$ written above the wire left of it and $y \oplus x$ right of it. A vertical line joins the control dot to the $\oplus$.
Use: redraw

Felső vezeték: vezérlés (control)

Alsó vezeték: adat (data)

## s25 · p27 · CNOT-KAPU
<!-- status: viewed pages/p027.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p027-f1.png -->
<!-- figure: figures/p027-f2.png -->
<!-- figure: figures/p027-f3.png -->

Igazságtábla

<!-- note: left half of the slide -->

| IN: $x$ | IN: $y$ | OUT: $x$ | OUT: $y \oplus x$ |
|---|---|---|---|
| 0 | 0 | 0 | $0 \oplus 0 = 0$ |
| 0 | 1 | 0 | $1 \oplus 0 = 1$ |
| 1 | 0 | 1 | $0 \oplus 1 = 1$ |
| 1 | 1 | 1 | $1 \oplus 1 = 0$ |

<!-- note: on the slide the header has two rows: "IN" spanning the x, y columns and "OUT" spanning the x, y⊕x columns -->

Mátrix

<!-- note: right half of the slide -->

$$|00\rangle \to |00\rangle \qquad |01\rangle \to |01\rangle$$

$$|10\rangle \to |11\rangle \qquad |11\rangle \to |10\rangle$$

<!-- note: a light blue block arrow points down from the mappings to the matrix -->

$$\mathbf{CNOT} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}$$

Mesteregyenlet

$$CNOT : |x\rangle|y\rangle \to |x\rangle|y \oplus x\rangle$$

## s26 · p28 · CNOT MINT KLASSZIKUS MÁSOLÓGÉP
<!-- status: viewed pages/p028.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p028-f1.png -->
<!-- figure: figures/p028-f2.png -->
<!-- figure: figures/p028-f3.png -->
<!-- figure: figures/p028-f4.png -->
<!-- figure: figures/p028-f5.png -->

Ha az adat bemenet $|0\rangle$, akkor CNOT kapu a vezérlés bemenetét teszi az adat kimenetére

Figure: the same CNOT circuit diagram as in s24, smaller, at the top right: wires $|C\rangle_{IN}$ → $|C\rangle_{OUT}$ (control dot, $x$ before and after) and $|D\rangle_{IN}$ → $|D\rangle_{OUT}$ ($\oplus$ target, $y$ before, $y \oplus x$ after), box labelled $CNOT$.
Use: redraw

- Legyen a vezérlés: $|C\rangle_{IN} = a|0\rangle + b|1\rangle$
- A szuperpozíció elve alapján a kezdeti bemeneti állapot

  $$|C\rangle_{IN} \otimes |D\rangle_{IN} = a|00\rangle + b|10\rangle$$

- A CNOT kapu alkalmazását követően

  $$a|0, 0 \oplus 0\rangle + b|1, 1 \oplus 0\rangle = a|00\rangle + b|11\rangle$$

Összefonódott pár!

<!-- note: "Összefonódott pár!" is in blue -->

## s27 · p29 · BELL ÁLLAPOTOK
<!-- status: viewed pages/p029.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p029-spdc.png -->

Nézzük meg a CNOT-kaput mint összefonódást előállító áramköri elemet!

$$|\beta_{ab}\rangle = \frac{|0, b\rangle + (-1)^a|1, NOT(b)\rangle}{\sqrt{2}}$$

$$a, b \in \{0, 1\}$$

Figure (left, under the heading): circuit diagram in a rounded frame ("Copyright © 2005 John Wiley & Sons Ltd."). Two wires left to right: the top wire, input label $a$, goes through a box $H$ (Hadamard) and then into a CNOT as the control (filled dot); the bottom wire, input label $b$, is the CNOT target ($\oplus$) directly below the dot. The CNOT is drawn inside a rounded rectangle. The output on the right of both wires together is labelled $|\beta_{ab}\rangle$.
Use: redraw

<!-- note: under the circuit, the same truth table as in s25 -->

| IN: $x$ | IN: $y$ | OUT: $x$ | OUT: $y \oplus x$ |
|---|---|---|---|
| 0 | 0 | 0 | $0 \oplus 0 = 0$ |
| 0 | 1 | 0 | $1 \oplus 0 = 1$ |
| 1 | 0 | 1 | $0 \oplus 1 = 1$ |
| 1 | 1 | 1 | $1 \oplus 1 = 0$ |

Figure (right, under the formula): drawing of spontaneous parametric down-conversion (SPDC). A red laser beam (label "Laser beam") comes in from the upper left and passes through a light blue rectangular crystal (label "Crystal"); left of the crystal the slide text "(beta-barium borate) or Lithium niobate". From the exit point of the crystal the red beam continues straight on, ending in a red dot, and two light green cones open up from the same point, tilted to either side of the beam and overlapping along it: the upper/right one labelled "Vertically-polarized photons", the lower/left one "Horizontally-polarized photons". Two green lines from the crystal run to the two points where the cone rims intersect; each point is marked with a small green four-way arrow cross (polarization), and both are labelled "Entangled photons". Dash-dotted lines mark the cone axes.
Use: image figures/p029-spdc.png

Spontaneous parametric down-conversion process can split photons into type II photon pairs with mutually perpendicular polarization.

<!-- note: this caption stands left of the cones, under the "(beta-barium borate) or Lithium niobate" text -->

## s28 · p30 · BELL-ÁLLAPOTOK
<!-- status: viewed pages/p030.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p030-f1.png -->

$$\begin{aligned} |\beta_{00}\rangle &= \frac{|00\rangle + |11\rangle}{\sqrt{2}}, \\ |\beta_{01}\rangle &= \frac{|01\rangle + |10\rangle}{\sqrt{2}}, \\ |\beta_{10}\rangle &= \frac{|00\rangle - |11\rangle}{\sqrt{2}}, \\ |\beta_{11}\rangle &= \frac{|01\rangle - |10\rangle}{\sqrt{2}}. \end{aligned}$$

A Bell-állapotok ortogonálisak!

## s29 · p31 · ÁLTALÁNOSÍTOTT KVANTUM ÖSSZEFONÓ
<!-- status: viewed pages/p031.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p031-f1.png -->

Figure: circuit diagram in a rounded frame ("Copyright © 2005 John Wiley & Sons Ltd."), no wire labels. Several horizontal wires, left to right. The top wire goes through a box $H$, then is the control (filled dot) of a sequence of CNOT gates: the first CNOT targets ($\oplus$) the second wire, the second CNOT targets the third wire, then a horizontal "…" between the control dots on the top wire, and the last CNOT targets the bottom wire. Between the third wire and the bottom wire a vertical "⋮" indicates further wires.
Use: redraw

- Elegendő az összefonódott kvantumbitek egyikéhez hozzáfonódni, hogy a teljes rendszerhez hozzáfonódjunk
- Összefonódást nem tudunk előállítani klasszikus kommunikáció segítségével

## s30 · p32 · DE MIRE JÓ MINDEZ?
<!-- status: auto -->

- Szupersűrű tömörítés (superdense coding)
- Teleportáció (quantum teleportation)
- Kvantum alapú kulcsszétosztás (quantum key distribution)
- Összefonódás megosztás (entanglement swapping)
- s még nagyon sok más helyen használjuk
