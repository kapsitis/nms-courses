Lineāras sakarības 
=====================

**Definīcija:** 
  Skaitļus :math:`a` un :math:`b` sauc par *savstarpējiem pirmskaitļiem*, 
  ja to lielākais kopīgais dalītājs ir :math:`1` (citiem vārdiem, 
  daļa :math:`\frac{a}{b}` ir nesaīsināma). 

**Uzdevums:**
  Pircējam ir monētas ar vērtību :math:`a` eirocenti, pārdevējs var izdot 
  atlikumu monētās ar vērtību :math:`b` eirocenti. 
  Ja :math:`a` un :math:`b` abi dalās ar kādu skaitli (piemēram, :math:`d=5`), 
  tad pircējs nevar samaksāt pārdevējam naudas vērtību, kas nedalās ar šo skaitli
  (piemēram, :math:`16` eirocentus, ja visas viņu monētu vērtības dalās ar :math:`5`). 

  Ja pircēja un pārdevēja monētu vērtības ir savstarpēji pirmskaitļi 
  (:math:`\text{LKD}(a,b) = 1`) -- vai šādā gadījumā pircējs var samaksāt 
  pārdevējam jebkuru summu?

**Uzdevums:** 
  Atrisināt kongruenču vienādojumus: 

    A. :math:`5x \equiv 1 \pmod {11}` (atrast :math:`x`, ka :math:`5x` dod atlikumu 
       :math:`1`, dalot ar :math:`11`),
    B. :math:`6x \equiv 2 \pmod {11}`,
    C. :math:`7x \equiv 3 \pmod {11}`, 
    D. :math:`5x \equiv 4 \pmod {12}`, 
    E. :math:`5x \equiv 11 \pmod {12}`,
    F. :math:`3x \equiv 8 \pmod {12}`,
    G. :math:`3x \equiv 9 \pmod {12}`. 




**Uzdevums:** 
  Uz kalkulatora ekrāna ir uzrakstīts kaut kāds skaitlis. 
  Naktī ar kalkulatoru sāk darboties rūķītis, kurš katru 
  sekundi pieskaita uz ekrāna redzamajam kādu 
  naturālu skaitli :math:`a < 100`. 
  Zināms, ka kalkulatora pēdējie divi cipari mainās un pieņem 
  visas vērtības no ``00`` līdz ``99``. 
  Cik dažādas :math:`a` vērtības rūķītis var izvēlēties?

  .. figure:: figs/calculator.png
     :width: 3in


**Apgalvojums:** 
  Dots skaitļa sadalījums pirmreizinātājos: :math:`n = p_1^{a_1} p_2^{a_2} \ldots p_k^{a_k}`. 
  Skaitlis :math:`n` ir pilns kvadrāts tad un tikai tad, ja visi :math:`a_i` ir 
  pāra skaitļi. Skaitlis :math:`n` ir pilns kubs tad un tikai tad, ja visi 
  :math:`a_i` dalās ar :math:`3` utt.

  Atceramies, ka skaitļa pozitīvo dalītāju skaitu var izteikt ar formulu: 

  .. math:: 

    d(n) = \left(a_1+1 \right) \cdot \left( a_2+1 \right)\cdot \ldots \cdot \left( a_k+1  \right).

**Piemēri:** 

  * Ja skaitlis :math:`n` ir pilns kvadrāts, tad tā pozitīvo dalītāju skaits 
    :math:`d(n)` ir nepāra skaitlis. Vai ir arī pretējais apgalvojums -- 
    ja :math:`d(n)` ir nepāra skaitlis, tad :math:`n` ir pilns kvadrāts?
  * Ja skaitlis :math:`n` ir pilns kubs, tad tam var būt :math:`1,4,7,10,13,\ldots` 
    pozitīvi dalītāji (t.i. dalītāju skaits :math:`d(n)` dod atlikumu :math:`1`, 
    dalot ar :math:`3`).
    Vai ir arī pretējais apgalvojums: Ja :math:`d(n)` dod atlikumu :math:`1`, 
    dalot ar :math:`3`, tad :math:`n` ir pilns kubs?



**Mazā Fermā teorēma:** 
  Dots pirmskaitlis :math:`p` un kāds skaitlis :math:`a`, kas nedalās ar :math:`p`. 
  Tad, reizinot :math:`a` pašu ar sevi :math:`p-1` reizes, iegūstam atlikumu :math:`1`, 
  dalot ar :math:`p` (jeb :math:`a^{p-1} \equiv 1 \pmod p`). 

**Piemērs:** 
  * Visi skaitļi :math:`1^6`, :math:`2^6`, :math:`3^6`, :math:`4^6`, :math:`5^6`, 
    :math:`6^6` dod vienādu atlikumu :math:`1`, dalot ar :math:`7`. 
  * Visi skaitļi :math:`a^4` beidzas ar ciparu :math:`1` vai :math:`6` (ja vien 
    :math:`a` nedalās ar :math:`5`). 
  
**Uzdevums:** 
  Atrast skaitļa :math:`N` atlikumu, dalot ar :math:`7`, kur 
  
  .. math:: 

    N = 2025^{2025^{2025}}\;\;(\text{pieraksts lasāms kā}\;\;2025^{\left(2025^{2025}\right)}).

**LT.SAV.2018.9_10.1:**
  Pierādīt, ka jebkurš naturāls skaitlis :math:`a` 
  ir vienāds ar naturāla skaitļa piektās pakāpes un naturāla skaitļa trešās pakāpes attīecību, 
  t.i. ka :math:`a = b^5 : c^3`, kur :math:`b` un :math:`c` ir naturāli skaitļi.

**Uzdevums:** 
  Uz šaha galdiņa :math:`8 \times 8` novietojās :math:`n` torņi. 
  Katrs tornis saskaitīja, cik citi torņi ir viņa horizontālē (torņi 
  ieguva skaitus :math:`h_1, h_2, \ldots, h_n`). Un katrs tornis saskaitīja, 
  cik citi torņi ir viņa vertikālē (torņi ieguva skaitus 
  :math:`v_1, v_2, \ldots, v_n`). Zināms, ka summas :math:`h_1 + h_2 + \ldots + h_n`
  un :math:`v_1 + v_2 + \ldots + v_n` abas vienādas ar :math:`18`. 
  Cik pavisam torņu var būt uz šaha galdiņa?


**Uzdevums:** 
  Pa šaha galdiņu :math:`8 \times 8` pārvietojas šaha zirdziņš. 
  Vai eksistē tāds maršruts, kas sākas kreisajā apakšējā stūrī (rūtiņā **a1**), 
  apstaigā visas rūtiņas, katrā nonākot tieši vienu reizi, un 
  beidzas blakus kreisajam apakšējam stūrim (rūtiņā **a2**)?


**Uzdevums:** 
  Pa šaha galdiņu :math:`8 \times 8` pārvietojas figūriņa "pūķis". 
  Katrā solī šī figūriņa var izdarīt kādu no gājieniem :math:`(1,1)`, 
  :math:`(-1,0)`, :math:`(0,-1)`. Pūķis sāk savu kustību kreisajā apakšējā 
  stūrī (rūtiņā **a1**)
  Cik daudzās šaha galdiņa rūtiņās šī figūriņa varēs nonākt, veicot 
  tieši :math:`60` gājienus?