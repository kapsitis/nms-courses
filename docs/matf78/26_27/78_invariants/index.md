---
layout: default
title: "7.2.temats: Invarianti: Kas saglabājas, veicot atļautos gājienus"
permalink: /matf78/26_27/78_invariants/


---
# 7.2.temats: Invarianti: Kas saglabājas, veicot atļautos gājienus

**Mērķis:** Kā lasīt uzdevumu, kā veidot jautājumam 
atbilstošu risinājuma struktūru. Kādus jautājumus sev 
uzdot pirms uzskatīt par atrisinātu. Kā analizēt vienkāršus 
6.-7.kl. olimpiāžu uzdevumus.
Matemātikā var izmantot jau zināmus vai izdomāt jaunus invariantus; 
tie veic līdzīgu lomu kā (enerģijas, masas, u.c.) nezūdamības 
likumi fizikā.

* **Uzdevumu lapa:** {% include doc_links.html url="/matf78/26_27/78_invariants/problems/" %}
* **1.nodarbības materiāls:** {% include doc_links.html url="/matf78/26_27/78_invariants/class1/" %}
* **2.nodarbības materiāls:** {% include doc_links.html url="/matf78/26_27/78_invariants/class2/" %}
{: .small}


* **Uzdevumu lapa:** {% include doc_links.html url="/matf78/26_27/78_invariants/problems/" %}
{: .small}

* SR: Procesam (gājienu vai pārveidojumu virknei) formulē invariantu un uzraksta neiespējamības pamatojumu ("invarianta vērtība sākumā nevar atšķirties no vērtības beigās").
Invariants var būt, piemēram, nemainīga izteiksme, nemainīgs atlikums vai 
kāds apgalvojums, kurš pārmaiņu gaitā saglabājas patiess.
* SR: Izvēlas piemērotu rūtiņu izkrāsošanu (šaha, joslu, trīs krāsu utml.) veidā, 
lai pamatotu pārklāšanas, figūriņu izgriešanas vai apstaigāšanas neiespējamību; 
formulē invariantu, kurš procesa laikā nemainās.
* SR: Pazīst monovariantu — lielumu, kas katrā gājienā tikai aug vai tikai dilst, lai pamatotu, ka process apstājas vai tā beigās izpildās kāda nevienādība.


Birkas: ParityInvariant, ColoringInvariant, ModularInvariant, MonovariantArgument, TilingByDominoesAndColoring; MTH_FixedInvariant, MTH_AuxiliaryColoring.


## SPARQL vaicājums 

Vaicājums glabājas failā [`problems.rq`](problems.rq); to izpilda ar

```
python nms-courses/scripts/select_problems.py \
       nms-courses/docs/matf78/26_27/78_invariants/problems.rq
```

```sparql
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

SELECT ?problemID ?grade ?diff
       (GROUP_CONCAT(DISTINCT ?family;       separator="+") AS ?families)
       (GROUP_CONCAT(DISTINCT ?domain;       separator="/") AS ?domains)
       (GROUP_CONCAT(DISTINCT ?questionType; separator="/") AS ?questionTypes)
       (GROUP_CONCAT(DISTINCT ?tag;          separator=",") AS ?tags)
WHERE {
  ?p a eliozo:Problem ;
     eliozo:problemID ?problemID ;
     eliozo:problemGrade ?grade ;
     eliozo:problemYear ?year ;
     eliozo:domain ?domain ;
     eliozo:questionType ?questionType ;
     eliozo:problemText ?text .
  OPTIONAL { ?p eliozo:_readingDifficulty ?diff }

  {
    { ?p eliozo:_hasSolutionConcept ?tag }
    UNION
    { ?p eliozo:_hasReasoningMethod ?tag }
    UNION
    { ?p eliozo:topic  ?topicIRI  . BIND(REPLACE(STR(?topicIRI),  "^.*#", "") AS ?tag) }
    UNION
    { ?p eliozo:method ?methodIRI . BIND(REPLACE(STR(?methodIRI), "^.*#", "") AS ?tag) }
  }

  FILTER (CONTAINS(?tag, "Invariant") || CONTAINS(?tag, "Monovariant")
          || ?tag = "ChessboardColoring" || ?tag = "ColoringProblems"
          || ?tag = "ColoringArgumentForCoverageOrUnreachability")

  BIND (
    IF (CONTAINS(?tag, "Monovariant"), "Mono",
    IF (CONTAINS(?tag, "Game"),        "Game",
    IF (CONTAINS(?tag, "Coloring"),    "Coloring",
    IF (CONTAINS(?tag, "Parity"),      "Parity",
                                       "Numeric")))) AS ?family )

  FILTER (LANGMATCHES(LANG(?text), "lv"))
  FILTER (?grade >= 6 && ?grade <= 9)
  FILTER (?year >= 2003 && ?year <= 2026)
  FILTER (?questionType != "ShortAnswer")
}
GROUP BY ?problemID ?grade ?diff
ORDER BY ?families ?grade ?problemID
```

**Kāpēc tieši tā atlasīts.**

* *Trīs birku slāņi, apvienoti ar `UNION`.* Invarianta ideja datubāzē ir
  ierakstīta trijās dažādās vietās: kā brīva teksta birka
  `eliozo:_hasSolutionConcept` (`Invariant`, `ParityInvariant`,
  `ChessboardColoring`, `Monovariant`), kā `eliozo:_hasReasoningMethod`
  (`FixedInvariantNumeric`, `InvariantMethod`, `ColoringInvariant`,
  `GameInvariantsInNT`, `ParameterizedInvariantValue`,
  `MonovariantStrictlyChangingQuantity`) un kā IRI zem `eliozo:topic` /
  `eliozo:method` (`InvariantParity`, `InvariantRemainder`, `GameInvariant`,
  `MTH_FixedInvariant`, `MTH_PeriodicInvariant`, `MTH_Monovariant`). Meklējot
  tikai vienā slānī, pazūd apmēram puse uzdevumu, tāpēc visi trīs tiek
  apvienoti vienā tekstiskā mainīgajā `?tag`. IRI slānis ir vienīgais, kas
  atrodams arī vecākos komplektos, kur LLM ģenerētās `_has*` birkas vēl nav
  pievienotas.
* *Kas apzināti netiek ņemts vērā.* Birkas `Tiling` un `Coloring` pašas par
  sevi norāda tikai to, ka uzdevumā kaut ko sagriež vai izkrāso — tur iekrīt
  arī sudoku, grafu krāsošana un parastie "sagriez figūru" uzdevumi, kuros
  nekāda invarianta nav. Palīgkrāsojumu kā *metodi* droši atpazīst tikai
  birkas `ChessboardColoring`, `ColoringInvariant`, `ColoringProblems` un
  `ColoringArgumentForCoverageOrUnreachability`. Šī sašaurināšana garo sarakstu
  samazina no $145$ uz $118$ uzdevumiem un izmet gandrīz tikai troksni.
* *`?family` — šķirošana pa invarianta tipiem.* Katrai birkai piekārto vienu no
  piecām saimēm (`Parity`, `Numeric`, `Coloring`, `Game`, `Mono`). Krāsojumu
  pārbauda pirms paritātes, jo krāsošanas uzdevumi gandrīz vienmēr nes līdzi
  arī `ParityInvariant` birku un citādi visi nonāktu nepareizā grupā. Tieši šī
  kolonna ļauj no viena vaicājuma izveidot abas nodarbības: 1. nodarbība ņem
  `Parity` un `Numeric`, 2. nodarbība — `Coloring`, `Game` un `Mono`.
* *Klašu un gadu robežas.* $6.-9.$ klase, nevis tikai $7.-8.$: $6.$ klases
  komplekti dod iesildīšanās uzdevumus ar to pašu ideju, bet mazākiem
  skaitļiem, savukārt $9.$ klases uzdevumi der spēcīgākajiem dalībniekiem un
  nākamajam gadam. Gadu intervāls $2003-2026$ aptver visu pieejamo LV.AMO un
  LV.NOL arhīvu.
* *`?questionType != "ShortAnswer"`.* Invarianta uzdevumā vērtīgais ir
  pierādījuma pieraksts, nevis skaitliskā atbilde; testa formāta uzdevumi šim
  tematam neder.
* *Kāpēc `?domain != "Geom"` šeit **netiek** izmantots* (atšķirībā no
  $1.$ temata): tieši rūtiņu un figūru uzdevumi ir palīgkrāsojuma dabiskā
  mājvieta, un to izmešana atņemtu visu $2.$ nodarbības materiālu.
* *Grupēšana pēc `?problemID`.* Vienam uzdevumam datubāzē mēdz būt vairākas
  `domain` un `questionType` vērtības (piem., `Alg` un `Comb`), tāpēc bez
  `GROUP BY` tas parādītos sarakstā divreiz.

## Atlasītie uzdevumu ID

Garais saraksts — $118$ uzdevumi, sagrupēti pēc vaicājuma kolonnas `?families`.

**Paritātes invariants** (20 uzd.)

* LV.AMO.2011.6.1
* LV.AMO.2012.6.4
* LV.AMO.2016.6.2
* LV.AMO.2017.6.4
* LV.NOL.2013.6.3
* LV.NOL.2024.6.5
* LV.AMO.2012.7.1
* LV.AMO.2017.7.4
* LV.AMO.2022A.7.5
* LV.AMO.2024.7.3
* LV.NOL.2004.7.1
* LV.NOL.2015.7.2
* LV.AMO.2012.8.5
* LV.AMO.2025.8.3
* LV.NOL.2008.8.1
* LV.NOL.2014.8.5
* LV.AMO.2006.9.5
* LV.AMO.2010.9.1
* LV.AMO.2023.9.5
* LV.AMO.2024.9.3

**Nemainīga izteiksme, summa vai atlikums** (72 uzd.)

* LV.AMO.2003.6.5
* LV.AMO.2005.6.3
* LV.AMO.2011.6.4
* LV.AMO.2012.6.1
* LV.AMO.2013.6.1
* LV.AMO.2014.6.4
* LV.AMO.2015.6.3
* LV.AMO.2015.6.5
* LV.AMO.2017.6.3
* LV.AMO.2019.6.2
* LV.AMO.2022A.6.2
* LV.AMO.2024.6.3
* LV.NOL.2011.6.1
* LV.NOL.2012.6.4
* LV.NOL.2013.6.2
* LV.NOL.2014.6.5
* LV.NOL.2015.6.2
* LV.NOL.2023.6.5
* LV.AMO.2003.7.2
* LV.AMO.2009.7.5
* LV.AMO.2010.7.4
* LV.AMO.2013.7.4
* LV.AMO.2017.7.2
* LV.AMO.2018.7.2
* LV.AMO.2018.7.5
* LV.AMO.2019.7.2
* LV.AMO.2022A.7.2
* LV.AMO.2022A.7.3
* LV.AMO.2023.7.5
* LV.NOL.2010.7.1
* LV.NOL.2013.7.4
* LV.NOL.2023.7.5
* LV.AMO.2003.8.4
* LV.AMO.2003.8.5
* LV.AMO.2004.8.5
* LV.AMO.2012.8.4
* LV.AMO.2018.8.2
* LV.AMO.2018.8.4
* LV.AMO.2019.8.2
* LV.AMO.2022A.8.2
* LV.AMO.2022B.8.4
* LV.AMO.2023.8.5
* LV.AMO.2024.8.3
* LV.NOL.2009.8.1
* LV.NOL.2010.8.3
* LV.NOL.2013.8.5
* LV.NOL.2015.8.2
* LV.NOL.2019.8.4
* LV.NOL.2021.8.1
* LV.AMO.2003.9.2
* LV.AMO.2008.9.4
* LV.AMO.2010.9.4
* LV.AMO.2011.9.3
* LV.AMO.2012.9.5
* LV.AMO.2013.9.1
* LV.AMO.2013.9.4
* LV.AMO.2014.9.5
* LV.AMO.2015.9.5
* LV.AMO.2016.9.4
* LV.AMO.2019.9.2
* LV.AMO.2019.9.4
* LV.AMO.2022A.9.2
* LV.AMO.2022B.9.4
* LV.AMO.2024.9.5
* LV.NOL.2004.9.4
* LV.NOL.2011.9.1
* LV.NOL.2011.9.3
* LV.NOL.2012.9.1
* LV.NOL.2012.9.5
* LV.NOL.2015.9.2
* LV.NOL.2015.9.5
* LV.NOL.2024.9.4

**Palīgkrāsojums** (16 uzd.)

* LV.AMO.2003.6.2
* LV.AMO.2004.6.2
* LV.AMO.2011.6.3
* LV.AMO.2012.6.3
* LV.AMO.2015.6.2
* LV.AMO.2022A.6.3
* LV.NOL.2015.6.4
* LV.NOL.2024.6.2
* LV.AMO.2015.7.2
* LV.AMO.2016.7.5
* LV.NOL.2015.7.3
* LV.AMO.2015.8.2
* LV.AMO.2024.8.5
* LV.AMO.2011.9.5
* LV.AMO.2015.9.2
* LV.AMO.2022B.9.5

**Invariants spēlē** (8 uzd.)

* LV.AMO.2003.7.3
* LV.AMO.2007.7.3
* LV.AMO.2022B.7.4
* LV.AMO.2011.8.5
* LV.AMO.2016.8.5
* LV.AMO.2003.9.5
* LV.AMO.2012.9.4
* LV.NOL.2006.9.5

**Monovariants** (2 uzd.)

* LV.AMO.2003.7.5
* LV.AMO.2023.9.1

## 1.nodarbības saturs

Pirmajā nodarbībā invariantu ievieš kā **skaitli, kas procesa laikā nemainās**.
Sākam ar gadījumiem, kur tas ir pats acīmredzamākais lielums — visu monētu
kopsumma vai uzrakstīto skaitļu summa —, un pierakstām trīs soļu shēmu:
(1) nosauc invariantu, (2) katram atļautā gājiena veidam parādi, ka tas
nemainās, (3) salīdzini vērtību sākumā un beigās. Tad pāriet uz gadījumiem, kur
nemainās nevis pats skaitlis, bet tā **atlikums**, dalot ar $2$, $3$ vai $4$:
"apēd $5$, pieliek $9$" tipa procesi, gabalu skaita maiņas, starpību summa pa
apli. Nodarbības beigās skolēni redz divus uzdevumus, kuros invariants nav
atrodams uzdevuma tekstā — jāizvēlas pašam, ko skaitīt (pirmreizinātāju skaitu,
vienas krāsas bumbiņu skaitu). Uzsveram arī robežu: invariants pierāda **tikai**
neiespējamību; ja atbilde ir "jā", papildus vajag konkrētu piemēru.

Šai nodarbībai specifiskie sasniedzamie rezultāti:

* SR: Procesa aprakstā atpazīst "gājienu" un pieraksta, par cik katrs gājiena
  veids maina izvēlēto lielumu; pārbauda **visus** gājienu veidus, nevis vienu.
* SR: Formulē invariantu kā apgalvojumu par atlikumu ("gabalu skaits vienmēr
  dalās ar $3$") un noslēdz spriedumu ar sākuma un beigu vērtības salīdzinājumu.
* SR: Atšķir situācijas, kurās invariants dod pilnu atbildi ("nevar"), no tām,
  kurās papildus jāuzrāda piemērs ("var").
* SR: Ja teksts nedod gatavu lielumu, izvēlas savu skaitāmo lielumu
  (pirmreizinātāju skaitu, vienas krāsas objektu skaitu) un pamato tā izvēli.

### Skaidrojamie piemēri

#### 1.1. LV.NOL.2015.8.2 — invarianta trīs soļu shēma

Autoservisā "Šrotiņš" ir $39$ mašīnas. Naskais Maigonis katra mēneša $20.$
datumā vai nu pārdod $7$ restaurētas mašīnas un to vietā nopērk $16$ vecas
mašīnas, vai arī $19$ mašīnas nodod metāllūžņos un to vietā nopērk $4$ vecas
mašīnas. Vai iespējams, ka "Šrotiņā" kāda mēneša $21.$ datumā būs tieši $2015$
mašīnas?

* *Saprašana:* "Vai iespējams" — ja atbilde ir "nē", vajag vispārīgu spriedumu,
  kas aptver **visas** iespējamās darbību virknes, ne tikai dažas.
* *Izpēte:* Uzraksti abus gājienus kā vienu skaitli: $-7+16 = +9$ un
  $-19+4 = -15$. Kas kopīgs skaitļiem $9$ un $15$?
* *Pārformulēšana:* Invariants: "mašīnu skaits vienmēr dalās ar $3$".
* *Risināšana:* (1) Sākumā $39$ dalās ar $3$. (2) $3k \pm 3m = 3(k \pm m)$,
  tātad pēc katra gājiena dalāmība saglabājas. (3) $2+0+1+5 = 8$ nedalās ar $3$,
  tātad $2015$ nav sasniedzams.
* *Atskats:* Vai spriedumā kaut kur tika izmantota gājienu **secība** vai
  **skaits**? Ja nē — tieši tāpēc arguments der visām virknēm uzreiz.

#### 1.2. LV.NOL.2023.7.5 — kad invarianta vien nepietiek

Kastē atrodas baltas, sarkanas un zaļas lodītes. Ar vienu gājienu var izņemt
divas dažādu krāsu lodītes un ielikt vienu trešās krāsas lodīti. Vai var
panākt, ka paliek tikai viena lodīte, ja sākumā ir **(A)** $10$ baltas, $12$
sarkanas, $16$ zaļas; **(B)** $10$ baltas, $12$ sarkanas, $15$ zaļas?

* *Saprašana:* Divas daļas — atbildes var būt dažādas, un katrai vajag savu
  pamatojuma veidu.
* *Izpēte:* Viens gājiens: divi skaiti $-1$, viens skaits $+1$. Tātad **visas
  trīs** paritātes mainās vienlaikus. Kas tad paliek nemainīgs? Jebkuru divu
  skaitu **starpība** pēc moduļa $2$.
* *Risināšana (A):* Sākumā visi trīs skaiti pāra — visas starpības pāra. Beigu
  stāvoklī $(1,0,0)$ divas starpības ir nepāra. Pretruna, tātad nevar.
* *Risināšana (B):* Paritātes $(\text{p}, \text{p}, \text{n})$ neizslēdz
  rezultātu $(0,0,1)$ — bet tas vēl nenozīmē, ka var! Jāuzrāda gājienu virkne:
  trīs gājieni *bs*, *bz*, *sz* samazina visus trīs skaitus par $1$; ar tiem
  nonāk pie $(1,3,6)$ un tālāk pabeidz ar rokām.
* *Atskats:* Formulē vienā teikumā, kāpēc invariants nekad nevar pierādīt "jā".

#### 1.3. LV.AMO.2024.7.3 — invariants, kas nav pats skaitlis

Skaitļu virknes pirmais loceklis ir $12$. Katru nākamo iegūst iepriekšējo vai
nu reizinot ar $2$ vai $3$, vai arī izdalot ar $2$ vai $3$ (ja dalās bez
atlikuma). Vai virknes $61.$ loceklis var būt $54$?

* *Izpēte:* Uzraksti dažus pirmos locekļus. Vai pats skaitlis aug vai dilst?
  Nē — tātad jāmeklē cits lielums.
* *Pārformulēšana:* Sadali pirmreizinātājos: $12 = 2 \cdot 2 \cdot 3$ (trīs
  reizinātāji), $54 = 2 \cdot 3 \cdot 3 \cdot 3$ (četri). Par cik mainās
  reizinātāju skaits vienā gājienā?
* *Risināšana:* Katrā gājienā $\pm 1$, tātad reizinātāju skaita **paritāte**
  mainās katrā solī. No $1.$ līdz $61.$ loceklim ir $60$ gājieni — pāra skaits,
  tātad $61.$ loceklim reizinātāju skaits ir nepāra, kā $12$. Bet $54$ tas ir
  pāra. Nevar.
* *Atskats:* Šeit invariants nav "lielums, kas nemainās", bet "lielums, kas
  mainās pilnīgi regulāri". Kāds ir vispārīgais secinājums par $n$-to locekli?

## 2.nodarbības saturs

Otrajā nodarbībā invariantu meklē tur, kur nav gatava skaitļa — rūtiņu lapā.
Galvenā ideja: **pats izvēlies krāsojumu** (šaha, joslu, trīs krāsu) un tad
skaiti vienas krāsas rūtiņas. Sākam ar domino un šaha galdiņu, kur katrs
kauliņš noklāj tieši vienu melnu un vienu baltu rūtiņu, un ar figūrām, kuras
neatkarīgi no pagrieziena vienmēr noklāj pāra skaitu melno rūtiņu; tad
parādām, ka tā pati doma der arī apstaigāšanas uzdevumos (varde maina rūtiņas
krāsu katrā lēcienā) un spēlēs, kur laukumu izkrāso uzvarošās un zaudējošās
pozīcijās. Nodarbības beigās ieviešam monovariantu — lielumu, kas tikai aug vai
tikai dilst — un to lieto novērtējumiem "ar mazāk nekā $k$ gājieniem nepietiek".
Visu laiku uzturam $1.$ nodarbībā ieviesto disciplīnu: krāsojums ir tikai
palīglīdzeklis, bet pierakstā joprojām jābūt invarianta formulējumam un sākuma
un beigu vērtības salīdzinājumam.

Šai nodarbībai specifiskie sasniedzamie rezultāti:

* SR: Izvēlas krāsojumu atbilstoši figūras formai (šaha — domino un pāra/nepāra
  uzdevumiem, joslu vai trīs krāsu — figūrām ar garumu $3$) un pamato izvēli.
* SR: Pārbauda figūras noklāto krāsu skaitu **visos** tās pagriezienos un
  spoguļattēlos, nevis vienā uzzīmētā novietojumā.
* SR: Spēles laukumu aizpilda ar uzvarošajām/zaudējošajām rūtiņām, analizējot
  spēli no beigām, un nolasa atbildi no sākumpozīcijas krāsas.
* SR: Atšķir invariantu (nemainās) no monovarianta (tikai aug vai tikai dilst)
  un zina, kādus secinājumus ļauj katrs no tiem.

### Skaidrojamie piemēri

#### 2.1. Klasiskais piemērs — trīs krāsu krāsojums

No $8 \times 8$ kvadrāta izgriež vienu rūtiņu. Vai atlikušās $63$ rūtiņas var
sagriezt $1 \times 3$ taisnstūrīšos? Kur jāizgriež rūtiņa, lai varētu šādi
sagriezt?

![](image05.png)

* *Saprašana:* $63 = 3 \cdot 21$, tātad laukums netraucē — vajadzīgs cits
  arguments.
* *Izpēte:* Šaha krāsojums nepalīdz, jo $1 \times 3$ figūra noklāj gan $2+1$,
  gan $1+2$ rūtiņas. Kāpēc der krāsojums **trīs** krāsās pa diagonālēm?
* *Pārformulēšana:* Katrs $1 \times 3$ taisnstūrītis noklāj tieši vienu $A$,
  vienu $B$ un vienu $C$ rūtiņu. Tātad invariants: noklāto $A$, $B$ un $C$
  skaitiem jābūt vienādiem.
* *Risināšana:* Saskaiti $A$, $B$, $C$ rūtiņas abos attēlā dotajos krāsojumos.
  Izgrieztajai rūtiņai jābūt tādā krāsā, kuras ir par vienu vairāk — un tas
  jāizpildās abiem krāsojumiem vienlaikus. Kuras rūtiņas tam atbilst?
* *Atskats:* Uzdevumā ir divas daļas: "kur var" (piemērs) un "citur nevar"
  (invariants). Vai atbildē ir abas?

#### 2.2. LV.AMO.2015.7.2 — figūras un melno rūtiņu paritāte

Vai taisnstūri ar izmēriem $7 \times 6$ rūtiņas var pārklāt ar 4.att.
redzamajām figūrām?

![](LV.AMO.2015.7.2.png)

* *Saprašana:* "Vai var" ar sagaidāmo atbildi "nē" — vajag spriedumu par visiem
  iespējamiem pārklājumiem uzreiz.
* *Izpēte:* Nokrāso taisnstūri šaha galdiņa veidā un saskaiti melnās rūtiņas:
  $7 \cdot 6 : 2 = 21$ — nepāra skaits.
* *Izpēte:* Katrai figūrai pārbaudi visus pagriezienus un spoguļattēlus: cik
  melnas rūtiņas tā noklāj? Katru reizi sanāk **pāra** skaits.
* *Risināšana:* Vairāku pāra skaitļu summa ir pāra, bet melno rūtiņu kopskaits
  ir $21$ — nepāra. Pretruna.
* *Atskats:* Piezīme risinājumā: der arī krāsojums joslās. Pārbaudi, vai ar to
  sanāk tas pats. Kāpēc šis pats spriedums bez izmaiņām strādā arī
  $10 \times 9$ taisnstūrim (LV.AMO.2015.8.2)?

#### 2.3. LV.AMO.2016.8.5 — krāsojums kā spēles invariants

Divi spēlētāji uz $N \times N$ laukuma pārvieto kauliņu no kreisā apakšējā
stūra: par vienu rūtiņu pa labi, par vienu uz augšu vai par divām pa diagonāli
uz augšu pa labi. Zaudē tas, kurš nevar izdarīt gājienu. Kurš uzvar, ja
**(A)** $N=7$, **(B)** $N=8$?

![](LV.AMO.2016.8.5.png)

* *Saprašana:* "Kurš uzvar" = nosaukt spēlētāju **un** aprakstīt stratēģiju,
  kas vienmēr strādā.
* *Izpēte:* Sāc no beigām. Labā augšējā rūtiņa ir zaudējoša ($Z$), jo no tās
  nav gājienu.
* *Pārformulēšana:* Rūtiņa ir uzvaroša ($U$), ja no tās var aiziet uz kādu $Z$;
  citādi tā ir $Z$. Tas ir krāsojums divās krāsās — un tas ir invariants:
  spēlētājs, kurš atstāj pretiniekam $Z$ rūtiņu, to var darīt vienmēr.
* *Risināšana:* Aizpildi $7 \times 7$ un $8 \times 8$ laukumu ar $U$ un $Z$.
  Abos gadījumos kreisā apakšējā rūtiņa iznāk $Z$ — uzvar otrais spēlētājs.
* *Atskats:* Vai stratēģijas aprakstā ir pateikts, ko otrais spēlētājs dara
  **katrā** pirmā spēlētāja gājienā? Vai spēle noteikti beidzas?
