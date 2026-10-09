# 7.3. Dirihlē princips

**Tvērums:**  
Vienkāršais Dirihlē princips ($n+1$ trusis $n$ būros) un vispārinātais
princips ($kn+1$ trusis $n$ būros $\Rightarrow$ kādā būrī vismaz $k+1$),
pierakstīts kā pierādījums no pretējā ("ja katrā būrī būtu ne vairāk kā $k$,
tad kopā būtu ne vairāk kā $kn$"). Galvenā prasme ir pašam izvēlēties
"būrus": krāsas, komplektus, atlikumu klases, skaitļu pārus vai grupas,
plaknes/rūtiņu lapas apgabalus. Tvērumā ietilpst arī tuvākie radinieki, kad
tie kalpo novērtējumam: vidējās vērtības spriedums ("kāds elements nav mazāks
par vidējo"), ekstremālais elements ("pat lētākās $4$ tortes maksā par daudz")
un optimizācijas uzdevumi "piemērs + novērtējums", kur novērtējumu iegūst,
sadalot laukumu nepārklājošos "būros".

Spriedumi pretējā virzienā — "ja $n$ objektus izvieto $n$ būros bez sadursmēm,
tad katrā būrī ir tieši viens", t.i., injektīvs attēlojums starp vienāda
izmēra kopām ir bijekcija — Latvijas olimpiāžu $7.-8.$ klases uzdevumos
praktiski neparādās. Tie atrodami $9.$ klases un vecākos komplektos
(atlikumu cikliskums [LV.VOL.2025.9.3](https://eliozo.dudajevagatve.lv/problem?problemid=LV.VOL.2025.9.3),
virknes periodiskums [LV.NOL.2005.9.5](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2005.9.5),
galda pagriezieni [LV.VOL.2014.9.4](https://eliozo.dudajevagatve.lv/problem?problemid=LV.VOL.2014.9.4)).
Tāpēc šajā tematā tos **neapskatām sistemātiski** — tikai kā "atskata"
piezīmi vienkāršos gadījumos — un atliekam uz $9.$ klases dalāmības un
atlikumu tematiem. Tāpat atliekam nepārtraukto (ģeometrisko) Dirihlē principu
ar attālumiem un laukumiem un grafu teoriju (Ramsija tipa uzdevumi, piem.
[LV.NOL.2010.8.5](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2010.8.5),
paliek tikai kā "pakāpiens uz augšu").

**Dažādu uzdevumu avoti:**

* `./nms-courses/avg-pulcins-2025/class03-pigeonhole/class03-pigeonhole.rst` —
  pulciņa teorija (vienkāršais un vispārinātais princips, vidējā vērtība) un
  klasiskie piemēri (zeķes, atlikumi, komplekti, punkti režģī).
* A. Engel. *Problem-Solving Strategies.* Springer, 1998, 4. nodaļa
  "The Box Principle".


## SPARQL vaicājums

Vaicājums glabājas failā [`problems.rq`](problems.rq); to izpilda ar

```
python nms-courses/scripts/select_problems.py \
       nms-courses/docs/matf78/26_27/78_pigeonhole/problems.rq
```

(Vajag `pyoxigraph`; tas ir uzstādīts virtuālajā vidē
`qualification-project/venv-eliozo`.)

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
    {
      { ?p eliozo:_hasSolutionConcept ?tag }
      UNION
      { ?p eliozo:_hasReasoningMethod ?tag }
      UNION
      { ?p eliozo:topic  ?topicIRI  . BIND(REPLACE(STR(?topicIRI),  "^.*#", "") AS ?tag) }
      UNION
      { ?p eliozo:method ?methodIRI . BIND(REPLACE(STR(?methodIRI), "^.*#", "") AS ?tag) }
      FILTER (REGEX(STR(?tag), "Pigeonhole|ExtremalElement|ExtremeElement|MeanValuePrinciple"))
    }
    UNION
    {
      ?p eliozo:problemSolution ?sol .
      ?sol eliozo:solutionText ?solText .
      FILTER (CONTAINS(STR(?solText), "Dirihl"))
      BIND ("SolutionMentionsDirichlet" AS ?tag)
    }
  }

  BIND (
    IF (REGEX(?tag, "Extrem|Mean"),                 "Extremal",
    IF (?tag = "SolutionMentionsDirichlet",         "Text",
    IF (?domain = "Geom" || CONTAINS(?tag, "Continuous"), "Geom",
                                                    "Basic"))) AS ?family )

  FILTER (LANGMATCHES(LANG(?text), "lv"))
  FILTER (?grade >= 6 && ?grade <= 9)
  FILTER (?year >= 2003 && ?year <= 2026)
  FILTER (?questionType != "ShortAnswer")
}
GROUP BY ?problemID ?grade ?diff
ORDER BY ?families ?grade ?problemID
```

**Kāpēc tieši tā atlasīts.**

* *Birku slāņi, apvienoti ar `UNION`.* Dirihlē princips datubāzē ierakstīts
  vairākos nosaukumos: `_hasSolutionConcept` (`PigeonholePrinciple`,
  `PigeonholePrincipleBasic`, `PigeonholePrincipleGeneralized`,
  `ExtremalElementArgument`), `_hasReasoningMethod` (`PigeonholeInNT`,
  `NumTheoryPigeonhole`, `NumTheoryExtremeElement`) un IRI zem
  `eliozo:method` (`MTH_PigeonholePrincipleBasic`,
  `MTH_PigeonholePrincipleGeneralized`, `MTH_ContinuousPigeonholePrinciple`,
  `MTH_ExtremeElements`, `MTH_MeanValuePrinciple`). Viens regulārs izteikums
  `Pigeonhole|ExtremalElement|ExtremeElement|MeanValuePrinciple` noķer tos
  visus. (Uzvednē minētās birkas `ParityInvariant`, `ColoringInvariant` u.c.
  attiecas uz iepriekšējo — invariantu — tematu, tāpēc šeit netiek lietotas.)
* *Atrisinājuma teksts kā otrais avots.* Daļai uzdevumu birku nav vai tās
  ir nepilnīgas, bet oficiālais atrisinājums tieši saka "pēc Dirihlē
  principa". Tāpēc otrā `UNION` zarā meklējam `eliozo:solutionText`, kas satur
  "Dirihl". Tā tika atrasts, piemēram, [LV.AMO.2025.8.4](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2025.8.4)
  (ķirbji), kuram nav nevienas Dirihlē birkas.
* *Kas apzināti netiek ņemts.* Birka `ArithmeticMean` pati par sevi
  (28 uzdevumi) apzīmē arī parastus vidējā aritmētiskā aprēķinus (vidējā
  atzīme, vidējais ātrums), kuros nav novērtējuma "kāds elements ir vismaz
  vidējais". Pārbaudot sarakstu, aptuveni puse no tiem bija `ShortAnswer`
  testa jautājumi, pārējie — vidējo vērtību aprēķini, vienādojumi un
  nevienādības (piem., LV.AMO.2012.8.3, LV.AMO.2017.9.2), tāpēc vidējās
  vērtības ideju ņemam tikai caur `MTH_MeanValuePrinciple`. Tāpat neņemam `CountingSumRule`,
  `DoubleCounting*` — tie ir kombinatorikas skaitīšanas paņēmieni, nevis
  Dirihlē princips.
* *`?family` — šķirošana pa "būru" veidiem.* `Basic` — būri ir krāsas,
  komplekti, atlikumi, skaitļu grupas (1. nodarbība); `Geom` — būri ir
  plaknes vai rūtiņu lapas daļas (2. nodarbība); `Extremal` — ekstremālais
  elements, vidējā vērtība (2. nodarbība); `Text` — atrasts tikai pēc
  atrisinājuma teksta.
* *Klašu un gadu robežas.* $6.-9.$ klase: $6.$ klases uzdevumi der
  iesildīšanai, $9.$ klases — spēcīgākajiem un nākamajam gadam (tur arī
  parādās no tvēruma atliktie "bijekcijas" spriedumi).
* *`?questionType != "ShortAnswer"`.* Dirihlē uzdevumā vērtīgs ir pamatojuma
  pieraksts, nevis skaitliska atbilde.

**Papildināts ar teksta meklēšanu.** Oxigraph krātuvē nav ielādēti visi
komplekti (piem., LV.NOL.2017-2018, LV.AMO.2025.9, LV.VOL.2025). Tāpēc
papildus izpildīta teksta meklēšana pēc "Dirihl" failos
`math/problembase/LV.*/*/content_lv.md` ($6.-9.$ klase); atrastie uzdevumi,
kuru vaicājuma rezultātā nav, ir uzskaitīti atsevišķi saraksta beigās.


## Atlasītie uzdevumu ID

Garais saraksts — $45$ uzdevumi no vaicājuma un $9$ no teksta meklēšanas,
sagrupēti pēc vaicājuma kolonnas `?families` (uzdevums ar vairākām saimēm
ierakstīts tajā, kur tas noderīgāks).

**Vienkāršais un vispārinātais princips: krāsas, komplekti, atlikumi, grupas** (25 uzd.)

* LV.AMO.2024.6.2
* LV.NOL.2021.6.3
* LV.AMO.2019.7.5
* LV.AMO.2023.7.1
* LV.AMO.2024.7.2
* LV.NOL.2014.7.5
* LV.NOL.2017.7.5
* LV.AMO.2019.8.5
* LV.AMO.2024.8.2
* LV.AMO.2025.8.4
* LV.NOL.2004.8.2
* LV.NOL.2006.8.3
* LV.NOL.2010.8.5
* LV.NOL.2013.8.5
* LV.NOL.2024.8.3
* LV.AMO.2006.9.5
* LV.AMO.2008.9.4
* LV.AMO.2023.9.4
* LV.AMO.2024.9.2
* LV.NOL.2005.9.5
* LV.NOL.2007.9.5
* LV.NOL.2011.9.5
* LV.NOL.2013.9.5
* LV.NOL.2021.9.5
* LV.VOL.2014.9.4

**Ģeometriskie "būri": plaknes daļas, rūtiņu bloki** (10 uzd.)

* LV.AMO.2011.7.5
* LV.AMO.2014.7.5
* LV.NOL.2011.7.4
* LV.NOL.2012.7.5
* LV.NOL.2013.7.3
* LV.NOL.2013.7.5
* LV.AMO.2018.8.5
* LV.AMO.2013.9.2
* LV.AMO.2018.9.5
* LV.AMO.2022A.9.5

(LV.NOL.2012.7.5 un LV.NOL.2013.7.5 ir viens un tas pats uzdevums.)

**Ekstremālais elements un vidējā vērtība** (10 uzd.)

* LV.NOL.2024.7.5
* LV.NOL.2024.8.4
* LV.AMO.2023.6.5
* LV.NOL.2010.7.4
* LV.VOL.2023.9.5
* LV.AMO.2013.7.1
* LV.NOL.2005.7.4
* LV.NOL.2016.7.5
* LV.AMO.2015.8.4
* LV.VOL.2024.9.1

(Pēdējie pieci ir vāji kandidāti: ekstremālais elements lietots
nevienādībai vai piemēra konstruēšanai, bez Dirihlē principa; trepēs tie
netiek izmantoti.)

**Teksta meklēšanas papildinājums — nav Oxigraph krātuvē** (9 uzd.)

* LV.NOL.2007.6.5
* LV.NOL.2018.6.2
* LV.NOL.2018.7.2
* LV.NOL.2018.8.2
* LV.NOL.2017.9.5
* LV.NOL.2018.9.2
* LV.AMO.2025.9.5
* LV.VOL.2018.9.2
* LV.VOL.2025.9.3
