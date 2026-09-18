---
layout: default
title: "9.1. temats. Atrisinājumu struktūras: Kas ir pilns pierādījums"
permalink: /matf910/26_27/910STRUCT_solution_structure/
---
# 9.1. temats. Atrisinājumu struktūras: Kas ir pilns pierādījums

**Apraksts:** Kā lasīt uzdevumu, kā veidot jautājumam atbilstošu 
risinājuma struktūru. Kādus jautājumus sev uzdot pirms uzskatīt uzdevumu
par atrisinātu. Analizēt grūti lasāmus uzdevumus.


* **Uzdevumu lapa:** {% include doc_links.html url="/matf910/26_27/910STRUCT_solution_structure/problems/" %}
* **1.nodarbības materiāls:** {% include doc_links.html url="/matf910/26_27/910STRUCT_solution_structure/class1/" %}
* **2.nodarbības materiāls:** {% include doc_links.html url="/matf910/26_27/910STRUCT_solution_structure/class2/" %}
* **Īso atbilžu tests:** {% include doc_links.html url="/matf910/26_27/910SHORT_ANSWERS/test19_intermediate/" %}
{: .small}

## Prasmes 

* SR: Atšķir olimpiāžu jautājumu pamattipus - "atrast visus", "vai var?",
  "lielākā/mazākā vērtība", "pierādīt", "konstruēt piemēru", "aprakstīt
  procedūru vai stratēģiju" - un zina katram atbilstošo pilnas atbildes
  struktūru.
* SR: Atšķir nepieciešamos un pietiekamos nosacījumus; lieto secināšanas
  rezultātus pareizajā virzienā. 
* SR: Sadala risināmo situāciju apakšgadījumos un pārliecinās, ka nekas nav izlaists.
* SR: Raksta pierādījumu no pretējā: formulē pieņēmuma noliegumu, iegūst
  pretrunu ar novērtējumu vai dalāmību.
* SR: Izmanto mērķtiecīgu risināšanas secību. Piemēram, 
  Saprast (tekstu), izpētīt (uzdevuma modeli), īstenot (risināšanas plānu), 
  atskatīties (uz risinājumu). (*En: Understand → Explore → Attack → Review.*)
  jeb *Saprašana → Izpēte → Pārformulēšana → Risināšana → Atskats*.


**Tipiski uzdevumi:**

[LV.AMO.2022B.10.2](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2022B.10.2)
(sadalījums divās grupās ar pirmskaitļu summām - "vai var" ar A un B daļu).

[LV.AMO.2022B.9.4](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2022B.9.4)
(pa apli jāuzraksta $1,\ldots,13$ **(A)** un $1,\ldots,14$ **(B)** tā, lai blakus 
skaitļi atšķirtos par $3$, $4$ vai $5$). Viens uzdevums ar abām atbildēm: **(A)** 
"nē" - vajadzīgs spriedums par visiem izkārtojumiem, **(B)** "jā" - pietiek 
uzrādīt vienu apli, piem., $1, 4, 8, 3, 6, 11, 14, 10, 13, 9, 12, 7, 2, 5$.

[LV.AMO.2024.9.2](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2024.9.2)
(no $28$ skolēniem vai nu $4$ ir vienāda atzīme, vai $4$ ieguvuši vairāk nekā $7$ balles). 
Prasība "vai nu A, vai B" liek noliegt abas daļas vienlaikus (De Morgana likums) - 
tieši tas parāda, ko nozīmē pieņemt pretējo saliktam apgalvojumam.

[LV.AMO.2017.8.5](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2017.8.5)
(vai desmitciparu skaitlis var būt vienāds ar savu ciparu reizinājumu). Atbilde "nē" 
jāpamato visiem skaitļiem uzreiz; noliegumu izdodas pierādīt ar vienu novērtējumu, 
nevis gadījumu pārlasi.

[LV.NOL.2024.8.1](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2024.8.1)
(vai, sareizinot sešus dažādus pirmskaitļus, var iegūt sešciparu skaitli ar vienādiem 
cipariem). Pretstats iepriekšējiem: atbilde ir "jā", tāpēc noliegums nemaz nav jāpierāda - 
pietiek ar $222222 = 2 \cdot 3 \cdot 7 \cdot 11 \cdot 13 \cdot 37$.

*Kandidāti atlasīti ar SPARQL vaicājumu [`problems.rq`](problems.rq) 
(`python scripts/select_problems.py docs/matf910/26_27/910STRUCT_solution_structure/problems.rq`).*

P.S. Centieties neizmantot LV.AMO.2025.9.5
un LV.VOL.2024.10.1 - no "./docs/matf910/26_27/curriculum_9_10.md" vai 
līdzīgus uzdevumus, kuros specifiskas zināšanas par nevienādībām un 
novērtējumiem (kā ķirbju uzdevumā LV.AMO.2025.9.5), vai par GCD (kā LV.VOL.2024.10.1) 
"aizēno" spriedumu loģisko struktūru.


## Skaidrojamie piemēri

Trīs īsi 8.-9.klases uzdevumi, kuros atrisinājuma struktūru nosaka apgalvojuma 
noliegums. Katram - ieteikumu secība pa fāzēm 
*Saprašana → Izpēte → Pārformulēšana → Risināšana → Atskats*.


### 2. LV.NOL.2013.9.1 — "Vai eksistē?" (atbilde: jā)

Vai eksistē tāds naturāls skaitlis, kura kvadrāta pēdējie $9$ cipari ir $987654321$?

* *Saprašana:* Eksistences apgalvojumu pierāda viens piemērs; tā noliegums prasītu spriedumu 
  par visiem naturālajiem skaitļiem. Vispirms meklē piemēru.
* *Izpēte:* Kvadrāts beidzas ar $1$ tikai tad, ja pats skaitlis beidzas ar $1$ vai $9$. 
  Ar to jau var sašaurināt meklēšanu.
* *Izpēte:* Pamēģini "vieniniekus": $11^2 = 121$, $111^2 = 12321$, $1111^2 = 1234321$. 
  Kāda likumsakarība redzama ciparos?
* *Risināšana:* $111111111^2 = 12345678987654321$; pēdējie deviņi cipari ir $987654321$. 
  Atbilde: jā.
* *Atskats:* Viens piemērs pabeidz atrisinājumu - nekas vairs nav jāpierāda. Cik daudz vairāk 
  būtu jāraksta, ja atbilde būtu "nē"?








