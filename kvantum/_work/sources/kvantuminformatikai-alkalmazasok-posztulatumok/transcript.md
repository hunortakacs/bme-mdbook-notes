# Kvantuminformatikai alkalmazások_posztulátumok.pdf

<!-- 20 pages, 20 units, grouping: heuristic -->

## s1 · p1 · (no title)
<!-- status: viewed pages/p001.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p001-f1.png -->
<!-- figure: figures/p001-f2.png -->

**Kvantummechanikai posztulátumok és alkalmazásuk**

Kvantuminformatikai alkalmazások
BMEVIHIAD00

**Oláh Kitti**

BME Hálózati Rendszerek és Szolgáltatások Tanszék
olah.kitti@edu.bme.hu

Budapest,
2026. 09. 21.

Figure: header banner with the HIT logo (large grey letters "HiT" with a red square as the dot of the i) and the text "HÁLÓZATI RENDSZEREK ÉS SZOLGÁLTATÁSOK TANSZÉK" in front of a light grey network graphic (nodes and edges); at the bottom right the Műegyetem logo (drawing of the university main building, "MŰEGYETEM 1782").
Use: none (decorative)

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
<!-- status: viewed pages/p005.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p005-f1.png -->

*Kvantummechanikai posztulátumok mérnöki interpretációban*

<!-- note: section divider slide. The extracted text "Elválasztó fólia címmel" (layout placeholder) is not visible on the slide and was dropped. -->

Figure: light grey network graphic (nodes and edges) across the top of the slide.
Use: none (decorative)

## s6 · p6 · I. POSZTULÁTUM
<!-- status: viewed pages/p006.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p006-bitqubit.png -->
<!-- figure: figures/p006-cat.png -->

**Állapotleírás**

**Zárt** fizikai rendszer aktuális állapota egy olyan állapotvektorral írható le, amely komplex együtthatókkal rendelkezik, egységnyi hosszú a Hilbert-térben (egy komplex lineáris vektortérben, amelyben értelmezve van a belső szorzat).

<!-- note: "Zárt" is bold and underlined on the slide. -->

Figure: illustration of a bit and a qubit. Left, under a curly brace labelled "BIT": two balls, a red one with a black arrow pointing down, labelled "0", and a blue one with a black arrow pointing up, labelled "1". Right, under a curly brace labelled "QUBIT": one ball whose upper half is blue and lower half is red, with a black arrow through it pointing diagonally up and to the right; "1" is written above the ball, "0" below it, and a small yellow ellipse sits at the arrow tip. Below the qubit, a yellow dot as legend with the text "|ψ⟩ = α|0⟩ + β|1⟩" (the yellow dot marks the state at the arrow tip).
Use: image figures/p006-bitqubit.png

Under the qubit:

$$|\alpha|^2 + |\beta|^2 = 1$$
$$\alpha, \beta \in \mathbb{C}$$

Figure: "Schrödinger's cat" written as a superposition: $\frac{1}{\sqrt{2}}$ times a ket containing a black silhouette of a sitting (living) cat, plus $\frac{1}{\sqrt{2}}$ times a ket containing a black silhouette of a cat lying on its back with its legs up (dead cat).
Use: image figures/p006-cat.png

In a red box, right:

$$|\varphi\rangle = \sum_{i=0}^{2^n-1} \varphi_i |i\rangle$$

Bottom right:

$$i\hbar \frac{d}{dt}|\Psi(t)\rangle = \hat{H}|\Psi(t)\rangle$$

Links: <https://www.shutterstock.com/hu/search/quantum-vacuum-state>

## s7 · p7 · KVANTUMBIT (QUBIT)
<!-- status: viewed pages/p007.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p007-circle.png -->

- Dirac ‘**ket**’ és ‘**bra**’ jelölés $|\varphi\rangle = \langle\varphi|^{\dagger}$
- Kvantumbit: mindkét klasszikus állapotot (bázisállapotot) tartalmazza egyidőben: szuperpozíció

$$|\varphi\rangle = \alpha|0\rangle + \beta|1\rangle = \alpha \begin{bmatrix}1\\0\end{bmatrix} + \beta \begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}\alpha\\\beta\end{bmatrix}$$

- ahol *a* és *b* komplex valószínűségi amplitúdók. Abszolút érték négyzetük adja meg a mérés eredményét (a klasszikus bázisban): $|\alpha|^2 + |\beta|^2 = 1$
- Műveletek: belső és külső szorzat

<!-- note: "ket" and "bra" are red on the slide; *a* and *b* are red italics; "komplex" is underlined. -->
<!-- suspect: the text names the amplitudes "a" and "b", while the formulas on the same slide use α and β (the figure uses a and b). -->

Figure: a unit circle with dash-dotted horizontal and vertical axes through its centre. A black arrow from the centre along the horizontal axis to the circle on the right, labelled "|0⟩" below it; a black arrow from the centre up the vertical axis to the circle on top, labelled "|1⟩" left of it. An orange arrow from the centre up and to the right to a point on the circle (about 30° above the horizontal), labelled "|φ⟩". From the tip of the orange arrow a blue dashed line runs horizontally to the vertical axis and a black dashed line runs vertically down to the horizontal axis; the projections are labelled "b" (on the vertical axis, left of it) and "a" (on the horizontal axis, below it).
Use: image figures/p007-circle.png

## s8 · p8 · HILBERT-TÉR
<!-- status: viewed pages/p008.png -->
<!-- flags: table, layout -->

- Végtelen dimenziójú euklideszi vektorterek általánosítása
- Teljes
- Metrikus

| Kvantum interpretáció | Hilbert-térben |
|---|---|
| Állapot leírás | Vektor |
| Megfigyelhető | Hermitikus operátor |
| Mérés eredménye | Operátor sajátértéke |
| Mérés valószínűsége | Belső szorzat négyzete |
| Időbeni változása | Unitér transzformáció (Schrödinger-egyenlet) |

## s9 · p9 · II. POSZTULÁTUM
<!-- status: viewed pages/p009.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p009-spheres.png -->
<!-- figure: figures/p009-f4.png -->

**Rendszer időbeli fejlődése**

A zárt rendszer időbeli fejlődése **unitér** transzformációval írható le, amely csak a kezdő és végállapottól függ. Adjungáltja megegyezik az inverzével. Sorok/oszlopok ortonormált bázist alkotnak. Kölcsönösen egyértelmű, hossztartó leképezés, ami megőrzi a belső szorzatot.

<!-- note: "unitér" is bold and underlined on the slide. -->

Figure: three Bloch spheres side by side, each a translucent grey sphere with x and y axes in the equatorial plane, "|0⟩" at the north pole and "|1⟩" at the south pole. Each shows a dark blue state arrow from the centre and a thin blue curve (the path of the rotation). Left sphere: the arrow points down to |1⟩; the curve runs from |0⟩ over the left (back) side of the sphere down to |1⟩. Middle sphere: the arrow points down to |1⟩; the curve runs from |0⟩ over the right side, past the x axis, down to |1⟩. Right sphere: the arrow points up to |0⟩; the curve is a tilted closed loop starting and ending at |0⟩ that reaches down towards the x axis on the right.
Use: image figures/p009-spheres.png

In a blue box, right of the spheres:

$$U^{\dagger} \equiv U^{-1}$$

## s10 · p10 · PAULI-KAPUK
<!-- status: viewed pages/p010.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p010-f1.png -->
<!-- figure: figures/p010-f2.png -->
<!-- figure: figures/p010-f3.png -->
<!-- figure: figures/p010-f4.png -->
<!-- figure: figures/p010-f5.png -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

Pauli X-kapu (bit-flip) :

$$\begin{bmatrix}a\\b\end{bmatrix}$$

$$|\psi\rangle = X|\varphi\rangle = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix}b\\a\end{bmatrix} = b|0\rangle + a|1\rangle$$

Pauli Z-kapu (phase-flip) :

$$\begin{bmatrix}a\\b\end{bmatrix}$$

$$|\psi\rangle = Z|\varphi\rangle = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix}a\\-b\end{bmatrix} = a|0\rangle - b|1\rangle$$

<!-- note: in each formula picture the lone column vector [a; b] stands directly above the column vector right of the matrix (probably an animation: the input vector |φ⟩ that is replaced by the result). "Pauli X-kapu (bit-flip) :" and "Pauli Z-kapu (phase-flip) :" are red. -->
<!-- suspect: as printed, the matrix multiplies the result vector ([b; a] for X, [a; -b] for Z) rather than [a; b]; the intended reading is X[a; b] = [b; a] and Z[a; b] = [a; -b]. -->

## s11 · p11 · PAULI-KAPUK
<!-- status: viewed pages/p011.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p011-f1.png -->
<!-- figure: figures/p011-f2.png -->
<!-- figure: figures/p011-f3.png -->
<!-- figure: figures/p011-f4.png -->
<!-- figure: figures/p011-f5.png -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

Pauli Y-kapu:

$$\begin{bmatrix}a\\b\end{bmatrix}$$

$$|\psi\rangle = Y|\varphi\rangle = \begin{bmatrix} 0 & -j \\ j & 0 \end{bmatrix} \begin{bmatrix}-jb\\ja\end{bmatrix} = -jb|0\rangle + ja|1\rangle$$

Fázis-kapu:

$$\begin{bmatrix}a\\b\end{bmatrix}$$

$$|\psi\rangle = P(\alpha)|\varphi\rangle = \begin{bmatrix} 1 & 0 \\ 0 & e^{j\alpha} \end{bmatrix} \begin{bmatrix}a\\e^{j\alpha}b\end{bmatrix} = a|0\rangle + e^{j\alpha}b|1\rangle$$

<!-- note: as on p10, the lone column vector [a; b] stands directly above the column vector right of the matrix. "Pauli Y-kapu:" and "Fázis-kapu:" are red. -->
<!-- suspect: as printed, the matrix multiplies the result vector ([-jb; ja] for Y, [a; e^{jα}b] for P(α)) rather than [a; b]; the intended reading is Y[a; b] = [-jb; ja] and P(α)[a; b] = [a; e^{jα}b]. -->

## s12 · p12 · HADAMARD-KAPU
<!-- status: viewed pages/p012.png -->
<!-- flags: math, graphic, image, stacked, table -->
<!-- figure: figures/p012-f1.png -->
<!-- figure: figures/p012-f2.png -->
<!-- figure: figures/p012-f3.png -->
<!-- figure: figures/p012-f4.png -->
<!-- figure: figures/p012-x82.png (raw layer) -->
<!-- figure: figures/p012-x83.png (raw layer) -->
<!-- figure: figures/p012-x84.png (raw layer) -->

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

$$\begin{bmatrix}a\\b\end{bmatrix}$$

$$|\psi\rangle = H|\varphi\rangle = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix}\frac{a+b}{\sqrt{2}}\\\frac{a-b}{\sqrt{2}}\end{bmatrix} = \frac{a+b}{\sqrt{2}}|0\rangle + \frac{a-b}{\sqrt{2}}|1\rangle$$

Hadamard-kapu **unitér transzformáció** és **hermitikus** is, emiatt:

$$\begin{aligned} H^{\dagger} &= H \\ H^{-1} &= H \\ H^{\dagger}H &= I \end{aligned}$$

In a red box, right:

$$H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}},$$
$$H|1\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}.$$

<!-- note: the stacked layers are three separate formula pictures: x84 is the line |φ⟩ = a|0⟩ + b|1⟩, x82 the H|φ⟩ equation with [a; b] above the result vector, x83 the boxed H|0⟩, H|1⟩ formulas. As on p10, the column vector [a; b] stands directly above the column vector right of the matrix. -->
<!-- suspect: as printed, (1/√2)[[1, 1], [1, -1]] multiplies the result vector [(a+b)/√2; (a-b)/√2] rather than [a; b]; the intended reading is H[a; b] = [(a+b)/√2; (a-b)/√2]. -->

## s13 · p13 · BLOCH-GÖMB
<!-- status: viewed pages/p013.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p013-f1.png -->
<!-- figure: figures/p013-f2.png -->

- https://bloch.kherb.io/
- https://www.justqlabs.com/simulator
- $|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle$

Figure: screenshot of an online Bloch sphere simulator on a black background. A wireframe sphere with three coloured axes through its centre: a green vertical axis labelled "+Z |0⟩" at the top and "−Z |1⟩" at the bottom, a red axis labelled "+X" (right) and "−X" (left), and a blue axis labelled "+Y" (upper left) and "−Y" (lower right). A magenta state arrow points from the centre straight up to +Z. Along the bottom: "|ψ⟩ = cos( 0 ) |0⟩ + e^{i( 0 )} sin( 0 ) |1⟩" with the three angle fields set to 0, and two buttons "UNDO" and "RESET" at the bottom right.
Use: image figures/p013-f2.png

Links: <https://bloch.kherb.io/>, <https://www.justqlabs.com/simulator>

## s14 · p14 · III. POSZTULÁTUM
<!-- status: viewed pages/p014.png -->
<!-- flags: math, graphic, image, table -->
<!-- figure: figures/p014-f1.png -->
<!-- figure: figures/p014-f2.png -->
<!-- figure: figures/p014-f3.png -->

**Mérés**

Legyen $\{m\}$ a mérés lehetséges eredményeinek a halmaza. Egy mérés a mérési operátorok halmazával adható meg: $\{M_m\}$. Ha a megmérendő rendszer állapota $|\varphi\rangle$ akkor annak a valószínűsége, hogy a mérés az $m$ eredményt adja:

In an orange box:

$$P(m \mid |\varphi\rangle) = \langle\varphi|M_m^{\dagger} M_m|\varphi\rangle$$

Figure: diagram of a measurement. A light blue rounded box labelled "mérődoboz" (in italics) holds a measuring gauge (yellow semicircular scale with a red needle pointing up and to the right). A thick black horizontal line runs across the whole diagram through the upper part of the box; "Klasszikus világ" is written above the line, "Kvantumvilág" below the box. An arrow labelled "|φ⟩" enters the box from the left, and an arrow leaves the box to the right, labelled "|φ′⟩".
Use: redraw

A mérés után a rendszer állapota az alábbi lesz:

In an orange box:

$$|\varphi'\rangle = \frac{M_m|\varphi\rangle}{\sqrt{\langle\varphi|M_m^{\dagger} M_m|\varphi\rangle}}$$

## s15 · p15 · IV. POSZTULÁTUM
<!-- status: viewed pages/p015.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p015-f1.png -->

**Összetett rendszer**

Ha *V* és *Y* a két kvantumrendszerhez rendelt Hilbert-tér, akkor az ebből a két rendszerből álló összetett rendszerhez a $W = V \otimes Y$ Hilbert-tér rendelhető.

Mire használható?

Példa két kvantumbitből álló regiszterre:

$$|\varphi_1\rangle = |0\rangle$$

$$|\varphi_2\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$

$$|\varphi\rangle = |0\rangle \otimes \frac{|0\rangle + |1\rangle}{\sqrt{2}} = \frac{|00\rangle + |01\rangle}{\sqrt{2}}$$

Figure: diagram from a research paper on a nuclear-spin quantum register. In the middle, a light blue triangle labelled "Register manifold" (left of it) contains three energy levels drawn as short black bars: upper left "|↑̃, 0⟩" with an orange dot, right "|↓̃, 1⟩" with an orange dot (slightly lower than the upper left level), and lower left "|↓̃, 0⟩" with a white dot. Two curved arrows connect |↑̃, 0⟩ and |↓̃, 1⟩ in both directions. Dotted lines run to the right from the upper and the lower level. A vertical bracket on the left between the upper and the lower level is labelled "χ"; a vertical bracket on the right of the triangle between the two dotted lines is labelled "ω_n". A curved arrow leaves the |↓̃, 0⟩ level to the left and is crossed out with "×". Three grey cones zoom from the levels to circles: from |↑̃, 0⟩ up to a circle labelled "Nuclear ensemble" (a 2×3 grid of blue nuclear spins, each a ball with a down-pointing triangle, with "..." marks), next to which an "Electron spin" (white ball with an up-pointing arrow, orange glow) exchanges with the ensemble via two curved arrows; from |↓̃, 0⟩ down left to a circle with the same blue grid, next to a white electron spin pointing down, with no arrows; from |↓̃, 1⟩ down right to a circle with a yellow glow in which one nuclear spin, labelled "i", is flipped to point up, next to a white electron spin pointing down that exchanges with the ensemble via two curved arrows, with "Σ_{i=1}^{N}" written below the circle.
Use: image figures/p015-f1.png

## s16 · p16 · KVANTUMREGISZTER
<!-- status: viewed pages/p016.png -->
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

$$|\varphi\rangle = a|0\rangle + b|1\rangle$$

$$|\varphi\rangle^{\otimes 2} = a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle$$

$$|\varphi\rangle^{\otimes 4} = a|0000\rangle + b|0001\rangle + \ldots + o|1110\rangle + p|1111\rangle$$

<!-- suspect: the tensor power of the single-qubit state a|0⟩ + b|1⟩ would have product coefficients (a², ab, ba, b² for ⊗2), not independent a, b, c, d; the slide reuses a and b with a new meaning and presumably means a general 2- and 4-qubit register state. -->

## s17 · p17 · SZÁMOLJUNK!
<!-- status: viewed pages/p017.png -->
<!-- flags: math, graphic, layout -->
<!-- figure: figures/p017-f1.png -->
<!-- figure: figures/p017-f2.png -->
<!-- figure: figures/p017-f3.png -->
<!-- figure: figures/p017-f4.png -->
<!-- figure: figures/p017-f5.png -->
<!-- figure: figures/p017-f6.png -->

Left column:

$$|0\rangle \otimes \frac{|0\rangle + |1\rangle}{\sqrt{2}} = \boldsymbol{\frac{|00\rangle + |01\rangle}{\sqrt{2}}}$$

$$|0\rangle \otimes \frac{|1\rangle + |0\rangle}{\sqrt{2}} = \boldsymbol{\frac{|01\rangle + |00\rangle}{\sqrt{2}}}$$

$$\frac{|0\rangle + |1\rangle}{\sqrt{2}} \otimes |0\rangle = \boldsymbol{\frac{|00\rangle + |10\rangle}{\sqrt{2}}}$$

$$|1\rangle \otimes \frac{|0\rangle + |1\rangle}{\sqrt{2}} = \boldsymbol{\frac{|10\rangle + |11\rangle}{\sqrt{2}}}$$

$$\frac{|0\rangle + |1\rangle}{\sqrt{2}} \otimes |1\rangle = \boldsymbol{\frac{|01\rangle + |11\rangle}{\sqrt{2}}}$$

$$\frac{|0\rangle + |1\rangle}{\sqrt{2}} \otimes \frac{|0\rangle + |1\rangle}{\sqrt{2}} = \boldsymbol{\frac{|00\rangle + |01\rangle + |10\rangle + |11\rangle}{2}}$$

Right column (beside the first two lines of the left column):

$$(\alpha|0\rangle + \beta|1\rangle) \otimes |0\rangle = \boldsymbol{\alpha|00\rangle + \beta|10\rangle}$$

$$|0\rangle \otimes (\alpha|0\rangle + \beta|1\rangle) = \boldsymbol{\alpha|00\rangle + \beta|01\rangle}$$

<!-- note: on the slide the results (right-hand sides) are set in bold. -->

## s18 · p18 · (no title)
<!-- status: viewed pages/p018.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p018-f1.png -->

**Kvantummechanikai posztulátumok fizikusi interpretációja**

<!-- note: section divider slide. The extracted text "Elválasztó fólia címmel" (layout placeholder) is not visible on the slide and was dropped. -->

Figure: light grey network graphic (nodes and edges) across the top of the slide.
Use: none (decorative)

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
<!-- status: viewed pages/p020.png -->
<!-- flags: graphic, image, no-text -->
<!-- figure: figures/p020-f1.png -->
<!-- figure: figures/p020-f2.png -->
<!-- figure: figures/p020-f3.png -->

Figure: closing slide: light grey network graphic at the top, the HIT logo ("HiT" with the text "HÁLÓZATI RENDSZEREK ÉS SZOLGÁLTATÁSOK TANSZÉK") and the Műegyetem logo ("MŰEGYETEM 1782") in the middle, and a large dark red area below.
Use: none (decorative)
