Grafi un krāsojumi
==================================

**Definīcija:** 
  *Grafs* :math:`G` satur kopu ar virsotnēm :math:`V = \{ v_1, v_2, \ldots, v_n\}` 
  un šķautnēm :math:`E = \{ (v_i, v_j), \ldots \}` -- katra šķautne savieno 
  divas grafa virsotnes. Šķautnes virziens nav svarīgs. 
  (*Orientētā grafā* šķautnes virziens ir svarīgs, uz šķautnēm zīmē bultiņas.)
  
Grafa virsotnes var pārvietot; šķautnes var attēlot gan taisnas, gan 
liektas. Mūs neinteresē šķautņu krustošanās ārpus grafa virsotnēm.
Parasti uzskata, ka šķautne nevar savienot virsotni pašu ar sevi;
nevar savienot tās pašas virsotnes ar vairākām šķautnēm.

**Definīcija**
  Par *koku* sauc tādu grafu, kas ir (1) *sakarīgs* -- no katras virsotnes var aiziet uz 
  katru citu virsotni, izmantojot šķautnes, (2) *bez cikliem* -- nevar 
  apstaigāt virsotnes pa ciklu 
  (atgriežoties sākumpunktā un izmantojot katru cikla šķautni tikai vienreiz).

**Gatavošanās jautājumi: Grafi un krāsojumi**

**1.jautājums:**
  **(A)**
    Kokam ir :math:`100` virsotnes. Cik šādam kokam ir šķautņu?

  **(B)**
    Kāds mazākais krāsu skaits :math:`n` nepieciešams, 
    lai jebkura koka virsotnes var izkrāsot :math:`n` krāsās tā, 
    ka ikviena šķautne 
    noteikti savienotu divas virsotnes dažādās krāsās?

**2.jautājums:** 
  No šaha galdiņa :math:`8 \times 8` izgriezta viena rūtiņa divos veidos (sk. attēlu). 
  Kurus no kvadrātiem var sagriezt taisnstūrīšos :math:`1 \times 3` un kurus nevar?

  .. figure:: figs/chess-boards.png
     :width: 2.4in

**3.jautājums:** 
  Deviņi punkti izvietoti kvadrātiskā režģī kā parādīts attēlā. 
  Novilkt lauztu līniju no 4 posmiem tā, lai tā ietu caur visiem deviņiem punktiem. 
  (Lauzta līnija sastāv no vairākiem savienotiem nogriežņiem -- to var novilkt, neatraujot 
  rakstāmo no papīra. Posmi drīkst savstarpēji krustoties un lauztajai līnijai 
  nav jāatgriežas sākumpunktā.)

  .. figure:: figs/nine-dots.png
     :width: 0.6in

**4.jautājums:** 
  Cik krāsas nepieciešamas, lai izkrāsotu katru valsti (un arī jūru) Eiropas kontūrkartē tā, ka 
  valstīm, kam ir kopīga robeža, būtu atšķirīgas krāsas; valsti, kas saskaras ar jūru, nevar 
  krāsot tāpat kā jūru. Sk. `Eiropas kontūrkarte <https://www.vectorstock.com/royalty-free-vector/blank-outline-map-of-europe-simplified-wireframe-vector-13703065>`_.
  (Valstis, kas kartē izskatās mazas vai neredzamas, nav jākrāso - Andora, Malta, 
  Lihtenšteina, Sanmarino, Monako, Vatikāns.)

.. only:: Internal 

  .. figure:: figs/europe-map.png
     :width: 3in

**5.jautājums:** 
  Grafā ir :math:`n = 10` virsotnes un katras divas virsotnes savienotas ar šķautni
  (tādu grafu sauc par *pilnu*). 
  Cik šajā grafā ir šķautņu?

**6.jautājums:** 
  Pusdienu starpbrīdī pie katra no 8 galdiņiem sēž tieši 6 cilvēki. 
  Daži no viņiem ir savstarpēji draugi (ja cilvēks :math:`A` ir draugs cilvēkam 
  :math:`B`, tad arī :math:`B` ir draugs :math:`A`); neviens nav draugs pašam sev. 
  Pie katra galdiņa sēdošie cilvēki nosauca, cik no viņu draugiem vēl sēž pie 
  šī galdiņa. Atrast, pie kuriem galdiņiem iegūtās atbildes ir neiespējamas.

  (A) :math:`5,4,3,2,1,0`; (B) :math:`6,5,4,3,2,1`; (C) :math:`2,2,2,2,2,2`; (D) :math:`3,3,3,2,2,2`. 

  (E) :math:`3,3,2,2,2,2`; (F) :math:`1,1,1,1,1,1`; (G) :math:`5,3,3,3,3,3`; (H) :math:`5,5,4,3,2,1`.
  


**7.jautājums:** 
  Daudzskaldņus var uzzīmēt kā grafus bez šķautņu krustošanās (piemēram, vienu skaldni 
  izstiepj ļoti lielu un visas virsotnes nonāk tās iekšpusē). 
  Zīmējumā attēlotajam kubam saskaitīt "Š" - cik kubā ir šķautņu; 
  "V" - cik kubā ir virsotņu; "S" - cik kubā ir skaldņu. 
  Aprēķināt izteiksmi Eilera formulai: V + S - Š. 

  .. figure:: figs/cubes-octahedron-combined.png
     :width: 3.6in

**8.jautājums:** 
  Uzzīmēt oktaedru (figūra, ko veido divas kopā ar pamatiem salīmētas četrstūra piramīdas; 
  sk. attēlu) kā planāru grafu. Saskaitīt oktaedrā šķautnes, virsotnes un skaldnes
  un aprēķināt Eilera formulas vērtību: V + S - Š.


**Olimpiāžu uzdevumi:** 


**1.uzdevums:**
  Diagrammā uzzīmētas apdzīvotas vietas ar norādītiem ceļiem un braukšanas 
  attālumiem. Autobuss izbrauca no pilsētas :math:`A` un pēc :math:`2222`
  kilometru nobraukšanas atgriezās pilsētā :math:`A`. 
  Pierādīt, ka autobuss noteikti brauca pa ceļa posmu :math:`EG`. 

  .. figure:: figs/bus-diagram.png
     :width: 2.8in

**2.uzdevums:** 
  Šaha turnīrā piedalās trīs komandas pa :math:`10` šahistiem katrā komandā. 
  Ikviens šahists turnīrā spēlēs tieši vienreiz ar katru no šahistiem 
  abās pārējās komandās (pavisam :math:`20` spēles). Kādā brīdī izrādījās, 
  ka ir izspēlētas jau :math:`201` spēles. Pierādīt, ka atradīsies trīs 
  šahisti, kuri katrs ar katru jau spēlējuši. 

**3.uzdevums:** 
  Dots balts kvadrāts, kas sastāv no :math:`10 \times 10` rūtiņām. 
  Pēterītis nokrāsoja melnas visas rūtiņas, kas pieskaras šī kvadrāta malām. 
  Vai var nokrāsot melnas vēl dažas no atlikušajām rūtiņām atlikušajā 
  baltajā laukumā :math:`8 \times 8` tā, lai nekur šajā kvadrātā nebūtu 
  vienkrāsains kvadrāts :math:`2 \times 2` vai arī kvadrāts :math:`2 \times 2`, kas 
  izkrāsots kā šaha galdiņš?

  .. figure:: figs/chess-patterns.png
     :width: 1.6in

