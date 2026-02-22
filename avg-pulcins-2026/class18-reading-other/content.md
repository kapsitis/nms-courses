---
title: "Citu (neģeometrisku) uzdevumu lasīšana (2026-02-16)"
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "Citu (neģeometrisku) uzdevumu lasīšana (2026-02-16)"
header-includes:
  - |
    \makeatletter
    \RedeclareSectionCommand[
      beforeskip=1.2ex plus 0.4ex minus 0.2ex,
      afterskip=0.4ex plus 0.2ex minus 0.2ex
    ]{subsection}
    \makeatother
  - \setcounter{section}{16}
  - |
    \usepackage{etoolbox}
    \AtBeginEnvironment{footnotesize}{\footnotesize}
---
# Citu (neģeometrisku) uzdevumu lasīšana (2026-02-16) 

Praktisks ieteikums (4R: Read, Restate, Represent, Roadmap):  
(1) **Izlasīt** uzdevumu un atrast visus nosacījumus;  
(2) **Pārformulēt** īsāk un saviem vārdiem;  
(3) **Attēlot** situāciju zīmējumā, tabulā utt.  
(4) **Izplānot** sagaidāmās risinājuma darbības.


## Iesildīšanās jautājumi  {-}

* Dalot $1$ ar $7$ "stabiņā" iegūstam atlikumu virkni $a_1 = 3$, $a_2 = 2$, $a_3 = 6$, 
  $a_4 = 4$, $a_5 = 5$, $a_6 = 1$, $\ldots$. Izteikt $a_{n+1}$ bez dalīšanas - tikai 
  ar reizināšanu un atlikuma operāciju "mod". 
* Pamatot, ka $ax \equiv b \pmod {13}$ var atrisināt visiem veseliem $a,b$, 
  ja vien $a \not\equiv 0 \pmod {13}$. (*Bijekcija skaitļa 13 atlikumiem.*)
* Sienāzis sāk kustību punktā ar koordināti $x=0$. Ar vienu lēcienu viņš vai nu dubulto 
  šo koordināti, vai pieskaita tai $1$. 
  Pēc $9$ lēcieniem viņš nonāk punktā $x = 100$. Kāds bija viņa pēdējais lēciens? (*Konstrukcija no beigām.*)
* Atrast naturālus $x,y$, kam izpildās $xy + 2x + 3y = 95$. (*Faktorizācijas triks.*)
* Pa rūtiņu līnijām uzzīmēts taisnstūris $a \times b$. Kādiem jābūt tā izmēriem, 
  lai taisnstūra laukums (rūtiņu vienībās) būtu vienāds ar tā perimetru? (*Vienādojums un faktorizācijas triks.*)



## 1.uzdevums (LV.VOL.2015.9.3) {-}


Aija izvēlas naturālu skaitli $n \leq 100$ un veido skaitļu virkni, kur katru 
nākamo virknes locekli iegūst pēc šāda likuma:

- ja $2 n \leq 100$, tad virknes nākamais loceklis ir $2n$;
- ja $2 n>100$, tad virknes nākamais loceklis ir $2n-100$.

Ja virknē vēl kādreiz parādās skaitlis $n$, tad skaitli $n$ sauksim par 
*patīkamu*. Cik pavisam ir *patīkamu* skaitļu, kas nepārsniedz $100$?

Piemēram, skaitlis $40$ ir *patīkams*, jo $40;\ 80;\ 60;\ 20;\ 40;\ \ldots$, bet 
$25$ - nav, jo $25;\ 50;\ 100;\ 100;\ \ldots$ (tālāk virknē nav skaitļu, kas 
atšķirīgi no $100$).


::: solution
## Atrisinājums

Ir $25$ skaitļi, kas nepārsniedz $100$ un dalās ar $4$. Parādīsim, ka visi šie 
skaitļi ir *patīkami*. Katrs no tiem pieder vienam no trim cikliem:

$100 \rightarrow 100$;

$20 \rightarrow 40 \rightarrow 80 \rightarrow 60 \rightarrow 20$;

$4 \rightarrow 8 \rightarrow 16 \rightarrow 32 \rightarrow 64 \rightarrow 28 \rightarrow 56 \rightarrow 12 \rightarrow 24 \rightarrow 48 \rightarrow 96 \rightarrow 92 \rightarrow 84 \rightarrow 68 \rightarrow 36 \rightarrow 72 \rightarrow 44 \rightarrow 88 \rightarrow 76 \rightarrow 52 \rightarrow 4$

Pierādīsim, ka tie skaitļi, kas nedalās ar $4$, nevar būt *patīkami*. Šķirojam 
divus gadījums.

- Nepāra skaitļi nevar būt *patīkami*, jo visi nākamie virknes locekļi būs tikai 
  pāra skaitļi un, tātad, sākotnējā $n$ vērtība tajā atkārtoti parādīties nevar.
- Pāra skaitļi, kas nedalās ar $4$, var pierakstīt formā $n=4k+2$. Šajā 
  gadījumā otrais virknes loceklis būs vai nu $2 \cdot(4k+2)=4 \cdot(2k+1)$, 
  vai $2 \cdot(4k+2)-100=4 \cdot(2k-24)$. Abos gadījumos virknes otrais 
  loceklis dalās ar $4$ un tas ir uzrakstāms formā $4m$. Visi nākamie virknes 
  locekļi arī dalīsies ar $4$, jo vai nu $2 \cdot 4m=8m$, vai 
  $2 \cdot 4m-100=4 \cdot(2m-25)$. Līdz ar to virknē nevar atkārtoti parādīties
  skaitlis, kas nedalās ar $4$, un skaitlis $n=4k+2$ nav *patīkams*.

Tātad pavisam ir $25$ *patīkami* skaitļi.

## Atrisinājums

Ir $25$ skaitļi, kas nepārsniedz $100$ un dalās ar $4$. Parādīsim, ka visi šie 
skaitļi ir *patīkami*. Ja skaitlis $x$ dalās ar $4$, tad gan $2x$, gan $2x-100$ 
arī dalīsies ar $4$. Aplūkosim virkni, sākot ar patvaļīgu skaitli $x_{1}$, kas 
dalās ar $4$: $x_{1},\ x_{2},\ x_{3},\ \ldots$ Tā kā ir tikai $25$ skaitļi, kas
tajā var parādīties, tad skaidrs, ka kādā brīdī virknes locekļi sāks 
atkārtoties. Aplūkosim pirmo skaitli virknē, kas atkārtojas, tas ir, tādu 
$x_{j+1}$, ka visi iepriekšējie $x_{1},\ x_{2},\ \ldots,\ x_{j}$ ir dažādi, bet
$x_{j+1}$ ir vienāds ar kādu no tiem. Pierādīsim, ka $x_{j+1}=x_{1}$, ar to arī
būs pierādīts, ka skaitlis $x_{1}$ ir *patīkams*. Pieņemsim pretējo, ka 
$x_{j+1}=x_{k+1}$ un aplūkosim, kādi varēja būt iepriekšējie skaitļi $x_{j}$ un
$x_{k}$. Tā kā tiem jābūt dažādiem, tad skaidrs, ka $x_{j+1}$ un $x_{k+1}$ tika
iegūti ar dažādām darbībām, tas ir, $x_{j+1}=2x_{j}$ un $x_{k+1}=2x_{k}-100$ 
(vai otrādi), kas nozīmē, ka $2x_{j}=2x_{k}-100$ jeb $x_{k}-x_{j}=50$ un tā ir 
pretruna, jo gan $x_{j}$, gan $x_{k}$ dalās ar $4$, bet $50$ nedalās ar $4$.

Vēl jāpierāda, ka pārējie skaitļi nav *patīkami*. Skaidrs, ka nepāra skaitļi nav 
*patīkami*, jo, ja $x$ ir nepāra skaitlis, tad gan $2x$, gan $2x-100$ ir pāra 
skaitļi un tālāk virknē visi skaitļi būs pāra.

Ja skaitlis $x$ dalās ar $2$, bet nedalās ar $4$, tad $x$ nav *patīkams*, jo, gan
$2x$, gan $2x-100$ dalās ar $4$ un tālāk virknē visi skaitļi dalīsies ar $4$.
:::


## 2.uzdevums (LV.VOL.2016.9.5) {-}

Naturālu skaitļu virkni $\left(s_{i}\right)$ pēc parauga " $2016$ " veido šādi: 
virknes pirmais loceklis $s_{1}$ ir $2$; virknes otrais loceklis $s_{2}$ - 
mazākais naturālais skaitlis, kas lielāks nekā $s_{1}$ un tā pierakstā ir 
cipars $0$; virknes trešais loceklis $s_{3}$ - mazākais naturālais skaitlis, 
kas lielāks nekā $s_{2}$ un tā pierakstā ir cipars $1$; virknes ceturtais 
loceklis $s_{4}$ - mazākais naturālais skaitlis, kas lielāks nekā $s_{3}$ un tā
pierakstā ir cipars $6$. Pēc tam meklētie cipari cikliski atkārtojas: 
$2-0-1-6-2-0-\ldots$. Virknes pirmie locekļi ir 
$2;\ 10;\ 11;\ 16;\ 20;\ 30;\ 31;\ 36;\ 42;\ 50$.

Kādi ir četri nākamie skaitļi, kas virknē seko aiz skaitļa $2016$?


::: solution
## Atrisinājums

Pavisam ir četru veidu *gājieni*: " $2 \rightarrow 0$ " (skaitlis satur $2$ un 
meklējam nākamo skaitli, kas satur $0$), " $0 \rightarrow 1$ ", 
" $1 \rightarrow 6$ " un " $6 \rightarrow 2$ ". Turklāt šie *gājieni* cikliski 
atkārtojas tieši šādā secībā.

Lai noskaidrotu, kuri nākamie skaitļi seko virknē pēc skaitļa $2016$, 
nepieciešams uzzināt, pēc kāda *gājiena* tika sasniegts skaitlis $2016$.

Aplūkosim iespējamos gadījumus.

**(A)** Skaitli $2016$ nevar iegūt pēc *gājiena* " $6 \rightarrow 2$ ", jo 
iepriekšējais virknes loceklis būtu $2006$, bet nākamais skaitlis, kas ir 
lielāks nekā $2006$ un satur ciparu $2$, ir $2007$.

**(B)** Skaitli $2016$ nevar iegūt pēc *gājiena* " $2 \rightarrow 0$ ", jo 
iepriekšējam virknes loceklim tad būtu jābūt $2015$, bet pirms tā izdarītajam 
*gājienam* jābūt " $6 \rightarrow 2$ ", kas noved pie tās pašas pretrunas kā 
(A) gadījumā.

**(C)** Skaitli $2016$ nevar iegūt pēc *gājiena* " $0 \rightarrow 1$ ", jo 
iepriekšējam virknes loceklim būtu jābūt $2015$, bet pirms tā izdarītajam 
*gājienam* jābūt " $2 \rightarrow 0$ " un skaitlim $2014$. Savukārt, pirms 
skaitļa $2014$ izdarītajam *gājienam* jābūt " $6 \rightarrow 2$ " un iegūstam 
līdzīgu pretrunu kā (A) gadījumā.

**(D)** Tātad skaitli $2016$ iegūst pēc *gājiena* " $1 \rightarrow 6$ ", un 
nākamie skaitļi virknē pēc *gājieniem* " $6 \rightarrow 2$ ", 
" $2 \rightarrow 0$ ", " $0 \rightarrow 1$ " un " $1 \rightarrow 6$ " ir 
skaitļi $2017,\ 2018,\ 2019$ un $2026$.
:::


## 3.uzdevums (LV.VOL.2014.9.4) {-}

Gatavojoties $13$ diplomātu apspriedei, krēsli tika izvietoti ap apaļu galdu 
vienādos attālumos un katrai no vietām tika sagatavota plāksnīte ar diplomāta 
vārdu. Diemžēl, ieņemot vietas pie galda, diplomāti šīs plāksnītes neņēma vērā 
un izrādījās, ka neviens no diplomātiem nav apsēdies pretī savai plāksnītei.

**(A)** Pierādīt: nepārsēdinot diplomātus, galdu ir iespējams pagriezt tā, ka 
vismaz divi diplomāti atradīsies pret savām plāksnītēm.  
**(B)** Pierādīt: ja sākumā tieši viens diplomāts būtu sēdējis pret savu 
plāksnīti, tad ir iespējams, ka viņi apsēdušies tā, ka, pagriežot galdu, nav 
iespējams panākt, ka pret savu plāksnīti atradīsies vairāk par vienu diplomātu.

::: solution
## Atrisinājums

**(A)** Apaļajam galdam pavisam ir $13$ derīgas pozīcijas, kuras var iegūt 
galda pagriešanas par noteiktu vietu skaitu rezultātā. Katrs diplomāts pret 
savu plāksnīti atradīsies tikai vienā no šīm pozīcijām. Katrai galda pozīcijai 
$i(1 \leq i \leq 13)$ ar $p_{i}$ apzīmējot diplomātu skaitu, cik šajā pozīcijā 
atrodas pret savām plāksnītēm, iegūstam $p_{1}+p_{2}+\ldots+p_{13}=13$.

Zināms, ka viena no $p_{i}$ vērtībām ir $0$, jo sākuma neviens no diplomātiem 
neatrodas pretī savai plāksnītei. Pēc Dirihlē principa kādai no atlikušajām 
$p_{j}$ vērtībām jābūt vismaz $2$, t. i., ir vismaz divi diplomāti, kas kādā 
pozīcijā atrodas pretī savām plāksnītēm.

**(B)** Pieņemot, ka diplomāti numurēti ar naturāliem skaitļiem no $1$ līdz 
$13$ pēc kārtas un sēdināt tos ap galdu bija paredzēts pulkstenrādītāja 
virzienā (plāksnītes saliktas $1-2-3-\ldots-12-13$), tad diplomātiem pie galda 
apsēžoties, piemēram, šādi $1-13-12-11-10-9-8-7-6-5-4-3-2$, izpildās uzdevumā 
prasītais. Diplomātiem $i$ un $j$, ja $i$ sēž savā vietā, tad $j$-tā plāksnīte 
atrodas $j-i$ vietas pa labi, bet $j$-ais diplomāts atrodas $j-i$ vietas pa 
kreisi. Tā kā $13$ ir nepāra skaitlis, tad $j$ nevar sēdēt pie savas 
plāksnītes.

*Piezīme.* Pavisam iespējami $13723$ atšķirīgi diplomātu izvietojuma varianti 
ar iepriekšminēto īpašību.
:::



## 4.uzdevums (LV.VOL.2013.9.4) {-}


Divas komandas savā starpā izspēlējušas vairākas (vairāk nekā vienu) spēles.
Par zaudējumu komanda saņem $n$ punktus ($n$- naturāls skaitlis), bet par uzvaru
$n+3$ punktus. Neizšķirtu rezultātu nav. Pēc spēļu beigām izrādījās, ka vienai
komandai ir par vienu uzvaru vairāk nekā otrai. Zināms, ka viena no komandām
kopsummā ieguva $92$ punktus. Cik punktus ieguva otra komanda?


::: solution
## Atrisinājums

Ja pieņemam, ka komanda-zaudētāja izcīnījusi $a$ uzvaras, tad komanda-uzvarētāja
izcīnījusi $a+1$ uzvaru. Kopējais punktu skaits komandai-zaudētājai ir
$a(n+3)+(a+1)n=2an+3a+n$, bet komandai-uzvarētājai $(a+1)(n+3)+an=2an+3a+n+3$.

Pierādīsim, ka komanda-uzvarētāja nevarēja izcīnīt $92$ punktus. Ja tā tomēr
būtu bijis, tad $2an+3a+n+3=92$ jeb eksistē tāds naturāls skaitlis $a$, ka
$n=\frac{89-3a}{2a+1}$ ir naturāls skaitlis. Tā kā $n \geq 1$, tad pieļaujamās
$a$ vērības ir $1 \leq a \leq 17$. Aplūkosim skaitītāja un saucēja vērtību
katrai no šīm vērtībām:

<!--
| $a$  | $89-3a$ | $2a+1$ |
| :--- | :------ | :----- |
| $1$  | $86$    | $3$    |
| $2$  | $83$    | $5$    |
| $3$  | $80$    | $7$    |
| $4$  | $77$    | $9$    |
| $5$  | $74$    | $11$   |
| $6$  | $71$    | $13$   |
| $7$  | $68$    | $15$   |
| $8$  | $65$    | $17$   |
| $9$  | $62$    | $19$   |
| $10$ | $59$    | $21$   |
| $11$ | $56$    | $23$   |
| $12$ | $53$    | $25$   |
| $13$ | $50$    | $27$   |
| $14$ | $47$    | $29$   |
| $15$ | $44$    | $31$   |
| $16$ | $41$    | $33$   |
| $17$ | $38$    | $35$   |
-->

Kā redzams, nevienai no pieļaujamajām $a$ vērtībām daļas vērtība nav naturāls
skaitlis. Tātad komanda-uzvarētāja nevar būt ieguvusi $92$ punktus.

Pārbaudīsim, vai komanda-zaudētāja varēja iegūt $92$ punktus. Tad $2an+3a+n=92$
un $n=\frac{92-3a}{2a+1}$. Ja $a=5$, tad $n=7$, vai, ja $a=8$, tad $n=4$, tātad,
komanda-zaudētāja varēja iegūt $92$ punktus.

Tā kā komanda-uzvarētāja ieguva par $3$ punktiem vairāk nekā komandu-zaudētāja,
tad otra komanda (uzvarētāja) ieguva $95$ punktus.
:::


## 5.uzdevums (LV.VOL.2018.9.5) {-}

Rindā izvietotas $2018$ monētas. Vienā gājienā drīkst paņemt vienu monētu, 
pārcelt to pāri tieši divām monētām un uzlikt to uz nākamās monētas. Vai $1009$
gājienos visas monētas iespējams savākt kaudzītēs pa divām monētām katrā 
kaudzītē?

![](LV.VOL.2018.9.5.png)

::: solution
## Atrisinājums

Pamatosim, ka prasītais ir iespējams. Ja ir $10$ monētas vai $8$ monētas, tad 
attiecīgi ar $5$ vai $4$ gājieniem tās var savākt kaudzītēs pa divām monētām 
katrā kaudzītē, skat., piemēram, 6.att. un 7.att. Tā kā $2018=201 \cdot 10+8$, 
tad ar $201 \cdot 5+4=1009$ gājieniem monētas iespējams savākt kaudzītēs pa 
divām monētām katrā kaudzītē.

![](LV.VOL.2018.9.5A.png)
::: 


## 6.uzdevums (LV.VOL.2017.9.5) {-}

Katra no bumbiņām, kas atrodas kastē, nokrāsota vienā no $N$ krāsām, un uz 
katras uzrakstīts naturāls skaitlis, kas nepārsniedz $N$. Zināms, ka katra no 
$N$ krāsām izmantota vismaz vienu reizi, tāpat arī katrs skaitlis, kas 
nepārsniedz $N$, izmantots vismaz vienu reizi. Kādām $N$ vērtībām kastē 
noteikti varēs atrast $N$ dažādu krāsu bumbiņas, uz kurām būs rakstīti $N$ 
dažādi skaitļi?


::: solution
## Atrisinājums

Ja $N=1$, tad kastē ir vismaz viena bumbiņa, kas nokrāsota vienīgajā 
iespējamajā krāsā un uz tās uzrakstīts skaitlis $1$. Tātad vērtība $N=1$ der.

Parādīsim, ja $N=2$, tad vienmēr var atrast divas bumbiņas, kam izpildās 
prasītās īpašības. Izvēlamies patvaļīgu bumbiņu. Tās krāsu apzīmējam ar 
$k_{1}$, bet skaitli, kas uz tās uzrakstīts - ar $s_{1}$. Ja kastē atrodas 
bumbiņa, kuras krāsa ir $k_{2}$ un uz kuras uzrakstīts skaitlis $s_{2}$, tad 
esam atraduši nepieciešamo bumbiņu pāri. Apskatīsim gadījumu, kad kastē nav 
bumbiņa, kuras krāsa ir $k_{2}$ un uz kuras uzrakstīts skaitlis $s_{2}$. Tā kā 
kastē ir divu dažādu krāsu bumbiņas, tad kastē ir jābūt bumbiņai, kuras krāsa 
ir $k_{2}$ un uz kuras uzrakstīts skaitlis $s_{1}$. Tā kā kastē ir bumbiņa, uz 
kuras uzrakstīts skaitlis $s_{2}$, tad kastē ir jābūt bumbiņai, kuras krāsa ir 
$k_{1}$ un uz kuras uzrakstīts skaitlis $s_{2}$. Tātad, kastē ir divas 
bumbiņas, kuru krāsas ir $k_{2}$ un $k_{1}$ un uz tām uzrakstītie skaitļi ir 
attiecīgi $s_{1}$ un $s_{2}$, kas veido nepieciešamo bumbiņu pāri.

Pamatosim, ka $N$ nevar būt lielāks kā $2$. Tabulā parādīts piemērs, kurā visas
uzdevumā minētās īpašības izpildās, bet nevar atrast $N$ dažādu krāsu bumbiņas,
uz kurām uzrakstīti visi skaitļi no $1$ līdz $N$.

![](LV.VOL.2017.9.5A.png)
::: 



## 7.uzdevums (LV.VOL.2004.9.4) {-}

Kvadrāts sastāv no $4 \times 4$ vienādām kvadrātiskām rūtiņām Andris pēc kārtas
novieto pa vienam tomim kādā vēl neaizņemtā rūtiņā saskaņā ar šādiem 
noteikumiem: pirmo torni viņš drīkst novietot patvaļīgā rūtiņā pēc savas 
izvēles, bet katru nākošo torni jānovieto tādā rūtiņā, kur to uzlikšanas brīdī 
apdraud nepāra skaits jau novietoto (divi torņi apdraud viens otru, ja tie abi 
atrodas vienā horizontālē vai vienā vertikālē un starp tiem nav citu torņu).

Kādu lielāko torņu daudzumu Andrim var izdoties novietot?

::: solution
## Atrisinājums

**(A)** var uzlikt $15$ torņus; skat., piem., 2.zīm.

![](LV.VOL.2004.9.4A.png)

**(B)** ja uzliktu $16$ torņus, tad tie būtu jānovieto arī visās stūra rūtiņās.
Bet to torni, kuru ievieto **pēdējā stūra rūtiņā**, uzlikšanas brīdī apdraud 
divi citi - pretruna.
:::



