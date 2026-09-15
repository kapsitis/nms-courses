# Kartiņa par 7.-8.kl. tematu: Atrisinājumu struktūras

**Virsraksts:** Atrisinājumu struktūras: Uzdotajam jautājumam atbilstoša atbilde

**Tvērums:** Kā lasīt uzdevumu, kā veidot jautājumam atbilstošu 
risinājuma struktūru. Kādus jautājumus sev uzdot pirms uzskatīt 
par atrisinātu. Kā analizēt vienkāršus 6.-7.kl. olimpiāžu uzdevumus. 

## Sasniedzamie rezultāti

SR: Atšķir olimpiāžu jautājumu pamattipus — “atrast visus”, “vai var?”, “lielākā/mazākā vērtība”, “pierādīt”, “konstruēt piemēru” (arī “aprakstīt procedūru/spēles stratēģiju”). Zina katram atbilstošo pilnas atbildes struktūru (piem., “atrast visus” = atrast + pamatot, ka citu nav).
SR: Apgalvojumu “var/eksistē” pamato ar konkrētu piemēru, bet “nevar/vienmēr” — ar vispārīgu spriedumu; optimizācijas uzdevumā uzraksta (konkrētu) optimālo piemēru un (vispārīgu) neiespējamību to uzlabot.
SR: Sistemātiski izmanto mazos gadījumus un sakārtotu pilno pārlasi; pieraksta gadījumus tā, lai lasītājam viegli pārliecināties, ka nekas nav izlaists.
SR: Izmanto secību: Saprast (tekstu), izpētīt (uzdevuma modeli), īstenot (risināšanas plānu), atskatīties (uz risinājumu). (En: Understand → Explore → Attack → Review.). Ar lietvārdiem: Saprašana → Izpēte → Pārformulēšana → Risināšana → Atskats.
SR: Atbildes rakstiska noformēšana: Uzdevumi ar apakšgadījumiem, atrisinājumi vairākās daļās, skaidrība, cik tālu uzrakstīts risinājums.



## 1. Motivācija 

* (Zeitz 2006). Ar ko uzdevumi atšķiras no piemēriem: 
  Piemēriem ir zināms, uz kuru jomu tie attiecas, ir zināma 
  procedūra, kā tos rēķināt (aprēķina piemērs par ātrumu un laiku, kurš 
  ir piemērs, lai arī saucas "teksta uzdevums"). 
  Uzdevumiem šādas vienotas procedūras nav.
  Apsveikšana dzimšanas dienā ir piemērs vai uzdevums?
  Uzdevuma risināšanas plāns jāveido risinātājam pašam.
* Sacerējumam jāatbilst uzdotajam tematam. 
* Jāvar piebremzēt vēlmi teikt pirmo, kas ienāk prātā. 
  "Sērkociņu kastīte un šķiltavas kopā maksā 1 eiro un 10 centus.
  Šķiltavas ir par 1 eiro dārgākas nekā sērkociņi. 
  Cik maksā sērkociņi un cik - šķiltavas?"

**Kāpēc to mācīties?** Jautājuma veids nosaka, kāda atbilde ir pietiekama, — 
un tā ir arī ārpus matemātikas. Ja draugs jautā *"Vai sestdien vari atnākt?"*, 
pietiek atrast vienu brīvu stundu. Ja treneris jautā *"Vai vari trenēties 
jebkurā nedēļas dienā?"*, jāpārbauda viss grafiks, un pietiek ar vienu 
aizņemtu dienu, lai godīgā atbilde būtu "nē". Ja apgalvo *"Lētāk par 25 eiro 
šīs austiņas nekur nopirkt nevar"*, nepietiek parādīt vienu veikalu ar šādu 
cenu — jāpārliecinās, ka arī citos veikalos lētāk nav (piemērs + pamatojums, 
ka labāk nevar). Programmētājs zina, ka viens veiksmīgs tests nepierāda, ka 
programma strādās vienmēr. Kontroldarbā garš risinājums, kas atbild uz citu 
jautājumu, dabū maz punktu — tāpat kā sacerējums par citu tēmu. Olimpiādē, 
eksāmenā, darba intervijā vai strīdā ar draugiem pārliecina tas, kurš atbild 
tieši uz uzdoto jautājumu un pamato visu, kas jāpamato, nevis tikai to, ko 
bija viegli pamanīt.


## 2. Uzdevumu atlases SPARQL

Vaicājums izpildīts lokālajā Oxigraph krātuvē (`$env:OXIGRAPH_DB_PATH`, 
ielādēti `docs/RDF_DATA/*.ttl`). To pašu vaicājumu izpilda skripts 
[select_problems.py](select_problems.py) (vajag Python vidi ar `pyoxigraph>=0.5`; 
krātuvi atver tikai lasīšanai):

```sparql
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemID ?questionType ?domain (STRLEN(?text) AS ?len) ?text
WHERE {
  ?p a eliozo:Problem ;
     eliozo:problemID ?problemID ;
     eliozo:problemGrade ?grade ;
     eliozo:problemYear ?year ;
     eliozo:questionType ?questionType ;
     eliozo:domain ?domain ;
     eliozo:_readingDifficulty "low" ;
     eliozo:problemText ?text .
  FILTER (LANGMATCHES(LANG(?text), "lv"))
  FILTER (?grade >= 5 && ?grade <= 7)
  FILTER (?year >= 2011 && ?year <= 2026)
  FILTER (?questionType != "ShortAnswer")
  FILTER (?domain != "Geom")
  FILTER (STRLEN(?text) <= 220)
  FILTER (!CONTAINS(?text, "![") && !CONTAINS(?text, "att.") && !CONTAINS(?text, "zīm.")
          && !CONTAINS(?text, "frac") && !CONTAINS(?text, "sqrt") && !CONTAINS(?text, "^"))
}
ORDER BY ?questionType ?len ?problemID
```

Filtru pamatojums:

* **Īsi teksti:** 5.-7. klases uzdevumu (2011-2026, 506 uzdevumi) vidējais 
  teksta garums ir ~266 zīmes; atstāti uzdevumi ar ≤ 220 zīmēm.
* **Viegli lasāmi:** `_readingDifficulty "low"`; tikai latviešu teksti 
  (2022. un 2023. gadam krātuvē ir arī angļu tulkojumi, kas citādi dublētos).
* **Vienkāršas priekšzināšanas:** izslēgti uzdevumi, kam vienīgā domēna birka 
  ir ģeometrija (`Geom`), uzdevumi ar zīmējumiem (`![`, "att.", "zīm.") 
  un ar daļskaitļiem, saknēm, pakāpēm.
* **Jautājuma tips ar pamatojumu:** izslēgti NOL `ShortAnswer` 
  (izvēles atbilžu jautājumi bez rakstiska pamatojuma).

Rezultāts: 50 uzdevumi — `ProveDisprove` 22, `FindExample` 9, `FindAll` 7, 
`FindCount` 7, `FindOptimal` 3, `Prove` 2. Tips `Algorithm` ("parādīt, kā" / 
stratēģija) atlasē neparādās: nevienam 5.-7. kl. šī tipa uzdevumam nav 
`_readingDifficulty "low"`, un visi teksti ir garāki par 270 zīmēm 
(īsākie: LV.AMO.2015.5.5, LV.NOL.2016.7.4, LV.NOL.2019.7.2).


## 3. Atlasīto uzdevumu numuri

Skripta `select_problems.py` izvade (sakārtota pēc `questionType`, tad pēc teksta garuma):

```
LV.AMO.2016.5.1
LV.AMO.2018.7.4
LV.AMO.2015.5.4
LV.AMO.2015.7.1
LV.NOL.2014.5.3
LV.NOL.2015.6.5
LV.AMO.2022A.6.4
LV.AMO.2018.7.1
LV.NOL.2011.7.2
LV.NOL.2013.7.2
LV.NOL.2014.7.3
LV.NOL.2014.5.4
LV.NOL.2014.6.4
LV.AMO.2022B.7.1
LV.AMO.2015.5.1
LV.NOL.2012.6.1
LV.AMO.2011.7.3
LV.NOL.2013.5.3
LV.NOL.2023.5.4
LV.NOL.2012.5.3
LV.NOL.2012.5.1
LV.AMO.2016.5.3
LV.NOL.2021.6.2
LV.NOL.2024.7.2
LV.AMO.2022B.5.1
LV.AMO.2014.5.5
LV.NOL.2012.7.4
LV.NOL.2016.7.2
LV.NOL.2019.7.4
LV.AMO.2016.5.2
LV.AMO.2016.6.2
LV.NOL.2011.6.3
LV.AMO.2012.7.1
LV.NOL.2013.5.1
LV.AMO.2011.6.1
LV.AMO.2013.6.4
LV.NOL.2011.5.1
LV.AMO.2014.7.2
LV.NOL.2013.7.4
LV.AMO.2019.6.5
LV.AMO.2022B.7.2
LV.NOL.2011.6.1
LV.NOL.2012.6.4
LV.AMO.2015.5.3
LV.NOL.2023.6.4
LV.AMO.2014.5.2
LV.AMO.2012.5.1
LV.AMO.2019.7.1
LV.NOL.2016.7.5
LV.AMO.2022B.6.3
```


## 4. Uzdevumi paraugpiemēriem


heštegi ir `Label` vērtības no `avg-pulcins-2027/hintTypes.csv` 
(divi jauni heštegi aprakstīti nodaļas beigās).




### Jauni heštegi (nav `hintTypes.csv`)

| Label | Phase | TitleLv | DescriptionLv |
|---|---|---|---|
| AnswerType | Understand | Jautājuma tips | Nosaki jautājuma tipu (atrast visus, vai var?, vai vienmēr?, lielākā/mazākā, pierādīt, parādīt kā) un to, no kādām daļām sastāv pilna atbilde. |
| ConstructExample | Engage | Uzbūvē piemēru | Uzbūvē vienu konkrētu piemēru un pārbaudi, ka tas apmierina visus nosacījumus; der "vai var? – jā" atbildei un optimizācijas uzdevuma piemēra daļai. |
