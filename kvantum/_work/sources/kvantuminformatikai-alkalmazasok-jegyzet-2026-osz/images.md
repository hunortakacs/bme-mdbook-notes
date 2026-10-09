# Images of text-with-images.md (img001–img037, sections 1–5)

## img001
context: "…mérhető fizikai mennyiségeket szoktuk hermitikus operátorokkal kifejezni, amely lehet:" / "A **harmadik posztulátummal** pedig definiáltuk…"

A hely operátor $\hat{x}$

A lendület operátor $\hat{p}$

Az energia (Hamilton-operátor) $\hat{H}$

## img002
context: "…az **ötödik posztulátum** a hullámfüggvény időbeli alakulását írja le Schrödinger-egyenlettel." / "Az előadás második részében pedig összehasonlítottunk…"

$$i\hbar \frac{d}{dt} |\Psi(t)\rangle = \hat{H} |\Psi(t)\rangle$$

## img003
context: "Egy mérés a mérési operátorok halmazával adható meg:" / ". Ha a megmérendő rendszer állapota"

$\{M_m\}$

## img004
context: "Ha a megmérendő rendszer állapota" / ", akkor annak a valószínűsége, hogy a mérés az *m* eredményt adja:"

$|\varphi\rangle$

## img005
context: "…annak a valószínűsége, hogy a mérés az *m* eredményt adja:" / "A mérés után a rendszer állapota az alábbi lesz:"

$$P(m \mid |\varphi\rangle) = \langle \varphi | M_m^\dagger M_m | \varphi \rangle$$

## img006
context: "A mérés után a rendszer állapota az alábbi lesz:" / "**4. posztulátum:** Ha V és Y két kvantumrendszerhez…"

$$|\varphi'\rangle = \frac{M_m |\varphi\rangle}{\sqrt{\langle \varphi | M_m^\dagger M_m | \varphi \rangle}}$$

## img007
context: "…(ez az ún. **szorzatállapotok** ellentéte). Ilyen állapot például:" / "Ez az állapot azt jelenti, hogy az összefonódott pár két tagja…"

$$\frac{1}{\sqrt{2}}|00> + \frac{1}{\sqrt{2}}|11>$$

<!-- note: the image closes the kets with ">" (greater-than sign) instead of an angle bracket; meant as \ket{00}, \ket{11}. -->

## img008
context: "Elmondta azt is, hogy mérnökként a" / "állapotot mutatja, ahol a korreláció az **azonos** értékre vonatkozik."

$$\frac{1}{\sqrt{2}}|00> + \frac{1}{\sqrt{2}}|11>$$

<!-- note: identical to img007; kets closed with ">" instead of an angle bracket. -->
<!-- suspect: the surrounding sentence "mérnökként a [img008] állapotot mutatja" seems to be missing words (e.g. "mérnökként a … állapotot használjuk, amely … mutatja"); the image itself is fine. -->

## img009
context: "…(pl. az egyik helyen ∣0⟩-t mérünk, a másik helyen pedig ∣1⟩-et):" / "Az összefonódott állapotok előállítására a **CNOT (vezérelt NEM) kapu** szolgál."

$$\frac{1}{\sqrt{2}}|01> + \frac{1}{\sqrt{2}}|10>$$

<!-- note: kets closed with ">" instead of an angle bracket. -->

## img010
context: "2. Az **adat** (data) az alsó vezeték." / "*Ábra forrása: Imre S.,* *Wiley, 2005*"

Figure: quantum circuit of the CNOT gate, drawn inside an outer rounded frame, with the label "$CNOT$" (italic) centred below an inner rounded box. Two horizontal wires run left to right through the inner box. Upper wire (control): input label $|C\rangle_{IN}$ at the left, output label $|C\rangle_{OUT}$ at the right; inside the box the wire carries $x$ on the left of the gate and $x$ on the right. Lower wire (data): input label $|D\rangle_{IN}$ at the left, output label $|D\rangle_{OUT}$ at the right; inside the box the wire carries $y$ on the left of the gate and $y \oplus x$ on the right. In the middle of the box a filled dot on the upper wire is connected by a vertical line down to a $\oplus$ (circle with a cross) on the lower wire.

Use: image images/img010.png

## img011
context: "…és rendelkeznek azzal a tulajdonsággal, hogy **ortogonálisak** egymásra." / "*Ábra forrása: Imre S.,* *Wiley, 2005*"

Figure: quantum circuit producing the Bell states, inside a rounded frame. Two horizontal wires: upper input labelled $a$, lower input labelled $b$ (italic, at the left). On the upper wire a box $H$ (Hadamard gate). Then a rounded box containing a CNOT: filled control dot on the upper wire, vertical line down to a $\oplus$ target on the lower wire. To the right of both wires, between them, the output label $|\beta_{ab}\rangle$.

Use: image images/img011.png

## img012
context: "…a fenti áramkör (Hadamard + CNOT) a **négy Bell-állapotot** állítja elő:" / "Kiemelte, hogy az összefonódás nem korlátozódik két bitre…"

$$|\Psi^+\rangle\text{:}\ \tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

$$|\Psi^-\rangle\text{:}\ \tfrac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$$

$$|\Phi^+\rangle\text{:}\ \tfrac{1}{\sqrt{2}}(|01\rangle + |10\rangle)$$

$$|\Phi^-\rangle\text{:}\ \tfrac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$$

<!-- suspect: the names are swapped against the usual convention (Nielsen–Chuang and most texts: Φ± = (|00⟩ ± |11⟩)/√2, Ψ± = (|01⟩ ± |10⟩)/√2). The circuit of img011 gives |β_00⟩ = (|00⟩+|11⟩)/√2, which is usually called Φ+. -->

## img013
context: "…létezik **több bittel is** (pl. **GHZ állapotok,** ami a hármas összefonódás)." / "*Ábra forrása: Imre S.,* *Wiley, 2005*"

Figure: quantum circuit for an n-qubit GHZ-type entangled state, inside a rounded frame. Unlabelled horizontal wires: the top wire, then the second, third, a vertical ellipsis (three dots) between the third and the last wire, then the last wire. On the top wire a box $H$ (Hadamard gate). After it, a sequence of CNOT gates all controlled by the top wire: a filled dot on the top wire with a vertical line to a $\oplus$ target on the second wire; next a filled dot on the top wire with a $\oplus$ target on the third wire; a horizontal ellipsis (three dots) between the second and third control dots region; finally a filled dot on the top wire with a $\oplus$ target on the last wire. The targets are placed left to right in order of the wires (staircase). No input or output labels.

Use: image images/img013.png

## img014
context: "A mérés áramköri jele:" / "A mérést a [img015] mátrixhalmazzal adjuk meg…"

Figure: circuit symbol of a measurement: a rectangle with a short wire entering on the left and a short wire leaving on the right; inside the rectangle a meter scale drawn as an upward arc, crossed by a diagonal needle line from lower left to upper right. No labels.

Use: image images/img014.png

## img015
context: "A mérést a" / "mátrixhalmazzal adjuk meg, ahol minden *m* skálaértékhez tartozik egy mátrix."

$\{M_m\}$

## img016
context: "A mérési posztulátum ismert mérődoboz és bemeneti állapot esetén megadja a mérési statisztikát." / "és a *k* skálaértéket mérve a hozzá tartozó mérés utáni állapotot:"

$$P(m \mid |\varphi\rangle) = \langle \varphi | M_m^\dagger M_m | \varphi \rangle$$

## img017
context: "és a *k* skálaértéket mérve a hozzá tartozó mérés utáni állapotot:" / "A teljességi reláció ugyan nem része a posztulátumnak…"

$$|\varphi'\rangle = \frac{M_m |\varphi\rangle}{\sqrt{\langle \varphi | M_m^\dagger M_m | \varphi \rangle}}$$

<!-- suspect: the text before it speaks of measuring the scale value "k", but the formula (same picture as img006) uses the index m. -->

## img018
context: "Segít ellenőrizni, hogy minden szóba jöhető érték felkerült-e a skálára." / "A mérési posztulátum egy analitikus állítás."

$$\sum_m M_m^\dagger M_m \equiv I$$

## img019
context: "…de vannak olyan ortogonális kvantumállapotok is, melyek nem klasszikusak, pl." / [img020]

$|+\rangle$

## img020
context: [img019] / "A projektív mérés konstruálása lineáris egyenletrendszerek megoldását követeli meg…"

$|-\rangle$

<!-- note: img019 and img020 stand side by side with only a space between them: "pl. |+⟩ |−⟩". -->

## img021
context: "…a folyamat józan megfontolásokkal végletesen leegyszerüsíthető:" / "Projektív mérés esetén a mérési operátorok speciális tulajdonsággal bírnak…"

$$M_m = |\varphi_m\rangle\langle\varphi_m|.$$

## img022
context: "…a mérési posztulátum és a teljességi reláció képletei egyszerűsödnek." / [img023]

$$P(m \mid |\varphi\rangle) = \langle \varphi | P_m | \varphi \rangle$$

## img023
context: [img022] / [img024]

$$|\varphi'\rangle = \frac{P_m |\varphi\rangle}{\sqrt{\langle \varphi | P_m | \varphi \rangle}}$$

## img024
context: [img023] / "A projektív mérés sajátos tulajdonsága, hogy egyszer megmérve egy elemi részecskét…"

$$\sum_m P_m \equiv I$$

<!-- note: img021–img024 use M_m in img021 and P_m in img022–img024 for the projective measurement operators, without saying P_m = M_m. -->

## img025
context: "…**a mérhetőség/megkülönböztethetőség és a másolhatóság szoros kapcsolatban állnak egymással**. Ezzel a következő órán fogunk megismerkedni." / "A POVM (Positive Operator Valued Measurement) mérések…"

Figure: circuit realising a general measurement with a projective measurement on an enlarged register, inside a rounded frame. Left: two input bundles of several parallel wires, each with a vertical ellipsis (three dots) at its top: the upper bundle labelled $|\varphi_k\rangle$, the lower bundle labelled $|\gamma\rangle$. Both bundles enter a large box $U$. Out of $U$ come the two bundles (again with vertical ellipses); above them the label $|\psi_k\rangle$. Both bundles enter a box labelled "Projective" containing a meter: an arc scale with dots marked 0, 1, 2, 3, 4 from left to right and an arrow (needle) pointing from the bottom towards the dot 3. Out of the measurement box the two bundles continue to the right edge (each with a vertical ellipsis).

Use: image images/img025.png

<!-- note: the surrounding text (two paragraphs above) explains this figure: enlarge the register, apply a suitable unitary, then a projective measurement; the upper register then shows the statistics of the general measurement. -->

## img026
context: "…jellegzetes interferenciaképet mutatva." / "Fényhullámok interferenciája (wikipédia)"

Figure: image from Wikipedia, a 4×4 grid of computed interference patterns in black, red, orange and yellow: rows of concentric rings and fringe patterns of two or more point sources, the patterns changing from cell to cell (rings at one source, hyperbolic fringe families between sources, dotted lattices of maxima). No labels, axes or values.

Use: image images/img026.png

<!-- note: the picture is small (210×210 px); it is illustrative only. -->

## img027
context: "…két normál smink vagy borotválkozó tükörből és egy adalékolt üveglapból áll, mely eltérő módon késleltetheti a fotonokat a két ágban." / "A féligáteresztő tükör a rá küldött fotonokat 50% eséllyel engedi át vagy veri vissza."

Figure: Mach–Zehnder-type quantum interferometer, inside a rounded frame; light paths drawn as dashed lines, legend in a box at the bottom right. Bottom left: a dashed box labelled $H$ containing a beam splitter (diagonal hatched bar, from lower left to upper right). Two inputs enter it: $|0\rangle$ from the left (arrow pointing right) and $|1\rangle$ from below (arrow pointing up). Two outputs leave it: $|0\rangle$ going up and $|1\rangle$ going right. The upward path hits a mirror at the top left (white bar) and turns right; the rightward path hits a mirror at the bottom right and turns up. In the middle a tall dashed box labelled $P$ holds two sheets of glass: $\alpha_0$ on the upper path and $\alpha_1$ on the lower path. The two paths meet at the top right in a second dashed box labelled $H$ with a beam splitter (same orientation). Its two outputs go to detectors (octagon with "D"): one up (arrow up), labelled $|0\rangle$, one to the right (arrow right), labelled $|1\rangle$. Legend: hatched bar = "Beam splitter"; white bar = "Mirror"; octagon with D = "Detector"; rounded square with $\alpha$ = "Sheet of glass".

Use: image images/img027.png

## img028
context: "A féligáteresztő tükrüket Hadamard-kapukkal, az üveglepot pedig egy fáziskapuval." / "Az elemzéssel meghatározhatjuk a 2 detektor megszólalási valószínűségeit:"

Figure: single-wire quantum circuit, inside a rounded frame. Input $|0\rangle$ on the left; the wire passes through three boxes in order: $H$, $P$, $H$, and ends on the right. Below the wire, upward arrows mark the state at four points: $|\varphi_0\rangle$ before the first $H$, $|\varphi_1\rangle$ between $H$ and $P$, $|\varphi_2\rangle$ between $P$ and the second $H$, $|\varphi_3\rangle$ after the second $H$.

Use: image images/img028.png

## img029
context: "Az elemzéssel meghatározhatjuk a 2 detektor megszólalási valószínűségeit:" / "Amennyiben a fázistolás 0 fok, akkor a 0-ás detektor 1 valószínűséggel szólal meg…"

$$P_0 = \cos^2\left(\frac{\Delta\alpha}{2}\right) = (1 + \cos(\Delta\alpha))\frac{1}{2},$$

$$P_1 = \sin^2\left(\frac{\Delta\alpha}{2}\right) = (1 - \cos(\Delta\alpha))\frac{1}{2}.$$

<!-- note: Δα is not defined in the text; presumably Δα = α_1 − α_0 (or α_0 − α_1), the phase difference of the two glass sheets of img027. -->

## img030
context: "…melynek egyik elemi részecskéje össze van fonódva az interferométerben repülő fotonnal." / "Az elemzést újra elvégezve a detektorok megszólalási valószínűségei a következők:"

Figure: the same interferometer as img027 (beam splitter $H$ with inputs $|0\rangle$ from the left and $|1\rangle$ from below, outputs $|0\rangle$ up and $|1\rangle$ right; two mirrors; dashed box $P$ with glass sheets $\alpha_0$ on the upper and $\alpha_1$ on the lower path; second beam splitter $H$; detectors labelled $|0\rangle$ (top) and $|1\rangle$ (right); the same legend: Beam splitter, Mirror, Detector, Sheet of glass), with a colour photo of a butterfly (yellow-orange wings with black spots) sitting on the top edge of the frame, above the $P$ box.

Use: image images/img030.png

## img031
context: "Az elemzést újra elvégezve a detektorok megszólalási valószínűségei a következők:" / "Jól látható, hogy itt a környezet változásának mértéke is befolyásolja a valószínűségeket…"

$$P_0 = (1 + \langle \Omega_0 | \Omega_1 \rangle \cos(\Delta\alpha))\frac{1}{2}$$

$$P_1 = (1 - \langle \Omega_0 | \Omega_1 \rangle \cos(\Delta\alpha))\frac{1}{2}$$

<!-- note: Ω_0, Ω_1 (the butterfly's states belonging to the two paths) are not defined in the text. -->

## img032
context: "Próbáljunk meg egy tökéletes kvantumos másológépet tervezni." / "A tervezés megkönnyítése érdekében megengedjük, hogy a környezet is hasson a Q másolóra…"

Figure: block diagram of a quantum copier, inside a rounded frame. A large rounded box $U$ contains a smaller rounded box $Q$ in its upper part. Inputs on the left: $|\varphi\rangle$ (top) and $|\mathbf{0}\rangle$ (middle, bold 0) enter $Q$; $|\Omega\rangle$ (bottom) enters $U$ below $Q$. Outputs on the right: $|\varphi\rangle$ (top) and $|\varphi\rangle$ (middle) leave $Q$; $|\Omega_\varphi\rangle$ (bottom) leaves $U$.

Use: image images/img032.png

## img033
context: "…bármely 2 bemenő vektor skaláris szorzatának meg kell egyeznie a hozzájuk tartozó kimeneti állapotok skaláris szorzatával." / "Azaz a bemeneten"

$$U : |\varphi\rangle|\mathbf{0}\rangle|\Omega\rangle \to |\varphi\rangle|\varphi\rangle|\Omega_\varphi\rangle$$

$$U : |\psi\rangle|\mathbf{0}\rangle|\Omega\rangle \to |\psi\rangle|\psi\rangle|\Omega_\psi\rangle$$

## img034
context: "Azaz a bemeneten" / "és a kimeneten"

$$\langle \Omega, \mathbf{0}, \psi | \varphi, \mathbf{0}, \Omega \rangle = \langle \psi | \varphi \rangle \langle \mathbf{0} | \mathbf{0} \rangle \langle \Omega | \Omega \rangle = \langle \psi | \varphi \rangle$$

<!-- note: the bra lists the factors in reverse order (Ω, 0, ψ), the ket in forward order (φ, 0, Ω); copied as shown. -->

## img035
context: "és a kimeneten" / "levő állapotoknak egyenlőnek kell lenniük."

$$\langle \Omega_\psi, \psi, \psi | \varphi, \varphi, \Omega_\varphi \rangle = \langle \psi | \varphi \rangle \langle \psi | \varphi \rangle \langle \Omega_\psi | \Omega_\varphi \rangle = \langle \psi | \varphi \rangle^2 \langle \Omega_\psi | \Omega_\varphi \rangle$$

## img036
context: "Ez vagy akkor teljesül ha" / "azaz a két állapot azonos vagy ha"

$\langle \psi | \varphi \rangle = \pm 1$

<!-- suspect: from ⟨ψ|φ⟩ = ⟨ψ|φ⟩²⟨Ω_ψ|Ω_φ⟩ the non-zero case gives ⟨ψ|φ⟩⟨Ω_ψ|Ω_φ⟩ = 1, i.e. |⟨ψ|φ⟩| = 1 (the states are equal up to a global phase, not only up to the sign ±1). Nielsen–Chuang, without the environment, gets ⟨ψ|φ⟩ = 1. "±1" is a narrower statement than the derivation gives. -->

## img037
context: "azaz a két állapot azonos vagy ha" / ", azaz a 2 állapot merőleges."

$\langle \psi | \varphi \rangle = 0$
