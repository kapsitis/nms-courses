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

**TODO:** Pievienojiet te dažus teikumus, lai izmantojot 
ikdienas piemērus 7.-8.klases jauniešiem 
paskaidrotu, kāpēc vispār šāda "Atrisinājumu struktūra"
kādam būtu jāmācās un kur dzīvē tā palīdzēs.


## 2. Uzdevumu atlases SPARQL

**TODO** Atlasīt 5.-7. klases uzdevumus (2011-2026 gadi), 
kuriem ir dažādas "questionType" vērtības, kuru teksti 
ir salīdzinoši īsāki nekā caurmēra olimpiāžu uzdevumiem. 
Un kuros nav izmantotas pārāk grūtas vai daudzveidīgas 
matemātikas priekšzināšanas, lai matemātiskā sarežģītība 
neaizēnotu jautājuma tipu un atrisinājuma struktūru. 

Uz šī datora ir SPARQL serveris - sk. `$env:OXIGRAPH_DB_PATH`. 

Ievietojiet savu SPARQL README.md dokumentā kā "code-block".


## 3. Atlasīto uzdevumu numuri

**TODO:** Atlasiet uzdevumus (SPARQL meklēšanas rezultātus vai 
arī atrastus ar Python skriptu direktorijā "docs/LV.AMO/", 
"docs/LV.NOL/", "docs/LV.VOL/", "docs/RDF_DATA/".
Ja izmantojat Python skriptu, ievietojiet viņu šajā pašā direktorijā: 
./avg-pulcins-2027/topic7_1_structure/

Šajā nodaļā ievietojiet vienkārši uzdevumu numurus - kā Markdown code-block, 
pa vienam ID katrā rindā.


## 3. Uzdevumi paraugpiemēriem

**TODO:** Ienest te 4-5 uzdevumus (atlasītus ar iepriekšējo 
SPARQL, vai aizgūtus no šiem failiem):

* `avg-pulcins-2026\handout56\content.md`
* `avg-pulcins-2026\handout78\content.md`
* `avg-pulcins-2027\topic7_1_structure\legacy_uzdevumi_par_atrisinajuma_strukturu.png`

Katram no uzdevumiem izveidot ieteikumu secību: 
(1) Katru ieteikumu var ievietot secīgā soļu shēmā: 
(*Saprašana → Izpēte → Pārformulēšana → Risināšana → Atskats*). 
Nav obligāti katram uzdevumam izmantot visus soļus; un, ja uzdevums 
to prasa, var izmantot arī izmainītu soļu secību. 
(2) Katrs ieteikums ir apmēram kā Twitter mikrobloga ieraksts (ap 140 zīmes vai mazāk), 
tas parasti satur "hintLabels" (kolonnu "Labels") no faila `avg-pulcins-2027\hintTypes.csv`
kā heštegu. Var piedāvāt arī jaunus heštagus.
