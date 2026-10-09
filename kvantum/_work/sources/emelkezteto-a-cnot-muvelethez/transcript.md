# Emélkeztető a CNOT művelethez.pdf

<!-- 4 pages, 3 units, grouping: heuristic -->

## s1 · p1 · CNOT kapu
<!-- status: viewed pages/p001.png -->
<!-- flags: math, graphic, image, table, layout -->
<!-- figure: figures/p001-cnot.png -->
<!-- figure: figures/p001-cnot-xor.png -->

**CNOT kapu**

Figure: kvantumáramköri jelölés, két vízszintes vezeték. A felső vezeték bal oldalán „control” felirat és $x$ bemenet, jobb oldalon $x$ kimenet; a vezetéken egy tömör fekete pont. A pontból függőleges vonal megy le az alsó vezetékre, ahol egy bekarikázott plusz jel ($\oplus$) van. Az alsó vezeték bal oldalán $y$ bemenet és alatta „target” felirat, jobb oldalon a kimenet $y \oplus x$.
Use: image figures/p001-cnot.png

A CNOT kapu egy két qubites kapu. Negálja a célbit értékét, ha a vezérlőbit 1, és nem végez semmilyen műveletet a célbiten, ha a vezérlőbit 0.

**Klasszikus bemenetekkel**

Igazságtábla klasszikus bemenetekhez:

| CNOT előtt: Control | CNOT előtt: Target | CNOT után: Control | CNOT után: Target |
|---|---|---|---|
| $\ket{0}$ | $\ket{0}$ | $\ket{0}$ | $\ket{0}$ |
| $\ket{0}$ | $\ket{1}$ | $\ket{0}$ | $\ket{1}$ |
| $\ket{1}$ | $\ket{0}$ | $\ket{1}$ | $\ket{1}$ |
| $\ket{1}$ | $\ket{1}$ | $\ket{1}$ | $\ket{0}$ |

<!-- note: in the slide the table has a two-level header (CNOT előtt / CNOT után over Control, Target); each row is in its own colour (blue, purple, red, orange), the same colours as the basis states on p2. -->

Áramköri rajz:

Figure: két rész egymás mellett. Bal oldalon ugyanaz a CNOT áramköri jel, mint fent (felső vezeték „control”, $x$ → $x$, tömör pont; alsó vezeték „target”, $y$ → $y \oplus x$, $\oplus$ jel), alatta egy táblázat „input” ($x$, $y$) és „output” ($x$, $y+x$) oszlopokkal:

| input $x$ | input $y$ | output $x$ | output $y+x$ |
|---|---|---|---|
| $\ket{0}$ | $\ket{0}$ | $\ket{0}$ | $\ket{0}$ |
| $\ket{0}$ | $\ket{1}$ | $\ket{0}$ | $\ket{1}$ |
| $\ket{1}$ | $\ket{0}$ | $\ket{1}$ | $\ket{1}$ |
| $\ket{1}$ | $\ket{1}$ | $\ket{1}$ | $\ket{0}$ |

Jobb oldalon egy kék, lekerekített keretben „Klasszikus megfelelője” felirat: egy XOR logikai kapu, bemenetei $x$ és $y$, kimenete $y \oplus x$; az $x$ bemenetről leágazik egy vezeték, amely a kapu fölött változatlanul $x$-ként jön ki. Alatta a klasszikus igazságtábla:

| input $x$ | input $y$ | output $x$ | output $y+x$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 |

Use: image figures/p001-cnot-xor.png

## s2 · p2 · Általában egy klasszikus|𝑥𝑦⟩ bemenet esetén a kimenet a következő:
<!-- status: viewed pages/p002.png -->
<!-- flags: math, table -->

Általában egy klasszikus $\ket{xy}$ bemenet esetén a kimenet a következő:

$$CNOT(\ket{xy}) = \ket{x(x \oplus y)}$$

Ahol $\oplus$ az XOR műveletet jelöli.

**Kvantum bemenetekkel**

**Bra-ket jelölés:**

Általános 2-kubit állapot bra-ket jelöléssel (CNOT előtt):

$$\ket{\psi} = a\ket{00} + b\ket{01} + c\ket{10} + d\ket{11}$$

A CNOT lineáris művelet (mint minden unitér művelet), ezért:

$$\begin{aligned} &CNOT(a\ket{00} + b\ket{01} + c\ket{10} + d\ket{11}) \\ &\quad = a\,CNOT(\ket{00}) + b\,CNOT(\ket{01}) + c\,CNOT(\ket{10}) + d\,CNOT(\ket{11}) \end{aligned}$$

Azonban az igazságtábla alapján ismerjük a szuperpozíció minden tagjának hatását:

$$a\,CNOT(\ket{00}) + b\,CNOT(\ket{01}) + c\,CNOT(\ket{10}) + d\,CNOT(\ket{11}) = a\ket{00} + b\ket{01} + c\ket{11} + d\ket{10}$$

**Vektorjelölés:**

Általános 2-kubit állapot bra-ket jelöléssel (CNOT előtt):
<!-- suspect: under the heading "Vektorjelölés" the sentence still says "bra-ket jelöléssel"; it introduces the column-vector form, so "vektorjelöléssel" is meant -->

$$\ket{\psi} = \begin{bmatrix} a \\ b \\ c \\ d \end{bmatrix}$$

A CNOT művelet mátrixa:

$$CNOT = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix} = \begin{bmatrix} I & \hat{0} \\ \hat{0} & X \end{bmatrix}$$

Ahol $\hat{0}$ a 2x2-es nulla almátrix.

Ezzel egy tetszőleges $\ket{\psi}$ állapoton végzett CNOT művelet eredménye:

$$\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} a \\ b \\ c \\ d \end{bmatrix} = \begin{bmatrix} a \\ b \\ d \\ c \end{bmatrix}$$

(Megjegyzendő, hogy az állapotvektor utolsó két komponense felcserélődött.)

<!-- note: colours on the slide: the coefficients a, b, c, d and the basis states |00>, |01>, |10>, |11> are blue, purple, red, orange; in the CNOT matrix the upper-left 2x2 block (I) is teal and the lower-right block (X) is green. -->

## s3 · p3-4 · Köszönetnyilvánítás
<!-- status: viewed pages/p004.png -->
<!-- flags: table -->

**Köszönetnyilvánítás**

The development of this course material has received funding from the European Union under grant agreement No 101081247 (QCIHungary project) and has been implemented with the support provided by the Ministry of Culture and Innovation of Hungary from the National Research, Development and Innovation Fund.

Views and opinions expressed are, however, those of the author(s) only and do not necessarily reflect those of the European Union or the European Commission. Neither the European Union nor the granting authority can be held responsible for them.
