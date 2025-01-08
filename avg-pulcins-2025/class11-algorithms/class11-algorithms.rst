Attiecības un konstrukcijas
============================

**Definīcija:** Par *bināru attiecību* (skaitļu, cilvēku utml. kopā)
sauc tādu īpašību, kas piemīt vai nepiemīt noteiktam sakārtotam pārim no šīs kopas.
Raksta :math:`(a,b) \in R` vai arī :math:`a\,R\,b`, kur attiecību apzīmē ar :math:`R`.

Kuriem skaitļiem definētas šādas attiecības (reāliem vai naturāliem)?

* "Ir lielāks par": :math:`a > b`
* "Ir lielāks vai vienāds par": :math:`a \geq b`
* "Ir savstarpēji pirmskaitļi": :math:`a \perp b` jeb :math:`LKD(a,b) = 1`
* "Dalās ar": :math:`a \vdots b` (piemēram, :math:`15` dalās ar :math:`3`)
* "Ir dalītājs": :math:`a \mid b` (piemēram, :math:`3` ir :math:`15` dalītājs)

Bināras attiecības starp cilvēkiem: 

* "Cilvēks A ir vecāks cilvēkam B": :math:`\text{\sc Vecaks}(A,B)`
* "Cilvēks A ir sencis cilvēkam B": :math:`\text{\sc Sencis}(A,B)`
* "Cilvēki A un B ir sibi jeb vienu vecāku bērni jeb brāļi/māsas (siblings)" (pilnīgie sibi, pussibi)
* "Cilvēki A un B ir draugi/pazīstami" (uzdevumos parasti ir simetriska draudzība). 

Var attēlot ar bultiņām (A iedur B, ja (A,B) pieder attiecībai). 
Var ierakstīt visus pārīšus tabulā ar divām kolonnām. Vai iezīmēt matricā.

**Definīcija:** 

* Bināru attiecību sauc par *refleksīvu*, ja katrs elements ir šajā attiecībā pats ar sevi: :math:`(a,a) \in R`.
* Bināru attiecību sauc par *simetrisku*, ja secība nav svarīga: :math:`(a,b) \in R` ir tad un tikai tad, ja 
  :math:`(b,a) \in R`. 
* Bināru attiecību sauc par *transitīvu*, ja no :math:`(a,b) \in R` un :math:`(b,c) \in R` seko 
  :math:`(a,c) \in R`. 

**Piemēri:**  
(A) Racionālu daļu vienādība: :math:`\frac{a}{b} \equiv \frac{c}{d}`, ja :math:`ad = bc`.
(B) Figūru vienādība: Divas plaknes figūras ir vienādas, ja eksistē pārveidojums no vienas uz otru, kas 
saglabā attālumus.
(C) Skaitļu kongruence pēc moduļa: :math:`8 \equiv 15 \pmod 7` (8 un 15 dod vienādus atlikumus, dalot ar 7).
(D) No pilsētas A var nonākt pilsētā B, nešķērsojot jūru. 


**1.uzdevums:** 
  Starp kopām :math:`\varnothing` (tukša kopa), :math:`\{ a \}`, :math:`\{ b\}` un 
  :math:`\{ a,b \}` ir apakškopas attiecība. To var attēlot šādi: 

  .. figure:: figs/subsets2.png
     :width: 1in
    
  Uzzīmēt līdzīgu attēlu visām trīs elementu kopas :math:`\{ a,b,c \}` apakškopām 
  tā, lai to apakškopu attiecības izskatītos kā kubs. (Tās attiecības, kas ir secināmas 
  no jau novilktajām bultiņām ar transitivitāti zīmējumā nav jāattēlo.)


**2.uzdevums:** 
  Uzzīmēt skaitļus no 1 līdz 12 kā aplīšus plaknē tā, lai izpildītos vairāki nosacījumi:

  * Ja skaitlis :math:`A` ir skaitļa :math:`B` dalītājs, tad :math:`A` iedur skaitlim 
    :math:`B` ar bultiņu un :math:`B` atrodas vismaz vienu centimetru augstāk nekā :math:`A`
    (t.i. visas bultiņas iet no apakšas uz augšu). 
  * Visiem tiem skaitļu pāriem, kuru attiecība ir :math:`B/A` ir vienāda ar 2, 
    bultiņas no :math:`A` uz :math:`B` ir vienādādā garumā un savstarpēji paralēlas.
  * Visiem tiem skaitļu pāriem, kuru attiecība ir :math:`B/A` ir vienāda ar 3, 
    bultiņas no :math:`A` uz :math:`B` ir vienādādā garumā un savstarpēji paralēlas
    (bet virziens ir cits nekā bultiņām starp skaitļiem ar attiecību 2).

  Četriem skaitļiem diagramma izskatās šādi: 

  .. figure:: figs/diamond.png
     :width: 0.9in


**LV.NOL.2024.8.5**
  Vai a) 22. att., b) 23. att. dotā kvadrāta rūtiņās var ierakstīt deviņus 
  dažādus naturālus skaitļus tā, lai katrā
  rūtiņā būtu ierakstīts viens skaitlis un katrā rindā un katrā kolonnā 
  skaitļi pieaugtu bultiņas norādītajā virzienā?

  .. figure:: figs/LV.NOL.2024.8.5.png
     :width: 2in

**LV.NOL.2023.7.2** 
  Vai a) 90 lampiņas, b) 73 lampiņas ar vadiem var savienot tā, lai katra no tām būtu savienota ar vadu ar
  tieši 5 citām lampiņām?


**LV.NOL.2023.8.2**
  Pasākumā satikās :math:`m` cilvēki. Katrs no tiem draudzējas ar tieši 3 citiem cilvēkiem 
  (ja :math:`A` draudzējas ar :math:`B`, tad
  :math:`B` draudzējas ar :math:`A`). Zināms, ka no katriem trim cilvēkiem 
  var atrast divus, kuri savā starpā nedraudzējas.
  Vai var gadīties, ka **(A)** :math:`m = 11`, **(B)** :math:`m = 10`?

**LV.NOL.2022.7.4**
  Pansionātam ir astoņi stāvi un tajā ir trīs lifti. Katrs lifts apstājas 
  pirmajā stāvā, astotajā stāvā un vēl četros citos stāvos. Vai liftu apstāšanos 
  var izkārtot tā, lai pansionāta iemītnieki no katra stāva var nokļūt jebkurā
  citā stāvā bez pārkāpšanas citā liftā?

**LV.NOL.2022.8.5**
  Rindā uzrakstīti skaitļi no 1 līdz 2022 (ieskaitot). Divi spēlētāji pēc 
  kārtas izsvītro pa vienam skaitlim no rindas
  tik ilgi, kamēr rindā paliek tikai divi skaitļi (katrā gājienā var 
  izsvītrot jebkuru no palikušajiem skaitļiem).
  Pirmais spēlētājs (tas spēlētājs, kurš sāk spēli) uzvar, ja divu beigās 
  palikušo skaitļu lielākais kopīgais dalītājs
  ir lielāks nekā 1, bet otrais uzvar, ja divu beigās palikušo skaitļu 
  lielākais kopīgais dalītājs ir 1. Pierādīt, ka, lai
  kā arī spēlētu pirmais spēlētājs, otrais spēlētājs vienmēr var uzvarēt!

**LV.NOL.2017.7.1**
  Varde vienā lēcienā var pārvietoties vienu rūtiņu uz augšu vai vienu rūtiņu pa labi. 
  Cik dažādos veidos varde no rūtiņas A var nokļūt rūtiņā B (skat. 11. att.)? 
  Iekrāsotajās rūtiņās ir šķērslis, tajās varde neiet.

  .. figure:: figs/LV.NOL.2017.7.1.png
     :width: 1.2in
