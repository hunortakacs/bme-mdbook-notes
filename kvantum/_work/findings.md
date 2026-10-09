# Findings

## F1 · confirmed · kvantuminformatikai-alkalmazasok-jegyzet-2026-osz all (img012)
Source says: Ψ± = (|00⟩ ± |11⟩)/√2, Φ± = (|01⟩ ± |10⟩)/√2; slides 03 s27–s28, 04 s13 use only |β_ab⟩.
Problem: swapped against the usual convention (Φ± for |00⟩±|11⟩, Ψ± for |01⟩±|10⟩).
Proposal: only |β_ab⟩.
Decision: user chose the proposal (2026-10-09): only |β_ab⟩, no Φ/Ψ names.

## F2 · confirmed · 03-osszefonodasalapjai-20260923 s10; bloch-gyak s5, s6
Source says: |φ⟩ = [x, y, z]ᵀ = [cos β sin α, sin β sin α, cos α]ᵀ.
Problem: equates the ket with its real Bloch vector.
Proposal: "a |φ⟩ állapotnak a Bloch-gömb [x, y, z]ᵀ = … pontja felel meg".
Decision: user chose the proposal (2026-10-09): the Bloch point corresponds to the state, no equals sign to the ket.

## F3 · confirmed · 05-interferometer-es-nct20261007 s21
Source says: P₀₀ = p₀₀·p₀₀ + p₀₁·p₁₀ = 0!, with detector 0 highlighted and detector 1 crossed out.
Problem: contradicts the figure, s28–s32 (Δα = 0 ⇒ P₀ = 1) and J5; probabilities cannot cancel, amplitudes do.
Proposal: detector 0 with probability 1, detector 1 never; amplitudes toward output 1 cancel; no "P₀₀ = 0".
Decision: user chose the proposal (2026-10-09): amplitude form, drop "P₀₀ = 0".

## F4 · confirmed · kvantuminformatikai-alkalmazasok-posztulatumok s16
Source says: |φ⟩^{⊗2} = a|00⟩ + b|01⟩ + c|10⟩ + d|11⟩ (and ⊗4 with a…p) for |φ⟩ = a|0⟩ + b|1⟩.
Problem: a tensor power has product coefficients; independent coefficients form a general register state.
Proposal: present it as a general 2- and 4-qubit register state.
Decision: user chose the proposal (2026-10-09): general 2- and 4-qubit register state, without the ⊗ power.

## F5 · confirmed · 05-interferometer-es-nct20261007 s48; jegyzet all (img036)
Source says: ⟨ψ|φ⟩ = ±1 ⇔ |φ⟩ = |ψ⟩, or ⟨ψ|φ⟩ = 0.
Problem: the derivation gives |⟨ψ|φ⟩| = 1 (equal up to a global phase).
Proposal: |⟨ψ|φ⟩| = 1.
Decision: user chose the proposal (2026-10-09): |⟨ψ|φ⟩| = 1, "csak globális fázisban különböznek".

## F6 · confirmed · notation (all sources)
Source says: j in the lectures; i in gyak1, the circuit-design sheet and PO s13; iħ in the Schrödinger equation.
Problem: one convention is needed.
Proposal: j everywhere except iħ; code unchanged.
Decision: user chose the proposal (2026-10-09): j everywhere, iħ in the Schrödinger equation, code keeps Python syntax.

## F7 · confirmed · jegyzet all (§1)
Source says: Shor's breaking speed "a titkosítási kulcs hosszának logaritmusával arányos".
Problem: the running time is polynomial in the key length.
Proposal: keep only the conclusion (a longer key does not protect).
Decision: user chose the proposal (2026-10-09): conclusion only, no speed claim.

## SCOPE-1 · confirmed · jegyzet all (§6–§12)
Source says: 2025 versions of the lectures not yet held, 189 images.
Problem: may change; no slides yet.
Proposal: add each section when its 2026 lecture arrives.
Decision: user chose the proposal (2026-10-09): wait; add each section when its 2026 lecture and slides arrive.
