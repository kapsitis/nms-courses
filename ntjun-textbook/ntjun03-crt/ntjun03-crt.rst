NMS Skaitļu teorija #3: Ķīniešu atlikumu teorēma
=================================================

Ievaduzdevumi
----------------

1. Ar :math:`\gcd(\ldots)` apzīmējam skaitļu kopīgo dalītāju. 
   Vai var atrast tādus naturālus :math:`a,b,c`, kuri
   ir savstarpēji pirmskaitļi: :math:`\gcd(a,b,c) = 1`, bet nekādi divi 
   no tiem nav *pa pāriem savstarpēji pirmskaitļi*, 
   t.i. :math:`\gcd(a,b) > 1`, :math:`\gcd(b,c) > 1` un :math:`\gcd(a,c) > 1`.
   
   
2. Atrast kādu veselu skaitli :math:`x`, kas apmierina šādas sakarības: 
   
   .. math::
   
     \left\{ \begin{array}{l} 
     x \equiv 5 \pmod 6,\\
     x \equiv 3 \pmod 8.\\
     \end{array} \right.
     
   
   
3. Naudas lādē glabājas monētas. Ja tās vienādi sadala sešiem draugiem, 
   paliek pāri četras monētas. Ja tās vienādi sadala pieciem draugiem, 
   paliek pāri trīs monētas. 
   
   Pieņemot, ka naudas lādē ir mazākais monētu skaits, kas atbilst
   šiem nosacījumiem, atrast, cik monētu paliks pāri, ja tās vienādi 
   sadalīs septiņiem draugiem.



Ķīniešu atlikumu teorēmas jēdzieni
------------------------------------

Multiplikatīvi inversie skaitļi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definīcija:**
  Aplūkojam naturālu skaitli :math:`m` un veselu skaitli :math:`a`. 
  Par vesela skaitļa :math:`a` *multiplikatīvi inverso* pēc :math:`m` moduļa jeb (mod :math:`m`) 
  sauc tādu veselu skaitli :math:`x`, kam izpildās kongruence :math:`a \cdot x \equiv 1 \pmod m`. 
  
**Apgalvojums:**
  Lai inversais skaitlis eksistētu ir nepieciešami un pietiekami, ka 
  :math:`a` un :math:`m` ir savstarpēji pirmskaitļi. 
  (Gadījumā, ja :math:`m` ir pirmskaitlis, tas nozīmē, ka :math:`a` nedrīkst dalīties 
  ar :math:`m` -- tātad inversais eksistē ikvienam skaitlim, izņemot tos, kuri kongruenti ar :math:`0`.)


Inverso raksta šādi: :math:`x = a^{-1} \pmod m`.
(Nevajadzētu rakstīt :math:`x = 1/a`, jo dalīšana kongruenču klasēm netiek definēta; 
tās vietā izmanto reizināšanu ar inverso.)

**Piemērs:** 
  :math:`3 \cdot 5 \equiv 1 \pmod 7`, tāpēc :math:`5 = 3^{-1} \pmod 7` un 
  arī otrādi: :math:`3 = 5^{-1} \pmod 7`. 

**Pierādījums:**
  Aplūkosim atsevišķu gadījumu, ja :math:`m` ir pirmskaitlis. 
  Tad funkcija :math:`f_a(x) = (a \cdot x) \% m` ir *injektīva funkcija*. 
  Zīmējumā attēlots gadījums :math:`m = 7`. 

  .. image:: figs-ntjun03-crt/multiplication-mod7.png
     :width: 4in
     
  :math:`a \cdot x_1 \equiv a \cdot x_2` nozīmētu 
  :math:`a \cdot (x_1 - x_2) \equiv 0 \pmod m`.
  
  Tāpēc pēc Dirihlē principa visi nenulles atlikumi 
  :math:`r \not\equiv 0` saņem kādu :math:`a \cdot x \pmod m`
  vērtību -- katram aplītim iedur kāda bultiņa. 
  Arī atlikumam :math:`r = 1` iedur bultiņa. 
  Tātad eksistē inversais :math:`a^{-1}`. :math:`\square`
  

  
Šī Python programmiņa rēķina inverso (paplašinātais Eiklīda algoritms):
  
.. code-block:: python

  def modInverse(a, m):
      m0 = m
      y = 0
      x = 1
      if m == 1:
          return 0
      while a > 1:
          q = a // m
          t = m 
          m = a % m
          a = t
          t = y
          y = x - q * y
          x = t
      if x < 0:
          x = x + m0 
      return x


Arī tad, ja :math:`m` nav pirmskaitlis, tad
aplūkojot tos atlikumus, kuri ir savstarpēji pirmskaitļi 
ar :math:`m`, var atkārtot līdzīgu spriedumu. 

**Piemērs:** 
  Ja :math:`m = 16`, tad inversie elementi ir šādi:

  .. math::
  
    \begin{array}{l}
    \mbox{}1^{-1} \equiv 1 \pmod {16}\\
    3^{-1} \equiv 11 \pmod {16}\\
    5^{-1} \equiv 13 \pmod {16}\\
    7^{-1} \equiv 7 \pmod {16}\\
    9^{-1} \equiv 9 \pmod {16}\\
    11^{-1} \equiv 3 \pmod {16}\\
    13^{-1} \equiv 5 \pmod {16}\\
    15^{-1} \equiv 15 \pmod {16}\\
    \end{array}



Bezū identitāte
^^^^^^^^^^^^^^^^

**Bezū identitāte:** 
  Pieņemsim, ka veseliem skaitļiem :math:`a` un :math:`b` lielākais kopīgais
  dalītājs ir :math:`d`. Eksistē veseli skaitļi :math:`\textcolor{red}{x}` un 
  :math:`\textcolor{red}{y}`,  kas ir atrisinājumi vienādojumam:
  :math:`a\textcolor{red}{x} + b\textcolor{red}{y} = d`.
    
    
.. note::
  Šie atrisinājumi :math:`(x,y)` nav unikāli, 
  vērtību :math:`d` var iegūt bezgalīgi daudz veidos.  

.. note:: 
  Visas izteiksmes :math:`ax+by` (pie dažādiem :math:`x,y \in \mathbb{Z}`) 
  pieņem vērtības, kas ir visi skaitļa :math:`d` daudzkārtņi.


**Piemērs:** 
  :math:`a = 18`, :math:`b = 42`, :math:`\text{gcd}(18,42) = 6`.  
  Der atrisinājumi :math:`(x,y) = (\textcolor{red}{-2},\textcolor{red}{1})`, 
  :math:`(\textcolor{red}{5},\textcolor{red}{-2}),\;(\textcolor{red}{12},\textcolor{red}{-5}), \ldots`. 
  
  .. math::
  
    18 \cdot (\textcolor{red}{-2}) + 42 \cdot \textcolor{red}{1} = 
    18 \cdot \textcolor{red}{5} + 42 \cdot (\textcolor{red}{-2}) = 
    18 \cdot (\textcolor{red}{12}) + 42 \cdot (\textcolor{red}{-5}) = 6.
    
  Atrisinājumi :math:`(x_1,y_1),(x_2,y_2),\ldots` veido 
  aritmētiskas progresijas ar diferencēm :math:`d_x = 7`, :math:`d_y = -3`.


**Bezū identitātes pierādījuma ideja:**
  Aplūkojam naturālu skaitļu kopu:

  .. math:: 
  
    S=\{ax+by \,\mid\, x,y\in\mathbb{Z} \text{ un } ax+by>0\}.
    
  Šajā kopā eksistē minimālais elements :math:`d^{\ast} = ax^{\ast} + by^{\ast}` kaut 
  kādām optimālām vērtībām :math:`(x^{\ast},y^{\ast})`.

  Jāpamato divas lietas:  
  
  1. :math:`d^{\ast}` ir skaitļu :math:`a` un :math:`b` kopīgs dalītājs.  
  2. Ja :math:`c` ir cits :math:`a` un :math:`b` kopīgs dalītājs, tad :math:`c < d^{\ast}`. 

  No abiem šiem punktiem sekotu, ka šādi definētais :math:`d^{\ast}` ir lielākais 
  no visiem kopīgajiem dalītājiem, tātad vienāds ar :math:`d = \gcd(a,b)`.




**Pirmā daļa: Tas ir kopīgs dalītājs** 
  Ja pieņemam, ka :math:`a` nedalās ar `$d^{\ast}$`, tad varētu izdalīt, iegūstot pozitīvu atlikumu: 
  :math:`a = d \cdot q + r`, kur :math:`q` ir kāds vesels skaitlis, bet :math:`0 < r < d^{\ast}`.  
  
  Bet šādā gadījumā arī :math:`r = a - d^{\ast} \cdot q = a - (ax^{\ast}+by^{\ast}) \cdot q`
  varētu izteikt formā :math:`ax+by`, kur :math:`r` arī ir pozitīvs skaitlis 
  un vēl mazāks par :math:`d^{\ast}`. 
  Bet pēc definīcijas `$d^{\ast}$` ir vismazākais. Pretruna.

**Otrā daļa: Tas ir lielākais kopīgais dalītājs:** 
  Ja :math:`c` ir dalītājs skaitļiem :math:`a` un :math:`b`, tad izsakām 
  :math:`a = cu` un :math:`b = cv`, un ievietojam tos :math:`d^{\ast}` izteiksmē:
  
  .. math::
  
    d^{\ast} = ax^{\ast}+by^{\ast} = cux^{\ast} + cvy^{\ast} = c(ux^{\ast} + vy^{\ast}).

  Esam ieguvuši, ka :math:`d^{\ast}` dalās ar :math:`c`, 
  t.i. :math:`d^{\ast} \geq c`. Tātad :math:`d^{\ast}` ir 
  lielākais no kopīgajiem dalītājiem. :math:`\square`

.. note:: 
  Ievērojam, ka :math:`(x^{\ast},y^{\ast})`, 
  lai iegūtu mazāko :math:`d^{\ast} = ax^{\ast}+by^{\ast}` 
  noteikti eksistē, bet nav nekāda algoritma, lai šos nezināmos :math:`x^{\ast},y^{\ast}` 
  iegūtu. tas tātad ir *nekonstruktīvs eksistences pierādījums*.




Blankinšipa algoritms
^^^^^^^^^^^^^^^^^^^^^^

Sk. `Blankinship Algorithm <http://mathworld.wolfram.com/BlankinshipAlgorithm.html>`_.

Sāk ar *matricu* (taisnstūrveida tabuliņu ar skaitļiem):

.. math::

  A = \left(
  \begin{array}{ccc}
  a & 1 & 0 \\
  b & 0 & 1 
  \end{array} \right).

No vienas rindiņas skaitļiem var atņemt otras rindiņas skaitļus
(un arī otrādi). Cenšamies panākt, lai matrica pārveidotos kādā no formām:

.. math::

  \left(
  \begin{array}{ccc}
  d & x & y \\
  0 & x' & y'
  \end{array} \right)\;\;\text{vai}\;\;\left(
  \begin{array}{ccc}
  0 & x' & y' \\
  d & x & y
  \end{array} \right)


**Piemērs:** 
  Pircējam un pārdevējam ir 
  neierobežots skaits monētu ar vērtībām :math:`21` un 
  :math:`34` centi. 
  Tā kā tie ir savstarpēji pirmskaitļi, tad Bezū identitātē
  var iegūt :math:`21x + 34y = 1`. 
  Kā pircējs var nomaksāt pārdevējam 1 centu?


**Risinājums ar Blankinšipa algoritmu:**

  .. math::

    \left( \begin{array}{c|cc}
    21 & 1 & 0 \\
    34 & 0 & 1 \end{array} \right) 
    \leadsto
    \left( \begin{array}{c|cc}
    21 & 1 & 0 \\
    13 & -1 & 1 \end{array} \right) 
    \leadsto
    \left( \begin{array}{c|cc}
    8 & 2 & -1 \\
    13 & -1 & 1 \end{array} \right) 
    \leadsto

  .. math::

    \leadsto \left( \begin{array}{c|cc}
    8 & 2 & -1 \\
    5 & -3 & 2 \end{array} \right) 
    \leadsto
    \left( \begin{array}{c|cc}
    3 & 5 & -3 \\
    5 & -3 & 2 \end{array} \right) 
    \leadsto
    \left( \begin{array}{c|cc}
    3 & 5 & -3 \\
    2 & -8 & 5 \end{array} \right) 
    \leadsto

  .. math::

    \leadsto
    \left( \begin{array}{c|cc}
    1 & 13 & -8 \\
    2 & -8 & 5 \end{array} \right) 
    \leadsto
    \left( \begin{array}{c|cc}
    \textcolor{red}{1} & \textcolor{red}{13} & \textcolor{red}{-8} \\
    0 & -34 & 21 \end{array} \right).

  .. math::

    \left\{ \begin{array}{l}
    21 = 1 \cdot \{21\} + 0 \cdot \{34\} \\
    34 = 0 \cdot \{21\} + 1 \cdot \{34\} \\
    \end{array} \right. 
    \;\;\Rightarrow\;\;
    \textcolor{red}{1} = \textcolor{red}{13} \cdot \{21\} + \textcolor{red}{(-8)} \cdot \{34\}.

  


**Sekas:** 
  Lineārai kongruencei 
  :math:`ax \equiv c \pmod b` (kur :math:`a,b` ir veseli skaitļi un :math:`c`
  dalās ar :math:`d = \text{LKD}(a,b)`) eksistē atrisinājums.

**Pierādījums:** 
  No Bezū identitātes: Var atrisināt `$ax+by=d$`, kam
  :math:`ax - d` dalās ar :math:`b` (tātad :math:`ax` un :math:`d` ir kongruenti pēc
  :math:`b` moduļa). 

  Pēc tam šādi atrastu :math:`x` reizina ar :math:`c/d`, 
  ja :math:`c` ir kāds lielāks skaitlis par LKD.



**Lineāru kongruenču piemēri:**

  1. Atrisināt kongruenci :math:`16x \equiv 14 \pmod 40`.
  2. Atrisināt kongruenci :math:`26x \equiv 14 \pmod 42`.
  3. Dots, ka :math:`x \equiv 7 \pmod 11` un `x \equiv 2 \pmod 7`. 
     Atrast, ar ko  kongruents `x` (mod :math:`77`). 
  4. Atrisināt kongruenci :math:`x^2 \equiv 7\,(\text{mod}\,27)`.




Ķīniešu atlikumu teorēma
^^^^^^^^^^^^^^^^^^^^^^^^^^


**Ķīniešu atlikumu teorēma:**
  Ja doti naturāli skaitļi :math:`n_1,n_2,\ldots,n_k` kuri 
  ir pa pāriem savstarpēji pirmskaitļi un 
  arī jebkādi veseli skaitļi :math:`a_1,a_2,\ldots,a_k`, tad 
  sistēmai 
    
  .. math::
          
    \left\{ \begin{array}{l}
    x \equiv a_1 \pmod {n_1}\\
    x \equiv a_2 \pmod {n_2}\\
    \vdots\\
    x \equiv a_k \pmod {n_k}\\
    \end{array} \right.
      
  eksistē atrisinājums un šis atrisinājums ir viens vienīgs 
  pēc moduļa :math:`N = n_1n_2\cdots{}n_k`. 








Skaitliski piemēri
--------------------

**1.Jautājums:** 
  Atrisināt kongruenču sistēmu:
  
  .. math::
    
    \left\{ \begin{array}{l}
    x \equiv 1 \pmod 3,\\
    x \equiv 4 \pmod 5,\\
    x \equiv 6 \pmod 7.\\
    \end{array} \right.
    
**Procedūra, kā atrisināt šādas sistēmas:**

  Aplūkojam kongruenču sistēmu, kurai visi moduļi ir pa pāriem savstarpēji pirmskaitļi. 

  1. Sākam ar kongruenci, kurā modulis ir vislielākais: :math:`x \equiv a_k \pmod{n_k}`.  
     Pārrakstām to ar izteiksmi, kurā ir mainīgais: :math:`x = n_k j_k + a_k`, kur :math:`j_k`
     ir kāds naturāls skaitlis.
  2. Ievietojam šo izteiksmi mainīgā :math:`x` vietā -- kongruencē ar nākamo lielāko moduli: :math:`n_kj_k+a_k \equiv a_{k-1} \pmod{n_{k-1}}`. 
     Atrodam kādu :math:`j_k`, kuram tas izpildās. Ievietojam to mainīgā :math:`x` izteiksmē un iegūstam 
     jaunu formulu mainīgajam :math:`x`. Piemēram, :math:`x = n_k n_{k-1} j_{k-1}+ a_{k-1}`, kur :math:`j_{k-1}`
     ir kāds naturāls skaitlis. 
  3. Ievietojam šo :math:`x` izteiksmi trešajā lielākajā kongruencē un risinām to, utt. 



**2.Jautājums:** 
  Atrisināt kongruenču sistēmu:
  
  .. math::
    
    \left\{ \begin{array}{l}
    x \equiv 2 \pmod 6,\\
    x \equiv 5 \pmod 9,\\
    x \equiv 7 \pmod 15.\\
    \end{array} \right.
    


**3.Jautājums:**
  Trīs komētas riņķo pa eliptiskām orbītām ap Sauli ar periodiem attiecīgi 
  3, 8 un 13 gadi. 
  To perihēliji (moments, kad komēta ir vistuvāk Saulei) pēdējo reizi 
  iestājās 2020.gadā, 2014.gadā un 2021.gadā. 
  
  Noskaidrot, kurš būs tuvākais gads, kad visām trim komētām perihēlijs
  iestāsies tanī pašā gadā. (Pieņemt, ka apriņķošanas periodi izteikti gados 
  ir veseli skaitļi un komētas neiespaido citu debess ķermeņu gravitācija, izņemot
  Sauli.)


**4.Jautājums:**
  Kādi ir pēdējie divi cipari skaitlī :math:`7^{2021}`?

**5.Jautājums:**
  Atrast mazāko naturālo skaitli, kuru dalot ar :math:`5`, ar :math:`7`, 
  ar :math:`9` un ar :math:`11`, iegūtie atlikumi ir attiecīgi 
  :math:`1`, :math:`2`, :math:`3` un :math:`4`.
  
**6.Jautājums:**
  Kādam virsniekam bija ne vairāk kā :math:`1200` karavīri. 
  
  * Ja tie nostājas rindās pa :math:`5` karavīriem rindā, :math:`3` paliek pāri; 
  * Ja tie nostājas rindās pa :math:`6` karavīriem rindā, :math:`3` paliek pāri; 
  * Ja tie nostājas rindās pa :math:`7` karavīriem rindā, :math:`1` paliek pāri; 
  * Ja tie nostājas rindās pa :math:`11` karavīriem rindā, :math:`0` paliek pāri. 
  
  Cik karavīru bija pavisam?


**7.Jautājums:**
  Tenisa spēlētājai ir pilns grozs ar bumbiņām. 
  Ja tās izņem no groza pa :math:`2`, tad :math:`1` paliek pāri. 
  Ja tās izņem no groza pa :math:`3`, tad :math:`2` paliek pāri. 
  Ja tās izņem no groza pa :math:`4`, :math:`5` vai :math:`6`, tad paliek pāri attiecīgi 
  :math:`3`, :math:`4` vai :math:`5`.
  Toties, ja tās izņem no groza pa :math:`7`, tad nepaliek pāri neviena. 
  Kāds mazākais bumbiņu skaits var būt grozā?


**8.Jautājums:**
  Trim draugiem :math:`A,B,C,D` visiem kopā ir mazāk nekā :math:`200` EUR.
  Zināms, ka katram no viņiem ir vesels daudzums eiru un izpildās sakarības:
  
  * Ja :math:`B` aizņemtos :math:`1` EUR no :math:`A`, tad :math:`B` naudas daudzums 
    būtu :math:`\frac{2}{3}` no :math:`A` naudas daudzuma. 
  * Ja :math:`C` aizņemtos :math:`2` EUR no :math:`B`, tad :math:`C` naudas daudzums 
    būtu :math:`\frac{3}{5}` no :math:`B` naudas daudzuma. 
  * Ja :math:`D` aizņemtos :math:`3` EUR no :math:`C`, tad :math:`D` naudas daudzums 
    būtu :math:`\frac{5}{7}` no :math:`C` naudas daudzuma. 
    
  Kāds ir mazākais naudas daudzums, kas viņiem visiem kopā var piederēt?
  



**9.Jautājums:**
  Kāds ir atlikums, ja skaitli :math:`{\displaystyle 12^{34^{56^{78}}}}`
  dala ar :math:`90`?
  
**10.Jautājums:**
  Atrast pēdējos divus nenulles ciparus skaitļa :math:`2021!` decimālpierakstā.




Sacensību uzdevumi
-------------------

**1.Uzdevums**
  Pierādīt, ka eksistē :math:`99` pēc kārtas sekojoši naturāli skaitļi
  :math:`a_1, a_2, \ldots, a_{99}`, kuriem :math:`a_i` dalās ar kāda naturāla
  skaitļa kubu, kas lielāks par :math:`1`. 

**Ieteikumi:** 
  Lai pamatotu, ka eksistē skaitļi ar noteikta veida 
  neparastu īpašību, sadalām šo īpašību daudzās lineārās kongruencēs 
  (pēc moduļiem, kuri ir savstarpēji pirmskaitļi)
  un risinām šo sistēmu. 

 

**2.Uzdevums (LV.VO.2001.9.1):** 
  Sienāža lēciena garums ir :math:`5`. 
  Viņš sākotnēji atrodas punktā ar koordinātām :math:`(0;0)` 
  un var pārvietoties tikai pa punktiem, kam abas koordinātas ir veseli skaitļi.

  1. Pierādīt, ka sienāzis var nokļūt punktā ar koordinātām :math:`(1;0)`,  
  2. Vai sienāzis var nokļūt jebkurā punktā ar veselām koordinātām?



**3.Uzdevums (LT.VUMIF.2016.10.3):**

  Atrodiet mazāko naturālo skaitli :math:`n`, kuram skaitļi 
  :math:`\sqrt[5]{5n}`, :math:`\sqrt[6]{6n}`, :math:`\sqrt[7]{7n}`
  ir naturāli. 


  Sk. Viļņas universitātes Matemātikas un informātikas fakultātes rīkotā olimpiāde skolēniem:  
  `<http://mif.vu.lt/matematikos-olimpiados/mif/>`_.






**4.Uzdevums (USAMO.2008.1):**
  Pierādīt, ka jebkuram naturālam :math:`n`, eksistē :math:`n+1` 
  savstarpēji pirmskaitļi :math:`k_0,k_1,\ldots,k_n`, kas visi lielāki par :math:`1`, kuriem 
  :math:`k_0 \cdot k_1 \cdot \ldots \cdot k_n - 1`
  ir divu pēc kārtas sekojošu naturālu skaitļu reizinājums.
  

  **Lemma 1:** 
    Ja :math:`t_i^2 + t_i+ 1` dalās ar pirmskaitli :math:`p_i` (:math:`i = 0,\ldots,n`), 
    tad eksistēs arī tāds :math:`t^{\ast}`, kuram :math:`(t^{\ast})^2 + t^{\ast} + 1` dalās
    ar visu šo pirmskaitļu reizinājumu?

  **Lemma 2:** 
    Vai eksistē bezgalīgi daudz pirmskaitļu :math:`p_i`, kuriem 
    var atrisināt :math:`t^2 + t + 1 \equiv 0` pēc :math:`p_i` moduļa? 
    (T.i. polinoma :math:`P(t) = t^2 + t + 1` vērtība kaut kādam 
    :math:`t` dalās ar :math:`p_i`)?




**5.Uzdevums (US.MPGO.2010.2):**
  Pierādīt, ka jebkuram naturālam :math:`n`, eksistē veseli skaitļi :math:`a` un :math:`b`, 
  kuriem :math:`4a^2 + 9b^2 - 1` dalās ar :math:`n`. 


**6.Uzdevums (BW.2016.2):**
  Pierādīt vai apgāzt sekojošus apgalvojumus:  
  
  **(a)** 
    Jebkuram :math:`k \geq 2`, un jebkuriem :math:`k` pēc kārtas sekojošiem naturāliem 
    skaitļiem atradīsies skaitlis, kurš nedalās ne ar vienu pirmskaitli, 
    kas mazāks par :math:`k`.

  **(b)** 
    Jebkuram :math:`k \geq 2`, un jebkurai :math:`k` pēc kārtas sekojošu naturālu 
    skaitļu virknei atradīsies skaitlis, kas ir savstarpējs pirmskaitlis 
    ar visiem citiem virknes locekļiem. 


  
  
**7.Uzdevums:**
  Sauksim režģa punktu :math:`X` rūtiņu plaknē par *redzamu* no 
  koordinātu sākumpunkta :math:`O`, ja nogrieznis :math:`O` nesatur 
  citus režģa punktus, izņemot :math:`O` un :math:`X`. 
  Pierādīt, ka jebkuram naturālam :math:`n` eksistē 
  kvadrāts ar izmēru :math:`n \times n` (kur kvadrāta malas ir 
  paralēlas koordinātu asīm), ka neviens no kvadrātā ietilpstošajiem 
  režģa punktiem nav redzams no koordinātu sākumpunkta.



**8.Uzdevums:**

  Vai eksistē bezgalīgi daudzi Fibonači skaitļi, kuri:    
  Dalās ar :math:`1001` bez atlikuma (atlikums :math:`0`),  

  Vai eksistē bezgalīgi daudzi Fibonači skaitļi, kuri:    
  dod atlikumu :math:`900`, dalot ar :math:`1001`.

  Vai eksistē bezgalīgi daudzi Fibonači skaitļi, kuri:    
  dod atlikumu :math:`1000`, dalot ar :math:`1001`.


  .. note:: 
    Fibonači virkni (:math:`0,1,1,2,3,5,8,13,21,\ldots`) definē šādi:  
    :math:`F_0 = 0`, :math:`F_1 = 1` un :math:`F_{k+1} = F_{k-1}+F_{k}` 
    visiem :math:`k \geq 1`. (Katrs nākamais
    loceklis ir divu iepriekšējo locekļu summa.)


**9.Uzdevums (BW.2016.2)**
  Pierādīt vai apgāzt sekojošus apgalvojumus:  

  1. Jebkuram :math:`k \geq 2`, un jebkuriem :math:`k` pēc kārtas sekojošiem naturāliem 
     skaitļiem atradīsies skaitlis, kurš nedalās ne ar vienu pirmskaitli, kas mazāks par :math:`k`.   

  2. Jebkuram :math:`k \geq 2`, un jebkurai :math:`k` 
     pēc kārtas sekojošu naturālu skaitļu virknei atradīsies skaitlis, 
     kas ir savstarpējs pirmskaitlis ar visiem citiem virknes locekļiem. 
     
     

**Ieteikumi:**
  Otrajā apgalvojumā ar mēģinājumu/kļūdu metodi atrod, ka atbilde ir :math:`17`: 
  Var atrast :math:`17` skaitļu intervālu :math:`[n;n+16]`; 
  kuru var pārklāt ar aritmētiskām progresijām ar diferencēm 
  :math:`d = 2,3,5,7,11,13` (un no katras progresijas virknē ir vismaz 
  divi locekļi).
     