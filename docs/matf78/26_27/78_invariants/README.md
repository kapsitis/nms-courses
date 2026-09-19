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




## 3. Atlasīšana no RDF datubāzes











