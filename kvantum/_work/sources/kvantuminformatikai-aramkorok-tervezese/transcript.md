# Kvantuminformatikai áramkörök tervezése.pdf

<!-- 6 pages, 6 units, grouping: heuristic -->

## s1 · p1 · Kvantuminformatikai áramkörök tervezése
<!-- status: viewed pages/p001.png -->
<!-- flags: math, layout -->

**Kvantuminformatikai áramkörök tervezése**

**1**

**A főnökünk átnézte két kvantumbit gyártó doboz leírását, és észrevette, hogy az egyik más globális fázissal állít elő kvantumbiteket, mint a másik. Már nem emlékszik rá, hogy melyik leírás melyik dobozhoz tartozik, így azt a feladatot adta nekünk, hogy méréssel különböztessük meg egymástól a kettőt.**

A globális fáziskülönbség egy $\ket{\psi}$ és egy $\ket{\psi'}$ kvantumbit között a következőt jelenti

$$\ket{\psi} = x\ket{0} + y\ket{1}, \qquad \ket{\psi'} = e^{i\theta}x\ket{0} + e^{i\theta}y\ket{1}$$

Ahol

$$|x|^2 + |y|^2 = 1, \qquad x, y \in C$$

A kettőt akkor tudjuk megkülönböztetni, ha $\ket{0}$ és $\ket{1}$ állapot megtalálási valószínűsége eltérő. $\ket{\psi}$ esetén a $\ket{0}$ állapot megtalálási valószínűsége $P(0) = |x|^2$, az $\ket{1}$ állapot megtalálási valószínűsége $P(1) = |y|^2$.

Mi lesz ez $\ket{\psi'}$ esetén?

## s2 · p2 · 2
<!-- status: viewed pages/p002.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p002-f1.png -->

**2**

**A főnökünk azt a feladatot adta nekünk, hogy keressünk olyan $U$ kaput, ami az állapotvektor hosszát a duplájára növeli. Lehetséges-e ez?**

Általános esetben egy 2x2-es $U$ unitér mátrix elemei a következőképpen írhatóak fel:

$$U = \begin{bmatrix} a & b \\ -e^{i\varphi}b^* & e^{i\varphi}a^* \end{bmatrix}, \qquad |a|^2 + |b|^2 = 1\ ,$$

<!-- note: the matrix is a pasted picture (figures/p002-f1.png is the whole page); it is a formula, not a figure. -->

Vegyük a következő állapotvektort:

$$\ket{\psi} = x\ket{0} + y\ket{1}, \qquad |x|^2 + |y|^2 = 1$$

Az $U$ művelet elvégzése után mi lesz az állapotvektor hossza:

$$U\ket{\psi} = x'\ket{0} + y'\ket{1}, \qquad |x'|^2 + |y'|^2 = ?$$

Bizonyítsa be a választ.

## s3 · p3 · 3
<!-- status: viewed pages/p003.png -->
<!-- flags: math -->

**3**

**A főnökünk továbbra is aggódik, hogy két kvantumállapot, ami csak egy globális fázisban különbözik egymástól valamilyen művelet után esetleg más eredményt fog adni. Azt a feladatot adta nekünk, hogy keressünk olyan $U$ kaput, mely után az eredmény a globális fázis függvényében különbözik, és amivel egy globális fázis kimutatható. Lehetséges-e ez?**

A globális fázis akkor kimutatható, ha méréssel különbséget tudunk tenni egy $\ket{\psi}$ és egy $\ket{\psi'}$ állapotvektor között, ahol

$$\ket{\psi} = x\ket{0} + y\ket{1}, \qquad \ket{\psi'} = e^{i\theta}x\ket{0} + e^{i\theta}y\ket{1}$$

Ezek között akkor tudunk különbséget tenni, ha $U\ket{\psi} = x'\ket{0} + y'\ket{1}$ és $U\ket{\psi'} = x''\ket{0} + y''\ket{1}$ esetén $|x'|^2 \neq |x''|^2$ (vagy $|y'|^2 \neq |y''|^2$). Minek kell $U$-ra teljesülnie ahhoz, hogy ezt meg tudjuk tenni?

## s4 · p4 · 4
<!-- status: viewed pages/p004.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p004-cnot-copy.png -->

**4**

**A főnökünk kipróbálta a CNOT kaput klasszikus benetekkel. Azt tapasztalta, hogy ha a target bit $\ket{0}$, akkor a kapu a control bit értékét a target bitre másolja. Ez alapján azt kéri, hogy a CNOT kapuval készítsünk független másolatot egy tetszőleges $\ket{\psi}$ kvantumbitről.**
<!-- suspect: "benetekkel" is a typo for "bemenetekkel" -->

$$\ket{\psi} = x\ket{0} + y\ket{1}, \qquad |x|^2 + |y|^2 = 1$$

Hogy néz ki egy független másolat?

$$\ket{\psi} \otimes \ket{\psi} = ?$$

Mit ad a CNOT kapu tetszőleges $\ket{\psi}$ control bemenet esetén?

Figure: kvantumáramkör két vezetékkel. A felső vezeték bemenete $\ket{\psi}$, rajta tömör fekete pont (control); a pontból függőleges vonal megy le az alsó vezetékre, amelynek bemenete $\ket{0}$, és ott $\oplus$ jel (target). A kimenetek nincsenek felcímkézve.
Use: image figures/p004-cnot-copy.png

Mikor egyezik meg a két eredmény egymással?

## s5 · p5 · 5
<!-- status: viewed pages/p005.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p005-bsc.png -->

**5**

**A főnökünk azt hallotta, hogy bináris szimmetrikus csatorna esetén a $H$ kapuval kódolt klasszikus bitek érzéketlenek a csatornában előforduló negálásra. Tervezzen olyan kódoló és dekódoló dobozt, amivel egy kvantumcsatornán klasszikus adat hibamentesen továbbítható. Igazolja az állítását.**

Figure: két rész egymás alatt. Felül a bináris szimmetrikus csatorna rajza: bal oldalon „Alice (encoder)” felirat a 0 és 1 bemenettel, jobb oldalon „Bob (decoder)” a 0 és 1 kimenettel. Zöld vízszintes nyíl 0 → 0, címkéje $1-p$; zöld vízszintes vonal 1 → 1, címkéje $1-p$; két piros, keresztező vonal 0 → 1 és 1 → 0, mindkettő címkéje $p$. Alul blokkdiagram balról jobbra: „message $m$” pont → „Alice” (zöld doboz) → $E(m)$ → „noise” (piros foltos doboz) → $y'$ → „Bob” (zöld-piros doboz) → $m = D(y')$ pont.
Use: image figures/p005-bsc.png

$$H_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

## s6 · p6 · Köszönetnyilvánítás
<!-- status: auto -->

The development of this course material has received funding from the European Union under grant agreement No 101081247 (QCIHungary project) and has been implemented with the support provided by the Ministry of Culture and Innovation of Hungary from the National Research, Development and Innovation Fund.

Views and opinions expressed are, however, those of the author(s) only and do not necessarily reflect those of the European Union or the European Commission. Neither the European Union nor the granting authority can be held responsible for them.
