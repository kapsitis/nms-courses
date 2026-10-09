---
layout: default
title: "7.3.temats: Dirihlē princips: Kad (trušu) sadursmes ir neizbēgamas"
permalink: /matf78/26_27/78_pigeonhole/
---
# 7.3.temats. Dirihlē princips: Kad (trušu) sadursmes ir neizbēgamas

**Mērķis:** Izmantot Dirihlē principu (un līdzīgus spriedumus ar kopu elementu skaitu),
lai pamatotu kādu novērtējumu vai kādas situācijas neizbēgamību. 
Piemēram to, ka vismaz vienā kastē nonāk vismaz divi objekti, 
vai vismaz vienā kastē nonāk ne mazāk kā noteikts skaits objektu. 
Izmantot to kopā ar vidējās vērtības, ekstremālā elementa metodi vai pierādījumos no pretējā.

* **Uzdevumu lapa:** {% include doc_links.html url="/matf78/26_27/78_pigeonhole/problems/" %}
* **1.nodarbības materiāls:** {% include doc_links.html url="/matf78/26_27/78_pigeonhole/class1/" %}
* **2.nodarbības materiāls:** {% include doc_links.html url="/matf78/26_27/78_pigeonhole/class2/" %}
{: .small}

* SR: Lieto vienkāršo un vispārināto Dirihlē principu, patstāvīgi izvēloties 
  "trušus" un "kastes" (atlikumu klases, krāsas, plaknes apgabalus, u.c.).
* SR: Sāk spriedumu no ekstremālā elementa ("aplūkojam lētāko / lielāko / malējo..."), 
  lai iegūtu novērtējumu, balstoties uz elementu skaitu kopā.
* SR: Optimizācijas uzdevumos ("atrast lielāko ...") — konstruē piemēru 
  un ar Dirihlē principu pierāda, ka to nevar uzlabot.

**Daži piemēri:** 

* [LV.NOL.2024.7.5](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2024.7.5), 
* [LV.NOL.2024.8.4](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2024.8.4) (toršu pirkšana — ekstremālais elements + novērtējums), 
* [LV.NOL.2024.8.3](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2024.8.3) (punkti režģī — Dirihlē pa rindām).



## 1.nodarbības saturs

Pirmajā nodarbībā formulējam **vienkāršo** ("ja $n+1$ trusis ir $n$ būros,
tad kādā būrī ir vismaz divi truši") un **vispārināto** Dirihlē principu
("ja vairāk nekā $kn$ truši ir $n$ būros, tad kādā būrī ir vismaz $k+1$
trusis") un to pierakstu kā pierādījumu no pretējā: "ja katrā būrī būtu ne
vairāk kā $k$, tad kopā būtu ne vairāk kā $k \cdot n$ — pretruna". Sākam ar
uzdevumiem, kuros būri ir redzami tekstā (krāsas, kori, atzīmes), tad pārejam
pie tiem, kuros būri jāizveido pašam: komplektu saraksts, ciparu grupas,
blakus esošu skaitļu pāri. Otrs nodarbības pavediens ir uzdevumi "kāds mazākais
skaits jāizvelk, lai noteikti...": atbilde sastāv no **divām daļām** —
Dirihlē novērtējuma ("ar $N$ pietiek") un sliktākā gadījuma piemēra
("ar $N-1$ var nepietikt"). Nodarbības beigās — uzdevumi, kuros Dirihlē
princips ir tikai viens solis garākā spriedumā (atlikumi, ekstremālais
elements).

Šai nodarbībai specifiskie sasniedzamie rezultāti:

* SR: Uzdevuma tekstā atpazīst "trušus" un "būrus" un pieraksta
  vispārināto principu kā nevienādību $k \cdot n < N$ (pierādījums no pretējā).
* SR: Ja būri nav doti, tos konstruē pats — uzskaita visus iespējamos
  komplektus vai sadala objektus grupās tā, lai **divi objekti vienā grupā
  jau dod vajadzīgo** īpašību.
* SR: Uzdevumos "kāds mazākais skaits jāizvelk" uzraksta abas daļas:
  novērtējumu ar Dirihlē principu un piemēru (sliktāko gadījumu), kas parāda,
  ka ar par vienu mazāk nepietiek.
* SR: Atšķir apgalvojumus "noteikti ir" (vajag pierādījumu visiem
  gadījumiem) un "var gadīties" (pietiek ar vienu piemēru).

### Skaidrojamie piemēri

#### 1.1. LV.AMO.2024.7.2 — būri ir visi iespējamie komplekti

Jurģis Miķeļdienas tirgū ar izlozes palīdzību izdalīja $11$ balvas. Katra
balva satur $6$ rudens labumus: ābolus, bumbierus un bietes. Pie tam zināms,
ka katra balva satur vismaz vienu ābolu, bumbieri un bieti. Pamatot, ka
noteikti tika izdalītas divas tādas balvas, kurām bija vienāds saturs.

* *Saprašana:* Kas ir "trusis" un kas ir "būris"? Truši — $11$ balvas, būri —
  dažādie iespējamie balvu saturi. Ja būru ir mazāk par $11$, esam galā.
* *Izpēte:* Cik veidos $6$ var izteikt kā trīs naturālu saskaitāmo summu?
  $4+1+1$, $3+2+1$, $2+2+2$ — bet secība ir svarīga (kurš auglis ir $4$?).
* *Risināšana:* Saskaiti sistemātiski: $4+1+1$ dod $3$ komplektus, $3+2+1$ —
  $6$ komplektus, $2+2+2$ — $1$ komplektu; kopā $10$ būri. $11 > 10$, tātad
  pēc Dirihlē principa divas balvas ir vienādas.
* *Atskats:* Pieraksta kvalitāte ir atkarīga no tā, vai komplektu saraksts ir
  **pilnīgs** un bez atkārtojumiem. Kā to pārliecinoši parādīt (tabula,
  sakārtošana pēc ābolu skaita)?

#### 1.2. LV.NOL.2021.6.3 — būrus izveido pats; novērtējums + piemērs

Dotas deviņas kārtis ar cipariem no $1$ līdz $9$, uz katras kārts uzrakstīts
atšķirīgs cipars. Kāds mazākais skaits kāršu jāizvelk (nezinot to vērtības),
lai no tām noteikti varētu izveidot divciparu skaitli, kurš dalās ar $7$
(veidojot divciparu skaitli, katru kārti drīkst izmantot ne vairāk kā vienu
reizi)?

* *Izpēte:* Izraksti divciparu skaitļus, kas dalās ar $7$ un kuros nav ciparu
  $0$ un nav divu vienādu ciparu: $14, 21, 28, 35, 42, 49, 56, 63, 84, 91, 98$.
  Kuri cipari "sadraudzējas"?
* *Pārformulēšana:* Sadali ciparus grupās tā, lai **jebkuri divi** vienas
  grupas cipari veido derīgu skaitli: $\{1,2,4\}$, $\{3,5,6\}$, $\{8,9\}$,
  $\{7\}$. Četras grupas — četri būri.
* *Risināšana:* Ja izvelk $5$ kārtis, tad pēc Dirihlē principa divas ir no
  vienas grupas — der. Ar $4$ kārtīm var nepietikt: $1, 3, 7, 8$ (pārbaudi
  visus $6$ pārus!).
* *Atskats:* Atbildē "mazākais skaits ir $5$" ir divi apgalvojumi. Kurš
  no tiem izmanto Dirihlē principu un kurš — piemēru? Kā atradām piemēru?
  (Pa vienam ciparam no katras grupas.)

#### 1.3. LV.AMO.2024.9.2 — vispārinātais princips un būru apvienošana

Katrs no $28$ klases skolēniem kontroldarbā saņēma atzīmi, kas ir vesels
skaitlis robežās no $0$ līdz $10$ ballēm. Pamatot, ka vai nu vismaz $4$
skolēniem ir vienāda atzīme, vai arī vismaz $4$ skolēni ieguva atzīmi, kas
ir augstāka nekā $7$.

* *Saprašana:* Ja par būriem ņem visas $11$ atzīmes, tad $28 \le 3 \cdot 11$,
  un Dirihlē princips neko nedod. Kāpēc uzdevumā ir otrā iespēja
  ("augstāka nekā $7$")?
* *Pārformulēšana:* Apvieno atzīmes $8$, $9$ un $10$ vienā būrī. Tagad būru
  ir $9$: atzīmes $0, 1, \ldots, 7$ un "augstāk par $7$".
* *Risināšana:* $28 > 3 \cdot 9 = 27$, tātad kādā būrī ir vismaz $4$
  skolēni. Ja tas ir viens no pirmajiem astoņiem — $4$ vienādas atzīmes; ja
  pēdējais — $4$ skolēni ar atzīmi virs $7$.
* *Atskats:* Būru skaits ir jāpielāgo trušu skaitam: $28 = 3 \cdot 9 + 1$.
  Cik būriem pietiktu, ja skolēnu būtu $25$?


## 2.nodarbības saturs

Otrajā nodarbībā Dirihlē princips kalpo **novērtējumam**. Pirmkārt,
**ekstremālais elements**: "pat $4$ lētākās tortes maksā vairāk nekā $85$
eiro, tātad neviens nevar nopirkt $4$ tortes" — un tad Dirihlē princips
pabeidz spriedumu. Otrkārt, **vidējā vērtība**: ja $n$ skaitļu summa ir $S$,
tad kāds no tiem ir vismaz $S/n$ (un, ja skaitļi ir veseli, — vismaz
$S/n$, noapaļots uz augšu). Treškārt, **rūtiņu lapas un figūras**: būri ir
nepārklājošas daļas ($2 \times 2$ kvadrātiņi, rindas, trijstūri). Optimizācijas
uzdevumos "kāds mazākais/lielākais" atbilde vienmēr ir **piemērs +
novērtējums**, un novērtējumu iegūst, sadalot laukumu tieši tik daudzos
būros, cik prasa piemērs. Nodarbības beigās — uzdevumi, kuros Dirihlē
principu jākombinē ar gadījumu analīzi, alkatīgu algoritmu vai grafiem.

Šai nodarbībai specifiskie sasniedzamie rezultāti:

* SR: Sāk spriedumu ar ekstremālo elementu ("aplūkojam lētākās / mazākās /
  lielāko ...") un no tā iegūst ierobežojumu, ko pabeidz ar Dirihlē principu.
* SR: Lieto vidējās vērtības spriedumu, saskaitot vienu un to pašu summu
  divos veidos (katrs elements tiek ieskaitīts vienādi daudz reižu).
* SR: Optimizācijas uzdevumā sadala rūtiņu laukumu nepārklājošās daļās tā,
  lai katrā daļā "jābūt vismaz vienam"; daļu skaits sakrīt ar piemēra
  vērtību.
* SR: Pārbauda, ka izvēlētie būri tiešām **nepārklājas** un katrs objekts
  pieder tieši vienam būrim.

### Skaidrojamie piemēri

#### 2.1. LV.NOL.2024.7.5 — ekstremālais elements + Dirihlē

Konditorejā nopērkamas $10$ tortes, to cena ir attiecīgi $20; 21; 22; \ldots;
29$ eiro (katra torte ir tieši vienā eksemplārā). Konditorejā viens pēc otra
iegriezās $3$ gardēži, katrs no tiem nopirka sev dažas tortes, turklāt katrs
iztērēja ne vairāk kā $85$ eiro. Pierādīt, ka pēc gardēžu apmeklējuma vismaz
viena torte vēl palika nenopirkta!

* *Izpēte:* Cik tortes var nopirkt viens gardēdis? Lai to noskaidrotu,
  aplūko **lētākās** tortes: $20+21+22+23 = 86 > 85$.
* *Risināšana (no pretējā):* Ja visas $10$ tortes nopirktas, tad
  $10 = 3 \cdot 3 + 1$ un pēc Dirihlē principa kāds gardēdis nopircis vismaz
  $4$ tortes — bet tās maksā vismaz $86$ eiro. Pretruna.
* *Risināšana (tieši):* Katrs nopirka ne vairāk kā $3$ tortes, kopā ne vairāk
  kā $9 < 10$.
* *Atskats:* Kāpēc pietiek aplūkot tieši **lētākās** $4$ tortes, nevis
  visas iespējamās četrinieku izvēles? Pārbaudi to pašu spriedumu uzdevumā
  LV.NOL.2024.8.4 ($16$ tortes, $5$ gardēži, $125$ eiro).

#### 2.2. LV.NOL.2011.7.4 — rūtiņu bloki kā būri; piemērs + novērtējums

Vai $8 \times 8$ rūtiņas lielā kvadrātā var aizkrāsot **(A)** $16$ rūtiņas,
**(B)** $17$ rūtiņas tā, ka nekādas divas aizkrāsotās rūtiņas neatrodas
blakus? (Par blakus rūtiņām sauksim rūtiņas, kurām ir kopīgs vismaz viens
punkts.)

* *Izpēte:* Mēģini aizkrāsot pēc iespējas vairāk rūtiņu. Kāds raksts rodas?
  (Katra otrā rūtiņa katrā otrajā rindā.)
* *Pārformulēšana:* Kurās figūrās var būt **ne vairāk kā viena** aizkrāsota
  rūtiņa? Jebkuras divas $2 \times 2$ kvadrātiņa rūtiņas ir blakus.
* *Risināšana:* (A) Var — piemēram, visas rūtiņas, kuru rindas un kolonnas
  numuri abi ir nepāra. (B) Sadala kvadrātu $16$ kvadrātiņos $2 \times 2$;
  $17 > 16$, tātad kādā kvadrātiņā ir divas aizkrāsotas rūtiņas — tās ir
  blakus. Nevar.
* *Atskats:* Piemērā $16$ rūtiņu katrā $2 \times 2$ kvadrātiņā ir **tieši
  viena** aizkrāsota rūtiņa. Tā ir pazīme, ka būri izvēlēti pareizi —
  novērtējums un piemērs "satiekas".

#### 2.3. LV.AMO.2024.8.2 — vidējās vērtības spriedums

Pa apli patvaļīgā secībā sarakstīti visi naturālie skaitļi no $1$ līdz $10$.
Pamatot, ka noteikti var atrast tādus trīs secīgus skaitļus, kuru summa būs
vismaz $17$.

* *Saprašana:* Cik ir trīs secīgu skaitļu trijnieku pa apli? Tieši $10$ —
  katrs skaitlis ir pirmais vienā trijniekā.
* *Izpēte:* Saskaiti visu $10$ trijnieku summas kopā. Cik reizes tajā
  ieskaitīts katrs skaitlis? Trīs reizes, tātad kopsumma ir
  $3 \cdot (1+2+\ldots+10) = 165$.
* *Risināšana:* Ja katra trijnieka summa būtu ne lielāka par $16$, kopsumma
  nepārsniegtu $160 < 165$. Pretruna. (Citiem vārdiem: vidējā trijnieka summa
  ir $16{,}5$, tātad kāda summa ir vismaz $17$.)
* *Atskats:* Šeit "truši" ir $165$ vienības, bet "būri" — $10$ trijnieki.
  Kāpēc iegūtais novērtējums ir $17$, nevis $16{,}5$?
