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


**1.uzdevums:** 
  Karlsonam ir :math:`30` milzīgi tortes gabali. Viņš izvēlas trīs gabalus un sagriež 
  katru no tiem vai nu :math:`3`, vai :math:`5` mazākos gabalos (visus izvēlētos gabalus sagriež 
  vienādā skaitā mazāku gabalu). Tad viņš atkal izvēlas kādus :math:`3` gabalus un
  sagriež katru no tiem vai nu :math:`3`, vai :math:`5` mazākos gabalos (visus izvēlētos gabalus 
  sagriež vienādā skaitā gabalu). Vai, atkārtoti izpildot šādas darbības, 
  Karlsons var iegūt tieši :math:`2000` tortes gabalus?


**2.uzdevums:** 
  Kādā dienā Karlsons uzlika uz galda :math:`44` kūciņas.  
  Karlsons izdomāja, ka vienā piegājienā viņš apēdīs vai nu :math:`5` kūciņas, 
  vai arī :math:`10` kūciņas. Ja Karlsons apēda :math:`5` kūciņas, tad Brālītis uzreiz 
  uz galda uzlika :math:`9` kūciņas. Ja Karlsons apēda :math:`10` kūciņas, tad Brālītis 
  uzreiz uz galda uzlika :math:`2` kūciņas. Vai iespējams, ka uz galda kādā brīdī
  bija tieši :math:`2022` kūciņas?



**3.uzdevums:** 
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


**4.uzdevums:**
  Elektroniskais pulkstenis rāda stundu skaitu (vesels skaitlis robežās no :math:`0` 
  līdz :math:`23`) un minūšu skaitu (vesels skaitlis robežās no 
  :math:`0` līdz :math:`59`). Noteikt, cik reižu diennaktī stundu skaita 
  un minūšu skaita starpība dalās ar :math:`7`.


**5.uzdevums:**
  Četru bērnu -- Almas, Bruno, Cēzara un Dorotejas -- tēvs mēdz bērniem iedot 
  sīknaudu. Tā reiz tēvs saviem bērniem iedeva sīknaudu šādi:

  * Almai kādu naudas summu viena centa monētās;
  * Bruno mazāko naudas summu divu centu monētās, kas ir lielāka nekā Almai iedotā naudas summa;
  * Cēzaram mazāko naudas summu piecu centu monētās, kas ir lielāka nekā Bruno iedotā naudas summa;
  * Dorotejai mazāko naudas summu desmit centu monētās, kas ir lielāka nekā Cēzaram iedotā naudas summa.

  Kāda ir **(A)** lielākā, **(B)** mazākā iespējamā starpība starp Dorotejai 
  un Almai iedotajām naudas summām?

**6.uzdevums:** 
  Māris iedomājās naturālu skaitli :math:`n`. Pēc tam viņš izvēlējās vienu 
  skaitļa :math:`n` dalītāju, pareizināja to ar :math:`4` un iegūto
  reizinājumu atņēma no dotā skaitļa :math:`n`, iegūstot vērtību :math:`11`. 
  Kāda varēja būt :math:`n` vērtība? Atrodi visus variantus un
  pamato, ka citu nav!


**7.uzdevums:** 
  Vai var atrast **(A)** :math:`5`; **(B)** :math:`15` naturālus skaitļus 
  (ne obligāti dažādus), kuru summa ir vienāda ar to reizinājumu?