## 78INV_invariants

**Virsraksts:** Atrisinājumu struktūras: Uzdotajam jautājumam atbilstoša atbilde

**Tvērums:** Izmantot invariantus neiespējamības pierādījumos. 
Ja invarianti izmantoti kā vairāksoļu procesa pētīšanas sastāvdaļa, 
līdzīgi kā saglabāšanās jeb nezūdamības likumi fizikā, tad apskatām arī tos.
Laukumi, tilpumi un masa parasti netiek aplūkoti šajā sadaļā, izņemot tad, 
ja tie palīdz analizēt  kombinatoriku, algoritmus vai spēles.


**Dažādu uzdevumu avoti:** 

* ./nms-courses/docs/matf78/26_27/78_invariants/legacy problems.md - dažādi par invariantiem
* ./nms-courses/avg-pulcins-2026/class19-cutting-square-grid/ - krāsošanas invariantu uzdevumi

[LV.AMO.2022A.7.2](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2022A.7.2) un [LV.AMO.2022A.8.2](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2022A.8.2)
(gabalu skaita paritāte procesā), 
[LV.AMO.2024.7.3](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2024.7.3) 
(virkne ar ×2, ×3, :2, :3), 
[LV.NOL.2023.7.5](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2023.7.5)
(lodīšu krāsu maiņa — atlikuma invariants).

 
## 1. Motivācija

Invarianti plaši izmantojami neiespējamības pamatošanai vai pierādījumiem 
no pretējā. Tipisks veids, kā pamatot neiespējamību, ir formulēt kādu 
izteiksmi (vai apgalvojumu), kurš paliek nemainīgs arī veicot daudzveidīgus 
soļus. 
Olimpiāžu matemātikā invariants parasti attēlojams nevis kā 
konkrēts matemātikas rezultāts jeb teorēma, uz kuru var atsaukties, bet 
veids kā saprotami izstāstīt pierādījumu atbilstoši shēmai: 

* Analīze/izpēte: Formulējam invarianta izteiksmi vai apgalvojumu.
* Risināšana: Katram atļauto soļu vai pārveidojumu tipam parādām, ka 
  invariants saglabājas nemainīgs. Ja vajadzīgs, ar matemātisko indukciju secinām, ka 
  invariants saglabājas arī pēc daudziem šādiem soļiem. 
* Salīdzinām invarianta stāvokli risināšanas sākumā un beigās. Ja tie 
  atšķiras, tad esam ieguvuši pretrunu. 

Invarianti var būt ne tikai neiespējamības pierādījumos, bet arī citās 
situācijās, ja analīzei noder kāds "saglabāšanās/nezūdamības" likums. 



## 2. Sasniedzamie rezultāti

* SR: Procesam (gājienu vai pārveidojumu virknei) formulē invariantu un uzraksta neiespējamības pamatojumu ("invarianta vērtība sākumā nevar atšķirties no vērtības beigās").
Invariants var būt, piemēram, nemainīga izteiksme, nemainīgs atlikums vai 
kāds apgalvojums, kurš pārmaiņu gaitā saglabājas patiess.
* SR: Izvēlas piemērotu rūtiņu izkrāsošanu (šaha, joslu, trīs krāsu utml.) veidā, 
lai pamatotu pārklāšanas, figūriņu izgriešanas vai apstaigāšanas neiespējamību; 
formulē invariantu, kurš procesa laikā nemainās.
* SR: Pazīst monovariantu — lielumu, kas katrā gājienā tikai aug vai tikai dilst, lai pamatotu, ka process apstājas vai tā beigās izpildās kāda nevienādība.



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












