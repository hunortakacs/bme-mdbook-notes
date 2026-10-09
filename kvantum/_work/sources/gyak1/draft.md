# gyak1.pdf

<!-- 24 pages, 24 units, grouping: heuristic -->

## s1 · p1 · (no title)
<!-- status: TODO view pages/p001.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p001-f1.png -->
<!-- figure: figures/p001-f2.png -->

**Basic operations of quantum informatics** (Műveletek kvantumbitekkel és kvantumregiszterekkel) **Practice** Kvantuminformatikai alkalmazások **Dr. Balázs Solymos Dr. László Bacsárdi**

Department of Networked Systems and Services Faculty of Electrical Engineering and Informatics *bacsardi@hit.bme.hu*, solymosb@hit.bme.hu

Links: <mailto:bacsardi@hit.bme.hu>

## s2 · p2 · POSTULATES OF QUANTUM MECHANICS FROM ENGINEERING POINT OF VIEW
<!-- status: TODO view pages/p002.png -->
<!-- flags: math, graphic, image, table -->
<!-- figure: figures/p002-f1.png -->

1^(th) postulate: *quantum bit*
- Vector in Hilbert space
2^(nd) postulate : *logic gates*
- Unitary transform
- Elementary logic gates
3^(rd) postulate : *Q/C conversion*
- Measurement statistics
- Post measurement state
4^(th) postulate : *registers*
- Tensor product

## s3 · p3 · QUBIT NOTATION
<!-- status: TODO view pages/p003.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p003-f1.png -->

- Inner product:
- Outer product:
- Tensor product:
𝜓1 ∙

𝜓ۧ 𝜙=

𝜓2 ∙

𝜙1 𝜓1𝜙1 𝜙2 𝜓1𝜙2

=

𝜙1 𝜓2𝜙1 𝜙2 𝜓2𝜙2

## s4 · p4 · BRA-KET NOTATION
<!-- status: TODO view pages/p004.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p004-f1.png -->

- Qubit:
- Inner product:
- Outer product:
- Tensor product:
𝜙1 𝜓1𝜙1

𝜓1 ∙

𝜙2 𝜓1𝜙2

𝜓⨂ۧ 𝜙=ۧ 𝜓ۧ 𝜙=

=

𝜙1 𝜓2𝜙1

𝜓2 ∙

𝜙2 𝜓2𝜙2

## s5 · p5 · QUANTUM GATES AS UNITARY OPERATORS
<!-- status: TODO view pages/p005.png -->
<!-- flags: graphic, image, stacked -->
<!-- figure: figures/p005-f1.png -->
<!-- figure: figures/p005-x45.png (raw layer) -->
<!-- figure: figures/p005-x46.png (raw layer) -->

## s6 · p6 · LET’S CALCULATE!
<!-- status: TODO view pages/p006.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p006-f1.png -->
<!-- figure: figures/p006-f2.png -->

## s7 · p7 · LET’S CALCULATE!
<!-- status: TODO view pages/p007.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p007-f1.png -->
<!-- figure: figures/p007-f2.png -->
<!-- figure: figures/p007-f3.png -->

|𝜓= ^(1)
- 0 1
𝜓ۧ 𝜙=

2

|𝜙=

1

2

1

1

2

1 ∙

1

2

= = ^(1) (ۧ|00 +ۧ |01 )ۧ

1

2

1

2

2

0

2

0 ∙

1

0

2

## s8 · p8 · LET’S CALCULATE!
<!-- status: TODO view pages/p008.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p008-f1.png -->
<!-- figure: figures/p008-f2.png -->

1

(ۧ|00 +ۧ |01 )

2

1

(ۧ|00 +ۧ |01 )

2

1

(ۧ|00 +ۧ |10 )
- 2
1

(ۧ|10 +ۧ |11 )
- 2
1

(ۧ|01 +ۧ |11 )

2

1 2 ^((ۧ|00) ^(+ۧ |01) ^(+ۧ |10) ^(+ۧ |11) ^())
      - aۧ|00 +ۧ 𝑏|10
      - aۧ|00 +ۧ 𝑏|01

## s9 · p9 · BASIS STATES
<!-- status: TODO view pages/p009.png -->
<!-- flags: math, graphic -->
<!-- figure: figures/p009-f1.png -->
<!-- figure: figures/p009-f2.png -->
<!-- figure: figures/p009-f3.png -->
<!-- figure: figures/p009-f4.png -->

Can the following states form a valid basis?

|ۧ+ = ^(1) |0 + ^(1) |1

2ۧ

2ۧ

|ۧ−= ^(1) |0 −^(1) |1

2

2

## s10 · p10 · BASIS STATES
<!-- status: TODO view pages/p010.png -->
<!-- flags: math, graphic, layout -->
<!-- figure: figures/p010-f1.png -->
<!-- figure: figures/p010-f2.png -->
<!-- figure: figures/p010-f3.png -->
<!-- figure: figures/p010-f4.png -->

Can the following states form a valid basis?

1

1

1

2
- 2ۧ ^(|0) ^(+) 2ۧ ^(|1 =)
|ۧ−=

|ۧ+ =

1

2

Check orthogonality:

1

2

−1

2

1 1

1

1

2ۧ ^(|0) ^(−) 2ۧ ^(|1) ^(=) 2 2

〈+ |ۧ−=

1

1

1

2

2ۧ ^(|0) ^(−) 2ۧ ^(|1 =)

−1

2

1 1 1 −1

2 2 ^(+) 2 2 ^(= 0)

=

Since the result is 0, they are orthogonal, and thus, can form a valid basis.

## s11 · p11 · LET’S WRITE SOME QUBITS
<!-- status: TODO view pages/p011.png -->
<!-- flags: math -->

- Define a qubit, which when measured (in the *|ۧ0* *, |ۧ1* basis) will give
a result of “1” every time!
- Define a qubit, which gives back 0 with 50% of probability!
- Do the same for measurements in the (in the *|ۧ+* *, |ۧ−* basis)

## s12 · p12 · PAULI X GATE
<!-- status: TODO view pages/p012.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p012-f1.png -->

- Pauli X gate, or bit-flip gate
- Symbol:
- Matrix: *X =* ^(0)
1
    - 1 0
- Its operation on *𝜑= 𝑎0* *+ 𝑏1* = ^(𝑎)
            - 𝑏
𝑎 𝑏
- X 𝜑=
= 𝑏0 + 𝑎1

0 1 1 0

## s13 · p13 · PAULI Z GATE
<!-- status: TODO view pages/p013.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p013-f1.png -->

- Pauli Z gate, or phase-flip gate
- Symbol:
- Matrix: *Z =* ^(1)
0
    - 0 −1
- Its operation on *𝜑= 𝑎0* *+ 𝑏1* = ^(𝑎)
            - 𝑏
𝑎 𝑏
- Z 𝜑=
*= 𝑎*0 −𝑏1

1 0 0 −1

## s14 · p14 · PAULI Y GATE
<!-- status: TODO view pages/p014.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p014-f1.png -->

- Its operation on *𝜑= 𝑎0* *+ 𝑏1* = ^(𝑎)
- Pauli Y gate
- Symbol:
- Matrix: *Y =* ^(0)
−𝑖
    - 𝑖 0
𝑎 𝑏
- Y *𝜑=*
0 −𝑖 𝑖 0
            - 𝑏
*= −𝑏𝑖*0 + 𝑎𝑖1

## s15 · p15 · PHASE ROTATOR
<!-- status: TODO view pages/p015.png -->
<!-- flags: math -->

- Phase rotator
𝑃𝛼
- Symbol:
- Alternative symbols (for a particular phase)
- Matrix: P 𝛼= ^(1)
0
    - 0 𝑒^(𝑖𝛼)
- Its operation on *𝜑= 𝑎0* *+ 𝑏1* = ^(𝑎)
            - 𝑏
𝑎 𝑏

= 𝑎0 + 𝑒^(𝑖𝛼)1
- P 𝜑=
1 0 0 𝑒^(𝑖𝛼)

## s16 · p16 · HADAMARD GATE
<!-- status: TODO view pages/p016.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p016-f1.png -->
<!-- figure: figures/p016-f2.png -->
<!-- figure: figures/p016-f3.png -->
<!-- figure: figures/p016-f4.png -->
<!-- figure: figures/p016-f5.png -->

- Hadamard gate
- Symbol:
1

1

2

2
- Matrix: *H =* 1
1

−

2

2
- Its operation on *𝜑= 𝑎0* *+ 𝑏1* = ^(𝑎)
                      - 𝑏
𝑎 𝑏

1

1

1

1
- H 𝜑=
= 𝑎 0 + 1 + b 0 −1 =

2

2

2
                        - 2
1
          - 1
−

2
          - 2
1

1

2 ^((𝑎+ 𝑏)) ^(0) ^(+) 2 ^((𝑎−𝑏)) ^(1)

## s17 · p17 · CNOT GATE
<!-- status: TODO view pages/p017.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p017-f1.png -->
<!-- figure: figures/p017-f2.png -->

- Symbol:
      - Truth table:
1 0 0 0 0 1 0 0
- Matrix: *CNOT =*
0 0 0 1 0 0 1 0

𝐶𝑁𝑂𝑇 (𝑎|00 +ۧ 𝑏|01 +ۧ 𝑐|10 +ۧ 𝑑|11 ) =ۧ 𝑎|00 +ۧ 𝑏|01 +ۧ 𝑑|10 +ۧ 𝑐|11

## s18 · p18 · LET’S TRY TO CREATE MEASUREMENT OPERATONS
<!-- status: TODO view pages/p018.png -->
<!-- flags: graphic, image, table -->
<!-- figure: figures/p018-f1.png -->
<!-- figure: figures/p018-f2.png -->

- Take the set of two orthogonal states
(for example:

)
- How does the projective operator look like?

## s19 · p19 · CONSTRUCTING A PROJECTIVE MEASUREMENT OPERATOR
<!-- status: TODO view pages/p019.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p019-f1.png -->

- Start with two orthogonal states:

## s20 · p20 · CONSTRUCTING A PROJECTIVE MEASUREMENT OPERATOR
<!-- status: TODO view pages/p020.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p020-f1.png -->
<!-- figure: figures/p020-f2.png -->
<!-- figure: figures/p020-f3.png -->

- Start with two orthogonal states :
- To find 𝑀0:
†𝑀0|ۧ0 = 1

ۦ|

0 𝑀0

†𝑀0|ۧ1 = 0

ۦ|

1 𝑀0

𝑀0𝑀0 = 𝑀0
- Searching for 𝑀0 in the following form:

## s21 · p21 · 3RD POSTULATE IN CASE OF PROJECTIVE MEASUREMENTS (1)
<!-- status: TODO view pages/p021.png -->
<!-- flags: math, layout -->

- To find 𝑀0 we have to solve:*ۦ|*
†𝑀0|ۧ0 = 1

1 =ۦ|

0 𝑀0

† 𝑎

1

𝑎 𝑏

𝑏

0 ^(=)

𝑐 𝑑 𝑐 𝑑

𝑎^(∗) 𝑐^(∗)

𝑎 𝑏

1 0

𝑏^(∗) 𝑑^(∗)

𝑐 𝑑

†𝑀0|ۧ1 = 0

0 =ۦ|

1 𝑀0

† 𝑎

0

𝑎 𝑏

𝑏

1 ^(=)

𝑐 𝑑 𝑐 𝑑

𝑎^(∗) 𝑐^(∗)

𝑎 𝑏

0 1

𝑏^(∗) 𝑑^(∗)

𝑐 𝑑

𝑀0 = ^(𝑎)

𝑏

†𝑀0|ۧ0 = 1

0 𝑀0

𝑐 𝑑

†𝑀0|ۧ1 = 0

ۦ|

1 𝑀0

𝑀0𝑀0 = 𝑀0

0

1 0 ^(⟹𝑎2 +) ^(𝑐2) ^(= 1)

1

0 1 ^(⟹𝑏2 +) ^(𝑑2) ^(= 0)

## s22 · p22 · CONSTRUCTING A PROJECTIVE MEASUREMENT OPERATOR
<!-- status: TODO view pages/p022.png -->
<!-- flags: math, layout -->

- To find 𝑀0 we have to solve:
†𝑀0|ۧ0 = 1

ۦ|

0 𝑀0

†𝑀0|ۧ1 = 0

ۦ|

1 𝑀0

𝑀0𝑀0 = 𝑀0

𝑎 0

𝑐 0 ^(=) ^(𝑎)

0

𝑎 0

𝑐 0

𝑐 0

𝑀0 = ^(1)

0
- Solution:
0 0

𝑀1 = ^(0)

0
- Similarly:
0 1

𝑀0 = ^(𝑎)

𝑏

𝑐 𝑑

𝑎^(2) + 𝑐^(2) = 1 𝑏^(2) + 𝑑^(2) = 0

𝑏^(2) ≥0 𝑏= 𝑑= 0 𝑑^(2) ≥0

𝑀0 = ^(𝑎)

0

𝑎^(2) = 𝑎

𝑐 0

𝑎𝑐= 𝑐

## s23 · p23 · CONSTRUCTING A PROJECTIVE MEASUREMENT OPERATOR
<!-- status: TODO view pages/p023.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p023-f1.png -->
<!-- figure: figures/p023-f2.png -->
<!-- figure: figures/p023-f3.png -->
<!-- figure: figures/p023-f4.png -->
<!-- figure: figures/p023-f5.png -->
<!-- figure: figures/p023-f6.png -->

Completeness:

Practical notation:

Conclusion

## s24 · p24 · PLATO'S ALLEGORY OF THE CAVE
<!-- status: TODO view pages/p024.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p024-f1.png -->
