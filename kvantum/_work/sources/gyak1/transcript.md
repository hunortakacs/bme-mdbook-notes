# gyak1.pdf

<!-- 24 pages, 24 units, grouping: heuristic -->

## s1 · p1 · (no title)
<!-- status: viewed pages/p001.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p001-f1.png -->
<!-- figure: figures/p001-f2.png -->

**Basic operations of quantum informatics**

(Műveletek kvantumbitekkel és kvantumregiszterekkel)

**Practice**

Kvantuminformatikai alkalmazások

**Dr. Balázs Solymos Dr. László Bacsárdi**

Department of Networked Systems and Services
Faculty of Electrical Engineering and Informatics
[bacsardi@hit.bme.hu](mailto:bacsardi@hit.bme.hu), solymosb@hit.bme.hu

Links: <mailto:bacsardi@hit.bme.hu>

Figure: HIT logo ("DEPARTMENT OF NETWORKED SYSTEMS AND SERVICES") over a grey network-graph background at the top of the slide; BME logo (building drawing, "MŰEGYETEM 1782") at the bottom right.

Use: none (decorative)

## s2 · p2 · POSTULATES OF QUANTUM MECHANICS FROM ENGINEERING POINT OF VIEW
<!-- status: viewed pages/p002.png -->
<!-- flags: math, graphic, image, table -->
<!-- figure: figures/p002-f1.png -->

<!-- note: layout: the postulate list is on the left; on the right each postulate has a framed formula beside it (red, brown, orange, green frames, top to bottom). The formulas are given here after the postulate they stand next to. -->

- 1<sup>th</sup> postulate: *quantum bit* <!-- suspect: "1th" instead of "1st" -->
  - Vector in Hilbert space

$$|\varphi\rangle = \sum_{i=0}^{2^n-1} \varphi_i |i\rangle$$

- 2<sup>nd</sup> postulate : *logic gates*
  - Unitary transform
  - Elementary logic gates

$$U^\dagger \equiv U^{-1}$$

- 3<sup>rd</sup> postulate : *Q/C conversion*
  - Measurement statistics
  - Post measurement state

$$P(m \mid |\varphi\rangle) = \langle\varphi|M_m^\dagger M_m|\varphi\rangle$$

$$|\varphi'\rangle = \frac{M_m|\varphi\rangle}{\sqrt{\langle\varphi|M_m^\dagger M_m|\varphi\rangle}}$$

- 4<sup>th</sup> postulate : *registers*
  - Tensor product

$$|\varphi\rangle = |0\rangle \otimes \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$

<!-- note: the postulate names (quantum bit, logic gates, Q/C conversion, registers) are in red on the slide; the frames are pasted formula pictures, no figure. -->

## s3 · p3 · QUBIT NOTATION
<!-- status: viewed pages/p003.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p003-f1.png -->

- Inner product:

$$\langle A|B\rangle \doteq A_1^*B_1 + A_2^*B_2 + \cdots + A_N^*B_N = \begin{pmatrix} A_1^* & A_2^* & \cdots & A_N^* \end{pmatrix} \begin{pmatrix} B_1 \\ B_2 \\ \vdots \\ B_N \end{pmatrix}$$

- Outer product:

$$|\phi\rangle\,\langle\psi| \doteq \begin{pmatrix} \phi_1 \\ \phi_2 \\ \vdots \\ \phi_N \end{pmatrix} \begin{pmatrix} \psi_1^* & \psi_2^* & \cdots & \psi_N^* \end{pmatrix} = \begin{pmatrix} \phi_1\psi_1^* & \phi_1\psi_2^* & \cdots & \phi_1\psi_N^* \\ \phi_2\psi_1^* & \phi_2\psi_2^* & \cdots & \phi_2\psi_N^* \\ \vdots & \vdots & \ddots & \vdots \\ \phi_N\psi_1^* & \phi_N\psi_2^* & \cdots & \phi_N\psi_N^* \end{pmatrix}$$

- Tensor product:

$$|\psi\rangle|\phi\rangle = \begin{bmatrix} \psi_1 \cdot & \begin{bmatrix} \phi_1 \\ \phi_2 \end{bmatrix} \\ \psi_2 \cdot & \begin{bmatrix} \phi_1 \\ \phi_2 \end{bmatrix} \end{bmatrix} = \begin{bmatrix} \psi_1\phi_1 \\ \psi_1\phi_2 \\ \psi_2\phi_1 \\ \psi_2\phi_2 \end{bmatrix}$$

<!-- note: the inner and outer product formulas are pasted formula pictures, no figure. -->

## s4 · p4 · BRA-KET NOTATION
<!-- status: viewed pages/p004.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p004-f1.png -->

- Qubit: $|\psi\rangle = \begin{bmatrix} \alpha \\ \beta \end{bmatrix} \quad \langle\psi| = \begin{bmatrix} \alpha^* & \beta^* \end{bmatrix},\ |\alpha|^2 + |\beta|^2 = 1$
- Inner product:

$$\langle A|B\rangle \doteq A_1^*B_1 + A_2^*B_2 + \cdots + A_N^*B_N = \begin{pmatrix} A_1^* & A_2^* & \cdots & A_N^* \end{pmatrix} \begin{pmatrix} B_1 \\ B_2 \\ \vdots \\ B_N \end{pmatrix}$$

- Outer product:

$$|\phi\rangle\,\langle\psi| \doteq \begin{pmatrix} \phi_1 \\ \phi_2 \\ \vdots \\ \phi_N \end{pmatrix} \begin{pmatrix} \psi_1^* & \psi_2^* & \cdots & \psi_N^* \end{pmatrix} = \begin{pmatrix} \phi_1\psi_1^* & \phi_1\psi_2^* & \cdots & \phi_1\psi_N^* \\ \phi_2\psi_1^* & \phi_2\psi_2^* & \cdots & \phi_2\psi_N^* \\ \vdots & \vdots & \ddots & \vdots \\ \phi_N\psi_1^* & \phi_N\psi_2^* & \cdots & \phi_N\psi_N^* \end{pmatrix}$$

- Tensor product:

$$|\psi\rangle\otimes|\phi\rangle = |\psi\rangle|\phi\rangle = \begin{bmatrix} \psi_1 \cdot & \begin{bmatrix} \phi_1 \\ \phi_2 \end{bmatrix} \\ \psi_2 \cdot & \begin{bmatrix} \phi_1 \\ \phi_2 \end{bmatrix} \end{bmatrix} = \begin{bmatrix} \psi_1\phi_1 \\ \psi_1\phi_2 \\ \psi_2\phi_1 \\ \psi_2\phi_2 \end{bmatrix}$$

<!-- note: the formulas are pasted formula pictures, no figure. -->

## s5 · p5 · QUANTUM GATES AS UNITARY OPERATORS
<!-- status: viewed pages/p005.png -->
<!-- flags: graphic, image, stacked, math -->
<!-- figure: figures/p005-f1.png -->
<!-- figure: figures/p005-x45.png (raw layer) -->
<!-- figure: figures/p005-x46.png (raw layer) -->

<!-- note: the whole slide is two pasted pictures of LaTeX output: layer x45 holds the text block, layer x46 the matrix at the bottom right. Both are transcribed here; neither is a figure. -->

**Unitary operators and matrices**

An invertible complex square matrix $U$ is unitary if its matrix inverse $U^{-1}$ equals its conjugate transpose $U^\dagger$, that is, if $U^\dagger = U^{-1}$.

Properties:

- $UU^\dagger = U^\dagger U = U^{-1}U = I$, where $I$ is the indentity. <!-- suspect: "indentity" is a typo for "identity" -->
- Given two complex vectors $x$ and $y$, multiplication by $U$ preserves their inner product; that is, $\langle x|y\rangle = \langle x|\,U^\dagger U\,|y\rangle$.
- $|\det U| = 1$.
- Its eigenspaces are orthogonal.

$$U = \begin{bmatrix} a & b \\ -\mathrm{e}^{i\phi}b^* & \mathrm{e}^{i\phi}a^* \end{bmatrix},\ |a|^2 + |b|^2 = 1$$

## s6 · p6 · LET’S CALCULATE!
<!-- status: viewed pages/p006.png -->
<!-- flags: graphic, image, math -->
<!-- figure: figures/p006-f1.png -->
<!-- figure: figures/p006-f2.png -->

<!-- note: exercises; every right-hand side is left empty on the slide. Two columns: the left column is the first six lines, the right column the last two. The formulas are pasted pictures, no figure. -->

$$|0\rangle\, \frac{|0\rangle + |1\rangle}{\sqrt{2}} =$$

$$|0\rangle\, \frac{|1\rangle + |0\rangle}{\sqrt{2}} =$$

$$\frac{|0\rangle + |1\rangle}{\sqrt{2}}\, |0\rangle =$$

$$|1\rangle\, \frac{|0\rangle + |1\rangle}{\sqrt{2}} =$$

$$\frac{|0\rangle + |1\rangle}{\sqrt{2}}\, |1\rangle =$$

$$\frac{|0\rangle + |1\rangle}{\sqrt{2}}\, \frac{|0\rangle + |1\rangle}{\sqrt{2}} =$$

$$(a|0\rangle + b|1\rangle)\, |0\rangle =$$

$$|0\rangle\, (a|0\rangle + b|1\rangle) =$$

## s7 · p7 · LET’S CALCULATE!
<!-- status: viewed pages/p007.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p007-f1.png -->
<!-- figure: figures/p007-f2.png -->
<!-- figure: figures/p007-f3.png -->

<!-- note: worked solution of the first exercise of s6. Left column: the exercise and the two vectors; right: the calculation. The formulas are pasted pictures, no figure. -->

$$|0\rangle\, \frac{|0\rangle + |1\rangle}{\sqrt{2}} =$$

$$|\psi\rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$

$$|\phi\rangle = \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}$$

$$|\psi\rangle|\phi\rangle = \begin{bmatrix} 1 \cdot & \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix} \\ 0 \cdot & \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix} \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0 \\ 0 \end{bmatrix} = \frac{1}{\sqrt{2}}(|00\rangle + |01\rangle)$$

## s8 · p8 · LET’S CALCULATE!
<!-- status: viewed pages/p008.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p008-f1.png -->
<!-- figure: figures/p008-f2.png -->

<!-- note: the exercises of s6 with their results; on the slide the right-hand sides (results) are in blue. Left column first six lines, right column the last two. The formulas are pasted pictures, no figure. -->

$$|0\rangle\, \frac{|0\rangle + |1\rangle}{\sqrt{2}} = \frac{1}{\sqrt{2}}(|00\rangle + |01\rangle)$$

$$|0\rangle\, \frac{|1\rangle + |0\rangle}{\sqrt{2}} = \frac{1}{\sqrt{2}}(|00\rangle + |01\rangle)$$

$$\frac{|0\rangle + |1\rangle}{\sqrt{2}}\, |0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)$$

$$|1\rangle\, \frac{|0\rangle + |1\rangle}{\sqrt{2}} = \frac{1}{\sqrt{2}}(|10\rangle + |11\rangle)$$

$$\frac{|0\rangle + |1\rangle}{\sqrt{2}}\, |1\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |11\rangle)$$

$$\frac{|0\rangle + |1\rangle}{\sqrt{2}}\, \frac{|0\rangle + |1\rangle}{\sqrt{2}} = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle)$$

$$(a|0\rangle + b|1\rangle)\, |0\rangle = a|00\rangle + b|10\rangle$$

$$|0\rangle\, (a|0\rangle + b|1\rangle) = a|00\rangle + b|01\rangle$$

## s9 · p9 · BASIS STATES
<!-- status: viewed pages/p009.png -->
<!-- flags: math, graphic -->
<!-- figure: figures/p009-f1.png -->
<!-- figure: figures/p009-f2.png -->
<!-- figure: figures/p009-f3.png -->
<!-- figure: figures/p009-f4.png -->

Can the following states form a valid basis?

$$|+\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$$

$$|-\rangle = \frac{1}{\sqrt{2}}|0\rangle - \frac{1}{\sqrt{2}}|1\rangle$$

<!-- note: the figure crops are pieces of the formulas, no figure. -->

## s10 · p10 · BASIS STATES
<!-- status: viewed pages/p010.png -->
<!-- flags: math, graphic, layout -->
<!-- figure: figures/p010-f1.png -->
<!-- figure: figures/p010-f2.png -->
<!-- figure: figures/p010-f3.png -->
<!-- figure: figures/p010-f4.png -->

Can the following states form a valid basis?

$$|+\rangle = \tfrac{1}{\sqrt{2}}|0\rangle + \tfrac{1}{\sqrt{2}}|1\rangle = \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix} \qquad |-\rangle = \tfrac{1}{\sqrt{2}}|0\rangle - \tfrac{1}{\sqrt{2}}|1\rangle = \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{-1}{\sqrt{2}} \end{bmatrix}$$

Check orthogonality:

$$\langle + |-\rangle = \tfrac{1}{\sqrt{2}}|0\rangle - \tfrac{1}{\sqrt{2}}|1\rangle = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{-1}{\sqrt{2}} \end{bmatrix} = \tfrac{1}{\sqrt{2}}\frac{1}{\sqrt{2}} + \tfrac{1}{\sqrt{2}}\frac{-1}{\sqrt{2}} = 0$$

<!-- note: layout: on the slide the column vector stands above the gap between the row vector and the next "=", i.e. it is the right factor of the row × column product. -->
<!-- suspect: "⟨+|−⟩ = 1/√2|0⟩ − 1/√2|1⟩" equates the inner product with the ket |−⟩; the middle expression looks wrong (it should be the bra ⟨+| applied to |−⟩, or be left out). -->

Since the result is 0, they are orthogonal, and thus, can form a valid basis.

<!-- note: the figure crops are pieces of the formulas, no figure. -->

## s11 · p11 · LET’S WRITE SOME QUBITS
<!-- status: viewed pages/p011.png -->
<!-- flags: math -->

- Define a qubit, which when measured (in the $|0\rangle, |1\rangle$ basis) will give a result of “1” every time!
- Define a qubit, which gives back 0 with 50% of probability!
- Do the same for measurements in the (in the $|+\rangle, |-\rangle$ basis) <!-- suspect: "in the (in the" is doubled -->

## s12 · p12 · PAULI X GATE
<!-- status: viewed pages/p012.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p012-f1.png -->

- Pauli X gate, or bit-flip gate
- Symbol:

Figure: quantum circuit symbol of the gate: a square box with a bold serif "X" inside, one horizontal wire entering it from the left and one leaving it to the right.

Use: redraw

- Matrix: $\mathrm{X} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$
- Its operation on $|\varphi\rangle = a|0\rangle + b|1\rangle = \begin{bmatrix} a \\ b \end{bmatrix}$
- $\mathrm{X}|\varphi\rangle = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix} = b|0\rangle + a|1\rangle$

<!-- note: layout: in the last line the matrix sits lower and the vector higher, side by side; read as the product matrix × vector. -->

## s13 · p13 · PAULI Z GATE
<!-- status: viewed pages/p013.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p013-f1.png -->

- Pauli Z gate, or phase-flip gate
- Symbol:

Figure: quantum circuit symbol of the gate: a square box with a bold serif "Z" inside, one horizontal wire entering it from the left and one leaving it to the right.

Use: redraw

- Matrix: $\mathrm{Z} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$
- Its operation on $|\varphi\rangle = a|0\rangle + b|1\rangle = \begin{bmatrix} a \\ b \end{bmatrix}$
- $\mathrm{Z}|\varphi\rangle = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix} = a|0\rangle - b|1\rangle$

<!-- note: layout: in the last line the matrix sits lower and the vector higher, side by side; read as the product matrix × vector. -->

## s14 · p14 · PAULI Y GATE
<!-- status: viewed pages/p014.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p014-f1.png -->

- Pauli Y gate
- Symbol:

Figure: quantum circuit symbol of the gate: a square box with a bold serif "Y" inside, one horizontal wire entering it from the left and one leaving it to the right.

Use: redraw

- Matrix: $\mathrm{Y} = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}$
- Its operation on $|\varphi\rangle = a|0\rangle + b|1\rangle = \begin{bmatrix} a \\ b \end{bmatrix}$
- $\mathrm{Y}|\varphi\rangle = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix} = -bi|0\rangle + ai|1\rangle$

<!-- note: layout: in the last line the matrix sits lower and the vector higher, side by side; read as the product matrix × vector. -->

## s15 · p15 · PHASE ROTATOR
<!-- status: viewed pages/p015.png -->
<!-- flags: math -->

- Phase rotator
- Symbol:

Figure: quantum circuit symbol of the gate: a square box with "$P(\alpha)$" inside, one horizontal wire entering it from the left and one leaving it to the right.

Use: redraw

- Alternative symbols (for a particular phase)

<!-- note: no alternative symbols are shown on the slide; the bullet stands alone. -->

- Matrix: $\mathrm{P}(\alpha) = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\alpha} \end{bmatrix}$
- Its operation on $|\varphi\rangle = a|0\rangle + b|1\rangle = \begin{bmatrix} a \\ b \end{bmatrix}$
- $\mathrm{P}|\varphi\rangle = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\alpha} \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix} = a|0\rangle + e^{i\alpha}|1\rangle$ <!-- suspect: the factor b is missing from the second term; the product gives a|0⟩ + b e^{iα}|1⟩ -->

<!-- note: layout: in the last line the matrix sits lower and the vector higher, side by side; read as the product matrix × vector. -->

## s16 · p16 · HADAMARD GATE
<!-- status: viewed pages/p016.png -->
<!-- flags: math, graphic, image, layout -->
<!-- figure: figures/p016-f1.png -->
<!-- figure: figures/p016-f2.png -->
<!-- figure: figures/p016-f3.png -->
<!-- figure: figures/p016-f4.png -->
<!-- figure: figures/p016-f5.png -->

- Hadamard gate
- Symbol:

Figure: quantum circuit symbol of the gate: a square box with a bold serif "H" inside, one horizontal wire entering it from the left and one leaving it to the right.

Use: redraw

- Matrix: $\mathrm{H} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$
- Its operation on $|\varphi\rangle = a|0\rangle + b|1\rangle = \begin{bmatrix} a \\ b \end{bmatrix}$
- $\mathrm{H}|\varphi\rangle = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix} = a\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) + \mathrm{b}\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = \frac{1}{\sqrt{2}}(a+b)|0\rangle + \frac{1}{\sqrt{2}}(a-b)|1\rangle$

<!-- note: layout: in the last line the matrix sits lower and the vector higher, side by side; read as the product matrix × vector. The "b" after the "+" is upright on the slide. -->

## s17 · p17 · CNOT GATE
<!-- status: viewed pages/p017.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p017-f1.png -->
<!-- figure: figures/p017-f2.png -->

<!-- note: layout: symbol and matrix on the left, truth table on the right, the equation across the bottom. -->

- Symbol:

Figure: quantum circuit symbol of the CNOT gate: two horizontal wires; on the upper wire a filled black dot (control), from which a vertical line goes down to the lower wire, ending in a circle with a plus inside (⊕, target).

Use: redraw

- Matrix: $\mathrm{CNOT} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}$

- Truth table:

Figure: truth table with the column groups IN (x, y) and OUT (x, y ⊕ x).

| IN: $x$ | IN: $y$ | OUT: $x$ | OUT: $y \oplus x$ |
|---|---|---|---|
| 0 | 0 | 0 | $0 \oplus 0 = 0$ |
| 0 | 1 | 0 | $1 \oplus 0 = 1$ |
| 1 | 0 | 1 | $0 \oplus 1 = 1$ |
| 1 | 1 | 1 | $1 \oplus 1 = 0$ |

Use: table

$$CNOT\ (a|00\rangle + b|01\rangle + c|10\rangle + d|11\rangle) = a|00\rangle + b|01\rangle + d|10\rangle + c|11\rangle$$

## s18 · p18 · LET’S TRY TO CREATE MEASUREMENT OPERATONS
<!-- status: viewed pages/p018.png -->
<!-- flags: graphic, image, table, math -->
<!-- figure: figures/p018-f1.png -->
<!-- figure: figures/p018-f2.png -->

<!-- suspect: the title says "OPERATONS" instead of "OPERATORS" -->

- Take the set of two orthogonal states
  (for example: $|\varphi_1\rangle = |0\rangle\,, |\varphi_2\rangle = |1\rangle$ )
- How does the projective operator look like?

In an orange frame at the bottom right (the 3rd postulate formulas of s2):

$$P(m \mid |\varphi\rangle) = \langle\varphi|M_m^\dagger M_m|\varphi\rangle$$

$$|\varphi'\rangle = \frac{M_m|\varphi\rangle}{\sqrt{\langle\varphi|M_m^\dagger M_m|\varphi\rangle}}$$

<!-- note: the figure crops are the pasted formula pictures, no figure. -->

## s19 · p19 · CONSTRUCTING A PROJECTIVE MEASUREMENT OPERATOR
<!-- status: viewed pages/p019.png -->
<!-- flags: graphic, image, math -->
<!-- figure: figures/p019-f1.png -->

- Start with two orthogonal states:
  $|\varphi_1\rangle = |0\rangle\,, |\varphi_2\rangle = |1\rangle$

<!-- note: the figure crop is the pasted formula picture, no figure. -->

## s20 · p20 · CONSTRUCTING A PROJECTIVE MEASUREMENT OPERATOR
<!-- status: viewed pages/p020.png -->
<!-- flags: math, graphic, image -->
<!-- figure: figures/p020-f1.png -->
<!-- figure: figures/p020-f2.png -->
<!-- figure: figures/p020-f3.png -->

- Start with two orthogonal states :
  $|\varphi_1\rangle = |0\rangle\,, |\varphi_2\rangle = |1\rangle$
- To find $M_0$:

$$\begin{aligned} \langle 0|{M_0}^\dagger M_0|0\rangle &= 1 \\ \langle 1|{M_0}^\dagger M_0|1\rangle &= 0 \\ M_0 M_0 &= M_0 \end{aligned}$$

- Searching for $M_0$ in the following form:

$$\mathbf{M}_0 = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$

<!-- note: the figure crops are the pasted formula pictures, no figure. -->

## s21 · p21 · 3RD POSTULATE IN CASE OF PROJECTIVE MEASUREMENTS (1)
<!-- status: viewed pages/p021.png -->
<!-- flags: math, layout -->

- To find $M_0$ we have to solve:

$$\begin{aligned} \langle 0|{M_0}^\dagger M_0|0\rangle &= 1 \\ \langle 1|{M_0}^\dagger M_0|1\rangle &= 0 \\ M_0 M_0 &= M_0 \end{aligned}$$

At the top right: $M_0 = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$

$$1 = \langle 0|{M_0}^\dagger M_0|0\rangle = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix}^\dagger \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} a^* & c^* \\ b^* & d^* \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} \Longrightarrow |a|^2 + |c|^2 = 1$$

$$0 = \langle 1|{M_0}^\dagger M_0|1\rangle = \begin{bmatrix} 0 & 1 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix}^\dagger \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 \end{bmatrix} \begin{bmatrix} a^* & c^* \\ b^* & d^* \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} \Longrightarrow |b|^2 + |d|^2 = 0$$

<!-- note: on the slide each of the two derivations wraps over three lines (the "=" chain breaks after [1 0] and after the first product). The first condition and its derivation are in dark orange, the second in light orange, so that each derivation is matched with its condition. -->

## s22 · p22 · CONSTRUCTING A PROJECTIVE MEASUREMENT OPERATOR
<!-- status: viewed pages/p022.png -->
<!-- flags: math, layout -->

- To find $M_0$ we have to solve:

At the top right: $M_0 = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$

Figure: derivation diagram connected by arrows.
- $\langle 0|{M_0}^\dagger M_0|0\rangle = 1$ (dark orange) → arrow to the right → $|a|^2 + |c|^2 = 1$ (dark orange).
- $\langle 1|{M_0}^\dagger M_0|1\rangle = 0$ (light orange) → arrow to the right → $|b|^2 + |d|^2 = 0$ (light orange).
- Below it: $|b|^2 \geq 0$ and $|d|^2 \geq 0$. A right curly brace groups the three lines $|b|^2 + |d|^2 = 0$, $|b|^2 \geq 0$, $|d|^2 \geq 0$ and points to $b = d = 0$.
- From $b = d = 0$ an arrow goes down to $M_0 = \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix}$.
- $M_0 M_0 = M_0$: an arrow from it goes down, and a line from $M_0 = \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix}$ joins it from the right, both leading to $\begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix} \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix} = \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix}$.
- From that equation a forked arrow points to two results: $a^2 = a$ and $ac = c$.

Use: text

The derivation as formulas:

$$\langle 0|{M_0}^\dagger M_0|0\rangle = 1 \longrightarrow |a|^2 + |c|^2 = 1$$

$$\langle 1|{M_0}^\dagger M_0|1\rangle = 0 \longrightarrow \left.\begin{aligned} |b|^2 + |d|^2 &= 0 \\ |b|^2 &\geq 0 \\ |d|^2 &\geq 0 \end{aligned}\right\} b = d = 0 \longrightarrow M_0 = \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix}$$

$$M_0 M_0 = M_0 \longrightarrow \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix} \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix} = \begin{bmatrix} a & 0 \\ c & 0 \end{bmatrix} \longrightarrow a^2 = a, \quad ac = c$$

- Solution: $M_0 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$
- Similarly: $M_1 = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$

## s23 · p23 · CONSTRUCTING A PROJECTIVE MEASUREMENT OPERATOR
<!-- status: viewed pages/p023.png -->
<!-- flags: graphic, image, math -->
<!-- figure: figures/p023-f1.png -->
<!-- figure: figures/p023-f2.png -->
<!-- figure: figures/p023-f3.png -->
<!-- figure: figures/p023-f4.png -->
<!-- figure: figures/p023-f5.png -->
<!-- figure: figures/p023-f6.png -->

Completeness:

$$\sum_m \mathbf{M}_m^\dagger \mathbf{M}_m = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \mathbf{I}$$

Practical notation:

$$M_0 = |0\rangle\langle 0| \text{ and } M_1 = |1\rangle\langle 1|$$

Conclusion

Thus we reached a very simple and practical rule of thumb: *In case we have a set of orthonormal states $\{|\varphi_m\rangle\}$ then the corresponding measurement operators which provide exact differentiation among them can be produced by $M_m = |\varphi_m\rangle\langle\varphi_m|$.*

<!-- note: the formulas and the conclusion paragraph are pasted pictures (the conclusion is a picture of a book page), no figure. -->

## s24 · p24 · PLATO'S ALLEGORY OF THE CAVE
<!-- status: viewed pages/p024.png -->
<!-- flags: graphic, image -->
<!-- figure: figures/p024-cave.png -->

Figure: illustration of Plato's allegory of the cave in the style of black-figure Greek vase painting, black figures on an orange cave background. From left to right: a burning flame (white) on top of a column; a bearded man in a robe, striding, holding up a stick with a bird figure on its top; a low dark wall; a seated man leaning against the wall, pointing to the right; on the right cave wall a bright white oval on which the shadow of the bird appears. Dashed lines run from the flame past the bird on the stick to its shadow on the wall, showing the light rays that cast the shadow. No text in the picture.

Use: image figures/p024-cave.png
