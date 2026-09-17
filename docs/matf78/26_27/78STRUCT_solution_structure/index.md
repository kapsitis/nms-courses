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

* **Uzdevumu lapa:** {% include doc_links.html url="/matf78/26_27/78STRUCT_solution_structure/problems/" %}
* **1.nodarbības materiāls:** {% include doc_links.html url="/matf78/26_27/78STRUCT_solution_structure/class1/" %}
* **2.nodarbības materiāls:** {% include doc_links.html url="/matf78/26_27/78STRUCT_solution_structure/class2/" %}
{: .small}


**Prasmes:** 

* SR: Atšķir 6 olimpiāžu jautājumu pamattipus — (1) "atrast visus", 
  (2) "atrast lielāko/mazāko vērtību" (optimizācijas uzdevumi), 
  (3) "vai vienmēr var?" / (4) "vai kādam var?" (JĀ/NĒ izlemšanas uzdevumi), 
  (5) "pierādīt", (6) "konstruēt piemēru" (aprakstīt 
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

* *Saprašana:* Divi "vai var?" jautājumi. Katram no tiem: "jā" = vajag piemēru, "nē" – spriedums par visiem taisnstūriem.
* *Saprašana:* Pirmskaitlim ir tieši $2$ dalītāji. Malas $a$ un $b$ ir naturāli skaitļi; laukums $a \cdot b$, perimetrs $2(a+b)$.
* *Izpēte:* Mazie gadījumi: $1 \times 1$, $1 \times 2$, $1 \times 3$, $2 \times 3$. 
   Kuriem laukums (perimetrs) ir pirmskaitlis?
* *Risināšana:* Laukumam pietiek ar vienu piemēru, kas ir pirmskaitlis. 
* *Risināšana:* Perimetrs $2(a+b)$ vienmēr ir pāra skaitlis. Vai pāra skaitļi var būt pirmskaitļi?
   Kuri tie ir un vai iespējami mūsu uzdevumā.
* *Atskats:* Vai (B) daļā ir vispārīgs spriedums par visiem $a$ un $b$, nevis tikai daži piemēri? 


### 4.2. Piemērs — "Vai noteikti?" (jā)

Daina, izmantojot visus ciparus, burtnīcā ierakstīja desmitciparu skaitli. 
Vai šis skaitlis noteikti dalās ar $3$?

* *Saprašana:* "Noteikti" nozīmē "vienmēr". Pretpiemērs pierādītu "nē"; "jā" jāpamato visiem šādiem skaitļiem.
* *Saprašana:* "Visi cipari" – tātad $0, 1, \ldots, 9$, katrs tieši vienu reizi (citādi nesanāk 10 cipari).
* *Izpēte:* Uzraksti dažus šādus skaitļus, piem., 1023456789 un 9876543210. Vai tie dalās ar 3?
* *Pārformulēšana:* Dalāmība ar 3 atkarīga tikai no ciparu summas, nevis no ciparu secības. Kāda ir ciparu summa?
* *Risināšana:* $0+1+\ldots +9 = 45$ dalās ar $3$, tātad katrs šāds skaitlis dalās ar $3$. Atbilde: jā, noteikti.
* *Atskats:* Vai skaitlis noteikti dalās arī ar 9? Ar 11? Kurai atbildei pietiek ar vienu pretpiemēru?

