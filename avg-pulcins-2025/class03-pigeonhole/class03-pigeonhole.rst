Dirihlē princips
=====================




**Dirihlē princips (vienkāršākais gadījums):** 
  Ja vairāk kā :math:`n` objektus saliek :math:`n` kastēs, tad vismaz vienā 
  no kastēm ir vismaz divi objekti. 

**Dirihlē princips (vispārīgāks gadījums):** 
  Visiem naturāliem skaitļiem :math:`n` un :math:`t`, ja :math:`tn+1` objektus 
  saliek :math:`n` kastēs, tad vismaz vienā kastē nonāks vairāk kā :math:`t` objekti. 

**Apgalvojums par vidējo vērtību:**
  Ja :math:`n` skaitļu vidējais aritmētiskais ir :math:`t`, tad 
  vismaz viens no skaitļiem ir vismaz :math:`t`. Un arī vismaz 
  viens no skaitļiem nepārsniedz :math:`t`. 

**Pierādījums:** 
  No pretējā: ja visi :math:`n` skaitļi būtu mazāki par :math:`t`,
  tad to summa 
  
  .. math:: 
    
    x_1 + x_2 + \ldots + x_n < \underbrace{t + t + \ldots + t}_{\text{n} reizes} = nt. 

  Izdalām abas nevienādības puses ar :math:`n` -- iegūstam, ka vidējais aritmētiskais 
  šiem :math:`n` skaitļiem ir mazāks par :math:`t`, kas ir pretrunā ar to, ka tas vienāds ar :math:`t`. 

..

    "Vobegona ezers, kur visas sievietes ir stipras, visi vīrieši ir izskatīgi, 
    un visi bērni ir virs vidusmēra."
    (*"Lake Wobegon, where all the women are strong, all the men are 
    good-looking, and all the children are above average."*)



**Piemēri** 

Par skaitļu starpību:
  Pierādīt, ka no jebkuriem astoņiem naturāliem skaitļiem var 
  izvēlēties tādus divus, kuru starpība dalās ar :math:`7`. 

Par skaitļu summu:
  Doti naturāli skaitļi no :math:`1` līdz :math:`8`. 
  Kāds mazākais skaits no tiem jāizvēlas, lai starp tiem 
  atrastos divi, kuru summa ir :math:`9`? 

Par skaitļu dalāmību:
  Uz galda ir :math:`5` kartiņas; uz katras uzrakstīts naturāls skaitlis. 
  Pierādīt, ka varēs izvēlēties trīs kartiņas tā, lai uz tām 
  uzrakstīto skaitļu aritmētiskais vidējais būtu vesels skaitlis. 

Zeķu uzdevums:
  Tumšā skapī atrodas :math:`8` pāri sarkanu zeķu, 
  :math:`7` pāri zilu zeķu, :math:`6` pāri zaļu zeķu. 
  Tās ir sajauktas un var izvilkt tikai pa vienai. 
  Cik zeķu neskatoties jāizvelk, lai starp tām būtu divas 
  vienādā krāsā. 

Vispārināts zeķu uzdevums:
  Citplanētietim ir silti, ja viņam ir kāds no sekojošiem apģērbu 
  komplektiem (pietiek izpildīt vienu variantu): 

  **(A)** 1 sega, **(B)** 2 džemperi, **(C)** 3 šalles, 
  **(D)** 4 legingi, **(E)** 5 adītas cepurītes, **(F)** 6 zeķes. 

  Kāds mazākais apģērbu skaits nepieciešams, lai 
  citplanētietim noteikti būtu silti?
  
Komplektu veidošana:
  Sniegbaltīte uzdāvināja katram no :math:`7` rūķīšiem pa 
  :math:`5` konfektēm: "Vāverīti", "Margrietiņu" un 
  "Lācīti", pie tam katrs rūķītis saņēma vismaz vienu 
  katra veida konfekti. Pierādīt ka ir divi tādi rūķīši, 
  kam viņa uzdāvināja vienādus konfekšu komplektus. 

Ģeometriska konfigurācija:
  Rūtiņu virsotnēs atzīmēti :math:`16` punkti; sākumā tie 
  visi ir balti (sk. zīmējumu). Vai tieši :math:`7` punktus 
  var nokrāsot melnus tā, lai nekādi trīs vienā krāsā nokrāsoti 
  punkti neatrastos uz vienas taisnes?
  
  .. plot:: class03-pigeonhole-figs/square-grid.py
     :include-source: false
     :width: 1.2in
     :align: center


**Uzdevumi** 


**1.uzdevums:** 
  Ir :math:`4` monētas ar dažādām masām un sviras svari bez atsvariem (uz tiem var 
  uzlikt divas monētas un noskaidrot, kura monēta ir smagāka). 
  Vai var sakārtot monētas augošā secībā pēc masas, salīdzinot monētas 
  **(A)** tieši :math:`4` reizes; **(B)** tieši :math:`5` reizes? 


**2.uzdevums:** 
  Kādā valstī ir :math:`N` pilsētas; dažas 
  no tām savieno divvirzienu avioreisi. 
  Pierādīt, ka atradīsies divas tādas pilsētas, 
  no kurām ir avioreisi uz vienādu skaitu pilsētu. 
  (Piemēram, zīmējumā abām apakšējām pilsētām 
  ir avioreisi uz divām pilsētām.)

  .. plot:: class03-pigeonhole-figs/airlines-graph.py
     :include-source: false
     :width: 1.2in
     :align: center

**3.uzdevums:** 
  Vienādmalu trijstūrī ar malas garumu :math:`1` atzīmēti desmit punkti. 
  Pierādīt, ka starp tiem atrodas divi punkti, kuru attālums 
  nepārsniedz :math:`{\displaystyle \frac{1}{3}}`. 


**4.uzdevums:** 
  Apskatām :math:`20` skaitļus :math:`S = \{ 1, 2, 3, \ldots, 20 \}`. 
  Pierādīt, ka izvēloties :math:`11` skaitļus no šīs kopas :math:`S` 
  atradīsies divi tādi skaitļi, ka viens skaitlis dalās ar otru. 



**5.uzdevums:** 
  Pierādīt, ka starp jebkuriem :math:`35` divicparu skaitļiem 
  var atrast trīs tādus skaitļus, kuru ciparu summas ir vienādas.


**6.uzdevums:** 
  Kādu mazāko skaitu rūtiņu jāiekrāso kvadrātā ar izmēru 
  :math:`6 \times 6` rūtiņas, lai neiekrāsotajā daļā 
  nevarētu ievietot tādu "stūrīti" (varbūt citādi pagrieztu), 
  kāds redzams zīmējumā? 

  .. plot:: class03-pigeonhole-figs/trimino.py
     :include-source: false
     :width: 1.0in
     :align: center

**7.uzdevums:** 
  Pierādīt, ka no septiņiem patvaļīgiem naturāliem skaitļiem 
  var izvēlēties divus tādus skaitļus, kuru kvadrātu starpība 
  dalās ar :math:`11`.

