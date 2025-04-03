Izteiksmes un invarianti
=========================================

Dots apraksts, atrast izteiksmi:
  Trīs rūķi dienā apēd :math:`p` kilogramu piparkūku. Cik kilogramus piparkūku apēd septiņi
  rūķi :math:`d` dienās?



Dota izteiksme, atrast aprakstu:
  Parka platība ir :math:`5000` kvadrātmetri. Norlands vienā stundā var nogrābt
  :math:`N` kvadrātmetrus, Rolands var nogrābt :math:`R` kvadrātmetrus.
  :math:`t` ir darba dienas garums stundās.
  Aprakstīt cilvēku valodā, ko izsaka izteiksmes: 
  **(A)** :math:`N \cdot t +R \cdot t`, 
  **(B)** :math:`5000-(N+R)\cdot 2`,
  **(C)** :math:`5000- N \cdot t - R \cdot (t-2)`.


Dots attēls un leņķi, izteikt citus leņķus:
  Zināms, ka jebkurā trijstūrī iekšējo leņķu summa ir :math:`180^{\circ}`. 
  Par regulāru piecstūri sauc piecstūri, kura visas malas un visi leņķi ir vienādi. 

  :math:`ABCDE` ir regulārs piecstūris ar centru punktā :math:`O`. Apzīmējam 
  leņķi :math:`\sphericalangle OAB`
  ar :math:`\alpha`. Izteikt leņķus :math:`\sphericalangle CBP = \beta`
  un :math:`\sphericalangle BOC = \gamma` ar :math:`\alpha`. 
  Izteikt :math:`\alpha` grādos. 

  
  .. figure:: class01-expressions-figs/pentagon.png
     :width: 2.2in


Izteikt skaitli kā reizinājumu dažādos veidos:
  Par skaitļa :math:`60` kvadrātsakni sauc tādu skaitli :math:`\sqrt{60} = x`, 
  kuru reizinot pašu ar sevi :math:`x^2 = x \cdot x`, iegūst :math:`60`. 
  Atrast veselu skaitli :math:`n`, kuram :math:`n < \sqrt{60} < n+1`. 
  (Noskaidrot, starp kuriem diviem veseliem skaitļiem atrodas kvadrātsakne no :math:`60`.)
  
  .. figure:: class01-expressions-figs/pairs-of-numbers.png
     :width: 3.0in

Dalītāju skaits intervālā :math:`[1;n]`:
  Cik skaitļu no :math:`1` līdz :math:`100` dalās ar :math:`7`?

Dalītāju skaits citos intervālos:
  Kāds ir lielākais iespējamais svētdienu skaits gadā?

Invariants:
  Vai uz :math:`4 \times 4` galdiņa šaha zirdziņš var nonākt no lauciņa 
  :math:`A` lauciņā :math:`B`, veicot tieši :math:`7` gājienus?

  .. plot:: class01-expressions-figs/chessboard.py
       :include-source: false
       :width: 1.3in


**LV.AMO.2022.7.2:**
  Karlsonam ir :math:`30` milzīgi tortes gabali. Viņš izvēlas trīs gabalus un sagriež 
  katru no tiem vai nu :math:`3`, vai :math:`5` mazākos gabalos (visus izvēlētos gabalus sagriež 
  vienādā skaitā mazāku gabalu). Tad viņš atkal izvēlas kādus :math:`3` gabalus un
  sagriež katru no tiem vai nu :math:`3`, vai :math:`5` mazākos gabalos (visus izvēlētos gabalus 
  sagriež vienādā skaitā gabalu). Vai, atkārtoti izpildot šādas darbības, 
  Karlsons var iegūt tieši :math:`2000` tortes gabalus?

.. only:: Internal

  **Ieteikums:**

    * Par cik pieaug tortes gabalu skaits pēc katra 
      Karlsona gājiena? 
    * Izveidot invariantu (neizmaināmu īpašību), kas 
      izpildās skaitlim :math:`30`, bet neizpildās skaitlim :math:`2000`.

  :math:`\square`

.. only:: Internal

  **Atbilde:**
    
    Ja visus trīs gabalus griež katru :math:`3` mazākos gabalos, tad gabalu skaits 
    pieaug par :math:`3 \cdot 3 - 3 = 6` (rodas :math:`9` jauni gabali, bet :math:`3`
    sagrieztie gabali pazūd). 

    Ja visus trīs gabalus griež katru :math:`5` mazākos gabalos, tad gabalu 
    skaits pieaug par :math:`3 \cdot 5 - 2 = 12` (rodas :math:`15` jauni gabali, 
    bet :math:`3` sagrieztie gabali pazūd). 

    Visos šajos gājienos tortes gabalu skaits palielinās skaitli, kas dalās ar :math:`4`. 

  :math:`\square`


**LV.AMO.2022.8.2:**
  Kādā dienā Karlsons uzlika uz galda :math:`44` kūciņas.  
  Karlsons izdomāja, ka vienā piegājienā viņš apēdīs vai nu :math:`5` kūciņas, 
  vai arī :math:`10` kūciņas. Ja Karlsons apēda :math:`5` kūciņas, tad Brālītis uzreiz 
  uz galda uzlika :math:`9` kūciņas. Ja Karlsons apēda :math:`10` kūciņas, tad Brālītis 
  uzreiz uz galda uzlika :math:`2` kūciņas. Vai iespējams, ka uz galda kādā brīdī
  bija tieši :math:`2022` kūciņas?



.. only:: Internal

  **Ieteikums:**

    * Par cik pieaug kūciņu skaits pēc katra gājiena?
    * Izveidot invariantu (neizmaināmu īpašību), kas 
      izpildās skaitlim :math:`44`, bet neizpildās skaitlim :math:`2022`.

  :math:`\square`



.. only:: Internal

  **Atbilde:**

    * Ja apēd :math:`5` kūciņas, tad vietā rodas :math:`9` jaunas kūciņas
      (pieaugums par :math:`4`). 
    * Ja apēd :math:`10` kūciņas, tad vietā rodas :math:`2` jaunas kūciņas 
      (pieaugums par :math:`-8`). 
    
    Katrā gājienā kūciņu skaita atlikums, dalot ar :math:`4` nemainās 
    (kūciņu skaita atlikums, dalot ar :math:`4` ir invariants).

    Ja sākumā bija :math:`44` kūciņas (atlikums, dalot ar :math:`4` ir :math:`0`), 
    tad beigās nevar rasties :math:`2022` (atlikums, dalot ar :math:`4` ir :math:`2`).  


  :math:`\square`




**LV.NOL.2011.7.5:** 
  Pilsētā, kurā dzīvo godīgie iedzīvotāji (kas vienmēr runā tikai 
  taisnību) un blēži (kas vienmēr melo), notika domes vēlēšanas, 
  kurās piedalījās visi pilsētas iedzīvotāji. Balsot varēja par kādu 
  no četrām partijām :math:`A`, :math:`B`, :math:`C` un :math:`D`, un katrs
  iedzīvotājs nobalsoja tieši par vienu partiju. Pirms rezultātu apkopošanas
  žurnālisti veica visu iedzīvotāju aptauju. Uz jautājumu "Vai jūs balsojāt par
  partiju :math:`A`?" ar "Jā" atbildēja :math:`22\%` pilsētas iedzīvotāju. 
  Uz līdzīgu jautājumu par partiju :math:`B` ar "Jā" atbildēja :math:`33\%`, 
  par partiju :math:`C` -- :math:`44\%`, bet par partiju :math:`D` --
  :math:`55\%` iedzīvotāju. Cik procenti pilsētas iedzīvotāju ir 
  godīgie iedzīvotāji un cik -- blēži? 




**LV.AMO.2023.7.5:** 
  Daži no :math:`272` ciema iedzīvotājiem visu laiku saka patiesību, 
  pārējie visu laiku melo. Katram no ciema iedzīvotājiem
  ir tieši viena mīļākā nedēļas diena. Aptaujājot iedzīvotājus, 
  viņiem tika lūgts atbildēt uz septiņiem jautājumiem,
  katrā no tiem izvēloties vienu no dotajām atbildēm:

  .. figure:: class01-expressions-figs/liars.png
     :width: 3.5in

  Uz katru jautājumu saņemto apstiprinošo (“jā”) atbilžu skaits bija šāds: 
  pirmdiena -- :math:`53`, otrdiena -- :math:`54`,
  trešdiena -- :math:`55`, ceturtdiena -- :math:`56`, 
  piektdiena -- :math:`57`, sestdiena -- :math:`58`, svētdiena -- :math:`59`. 
  Cik ciema iedzīvotāji visu laiku melo?

.. only:: Internal

  **Ieteikums:**

    * Vienkāršojam uzdevumu. Pieņemam, ka visi saka patiesību. 
    * Uzzināt, kāds ir invariants (algebriska izteiksme, kuras vērtība nemainās,
      lai kā arī nebūtu sadalījušās iedzīvotāju mīļākās nedēļas dienas). 
    * Saprast, kā invariants mainās 

  :math:`\square`


.. only:: Internal 

  **Atbilde:**

    Ciemā ir :math:`24` meļi.

    Ievērojam, ka atbilžu "Jā" kopskaits nemainās pie dota meļu skaita.  
    Invariants ir visu 7 "jā" skaitļu summa: 
    :math:`S = j_1 + j_2 + j_3 + j_4 + j_5 + j_6 + j_7`.

    Mūsu situācijā kopā ir :math:`53 + 54 + 55 + 56 + 57 + 58 + 59 = 392` 
    atbildes "jā". Ievērosim, ka katrs ciema iedzīvotājs, kas saka patiesību, 
    atbildēja "jā" tieši vienu reizi (savai mīļākajai dienai), bet katrs
    melis -- tieši sešas reizes (visām dienām, kas nav viņa mīļākā diena). 
    Tātad, ja mēs vienu iedzīvotāju, kurš saka patiesību, pārvērstu par meli, 
    tad papildus mēs iegūstu piecas "liekas" atbildes jā.

    Iesākumā pieņemsim, ka visi ciema iedzīvotāji saka patiesību, 
    tādā gadījumā mums kopā būtu tieši :math:`272` atbildes "jā". 
    Tā kā mums ir :math:`394` atbildes "jā", tad mums "liekas" ir 
    :math:`392 - 272 = 120` atbildes "jā".
    Tātad par meļiem mums jāpārvērš :math:`120:5=24` ciema iedzīvotāji.



  :math:`\square`

**LV.AMO.2022.7.4:**
  Elektroniskais pulkstenis rāda stundu skaitu (vesels skaitlis robežās no :math:`0` 
  līdz :math:`23`) un minūšu skaitu (vesels skaitlis robežās no 
  :math:`0` līdz :math:`59`). Noteikt, cik reižu diennaktī stundu skaita 
  un minūšu skaita starpība dalās ar :math:`7`.

.. only:: Internal 

  **Atbilde:** 

    Apkopojam tabuliņā tās starpības, kas dalās ar 7 (atkarībā no izvēlētās stundas): 

    .. figure:: class01-expressions-figs/hour-minute-differences.png
       :width: 5in

    Ir pavisam :math:`15` dažādas stundas (virknītes :math:`0,7,14,21`, 
    un :math:`1,8,15,22`, un :math:`2,9,16,23` kā arī :math:`3,10,17`), 
    kurām atbilst 9 dažādas minūšu vērtības ar starpībām, kas dalās ar :math:`7`. 

    Un ir arī :math:`9` dažādas stundas (virknītes :math:`4,11,18`, un 
    :math:`5,12,19`, un :math:`6,13,20`), kurām atbilst 8 dažādas minūšu vērtības. 

    Izteiksme, kas saskaita visas šīs iespējas ir :math:`15 \cdot 9 + 9 \cdot 8 = 207`. 

    .. raw:: latex

       \clearpage

    Tabulā iekrāsotas visas rūtiņas, kurām stundu un minūšu starpība
    dalās ar 7: 

    .. plot:: class01-expressions-figs/hours.py
       :include-source: false
       :width: 8in
       :align: center

  :math:`\square`



**LV.AMO.2023.8.4:**
  Četru bērnu -- Almas, Bruno, Cēzara un Dorotejas -- tēvs mēdz bērniem iedot 
  sīknaudu. Tā reiz tēvs saviem bērniem iedeva sīknaudu šādi:

  * Almai kādu naudas summu viena centa monētās;
  * Bruno mazāko naudas summu divu centu monētās, kas ir lielāka nekā Almai iedotā naudas summa;
  * Cēzaram mazāko naudas summu piecu centu monētās, kas ir lielāka nekā Bruno iedotā naudas summa;
  * Dorotejai mazāko naudas summu desmit centu monētās, kas ir lielāka nekā Cēzaram iedotā naudas summa.

  Kāda ir **(A)** lielākā, **(B)** mazākā iespējamā starpība starp Dorotejai 
  un Almai iedotajām naudas summām?

**LV.AMO.2022.8.4:** 
  Māris iedomājās naturālu skaitli :math:`n`. Pēc tam viņš izvēlējās vienu 
  skaitļa :math:`n` dalītāju, pareizināja to ar :math:`4` un iegūto
  reizinājumu atņēma no dotā skaitļa :math:`n`, iegūstot vērtību :math:`11`. 
  Kāda varēja būt :math:`n` vērtība? Atrodi visus variantus un
  pamato, ka citu nav!


**LV.AMO.2022A.7.2** 
  Vai var atrast **(A)** :math:`5`; **(B)** :math:`15` naturālus skaitļus 
  (ne obligāti dažādus), kuru summa ir vienāda ar to reizinājumu?

Pieslēgšanās vietnei `<https://www.socrative.com/>`_ (īso atbilžu tests par šo tēmu):

.. |socrative01| image:: class01-expressions-figs/socrative01.png
   :width: 200px
   :align: middle

.. |socrative02| image:: class01-expressions-figs/socrative02.png
   :width: 200px
   :align: middle

.. |socrative03| image:: class01-expressions-figs/socrative03.png
   :width: 200px
   :align: middle

.. |socrative04| image:: class01-expressions-figs/socrative04.png
   :width: 200px
   :align: middle

.. list-table:: 
   :widths: 25 25 25 25
   :align: center
   :header-rows: 0

   * - |socrative01|
     - |socrative02|
     - |socrative03|
     - |socrative04|

