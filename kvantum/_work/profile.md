# Profile: kvantum

## Course

Kvantuminformatikai alkalmazások (BMEVIHIAD00), BME VIK, HIT tanszék, 2026 ősz. Lecturers: Bacsárdi László, Imre Sándor, Oláh Kitti, Galambos Máté, Czermann Márton; practice: Solymos Balázs, Márton Botond, Mihály András. Sources and book in Hungarian; some practice slides and pasted book excerpts are in English and are rendered in Hungarian prose.
Covers the four postulates in engineering interpretation, measurement, entanglement, interferometer, no-cloning, later teleportation, QKD, quantum algorithms (Deutsch–Jozsa, QFT, phase estimation, Shor, Grover), and Qiskit programming in the practices.
The course notes `Kvantuminformatikai alkalmazások jegyzet 2026 ősz.md` (Google Docs export) cover all lectures; the lecturers update it lecture by lecture, so sections dated 2025 are the previous year's version. Its formulas and figures are embedded base64 PNGs: prepare.py does not handle them; they are decoded to `_work/sources/kvantuminformatikai-alkalmazasok-jegyzet-2026-osz/images/imgNNN.png` with `text-with-images.md`, and transcribed into `images.md` there (img001–img037 done = §1–§5).

## Terminology

- kvantumbit (qubit); Q/C átalakító (the lecturer's preferred engineering name for mérés); mérődoboz, skála, skálaérték; mérési operátor {M_m}; mérési statisztika; mérés utáni állapot; teljességi reláció
- projektív mérés (Neumann-mérés), projektor P_m; Neumark-kiterjesztés; POVM (pozitív operátor értékű mérés), "nem tudom" állapot
- vezérlés (control) and adat (data) for the CNOT wires (also célbit/target); mesteregyenlet |x⟩|y⟩ → |x⟩|y⊕x⟩
- szorzatállapot (product), összefonódott állapot (entangled); hozzáfonódás; általánosított kvantum összefonó
- féligáteresztő tükör / nyalábosztó (beamsplitter), polarizáló nyalábosztó, egyfoton detektor, detektormodul; kvantuminterferométer; pillangó (butterfly) for the environment; dekoherencia
- fázisforgató kapu (fáziskapu) P(α); Pauli-X (bit-flip), Pauli-Z (fázis-flip), Pauli-Y; Hadamard-kapu (H-kapu); |+⟩ „ket plusz”, |−⟩ „ket mínusz”
- no-cloning (másolhatatlansági) tétel; univerzális kvantummásoló U ⊇ Q
- kvantumalgoritmus receptje: inicializálás → kvantum-párhuzamosság → amplitúdó erősítés → mérés → utó-feldolgozás

## Notation and conventions

- Imaginary unit **j** everywhere (lecture notation), except the Schrödinger equation iħ d/dt|Ψ⟩ = Ĥ|Ψ⟩; Python keeps its own syntax (`0.6j`). (F6)
- Kets with `\ket{}`, bras `\bra{}`, inner products `\braket{a|b}`; state names φ (`\varphi`), ψ; amplitudes a, b; general unitary U = [[a, b], [−e^{jφ}b*, e^{jφ}a*]].
- Gate formulas always "matrix · [a; b] = result" (the slides' animation layout shows matrix · result; the lecturer himself called the book's form wrong, J §3).
- Bloch sphere: α polar (from z), β azimuth (from x), γ global phase; the Bloch point [x, y, z]ᵀ "corresponds to" the state, never "=" the ket (F2).
- Bell states only as |β_ab⟩ = (|0,b⟩ + (−1)^a|1,NOT(b)⟩)/√2; no Φ±/Ψ± names (F1).
- Interferometer: Δα ≜ α₀ − α₁, P₀ = cos²(Δα/2), P₁ = sin²(Δα/2).
- Qiskit code kept as in the notebooks (Hungarian comments); InstructionSet return values are not shown; random counts are shown as in the notebook with a note that they vary.
- Figures: circuits and setups are images (jegyzet originals preferred, `img/jegyzet-*.png`); only the algorithm recipe is Mermaid. Image names `img/<source abbreviation>-<what>.png`.

## Recurring decisions

- F3: no "P₀₀ = 0" for the Mach–Zehnder; explain by cancelling amplitudes (detector 0 with probability 1).
- F4: |φ⟩^{⊗2} with independent a, b, c, d is presented as a general 2-qubit register state.
- F5: no-cloning condition written |⟨ψ|φ⟩| = 1 (equal up to a global phase).
- F7: no speed claim for Shor; only "a longer key does not protect".
- SCOPE-1: jegyzet sections for lectures not yet held (2025 versions, §6–§12) are added only when the 2026 lecture and slides arrive; transcribe their images (img038–img226) then.
- Exercises from the practice sheets go to the chapter of their topic; solutions only where the notebook/sheet has them.

## Verifiers

- `verify/qiskit_examples`: runs the Python blocks of every chapter that uses Qiskit, chapter by chapter like a notebook, with the venv interpreter `~/.local/share/venvs/qiskit/bin/python` (qiskit 2.5.2, qiskit-aer 0.17.2, matplotlib, pylatexenc; override with $KVANTUM_QISKIT_PYTHON), and compares each block's output with the ```text block after it (numbers ±1e-6, measurement counts only keys and total). Directives `<!-- verify: skip -->` and `<!-- verify: prelude ... -->` in the chapter. A LaTeX value (`array_to_latex`) is compared with the `$$…$$` formula in the paragraph after the block, but `array_to_latex` without `source=True` needs IPython, which the venv lacks (sympy is installed), so those two blocks carry `verify: skip`; their LaTeX was checked by hand with `source=True` (2026-10-09). Does not check figures or prose claims about outputs.
