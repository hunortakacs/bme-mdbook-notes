# Kvantuminformatikai áramkörök tervezése.pdf

<!-- 6 pages, 6 units, grouping: heuristic -->

## s1 · p1 · Kvantuminformatikai áramkörök tervezése
<!-- status: TODO view pages/p001.png -->
<!-- flags: math, layout -->

**A főnökünk átnézte két kvantumbit gyártó doboz leírását, és észrevette, hogy az egyik más globális** **fázissal állít elő kvantumbiteket, mint a másik. Már nem emlékszik rá, hogy melyik leírás melyik** **dobozhoz tartozik, így azt a feladatot adta nekünk, hogy méréssel különböztessük meg egymástól a**

A globális fáziskülönbség egy |𝜓⟩ és egy |𝜓′⟩ kvantumbit között a következőt jelenti 1

**kettőt.**

Ahol

𝑃(1) = |𝑦|^(2).

Mi lesz ez |𝜓′⟩ esetén?

|𝜓⟩= 𝑥|0⟩+ 𝑦|1⟩, |𝜓′⟩= 𝑒^(𝑖𝜃)𝑥|0⟩+ 𝑒^(𝑖𝜃)𝑦|1⟩

|𝑥|^(2) + |𝑦|^(2) = 1, 𝑥, 𝑦∈𝐶

A kettőt akkor tudjuk megkülönböztetni, ha |0⟩ és |1⟩ állapot megtalálási valószínűsége eltérő. |𝜓⟩ esetén a |0⟩ állapot megtalálási valószínűsége 𝑃(0) = |𝑥|^(2), az |1⟩ állapot megtalálási valószínűsége

## s2 · p2 · 2
<!-- status: TODO view pages/p002.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p002-f1.png -->

**A főnökünk azt a feladatot adta nekünk, hogy keressünk olyan** 𝑼 **kaput, ami az állapotvektor hosszát** **a duplájára növeli. Lehetséges-e ez?**

Általános esetben egy 2x2-es 𝑈 unitér mátrix elemei a következőképpen írhatóak fel:

Vegyük a következő állapotvektort:

|𝜓⟩= 𝑥|0⟩+ 𝑦|1⟩, |𝑥|^(2) + |𝑦|^(2) = 1

Az 𝑈 művelet elvégzése után mi lesz az állapotvektor hossza:

|𝑥′|^(2) + |𝑦′|^(2) =?

𝑈|𝜓⟩= 𝑥′|0⟩+ 𝑦′|1⟩,

Bizonyítsa be a választ.

## s3 · p3 · 3
<!-- status: TODO view pages/p003.png -->
<!-- flags: math -->

**A főnökünk továbbra is aggódik, hogy két kvantumállapot, ami csak egy globális fázisban különbözik** **egymástól valamilyen művelet után esetleg más eredményt fog adni. Azt a feladatot adta nekünk,** **hogy keressünk olyan** 𝑼 **kaput, mely után az eredmény a globális fázis függvényében különbözik, és** **amivel egy globális fázis kimutatható. Lehetséges-e ez?**

A globális fázis akkor kimutatható, ha méréssel különbséget tudunk tenni egy |𝜓⟩ és egy |𝜓′⟩ állapotvektor között, ahol

|𝜓⟩= 𝑥|0⟩+ 𝑦|1⟩, |𝜓′⟩= 𝑒^(𝑖𝜃)𝑥|0⟩+ 𝑒^(𝑖𝜃)𝑦|1⟩

Ezek között akkor tudunk különbséget tenni, ha 𝑈|𝜓⟩= 𝑥′|0⟩+ 𝑦′|1⟩ és 𝑈|𝜓′⟩= 𝑥′′|0⟩+ 𝑦′′|1⟩ esetén |𝑥′|^(2) ≠|𝑥′′|^(2) (vagy |𝑦′|^(2) ≠|𝑦′′|^(2)). Minek kell 𝑈-ra teljesülnie ahhoz, hogy ezt meg tudjuk tenni?

## s4 · p4 · 4
<!-- status: TODO view pages/p004.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p004-f1.png -->

**A főnökünk kipróbálta a CNOT kaput klasszikus benetekkel. Azt tapasztalta, hogy ha a target bit** |𝟎⟩**,** **akkor a kapu a control bit értékét a target bitre másolja. Ez alapján azt kéri, hogy a CNOT kapuval** **készítsünk független másolatot egy tetszőleges** |𝝍⟩ **kvantumbitről.**

|𝜓⟩= 𝑥|0⟩+ 𝑦|1⟩, |𝑥|^(2) + |𝑦|^(2) = 1

Hogy néz ki egy független másolat?

|𝜓⟩⨂|𝜓⟩=?

Mit ad a CNOT kapu tetszőleges |𝜓⟩ control bemenet esetén?

|𝜓⟩

|0⟩

Mikor egyezik meg a két eredmény egymással?

## s5 · p5 · 5
<!-- status: TODO view pages/p005.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p005-f1.png -->

**A főnökünk azt hallotta, hogy bináris szimmetrikus csatorna esetén a** 𝑯 **kapuval kódolt klasszikus** **bitek érzéketlenek a csatornában előforduló negálásra. Tervezzen olyan kódoló és dekódoló dobozt,** **amivel egy kvantumcsatornán klasszikus adat hibamentesen továbbítható. Igazolja az állítását.**

## s6 · p6 · Köszönetnyilvánítás
<!-- status: auto -->

The development of this course material has received funding from the European Union under grant agreement No 101081247 (QCIHungary project) and has been implemented with the support provided by the Ministry of Culture and Innovation of Hungary from the National Research, Development and Innovation Fund.

Views and opinions expressed are, however, those of the author(s) only and do not necessarily reflect those of the European Union or the European Commission. Neither the European Union nor the granting authority can be held responsible for them.
