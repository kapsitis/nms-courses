---
layout: default
title: "7.1.temats: Atrisinājumu struktūras"
permalink: /matf78/26_27/78STRUCT_solution_structure/
---
# 1.temats: Atrisinājumu struktūras. Uzdotajam jautājumam atbilstoša atbilde

**Mērķis:** Kā lasīt uzdevumu, kā veidot jautājumam 
atbilstošu risinājuma struktūru. Kādus jautājumus sev 
uzdot pirms uzskatīt par atrisinātu. Kā analizēt vienkāršus 
6.-7.kl. olimpiāžu uzdevumus.

* **Uzdevumu lapa:** [web]({{ '/matf78/26_27/78STRUCT_solution_structure/problems/' | relative_url }}), [pdf]({{ '/matf78/26_27/78STRUCT_solution_structure/problems.pdf' | relative_url }}), [docx]({{ '/matf78/26_27/78STRUCT_solution_structure/problems.docx' | relative_url }})
* **1.nodarbības izdales materiāls:** [web]({{ '/matf78/26_27/78STRUCT_solution_structure/handout_class1/' | relative_url }}), [pdf]({{ '/matf78/26_27/78STRUCT_solution_structure/handout_class1.pdf' | relative_url }}), [docx]({{ /matf78/26_27/78STRUCT_solution_structure/handout_class1.docx' | relative_url }})
* **2.nodarbības izdales materiāls:** TBD


**Rezultātu izklāsts:** 

* SR: Atšķir 6 olimpiāžu jautājumu pamattipus — "atrast visus", 
  "atrast lielāko/mazāko vērtību" (optimizācijas uzdevumi), 
  "vai vienmēr var?"/"vai kādam var?" (JĀ/NĒ izlemšanas uzdevumi), 
  "pierādīt", "konstruēt piemēru" (aprakstīt 
  algoritmu vai spēles stratēģiju). Zina katram atbilstošo pilnas atbildes struktūru 
  (piem., "atrast visus" = atrast + pamatot, ka citu nav).
* SR: Apgalvojumu "var/eksistē" pamato ar konkrētu piemēru, bet "nevar/vienmēr" — 
  ar vispārīgu spriedumu;  optimizācijas uzdevumā uzraksta optimālo 
  piemēru + neiespējamību to uzlabot.
* SR: Sistemātiski izmanto mazos gadījumus un sakārtotu pilno pārlasi; apskata 
  gadījumus tā, lai būtu redzams, ka nekas nav izlaists.
* Veicināta arī mērķtiecīga risināšanas secība. Piemēram, 
  Saprast (tekstu), izpētīt (uzdevuma modeli), īstenot (risināšanas plānu), 
  atskatīties (uz risinājumu). (*En: Understand → Explore → Attack → Review.*)
  jeb *Saprašana → Izpēte → Pārformulēšana → Risināšana → Atskats*.


**Tipiski uzdevumi:** 
[LV.NOL.2024.7.2](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2024.7.2) 
(atrast lielāko: piemērs + uzlabošanas neiespējamība), 
[LV.AMO.2023.7.1](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2023.7.1) (Pamatot/apgāzt ar A,B daļām), 
[LV.NOL.2024.7.3](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2024.7.3) (Atrast visus ar abu robežu pārbaudi).

## Skaidrojamie piemēri

Pieci uzdevumi ar dažādiem jautājumu tipiem - 4 no NMS arhīva un 1 no 5.-9.kl. grāmatas.
Katram — ieteikumu secība pa fāzēm *Saprašana → Izpēte → Pārformulēšana → Risināšana → Atskats*. 

### 4.1. LV.AMO.2015.5.3 — "Vai var?" (A: jā, B: nē)

Vai iespējams uzzīmēt tādu taisnstūri, kura malu garumi ir naturāli skaitļi, 
bet **(A)** laukums ir pirmskaitlis; **(B)** perimetrs ir pirmskaitlis?

1. *Saprašana:* Divi "vai var?" jautājumi. Katram izlem: "jā" pierāda viens piemērs, "nē" – spriedums par visiem taisnstūriem. `#AnswerType`
2. *Saprašana:* Pirmskaitlim ir tieši 2 dalītāji. Malas a un b ir naturāli skaitļi; laukums a·b, perimetrs 2(a+b). `#ClarifyGoal`
3. *Izpēte:* Pamēģini 1×1, 1×2, 1×3, 2×3. Kuriem sanāk pirmskaitlis laukumā? Un perimetrā? #SmallCases
4. *Risināšana:* (A) Taisnstūrim 1×3 laukums ir 3 – pirmskaitlis. Ar vienu šādu piemēru pietiek: atbilde "jā". `#ConstructExample`
5. *Risināšana:* (B) Perimetrs 2(a+b) vienmēr ir pāra skaitlis un vismaz 4, tātad nav pirmskaitlis. Atbilde "nē". `#ParityAndRemainders`
6. *Atskats:* Vai (B) daļā ir vispārīgs spriedums par visiem a un b, nevis tikai daži izmēģināti taisnstūri? `#LookBack`


### 4.2. Vecās tabulas 15. uzdevums — "Vai noteikti?" (jā)

Daina, izmantojot visus ciparus, burtnīcā ierakstīja desmitciparu skaitli. 
Vai šis skaitlis noteikti dalās ar 3?

1. *Saprašana:* "Noteikti" nozīmē "vienmēr". Pretpiemērs pierādītu "nē"; "jā" jāpamato visiem šādiem skaitļiem. `#AnswerType`
2. *Saprašana:* "Visi cipari" – tātad 0, 1, …, 9, katrs tieši vienu reizi (citādi nesanāk 10 cipari). `#ClarifyGoal`
3. *Izpēte:* Uzraksti dažus šādus skaitļus, piem., 1023456789 un 9876543210. Vai kāds nedalās ar 3? `#TryToDisprove`
4. *Pārformulēšana:* Dalāmība ar 3 atkarīga tikai no ciparu summas, nevis no ciparu secības. Kāda ir summa? `#Paraphrase`
5. *Risināšana:* 0+1+…+9 = 45 dalās ar 3, tātad katrs šāds skaitlis dalās ar 3. Atbilde: jā, noteikti. `#ParityAndRemainders`
6. *Atskats:* Vai skaitlis noteikti dalās arī ar 9? Ar 11? Kurai atbildei pietiek ar vienu pretpiemēru? `#LookBack`


### 4.3. LV.AMO.2015.5.4 — "Atrast visus"

Kādu naturālu skaitli, saskaitot ar savu ciparu summu, iegūst skaitli $328$? 
Atrodi visus tādus skaitļus un pamato, ka citu nav!

1. *Saprašana:* Atbildē divas daļas: (1) parādīt skaitļus, kas der; (2) pierādīt, ka citu nav. `#AnswerType`
2. *Izpēte:* Izmēģini: 300+3 = 303, 310+4 = 314, 320+5 = 325. Kurā apgabalā jāmeklē? `#TrialAndError`
3. *Risināšana:* Divciparu skaitlis dod ne vairāk kā 99+9+9 = 117, četrciparu – vismaz 1000. Tātad skaitlis ir trīsciparu. `#ExtremeCases`
4. *Risināšana:* Ciparu summa ≤ 3+9+9 = 21, tātad skaitlis ≥ 328−21 = 307: pirmais cipars 3, otrais 0, 1 vai 2. `#AuxiliaryElements`
5. *Risināšana:* Otrais cipars 0: 2c = 25; 1: 2c = 14, c = 7; 2: 2c = 3. Der tikai 317. `#CaseAnalysis`
6. *Atskats:* Pārbaudi 317+3+1+7 = 328. Vai pierakstā redzams, ka neviens gadījums nav izlaists? `#LookBack`


### 4.4. LV.NOL.2024.7.2 — "Lielākā vērtība"

Kāda lielākā ciparu summa var būt desmitciparu skaitlim, kas dalās ar $18$?

1. *Saprašana:* "Lielākā" prasa divas daļas: piemēru, kurā vērtība sasniegta, un pamatojumu, ka lielāka nav iespējama. `#ExampleAndBound`
2. *Pārformulēšana:* 18 = 2·9, un 2 un 9 ir savstarpēji pirmskaitļi: skaitlis ir pāra, un tā ciparu summa dalās ar 9. `#Paraphrase`
3. *Izpēte:* Sāc no galējā: summa 90 ir tikai skaitlim 9999999999. Vai tas dalās ar 18? `#ExtremeCases`
4. *Risināšana:* Summa dalās ar 9 un nav 90, tātad nav lielāka par 81. Tas ir novērtējums. `#ExampleAndBound`
5. *Risināšana:* Piemērs: 9999999990 ir pāra skaitlis, ciparu summa 81 dalās ar 9. Atbilde: 81. `#ConstructExample`
6. *Atskats:* Vai uzrakstīts gan piemērs, gan novērtējums? Ja vienas daļas trūkst, risinājums nav pilns. `#LookBack`


### 4.5. LV.AMO.2018.7.1 — "Cik?" (sakārtota pilnā pārlase)

Cik dažādus naturālus skaitļus, kam visi cipari ir dažādi, var izveidot no 
cipariem $2,\ 0,\ 1,\ 8$?

1. *Saprašana:* Vai jāizmanto visi 4 cipari? Nē – der arī 1, 2 un 3 ciparu skaitļi. Skaitlis nesākas ar 0. `#ClarifyGoal`
2. *Saprašana:* "Cik?" – jāpārliecina lasītājs, ka nekas nav izlaists un nekas nav saskaitīts divreiz. `#AnswerType`
3. *Izpēte:* Izraksti sakārtoti viencipara un divciparu skaitļus: 1, 2, 8; 10, 12, 18, 20, … Cik to ir? `#SmallCases`
4. *Pārformulēšana:* Sadali gadījumos pēc ciparu skaita (1, 2, 3, 4). Gadījumi nepārklājas, tāpēc skaitus var saskaitīt. `#CaseAnalysis`
5. *Risināšana:* Pirmajam ciparam 3 iespējas (ne 0), otrajam arī 3, tad 2, tad 1: 3, 3·3, 3·3·2, 3·3·2·1. `#LookForPattern`
6. *Atskats:* Salīdzini 3·3 = 9 ar 3. soļa sarakstu. Atbilde: 3+9+18+18 = 48. `#LookBack`
