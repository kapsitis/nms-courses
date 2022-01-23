NMS Skaitļu teorija #2: Modulārā aritmētika
=================================================

Ievads un tēmas
------------------

1. Kongruenču klases, modulārā aritmētika. 
2. Dalāmības pazīmes, kas saglabā dalāmības pa
3. Mazā Fermā teorēma. Periodiskas decimāldaļas.
4. Cikliski procesi . Periodiskas atlikumu virknes. 
5. Periodi un priekšperiodi virknēs.


**Uzdevums (Valsts4Posms-2012.P1):** 
  Ar :math:`S(x)` apzīmēsim skaitļa :math:`x` ciparu summu. 
  Aprēķināt :math:`S(S(S(2012^{2012})))`.


**Risinājuma plāns:** 
  Skaitlis :math:`2012^{2012}` ir ļoti liels; aprēķināt visus šos ciparus ir 
  praktiski neiespējami. Toties skaitļa ciparu summa apmierina svarīgu invariantu 
  (atlikums, dalot ar :math:`9` saglabājas. 
  Risinājuma pirmajā daļā meklēsim vienīgi skaitļu :math:`S(S(S(2012^{2012})))`, 
  :math:`S(S(2012^{2012}))`, :math:`S(2012^{2012})` un :math:`2012^{2012}` atlikumu, 
  dalot ar :math:`9` (visiem tiem jābūt vienādiem). 
  Risinājuma otrajā daļā noskaidrosim, kurš no skaitļiem ar atrasto atlikumu 
  ir konkrēti :math:`S(S(S(2012^{2012})))` (novērtējot to ar nevienādībām). 

**Apgalvojums 1:**
  Ja :math:`n` ir naturāls skaitlis, tad tā ciparu summa :math:`S(n)`
  un pats skaitlis :math:`n` dod vienādus atlikumus, dalot ar :math:`9`. 
  (Šis apgalvojums pazīstams kā vispārināta dalāmības pazīme ar :math:`9`.) 
  
**Pierādījums:** 
  Skaitlis :math:`n = \overline{c_1c_2\ldots{}c_{k-1}c_k}`, kur :math:`c_i` ir decimālcipari, 
  ir pierakstāms kā polinoms, kur mainīgā vietā ir decimālsistēmas bāze :math:`x = 10`: 
  
  .. math:: 
  
    n = c_1 \cdot 10^{k-1} + c_2 \cdot 10^{k-2} + \ldots + c_{k-1} \cdot 10^{1} + c_k \cdot 10^{0}). 
    
  Ja aprēķinām ciparu summu :math:`S(n) = c_1 + c_2 + \ldots + c_{k-1} + c_k`, 
  tad tā atšķiras no :math:`n` ar to, ka saskaitāmo :math:`c_i \cdot 10^{k-i}` vietā 
  ir saskaitāmie :math:`c_i`. (Piemēram, ja ceturtais cipars no skaitļa beigām jeb *tūkstošu cipars* 
  ir :math:`c_{k-3} = 7`, tad vērtības :math:`7 \cdot 1000` vietā pieskaitām vienkārši vērtību :math:`7`.)
  
  Starpība abām vērtībām ir :math:`c_i \cdot 10^{k-i} - c_i = c_i \cdot \overline{99\ldots99}`, kur
  cipars :math:`c_i` ir pareizināts ar skaitli kas sastāv no daudziem deviņniekiem. 
  Šis skaitlis, acīmredzot dalās ar :math:`9`. Tāpēc atlikums, dalot ar :math:`9` (ja 
  skaitli :math:`n` aizstāj ar :math:`S(n)` jeb katru ciparu :math:`c_i` piesummē vienkārši, 
  nevis reizina ar :math:`10` pakāpi :math:`c_i \cdot 10^{k-i}`) nemainās. :math:`\square`

  
**Apgalvojums 2:** 
  Pamatosim, ka :math:`2012^{2012}` dod atlikumu :math:`7`, dalot ar :math:`9`. 
  

**Pierādījums:** 
  Aplūkojot pakāpju :math:`a^b` atlikumus, dalot ar :math:`9`, 
  ievērojam, ka tie atkarīgi vienīgi
  no :math:`a` atlikuma, dalot ar :math:`9`, jo reizinot (un kāpinot)
  skaitļus ar vienādiem atlikumiem, arī rezultāti dos vienādus atlikumus. 
  Tātad :math:`a^b` atlikumi dalīšanā ar :math:`9`
  atkārtojas ar ciklu :math:`9`, ja pakāpes bāze :math:`a` aug.
  Izsakām :math:`(2012)^{2012} = (223 \cdot 9 + 5)^{2012}`. 
  Tātad jāmeklē atlikums, dalot :math:`5^{2012}` ar :math:`9`. 
  
  Otrs novērojums -- pakāpju :math:`a^b` atlikumi, dalot ar :math:`9`, 
  cikliski atkārtojas ik pēc :math:`6`, ja kāpinātājs :math:`b` aug.
  
  ================   ================   =====================
  :math:`n`          :math:`5^n`        Atlikums, dalot ar 9
  :math:`5^0`        :math:`1`          :math:`1`
  :math:`5^1`        :math:`5`          :math:`5`
  :math:`5^2`        :math:`25`         :math:`7`
  :math:`5^3`        :math:`125`        :math:`8`
  :math:`5^4`        :math:`625`        :math:`4`
  :math:`5^5`        :math:`3125`       :math:`2`
  :math:`5^6`        :math:`15625`      :math:`1`
  ================   ================   =====================

  Vēl lielākām pakāpēm atlikumi, dalot ar :math:`9` labajā kolonnā sāk atkārtoties: :math:`5^7` dod tādu pašu atlikumu kā :math:`5^1`, 
  :math:`5^8` dod tādu pašu atlikumu kā :math:`5^2`, utt. 
  Arī šīs tabulas aizpildīšanai var godīgi nekāpināt. Ja, teiksim, :math:`5^2 = 25` dod atlikumu :math:`7`, dalot ar :math:`9`, 
  tad nākamā atlikuma iegūšanai pietiek ar :math:`5` pareizināt nevis visu :math:`25`, bet gan tikai šo atlikumu :math:`7` -- rezultāts
  jeb atlikums skaitlim :math:`35` būs tas pats, kas atlikums skaitlim :math:`125`. 
  
  Tā kā :math:`5^6` dod atlikumu :math:`1`, dalot ar :math:`9`, 
  tad arī :math:`(5^6)^{335} = 5^{2010}` dod atlikumu :math:`1`. 

  Visbeidzot, :math:`5^{2012} = 5^{2010} \cdot 5^2 = 1 \cdot 25`, kas dod atlikumu :math:`7`, dalot ar :math:`9`.  
  :math:`\square`
  

**Secinājums:**
  Arī skaitlis :math:`S(S(S(2012^{2012})))` dod atlikumu :math:`7`, dalot ar :math:`9`. 
  :math:`\square`. (Apvienojam Apgalvojumu 1 un Apgalvojumu 2.) 


**Apgalvojums 3:** 
  :math:`S(S(S(2012^{2012}))) = 7`. 
  
**Pierādījums:** 
  Mums jāpārbauda, vai :math:`S(S(S(2012^{2012})))` nevar būt vienāds ar kādu citu skaitli, kas arī 
  dod atlikumu :math:`7`, dalot ar :math:`9`. Mazākais šāds skaitlis ir :math:`7+9 = 16`. 
  Pamatosim nevienādības: 
  
  .. math::
  
    \begin{array}{rl}
    (1) & S(S(S(2012^{2012}))) < 16,\\
    (2) & S(S(2012^{2012})) < 79,\\
    (3) & S(2012^{2012}) < 799999999.\\
    \end{array}

  Skaitlis :math:`79` ir mazākais, kurš dod atlikumu :math:`7` dalot ar :math:`9`, bet kura ciparu summa ir :math:`16`. 
  Skaitlis :math:`799999999` ir mazākais, kurš dod atlikumu :math:`7` dalot ar :math:`9`, bet kura ciparu summa ir :math:`79`. 
  Tāpēc :math:`(3) \rightarrow (2) \rightarrow (1)`. 
  
  Pierādīsim pašu pēdējo no minētajām nevienādībām, novērtējot pašu skaitli :math:`2012^{2012}`.
  
  .. math::
  
    2012^{2012} < 2100^{2100} = ((2.1)^3)^{700} \cdot (1000)^{2100} = (9.261)^{700} \cdot (1000)^{2100} < 10^{700} \cdot 10^{6300} = 10^{7000}.
    
  Iegūstam, ka skaitļa :math:`2012^{2012}` decimālpierakstā ir ne vairāk kā :math:`7000` cipari. 
  Pat ja tie visi būtu deviņnieki, tad to summa nepārsniedz :math:`63000`, kas ir mazāk nekā :math:`799999999`. 
  Tātad nevienādība (3) ir pierādīta (un tātad arī nevienādības (2) un (1)). :math:`\square`
    

Var pārbaudīt iegūto rezultātu (skaitli :math:`7`) ar aprēķinu valodā Python: 

.. code-block:: python

  def S(num):
      return sum(int(digit) for digit in str(num))

  S(S(S(2012**2012)))

  
