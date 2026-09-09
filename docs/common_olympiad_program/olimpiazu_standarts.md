---
layout: default
lang: lv
title: "Matemātikas olimpiāžu satura standarts (5.-12. klase)"
permalink: /common_olympiad_program/olimpiazu_standarts/
---

# Matemātikas olimpiāžu satura standarts

*Saturs, kas jāapgūst, gatavojoties Latvijas matemātikas olimpiādēm 5.-12. klasē*

## Ievads

Dokuments [Matemātikas olimpiāžu programma (2022)](https://kapsitis.github.io/nms-courses/courses_26_27/common_olympiad_program/) uzskaita tēmas un metodes,
kas tiek izmantotas Latvijas matemātikas olimpiāžu uzdevumos, taču nenorāda, **kurā
vecumposmā** katra tēma ir jāapgūst. Šis dokuments to precizē: tas sadala olimpiāžu
saturu četrās vecumposmu grupās un katrai grupai nosaka sasniedzamos rezultātus.

Saturs ir izvēlēts, analizējot aptuveni $950$ uzdevumus, kas laika posmā no $2016$.
līdz $2026$. gadam piedāvāti trijās Latvijas olimpiādēs:

* **AMO** - atklātā matemātikas olimpiāde (5.-12. klase),
* **NOL** - novadu (2. posma) matemātikas olimpiāde (5.-12. klase),
* **VOL** - valsts (3. posma) matemātikas olimpiāde (9.-12. klase, atsevišķos gados arī 7.-8. klase).

Uzdevumu sadalījums pa matemātikas apakšnozarēm šajā periodā ir samērā līdzsvarots,
tomēr jaunākajās klasēs nedaudz dominē kombinatorika, bet vecākajās - skaitļu teorija un
algebra (sadalījums pēc uzdevuma galvenās apakšnozares):

| Vecumposms | Kombinatorika | Skaitļu teorija | Ģeometrija | Algebra |
|---|---|---|---|---|
| 5.-6. klase | $31\%$ | $28\%$ | $26\%$ | $15\%$ |
| 7.-8. klase | $29\%$ | $25\%$ | $28\%$ | $17\%$ |
| 9.-10. klase | $23\%$ | $30\%$ | $24\%$ | $23\%$ |
| 11.-12. klase | $16\%$ | $31\%$ | $23\%$ | $30\%$ |

Būtiski mainās prasītā atbildes forma. 5.-6. klasē pierādījumu prasa aptuveni trešdaļa
uzdevumu, un pārsvarā tiek prasīts atrast piemēru vai pārbaudīt apgalvojumu; 7.-8. klasē
tā ir jau puse, 9.-10. klasē - gandrīz $60\%$, bet 11.-12. klasē pierādījumu prasa
aptuveni **septiņi uzdevumi no desmit**. Tāpēc pierādīšanas metodes šajā dokumentā ir
izdalītas atsevišķā sadaļā (skat. 5. nodaļu "Vispārīgās metodes un pierādīšana").

## Kā lietot šo dokumentu

### Vecumposmu grupas

Saturs ir sadalīts četrās grupās. **Ieraksts "7.-8. klase" nozīmē, ka attiecīgā tēma ir
jāapgūst 7. vai 8. klasē**, lai skolēns būtu sagatavots savas klases olimpiādēm.
Sadalījums grupās nav sasaistīts ar konkrētu mācību gadu vai stundu skaitu - skolotājs
pats izvēlas, kurā no abām klasēm tēmu mācīt.

Prasības ir **kumulatīvas**: katrā vecumposmā tiek pieņemts, ka visu iepriekšējo
vecumposmu saturs ir apgūts un tiek lietots patstāvīgi.

Grupas apzināti nesakrīt ar pamatskolas/vidusskolas robežu. 9. un 10. klases olimpiāžu
uzdevumu komplekti ir tuvi pēc satura un grūtības (bieži viens un tas pats uzdevums
abām klasēm tiek dots ar nedaudz atšķirīgiem skaitliskiem datiem), tāpēc tie apvienoti
vienā grupā. Tas pats attiecas uz 11. un 12. klasi.

### Apzīmējumi

* **★** - tēma vai prasme, kas attiecīgajā vecumposmā **nav** vispārējās izglītības
  standarta programmā (MK noteikumi Nr. 747 un Nr. 416) vai tajā tiek skarta tikai
  pavisam virspusēji. Tā jāapgūst pulciņā, fakultatīvā vai patstāvīgi.
* **-** - tēma šajā vecumposmā olimpiādēs netiek prasīta.
* Uzdevumu kodi, piemēram, `LV.NOL.2025.8.3`, norāda uz olimpiādi, gadu, klasi un
  uzdevuma numuru. Uzdevumi ar atrisinājumiem pieejami šī projekta uzdevumu arhīvā
  (mapes `docs/LV.AMO`, `docs/LV.NOL` un `docs/LV.VOL`) un
  [pa tēmām sakārtotā uzdevumu pārlūkā](https://www.dudajevagatve.lv/eliozo/curriculum).

### Ko šis dokuments nenosaka

Dokuments **nenosaka tēmu apguves secību**, stundu skaitu un mācību gada plānu. Tēmas
ir grupētas pēc matemātikas apakšnozarēm, un katras apakšnozares ietvaros tās ir
sakārtotas "spirālē": vienas tabulas rindas šūnas apraksta vienu un to pašu tematisko
līniju arvien augstākā sarežģītības pakāpē. Skolotājs var brīvi mainīt secību un
apvienot tēmas.

Tāpat kā olimpiāžu programmā, arī šeit netiek iekļauta varbūtību teorija, statistika,
robežas, atvasinājumi, integrāļi un kompleksie skaitļi.

---

## 1. Algebra

### 1.1. Satura karte

| Tematiskā līnija | 5.-6. klase | 7.-8. klase | 9.-10. klase | 11.-12. klase |
|---|---|---|---|---|
| **A1** Izteiksmes un to pārveidojumi | Skaitliskas izteiksmes, darbību secība, daļas un procenti | Burtu izteiksmes, saīsinātās reizināšanas formulas | Daļveida izteiksmes, kvadrātsaknes, pilnā kvadrāta atdalīšana ★ | Simetriskas izteiksmes, teleskopiskas summas un reizinājumi ★ |
| **A2** Vienādojumi un to sistēmas | Nezināmā atrašana, spriešana no beigām | Lineāri vienādojumi un sistēmas, teksta uzdevumi | Kvadrātvienādojums, Vjeta formulas, sistēmas ar aizvietošanu | Iracionāli un augstākas pakāpes vienādojumi, cikliskas sistēmas ★ |
| **A3** Nevienādības un to pierādīšana | Izteiksmju salīdzināšana, tās neaprēķinot | Novērtējumi, nevienādība $a^2 \geq 0$ ★ | Pilnā kvadrāta metode, $\frac{a}{b}+\frac{b}{a} \geq 2$ ★ | Nevienādība starp vidējiem, Koši nevienādība, pastiprināšana ★ |
| **A4** Funkcijas | Sakarības tabulās un grafikos | Lineāra funkcija un tās grafiks | Kvadrātfunkcija, lielākā un mazākā vērtība | Monotonitāte, trigonometriskās funkcijas, funkcionāli vienādojumi ★ |
| **A5** Virknes | Likumsakarības un periodiskums virknēs ★ | Rekurentas virknes ar darbībām starp cipariem ★ | Aritmētiskā un ģeometriskā progresija, periodiskuma pierādīšana | Rekurences, virknes $x^n+y^n$, virkņu novērtējumi ★ |
| **A6** Polinomi | - | Sadalīšana reizinātājos, kopīgā reizinātāja iznešana | Kvadrāttrinoms, saknes, sadalīšana reizinātājos | Polinoma racionālās saknes, sakņu simetriskās funkcijas ★ |

### 1.2. A1. Izteiksmes un to pārveidojumi

**5.-6. klase.**

* Aprēķina skaitliskas izteiksmes vērtību, ievērojot darbību secību un iekavas; sastāda
  izteiksmi ar dotiem skaitļiem un darbību zīmēm, lai iegūtu doto rezultātu.
* Lieto daļas, procentus un procentu virknes (vairākkārtēju palielinājumu par $p\%$).
* Prot izmantot darbību īpašības aprēķinu vienkāršošanai, piemēram, grupēšanu un
  sadalījuma likumu.

*Piemērs.* Ar skaitļiem $3, 5, 7, 9$ (katru tieši vienu reizi) un trim darbību zīmēm
uzrakstīt izteiksmes ar vērtībām $0, 1, \ldots, 9$ (`LV.AMO.2024.5.3`).
Telegrammu skaits katru gadu pieaug tieši par $10\%$ - cik to bija pēc četriem gadiem
(`LV.AMO.2025.6.5`)?

**7.-8. klase.**

* Pārveido burtu izteiksmes: atver iekavas, ievieto kopīgo reizinātāju pirms iekavām,
  saīsina daļas.
* Brīvi lieto saīsinātās reizināšanas formulas
  $(a \pm b)^2 = a^2 \pm 2ab + b^2$ un $a^2 - b^2 = (a-b)(a+b)$ abos virzienos.
* ★ Saskata izteiksmē atkārtotu fragmentu un apzīmē to ar jaunu mainīgo.

*Piemērs.* Skaitli $2025$ izteikt ar deviņiem vieniniekiem, lietojot aritmētiskās
darbības, kāpināšanu un iekavas (`LV.AMO.2025.8.1`).

**9.-10. klase.**

* Veic darbības ar daļveida izteiksmēm; nosaka izteiksmes definīcijas apgabalu.
* Veic darbības ar kvadrātsaknēm, atbrīvojas no iracionalitātes saucējā.
* ★ Atdala pilno kvadrātu: $x^2 + px + q = \left(x + \frac{p}{2}\right)^2 + q - \frac{p^2}{4}$.
* ★ Izmanto identitāti $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$ un formulu
  $(a+b+c)^2 = a^2+b^2+c^2+2(ab+bc+ca)$.

*Piemērs.* Aprēķināt $\dfrac{20252024^2}{20252023^2 + 20252025^2 - 2}$, apzīmējot
$n = 20252024$ (`LV.NOL.2025.9.1`).
Vai izteiksmi $(2+1)(2^2+1)(2^4+1)\cdots(2^{128}+1)$ var pierakstīt formā $2^a - 2^b$
(`LV.NOL.2026.9.2`)?

**11.-12. klase.**

* ★ Lieto simetriskas izteiksmes un elementārās simetriskās funkcijas $s = x+y$,
  $p = xy$; izsaka ar tām $x^2+y^2$, $x^3+y^3$ un tamlīdzīgas izteiksmes.
* ★ Atpazīst teleskopiskas summas un reizinājumus, kuros vairums locekļu saīsinās.
* ★ Prot strādāt ar cikliskām izteiksmēm no trim un vairāk mainīgajiem, izmantojot
  vispārīguma nezaudēšanu (piemēram, pieņemot $a \geq b \geq c$).

*Piemērs.* Reāliem $a, b > 0$ zināms, ka $2026$ skaitļu
$\frac{a+1}{b+1}, \ldots, \frac{a+2026}{b+2026}$ summa ir $2026$; atrast šo skaitļu
reizinājumu (`LV.VOL.2026.11.1`).

### 1.3. A2. Vienādojumi un to sistēmas

**5.-6. klase.**

* Atrod nezināmo darbības locekli; pārbauda atrisinājumu.
* Lieto paņēmienu "spriežu no beigām", ja procesā secīgi tiek veiktas darbības.
* Pieraksta teksta uzdevuma nosacījumus ar vienādību un atrisina to ar spriešanu.

*Piemērs.* Trīs meitenēm kopā ir $120$ konfektes; katra pēc kārtas iedod pārējām divām
tikpat, cik tām tobrīd ir; beigās visām ir vienādi - cik konfekšu bija sākumā
(`LV.NOL.2026.5.1`)?

**7.-8. klase.**

* Atrisina lineāru vienādojumu un divu lineāru vienādojumu sistēmu ar diviem
  nezināmajiem (aizvietošanas un saskaitīšanas paņēmiens).
* Sastāda vienādojumu vai sistēmu pēc teksta uzdevuma nosacījumiem; izvēlas, ko apzīmēt
  ar mainīgo.
* ★ Prot rīkoties, ja vienādojumu ir mazāk nekā nezināmo, bet nezināmie ir naturāli
  skaitļi: apvieno vienādojumu ar novērtējumu vai dalāmības apsvērumu.

*Piemērs.* Trīs zēniem katram iedeva $n$ eiro; viens nopirka cirkuli, otrs divas
pildspalvas, trešais piecus zīmuļus, un kopā atlika tikpat, cik katram bija sākumā
(`LV.VOL.2026.7.4`).

**9.-10. klase.**

* Atrisina kvadrātvienādojumu; lieto diskriminantu un Vjeta formulas
  $x_1 + x_2 = -\frac{b}{a}$, $x_1 x_2 = \frac{c}{a}$.
* ★ Pēta vienādojumu, to neatrisinot: nosaka sakņu zīmes, sakņu skaitu, sakņu
  veselumu.
* Atrisina nelineāras sistēmas ar aizvietošanu un ar jaunu mainīgo ieviešanu.
* ★ Izmanto sadalīšanu reizinātājos un nulles reizinājuma likumu.

*Piemērs.* Vai eksistē kvadrāttrinoms $ax^2+bx+c$ ar veseliem nepāra koeficientiem,
kuram $\frac{1}{2026}$ ir sakne (`LV.VOL.2026.10.1`)?

**11.-12. klase.**

* ★ Atrisina iracionālus vienādojumus, ievērojot definīcijas apgabalu un pārveidojumu
  ekvivalenci.
* ★ Atrisina simetriskas un cikliskas sistēmas, izmantojot vienādojumu saskaitīšanu,
  atņemšanu un sakārtojuma $x \geq y \geq z$ pieņēmumu.
* ★ Lieto novērtējumus kā vienādojuma risināšanas līdzekli: ja $f(x) \geq A$ un
  $g(x) \leq A$, tad vienādojums $f(x) = g(x)$ ir spēkā tikai vienādības gadījumā.

*Piemērs.* Atrisināt reālos skaitļos vienādojumu
$x\left(5\sqrt{x^2-1} + 7\sqrt{x+1}\right) = -2$ (`LV.AMO.2025.12.1`).
Atrisināt sistēmu $x + \frac{1}{x} = y+z$, $y + \frac{1}{y} = x+z$,
$z + \frac{1}{z} = x+y$ (`LV.VOL.2024.12.1`).

### 1.4. A3. Nevienādības un to pierādīšana

**5.-6. klase.**

* Salīdzina divu izteiksmju vērtības, tās precīzi neaprēķinot (pēc reizinātājiem, pēc
  aptuvenās vērtības, pēc kopīga saskaitāmā).
* ★ Novērtē lielumu no augšas un no apakšas, lai pamatotu, ka kāda vērtība nav
  sasniedzama.

*Piemērs.* Kāda ir mazākā iespējamā sešciparu skaitļa ciparu summa, ja skaitlis dalās
ar $24$ (`LV.AMO.2025.5.3`)?

**7.-8. klase.**

* ★ Zina un lieto pamatnevienādību $a^2 \geq 0$ un no tās izrietošo $a^2+b^2 \geq 2ab$.
* ★ Pierāda nevienādību ar ekvivalentiem pārveidojumiem: pārnes visu uz vienu pusi un
  parāda, ka iegūtā izteiksme ir nenegatīva.
* Lieto trijstūra nevienādību un vienkāršus skaitliskus novērtējumus teksta uzdevumos.

*Piemērs.* $150$ kg ķirbju, katrs ne smagāks par $10$ kg, jāuznes pa daļām, ne vairāk
kā $30$ kg reizē; kāds ir mazākais reižu skaits (`LV.AMO.2025.8.4`)?

**9.-10. klase.**

* ★ Pierāda nevienādības, atdalot pilno kvadrātu, arī vairākiem mainīgajiem.
* ★ Zina nevienādību starp vidējo aritmētisko un vidējo ģeometrisko diviem skaitļiem:
  $\frac{a+b}{2} \geq \sqrt{ab}$, un tās sekas $\frac{a}{b}+\frac{b}{a} \geq 2$.
* ★ Nosaka, kad nevienādība pāriet vienādībā, un izmanto to lielākās vai mazākās
  vērtības atrašanai.

*Piemērs.* Diviem dažādiem naturāliem $a$ un $b$ pierādīt, ka
$\frac{a}{b}+\frac{b}{a} \geq 2 + \frac{1}{ab}$ (`LV.AMO.2025.10.1`).

**11.-12. klase.**

* ★ Lieto nevienādību starp vidējo aritmētisko un vidējo ģeometrisko $n$ skaitļiem, kā
  arī vidējo kvadrātisko un vidējo harmonisko.
* ★ Lieto Koši-Buņakovska nevienādību un nevienādību summēšanu (vairāku "triviālu"
  nevienādību saskaitīšanu).
* ★ Lieto nevienādības pastiprināšanas metodi un homogenizāciju, ja dots papildu
  nosacījums, piemēram, $x+y+z=1$.
* ★ Atrod lielāko vai mazāko konstanti, ar kuru nevienādība ir spēkā visiem
  argumentiem.

*Piemērs.* Pozitīviem $x, y, z$ ar $x+y+z=1$ pierādīt, ka
$\sum \frac{1}{xy - z + 2} \geq \frac{27}{16}$ (`LV.VOL.2025.12.3`).
Atrast lielāko reālo $A$, ar kuru $3x^2+y^2+1 \geq A(x^2+xy+x)$ visiem reāliem
$x, y$ (`LV.VOL.2024.12.5`).

### 1.5. A4. Funkcijas

**5.-6. klase.**

* Nolasa un veido sakarības starp diviem lielumiem tabulā, vārdiski un grafikā.
* Lieto tieši un apgriezti proporcionālus lielumus.

*Piemērs.* Uzdevumi par ceļu, ātrumu un laiku, kuros jāsaskata, kurš lielums nemainās.

**7.-8. klase.**

* Pieraksta un pēta lineāru funkciju $y = kx + b$; nosaka nulles un monotonitāti.
* ★ Izmanto grafiku kā argumentu: no grafiku savstarpējā novietojuma secina par
  vienādojuma sakņu skaitu.

*Piemērs.* Uzdevumi, kuros no lineāras sakarības starp diviem veseliem lielumiem
jāsecina par iespējamām vērtībām.

**9.-10. klase.**

* Pēta kvadrātfunkciju: virsotne, monotonitātes intervāli, lielākā un mazākā vērtība.
* ★ Izmanto funkcijas mazāko vērtību nevienādību pierādīšanai un optimizācijas
  uzdevumos.
* Lieto funkcijas $y = \frac{k}{x}$, $y = x^3$, $y = \sqrt{x}$ un moduļa funkciju.

*Piemērs.* Kāda ir izteiksmes $2x^2 - 8xy + 4x + 9y^2 - 14y + 9$ mazākā vērtība
(`LV.AMO.2023.12.2`)?

**11.-12. klase.**

* ★ Lieto funkcijas monotonitāti vienādojumu un nevienādību risināšanā ("ja funkcija ir
  stingri augoša, tad vienādojumam $f(x)=c$ ir ne vairāk kā viena sakne").
* ★ Lieto trigonometrisko funkciju pamatīpašības un pamatidentitāti
  $\sin^2 \alpha + \cos^2 \alpha = 1$.
* ★ Risina vienkāršus funkcionālus vienādojumus ar aizvietošanu.

*Piemērs.* Trijstūra leņķiem $\alpha < \beta < \gamma$ zināms, ka
$\sin^2 \alpha + \sin^2 \beta = \cos^2 \alpha + \cos^2 \beta$; pierādīt, ka
$\gamma = 90^\circ$ (`LV.VOL.2026.12.1`).
Atrisināt vienādojumu $x^2 - \cos x + 1 = 0$ (`LV.VOL.2022.12.1`).

### 1.6. A5. Virknes

**5.-6. klase.**

* Turpina virkni pēc saskatītas likumsakarības; formulē to vārdiski.
* ★ Saskata virknes periodiskumu un izmanto to, lai noteiktu tālu virknes locekli.

*Piemērs.* Virknes pirmais loceklis ir $41$, katru nākamo iegūst, iepriekšējā skaitļa
ciparu reizinājumam pieskaitot $23$; kāds ir $2024$. loceklis (`LV.NOL.2024.5.4`)?

**7.-8. klase.**

* ★ Pieraksta rekurentu sakarību un aprēķina virknes locekļus.
* ★ Pierāda virknes periodiskumu: parāda, ka atkārtojas viss stāvoklis, no kura virkne
  tiek turpināta.
* Prot pamatot, ka virknes locekļu skaits ar kādu īpašību ir bezgalīgs vai galīgs.

*Piemērs.* Katru nākamo locekli iegūst, iepriekšējam pieskaitot tā lielāko ciparu; vai
eksistē virkne, kurā visi locekļi ir nepāra (`LV.AMO.2025.8.3`)?

**9.-10. klase.**

* Lieto aritmētisko un ģeometrisko progresiju: $n$-tā locekļa un summas formulas.
* ★ Pēta virknes, kas definētas ar rekurenci, kurā piedalās cipari vai atlikumi;
  pierāda periodiskumu, izmantojot to, ka stāvokļu skaits ir galīgs (Dirihlē princips).

*Piemērs.* Bezgalīgā virknē $1, 2, 3, 6, 1, \ldots$ katrs loceklis, sākot ar ceturto,
ir iepriekšējo trīs summas kvadrāta pēdējais cipars; atrast $2025$. locekli
(`LV.AMO.2025.9.4`).

**11.-12. klase.**

* ★ Sastāda un lieto lineāras rekurences skaitīšanas uzdevumos.
* ★ Lieto virkni $t_n = x^n + y^n$ un tās rekurenci $t_{n+1} = (x+y)t_n - xy\, t_{n-1}$.
* ★ Novērtē virknes locekļus un pierāda apgalvojumus par bezgalīgām virknēm.

*Piemērs.* Reāliem $x, y$ zināms, ka $x+y=1$ un $x^2+y^2=3$; pierādīt, ka $x^{11}+y^{11}$
ir vesels skaitlis, un atrast to (`LV.VOL.2023.11.1`).
Cik ir tādu sešciparu skaitļu no cipariem $1, 2, 3, 4$, kuros nekur blakus nav divi
cipari $4$ (`LV.AMO.2025.12.2`)?

### 1.7. A6. Polinomi

**5.-6. klase.** -

**7.-8. klase.**

* Sadala izteiksmi reizinātājos, iznesot kopīgo reizinātāju un lietojot saīsinātās
  reizināšanas formulas.
* Veic darbības ar monomiem un polinomiem.

*Piemērs.* Uzdevumi, kuros reizinājuma sadalījums palīdz pierādīt dalāmību.

**9.-10. klase.**

* Sadala kvadrāttrinomu reizinātājos: $ax^2+bx+c = a(x-x_1)(x-x_2)$.
* ★ Lieto Vjeta formulas, lai spriestu par saknēm bez to aprēķināšanas.
* ★ Zina, ka polinoma pakāpes $n$ vienādojumam ir ne vairāk kā $n$ saknes.

*Piemērs.* Skolēni pa vienam maina kvadrātvienādojuma $x^2+10x+20=0$ koeficientu vai
brīvo locekli par $1$; ko var apgalvot par gala rezultāta saknēm (`LV.VOL.2026.9.4`)?

**11.-12. klase.**

* ★ Lieto Vjeta formulas trešās pakāpes vienādojumam.
* ★ Lieto teorēmu par polinoma racionālajām saknēm un Bezū teorēmu (atlikums, dalot ar
  $x-a$, ir $P(a)$).
* ★ Pēta polinomus ar veseliem koeficientiem: ja $a - b$ dala $P(a) - P(b)$, tad no tā
  izriet dalāmības ierobežojumi.

*Piemērs.* Vienādojuma $x^3 - 54x^2 + 865x - 3480 = 0$ saknes ir trijstūra malu garumi;
aprēķināt trijstūra laukumu (`LV.VOL.2022.11.4`).
Uz tāfeles ir polinomi $P(x)=x^2+2$ un $Q(x)=x+1$; kādus polinomus var iegūt, veicot ar
tiem saskaitīšanu, atņemšanu un reizināšanu (`LV.VOL.2025.12.5`)?

---

## 2. Ģeometrija

### 2.1. Satura karte

| Tematiskā līnija | 5.-6. klase | 7.-8. klase | 9.-10. klase | 11.-12. klase |
|---|---|---|---|---|
| **Ģ1** Pamatjēdzieni un leņķi | Punkts, nogrieznis, taisne, taišņu krustpunkti | Paralēlas taisnes, leņķu ķēdes, trijstūra leņķu summa | Leņķu ķēdes ar riņķa līniju, ārējais leņķis | Sarežģītas leņķu konfigurācijas, leņķu ķēžu vairāki gadījumi ★ |
| **Ģ2** Trijstūri | Trijstūru veidi, perimetrs | Vienādības pazīmes, vienādsānu trijstūris, ievilktās līnijas, trijstūra nevienādība | Līdzība, Pitagora teorēma, augstumu krustpunkts | Sinusu un kosinusu teorēma, laukuma formulas, nogriežņu attiecības ★ |
| **Ģ3** Četrstūri un daudzstūri | Taisnstūris, kvadrāts, figūru skaitīšana | Paralelograms un tā pazīmes, trapece | Trapeces diagonāles, ievilkti un apvilkti četrstūri | Izliekti daudzstūri, regulāru daudzstūru diagonāles ★ |
| **Ģ4** Riņķa līnija | Riņķa līnija kā vienādi attālu punktu kopa | Horda, pieskare, centra leņķis | Ievilktais leņķis, ievilkts četrstūris, pieskares un hordas leņķis | Punkta pakāpe, divu riņķa līniju konfigurācijas ★ |
| **Ģ5** Laukumi | Laukums, skaitot rūtiņas; laukuma saglabāšanās | Trijstūra un paralelograma laukums, vienāda laukuma dalījumi | Laukumu attiecības, kopīgs augstums | Laukumu metode vienādību un nevienādību pierādīšanai ★ |
| **Ģ6** Transformācijas un simetrija | Ass simetrija, pagrieziens par $90^\circ$ un $180^\circ$ | Centrālā simetrija, paralēlā pārnese, pagrieziena lietojums pierādījumā ★ | Simetrija īsākā ceļa uzdevumos, homotētija ★ | Homotētija, vektori, palīgkonstrukciju izvēle ★ |
| **Ģ7** Ģeometrija rūtiņu lapā | Figūru sagriešana un salikšana, noklāšana | Noklāšanas iespējamība, krāsošanas arguments ★ | Kvadrāta sagriešana kvadrātos, režģa punkti ★ | Sagriešanas optimums, kombinatoriska ģeometrija ★ |

### 2.2. Ģ1. Pamatjēdzieni un leņķi

**5.-6. klase.**

* Lieto jēdzienus punkts, nogrieznis, stars, taisne, lauzta līnija, leņķis.
* Nosaka, cik krustpunktu var būt vairākām taisnēm plaknē; konstruē piemērus ar dotu
  krustpunktu skaitu.
* Mēra un konstruē leņķus; zina blakusleņķu un krustleņķu īpašības.

*Piemērs.* Vai var novietot plaknē $5$ taisnes tā, lai katras divas krustotos un kopā
būtu tieši $6$ krustpunkti (`LV.AMO.2019.5.3`)?
Vai var uzzīmēt slēgtu lauztu līniju no $7$ posmiem, kas katru savu posmu krusto tieši
vienu reizi (`LV.NOL.2024.6.5`)?

**7.-8. klase.**

* Zina un lieto trijstūra iekšējo leņķu summu $180^\circ$ un ārējā leņķa teorēmu.
* Lieto leņķus pie paralēlām taisnēm (iekšējie šķērsleņķi, atbilstošie leņķi).
* ★ Prot veidot leņķu ķēdi: pakāpeniski izsaka nezināmus leņķus caur vienu apzīmējumu
  $x$ un iegūst vienādojumu.

*Piemērs.* Uz trijstūra malām atzīmēti punkti $M$ un $N$ tā, ka
$\angle BNC = 4x$, $\angle BCN = 6x$, $\angle BMC = \angle CBM = 5x$; pierādīt, ka
trijstūris ir taisnleņķa (`LV.NOL.2025.7.3`).

**9.-10. klase.**

* Apvieno leņķu ķēdes ar riņķa līnijas īpašībām un ar vienādsānu trijstūriem.
* ★ Prot pamatot, kāpēc iegūtais leņķu sadalījums ir vienīgais iespējamais, un aplūkot
  punktu izvietojuma gadījumus.

*Piemērs.* Vienādsānu trijstūrī $AB=AC$, $\angle BAC = 80^\circ$, uz $AC$ atlikts
punkts $E$ ar $\angle EBC = 30^\circ$ (`LV.VOL.2025.10.2`).

**11.-12. klase.**

* ★ Strādā ar konfigurācijām, kurās leņķu vienādība jāpierāda, apejot vairākas
  starpfigūras; izvēlas pareizo pierādījuma virzienu.
* ★ Apzinās, ka zīmējums var neatbilst visiem gadījumiem, un pamato apgalvojumu
  neatkarīgi no zīmējuma.

*Piemērs.* Riņķa līnijā ievilktam četrstūrim $ABCD$ punkti $K$ un $L$ izvēlēti tā, ka
$\angle KAD = \angle KBC$ un $\angle LDA = \angle LCB$; pierādīt, ka $EK = EL$
(`LV.VOL.2026.11.3`).

### 2.3. Ģ2. Trijstūri

**5.-6. klase.**

* Atšķir trijstūru veidus pēc malām un pēc leņķiem; aprēķina perimetru.
* Saskata trijstūrus saliktos zīmējumos un tos saskaita.

*Piemērs.* $3 \times 3$ punktu režģī $5$ punkti nokrāsoti sarkani; cik trijstūrus ar
sarkanām virsotnēm var uzzīmēt (`LV.NOL.2026.7.4`)?

**7.-8. klase.**

* Lieto trijstūru vienādības pazīmes (mlm, lml, mmm) un vienādsānu trijstūra īpašības
  un pazīmes.
* Lieto mediānu, bisektrisi, augstumu un vidusperpendikulu; zina vidusperpendikula un
  bisektrises punktu raksturojumu.
* Lieto trijstūra nevienādību un sakarību starp malām un pretējiem leņķiem.
* ★ Prot novilkt palīglīniju: pagarināt mediānu, atlikt vienādu nogriezni, novilkt
  paralēli.

*Piemērs.* Uz vienādsānu trijstūra sānu malām izvēlēti $M$ un $K$ tā, ka $AK \perp MC$
un $AM = AK = AC$; aprēķināt trijstūra leņķus (`LV.AMO.2025.8.2`).
Trijstūrī ar $\angle A = 120^\circ$ uz bisektrises atlikts $D$ ar $AD = AB + AC$;
pierādīt, ka $BDC$ ir vienādmalu (`LV.NOL.2026.9.5`).

**9.-10. klase.**

* Lieto trijstūru līdzības pazīmes un līdzīgu trijstūru malu attiecības; lieto
  proporcionālu nogriežņu (Talesa) teorēmu.
* Lieto Pitagora teorēmu un metriskās sakarības taisnleņķa trijstūrī; lieto šaura leņķa
  trigonometriskās attiecības.
* ★ Lieto augstumu krustpunktu (ortocentru) un ar to saistītās vienādības; zina
  viduslīnijas īpašību.

*Piemērs.* Šaurleņķu trijstūrī novilkti augstumi $AK$ un $BL$, turklāt $BK = KL$;
pierādīt, ka trijstūris ir vienādsānu (`LV.NOL.2025.9.3`).
Šaurleņķu trijstūrī visi augstumi krustojas punktā $M$; aprēķināt $\angle ACB$, ja
$AB = CM$ (`LV.NOL.2025.8.3`).

**11.-12. klase.**

* ★ Lieto sinusu un kosinusu teorēmu, arī apvilktās riņķa līnijas rādiusa atrašanai.
* ★ Lieto trijstūra laukuma formulas $S = \frac{1}{2}ab\sin\gamma$, $S = pr$,
  $S = \frac{abc}{4R}$ un Herona formulu.
* ★ Aprēķina un salīdzina nogriežņu attiecības uz trijstūra malām, lietojot laukumu
  attiecības vai līdzību.

*Piemērs.* Trijstūra malu garumiem $a, b, c$ pierādīt, ka
$a+b+c > \sqrt{2(a^2+b^2+c^2)}$ (`LV.AMO.2024.12.1`).
Trijstūrī novilkts augstums $BD$ un mediāna $BE$, $\angle ABE = \angle CBD = 23^\circ$;
aprēķināt $\angle DBE$ (`LV.AMO.2025.12.3`).

### 2.4. Ģ3. Četrstūri un daudzstūri

**5.-6. klase.**

* Lieto taisnstūra un kvadrāta īpašības; aprēķina perimetru un laukumu.
* Saskaita figūras ar dotām īpašībām (piemēram, taisnstūrus ar doto perimetru).

*Piemērs.* Kādu taisnstūru ar veseliem malu garumiem ir vairāk - ar perimetru $2024$ vai
ar perimetru $2026$ (`LV.NOL.2026.6.5`)?

**7.-8. klase.**

* Lieto paralelograma, romba, taisnstūra un kvadrāta īpašības un pazīmes.
* Lieto trapeces īpašības un viduslīniju.
* Zina izliekta $n$-stūra iekšējo leņķu summu $(n-2) \cdot 180^\circ$.

*Piemērs.* Izliektā četrstūrī $ABCD$ ir $AB = DC$ un $AC = DB$; pierādīt, ka diagonāļu
krustpunktam $O$ ir spēkā $AO = DO$ (`LV.NOL.2026.8.1`).

**9.-10. klase.**

* Lieto trapeces diagonāļu īpašības un tās veidoto trijstūru laukumu attiecības.
* ★ Zina ievilkta četrstūra pazīmi (pretējo leņķu summa $180^\circ$) un apvilkta
  četrstūra pazīmi ($AB + CD = BC + AD$).

*Piemērs.* Izliektā četrstūrī $\angle CBD = 2\angle CAD$ un $\angle CDB = 2\angle CAB$;
pierādīt, ka $CA$ ir leņķa $BCD$ bisektrise (`LV.NOL.2026.10.4`).

**11.-12. klase.**

* ★ Pierāda četrstūra veidu no metriskiem nosacījumiem (piemēram, no perimetru
  vienādības).
* ★ Strādā ar regulāru daudzstūru diagonālēm un simetrijām.

*Piemērs.* Izliekta četrstūra diagonāles sadala to četros vienāda perimetra trijstūros;
pamatot, ka četrstūris ir rombs (`LV.AMO.2024.11.4`).
Izliektā piecstūrī četras diagonāles ir paralēlas kādai malai; pierādīt, ka arī piektā
ir (`LV.NOL.2025.12.3`).

### 2.5. Ģ4. Riņķa līnija

**5.-6. klase.**

* Lieto riņķa līniju kā punktu kopu, kas atrodas vienādā attālumā no centra; konstruē ar
  cirkuli.
* Risina uzdevumus par attālumiem, izmantojot riņķa līniju krustpunktus.

*Piemērs.* Dārzā aug $4$ bumbieres; no katras ābeles tieši $10$ m attālumā aug tieši
divas bumbieres - kāds ir lielākais ābeļu skaits (`LV.VOL.2026.8.3`)?

**7.-8. klase.**

* Lieto jēdzienus horda, diametrs, pieskare, sekante, loks, sektors, segments.
* Zina, ka pieskare ir perpendikulāra rādiusam pieskaršanās punktā, un ka vienādas
  hordas atbilst vienādiem lokiem.

*Piemērs.* Uzdevumi, kuros no vienādiem rādiusiem izriet vienādsānu trijstūri.

**9.-10. klase.**

* ★ Lieto ievilktā leņķa teorēmu un tās sekas: leņķi, kas balstās uz vienu loku, ir
  vienādi; leņķis, kas balstās uz diametru, ir taisns.
* ★ Pierāda, ka četri punkti atrodas uz vienas riņķa līnijas.
* ★ Lieto pieskares un hordas leņķi; lieto apvilkto un ievilkto riņķa līniju centrus.

*Piemērs.* Uz trijstūra malas $BC$ izvēlēts $D$; $I_1$ un $I_2$ ir trijstūros $ABD$ un
$ACD$ ievilkto riņķa līniju centri (`LV.VOL.2023.12.2`).

**11.-12. klase.**

* ★ Lieto punkta pakāpi attiecībā pret riņķa līniju un krustojošos hordu īpašību
  $AP \cdot PB = CP \cdot PD$.
* ★ Strādā ar divām riņķa līnijām: to otro krustpunktu, pieskaršanos, kopīgo hordu.
* ★ Lieto apvilktās riņķa līnijas centru un tā īpašības sarežģītās konfigurācijās.

*Piemērs.* Trijstūru $ABC$ un $BHT$ apvilktās riņķa līnijas vēlreiz krustojas punktā
$X$; pierādīt, ka $\angle TXA = \angle BAC$ (`LV.NOL.2026.11.3`).
Riņķa līnijā ievilktam četrstūrim $AB + CD = AD$; pierādīt, ka leņķu $ABC$ un $BCD$
bisektrišu krustpunkts atrodas uz malas $AD$ (`LV.VOL.2025.12.2`).

### 2.6. Ģ5. Laukumi

**5.-6. klase.**

* Aprēķina figūras laukumu, skaitot rūtiņas un papildinot līdz taisnstūrim.
* ★ Lieto laukuma saglabāšanos, sagriežot un pārliekot figūru.

*Piemērs.* Sagriezt doto figūru divās vienādās daļās pa rūtiņu līnijām
(`LV.AMO.2024.6.4`).

**7.-8. klase.**

* Aprēķina trijstūra, paralelograma un trapeces laukumu.
* ★ Lieto to, ka trijstūriem ar vienādu pamatu un vienādu augstumu ir vienādi laukumi;
  mediāna sadala trijstūri divās vienāda laukuma daļās.

*Piemērs.* Uzdevumi par figūras sadalīšanu vienāda laukuma daļās.

**9.-10. klase.**

* ★ Lieto laukumu attiecības: trijstūriem ar kopīgu augstumu laukumi attiecas kā pamati;
  līdzīgām figūrām laukumi attiecas kā līdzības koeficienta kvadrāts.
* ★ Izsaka meklēto laukumu caur zināmiem laukumiem, sadalot figūru daļās.

*Piemērs.* Trijstūrī $ED \parallel BC$, nogriežņi $EB$ un $CD$ krustojas punktā $F$;
zinot $S(BFD)$ un $S(EFD)$, aprēķināt $S(ABC)$ (`LV.NOL.2026.11.1`).
Trapecē ar diagonāļu krustpunktu $E$ pierādīt, ka
$S_{ABE} \cdot S_{ABCD} = S_{ABC}^2$ (`LV.NOL.2022.11.3`).

**11.-12. klase.**

* ★ Lieto laukumu metodi vienādību un nevienādību pierādīšanai, arī apvienojumā ar
  trigonometrisko laukuma formulu.
* ★ Lieto laukumu attiecības nogriežņu attiecību atrašanai un otrādi.

*Piemērs.* Taisnstūra $ABCD$ diagonāle $BD$ ir kvadrāta $BDEF$ mala, un $C$ atrodas
kvadrāta iekšpusē; pierādīt, ka $S_{ABD} \leq S_{CEF}$ (`LV.AMO.2023.12.3`).

### 2.7. Ģ6. Transformācijas un simetrija

**5.-6. klase.**

* Atpazīst un konstruē figūras ass simetriju; lieto pagriezienu par $90^\circ$ un
  $180^\circ$, lai pamatotu figūru vienādību.
* Nosaka, vai divas figūras ir vienādas, tās pagriežot vai apmetot otrādi.

*Piemērs.* Sagriezt $3 \times 3$ kvadrātu trīs dažādos gabalos tā, lai katri divi kopā
veidotu simetrisku figūru (`LV.AMO.2025.7.2`).

**7.-8. klase.**

* ★ Lieto centrālo simetriju, paralēlo pārnesi un pagriezienu kā pierādījuma līdzekli:
  attēlo figūras daļu un iegūst jaunu, izdevīgāku konfigurāciju.

*Piemērs.* Uzdevumi, kuros trijstūra mediānu pagarina divkārt (pagrieziens par
$180^\circ$ ap mediānas galapunktu).

**9.-10. klase.**

* ★ Lieto simetriju īsākā ceļa un ekstremālos uzdevumos (atstarošanas princips).
* ★ Lieto homotētiju vienkāršās situācijās (viduslīnijas, līdzīgu figūru centri).

*Piemērs.* Uz trijstūra malām un uz staru pagarinājumiem atlikti punkti attiecībā
$1:2$; pierādīt, ka iegūtais četrstūris $ABKL$ ir paralelograms (`LV.NOL.2025.10.3`).

**11.-12. klase.**

* ★ Lieto homotētiju un vektorus, tostarp vektoru vienādības pierādīšanai.
* ★ Izvēlas palīgkonstrukciju (papildu punktu, riņķa līniju vai paralēlu taisni), kas
  konfigurāciju padara simetrisku.

*Piemērs.* Punkts $P$ atrodas paralelograma $ABCD$ iekšpusē; pierādīt, ka
$\overrightarrow{PA} + \overrightarrow{PC} = \overrightarrow{PB} + \overrightarrow{PD}$
(`LV.NOL.2022.11.1`).

### 2.8. Ģ7. Ģeometrija rūtiņu lapā

**5.-6. klase.**

* Sagriež figūru vienādās daļās pa rūtiņu līnijām; parāda vairākus dažādus veidus.
* Noskaidro, vai doto figūru komplektu var ievietot dotā taisnstūrī.

*Piemērs.* Parādīt, kā $5 \times 7$ rūtiņu taisnstūri sagriezt vienā $1 \times 3$
taisnstūrī un astoņās "T" formas figūrās (`LV.AMO.2025.5.4`).

**7.-8. klase.**

* ★ Pamato, ka noklāšana **nav** iespējama, izmantojot rūtiņu krāsošanu vai skaita un
  paritātes apsvērumus.
* Nosaka lielāko figūru skaitu, ko var izgriezt no dotās figūras.

*Piemērs.* Vai doto figūru var noklāt ar dotajām figūrām, ja dalījuma līnijas iet tikai
pa rūtiņu līnijām (`LV.NOL.2026.7.2`)?

**9.-10. klase.**

* ★ Risina uzdevumus par kvadrāta sagriešanu mazākos kvadrātos ar ierobežojumiem.
* ★ Lieto režģa punktu koordinātas un to paritāti.

*Piemērs.* Vai eksistē pirmskaitlis $p$, kuram $p \times p$ kvadrātu var sagriezt
kvadrātos, kam malas garums ir vismaz $2$ (`LV.AMO.2025.9.3`)?
No $5 \times 5$ kvadrāta izgrieztas sešas figūras - $1 \times 4$ taisnstūri vai
$2 \times 2$ kvadrāti; kura rūtiņa var palikt pāri (`LV.VOL.2025.10.4`)?

**11.-12. klase.**

* ★ Nosaka optimālu sagriešanu vai izvietojumu un pierāda tā optimalitāti.
* ★ Apvieno ģeometriskus un kombinatoriskus apsvērumus vienā risinājumā.

*Piemērs.* $2026 \times 2026$ tabulā atzīmētas $2026$ rūtiņas, katrā rindā un kolonnā
tieši viena; kāds ir lielākais tukšais taisnstūris (`LV.NOL.2026.11.4`)?
$9 \times 9$ kvadrāts sadalīts deviņos deviņu rūtiņu daudzstūros; pierādīt, ka visi ir
$3 \times 3$ kvadrāti (`LV.VOL.2022.12.5`).

---

## 3. Kombinatorika

### 3.1. Satura karte

| Tematiskā līnija | 5.-6. klase | 7.-8. klase | 9.-10. klase | 11.-12. klase |
|---|---|---|---|---|
| **K1** Objektu skaitīšana | Sistemātiska uzskaitīšana, saskaitīšanas likums | Reizināšanas likums, dubultā skaitīšana ★ | Permutācijas, kombinācijas, papildinājuma skaitīšana | Binomiālie koeficienti, rekurentā skaitīšana, ieslēgumu un izslēgumu formula ★ |
| **K2** Dirihlē princips | Pamatformulējums ar krāsām un grupām ★ | Vispārinātais princips, atlikumu grupas ★ | Dirihlē princips skaitļu teorijā un ģeometrijā ★ | Pašu konstruētas "kastes", vidējošanas princips ★ |
| **K3** Invarianti un monovarianti | Paritātes invariants, krāsošana ★ | Skaitlisks invariants, summa pēc moduļa ★ | Monovariants, procesu beigu stāvokļi ★ | Invarianti spēlēs un algebriskos procesos ★ |
| **K4** Grafi | Zīmējums ar punktiem un līnijām, virsotņu pakāpe ★ | Rokasspiedienu lemma, pilns grafs ★ | Sakarīgums, koki, cikli, grafa krāsošana ★ | Ekstremāli grafu uzdevumi, Ramseja tipa apgalvojumi ★ |
| **K5** Matemātiskās spēles | Simetrijas stratēģija ★ | Uzvarošas un zaudējošas pozīcijas ★ | Pozīciju analīze ar atlikumiem, spēles ar invariantu ★ | Spēles ar sarežģītu stāvokļu telpu, stratēģijas nozagšana ★ |
| **K6** Algoritmi, svēršanas un informācija | Svēršanas uzdevumi ar diviem soļiem ★ | Meklēšanas un kārtošanas uzdevumi, turnīri ★ | Informācijas apjoma novērtējums ★ | Algoritma optimalitātes pierādījums ★ |
| **K7** Loģikas uzdevumi | Patiesie un melīgie apgalvojumi | Apgalvojumu sistēmas, implikācijas | Apgalvojumi ar kvantoriem, pilnā pārlase pa gadījumiem | Uzdevumi par zināšanu un informācijas sadalījumu ★ |

### 3.2. K1. Objektu skaitīšana

**5.-6. klase.**

* Uzskaita visus variantus sistemātiski (pēc kārtas, koka diagrammā, tabulā) un pamato,
  ka citu nav.
* Lieto saskaitīšanas likumu, sadalot iespējas nekrustojošos gadījumos.
* Lieto Eilera-Venna diagrammas, ja objektiem ir divas pazīmes.

*Piemērs.* Kādus deviņciparu skaitļus ar dažādiem cipariem var izveidot, ja katri divi
blakus cipari veido skaitli, kas dalās ar $7$ vai $13$ (`LV.NOL.2026.5.3`)?

**7.-8. klase.**

* Lieto reizināšanas likumu neatkarīgām izvēlēm.
* ★ Lieto dubulto skaitīšanu: vienu un to pašu lielumu saskaita divos veidos un
  pielīdzina.

*Piemērs.* $30$ bērni sastājās aplī; $20$ bērni turēja aiz rokas vismaz vienu
pirmklasnieku, $24$ - vismaz vienu otrklasnieku (`LV.NOL.2025.7.4`).

**9.-10. klase.**

* Lieto permutācijas, variācijas un kombinācijas; atšķir sakārtotas un nesakārtotas
  izlases.
* ★ Skaita papildinājumu, ja tiešā skaitīšana ir sarežģītāka.
* ★ Sastāda rekurenci vienkāršos skaitīšanas uzdevumos.

*Piemērs.* Sienāzis lec pa skaitļu taisni $2$ vai $3$ vienības pa labi un nedrīkst
nonākt pirmskaitļos; cik veidos tas no $1$ nokļūst uz $36$ (`LV.VOL.2026.8.5`)?

**11.-12. klase.**

* ★ Lieto binomiālos koeficientus un Ņūtona binomu; zina Paskāla trijstūra īpašības.
* ★ Lieto ieslēgumu un izslēgumu formulu.
* ★ Skaita ar bijekciju: pierāda, ka divu kopu elementu skaits sakrīt, uzrādot atbilstību.

*Piemērs.* Cik dažādos veidos skaitli $12$ var izteikt kā vieninieku, divnieku un
četrinieku summu, ja saskaitāmo secība ir svarīga (`LV.AMO.2025.11.4`)?

### 3.3. K2. Dirihlē princips

**5.-6. klase.**

* ★ Formulē un lieto Dirihlē principu: ja $n$ objekti izvietoti $k < n$ grupās, tad kādā
  grupā ir vismaz divi objekti.
* ★ Nosaka mazāko izvēļu skaitu, kas **garantē** vēlamo rezultātu, un uzrāda piemēru, kas
  parāda, ka ar mazāku skaitu nepietiek.

*Piemērs.* Kastē ir $7$ zaļas, $3$ sarkanas, $11$ melnas un $9$ baltas bumbiņas; kāds ir
mazākais izvelkamo bumbiņu skaits, lai garantēti būtu divas vienādas krāsas
(`LV.AMO.2024.5.2`)?

**7.-8. klase.**

* ★ Lieto vispārināto Dirihlē principu: ja $n$ objekti ir $k$ grupās, tad kādā grupā ir
  vismaz $\left\lceil \frac{n}{k} \right\rceil$ objekti.
* ★ Izmanto atlikumus kā "kastes": $n+1$ skaitļu vidū ir divi ar vienādu atlikumu, dalot
  ar $n$.

*Piemērs.* Piecās kastēs kopā ir $21$ bumbiņa, un jebkurās divās kastēs bumbiņu skaits
ir atšķirīgs (`LV.NOL.2026.7.3`).

**9.-10. klase.**

* ★ Lieto Dirihlē principu virkņu periodiskuma pierādīšanai (galīgs stāvokļu skaits).
* ★ Lieto Dirihlē principu ģeometrijā (punkti apgabalā) un skaitļu teorijā (atlikumi).

*Piemērs.* Bezgalīgā virknē katru nākamo skaitli iegūst, pieskaitot $54$ vai $77$;
pierādīt, ka virknē ir skaitlis ar diviem vienādiem pēdējiem cipariem
(`LV.VOL.2025.9.3`).

**11.-12. klase.**

* ★ Pats konstruē "kastes", kas nav dotas uzdevuma formulējumā.
* ★ Lieto vidējošanas principu: ja vidējā vērtība ir $A$, tad kāds elements ir vismaz
  $A$ un kāds - ne lielāks par $A$.

*Piemērs.* Katrs no $7$ dalībniekiem zina dažus himnas pantiņus, un jebkuri $3$ kopā
zina visu himnu; vai noteikti ir divi, kas zina visu (`LV.AMO.2025.11.5`)?
Doti $104$ reāli skaitļi ar ciklisku nosacījumu; pierādīt, ka vismaz $52$ no tiem ir
vienādi (`LV.VOL.2026.12.2`).

### 3.4. K3. Invarianti un monovarianti

**5.-6. klase.**

* ★ Saskata lielumu, kas procesa gaitā nemainās (visbiežāk - paritāti vai summu).
* ★ Lieto krāsošanu, lai parādītu, ka kāds stāvoklis nav sasniedzams.

*Piemērs.* Automāts par diviem vienādiem žetoniem izsniedz zaļu, par diviem dažādiem -
dzeltenu; kādi žetonu komplekti var palikt (`LV.NOL.2024.5.5`)?
$3 \times 3$ tabulā katrā gājienā $2 \times 2$ kvadrātam pieskaita $1$; vai tieši $8$ no
skaitļiem var būt pirmskaitļi (`LV.AMO.2025.5.5`)?

**7.-8. klase.**

* ★ Lieto skaitlisku invariantu: summu, reizinājumu vai atlikumu pēc kāda moduļa.
* ★ Formulē invariantu precīzi un pamato, ka gājiens to nemaina.

*Piemērs.* Uzdevumi, kuros gājiens maina divus skaitļus, bet saglabā to summas atlikumu.

**9.-10. klase.**

* ★ Lieto monovariantu (pusinvariantu): lielumu, kas visu laiku tikai aug vai tikai
  samazinās, lai pierādītu, ka process beidzas.
* ★ Apraksta procesa iespējamos beigu stāvokļus.

*Piemērs.* Uz tāfeles ir $2025$ dažādi naturāli skaitļi; katrā gājienā divus no tiem
aizstāj ar to LKD un MKD (`LV.AMO.2025.10.4`).

**11.-12. klase.**

* ★ Konstruē invariantu spēlēm un algebriskiem procesiem, tostarp ar polinomiem.
* ★ Apvieno invariantu ar konstruktīvu piemēru, lai pierādītu precīzu robežu.

*Piemērs.* Sākumā uz tāfeles ir divi vieninieki; gājienā skaitli var divkāršot vai
lielāko aizstāt ar starpību (`LV.VOL.2025.11.5`).
Rūķīši pie apaļa galda atdod pusi konfekšu kaimiņam, un feja pieliek vienu, ja atlicis
nepāra skaits (`LV.NOL.2025.12.4`).

### 3.5. K4. Grafi

**5.-6. klase.**

* ★ Attēlo situāciju ar punktiem un tos savienojošām līnijām; saskaita līnijas.
* ★ Lieto virsotnes pakāpi vienkāršos gadījumos.

*Piemērs.* Uzdevumi par pazīšanos un rokasspiedieniem nelielā cilvēku grupā.

**7.-8. klase.**

* ★ Zina un lieto rokasspiedienu lemmu: visu virsotņu pakāpju summa ir vienāda ar
  divkāršotu šķautņu skaitu, tātad nepāra pakāpes virsotņu skaits ir pārskaitlis.
* ★ Strādā ar pilnu grafu un ar grafu, kura šķautnes ir divās krāsās.

*Piemērs.* Ciemā katras divas pļāpas sarunājās tieši vienu reizi; pierādīt, ka atradīsies
trīs ar noteiktu īpašību (`LV.VOL.2026.7.3`).

**9.-10. klase.**

* ★ Lieto sakarīguma jēdzienu, komponentes, ciklus un kokus; zina, ka kokam ar $n$
  virsotnēm ir $n-1$ šķautnes.
* ★ Lieto grafu virsotņu krāsošanu.

*Piemērs.* Kāds ir mazākais ceļu skaits starp $100$ pilsētām, pie kura grafs noteikti ir
sakarīgs (`LV.VOL.2023.12.5`)?
Elza uzzīmēja $99$ pilsētas un $N$ ceļus, pēc tam ar Ramonu pamīšus dzēš ceļus
(`LV.NOL.2026.9.3`).

**11.-12. klase.**

* ★ Risina ekstremālus grafu uzdevumus: atrod lielāko vai mazāko šķautņu skaitu ar dotu
  īpašību.
* ★ Zina Ramseja tipa apgalvojumu: sešu cilvēku vidū vienmēr ir trīs savstarpēji
  pazīstami vai trīs savstarpēji nepazīstami.

*Piemērs.* Vai noteikti var atrast trīs rūķus, kas visi savā starpā draudzējas, ja zemē
ir (A) $5$, (B) $6$ rūķi (`LV.NOL.2023.11.2`)?
Datorklasē daži datori ir savienoti; pierādīt, ka vienmēr ir divi datori, kas saņēmuši
vienādu ziņojumu skaitu (`LV.VOL.2024.11.3`).

### 3.6. K5. Matemātiskās spēles

**5.-6. klase.**

* ★ Lieto simetrijas stratēģiju: atkārto pretinieka gājienu simetriski.
* ★ Pamato, kurš spēlētājs uzvar, un apraksta uzvaras stratēģiju pilnībā, nevis tikai
  pirmo gājienu.

*Piemērs.* Divās vāzēs ir $46$ un $43$ tulpes; gājienā no vienas vāzes izņem $1$ vai $3$
tulpes (`LV.AMO.2019.5.2`).

**7.-8. klase.**

* ★ Nosaka uzvarošās un zaudējošās pozīcijas, ejot no spēles beigām uz sākumu.
* ★ Saskata pozīciju periodiskumu (piemēram, pēc atlikuma, dalot ar $k+1$).

*Piemērs.* Alise un Kate pamīšus pieskaita skaitli no $1$ līdz $10$; kurš uzvar
(`LV.NOL.2025.5.4`, `LV.NOL.2025.8.4`)?
Rindā ir $12$ glāzes; gājienā izdzer vienu vai divas blakusesošas (`LV.AMO.2025.7.4`).

**9.-10. klase.**

* ★ Analizē spēles, kurās gājiens maina stāvokli sarežģītāk (skaitļu aizstāšana,
  kaudzīšu apvienošana).
* ★ Lieto invariantu, lai pamatotu, ka viens spēlētājs vienmēr saglabā izdevīgu stāvokli.

*Piemērs.* Uz $1 \times n$ taisnstūra Kims un Māris pārvieto savus kauliņus
(`LV.NOL.2025.10.4`).
Uz tāfeles ir skaitlis $2$; gājienā to nomaina pēc noteikta likuma (`LV.VOL.2026.9.2`).

**11.-12. klase.**

* ★ Strādā ar spēlēm, kurām ir liela stāvokļu telpa; sadala stāvokļus klasēs.
* ★ Lieto stratēģijas nozagšanas ideju un spēles ar pretinieka atbildes izvēli
  (adaptīvas spēles).

*Piemērs.* Katrā gājienā spēlētājs paņem $p^n$ konfektes, kur $p$ - pirmskaitlis
(`LV.NOL.2024.12.4`).
Ar $30$ atsvariem $1, 2, \ldots, 30$ kg spēlētāji pamīšus liek atsvarus uz svaru
kausiem (`LV.NOL.2026.12.4`).

### 3.7. K6. Algoritmi, svēršanas un informācija

**5.-6. klase.**

* ★ Sastāda svēršanas plānu ar sviru svariem bez atsvariem; apraksta, ko dara katrā no
  iespējamiem iznākumiem.

*Piemērs.* Sešiem atsvariem viens uzraksts ir nepareizs; kā to atrast ar divām
svēršanām (`LV.NOL.2025.6.5`)?

**7.-8. klase.**

* ★ Risina meklēšanas un kārtošanas uzdevumus, tostarp par turnīriem un uzvarētāju
  noteikšanu.
* ★ Novērtē vajadzīgo darbību skaitu no apakšas.

*Piemērs.* Uzdevumi par turnīriem, kuros no rezultātu summas jāsecina par uzvarētāju.

**9.-10. klase.**

* ★ Novērtē, cik informācijas dod viens gājiens, un no tā izsecina apakšējo robežu
  gājienu skaitam.
* ★ Konstruē algoritmu, kas šo robežu sasniedz.

*Piemērs.* No septiņām monētām divas ir viltotas un vieglākas; kā tās atrast ar trim
svēršanām (`LV.VOL.2025.9.4`)?
Kāds ir mazākais gājienu skaits, lai iztukšotu $2023$ kastes (`LV.NOL.2023.12.5`)?

**11.-12. klase.**

* ★ Pierāda algoritma optimalitāti, apvienojot informācijas novērtējumu ar konstrukciju.
* ★ Risina uzdevumus, kuros pretinieks atbild "sliktākajā iespējamajā" veidā.

*Piemērs.* Kristīne vēlas noteikt Alberta pierakstīto permutāciju, veicot gājienus ar
jautājumiem (`LV.VOL.2026.11.5`).
Juris nosauc piecus skaitļus, un Andris atbild ar vienu no reizinājumiem
(`LV.VOL.2026.7.5`).

### 3.8. K7. Loģikas uzdevumi

**5.-6. klase.**

* Risina uzdevumus par patiesības teicējiem un meļiem; pārbauda visus pieņēmumus.
* Nosaka apgalvojuma patiesumu un uzrāda pretpiemēru.

*Piemērs.* Katrs no $10$ rūķīšiem vienmēr saka patiesību vai vienmēr melo
(`LV.AMO.2024.6.3`).
Alise satika $5$ rūķīšus un saņēma $5$ atšķirīgas atbildes uz jautājumu, cik ir meļu
(`LV.NOL.2026.5.4`).

**7.-8. klase.**

* Analizē vairāku apgalvojumu sistēmu, no kuriem daļa ir patiesi; lieto implikāciju
  "ja..., tad...".
* Nosaka, cik apgalvojumu var būt patiesi vienlaikus.

*Piemērs.* Četri eksperti izteica prognozes par maratona rezultātiem (`LV.NOL.2026.6.3`).

**9.-10. klase.**

* Lieto kvantorus "eksistē" un "katram"; formulē apgalvojuma noliegumu.
* Sadala risinājumu gadījumos un pamato, ka gadījumi ir visi.

*Piemērs.* Uzdevumi, kuros jāizšķir, vai prasīts pierādīt eksistenci vai apgalvojumu
visiem objektiem.

**11.-12. klase.**

* ★ Risina uzdevumus par informācijas sadalījumu starp vairākiem dalībniekiem (ko katrs
  zina un ko var secināt).
* ★ Formulē un lieto nepieciešamos un pietiekamos nosacījumus.

*Piemērs.* Uzdevumi, kuros dalībnieki secīgi paziņo, ka nezina atbildi, un no tā izriet
secinājums.

---

## 4. Skaitļu teorija

### 4.1. Satura karte

| Tematiskā līnija | 5.-6. klase | 7.-8. klase | 9.-10. klase | 11.-12. klase |
|---|---|---|---|---|
| **S1** Dalāmība | Dalāmības pazīmes ar $2, 3, 5, 9, 10$; dalīšana ar atlikumu | Pazīmes ar $4, 8, 11, 25$; dalāmības īpašības, LKD un MKD | Eiklīda algoritms, dalītāju skaits, savstarpēji pirmskaitļi | Dalītāju funkcija $d(n)$, faktoriāla dalāmība, pakāpes rādītājs ★ |
| **S2** Pirmskaitļi | Pirmskaitļi līdz $100$, sadalījums reizinātājos | Sadalījuma viennozīmība, savstarpēji pirmskaitļi | Dalītāju skaita formula, pilnie kvadrāti | Pirmskaitļu īpašības vienādojumos, pirmskaitļu pakāpes ★ |
| **S3** Skaitļa decimālais pieraksts | Ciparu summa un reizinājums, skaitļu rēbusi | Pieraksts $\overline{ab} = 10a+b$, ciparu pārvietošana | Skaitļi ar dotām ciparu īpašībām, ciparu virknes | Skaitļu pierakstu savienošana, cita bāze ★ |
| **S4** Kongruences | Paritāte, pēdējais cipars | Atlikumi pēc maza moduļa, paritātes arguments | Kongruences pēc moduļa $n$, pakāpju periodiskums ★ | Fermā mazā teorēma, atlikumu kvadrāti ★ |
| **S5** Vienādojumi veselos skaitļos | Skaitļu atrašana ar pārlasi un novērtējumu | Sadalīšana reizinātājos, novērtējums | Vienādojumi ar daļām, pretruna pēc moduļa | Diofanta vienādojumi ar pirmskaitļiem un faktoriāliem ★ |
| **S6** Pilnie kvadrāti un pakāpes | Kvadrātu tabula, pēdējais cipars | Kvadrāta atlikumi pēc $3$ un $4$ ★ | Skaitlis starp diviem secīgiem kvadrātiem ★ | Pilnas pakāpes, pakāpju salīdzināšana ★ |

### 4.2. S1. Dalāmība

**5.-6. klase.**

* Lieto dalāmības pazīmes ar $2, 3, 5, 9, 10$ un to kombinācijas (piemēram, ar $6$, $15$,
  $45$).
* Veic dalīšanu ar atlikumu; pieraksta $a = bq + r$, kur $0 \leq r < b$.
* Atrod skaitļa dalītājus un kopīgos dalītājus.

*Piemērs.* Skaitlis PLATONS dalās ar $45$; pierādīt, ka SOKRATS nedalās ar $45$
(`LV.AMO.2025.6.4`).
Sešstūra virsotnēs ierakstīt skaitļus tā, lai blakus esošo skaitļu LKD būtu $1$
(`LV.NOL.2025.5.1`).

**7.-8. klase.**

* Lieto dalāmības pazīmes ar $4, 8, 11, 25$; zina to pamatojumu ar decimālo pierakstu.
* Lieto dalāmības īpašības: ja $a \, \vdots \, c$ un $b \, \vdots \, c$, tad
  $(a \pm b) \, \vdots \, c$.
* Lieto LKD un MKD; zina sakarību $\mathrm{LKD}(a,b) \cdot \mathrm{MKD}(a,b) = ab$.

*Piemērs.* Naturāliem $a$ un $b$ dots $34a = 43b$; pierādīt, ka $a+b$ nav pirmskaitlis
(`LV.NOL.2026.8.3`).
Kāda ir mazākā sešciparu skaitļa ciparu summa, ja skaitlis dalās ar $99$
(`LV.AMO.2025.7.3`)?

**9.-10. klase.**

* ★ Lieto Eiklīda algoritmu un īpašību
  $\mathrm{LKD}(a, b) = \mathrm{LKD}(a - b, b)$.
* ★ Lieto to, ka savstarpēji pirmskaitļu reizinājums dala skaitli tad un tikai tad, ja to
  dala katrs reizinātājs.
* ★ Aprēķina dalītāju skaitu no sadalījuma pirmreizinātājos.

*Piemērs.* Kāds ir vismazākais naturālais skaitlis, kuram ir tieši $18$ dalītāju un kas
dalās ar $7$ (`LV.NOL.2025.10.2`)?
Atrast mazāko $N$, kuram $N!$ dalās ar $2025$ (`LV.NOL.2025.9.2`).

**11.-12. klase.**

* ★ Lieto dalītāju funkciju $d(n)$ un dalītāju summu; zina, ka $d(n)$ ir nepāra tad un
  tikai tad, ja $n$ ir pilns kvadrāts.
* ★ Nosaka pirmskaitļa $p$ pakāpes rādītāju skaitļā $n!$ (Ležandra formula).
* ★ Lieto pakāpes rādītāju salīdzināšanu dalāmības pierādīšanai.

*Piemērs.* Naturālam $A$ ir tieši $111$ dalītāju; pierādīt, ka $A$ nedalās ar $216$
(`LV.NOL.2025.11.2`).
Pierādīt, ka katram $k$ eksistē tādi $a, b$, ka $a!$ dalās ar $b$, $b!$ dalās ar $a$ un
$a - b = k$ (`LV.AMO.2025.11.1`).

### 4.3. S2. Pirmskaitļi

**5.-6. klase.**

* Atšķir pirmskaitļus un saliktus skaitļus līdz $100$; zina Eratostena sieta ideju.
* Sadala skaitli pirmreizinātājos un lieto sadalījumu dalītāju atrašanai.

*Piemērs.* Vai naturāla skaitļa ciparu reizinājums var būt $2520$ vai $5460$
(`LV.NOL.2025.5.2`)?
Vai $299$ var izteikt kā vairāku naturālu skaitļu summu tā, lai arī reizinājums būtu
$299$ (`LV.NOL.2025.6.2`)?

**7.-8. klase.**

* Lieto sadalījuma pirmreizinātājos viennozīmību.
* Lieto savstarpēji pirmskaitļu jēdzienu; pamato, kad divi skaitļi ir savstarpēji
  pirmskaitļi.
* ★ Pamato, ka skaitlis nav pirmskaitlis, uzrādot tā sadalījumu reizinātājos.

*Piemērs.* Kāds ir lielākais dažādu naturālu skaitļu skaits, ko var uzrakstīt tā, ka
neviens nedalās ar $210$, bet jebkuru četru reizinājums dalās (`LV.NOL.2026.7.5`)?

**9.-10. klase.**

* ★ Lieto dalītāju skaita formulu: ja $n = p_1^{a_1} \cdots p_k^{a_k}$, tad
  $d(n) = (a_1+1)\cdots(a_k+1)$.
* ★ Pamato, ka skaitlis ir pilns kvadrāts, no tā sadalījuma pirmreizinātājos.
* ★ Lieto to, ka pirmskaitļu ir bezgalīgi daudz.

*Piemērs.* Atrast visus $n$, kuriem $n-1$ un $n+1$ ir pirmskaitļi un visu $n$ dalītāju
summa ir $2n$ (`LV.NOL.2026.10.5`).

**11.-12. klase.**

* ★ Lieto pirmskaitļa īpašību: ja $p \mid ab$, tad $p \mid a$ vai $p \mid b$.
* ★ Risina uzdevumus, kuros mainīgie ir pirmskaitļi, aplūkojot mazos pirmskaitļus
  atsevišķi.

*Piemērs.* Atrast visus pirmskaitļu pārus $(p; q)$, kuriem $p^q = q^p + 7$
(`LV.NOL.2024.12.5`).
Pierādīt, ka $p^4 - 1$ dalās ar $240$ katram pirmskaitlim $p \geq 7$
(`LV.NOL.2022.12.4`).

### 4.4. S3. Skaitļa decimālais pieraksts

**5.-6. klase.**

* Aprēķina ciparu summu un ciparu reizinājumu; lieto tos dalāmības uzdevumos.
* Risina skaitļu rēbusus (burti vietā ciparu), pamatojot katru soli.

*Piemērs.* Ierakstīt ciparus burtu vietā, lai iegūtu pareizu reizināšanas piemēru
(`LV.AMO.2025.5.2`).

**7.-8. klase.**

* Pieraksta skaitli pozicionālā formā, piemēram, $\overline{abc} = 100a + 10b + c$, un
  ar to strādā algebriski.
* ★ Analizē, kā mainās skaitlis, pārvietojot, dzēšot vai pievienojot ciparu.

*Piemērs.* Saskaitot divus skaitļus, viena skaitļa beigās nejauši pierakstīts $0$;
atjaunot sākotnējos skaitļus (`LV.VOL.2026.8.1`).
LAPSA un SPALS dalās ar $9$; pierādīt, ka tieši viens no tiem dalās ar $11$
(`LV.AMO.2025.8.5`).

**9.-10. klase.**

* ★ Risina uzdevumus par skaitļiem ar dotām ciparu īpašībām, apvienojot dalāmību un
  novērtējumu.
* ★ Pēta virknes, kuru veidošanā piedalās cipari (ciparu summa vai reizinājums).

*Piemērs.* Atrast visus trīsciparu skaitļus, kas ir tieši $5$ reizes lielāki par savu
ciparu reizinājumu (`LV.NOL.2025.10.1`).
Naturālu skaitli sauc par īpašu, ja, nodzēšot jebkuru ciparu, iegūst tā dalītāju
(`LV.VOL.2025.10.5`).

**11.-12. klase.**

* ★ Strādā ar skaitļiem, kas iegūti, savienojot citu skaitļu pierakstus.
* ★ Lieto pierakstu citā skaitīšanas sistēmā, ja tas vienkāršo uzdevumu.

*Piemērs.* Uz tāfeles blakus uzrakstīti $2^n$ un $14^n$; vai iegūtais skaitlis mīnus $1$
var būt pirmskaitlis (`LV.VOL.2024.12.4`)?
Vai $45$-ciparu skaitlis, kurā ir viens vieninieks, divi divnieki, ..., deviņi
devītnieki, var būt pilns kvadrāts (`LV.VOL.2026.8.4`)?

### 4.5. S4. Kongruences

**5.-6. klase.**

* Lieto paritāti: pāra un nepāra skaitļu summas un reizinājumi.
* Nosaka reizinājuma un pakāpes pēdējo ciparu.

*Piemērs.* Vai tūrista maršruta garums pilsētas kvadrātveida ielu tīklā var būt tieši
$25$ km (`LV.NOL.2025.6.4`)?

**7.-8. klase.**

* ★ Aplūko skaitļus pēc atlikuma, dalot ar maziem moduļiem ($2, 3, 4, 5, 9$).
* ★ Lieto paritātes argumentu pierādījumos no pretējā.

*Piemērs.* Cik starp pirmajiem $2025$ naturālajiem skaitļiem ir tādu $x$, ka $x(x+1)$
dalās ar $74$ (`LV.NOL.2025.8.2`)?

**9.-10. klase.**

* ★ Lieto kongruences pierakstu $a \equiv b \pmod{n}$ un darbības ar kongruencēm.
* ★ Lieto pakāpju atlikumu periodiskumu, lai noteiktu $a^n$ atlikumu.
* ★ Zina, ka pilna kvadrāta atlikums, dalot ar $4$, ir $0$ vai $1$, bet, dalot ar $3$, -
  $0$ vai $1$.

*Piemērs.* Pierādīt, ka nekādu divu secīgu naturālu skaitļu reizinājums nav izsakāms
formā $36n + 8$ (`LV.NOL.2023.11.4`).

**11.-12. klase.**

* ★ Lieto Fermā mazo teorēmu: ja $p$ ir pirmskaitlis un $p \nmid a$, tad
  $a^{p-1} \equiv 1 \pmod{p}$.
* ★ Lieto atlikumu kvadrātus (kvadrātiskos atlikumus) pēc mazu pirmskaitļu moduļa.
* ★ Apvieno vairākus moduļus vienā risinājumā.

*Piemērs.* Pierādīt, ka $2^{2n-1} 3^{n-1} + 5^n$ dalās ar $7$ visām naturālām $n$
vērtībām (`LV.VOL.2025.12.1`).
Pierādīt, ka nevar atrast tādus pirmskaitļus $p, q$, kuriem $p^{q-1} + q^{p-1} + 1$ ir
vesela skaitļa kvadrāts (`LV.VOL.2023.12.4`).

### 4.6. S5. Vienādojumi veselos skaitļos

**5.-6. klase.**

* Atrod skaitļus ar dotu īpašību ar sistemātisku pārlasi, iepriekš sašaurinot meklēšanas
  apgabalu.
* Pamato, ka citu atrisinājumu nav.

*Piemērs.* Kādu četru dažādu naturālu skaitļu reizinājums ir $414$ (`LV.NOL.2025.7.2`)?

**7.-8. klase.**

* ★ Sadala vienādojuma vienu pusi reizinātājos un aplūko reizinātāju iespējamās vērtības.
* ★ Lieto novērtējumu, lai ierobežotu mainīgo vērtību apgabalu.

*Piemērs.* Uzdevumi, kuros no $xy + x + y = N$ jāiegūst $(x+1)(y+1) = N+1$.

**9.-10. klase.**

* ★ Risina vienādojumus ar daļām, piemēram, $\frac{1}{a}+\frac{1}{b}+\frac{1}{c} = k$,
  pieņemot $a \leq b \leq c$ un novērtējot.
* ★ Pierāda atrisinājumu neesamību ar pretrunu pēc moduļa.

*Piemērs.* Atrast divus dažādus trijniekus $(a,b,c)$ ar $a<b<c$ un
$\frac{1}{a}+\frac{1}{b}+\frac{1}{c} = \frac{4}{2025}$ (`LV.AMO.2025.9.1`).
Atrisināt naturālos skaitļos $(a+1)(b+1)(c+1) = 3abc$ (`LV.NOL.2025.10.5`).

**11.-12. klase.**

* ★ Risina Diofanta vienādojumus, kuros piedalās pirmskaitļi, faktoriāli vai pakāpes.
* ★ Pierāda, ka atrisinājumu ir bezgalīgi daudz, uzrādot parametrisku sēriju.

*Piemērs.* Atrisināt veselos skaitļos $17a^2 - 7b^2 + c^2 = 2023$ (`LV.AMO.2023.11.5`).
Atrast visus naturālo skaitļu trijniekus $a, b, c$, kuriem $ab+1$, $bc+1$ un $ca+1$ ir
faktoriāli (`LV.VOL.2026.11.4`).

### 4.7. S6. Pilnie kvadrāti un pakāpes

**5.-6. klase.**

* Zina kvadrātu tabulu un atpazīst pilnos kvadrātus; zina, ar kādiem cipariem kvadrāts
  var beigties.

*Piemērs.* Uzdevumi, kuros no pēdējā cipara secina, ka skaitlis nav kvadrāts.

**7.-8. klase.**

* ★ Lieto kvadrāta atlikumus: pilns kvadrāts, dalot ar $4$, dod atlikumu $0$ vai $1$;
  dalot ar $3$, - $0$ vai $1$.
* ★ Lieto sakarību $a^2 - b^2 = (a-b)(a+b)$ pilno kvadrātu uzdevumos.

*Piemērs.* Uzdevumi, kuros jāpierāda, ka dots skaitlis nav pilns kvadrāts.

**9.-10. klase.**

* ★ Lieto novērtējumu $n^2 < N < (n+1)^2$, lai pamatotu, ka $N$ nav pilns kvadrāts.
* ★ Kombinē kvadrāta īpašības ar dalāmību un sadalījumu pirmreizinātājos.

*Piemērs.* Atrast visus $n$, kuriem $n! - 8$ vai $n! - 1$ ir pilns kvadrāts
(`LV.NOL.2026.9.4`).

**11.-12. klase.**

* ★ Strādā ar pilnām $k$-tajām pakāpēm; lieto pakāpju rādītāju dalāmību.
* ★ Salīdzina pakāpes ar dažādām bāzēm, izmantojot novērtējumus.

*Piemērs.* Vai eksistē naturāls skaitlis, kuru reizinot ar $2$, iegūst kvadrātu, ar $3$ -
kubu, ar $5$ - piekto pakāpi (`LV.VOL.2022.11.1`)?
Naturāliem $x, y$ skaitlis $x + 2y + 1$ ir pirmskaitlis; pierādīt, ka $x^2 + 2xy - 2y$
nav pilns kvadrāts (`LV.AMO.2025.12.5`).

---

## 5. Vispārīgās metodes un pierādīšana

Šīs sadaļas prasmes nav piesaistītas konkrētai matemātikas apakšnozarei. Tās ir tas, kas
olimpiāžu uzdevumu risināšanu visvairāk atšķir no ierastajiem mācību stundu uzdevumiem,
un tieši šeit skolēni visbiežāk zaudē punktus.

### 5.1. Satura karte

| Tematiskā līnija | 5.-6. klase | 7.-8. klase | 9.-10. klase | 11.-12. klase |
|---|---|---|---|---|
| **M1** Apgalvojumi un risinājuma noformējums | Atbildes pamatošana; pretpiemērs | Kvantori "eksistē" un "katram"; ko nozīmē "vai var" ★ | Nepieciešams un pietiekams nosacījums; pierādījuma struktūra ★ | Pilnīgs noformējums, atsauces uz zināmām teorēmām ★ |
| **M2** Pilnā pārlase un gadījumu analīze | Sistemātiska visu variantu uzskaitīšana | Gadījumi pēc paritātes vai atlikuma | Pārlases apjoma samazināšana ar novērtējumu | Pārlase ar vispārīguma nezaudēšanu ★ |
| **M3** Konstruktīvs piemērs | Piemēra atrašana un pārbaude | Konstrukcijas vispārināšana uz patvaļīgu $n$ ★ | Bezgalīgas piemēru sērijas ★ | Rekursīva un parametriska konstrukcija ★ |
| **M4** Pierādījums no pretējā | Vienkārši spriedumi "tā nevar būt, jo..." | Pretruna ar paritāti vai dalāmību ★ | Pretruna ar novērtējumu, minimālais pretpiemērs ★ | Bezgalīgās nolaišanās metode ★ |
| **M5** Novērtējums un konstrukcija | Uzdevumi "kāds ir mazākais skaits" ★ | Novērtējums, sadalot grupās ★ | Novērtējums ar dubulto skaitīšanu vai vidējošanu ★ | Optimuma pierādījums sarežģītās konfigurācijās ★ |
| **M6** Matemātiskā indukcija | - | Induktīvas konstrukcijas bez formāla pieraksta ★ | Indukcija ar soli $1$ ★ | Indukcija ar stiprinātu apgalvojumu un vairākiem soļiem ★ |
| **M7** Ekstremālā elementa metode | Lielākā vai mazākā objekta aplūkošana ★ | Ekstremālais elements pierādījumā no pretējā ★ | Ekstremālais elements grafos un virknēs ★ | Vidējošanas princips ★ |
| **M8** Vispārināšana un vienkāršošana | Mazāka gadījuma izspēlēšana ★ | Pāreja uz līdzīgu, vienkāršāku uzdevumu ★ | Hipotēzes formulēšana no piemēriem ★ | Uzdevuma pārformulēšana citā valodā ★ |

### 5.2. M1. Apgalvojumi un risinājuma noformējums

**5.-6. klase.**

* Pamato katru atbildi ar spriedumu "..., jo ..."; nepietiek tikai ar atbildi.
* Uzrāda pretpiemēru, lai parādītu, ka vispārīgs apgalvojums nav patiess.
* Zina, ka atrastais piemērs ir jāpārbauda.

**7.-8. klase.**

* ★ Atšķir uzdevumus "atrast piemēru", "atrast visus", "pierādīt" un "vai var".
* ★ Zina, ka atbilde "jā" prasa piemēru, bet atbilde "nē" prasa pierādījumu visiem
  gadījumiem.
* ★ Lieto vārdus "eksistē" un "katram" precīzi.

**9.-10. klase.**

* ★ Atšķir īpašību no pazīmes, nepieciešamu nosacījumu no pietiekama.
* ★ Strukturē pierādījumu: kas ir dots, kas jāpierāda, kāda ir spriedumu ķēde.
* ★ Prot pārbaudīt cita risinājuma korektumu un atrast tajā kļūdu.

**11.-12. klase.**

* ★ Noformē pilnīgu risinājumu, kurā ir aplūkoti visi gadījumi un atsauces uz izmantotām
  teorēmām.
* ★ Atsevišķi noformē uzdevuma abas daļas: novērtējumu un konstrukciju, eksistenci un
  vienīgumu.

### 5.3. M2. Pilnā pārlase un gadījumu analīze

**5.-6. klase.**

* Uzskaita visus variantus sakārtotā secībā un pamato, ka neviens nav palaists garām.
* Atmet variantus, kas neapmierina nosacījumus.

*Piemērs.* Caurspīdīgā kastē ir konfektes; četri bērni min skaitu, neviens nav uzminējis,
un zināmas kļūdu lielumu vērtības (`LV.AMO.2024.6.5`).

**7.-8. klase.**

* ★ Sadala uzdevumu gadījumos pēc paritātes, pēc atlikuma vai pēc figūras novietojuma.
* ★ Pamato, ka gadījumu saraksts ir pilnīgs.

*Piemērs.* $9$ veselu skaitļu virknē katru $5$ pēc kārtas rakstīto skaitļu vidējais
aritmētiskais ir $10$ (`LV.NOL.2026.8.4`).

**9.-10. klase.**

* ★ Samazina pārlases apjomu ar iepriekšēju novērtējumu vai dalāmības apsvērumu.
* ★ Zina, kad drīkst pieņemt $a \leq b \leq c$, nezaudējot vispārīgumu.

**11.-12. klase.**

* ★ Lieto simetriju, lai samazinātu aplūkojamo gadījumu skaitu, un to precīzi pamato.
* ★ Sadala bezgalīgu situāciju skaitu galīgā skaitā klašu.

### 5.4. M3. Konstruktīvs piemērs

**5.-6. klase.**

* Atrod un pieraksta piemēru, kas apmierina visus nosacījumus; pārbauda katru nosacījumu
  atsevišķi.
* Zina, ka uzdevumā "parādi vienu veidu" pietiek ar vienu korektu piemēru.

*Piemērs.* Ierakstīt aplīšos skaitļus no $1$ līdz $12$ tā, lai uz katras sešstūra malas
summa būtu vienāda (`LV.AMO.2025.5.1`).

**7.-8. klase.**

* ★ Konstruē piemēru patvaļīgam $n$, aprakstot vispārīgu konstrukcijas likumu.
* ★ Pamato, kāpēc konstrukcija darbojas visiem $n$.

*Piemērs.* Pierādīt, ka skaitļus no $1$ līdz $2022$ var sakārtot rindā tā, ka blakus
esošie atšķiras par $6$ vai $11$ (`LV.NOL.2022.11.5`).

**9.-10. klase.**

* ★ Konstruē bezgalīgu piemēru sēriju, lai pierādītu, ka objektu ar doto īpašību ir
  bezgalīgi daudz.

*Piemērs.* Pierādīt, ka eksistē bezgalīgi daudz naturālu skaitļu četrinieku ar doto
īpašību (`LV.VOL.2023.11.4`).

**11.-12. klase.**

* ★ Veido rekursīvu konstrukciju: no piemēra ar $n$ elementiem iegūst piemēru ar $n+1$
  elementiem.
* ★ Veido konstrukciju ar parametru un izvēlas parametru tā, lai izpildītos visi
  nosacījumi.

### 5.5. M4. Pierādījums no pretējā

**5.-6. klase.**

* Pamato, ka kaut kas nav iespējams, norādot uz pretrunu ar doto nosacījumu.

*Piemērs.* Vai iespējams, ka pēc automāta izmantošanas palika noteikts žetonu komplekts
(`LV.NOL.2024.5.5`)?

**7.-8. klase.**

* ★ Pieņem pretējo, iegūst pretrunu ar paritāti, dalāmību vai skaita apsvērumu.
* ★ Formulē pieņēmumu skaidri: "pieņemsim pretējo - ka ...".

*Piemērs.* Pierādīt, ka $45$-ciparu skaitlis nevar būt pilns kvadrāts
(`LV.VOL.2026.8.4`).

**9.-10. klase.**

* ★ Lieto minimālā pretpiemēra ideju: aplūko mazāko objektu, kas apgāž apgalvojumu.
* ★ Iegūst pretrunu ar novērtējumu (skaitlis vienlaikus lielāks un mazāks par kādu
  lielumu).

**11.-12. klase.**

* ★ Lieto bezgalīgās nolaišanās metodi: no pretpiemēra konstruē mazāku pretpiemēru.

*Piemērs.* Pierādīt, ka divu vai vairāku secīgu naturālu skaitļu kubu summa nevar būt
pirmskaitlis (`LV.VOL.2022.12.3`).

### 5.6. M5. Novērtējums un konstrukcija

Šī ir biežākā olimpiāžu uzdevumu struktūra vecākajās klasēs: ja jautāts par lielāko vai
mazāko iespējamo vērtību $N$, risinājumam ir **divas daļas** - pierādījums, ka labāk
nevar ($N$ ir robeža), un piemērs, kas robežu sasniedz.

**5.-6. klase.**

* ★ Uzdevumā "kāds ir mazākais skaits" saprot, ka jāatbild uz diviem jautājumiem:
  kāpēc ar mazāku skaitu nepietiek un kā ar doto skaitu pietiek.

*Piemērs.* Kāds mazākais punktu skaits jānodzēš, lai nekādi trīs no atlikušajiem
neatrastos uz vienas taisnes (`LV.NOL.2024.5.2`)?
Kādu mazāko trijstūrīšu skaitu jānokrāso melnus, lai katram baltajam būtu melns kaimiņš
(`LV.NOL.2026.5.5`)?

**7.-8. klase.**

* ★ Iegūst novērtējumu, sadalot objektus grupās un novērtējot katru grupu.
* ★ Uzrāda konstrukciju, kas sasniedz novērtējumu.

*Piemērs.* Kāds ir mazākais reižu skaits, lai uznestu $150$ kg ķirbju
(`LV.AMO.2025.8.4`)?

**9.-10. klase.**

* ★ Iegūst novērtējumu ar dubulto skaitīšanu, vidējošanu vai Dirihlē principu.

*Piemērs.* Kāds ir mazākais gājienu skaits, ar kuru var iztukšot $2023$ kastes
(`LV.NOL.2023.12.5`)?

**11.-12. klase.**

* ★ Pierāda optimalitāti konfigurācijās ar daudziem parametriem; nošķir gadījumus, kad
  optimums atšķiras.

*Piemērs.* Atrast mazāko iespējamo "labo" rūtiņu skaitu $10 \times 10$ tabulā
(`LV.VOL.2026.12.4`).
Kāds lielākais rūtiņu skaits var būt tukšam taisnstūrim $2026 \times 2026$ tabulā
(`LV.NOL.2026.11.4`)?

### 5.7. M6. Matemātiskā indukcija

**5.-6. klase.** -

**7.-8. klase.**

* ★ Lieto induktīvu konstrukciju bez formāla pieraksta: parāda, kā no risinājuma ar $n$
  objektiem iegūt risinājumu ar $n+1$ objektiem.

**9.-10. klase.**

* ★ Zina un lieto matemātiskās indukcijas principu ar soli $1$: bāze, induktīvais
  pieņēmums, induktīvā pāreja.
* ★ Lieto indukciju dalāmības apgalvojumu un summu formulu pierādīšanai.

*Piemērs.* Pierādīt, ka $2^{2n-1} 3^{n-1} + 5^n$ dalās ar $7$ (`LV.VOL.2025.12.1`).

**11.-12. klase.**

* ★ Lieto indukciju ar vairākiem soļiem un stipro indukciju.
* ★ Zina, ka dažkārt jāpierāda stiprināts apgalvojums, lai induktīvā pāreja izdotos.
* ★ Lieto indukciju kombinatorikā un ģeometrijā (konstrukcijas, sagriešanas).

### 5.8. M7. Ekstremālā elementa metode

**5.-6. klase.**

* ★ Aplūko lielāko vai mazāko objektu situācijā (lielāko skaitli, garāko nogriezni,
  cilvēku ar visvairāk kaimiņiem).

*Piemērs.* Piecās mājās dzīvo dažāds cilvēku skaits; aplūkojot māju ar vislielāko
iedzīvotāju skaitu (`LV.AMO.2025.7.1`).

**7.-8. klase.**

* ★ Apvieno ekstremālo elementu ar pierādījumu no pretējā: pieņem pretējo un aplūko
  "sliktāko" objektu.

**9.-10. klase.**

* ★ Lieto ekstremālo elementu grafos (virsotne ar lielāko pakāpi) un virknēs (lielākais
  loceklis).

*Piemērs.* Rindā ir $n$ bumbiņas $100$ krāsās, un katrai krāsu pārei $A, B$ kāda $A$
krāsas bumbiņa atrodas pa kreisi no kādas $B$ krāsas bumbiņas; atrast mazāko $n$
(`LV.NOL.2025.9.5`).

**11.-12. klase.**

* ★ Lieto vidējošanas principu un ekstremālo elementu kopā ar novērtējumiem.

*Piemērs.* Šaha festivālā katrs izspēlēja ne vairāk kā $10$ partijas un katrs vismaz
vienu zaudēja (`LV.AMO.2024.11.2`).

### 5.9. M8. Vispārināšana un vienkāršošana

**5.-6. klase.**

* ★ Izspēlē uzdevumu ar mazākiem skaitļiem, lai saskatītu likumsakarību.

*Piemērs.* Uzdevumi ar gadskaitli ($2024$, $2025$, $2026$), kuros vispirms jāaplūko mazi
gadījumi.

**7.-8. klase.**

* ★ Pāriet uz līdzīgu, vienkāršāku uzdevumu un pēc tam atgriežas pie sākotnējā.
* ★ Saskata, ka lielā skaitļa vietā var strādāt ar tā atlikumu vai ar mazāku analogu.

**9.-10. klase.**

* ★ Formulē hipotēzi, aplūkojot vairākus gadījumus, un pēc tam to pierāda.
* ★ Saskata, ka uzdevums ar $2025$ objektiem ir uzdevums ar $n$ objektiem.

**11.-12. klase.**

* ★ Pārformulē uzdevumu citā matemātikas valodā: kombinatorisku - kā grafu, skaitlisku -
  kā polinomu, ģeometrisku - kā algebrisku.

*Piemērs.* Uzdevums par pilsētām un ceļiem, kas pārformulēts kā uzdevums par grafa
sakarīgumu (`LV.VOL.2023.12.5`).

---

## Avoti un saistītie dokumenti

* [Matemātikas olimpiāžu programma (2022)](https://kapsitis.github.io/nms-courses/courses_26_27/common_olympiad_program/) -
  tēmu saraksts, īsa teorija un paraugpiemēri.
* [Pamatskolas standarts (MK Nr. 747)](https://kapsitis.github.io/nms-courses/pamatskolas_standarts/) - sasniedzamie
  rezultāti, beidzot 3., 6. un 9. klasi.
* [Vidusskolas standarts (MK Nr. 416)](https://kapsitis.github.io/nms-courses/vidusskolas_standarts/) - sasniedzamie
  rezultāti vispārīgajā, optimālajā un augstākajā apguves līmenī.
* Uzdevumu arhīvs: mapes `docs/LV.AMO`, `docs/LV.NOL` un `docs/LV.VOL`; uzdevumi
  pa tēmām - [uzdevumu pārlūkā](https://www.dudajevagatve.lv/eliozo/curriculum).
* LU A. Liepas Neklātienes matemātikas skolas [grāmatas un materiāli](https://www.nms.lu.lv/arhivs-un-materali/gramatas/).
