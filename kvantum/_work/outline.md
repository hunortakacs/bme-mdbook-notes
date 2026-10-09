# Outline: kvantum

Book title: **Kvantuminformatikai alkalmazások**. Language: Hungarian (the sources' language; English slide passages are rendered in Hungarian prose, English terms given once in parentheses).

Sources of the first run: lectures 01, posztulátumok (lecture 2), 03, 04, 05; practice sheets gyak1, bloch_gyak, Kvantuminformatikai áramkörök tervezése, Emlékeztető a CNOT művelethez; notebooks 2_bloch, gyak_qiskit_bev; course notes "Kvantuminformatikai alkalmazások jegyzet 2026 ősz.md" (abbreviated *jegyzet* below; sections 1–5 = lectures held so far).

Unit abbreviations: 01 = 01-bevezetes-20260909, PO = kvantuminformatikai-alkalmazasok-posztulatumok, 03 = 03-osszefonodasalapjai-20260923, 04 = 04-meresek20260930, 05 = 05-interferometer-es-nct20261007, G1 = gyak1, BG = bloch-gyak, AT = kvantuminformatikai-aramkorok-tervezese, CN = emelkezteto-a-cnot-muvelethez, NB = 2-bloch, QB = gyak-qiskit-bev, J = jegyzet (one unit "all"; J1–J5 = its sections).

## Chapter tree (all NEW)

- `intro.md` Bevezetés: what the course is about (two or three sentences, from 01 s43 "kvantumos szemlélet", J1).
- `motivacio.md` A kvantuminformatika motivációja: what "kvantum" means and its features (01 s8, 03 s4), quantum-mechanical systems around us (01 s9), Schrödinger's 1952 claim and the second quantum revolution (01 s10–s11, J1), the threat to RSA: Shor, post-quantum cryptography vs quantum communication (J1), Mosca inequality and expert estimates (01 s25), CSA date 2030-04-14 (01 s26, J1), the quantum view of an apple (01 s57, J1). ← 01 s8–s11, s25–s26, s57; 03 s4; J1.
- `posztulatumok.md` A kvantummechanika posztulátumai: axiom vs postulate (PO s4, J2), the four postulates in engineering interpretation with their formula boxes (PO s3, 03 s6–s8, 04 s6, 05 s3, BG s2–s3, G1 s2, J2), the physicist interpretation (5 postulates, wave function, hermitian operators x̂, p̂, Ĥ, Schrödinger equation) (PO s6, s19, J2), Hilbert space and the table "kvantum interpretáció ↔ Hilbert-tér" (PO s8, J2).
  - `posztulatumok/kvantumbit.md` A kvantumbit: 1st postulate, superposition, bit vs qubit figure, Schrödinger's cat, ket/bra, amplitudes, |a|²+|b|²=1, the unit-circle picture, inner/outer/tensor product in vector form, the |+⟩, |−⟩ basis and its orthogonality; exercises G1 s11. ← PO s6–s7, 03 s9, s19–s20, BG s4, G1 s3–s4, s9–s11, J2, J3 (|+⟩/|−⟩ part).
  - `posztulatumok/bloch-gomb.md` A Bloch-gömb: parametrisation with α, β, γ (and the θ, φ form of PO s13), global phase, Bloch vector [x, y, z], figure, plotting a state in Qiskit (`plot_bloch_multivector`); exercises BG s14 (first three), AT 1 and 3 (global phase). ← 03 s10–s11, BG s5–s6, PO s13, NB s3, AT s1, s3.
  - `posztulatumok/kapuk.md` Unitér transzformációk és kvantumkapuk: 2nd postulate, unitary properties (G1 s5, PO s9, J2), general 2×2 unitary, Pauli X/Y/Z, phase gate P(α), Hadamard (matrices, action on a|0⟩+b|1⟩, H|0⟩, H|1⟩ = |+⟩, |−⟩, H†=H, HH=I), gate symbols, rotations on the Bloch sphere (04 s14–s15, PO s9, BG s9 with e^{−jαX/2}), H and the superposition principle with the electric-circuit analogy (BG s13); exercises: identities HH=I, XX=I, ZZ=I, HXH=Z, HZH=X (BG s14), AT 2 and 5. ← PO s9–s12, 03 s12–s15, 04 s14–s15, BG s7–s13, G1 s5, s12–s16, AT s2, s5, J2, J3.
  - `posztulatumok/regiszterek.md` Kvantumregiszterek: 4th postulate, tensor product examples ("Számoljunk!" with results), general n-qubit register, 2ⁿ dimension, what 500 qubits are enough for (wheat on the chessboard), physical register example (nuclear spins). ← PO s15–s17, G1 s6–s8, 04 s11, J2.
- `meres.md` Mérés (3rd postulate): Q/C conversion, the measuring box (bemenet, kimenet, skála, {M_m}), circuit symbol, measurement statistics and post-measurement state, randomness (Einstein/Born dialogue), completeness relation, measurement disturbs the system (shrew/elephant, microscope and EM spectrum, the observation paradox of 05 s25), the postulate is analytic, engineers need constructions. ← 03 s8, 04 s17–s25, 05 s25 (second half), PO s14, J4.
  - `meres/projektiv.md` Projektív mérés: physical measurement with a polarizing beam splitter and single-photon detectors, conditions on M₀ and M₁, completeness of the detector module, projection and normalisation, two beam splitters in series (M₀M₀=M₀, repeatability), construction of M₀ = |0⟩⟨0|, M₁ = |1⟩⟨1| (incl. the M₀M₀=M₀ step of G1), rule of thumb M_m = |φ_m⟩⟨φ_m|, properties of projectors, measurement with projectors, measuring a|0⟩+b|1⟩ in the computational basis, Neumark extension; exercise 3.1 (|+⟩/|−⟩ measurement). ← 04 s27–s44, 05 s4–s10, G1 s18–s23, J4.
  - `meres/povm.md` Kitekintés: POVM: non-orthogonal states, zoo example (projective vs POVM, D₀, D₁, D₂ = I − D₀ − D₁, the "nem tudom" outcome). ← 04 s45–s49, 05 s11–s15, J4.
- `osszefonodas.md` Összefonódás: superposition vs entanglement, product vs entangled states, a|00⟩+b|11⟩ has no decomposition, the correlation of |00⟩+|11⟩ and |01⟩+|10⟩, non-locality but no communication, agreeing on the basis, the travelling-pair collage, uses (teleportation, superdense coding, QKD, entanglement swapping, quantum memory), cannot be produced classically. ← 03 s21–s22, s30, 04 s12, J3.
  - `osszefonodas/cnot.md` A CNOT-kapu: control/data wires, truth table, classical XOR equivalent, mapping and matrix (block form [I 0; 0 X]), master equation |x⟩|y⟩ → |x⟩|y⊕x⟩, action on a general 2-qubit state in bra-ket and vector form, CNOT as classical copier → entangled pair. ← 03 s24–s26, CN s1–s2, G1 s17, J3.
  - `osszefonodas/bell.md` Bell-állapotok: H + CNOT circuit, |β_ab⟩ formula, the four states, orthogonality, SPDC photon pairs, generalised entangler / GHZ, the third-party "hozzáfonódás" risk. ← 03 s27–s29, 04 s13, J3.
- `interferometer.md` A kvantuminterferométer: probabilistic box and the coin, two boxes in series (classical 0.5), half-silvered mirror, Mach–Zehnder: what we expect vs what happens, classical interference picture, beam splitter and two beam splitters as identity, extra detectors make it random again, generalised interferometer with glass sheets, circuit H–P–H, analysis step by step (matrices and linearity), P₀ = cos²(Δα/2), P₁ = sin²(Δα/2), the physicist / electrical engineer / computer scientist views incl. the quantum-algorithm recipe (Mermaid) and the Qiskit code. ← 05 s16–s40, s25 (first half), J5.
  - `interferometer/dekoherencia.md` Dekoherencia: closed systems only, the butterfly entangled with the photon, analysis with |Ω₀⟩, |Ω₁⟩, P₀/P₁ with ⟨Ω₀|Ω₁⟩, the two limiting cases. ← 05 s41–s45, J5.
- `no-cloning.md` A no-cloning tétel: universal quantum copier U ⊇ Q, unitarity preserves inner products, the derivation, the theorem (orthogonal sets and known states can be copied), link to distinguishability (04 s44 / 05 s10); exercise AT 4 (CNOT copy). ← 05 s46–s49, AT s4, J5.
- `qiskit.md` Kvantumáramkörök Qiskitben: QuantumCircuit, gates, drawing, stored data (`data`), composing (`compose`, `to_instruction`, `append`, `decompose`), controlled gates, registers, initialising with a Statevector, reading the state (`Statevector`, `array_to_latex`), simulators (statevector, aer/qasm), measurement and counts, histogram, `save_statevector` before/after measurement, the 2_bloch example (initialize, X, Y, Z, H, P, Bloch plot, measurement, histogram); exercises with solutions from the notebook (sign flip of |0⟩, global phase, arbitrary 1-qubit state). ← QB s1, s3–s13, NB s1–s5.

## Cut list

- Course administration: 01 s1–s2, s5, s7, s29–s54 (lecturers, schedule, grading, ZH, homework, related courses, competition, TDK), 03 s1–s2, s16–s17, 04 s1–s2, s4, 05 s1, PO s1, BG s1, G1 s1, CN s3, AT s6 (acknowledgements), QB s2 (authors), J1 admin paragraphs, J3 homework/AI paragraphs.
- Installation: NB s1, QB s3 (pip install, starting Jupyter).
- History, trivia, quotes, jokes, polls, press, lab: 01 s3–s4, s6, s12–s24, s27–s28, s55–s56, s58; 04 s3, s5, s7–s10, s16, s50; 05 s50; PO s2; G1 s24 (Plato's cave, no text).
- Title, section and TOC slides: 01 s29 heading only; 03 s3, s18, s23; 04 s17, s26, s45; 05 s2, s4, s11, s16, s22, s46; PO s3, s5, s18, s20.
- Recaps: no recap sections; recap slides (03 s6–s15, 04 s6, s12–s15, 05 s3, s5–s15, BG s2–s4, G1 s2) feed the chapter of their topic, where anything only they have is kept. 03 s5 is a duplicate of 01 s10.
- Online simulator links (PO s13 links), the Slido word cloud.
- J sections 6–12 (2025 versions of lectures not yet held): pending question SCOPE-1.

## Figures

Images: lecture-note originals for circuits and setups (J img010, img011, img013, img014, img025, img027, img028, img030, img032), Bloch spheres (03 s11, 04 s14–s15, PO s9), bit/qubit and cat (PO s6), unit circle (PO s7), measuring box (04 s19, PO s14), shrew/elephant (04 s23), EM spectrum (04 s24), beam-splitter setups and projection diagrams (04 s27–s36, new crops), POVM vector diagrams (04 s47–s49, new crops), entanglement collage (04 s12), SPDC (03 s27), cat (03 s19), interferometer drawings and lab photo (05 s17–s26, s37–s38, s44), CNOT and XOR (CN s1), CNOT copy and BSC (AT s4–s5), quantum systems grid and risk chart and apple timeline (01 s9, s25, s57), nuclear-spin register (PO s15), circuit analogy (BG s13), notebook outputs (NB, QB).
Redrawn: quantum-algorithm recipe as Mermaid (05 s39); gate symbols as a text drawing; Mosca inequality as a formula with a crop of the diagram.
Dropped: logos, backgrounds, stock photos, cartoons, portraits.

## Trivial fixes (made silently)

Typos (aggatjuk, törvényei, imétlés, belőle, részletek, szorzatot, OPERATORS, identity, …); the gate formulas written "matrix × result" on the slides become "matrix × [a; b] = result" (the lecturer's own correction, J3); 04 s22 stray dagger on the bra; 04 s32 missing ⟩; 04 s35 normalisation label ⟨φ|M₀†M₀|φ⟩; 04 s42/05 s9 P(1|φ) = ⟨φ|P₁|φ⟩; 04 s43 P_m|φ⟩ in the numerators; 04 s11 2⁶⁴−1 grains in total; 05 s43 stray "= |φ₂⟩ ="; 05 s39 `qc.p(Dalpha, 0)`; G1 s10 ⟨+|−⟩ without the ket in the middle; G1 s15 b·e^{iα}; J2 "hermitikus ⇔ önadjungált" sentence; J4 index k → m.

## Verified by running (numpy; Qiskit is not installed)

NB cell 5 final state and Bloch angle; QB cells 63, 65, 70 statevectors and the circuit parameters 1.287, −π/2, 2.4981; Bell states from H+CNOT; HH=I, XX=I, ZZ=I, HXH=Z, HZH=X; e^{−jαX/2} = cos(α/2)I − j sin(α/2)X; CNOT on a|00⟩+b|01⟩+c|10⟩+d|11⟩; interferometer P₀ = cos²(Δα/2); butterfly P₀ = (1+⟨Ω₀|Ω₁⟩cosΔα)/2; path amplitudes of two H (0→1 cancels). All agree with the sources except the findings below.

## Findings

F1 Bell-state names (J img012), F2 Bloch vector written as a ket (03 s10, BG s5–s6), F3 interferometer "P₀₀ = 0" (05 s21), F4 tensor power with independent coefficients (PO s16), F5 no-cloning "⟨ψ|φ⟩ = ±1" (05 s48, J img036), F6 imaginary unit j vs i, F7 Shor speed "logarithm of the key length" (J1). Details in findings.md.

## Removed sources

None (first run).

## Open questions

SCOPE-1: include J sections 6–12 now or wait for their 2026 lectures.
