# 2_bloch.ipynb

<!-- 1 pages, 5 units, grouping: - -->

## s1 · p1 · Általános Qiskit információk
<!-- status: auto -->

# Általános Qiskit információk
A demonstrációhoz a Qiskit python-os könyvtárat és a Jupyter Notebook környezetet használom. Ha valaki saját gépen szeretné követni az anyagot, akkor fel kell telepíteni a Python-t, a Jupyter-t és a Qiskit-et. Az utolsó kettőt pip segítségével a következő módon lehet telepíteni egy már működő python installációhoz:

    pip install notebook
    pip install qiskit[visualization]
    pip install qiskit-ibm-runtime
    pip install qiskit-aer
Ezután indítható el a Jupyter a "jupyter notebook" paranccsal.

## s2 · p1 · Bloch gömb Qiskit példa
<!-- status: auto -->

# Bloch gömb Qiskit példa

## s3 · p1 · 1. Bloch gömb rajzolása állapotvektor alapján
<!-- status: viewed figures/cell003-1.png -->
<!-- flags: image -->

## 1. Bloch gömb rajzolása állapotvektor alapján

<!-- cell 3 -->
```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import numpy as np

#state = Statevector([1/np.sqrt(2), 1/np.sqrt(2)])
state = Statevector([0.6, 0.8])
plot_bloch_multivector(state)
```

<!-- figure: figures/cell003-1.png (output of cell 3) -->

Figure: Bloch-gömb „qubit 0” címmel; a pólusokon $\ket{0}$ (fent) és $\ket{1}$ (lent), a tengelyek $x$ (előre-balra) és $y$ (jobbra). A rózsaszín állapotvektor-nyíl a középpontból az $x$ tengely irányába, az egyenlítő alá mutat (a déli félgömb felé), azaz a $[0.6, 0.8]$ állapot.
Use: image figures/cell003-1.png

## s4 · p1 · 2. Egyszerű kvantumhálózat készítése és kapuk alkalmazása
<!-- status: viewed figures/cell005-1.png -->
<!-- flags: image -->

## 2. Egyszerű kvantumhálózat készítése és kapuk alkalmazása

<!-- cell 5 -->
```python

qc = QuantumCircuit(1,1) # 1 kvantum és 1 klasszikus bit (1 klasszikus bit a későbbi mérési eredmények tárolására kell)
qc.initialize([0.8, 0.6j], 0) #kezdeti állapot beállítása

#kvantumkapuk alkalmazása ()
qc.x(0) # Pauli X kapu
qc.y(0) # Pauli Y kapu
qc.z(0) # Pauli Z kapu
qc.h(0) # H kapu
#fázisforgató kapu
theta = np.pi
qc.p(theta, 0)
state = Statevector(qc)
plot_bloch_multivector(state)
```

<!-- figure: figures/cell005-1.png (output of cell 5) -->

Figure: Bloch-gömb „qubit 0” címmel, ugyanazokkal a feliratokkal ($\ket{0}$ fent, $\ket{1}$ lent, $x$, $y$). A rózsaszín nyíl az egyenlítő síkjában, közel a $+y$ irányba mutat (kissé a $-x$ felé elfordulva).
Use: image figures/cell005-1.png

## s5 · p1 · 3.mérés definiálása
<!-- status: viewed figures/cell011-1.png -->
<!-- flags: image -->

## 3.mérés definiálása

<!-- cell 7 -->
```python


qc.measure(range(1),range(1)) #mely qubiteken végezzünk mérést és azok eredményeit hova írjuk
qc.draw() #ellenőrzésként a hálózat lerajzoltatható
```

Output:
```text
     ┌──────────────────────┐┌───┐┌───┐┌───┐┌───┐┌──────┐┌─┐
  q: ┤ Initialize(0.8,0.6j) ├┤ X ├┤ Y ├┤ Z ├┤ H ├┤ P(π) ├┤M├
     └──────────────────────┘└───┘└───┘└───┘└───┘└──────┘└╥┘
c: 1/═════════════════════════════════════════════════════╩═
                                                          0
```

### Mérési eredmények szimulációja

<!-- cell 9 -->
```python
from qiskit_aer import Aer
from qiskit import transpile

#szimulátor kijelölése
backend = Aer.get_backend('qasm_simulator')
job_sim = backend.run(transpile(qc, backend), shots=1000) # 1000-szer ismételjük meg a kísérletet, hogy statisztikát kapjunk és elvégezzük a mérést

result_sim = job_sim.result() 

counts = result_sim.get_counts()
print(counts) #mérési eredmények kiírása
```

Output:
```text
{'1': 481, '0': 519}
```

### Mérési eredmények vizualizációja

<!-- cell 11 -->
```python
from qiskit.visualization import plot_histogram

#hisztogram a mérési eredményekből
plot_histogram(counts)
```

<!-- figure: figures/cell011-1.png (output of cell 11) -->

Figure: oszlopdiagram (hisztogram) két kék oszloppal. Vízszintes tengely: a mérési eredmények „0” és „1” (ferdén írva); függőleges tengely: „Count”, beosztás 0, 150, 300, 450, szaggatott vízszintes rácsvonalakkal. A „0” oszlop magassága 519, az „1” oszlopé 481; az értékek az oszlopok fölé vannak írva.
Use: image figures/cell011-1.png
