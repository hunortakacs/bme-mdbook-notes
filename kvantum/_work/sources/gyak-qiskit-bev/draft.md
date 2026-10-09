# gyak_qiskit_bev.ipynb

<!-- 1 pages, 13 units, grouping: - -->

## s1 · p1 · Kvantumszámítógépek programozása 2.: algoritmus implementációja áramköri rajz segítségével
<!-- status: auto -->

# Kvantumszámítógépek programozása 2.: algoritmus implementációja áramköri rajz segítségével

## s2 · p1 · Kvantuminformatikai alkalmazások,
<!-- status: auto -->

## Kvantuminformatikai alkalmazások,
### 2026 ősz

#### Dr. Solymos Balázs, Dr. Bacsárdi László, Dr. Imre Sándor
solymosb@hit.bme.hu

## s3 · p1 · Általános információk
<!-- status: auto -->

## Általános információk

Az órán a [Qiskit](https://qiskit.org/) python-os könyvtárat és a [Jupyter Notebook](https://jupyter.org/) környezetet használjuk.
Ha valaki saját gépen szeretné elvégezni a mérést, akkor fel kell telepíteni a Python-t, a Jupyter-t és a Qiskit-et. Az utolsó kettőt `pip` segítségével a következő módon lehet telepíteni egy már működő python installációhoz: 

```
pip install notebook
pip install qiskit[visualization]
pip install qiskit-ibm-runtime
pip install qiskit-aer
```

Ezután indítható el a Jupyter a "`jupyter notebook`" paranccsal.

## s4 · p1 · 1. Egyszerű kvantumos áramkörök a Qiskit-tel
<!-- status: auto -->

## 1. Egyszerű kvantumos áramkörök a Qiskit-tel

Egy áramkört a "QuantumCircuit" osztály példányosításával tudunk létrehozni.

<!-- cell 4 -->
```python
from qiskit import QuantumCircuit #importáljuk a megfelelő qiskit könyvtárat
qc = QuantumCircuit(3)            #létrehozunk egy QuantumCircuit példányt
```

A konstruktor paraméterének megadható, hogy mennyi qubit legyen az áramkörben. Az egy qubit-ekhez indexek tartoznak, melyek számozása 0-tól indul.

## s5 · p1 · Kapuk hozzáadása
<!-- status: auto -->

## Kapuk hozzáadása

Ha szeretnénk hozzáadni egy kaput az áramkörhöz, akkor azt az áramkör objektum megfelelő függvényével tudjuk megtenni.

<!-- cell 7 -->
```python
qc.h(0)
```

Output:
```text
<qiskit.circuit.instructionset.InstructionSet at 0x18c8caccc10>
```

Lehetőségünk van irányított kapukat is elhelyezni. Ekkor az első paraméter a kontrollbit indexe, míg a második a célbithez tartozó.

<!-- cell 9 -->
```python
qc.cx(0,1)
qc.cx(0,2)
```

Output:
```text
<qiskit.circuit.instructionset.InstructionSet at 0x18c8baeece0>
```

## s6 · p1 · Áramkör megjelenítése
<!-- status: TODO view figures/cell011-1.png -->
<!-- flags: image -->

## Áramkör megjelenítése

Az áramkör megjeleníthető a "draw()" függvénnyel.

A függvény paraméter egy string, amivel megadható a kimenet formátuma. 

Pl.: "text", "latex" és "mpl".

<!-- cell 11 -->
```python

qc.draw("mpl")
```

<!-- figure: figures/cell011-1.png (output of cell 11) -->

## s7 · p1 · Áramkörök a qiskitben
<!-- status: TODO view figures/cell013-1.png -->
<!-- flags: image -->

## Áramkörök a qiskitben

Hogyan kezeli a qiskit az áramköröket?

Vizsgáljuk meg az egyszerű X kaput!

<!-- cell 13 -->
```python
qc_x = QuantumCircuit(2,0)
qc_x.x(0)
qc_x.draw("mpl")
```

<!-- figure: figures/cell013-1.png (output of cell 13) -->

### Tárolt adatstruktúra

<!-- cell 15 -->
```python
qc_x.data
```

Output:
```text
[CircuitInstruction(operation=Instruction(name='x', num_qubits=1, num_clbits=0, params=[]), qubits=(<Qubit register=(2, "q"), index=0>,), clbits=())]
```

Az "X" kapu:

<!-- cell 17 -->
```python
qc_x.data[0].operation.definition.draw('mpl')
```

<!-- figure: figures/cell017-1.png (output of cell 17) -->

Fontos, hogy a `CircuitInstruction` és `QuantumCircuit` különbözik, pedig mindkettő egy kvantumbit vagy kvantumbitek módosítását írja le.

### Áramkörök összekapcsolása
Két külön készített áramkör összekapcsolható a "compose" függvénnyel:

<!-- cell 20 -->
```python
qc_a = QuantumCircuit(3) #Első áramkör
qc_a.x(1) 
qc_b = QuantumCircuit(2, name="qc_b") #Második áramkör
qc_b.x(0)
qc_b.z(1)
combined = qc_a.compose(qc_b, qubits=[1, 2]) #Összekapcsolás
```

A függvény első paramétere az áramkör, amit hozzá szeretnénk adni a megfelelő áramkörünkhöz. A második paraméter pedig azok a kvantumbitek, amiken hatni fog.

<!-- cell 22 -->
```python
combined.draw("mpl")
```

<!-- figure: figures/cell022-1.png (output of cell 22) -->

### Áramkörök összekapcsolása 2.

Egy másik megoldás, ha az áramkörünket a ".to_instruction()" függvénnyel instrukcióvá alakítjuk. Ezután már elég csak úgy kezelni, mint pl. egy kaput.

<!-- cell 24 -->
```python
qc_a = QuantumCircuit(3)
qc_a.x(1)
qc_b = QuantumCircuit(2, name="qc_b")
qc_b.x(0)
qc_b.z(1)
inst = qc_b.to_instruction()
```

Ezután az append függvénnyel tudunk a meglévő áramkörhöz új elemeket hozzáfűzni.
Itt szintén meg kell adni, hogy mely kvantumbitekre hasson az új elem.

<!-- cell 26 -->
```python
qc_a.append(inst, [1, 2])
```

Output:
```text
<qiskit.circuit.instructionset.InstructionSet at 0x18c84a08370>
```

### Áramkörök összekapcsolása 2.

<!-- cell 28 -->
```python
qc_a.draw("mpl")
```

<!-- figure: figures/cell028-1.png (output of cell 28) -->

A "decompose" függvény segítségével láthatjuk minden instrukció megvalósítását.

<!-- cell 30 -->
```python
qc_a.decompose().draw("mpl")
```

<!-- figure: figures/cell030-1.png (output of cell 30) -->

### Vezérelt kapu készítése
Ha az áramkör, amit instrukcióként akarunk használni unitér, akkor úgy tudjuk kezelni, mint bármelyik más kaput. Például vezérelt változatot is tudunk készíteni belőle.

<!-- cell 32 -->
```python
gate = qc_b.to_gate().control()
# Mivel ez egy vezérelt kapu, ezért 3 indexet kell megadni.
qc_a.append(gate, [0, 1, 2])
qc_a.draw("mpl")
```

<!-- figure: figures/cell032-1.png (output of cell 32) -->

### Vezérelt kapu készítése
Az áramkör dekompozíciója:

<!-- cell 34 -->
```python
qc_a.decompose().draw("mpl")
```

<!-- figure: figures/cell034-1.png (output of cell 34) -->

## s8 · p1 · Áramkörök inicializálása állapotvektorral
<!-- status: TODO view figures/cell042-1.png -->
<!-- flags: image -->

## Áramkörök inicializálása állapotvektorral
Hálózat inicializáció (most regisztereket használva):

<!-- cell 36 -->
```python
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
q = QuantumRegister(2,'q') #kvantumbiteket tartalmazó regiszter létrehozása
c = ClassicalRegister(2,'c') #klasszikus biteket tartalmazó regiszter
qc = QuantumCircuit(q,c) #kvantumhálózat készítése a regiszterekból
```

Állapotvektor megadása:

<!-- cell 38 -->
```python
from qiskit.quantum_info import Statevector
state1 = Statevector([0.6,0.8])
```

Állapot inicializáció:

<!-- cell 40 -->
```python
qc.initialize(state1,qubits=q[0], normalize=True)
```

Output:
```text
<qiskit.circuit.instructionset.InstructionSet at 0x18c8e329f90>
```

Az elkészült hálózat:

<!-- cell 42 -->
```python
qc.draw("mpl")
```

<!-- figure: figures/cell042-1.png (output of cell 42) -->

Állapotvektor kinyerése a kvantumhálózatból:

<!-- cell 44 -->
```python
state_qc = Statevector(qc)
print(state_qc)
```

Output:
```text
Statevector([0.6+0.j, 0.8+0.j, 0. +0.j, 0. +0.j],
            dims=(2, 2))
```

Ismerős LaTeX formázásban is kiíratható az állapot:

<!-- cell 46 -->
```python
from qiskit.visualization import array_to_latex
array_to_latex(state_qc) # Latex-es kiírás
```

Output:
```text
<IPython.core.display.Latex object>
```

## s9 · p1 · Áramkörök futtatása
<!-- status: TODO view figures/cell053-1.png -->
<!-- flags: image -->

## Áramkörök futtatása

Az áramkörök futtatásához jellemzően valamilyen szimulátort használunk. (Lehetőség van természetesen a felhőben elérhető kvantumszámítógépek használatára is tokenek fejében, csak ott ki kell várni a várakozási sort.)

Legtöbbször úgy szeretnénk szimulálni az áramkört, hogy a végén klasszikus információt kapjunk.
Ehhez elengedhetetlen még hiányzó operáció a mérés, amely egy kvantumos regiszteren végrehajtja az előírt mérési operátort, és egy klasszikus regiszterbe írja a mérési eredményt.

Hozzunk létre egy kvantumos és klasszikus regisztereket is tartalmazó áramkört:

<!-- cell 49 -->
```python
qc = QuantumCircuit(2,2) # a második paraméter a klasszikus bitek száma
qc.h(0)
qc.cx(0,1)
qc.draw()
```

Output:
```text
     ┌───┐     
q_0: ┤ H ├──■──
     └───┘┌─┴─┐
q_1: ─────┤ X ├
          └───┘
c: 2/══════════
```

Használjuk az állapotvektor szimulátort!

<!-- cell 51 -->
```python
from qiskit_aer import Aer
backend = Aer.get_backend("statevector_simulator")
job = backend.run(qc)
result = job.result() # Blokkoló hívás!
outputstate = result.get_statevector(qc)
array_to_latex(outputstate)
```

Output:
```text
<IPython.core.display.Latex object>
```

A measure függvény szolgál a mérések elhelyezésére, melynek első paramétere a mérni kívánt qubitek listája, a második a mérési eredményeket tároló klasszikus bitek listája. A méréshez használjuk az Aer szimulátort!

<!-- cell 53 -->
```python
qc.measure(range(2), range(2))
qc.draw("mpl")
```

<!-- figure: figures/cell053-1.png (output of cell 53) -->

<!-- cell 54 -->
```python
backend = Aer.get_backend("aer_simulator")
result = backend.run(qc, shots=1000).result()
# A mérési eredményeket a result.get_counts függvénnyel tudjuk elérni.
counts = result.get_counts()
print(counts)
```

Output:
```text
{'11': 500, '00': 500}
```

A mérési eredményeket hisztogrammal is szemléltethetjük.

<!-- cell 56 -->
```python
from qiskit.visualization import plot_histogram
plot_histogram(counts)
```

<!-- figure: figures/cell056-1.png (output of cell 56) -->

### Állapotvektorok kinyerése a szimulációból
Hálózat előkészítése:

<!-- cell 58 -->
```python
q = QuantumRegister(2,'q') #kvantumbiteket tartalmazó regiszter létrehozása (q[index]-el indexelhetőek az egyes bitek)
c = ClassicalRegister(2,'c') #klasszikus biteket tartalmazó regiszter (c[index]-el indexelhetőek az egyes bitek)
qc = QuantumCircuit(q,c) #kvantumhálózat készítése a regiszterekból
qc.h(q[0]) #H kapu
qc.cx(q[0],q[1]) #CNOT kapu
qc.save_statevector(label = 'mereselott', pershot = True)
qc.measure(q[0],c[0])
qc.save_statevector(label = 'meresutan', pershot = True)
qc.measure(q[1],c[1])
qc.draw()
```

Output:
```text
     ┌───┐      mereselott ┌─┐ meresutan    
q_0: ┤ H ├──■───────░──────┤M├─────░────────
     └───┘┌─┴─┐     ░      └╥┘     ░     ┌─┐
q_1: ─────┤ X ├─────░───────╫──────░─────┤M├
          └───┘     ░       ║      ░     └╥┘
c: 2/═══════════════════════╩═════════════╩═
                            0             1
```

Szimuláció:

<!-- cell 60 -->
```python
from qiskit import transpile
backend = Aer.get_backend('qasm_simulator')
job_sim = backend.run(transpile(qc, backend), shots=4,memory=True) # 4-szer ismételjük meg a kísérletet, hogy statisztikát kapjunk és elvégezzük a mérést
#mérési eredmény kinyerése
result_sim = job_sim.result()
print(result_sim.data(0)['mereselott'])
print(result_sim.data(0)['meresutan'])
```

Output:
```text
[Statevector([0.70710678+0.j, 0.        +0.j, 0.        +0.j,
             0.70710678+0.j],
            dims=(2, 2)), Statevector([0.70710678+0.j, 0.        +0.j, 0.        +0.j,
             0.70710678+0.j],
            dims=(2, 2)), Statevector([0.70710678+0.j, 0.        +0.j, 0.        +0.j,
             0.70710678+0.j],
            dims=(2, 2)), Statevector([0.70710678+0.j, 0.        +0.j, 0.        +0.j,
             0.70710678+0.j],
            dims=(2, 2))]
[Statevector([1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            dims=(2, 2)), Statevector([1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
            dims=(2, 2)), Statevector([0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j],
            dims=(2, 2)), Statevector([0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j],
            dims=(2, 2))]
```

## s10 · p1 · Tetszőleges kvantumos állapot előkészítése
<!-- status: auto -->

## Tetszőleges kvantumos állapot előkészítése
### $|0\rangle$ előjelváltása

Tetszőleges $\alpha|0\rangle + \beta|1\rangle$ állapotot szeretnénk a $-\alpha|0\rangle + \beta|1\rangle$ állapotba alakítani. Hogyan tudjuk ezt elérni Pauli-kapukkal?

<!-- cell 63 -->
```python
from qiskit_aer import Aer

qc = QuantumCircuit(1) 
qc.initialize([0.6, 0.8], 0)
qc.x(0)
qc.z(0)
qc.x(0)
sim = Aer.get_backend("statevector_simulator")
output_state = sim.run(qc).result().get_statevector(qc)
print(output_state)
```

Output:
```text
Statevector([-0.6+0.j,  0.8+0.j],
            dims=(2,))
```

## s11 · p1 · Tetszőleges kvantumos állapot előkészítése
<!-- status: auto -->

## Tetszőleges kvantumos állapot előkészítése
### Globális fázis állítása

 $\alpha|0\rangle + \beta|1\rangle$ állapotból indulva jussunk el a: $e^{j\pi/4}\alpha|0\rangle + e^{j\pi/4}\beta|1\rangle$ állapotba!

<!-- cell 65 -->
```python
from qiskit_aer import Aer
import numpy as np
qc = QuantumCircuit(1) 
qc.initialize([0.6, 0.8], 0)
angle = np.pi/4
qc.x(0)
qc.p(angle,0) # fázisforgató kapu - 1. paraméter: szög, 2. paraméter: qubit index
qc.x(0)
qc.p(angle,0)
sim = Aer.get_backend("statevector_simulator")
output_state = sim.run(qc).result().get_statevector(qc)
print(output_state)
```

Output:
```text
Statevector([0.42426407+0.42426407j, 0.56568542+0.56568542j],
            dims=(2,))
```

## s12 · p1 · Tetszőleges kvantumos állapot előkészítése
<!-- status: auto -->

## Tetszőleges kvantumos állapot előkészítése
Építsünk tetszőleges egybites kvantumos állapot létrehozására alkalmas kvantumáramkört!

<!-- cell 67 -->
```python
import numpy as np
a = 0.6
b = 0.8 
param1 = 0
param2 = 0
param3 = 0
qc = QuantumCircuit(1)
# Készített hálózat itt....


print(Statevector(qc))
qc.draw()
```

Output:
```text
Statevector([1.+0.j, 0.+0.j],
            dims=(2,))
```

Output:
```text
   
q:
```

## s13 · p1 · Tetszőleges kvantumos állapot előkészítése
<!-- status: auto -->

## Tetszőleges kvantumos állapot előkészítése
Építsünk tetszőleges egybites kvantumos állapot létrehozására alkalmas kvantumáramkört!

Cél: a|0> + b|1> állapot előkészítése egy kvantumregiszterben.

<!-- cell 70 -->
```python
import numpy as np
a = -0.8
b = 0.6
alpha = 2* np.arccos(np.absolute(a))
beta= np.angle(b) - np.angle(a)
gamma = -0.5 * alpha + np.angle(a) 
qc = QuantumCircuit(1)
qc.h(0)
qc.p(alpha,0)
qc.h(0)
qc.p(beta + 0.5* np.pi,0)
qc.x(0)
qc.p(gamma,0)
qc.x(0)
qc.p(gamma,0)
print(Statevector(qc))
qc.draw()
```

Output:
```text
Statevector([-0.8+4.13002965e-17j,  0.6-7.81597009e-17j],
            dims=(2,))
```

Output:
```text
   ┌───┐┌──────────┐┌───┐┌─────────┐┌───┐┌───────────┐┌───┐┌───────────┐
q: ┤ H ├┤ P(1.287) ├┤ H ├┤ P(-π/2) ├┤ X ├┤ P(2.4981) ├┤ X ├┤ P(2.4981) ├
   └───┘└──────────┘└───┘└─────────┘└───┘└───────────┘└───┘└───────────┘
```
