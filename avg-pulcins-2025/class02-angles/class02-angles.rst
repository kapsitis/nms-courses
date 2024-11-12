Trijstūri un leņķi
=========================================

Riņķa dalīšana daļās
  Uz riņķa līnijas atzīmēti :math:`n` punkti (:math:`n = 1,2,3,4,5,6`). 
  Katri divi punkti savienoti ar nogriezni. Cik daļās tie sadala riņķi? 
  (Rezultātus var apkopot tabulā un atrast sakarību - kā daļu skaits pieaug, 
  ja pieaug punktu skaits :math:`n`.)

  .. figure:: class02-angles-figs/dividing-circles.png
     :width: 3in

.. only:: Internal 

  **Atbilde:** 

    Zīmējumā redzami gadījumi :math:`n=1,2,3`. 
    Daļu skaits, kuros nogriežņi sadala apli ir attiecīgi :math:`1,2,4`. 

    Lielākām :math:`n` vērtībām: 

    ============  ====  ====  ====  ====  ====  ====
    :math:`n`     1     2     3     4     5     6
    ============  ====  ====  ====  ====  ====  ====  
    Daļu skaits   1     2     4     8     16    31
    ============  ====  ====  ====  ====  ====  ====

    Sešiem un vairāk punktiem tos var atzīmēt arī tā, ka sešstūra iekšpusē 
    vienā punktā krustojas vairāk kā divas diagonāles (piemēram, ja saliek 
    šos punktus regulāra sešstūra virsotnēs). 
    Šādos gadījumos pie :math:`n = 6`
    Šādos gadījumos pie :math:`n = 6` rodas mazāk daļu, piemēram, :math:`30`. 
    Skaitlis :math:`31` ir *lielākais* daļu skaits, ko var dabūt sešiem punktiem.
    
    Ģeometrijā ir bīstami izdarīt pārsteidzīgus secinājumus 
    (piemēram, noticēt tam, ka daļu skaits ikreiz dubultojas, veidojot 
    virkni :math:`1,2,4,8,16,32,64,\ldots`). Visas hipotēzes ir jāpārbauda.

  :math:`\square`

Leņķi pie punkta un pie paralēlām taisnēm 
  Definēt, kas ir blakusleņķi, krustleņķi, kāpšļu leņķi, šķērsleņķi, 
  iekšējie/ārējie vienpusleņķi. Kuri no tiem ir savstarpēji vienādi, 
  kuru summa ir :math:`180^{\circ}`?

Iekšējo leņķu summa daudzstūrī:
  Pierādīt šādus apgalvojumus: Trijstūrī iekšējo leņķu summa ir :math:`180^{\circ}`. 
  Izliektā daudzstūrī ar :math:`n` malām iekšējo leņķu summa ir :math:`180^{\circ} \cdot (n-2)`. 


Ārējo leņķu summa daudzstūrī: 
  Pierādīt, ka ārējo leņķu summa jebkurā izliektā daudzstūrī ir :math:`360^{\circ}`. 

  .. figure:: class02-angles-figs/external-angles.png
     :width: 1.4in


Pusaplī ievilkts leņķis: 
  Dota riņķa līnija, :math:`AB` ir diametrs, bet :math:`C` ir virsotne uz riņķa līnijas. 
  Pierādīt, ka :math:`\sphericalangle ACB = 90^{\circ}`. 

  .. figure:: class02-angles-figs/inscribed-semicircle.png
     :width: 2in



Mediāna taisnleņķa trijstūrī: 
  Ja taisnleņķa trijstūrī :math:`ABC` leņķis :math:`ACB` ir taisns, bet :math:`M` ir 
  malas :math:`AB` viduspunkts, tad :math:`AB = 2CM` (mediāna ir puse no taisnleņķa trijstūra 
  garākās malas jeb hipotenūzas). 


Trijstūra laukums: 
  Pamatot, ka trijstūra laukums ir :math:`S = \frac{1}{2}a \cdot h_{a}`, kur 
  :math:`a` ir trijstūra mala (pamats) un :math:`h_a` ir augstums, kas novilkts 
  pret pamatu :math:`a`. 



.. Atvērtā kopa 2019, 7.klase

**1.uzdevums:** 
  Dots, ka :math:`a` un :math:`b` ir neparalēlas taisnes. Plaknē uzzīmēja vēl 
  :math:`10` taisnes; katra no tām paralēla vai nu :math:`a`, vai :math:`b`. 
  Pēc tam taisnes :math:`a` un :math:`b` nodzēsa. Cik punktos krustojas palikušās 
  :math:`10` taisnes? Atrodiet visas iespējas un
  pierādiet, ka citu, bez jūsu atrastajām, nav.



.. only:: Internal 

  **Atbilde:**

    Sākotnējās taisnes :math:`a` un :math:`b` var nemaz nezīmēt -- šajā situācijā svarīgi, ka 
    atlikušās :math:`10` taisnes kaut kā sadalītas divās paralēlu taišņu grupās
    (dažreiz šādas grupas sauc par *paralēlu taišņu kūļiem*). 

    Ievērojam, ka vienā grupā esošas taisnes savstarpēji nekrustojas, jo ir savstarpēji paralēlas. 
    Savukārt dažādās grupās esošas taisnes krustojas -- katras divas krustojas vienā punktā. 

    .. figure:: class02-angles-figs/intersecting-lines.png 
       :width: 2in

    Attēlā parādīts, kā grupas, kurās ir :math:`7` un :math:`3` taisnes, krustojas 
    :math:`7 \cdot 3 = 21` punktā. 
    Apskatot visas iespējas, kā :math:`10` taisnes var sadalīt divās grupās, iegūsim 
    šādus reizinājumus: 

    * :math:`0 \cdot 10 = 0`
    * :math:`1 \cdot 9 = 9`
    * :math:`2 \cdot 8 = 16`
    * :math:`3 \cdot 7 = 21`
    * :math:`4 \cdot 6 = 24`
    * :math:`5 \cdot 5 = 25`

    Pārējie reizinājumi :math:`6 \cdot 4, 7 \cdot 3, \ldots` sakrīt ar kādu no šiem. 
    Tādēļ iespējamās atbildes ir :math:`\{ 0, 9, 16, 21, 24, 25 \}`. 

  :math:`\square`


.. Atvērtā kopa 2019, 8.klase

**2.uzdevums:** 
  Sadalīt regulāru sešstūri **(A)** :math:`9` un **(B)** :math:`8` vienādās daļās.

.. only:: Internal 

  **Ieteikums:**

    * Kas ir "vienādas daļas"? (Jēdziens par kongruentām figūrām).
    * Ja sarežģīti dalīt uzreiz :math:`9` vai :math:`8` daļās, var dalīt 
      vispirms :math:`2` vai :math:`3`, vai :math:`4`, vai :math:`6` daļās. 
    * Lai dalītu :math:`9` daļās, var vispirms dalīt :math:`3` daļās, tad katru 
      no daļām dalīt vēl :math:`3` daļās. 
    * Regulāru sešstūri var sadalīt mazos trijstūrīšos (dažādā skaitā trijstūrīšu 
      atkarībā no to izmēra). Šāds mazo trijstūrīšu režģis var palīdzēt dalīt 
      vienādās daļās - pa mazo trijstūrīšu režģa līnijām. 

  :math:`\square`

.. Atvērtā kopa 2018, 7.klase

**3.uzdevums:** 
  Vai iespējams 4 nogriežņus izkārtot tā, ka katrs no tiem krustojas ar
  
  A. :math:`1`, :math:`2`, :math:`2` un :math:`3` citiem nogriežņiem;
  B. :math:`1`, :math:`2`, :math:`3` un :math:`3` citiem nogriežņiem?

  Gadījums, kur krustotos ar :math:`0`, :math:`1`, :math:`1` un :math:`2` 
  nogriežņiem, parādās 1. zīmējumā. 

  .. figure:: class02-angles-figs/segments.png
     :width: 1.2in

.. only:: Internal 

  **Ieteikums:**

    **(A)** 
      Zīmējot nogriežņus, var viegli atrast piemēru, kuram vajadzīgais 
      krustpunktu skaits uz katra nogriežņa ir zināms.

    **(B)** 
      Katrs krustpunkts starp diviem nogriežņiem ir abpusējs (ja 1.nogrieznis 
      krustojas ar 2.nogriezni, tad arī 2.nogrieznis krustojas ar 1.nogriezni) -- 
      šādai attiecībai vienmēr ir divas puses.

      Krustpunktiem :math:`1,2,3,3` tas nav iespējams, jo šo skaitļu summa ir 
      :math:`1+2+3+3 = 9` ir nepāra skaitlis.
    
  :math:`\square`


.. LV.AMO.2022A.8.1; 

**4.uzdevums:** 
  Taisnes :math:`y = x` un :math:`y = -2x + 2022` krustojas 
  punktā :math:`A`. Punkti :math:`B` un :math:`C` ir attiecīgi šo 
  taišņu krustpunkti ar :math:`y` asi. Aprēķināt trijstūra 
  :math:`ABC` laukumu. 


.. LV.AMO.2022A.8.3; 

**5.uzdevums:** 
  Kvadrātā :math:`ABCD` novilkta diagonāle :math:`AC` un uz tās 
  atzīmēts punkts :math:`E` tā, ka 
  :math:`\sphericalangle DEC=75^{\circ}`. 
  Nogriežņa :math:`DE` pagarinājums krusto malu :math:`AB` punktā
  :math:`F`. Pierādīt, ka :math:`EF=FB`!


.. LV.AMO.2022B.8.3; 

**6.uzdevums:** 
  Trijstūrī :math:`ABC` uz malas :math:`BC` atlikts tāds punkts :math:`D`, 
  ka :math:`AD = BD` un :math:`AB = DC = AC`. 
  Aprēķināt trijstūra :math:`ABC` leņķus!

.. LV.AMO.2023.7.3

**7.uzdevums:** 
  No četrām tādām figūrām, kāda dota 12. att., uzzīmē figūru, kurai ir tieši: 

  A. 2 simetrijas asis;
  B. 4 simetrijas asis!  

  *Piezīme.* Figūru, kas dota 12. att., drīkst pagriezt. 
  Uzzīmētajai figūrai var būt arī caurumi. Figūrai jābūt
  saistītai, tas ir, no figūras katras rūtiņas jābūt iespējai 
  aiziet uz jebkuru citu šīs figūras rūtiņu, ejot tikai
  pa šīs figūras rūtiņām, katru reizi pārejot no attiecīgās 
  rūtiņas uz blakus rūtiņu, ar ko tai ir kopīga mala.

  .. figure:: class02-angles-figs/LV.AMO.2023.7.3.png 
     :width: 0.8in
