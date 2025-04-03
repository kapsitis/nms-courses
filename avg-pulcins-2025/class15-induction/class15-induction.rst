Matemātiskā Indukcija
======================

Šerloks Holmss nodarbojās ar *dedukciju* (pielietoja vispārīgas zināšanas 
atsevišķos gadījumos), pretējā darbība ir *indukcija* -- no atsevišķiem 
piemēriem nonākt pie vispārīgām zināšanām.

Matemātiskā indukcija parasti pierāda kādu apgalvojumu vienam skaitlim 
:math:`n=1` (*indukcijas bāze*); pēc tam pieņem, ka apgalvojums 
ir spēkā pie kādas vērtības :math:`k` (*induktīvā hipotēze*) un pierāda, ka 
tad tam jābūt spēkā arī pie vērtības :math:`k+1` (*induktīvā pāreja*). 
Un tad tas ir spēkā visiem naturāliem :math:`n`. 

**Apgalvojums:** 
  Summa :math:`1 + 2 + 3 + \ldots + n` katram naturālam :math:`n` ir vienāda 
  ar :math:`{\displaystyle \frac{n(n+1)}{2}}`. 

**Pierādījums:**
  
  **Indukcijas bāze:** Ja :math:`n=1`, tad ievieto un pārbauda, vai :math:`1 = \frac{1(1+1)}{2}`.

  **Induktīvā hipotēze:** Pieņem, ka pie :math:`n=k` ir spēkā :math:`1 + 2 + \ldots +k = \frac{k(k+1)}{2}`. 

  **Induktīvā pāreja:** Pamato, ka pie :math:`n=k+1` ir spēkā :math:`1 + 2 + \ldots + k + (k+1) = \frac{(k+1)(k+2)}{2}`. 

**1.uzdevums:** 
  Vilmārs zīmē figūras, pirmās trīs no kurām parādītas attēlā. Pirmā figūra sastāv no četriem
  vienādiem kvadrātiem un tās perimetrs ir 5 vienības. Katru nākamo figūru Vilmārs iegūst, iepriekšējai figūrai
  labajā pusē piezīmējot klāt vēl trīs kvadrātus ar izmēru :math:`1 \times 1`. 

  .. figure:: figs/square-construction.png
     :width: 2.4in

  **(A)** Atrast 20.figūras laukumu un perimetru. 
  
  **(B)** Kāds ir kārtas numurs figūrai, kuras perimetrs ir 1000?

**2.uzdevums:** 
  Pierādīt, ka kvadrātu var sadalīt :math:`n` mazākos kvadrātos, ja :math:`n \geq 6`. 

**3.uzdevums:** 
  Atrast skaitļa :math:`1^2 + 2^2 + \ldots + 99^2` pēdējo ciparu. 


.. 60281	

**4.uzdevums:** 
  Pierādīt identitāti :math:`1 + 3 + 5 + \ldots + (2n-1) = n^2`. 
  (*Identitāte* - tāda vienādība, kas ir spēkā jebkurām 
  mainīgo vērtībām.)

.. 34930

**5.uzdevums:** 
  Vairākas taisnes sadala plakni gabalos. 
  Pierādīt, ka šos gabalus var izkrāsot 2 krāsās 
  tā, ka blakus esošiem apgabaliem būs atšķirīga krāsa.


**6.uzdevums:** 
  Hanojas tornī ir 3 stieņi; uz viena no tiem 
  uzvērti :math:`n` dažādu diametru diski. 
  Uzdevums ir pārvietot diskus uz blakus stieni tā, lai 
  katru no tiem pārceltu pa vienam, pārvietojot uz 
  brīvu stieni vai virsū tur jau esošam diskam, bet 
  nekad neliktu lielāku disku virsū mazākam.

  Pierādīt, ka :math:`n` diskus uz blakus stieni var pārvietot 
  :math:`2^n-1` gājienos, ievērojot šos noteikumus.

  .. figure:: figs/hanoi-tower.png
     :width: 2in


..  31369

**7.uzdevums:**
  Rūtiņu lapā uzzīmēts taisnstūris ar :math:`3` rindiņām un :math:`n` kolonnām. 
  Katrā rūtiņā novietots aplītis kādā no trim krāsām. 
  Pavisam ir :math:`n` aplīši katrā krāsā.  

  Pierādīt, ka katrā rindiņā var samainīt aplīšu secību tā, lai katrā kolonnā 
  nonāktu aplīši visās trīs krāsās. 

**8.uzdevums:** 
  :math:`n` biedri dala laupījumu. Laupījums sastāv no dažādām daļām, 
  tās visas var jebkādi dalīt, nezaudējot vērtību (piemēram, 
  šķidrumi vai metāli). 
  Katram biedram var būt cits viedoklis par tās vai citas daļas vērtību; 
  un viņš vēlas iegūt ne mazāk kā :math:`1/n` daļu no laupījuma (no sava viedokļa). 
  Atrast veidu, kā sadalīt laupījumu.

**9.uzdevums:** 
  :math:`n` cilvēki nav savstarpēji pazīstami. 
  Pierādīt, ka daži no viņiem var abpusēji iepazīties tā, lai 
  nekādiem trim no viņiem nebūtu vienāds skaits paziņu starp atlikušajiem 
  :math:`n-1`.



**10.uzdevums:** 
  Pierādīt, ka katram naturālam :math:`n` ir spēkā vienādība: 
  
  .. math::

    1 \cdot 4 + 2 \cdot 7 + 3 \cdot 10 + \ldots + n \cdot (3n+1) = n(n+1)^2. 


**11.uzdevums:** 
  Pierādīt, ka visām naturālām :math:`n` vērtībām :math:`7^n + 3^{n+1}` dalās ar :math:`4`. 


**Kļūdains spriedums ar indukciju:** 
  Visi zirgi ir vienādā krāsā. (Par zirga krāsu sauc viņa apmatojuma krāsu, piemēram, 
  "bēris", "sarķis", "sirmis".)

  **Bāze:** :math:`n=1` Viens zirgs ir noteiktā krāsā; tā arī ir vienīgā krāsa. 

  **Induktīvais pieņēmums:** :math:`n=k`. 
    Pieņemam, ka parametra vērtībai :math:`n=k` izpildās apgalvojums: :math:`k` zirgi ir vienādā krāsā. 

  **Induktīvā pāreja:** :math:`k \rightarrow k+1`. 
    Aplūkojam :math:`k+1` zirgus. Vispirms no zirgu kopas izņem vienu no zirgiem un pamato, ka 
    atlikušie ir vienā krāsā (pēc pieņēmuma). Pēc tam izņem citu zirgu un atkal pamato, ka atlikušie 
    ir vienā krāsā. 

**Kļūdains spriedums ar indukciju:** 
  Kādā skolā matemātikas stundas notiek katru darba dienu (no pirmdienas līdz piektdienai). 
  Skolotāja klasei apsolīja, ka nākamajā nedēļā paredzēts kontroldarbs, bet kontroldarba 
  diena nebūs skolēniem iepriekš zināma.

  Pamatot ar indukciju, ka kontroldarbu ar šādiem nosacījumiem nevar uzdot. 
  Atrast induktīvajā spriedumā kļūdu.


