# Emélkeztető a CNOT művelethez.pdf

<!-- 4 pages, 3 units, grouping: heuristic -->

## s1 · p1 · CNOT kapu
<!-- status: TODO view pages/p001.png -->
<!-- flags: math, graphic, image, table, layout -->
<!-- figure: figures/p001-f1.png -->

A CNOT kapu egy két qubites kapu. Negálja a célbit értékét, ha a vezérlőbit 1, és nem végez semmilyen műveletet a célbiten, ha a vezérlőbit 0. Klasszikus bemenetekkel Igazságtábla klasszikus bemenetekhez:

control

target

Áramköri rajz:

control

target

**CNOT előtt** **CNOT után**

**Control Target Control Target**

|0⟩ |0⟩ |0⟩ |0⟩

|0⟩ |1⟩ |0⟩ |1⟩

|1⟩ |0⟩ |1⟩ |1⟩

|1⟩ |1⟩ |1⟩ |0⟩

Klasszikus

megfelelője

## s2 · p2 · Általában egy klasszikus|𝑥𝑦⟩ bemenet esetén a kimenet a következő:
<!-- status: TODO view pages/p002.png -->
<!-- flags: math, table -->

𝐶𝑁𝑂𝑇(|𝑥𝑦⟩) = |𝑥(𝑥⊕𝑦)⟩

Ahol ⊕ az XOR műveletet jelöli. Kvantum bemenetekkel Bra-ket jelölés: Általános 2-kubit állapot bra-ket jelöléssel (CNOT előtt):

|𝜓⟩= 𝑎|*00*⟩+ 𝑏|*01*⟩+ 𝑐|*10*⟩+ 𝑑|*11*⟩

A CNOT lineáris művelet (mint minden unitér művelet), ezért:

𝐶𝑁𝑂𝑇(𝑎|*00*⟩+ 𝑏|*01*⟩+ 𝑐|*10*⟩+ 𝑑|*11*⟩)

= 𝑎 𝐶𝑁𝑂𝑇(|*00*⟩) + 𝑏 𝐶𝑁𝑂𝑇(|*01*⟩) + 𝑐 𝐶𝑁𝑂𝑇(|*10*⟩) + 𝑑 𝐶𝑁𝑂𝑇(|*11*⟩)

Azonban az igazságtábla alapján ismerjük a szuperpozíció minden tagjának hatását:

𝑎 𝐶𝑁𝑂𝑇(|*00*⟩) + 𝑏 𝐶𝑁𝑂𝑇(|*01*⟩) + 𝑐 𝐶𝑁𝑂𝑇(|*10*⟩) + 𝑑 𝐶𝑁𝑂𝑇(|*11*⟩) = 𝑎|*00*⟩+ 𝑏|*01*⟩+ 𝑐|*11*⟩+ 𝑑|*10*⟩

Vektorjelölés: Általános 2-kubit állapot bra-ket jelöléssel (CNOT előtt):

𝑎 𝑏

|𝜓⟩= [ ]

𝑐 𝑑

A CNOT művelet mátrixa:

1 0 0 0 0 1 0 0

] = [^(𝐼)

0̂

0 0 0 1 0̂ 𝑋^(])

𝐶𝑁𝑂𝑇= [

0 0 1 0

Ahol 0̂ a 2x2-es nulla almátrix. Ezzel egy tetszőleges|𝜓⟩ állapoton végzett CNOT művelet eredménye:

𝑎 𝑎

1 0 0 0

𝑏 𝑏

0 1 0 0

] [ ] = [ ]

[

𝑐 𝑑

0 0 0 1

𝑑 𝑐

0 0 1 0

(Megjegyzendő, hogy az állapotvektor utolsó két komponense felcserélődött.)

## s3 · p3-4 · Köszönetnyilvánítás
<!-- status: TODO view pages/p004.png -->
<!-- flags: table -->

The development of this course material has received funding from the European Union under grant agreement No 101081247 (QCIHungary project) and has been implemented with the support provided by the Ministry of Culture and Innovation of Hungary from the National Research, Development and Innovation Fund. Views and opinions expressed are, however, those of the author(s) only and do not necessarily reflect those of the European Union or the European Commission. Neither the European Union nor the granting authority can be held responsible for them.
