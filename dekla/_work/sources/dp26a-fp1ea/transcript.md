# dp26a-fp1ea.pdf

<!-- 136 pages, 55 units, grouping: labels -->

## s1 · p1 · (no title)
<!-- status: auto -->
<!-- header: Deklaratív programozás 1. előadás | 1 / 52 -->

Deklaratív programozás 1. előadás

Kabódi László^(1) Marussy Kristóf^(2)

BME Számítástudományi és Információelméleti Tanszék Mesterséges Intelligencia és Rendszertervezés Tanszék

1`kabodi.laszlo@vik.bme.hu`

2`marussy@mit.bme.hu`

2026. ősz

## s2 · p2 · I. rész
<!-- status: auto -->

Deklaratív programozás, követelmények,

áttekintés

1 Deklaratív programozás, követelmények, áttekintés

2 Elixir: fő jellemzői, telepítés, használat

## s3 · p3 · A tantárgy témája
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | 3 / 52 -->

- Deklaratív programozási nyelvek – gyakorlati megközelítésben
- Két fő irány:
  - funkcionális programozás **Elixir** nyelven,
  - logikai programozás **Prolog** nyelven.

## s4 · p4 · Tartalom
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | Tudnivalók, követelmények | 4 / 52 -->

1 Deklaratív programozás, követelmények, áttekintés
- Tudnivalók, követelmények
- A deklaratív programozási paradigma áttekintése

## s5 · p5 · Honlap, Elektronikus TanárSegéd, Teams csoport
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | Tudnivalók, követelmények | 5 / 52 -->

- Honlap: <https://dp.iit.bme.hu>, a jelen félév honlapja: <https://dp.iit.bme.hu/dp-current>
- ETS, az Elektronikus TanárSegéd^(1) <https://dps.iit.bme.hu/ets>, csak a tantárgy jelenlegi hallgatói tudnak belépni a Neptun-kódjukkal
- Deklaratív programozás Teams csoport
1Az ETS 2024-es új kiadása Hanák Dávidnak köszönhető. Forrás: <https://github.com/dhanak/ets/>

Links: <https://dp.iit.bme.hu>, <https://dp.iit.bme.hu/dp-current>, <https://dps.iit.bme.hu/ets>, <https://github.com/dhanak/ets/>

## s6 · p6 · DP-követelmények: gyakorlatok
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | Tudnivalók, követelmények | 6 / 52 -->

Gyakorlatok
- Az 1. oktatási héttől kezdve lesznek tantermi gyakorlatok, mégpedig az ötkredites VISZAD01 kurzus hallgatói számára minden héten, a háromkredites VISZAD00 kurzus hallgatói számára minden második héten. Részletes beosztás a honlapon.
- A gyakorlatok anyagát elektronikus formában a honlapon tesszük közzé.
- A tantermi gyakorlatokon nagyon ajánlott a hordozható számítógép (laptop) használata, különösen az FP-gyakorlatokon, ahol a Livebook for Elixir notebook-formában adjuk ki a feladatsorokat.
- További Elixir gyakorlási lehetőség az EDUX, Prolog gyakorlási lehetőség a PLWIN rendszerben (lásd honlap).

## s7 · p7 · DP-követelmények: kis házi feladatok
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | Tudnivalók, követelmények | 7 / 52 -->

Kis házi feladatok (KHF)
- 3 feladat funkcionális, 3 logikai programozási nyelven, ütemterv szerint.
- Kiírás a honlapon, beadás szintén elektronikus úton (ld. honlap, ETS).
- **Kötelező** legalább **két** FP és **két** LP KHF érvényes és sikeres beadása.
- A KHF-ek egyre összetettebbek és részben *egymásra épülnek* – érdemes *minél előbb* elkezdeni a KHF-ek beadását!
- Egy KHF beadása érvényes, ha az összes beadási tesztesetre jól fut le.
- A KHF-ek az ún. éles tesztelés során kapnak pontszámot (ezek az éles tesztesetek a beadási tesztesetekhez hasonlóak, de nem ugyanazok).
- Minden KHF sikeres megoldásáért – azaz az összes éles teszteset megoldásáért – 1-1 jutalompont (azaz a 100 alappont feletti pont) jár.
- Ha valaki mindhárom KHF-et megoldja az adott nyelven, azzal **megduplázza** a pontszámát, azaz 3 helyett 6 pontot kap.
- Minden **KHF**-nek külön határideje van, **pótlási lehetőség nincs**.
- A beadási határidejéig a KHF többször is beadható, az utolsót értékeljük.
- Mindenkinek el kell tudnia magyaráznia a megoldását az oktatóknak.

## s8 · p8 · DP-követelmények: nagy házi feladat
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | Tudnivalók, követelmények | 8 / 52 -->

Nagy házi feladat (NHF)
- Programozás mind funkcionális, mind logikai nyelven.
- Mindenkinek önállóan kell dolgoznia!
- Elvárás: hatékony (időlimit!), jól dokumentált („kommentezett”) programok.
- A programokhoz 5–10 oldalas fejlesztői dokumentáció PDF-ben.
- Az FP NHF kiírása 6. héten, az LP NHF-é 11. héten a honlapon.
- Az FP NHF beadása 8. héten, az LP NHF-é 13. héten az ETS-sel.
- A beadáskor és a pontozáskor most is külön-külön tesztsorozatot használunk (nehézségben hasonlókat, de nem azonosakat).
- Azok a programok, amelyek megoldják az éles tesztesetek 80%-át, létraversenyen vesznek részt (hatékonysági, gyorsasági plusz pontokért).
- Azok a hallgatók, akik **mindkét** nyelvből bejutnak a létraversenybe, és a kis házi feladatokra vonatkozó követelményeket is teljesítik, **megajánlott** jegyet kapnak.
- A beadási határidejéig az NHF többször beadható, az utolsót értékeljük.

## s9 · p9 · DP-követelmények: nagy házi feladat (folyt.)
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | Tudnivalók, követelmények | 9 / 52 -->

Nagy házi feladat (folyt.)
- Pontozása mindkét nyelvből:
  - helyes (azaz jó eredményt időkorláton belül adó) futás esetén a 10 teszteset mindegyikére 0,5-0,5 pont, összesen max. 5 pont;
  - a dokumentációra, a kód olvashatóságára, kommentezettségére max. 2 pont;
  - tehát nyelvenként összesen max. 7 pont szerezhető.
- Így az NHF súlya az osztályzatban: 14% (a 100 pontból 14).
- Az NHF beadása **nem kötelező, de ajánlott!** Hogy miért? Többek között
  - egy-egy nagyobb feladat megoldásával lehet igazán megérteni, megérezni a funkcionális, ill. a logikai programozási szemléletet;
  - mindkét NHF hatékony megoldásával megajánlott jegyet lehet szerezni, ami a külföldön tanulóknak, „home office”-ban dolgozóknak, sok zéhát íróknak stb. különösen hasznos lehet;
  - maguk a feladványok is érdekesek, például abból a szempontból, hogy hogyan lehet hatékonyan algoritmizálni őket;
  - lehetőséget adnak egy új szakmai területre, a korlátprogramozásba (constraint programming) való „belekóstolásra”.

## s10 · p10 · DP-követelmények: zárthelyik
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | Tudnivalók, követelmények -->

Nagyzárthelyik, pótzárthelyik (NZH-k, PZH-k)
- Két NZH-t tartunk, egyet a funkcionális, egyet a logikai részből.
- Két PZH-t tartunk, mindkét PZH-n bármelyik NZH-t lehet pótolni, akár mind a kettőt (de szűkebb időkerettel).
- Az FP-zéhákat terveink szerint gépteremben, Livebook for Elixir notebookkal kell megírni.
- Mind a funkcionális, mind a logikai részből **kötelező** a zárthelyi érvényes teljesítése, kivéve megajánlott jegy esetén (lásd alább).
- 40%-os szabály: **nyelvenként** a maximális pontszám 40%-a kell az érvényességhez.
- Zárthelyi időpontok: lásd a honlapon.
- A zárthelyik súlya az osztályzatban: 43%–43% (a 100 pontból max. 86).

## s11 · p11-12 · DP-követelmények: megajánlott jegy, önálló feladatmegoldás
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | Tudnivalók, követelmények -->

A megajánlott jegy feltételei
- Alapfeltételek: a KHF követelmények teljesítése; az NHF „megvédése”.
- Azok a programok, amelyek megoldják az éles tesztesetek 80%-át az időkorláton belül, létraversenyen vesznek részt
  - Jóval nehezebb létra-tesztesetek: verseny a hallgatók között, hogy kinek a programja hányat tud megoldani időre
- Jó (4): a nagy házi feladat mindkét nyelvből bejut a létraversenybe.
- Jeles (5): legalább 40%-os eredmény a létraversenyen, mindkét nyelvből.
Az NHF „megvédése” azt jelenti, hogy a hallgatónak személyes (vagy távjelenléti) formában el kell magyaráznia a tantárgy egy oktatójának, hogyan oldotta meg az NHF-et, és válaszolni kell tudnia az oktató kérdéseire.

*Magától értetődő, hogy* minden házi feladatot önállóan kell elkészíteni. Másolás esetén kötelesek vagyunk fegyelmi eljárást indítani, *lásd a 3/2011.* (III.23.) rektori utasításban a "Beadandó feladat, szakdolgozat, diplomaterv elkészíttetése mással" tételt.

Links: <http://www.kth.bme.hu/document/189/original/bme_rektori_utasitas_05.pdf>

## s12 · p13 · DP-követelmények: IMSc-pontozás
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | Tudnivalók, követelmények -->

- A tantárgyból kétféle módon szerezhető IMSc pont:
  - egyes zárthelyik során pluszfeladatok megoldásával (max. 13 pont),
  - a létraversenyen a megajánlott jeles érdemjegyhez szükséges 40%-os teljesítés felett minden további 10%-os teljesítésért mindkét nyelv esetén 1–1 pont (összesen max. 12 pont).
- A hallgató a fenti módokon szerzett pontok összegét kapja, de a VISZAD00 kurzus esetén legfeljebb 15 IMSc pontot.
- Az IMSc pontok gyűjtése teljesen független a tantárgyban szerezhető ZH és HF pontoktól. Ezen pontok megszerzése és a fakultatív feladatok megoldása nélkül is jeles szinten teljesíthetők a tantárgy követelményei.
- Az IMSc pontok megszerzése az IMSc programban nem résztvevő hallgatók számára is lehetséges.

## s13 · p14 · Tartalom
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | A deklaratív programozási paradigma áttekintése -->

1 Deklaratív programozás, követelmények, áttekintés
- Tudnivalók, követelmények
- A deklaratív programozási paradigma áttekintése

## s14 · p15-19 · Deklaratív programozás
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | A deklaratív programozási paradigma áttekintése -->

- A „deklaratív programozás” jelentése (Wikipédia): (. . . ) a deklaratív programozás egy programozási paradigma, (. . . ) amely kifejezi a számítás logikáját anélkül, hogy leírná a vezérlési folyamatát. (. . . ) declarative programming is a programming paradigm (. . . ) that expresses the logic of a computation without describing its control flow.
- A „deklaratív” jelző értelmezése (Topszótár):
  - *kijelentő*, kinyilatkoztató
  - ellentmondást nem tűrő
- A *„deklaratív”* jelző a nyelvészetből származik, pl. „kijelentő mondat”.
- Milyen más mondatfajták vannak?
  - kérdő,
  - *felszólító* (imperatív) stb.
- A számítógépek belső nyelve (gépi kódja) alapvetően *felszólító* jellegű: add hozzá, szorozd meg, ugorj, . . .
- A magas szintű programnyelvek többsége is *imperatív*: `while ... do ...`, `goto ...`, értékadás (írd felül a változó értékét) stb.

## s15 · p20-21 · Deklaratív programozás (folyt.)
<!-- status: viewed pages/p021.png -->
<!-- flags: layout -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | A deklaratív programozási paradigma áttekintése -->

- Lehet-e pl. C-ben deklaratívan programozni?
  Igen, pl. ciklus helyett rekurzió használatával:

  ```c
  int fact(int n) {if (n > 0) return n * fact(n-1);
                    else return 1;
                   }
  ```

- Igen, de ez lassú! ⇝ Ún. jobbrekurzív (farokrekurzív, tail recursive) változata a ciklussal azonos hatékonyságú kóddá fordul.
- Mi az előnye a deklaratív szemléletnek? A programkód sokkal közelebb áll a specifikációhoz, helyességéről sokkal könnyebb meggyőződni.
- A deklaratív megközelítés jelmondata:

  *MIT* és nem *HOGYAN*

  vagy kicsit enyhítve:

  Inkább *MIT,* mint *HOGYAN*
  (*WHAT* rather than *HOW*)

- A *deklaratív* nyelvekben a *változó* a *matematika* változófogalmának felel meg: *egyetlen*, esetleg még ismeretlen értéket jelöl.

## s16 · p22-23 · Funkcionális és logikai programozás
<!-- status: viewed pages/p023.png -->
<!-- flags: graphic, layout -->
<!-- figure: figures/p023-f1.png -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | A deklaratív programozási paradigma áttekintése -->

- A *deklaratív* programozás két fő ága egy-egy alapvető *matematikai fogalom*hoz kapcsolódik:
  - Funkcionális programozás (FP) – *függvények*
  - Logikai programozás (LP) – *relációk*

Figure: fa diagram „**Programozási paradigmák – programozási nyelvek**” címmel. A gyökérből két él vezet lefelé: balra az **Imperatív**, jobbra a **Deklaratív** csomóponthoz. Az Imperatív alatt nyelvlista: *Fortran*, *Algol*, *C*, *Java*, *Python*, *. . .* (dőlt betűvel). A Deklaratív csomópontból két él vezet lefelé: balra a **Funkcionális**, jobbra a **Logikai** csomóponthoz. A Funkcionális alatt: *LISP*, *ML*, *Haskell*, *Erlang*, *Elixir* (kiemelt színnel), *. . .*. A Logikai alatt: *SQL*, *Prolog* (kiemelt színnel), *Constraint Prog.*, *. . .*.
Use: redraw

- A kurzus tárgya: az *Elixir* funkcionális és a *Prolog* logikai programozási nyelv.

## s17 · p24-32 · Példa: Listák összefűzése Elixirben és Prologban
<!-- status: auto -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | A deklaratív programozási paradigma áttekintése -->

- Az Elixir és a Prolog nyelvek (közös) szintaxisa a láncolt listák jelölésére:
  - `[]` – üres lista
  - `[Head|Tail]` – egy olyan lista, amelynek feje `Head`, farka pedig `Tail`
- Példa: az `1`, `2`, `3` számokból álló lista: `[1|[2|[3|[]]]]`
- Ugyanez az adatstruktúra tömörebben is leírható: `[1,2,3]`
- Írjunk egy `app` nevű kétargumentumú *Elixir függvényt* (`app/2`):

```
#   app(l1,   l2): l1 és l2 listák összefűzöttje (l1⊕l2)
def app([],    b) do            b end       # [] ⊕b = b
def app([x|a], b) do [x|app(a,b)] end       # [x|a] ⊕b = [x|a⊕b]
```

- Az `app` függvénynek egy 3-argumentumú *Prolog eljárás* (másnéven *predikátum*) felel meg (`app/3`), a 3. argumentum az *Elixir fv.* eredménye):

```
%   app(L1, L2, L12): L1 és L2 listák összefűzöttje L12 (L1⊕L2 = L12)
    app([],    B,               B).         % [] ⊕B = B
    app([X|A], B,    [X|       C]) :-       % [X|A] ⊕B = [X|C] ha
           app(A, B, C).                    %      A ⊕B = C
```

- Az eljáráshívások (a függvényhívásokkal ellentétben) nem ágyazhatók egymásba, ezért van szükség a `C` segédváltozóra.
- **DE**: az `app/3` Prolog eljárás jobbrekurzív (azaz ciklussá fordul!)

## s18.1 · p33-44 · Az app/3 Prolog eljárás használata
<!-- status: viewed pages/p034.png -->
<!-- flags: variant -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | A deklaratív programozási paradigma áttekintése -->

- Prologban megengedett, hogy egy *adatstruktúrában* *behelyettesítetlen* változó szerepeljen:

  ```prolog
  app([],    B, B).
  app([X|A], B, L) :- L = [X|C], app(A, B, C).
  ```

- A Prolog változó pointerként is felfogható: pl. `app` először felépíti az eredménylista első láncszemét (`[X|C]`), majd az `app` jobbrekurzív hívásával kitölti az eredménylista `C` által mutatott farkát

<!-- note: the later steps (p35-p44) only append ", pl." to the last sentence and add content; everything here is also in s18.2 -->


## s18.2 · p33-44 · Az app/3 Prolog eljárás használata
<!-- status: viewed pages/p044.png -->
<!-- flags: layout, variant -->
<!-- header: Deklaratív programozás, követelmények, áttekintés | A deklaratív programozási paradigma áttekintése -->

Differs from s18.1: the second bullet ends in "farkát, pl." followed by a worked example, and a third bullet with Prolog queries and their answers is added (built up line by line on p36-p44).

- Prologban megengedett, hogy egy *adatstruktúrában* *behelyettesítetlen* változó szerepeljen:

  ```prolog
  app([],    B, B).
  app([X|A], B, L) :- L = [X|C], app(A, B, C).
  ```

- A Prolog változó pointerként is felfogható: pl. `app` először felépíti az eredménylista első láncszemét (`[X|C]`), majd az `app` jobbrekurzív hívásával kitölti az eredménylista `C` által mutatott farkát, pl.

  ```text
  app([1], [2], L) ⇒ L = [1|C], app([], [2], C) ⇒ L = [1|[2]] = [1,2]
  ```

- Az `app/3` eljárás nemcsak összefűzésre használható:

  ```text
  | ?- app([1,2], [3,4], L).        ⟹   L = [1,2,3,4] ? ; no
  | ?- app([1,2], B, [1,2,3,4]).    ⟹   B = [3,4] ? ; no
  | ?- app([1,2], B, [1,3,4,5]).    ⟹   no
  | ?- app(A, B, [1,2]).            ⟹   A = [], B = [1,2] ? ;
                                         A = [1],  B = [2] ? ;
                                         A = [1,2], B = [] ? ; no
  ```

<!-- note: queries on the left, the Prolog answers to the right of the ⟹ arrows; the arrows are slide notation, not Prolog. The math flag was removed: the only symbols are ⇒/⟹ arrows inside code. -->


## s19 · p45 · II. rész
<!-- status: auto -->

Elixir: fő jellemzői, telepítés, használat

1 Deklaratív programozás, követelmények, áttekintés

2 Elixir: fő jellemzői, telepítés, használat

## s20 · p46 · Tartalom
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir nyelv fő jellemzői -->

2 Elixir: fő jellemzői, telepítés, használat
- FPE-1 – Az Elixir nyelv fő jellemzői
- FPE-1 – Elixir: Telepítés, szövegszerkesztők
- FPE-1 – Az Elixir interaktív használata (`IEx`)
- FPE-1 – Projektszervezés és más hasznosságok: mix, benchee

## s21 · p47 · Az Elixir nyelv fő jellemzői
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir nyelv fő jellemzői -->

- Funkcionális
- A nyelvben minden kifejezés (nincs statement / expression megkülönböztetés)
- Mintaillesztés
- Rekurzió és magasabb rendű függvények (ciklusok helyett)
- Dinamikusan típusos
- Nincs semmi megosztva, a processzek üzenetekkel kommunikálnak
- Erlang függvények hívhatók Elixirből, Elixir függvények Erlangból

## s22.1 · p48-52 · Mintaillesztés
<!-- status: viewed pages/p051.png -->
<!-- flags: variant -->
<!-- header: FPE-1 – Az Elixir nyelv fő jellemzői -->

- Mintakifejezés, röviden minta: termhez hasonló olyan kifejezés, amelyben nincs függvénykifejezés, de lehet benne szabad változó
- Egy szabad változó mindenre illeszkedik, az értékét az illeszkedő kifejezés megfelelő részéhez *kötjük* a sikeres illesztéskor
- Egyszerű változó kötés: `x = 5`, az `x` mintát illeszti az 5 kifejezésre
- `[hd|tl] = valami()`: `hd` és `tl` változókat köti a `valami()` által visszaadott lista fejéhez és farkához
  - hibával leáll, ha a `valami()` üres listával (vagy bármi mással) tér vissza: `(MatchError) no match of right hand side value`
- Mintaillesztés `case` kifejezéssel

  ```elixir
  case valami() do
    [hd|tl] -> ... # Ha nem üres lista
    [] -> ... # Ha üres lista
    _ -> ... # Bármi más
  end
  ```

## s22.2 · p48-52 · Mintaillesztés
<!-- status: viewed pages/p052.png -->
<!-- flags: variant -->
<!-- header: FPE-1 – Az Elixir nyelv fő jellemzői -->

Differs from s22.1: the `case` example is replaced by one with a guard (`when is_integer(hd)`) and concrete results (`hd * 2`, `0`, `nil`) instead of `...`; the bullet reads "kifejezéssel és *őrfeltétellel*"; a last bullet on function calls is added.

- Mintakifejezés, röviden minta: termhez hasonló olyan kifejezés, amelyben nincs függvénykifejezés, de lehet benne szabad változó
- Egy szabad változó mindenre illeszkedik, az értékét az illeszkedő kifejezés megfelelő részéhez *kötjük* a sikeres illesztéskor
- Egyszerű változó kötés: `x = 5`, az `x` mintát illeszti az 5 kifejezésre
- `[hd|tl] = valami()`: `hd` és `tl` változókat köti a `valami()` által visszaadott lista fejéhez és farkához
  - hibával leáll, ha a `valami()` üres listával (vagy bármi mással) tér vissza: `(MatchError) no match of right hand side value`
- Mintaillesztés `case` kifejezéssel és *őrfeltétellel*

  ```elixir
  case valami() do
    [hd|tl] when is_integer(hd) -> hd * 2 # Ha nem üres lista
    [] -> 0 # Ha üres lista
    _ -> nil # Bármi más: hibajelzés
  end
  ```

- Függvényhívás: az aktuális paramétereket *illesztjük* a formális paraméterekre az egyes *klózokban*

## s23 · p53-57 · Rekurzió
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir nyelv fő jellemzői -->

- Lineáris rekurzió: egy *rekurzív hívás* a függvényben

```
def fac(0), do: 1 # 1. klóz: Alapeset
def fac(n): do: n * fac(n - 1) # 2. klóz: Rekurzív eset
```

- Jobbrekurzív (farokrekurzív, tail recursive): rekurzív hívás *visszatérési* *pozícióban* →hatékonyabb gépi kód, nem kell stack

```
def fac(n), do: fac(n, 1) # Segédfüggvény meghívása akkumulátor paraméterrel
def fac(0, a), do: a
def fac(n, a), do: fac(n - 1, n * a)
```

- Elágazó rekurzíció: több *rekurzív hívás*, sokszor nem hatékony

```
def fib(n) when n <= 1, do: n # 1. klóz őrfeltétellel: Alapeset
def fib(n), do: fib(n - 1) + fib(n - 2) # 2. klóz: Rekurzív eset
```

- Lineáris rekurzív adatszerkezetek: pl. `[...]` egyszeresen láncolt listák
  - Alapeset: `[]` üres lista
  - *Rekurzív eset*: legalább egy elemű `[H|T]`, ahol `T` is egy lista (`[]` vagy legalább egy elemű)
- Elágazó rekurzív adatszerekezetek: pl. bináris fa
- Algebrai módszer: *rekurzív adatszerekezetek* feldolgozása *mintaillesztéssel* rekurzív függvényekkel

## s24 · p58-62 · Magasabb rendű függvények
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir nyelv fő jellemzői -->

- A függvény is érték: változóhoz köthető, adatstruktúra eleme lehet, függvény eredménye lehet, paraméterként átadható stb. Azaz: a függvény is ún. first class citizen, teljes jogú polgár

```
> L.map [1, 2, 3], fn(x) -> 2 * x end
[2, 4, 6]
```

- Egyre gyakoribb az objektumorientált nyelvekben is
    - Java: `List.of(1, 2, 3).stream().map(x -> 2 * x).toList()`
    - C#: `new List<int>{1, 2, 3}.Select(x => 2 * x)`
- Ciklusok helyett: szétválaszthatjuk az adatszerkezet rekurzív bejárását az elvégzendő műveletektől

```
defmodule L do # Egyszeresen láncolt lista bejárás
  def map([], _f), do: []
  def map([hd|tl], f), do: [f.(hd)|map(tl, f)]
end
defmodule T do # Bináris fa bejárás
  def map(nil, _f), do: nil
  def map({x, left, right}, f), do: {f.(x), map(left, f), map(right, f)}
end
```

## s25 · p63-66 · Dinamikus típusok
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir nyelv fő jellemzői -->

Az Elixir
- erősen típusos: minden értéknek pontosan egy futásidejű típusa van
- dinamikus típusellenőrzéssel: a típusokat nem kötelező megadni a kódban, egy változóhoz nem feltétlenül csak egy típus tartozik
- *DE:* típus specifikációk megadhatók dokumentációs céllal
  - @spec tl(xs :: [any()]) :: ts :: [any()] | nil „A `tl` függvény argumentuma egy `xs` tetszőleges elemű lista, visszatérési értéke (`ts`) egy szintén tetszőleges elemű lista vagy `nil`.”
  - @spec nth(xs :: [any()], n :: integer()) :: r :: any() | nil „Az `nth` függvény argumentumai egy `xs` tetszőleges elemű lista és egy `n` egész szám, visszatérési értéke (`r`) vagy egy tetszőleges típusú érték vagy `nil`.”

## s26 · p67-71 · Folyamatok üzenetekkel kommunikálnak
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir nyelv fő jellemzői -->

- Nincs folyamatok (processzek) között megosztott memória
- Kommunikáció üzenetküldés segítségével (aktor modell)

```
worker = spawn(fn -> # Új folyamat indítása
  receive do # Várakozás üzenetre
    {:hello, from} -> # Válasz küldése from felé
      send(from, {:reply, "Hello from the worker process!"})
  end
end)
send(worker, {:hello, self()}) # Üzenet küldése válaszcímmel
receive do # Várakozás a worker folyamat válaszára
  {:reply, message} -> # Üzenet fogadása mintaillesztéssel
    IO.puts(message)
end
```

- Válasz egymásutáni üzenetekre rekurzív függvények segítségével

## s27 · p72-76 · Erlang és Elixir
<!-- status: viewed pages/p076.png -->
<!-- header: FPE-1 – Az Elixir nyelv fő jellemzői -->

- Erlang Open Telecom Platform (OTP): az Ericsson által fejlesztett nyílt forráskódú rendszer masszívan párhuzamos, elosztott, megbízható alkalmazások fejlesztésére
  - Kihasználja az üzenetküldést és azt, hogy nincs megosztott memória vagy változó módosítás
  - Akár függvények is átküldhetők a szerverek között
- Erlang: az OTP platform eredeti funkcionális programozási nyelve, Prologhoz hasonló szintaxis
- BEAM: az Erlang/OTP virtuális gépe
- Elixir: funkcionális programozási nyelv a BEAM platforma, modern (Ruby-ra hasonlító) szintaxissal <!-- suspect: "a BEAM platforma" probably means "a BEAM platformra" (missing "r") -->

BEAM : Erlang : Elixir ≈ JVM : Java : Kotlin

Jupyter ≈ Livebook

<!-- note: the two centred lines are analogies (≈ = "is like"), not formulas; the math flag was removed -->


## s28 · p77 · Tartalom
<!-- status: auto -->
<!-- header: FPE-1 – Elixir: Telepítés, szövegszerkesztők -->

2 Elixir: fő jellemzői, telepítés, használat
- FPE-1 – Az Elixir nyelv fő jellemzői
- FPE-1 – Elixir: Telepítés, szövegszerkesztők
- FPE-1 – Az Elixir interaktív használata (`IEx`)
- FPE-1 – Projektszervezés és más hasznosságok: mix, benchee

## s29 · p78 · Elixir: használat, telepítés
<!-- status: auto -->
<!-- header: FPE-1 – Elixir: Telepítés, szövegszerkesztők -->

- Elixir homokozó: <https://dps.iit.bme.hu/edux/>.^(2)
- Az Elixir előtt a megfelelő verziójú Erlangot is telepíteni kell.
- Telepítés: <https://elixir-lang.org/install.html>
- Összetettebb esetekhez: különféle csomagkezelők: Debian, Ubuntu, Windows, macOS
  - **asdf** verziókezelő (több verzió telepíthető vele párhuzamosan).
  - **mise** verziókezelő (asdf-en alapul, ugyancsak több verziót tud kezelni): <https://mise.jdx.dev/getting-started.html>. Az Erlangot a **mise** alapból ismeri (lásd: Plugins, Core Plugins), az Elixir telepítése itt van leírva: <https://github.com/mise-plugins/mise-elixir>.
2Köszönet Gergely Viktornak az EDUX-ért! Forrás: <https://github.com/vikger/edux/>

Links: <https://dps.iit.bme.hu/edux/>, <https://elixir-lang.org/install.html>, <https://github.com/mise-plugins/mise-elixir>, <https://github.com/vikger/edux/>, <https://mise.jdx.dev/getting-started.html>

## s30 · p79 · Livebook for Elixir telepítése
<!-- status: auto -->
<!-- header: FPE-1 – Elixir: Telepítés, szövegszerkesztők -->

- A Livebook a Python Jupyterhez hasonló notebook. Telepítéséről itt lehet olvasni: <https://livebook.dev/#install>.
- Macre és Windowsra telepítőkkel lehet fölrakni.
- Linuxon csak kicsit bonyolultabb (hála az Elixir escript funkciójának), a leírás itt található: <https://github.com/livebook-dev/livebook#direct-installation-with-elixir>.
- Ha az Elixirt és Erlangot a mise-zel telepítettük, akkor az Erlang függőségeit, amelyek az említett szakaszban vannak felsorolva (`inets`, `os_mon`, `runtime_tools`, `ssl`, `xmerl`), nem az operációs rendszer, hanem az Erlang már említett rebar csomagkezelőjével kell telepíteni:
  - `rebar3 local install inets` stb.
- Futtatás csomagkezelőből telepítés után: <https://github.com/livebook-dev/livebook#escript>.
Ha nem akarunk a telepítésekkel bajlódni, akkor használhatjuk a dockerizált Elixirt és Livebookot. Részletek a következő dián.

Links: <https://github.com/livebook-dev/livebook#direct-installation-with-elixir>, <https://github.com/livebook-dev/livebook#escript>, <https://livebook.dev/#install>

## s31 · p80 · Elixir: használat Docker konténerekkel
<!-- status: auto -->
<!-- header: FPE-1 – Elixir: Telepítés, szövegszerkesztők -->

- Elixir Docker: <https://elixir-lang.org/install.html#docker>
  - Run iex (interactive mode): `docker run -it --rm elixir`
  - Run elixir (compiler & iex): `docker run -it --rm elixir bash`
- Elixir notebook, azaz Livebook for Elixir: <https://livebook.dev/>
  - Docker: <https://github.com/livebook-dev/livebook#docker>
  - Lokális tárhely a `-v $(pwd):/data` opcióval megadott mappában; `$(pwd)` használata esetén abban a mappában, ahol a `docker ...` parancsot kiadjuk. Tulajdonosi jogok beállítása a `-u $(id -u):$(id -g)` opcióval.

```
docker run -p 8080:8080 -p 8081:8081 --rm --pull always \
-u $(id -u):$(id -g) -v $(pwd):/data ghcr.io/livebook-dev/livebook
```

  - Már letöltött konténer gyorsindítása frissítés nélkül:

```
docker run -p 8080:8080 -p 8081:8081 --rm \
-u $(id -u):$(id -g) -v $(pwd):/data ghcr.io/livebook-dev/livebook
```

Links: <https://elixir-lang.org/install.html#docker>, <https://github.com/livebook-dev/livebook#docker>, <https://livebook.dev/>

## s32 · p81 · Elixir: szövegszerkesztők
<!-- status: auto -->
<!-- header: FPE-1 – Elixir: Telepítés, szövegszerkesztők -->

- Editors for Elixir: <https://github.com/elixir-editors>
  - vim-elixir for VIM: <https://github.com/elixir-editors/vim-elixir>
  - emacs-elixir for Emacs: <https://github.com/elixir-editors/emacs-elixir>
  - language-elixir for Atom: <https://github.com/elixir-editors/language-elixir>
  - Visual Studio Code with ElixirLS: <https://thinkingelixir.com/elixir-in-vs-code/>
  - IntelliJIdea with intellij-elixir plugin: <https://github.com/KronicDeth/intellij-elixir>

Links: <https://github.com/KronicDeth/intellij-elixir>, <https://github.com/elixir-editors>, <https://github.com/elixir-editors/emacs-elixir>, <https://github.com/elixir-editors/language-elixir>, <https://github.com/elixir-editors/vim-elixir>, <https://thinkingelixir.com/elixir-in-vs-code/>

## s33 · p82 · Elixir felvezető tutorial Livebookban
<!-- status: auto -->
<!-- header: FPE-1 – Elixir: Telepítés, szövegszerkesztők -->

Az Elixir az előadásban szereplő jellegzetességeinek további bemutatásához Livebook segítségével készítettünk egy interaktív bemutatót. A Livebook-példák interaktív Markdown formátumban innen tölthetők le:
- <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp1gyfel.livemd>.
Mivel egyetlen programozási nyelvet sem lehet lineárisan, minden részletre kitérve ismertetni, megtanulni, ezért a fontos dolgokra később is visszatérünk.

A következő diákon az Elixir interaktív használatát mutatjuk be kisebb példákon.

Links: <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp1gyfel.livemd>

## s34 · p83 · Tartalom
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir interaktív használata (IEx) -->

2 Elixir: fő jellemzői, telepítés, használat
- FPE-1 – Az Elixir nyelv fő jellemzői
- FPE-1 – Elixir: Telepítés, szövegszerkesztők
- FPE-1 – Az Elixir interaktív használata (`IEx`)
- FPE-1 – Projektszervezés és más hasznosságok: mix, benchee

## s35 · p84-98 · Interactive Elixir (REPL: read-eval-print loop)
<!-- status: viewed pages/p098.png -->
<!-- flags: layout -->
<!-- header: FPE-1 – Az Elixir interaktív használata (IEx) -->

<!-- note: two columns separated by a vertical line; the first block is the left column, the second the right column. Typed input (iex, expressions, Ctrl+C, Ctrl+G, h, q) is shown in red on the slide. -->

```iex
$ iex
Erlang/OTP ...
Interactive Elixir ...
  press Ctrl+C to exit
  (type h() ENTER for help)
iex(1)> 3.2 + 2.1 * 2
7.4
iex(2)> :atom
:atom
iex(3)> Atom
Atom
iex(4)> "string"
"string"
iex(5)> {:ennes,:%,A,:':',9.8}
{:ennes, :%, A, :":", 9.8}
iex(6)> [:lista,:%,A,:':',9.8]
[:lista, :%, A, :":", 9.8]
iex(7)> i :':'
...Data type
    Atom...
```

```iex
iex(8)> Ctrl+C
BREAK: (a)bort (A)bort with dump (c)ontinue
   (p)roc info (i)nfo (l)oaded (v)ersion
   (k)ill (D)b-tables (d)istribution
Ctrl+C
$

iex(8>) Ctrl+G
User switch command
--> h
  c [nn]            - connect to job
  i [nn]            - interrupt job
  k [nn]            - kill job
  j                 - list all jobs
  s [shell]         - start local shell
  r [node [shell]]  - start remote shell
  q                 - quit erlang
  ? | h             - this message
  --> q
$
```

<!-- suspect: the prompt "iex(8>) Ctrl+G" has ">" and ")" swapped; it should read "iex(8)>" -->

## s36 · p99-100 · Interactive Elixir (IEx): parancsok
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir interaktív használata (IEx) -->

```
iex(1)> h().
Welcome to Interactive Elixir.
...
c/1            - compiles a file
c/2            - compiles a file and writes bytecode to the given path
cd/1           - changes the current directory
clear/0        - clears the screen
exports/1      - shows all exports (functions + macros) in a module
h/1            - prints help for the given module, function or macro
i/0            - prints information about the last value
i/1            - prints information about the given term
ls/0           - lists the contents of the current directory
ls/1           - lists the contents of the specified directory
pwd/0          - prints the current working directory
r/1            - recompiles the given module's source file
v/0            - retrieves the last value from the history
v/1            - retrieves the nth value from the history
...
To learn more about IEx as a whole, type h(IEx).
```

## s37 · p101-105 · Saját program fordítása, futtatása
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir interaktív használata (IEx) -->

`fpea.ex` – Faktoriális

```
defmodule Fpea do
# Fájlnév csupa kisbetűvel, szavak között aláhúzás (snake_case)
# Modulnév egybe, szavak nagy kezdőbetűvel (BumpyCase, CamelCase)
  @spec fac(n::integer) :: f::integer # Típusspecifikáció
  # f = n! (azaz f az n faktoriálisa) # Fejkomment
  def fac(0), do: 1            # ha az n=0 mintaillesztés sikeres
  def fac(n), do: n * fac(n-1) # ha az n=0 mintaillesztés sikertelen
end

  iex(1)> c "fpea.ex"  # fordítás
  [Fpea]
  iex(2)> Fpea.fac(5)  # futtatás
  120
  iex(3)> fac(5)         # a modulnevet ki kell írni
  ** (CompileError) iex:3: undefined function fac/1
  iex(4)> Fpea.fac 5   # argumentum körül a zárójel sokszor elhagyható
  120
```

## s38.1 · p106-115 · Elixir docker – IEx
<!-- status: viewed pages/p111.png -->
<!-- flags: variant -->
<!-- header: FPE-1 – Az Elixir interaktív használata (IEx) -->

```iex
# tárhely a docker konténerben
$ docker run -it --rm -w /home elixir
Erlang/OTP ...
Interactive Elixir ...
iex(1)> pwd
/home
iex(2)> Enum.map 1..5, fn(x) -> -x end
[-1, -2, -3, -4, -5]
iex(3)> Ctrl+C kétszer

# tárhely a hoszton
$ docker run -it --rm -v "$PWD":/home -w /home elixir
iex(1)>
```

<!-- note: typed input (commands after $ and iex prompts, "Ctrl+C kétszer") is red on the slide; s38.2 only continues the last line ("iex(1)>ls") and adds lines, everything here is also in s38.2 -->

## s38.2 · p106-115 · Elixir docker – IEx
<!-- status: viewed pages/p115.png -->
<!-- flags: variant -->
<!-- header: FPE-1 – Az Elixir interaktív használata (IEx) -->

Differs from s38.1: the last prompt `iex(1)>` is followed by `ls`, and the session continues with compiling `fpea.ex`, `exports Fpea` and calling `Fpea.fac 5`.

```iex
# tárhely a docker konténerben
$ docker run -it --rm -w /home elixir
Erlang/OTP ...
Interactive Elixir ...
iex(1)> pwd
/home
iex(2)> Enum.map 1..5, fn(x) -> -x end
[-1, -2, -3, -4, -5]
iex(3)> Ctrl+C kétszer

# tárhely a hoszton
$ docker run -it --rm -v "$PWD":/home -w /home elixir
iex(1)>ls
fpea.ex      fpea.exs      ...
iex(2)> c "fpea.ex"
[Fpea]
iex(3)> exports Fpea
fac/1
4> Fpea.fac 5
120
```

<!-- suspect: the prompt "4> Fpea.fac 5" should be "iex(4)> Fpea.fac 5" -->

## s39 · p116-123 · Elixir docker – bash
<!-- status: auto -->
<!-- header: FPE-1 – Az Elixir interaktív használata (IEx) -->

```
# tárhely a hoszton
$ docker run -it --rm -v "$PWD":/home -w /home elixir /bin/bash
root@...:/home#
# ls *.ex *.exs
fpea.ex      fpea.exs
# iex fpea.ex
Erlang/OTP ...
Interactive Elixir ...
iex(1)> Fpea.fac 5
120
iex(2)> Ctrl+C kétszer
$root@...:/home# ˆD exit
$
```

## s40 · p124 · Tartalom
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

2 Elixir: fő jellemzői, telepítés, használat
- FPE-1 – Az Elixir nyelv fő jellemzői
- FPE-1 – Elixir: Telepítés, szövegszerkesztők
- FPE-1 – Az Elixir interaktív használata (`IEx`)
- FPE-1 – Projektszervezés és más hasznosságok: mix, benchee

## s41 · p125 · Projektszervezés Elixirben 1: mix
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

Foglalkozzunk egy kicsit az Elixir projektek szervezésével.
- Az Elixirhez sokféle modul van, a gyakran használtak (pl. `Kernel`, `Enum`, `List`, `String`) az Elixir-alapcsomag része, a többit (pl. `Benchee`) utólag kell telepíteni, ha és amikor szükség van rájuk.
- Magának a fordítónak (`elixir`, `elixirc`, `iex`) is, a moduloknak is több verziójuk van, az újabb verziók nem mindig kompatibilisek a korábbiakkal: a függőségeket kezelni kell.
- Általában egy saját projekt is több modulból áll, plusz a teszteléshez használt adatokból, segédprogramokból – célszerű ezeket is jól áttekinthetően, rendben tartani.
- Ahhoz, hogy az Elixirhez kidolgozott segédeszközöket használni tudjuk, be kell tartani a konvenciókat – nemcsak a névadásra, hanem például a fájlokat tároló mappák szerkezetére vonatkozóakat is.
- Elixir projektek kezelésére készült a `mix`. A `mix` az Elixir-csomag része. <https://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html>

Links: <https://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html>

## s42 · p126 · Projektszervezés Elixirben 2: mix
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

Indítsuk el `mix`-et a `~/tmp/` mappában:

```
  ...$ cd ~/tmp
  ~/tmp$ mix --help
Mix is a build tool for Elixir

Usage: mix [task]

Examples:

    mix             - Invokes the default task (mix run) in a project
    mix new PATH    - Creates a new Elixir project at the given path
    mix help        - Lists all available tasks
    mix help TASK   - Prints documentation for a given task

The --help and --version options can be given instead of a task for
usage and versioning information.
```

Használhatjuk a dokkeres Elixirt is:

```
~$ docker run -it --rm -v "$PWD":/home -w /home elixir /bin/bash
.../home#
```

## s43 · p127 · Projektszervezés Elixirben 3: mix
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

Hozzunk létre egy új projektet egy új mappában. A projekt és a mappa neve legyen `fp`. Az `fp/lib` mappában is létrejön egy fájl `fp.ex` néven, benne az Fp modul-sablonnal – ez lenne a neve a `--module` opció nélkül is.

```
# mix new fp --module Fp
* creating README.md
* creating .formatter.exs
* creating .gitignore
* creating mix.exs
* creating lib
* creating lib/fp.ex
* creating test
* creating test/test_helper.exs
* creating test/fp_test.exs

Your Mix project was created successfully.
You can use "mix" to compile it, test it, and more:
    cd fp
    mix test
Run "mix help" for more commands.

# ls -F fp
lib/  mix.exs  README.md  test/
```

## s44 · p128 · Projektszervezés Elixirben 4: mix
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

Nézzük, mi van a `mix.exs` fájlban^(3):

```
~/tmp$ cd fp
~/tmp/fp$ cat mix.exs
defmodule Fp.MixProject do
  use Mix.Project
  def project do
    [
      app: :fp,
      version: "0.1.0",
      elixir: "~> 1.18",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end
  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:logger]
    ]
  end
```

(Folytatás a következő dián.)

3Mi más lenne, mint Elixir-kód. :-)

## s45 · p129 · Projektszervezés Elixirben 5: mix
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

(Az előző dia folytatása.)

```
 # Run "mix help deps" to learn about dependencies.
 defp deps do
  [
   # {:dep_from_hexpm, "~> 0.3.0"},
   # {:dep_from_git, git: "https://github.com/elixir-lang/my_dep.git", tag: ...}
  ]
 end
end
```

- `mix.exs` két publikus (`def`) és egy privát (`defp`) függvényt definiál.
- `project` a projektkonfigurációról tárol adatokat, `appication`-nel pedig egy applikációs fájlt lehet generálni – ezek részleteibe nem megyünk bele.
- A `deps` privát függvény törzsében kell leírni a függőségeket, megadni a kívánt modulok nevét és paramétereit.
- Egy új modult fogunk megadni, a `Benchee`-t, ami – ahogy a neve is sugallja – benchmarkingra használható: <https://github.com/bencheeorg/benchee>
- A következő dián a `mix.exs` fájl végét láthatjuk ismét az új függőséggel.

Links: <https://github.com/bencheeorg/benchee>

## s46 · p130 · Projektszervezés Elixirben 6: mix
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

```
 # Run "mix help deps" to learn about dependencies.
 defp deps do
  [
   {:benchee, "~> 1.0", only: :dev},
   # {:dep_from_hexpm, "~> 0.3.0"},
   # {:dep_from_git, git: "https://github.com/elixir-lang/my_dep.git", tag: ...}
  ]
 end

Telepítsük és fordítsuk le az új modult és függőségeit!4

~/tmp/fp$ mix do deps.get + deps.compile
Resolving Hex dependencies...
Resolution completed in 0.051s
New:
  benchee 1.4.0
  deep_merge 1.0.0
  statistex 1.1.0
...
Compiling ...
```

4Az új modulok az adott projekt részei lesznek, lokálisak, nem globálisak.

## s47 · p131 · Egészlista elemeinek összege: lib/sum.ex
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

Alább látható egy egészlisták összegét kiszámoló függvény három változatban. `sum1` első, `sum2` második klóza illeszkedik az üres listára, `sum3` pedig egy jobbrekurzív segédfüggvényt hív meg. Van-e különbség a hatékonyságukban?

```
defmodule Sum do
  def sum1([]), do: 0
  def sum1([x|xs]), do: x + sum1(xs)

  def sum2([x|xs]), do: x + sum2(xs)
  def sum2([]), do: 0

  def sum3(xs), do: sumi(xs, 0)

  defp sumi([x|xs], sum), do: sumi(xs, sum+x)
  defp sumi([], sum), do: sum
end

# A fájl végére írt kifejezéseket az iex automatikusan ki fogja értékelni
1..1000 |> Range.to_list() |> Sum.sum1() |> IO.inspect()
1..1000 |> Range.to_list() |> Sum.sum2() |> IO.inspect()
1..1000 |> Range.to_list() |> Sum.sum3() |> IO.inspect()
```

## s48 · p132 · Fordítás, futtatás mix-szel: mix compile; iex -S mix
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

- Fordítani a `mix compile`-lal lehet, a `_build/dev/lib/fp/ebin/` mappába kerül a lefordított fájl, pl. a `sum.ex` esetében `Elixir.Sum.beam` néven.
- `iex` indítása a `mix` projekt konfigurációjával és függőségeivel: (lásd `mix help`, `elixir --help`)

```
iex -S mix # Starts IEx and runs the default task
```

- Betölteni, újratölteni egyszerű a programunkat az `r` parancssal (korrektebben: az `r` helper funkcióval):

```
iex> r Sum
```

- A `Sum` modulban definiált függvények meghívása:

```
iex> Sum.sum1 [1,2,3,4,5]
15
```

- A modult záró `end` után lehetnek olyan függvényhívások, melyeket az `iex` betöltéskor kiértékel; az `IO.inspect` ezek eredményét kiírja, pl.

```
1..1000 |> Range.to_list() |> Sum.sum1() |> IO.inspect()
```

Ha újratöltjük a programot az `r` helper függvénnyel, az eredmény megjelenik a képernyőn:

```
iex> r Sum
...
500500
{:reloaded, [Sum]}
```

## s49 · p133 · Mérések, profilozás: benchee
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

- Már láttuk, hogyan kell telepíteni a `benchee` modult.
- Most nézzünk egy példát a használatára, vizsgáljuk meg a `Sum.sum1/1`, `Sum.sum2/1`, `Sum.sum3/1` függvények működését.
- A `Benchee.run/1` függvényt kell meghívni egy fájlban, pl. a `benchee_sum.exs`-ben. Ennek egy szótár a paramétere, amiben a függvényhívásokat kell megadni egy-egy névtelen függvény törzsében:

```
Benchee.run(%{"sum1" => fn -> 1..10_000 |> Enum.to_list() |> Sum.sum1() end,
              ...
              }
           )
```

- Az elemzést a `mix run lib/benchee_sum.exs`-szel indítjuk el.
- Ha azt is szeretnénk tudni, hogy a függvényeink által meghívott függvények milyen gyakran és mennyi ideig futnak, akkor a `profile_after` opciót kell megadnunk, így:

```
Benchee.run(%{"sum1" => fn -> 1..10_000 |> Enum.to_list() |> Sum.sum1() end,
              ...
             },
             profile_after: true
           )
```

## s50 · p134 · Benchmarking eredmények (részletek): sum.ex
<!-- status: viewed pages/p134.png -->
<!-- flags: layout -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

```text
Operating System: Linux
CPU Information: Intel(R) Core(TM) i5-8365U CPU @ 1.60GHz
Number of Available Cores: 8
Available memory: 38.81 GB
Elixir 1.18.4
Erlang 28.0.1
JIT enabled: true

Benchmark suite executing with the following configuration:
warmup: 2 s
time: 5 s
...
Estimated total run time: 21 s
...
Name           ips        average  deviation         median         99th %
sum3       16.26 K       61.50 µs    ±16.25%       63.65 µs       79.93 µs
sum2        8.87 K      112.80 µs    ±18.45%       97.88 µs      175.92 µs
sum1        8.26 K      121.01 µs    ±18.40%      105.16 µs      187.74 µs

Comparison:
sum3       16.26 K (2. klóz illeszkedik az üres listára a jobbrekurzív segédfüggvényben)
sum2        8.87 K - 1.83x slower +51.30 µs (2. klóz illeszkedik az üres listára)
sum1        8.26 K - 1.97x slower +59.52 µs (1. klóz illeszkedik az üres listára)
```

<!-- note: the slide has no text besides this output, which stands in a single bullet point. The three parenthesised remarks after the Comparison lines are red annotations added by the lecturer in a serif font, not part of the Benchee output. -->

## s51 · p135 · Benchmarking eredmények (részletek): sum.ex
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

A `Benchee` modul használatára példát az első előadás segédanyaga tartalmaz: dp26a-fp1ea-sum-benchee.livemd, dp26a-fp1ea-sum-benchee.pdf.

## s52 · p136 · 1. gyakorlat
<!-- status: auto -->
<!-- header: FPE-1 – Projektszervezés és más hasznosságok: mix, benchee -->

- Kedden 10:15 az IB027 és IE007 termekben
- Felkészüléshez ajánlott
  - Erlang, Elixir, Livebook telepítés (a gyakorlaton segítünk, ha valaki elakadt)
  - Elixir felvezető tutorial: <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp1gyfel.livemd>
  - Benchee használat példa: <https://dp.iit.bme.hu/dp26a/ea/dp26a-fp1ea-sum-benchee.livemd>
- Gyakorlat anyaga: <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp1gy.livemd>

Links: <https://dp.iit.bme.hu/dp26a/ea/dp26a-fp1ea-sum-benchee.livemd>, <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp1gy.livemd>, <https://dp.iit.bme.hu/dp26a/gy/dp26a-fp1gyfel.livemd>
