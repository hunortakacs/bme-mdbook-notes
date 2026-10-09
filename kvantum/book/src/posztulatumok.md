# A kvantummechanika posztulátumai

## Axióma és posztulátum

Az **axióma** egy adott tudományágon belül bizonyíthatatlan, de magától értetődőnek tekintett állítás, elfogadott igazság, amely nem igényel bizonyítást. Ilyenek a Newton-féle axiómák, vagy az euklideszi geometriában az, hogy a párhuzamos egyenesek soha nem találkoznak.

A **posztulátum** valamely gondolati rendszer alapját képező, szükségképpen igaznak tekintett állítások egyike. Bizonyítás nélkül elfogadott, a gondolkodás szempontjából nélkülözhetetlen feltevés: az a minimális feltétel, amely alapján további következtetéseket lehet levonni (például: a béke a jövő fejlődésének posztulátuma). Geometriai posztulátumokra épül például az euklideszi geometria. Egy szükségszerű körülményt ír le, amely egy állapot vagy jelenség bekövetkezésének előfeltétele.

A sakk szabályai 24, a fociéi és a gombfociéi 33, a kézilabdáéi kiegészítésekkel 134 A4-es oldalt töltenek ki. A kvantummechanikának, azaz a természetnek mindössze négy szabálya van: a négy posztulátum.

## A posztulátumok mérnöki interpretációban

A tárgy a posztulátumokat mérnöki interpretációban használja. Röviden:

| Posztulátum | Tárgya | Kulcsfogalmak | Képlet |
|---|---|---|---|
| 1. | kvantumbit | Hilbert-tér | $\ket{\varphi} = \sum_{i=0}^{2^n-1} \varphi_i \ket{i}$ |
| 2. | logikai kapuk | unitér transzformáció, elemi kvantum logikai kapuk | $U^\dagger \equiv U^{-1}$ |
| 3. | Q/C átalakítás | mérési statisztika, mérés utáni állapot | $P(m \mid \ket{\varphi}) = \bra{\varphi} M_m^\dagger M_m \ket{\varphi}$, $\ket{\varphi'} = \frac{M_m\ket{\varphi}}{\sqrt{\bra{\varphi} M_m^\dagger M_m \ket{\varphi}}}$ |
| 4. | regiszterek | tenzorszorzás | $\ket{\varphi} = \ket{0} \otimes \frac{\ket{0}+\ket{1}}{\sqrt{2}}$ |

Teljes szövegükkel:

1. **Állapotleírás.** Zárt fizikai rendszer aktuális állapota egy olyan állapotvektorral írható le, amely komplex együtthatókkal rendelkezik, és egységnyi hosszú a $H$ Hilbert-térben (egy komplex lineáris vektortérben, amelyben értelmezve van a belső szorzat). Részletesen: [A kvantumbit](posztulatumok/kvantumbit.md).
2. **Zárt rendszer időbeli fejlődése.** A zárt rendszer időbeli fejlődése unitér transzformációval írható le, amely csak a kezdő- és a végállapottól függ. Részletesen: [Unitér transzformációk és kvantumkapuk](posztulatumok/kapuk.md).
3. **A mérés.** Legyen $\{m\}$ a mérés lehetséges eredményeinek halmaza. Egy mérés a mérési operátorok $\{M_m\}$ halmazával adható meg. Ha a megmérendő rendszer állapota $\ket{\varphi}$, akkor annak a valószínűsége, hogy a mérés az $m$ eredményt adja, $P(m \mid \ket{\varphi}) = \bra{\varphi} M_m^\dagger M_m \ket{\varphi}$, és a mérés után a rendszer állapota $\ket{\varphi'} = M_m\ket{\varphi} / \sqrt{\bra{\varphi} M_m^\dagger M_m \ket{\varphi}}$. Részletesen: [Mérés](meres.md).
4. **Összetett rendszer.** Ha $V$ és $Y$ a két kvantumrendszerhez rendelt Hilbert-tér, akkor az ebből a két rendszerből álló összetett rendszerhez a $W = V \otimes Y$ Hilbert-tér rendelhető, ahol $\otimes$ a tenzorszorzás. Részletesen: [Kvantumregiszterek](posztulatumok/regiszterek.md).

Az első két posztulátum csak **zárt** rendszerre érvényes. Ennek a jelentőségét a [dekoherencia](interferometer/dekoherencia.md) mutatja meg.

## A Hilbert-tér

A Hilbert-tér a végtelen dimenziójú euklideszi vektorterek általánosítása, amelyben értelmezve van

- a belső szorzat (skalárszorzat), $\braket{\psi|\phi}$,
- a vektorok hossza, azaz normája,
- a távolság (metrikus tér): két vektor között van mérhető távolság,
- és amely teljes: minden Cauchy-sorozatnak van határértéke a térben.

A kvantummechanikában az állapotok (hullámfüggvények) egy Hilbert-tér vektorai. A kvantumos fogalmaknak a Hilbert-térben a következők felelnek meg:

| Kvantum interpretáció | Hilbert-térben |
|---|---|
| Állapotleírás | Vektor |
| Megfigyelhető | Hermitikus operátor |
| Mérés eredménye | Operátor sajátértéke |
| Mérés valószínűsége | Belső szorzat négyzete |
| Időbeni változás | Unitér transzformáció (Schrödinger-egyenlet) |

## A posztulátumok fizikusi interpretációban

A fizikusok a posztulátumokat másképp, öt pontban fogalmazzák meg:

1. Minden kvantumrendszert egy $\Psi(r, t)$ **hullámfüggvény** ír le, amely függ a térbeli koordinátáktól ($r$) és az időtől ($t$). Ez a függvény tartalmazza a rendszer összes mérhető információját.
2. Minden fizikailag megfigyelhető tulajdonságot (például energia, impulzus, pozíció) egy **hermitikus operátor** ábrázol. Ezek az operátorok a hullámfüggvényre hatva adják meg a megfigyelhető értékeit.
3. Ha egy kvantumrendszeren mérést végzünk, az eredmény a megfelelő operátor egyik sajátértéke lesz. Egy adott sajátérték megfigyelésének valószínűségét a hullámfüggvénynek a megfelelő sajátállapotra vett vetülete nagyságának négyzete határozza meg.
4. Méréskor a rendszer hullámfüggvénye „összeomlik” a megfigyelt sajátértéknek megfelelő sajátállapotok egyikébe.
5. A hullámfüggvény időbeli alakulását az időfüggő Schrödinger-egyenlet írja le:

   $$i\hbar \frac{d}{dt}\ket{\Psi(t)} = \hat{H}\ket{\Psi(t)}$$

A hermitikus operátorok sajátértékei valósak, így a mérés eredményei is csak valós számok lehetnek. Sajátállapotaik ortonormált bázist alkotnak, amely kifeszíti a teljes Hilbert-teret; ez kell ahhoz, hogy egy kvantumállapotot teljes mértékben leírhassunk. A hermitikus operátorok **önadjungáltak**: az operátor megegyezik a saját komplex konjugált transzponáltjával. Mátrixok esetén ez azt jelenti, hogy a főátló elemei valós számok, a főátlóra tükrös elemek pedig egymás komplex konjugáltjai. Mérhető fizikai mennyiség például a hely operátor $\hat{x}$, a lendület operátor $\hat{p}$ és az energia (Hamilton-operátor) $\hat{H}$.

A mérés hatására a kvantuminformáció klasszikus információvá alakul. A mérnöki interpretációban a fizikusi 3. pont vetületnégyzete a komplex valószínűségi amplitúdó abszolútérték-négyzete, a 4. pont pedig a mérés utáni állapot képlete.

<p class="sources">Forrás: Kvantuminformatikai alkalmazások_posztulátumok.pdf (4., 6., 8., 14–15., 19. dia), 03_osszefonodasalapjai_20260923.pdf (6–8. dia), 04_Meresek20260930.pdf (6–7. dia), 05_INterferometer_es_NCT20261007.pdf (3. dia), bloch_gyak.pdf (2–3. dia), gyak1.pdf (2. dia), Kvantuminformatikai alkalmazások jegyzet 2026 ősz.md</p>
