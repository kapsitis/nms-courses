NMS Skaitļu teorija #5: Valuācijas
=====================================



Valuāciju jēdziens
-----------------------

Valuācijas apraksta augstāko pirmskaitļa pakāpi, ar kuru dalās dotais skaitlis. 

* Skaitļu teorijā dažreiz pietiek analizēt situāciju terminos "dalās" vai "nedalās" (no šejienes ir termini  
  *pirmskaitlis*, *savstarpēji pirmskaitļi*, *LKD*, *MKD*). 
* Dažreiz jāaplūko arī moduļi jeb kongruenču klases pēc kāda pirmskaitļa vai pirmskaitļa pakāpes moduļa (par to ir modulārā aritmētika)
* Vēl detalizētāk var aplūkot atlikumus, dalot ar dažādiem pirmskaitļiem (vai dažādu pirmskaitļu pakāpēm) -- ķīniešu atlikumu teorēma. 
* Visbeidzot, valuācijas ir vēl precīzāks instruments -- aplūko "cik laba ir dalāmība" ar kādu pirmskaitli. 




**Definīcija:** 
  Ar :math:`n` apzīmējam jebkuru naturālu skaitli un ar :math:`p` -- kādu pirmskaitli. 
  Par skaitļa :math:`n` :math:`p`-valuāciju sauc tādu skaitli :math:`k`, ka 
  :math:`n` dalās ar :math:`p^k`, bet nedalās ar :math:`p^{k+1}`. 
  Šo faktu pieraksta, izmantojot grieķu burtu "nī": 
  
  .. math:: 
  
    \nu_p(n) = k. 
    
    
  .. figure:: figs-ntjun05-valuations/greek-alphabet.png
     :width: 2in
     :alt: Greek alphabet
     
     Grieķu alfabēts
  
**Piemēri:**
  Ja pirmskaitlis :math:`p = 3`, tad 
  
  .. math::
    
    \left\{
    \begin{array}{l}
    \nu_3(1) = \nu_3(2) = \nu_3(4) = \nu_3(5) = \ldots = 0\\
    \nu_3(3) = \nu_3(6) = \nu_3(12) = \nu_3(15) = \ldots = 1\\
    \nu_3(9) = \nu_3(18) = \nu_3(36) = \nu_3(45) = \ldots = 2\\
    \nu_3(27) = \nu_3(54) = \ldots = 3\\
    \nu_3{81} = \ldots = 4\\
    \ldots
    \end{array}
    \right.


Funkcijas :math:`f(n) = \nu_3(n)` grafiks redzams zīmējumā -- 
tā ir zāģveidīga trepīte, kurā ar regulārām atstarpēm rodas arvien garāki 
"zāģa zobi". 

.. image:: figs-ntjun05-valuations/valuations-by-3-all-naturals.png
   :width: 4in



**Valuāciju īpašības:** 
  Iedomāsimies, ka :math:`p` ir jebkurš fiksēts pirmskaitlis. 

  * :math:`\nu_p(a) = \infty` tad un tikai tad, ja :math:`a = 0`. (Visiem citiem veseliem skaitļiem 
    atrodas tik augsta pirmskaitļa :math:`p` pakāpe :math:`p^{k+1}`, ka :math:`a` vairs nedalās ar :math:`p^{k+1}`.)
  * :math:`\nu_p(ab) = \nu_p(a) + \nu_p(b)`. (Augstākās pakāpes saskaitās, ja abus skaitļus :math:`a` un :math:`b` reizina.)
  * :math:`\nu_p(a + b) \geq \min(\nu_p(a), \nu_p(b))`. Šajā izteiksmē pastāv vienādība, ja \math:`\nu_p(a) \neq \nu_p(b)`. 



Valuācijas kombinatorikā
----------------------------

Ležandra teorēma
^^^^^^^^^^^^^^^^^^

**Teorēma (Adrien-Marie Legendre):**
  Katram pirmskaitlim :math:`p` un katram naturālam :math:`n` :math:`p`-valuācija ir aprēķināma pēc formulas

  .. math:: 
  
    \nu_p(n!) = \sum_{i=1}^{\infty} \left\lfloor \frac{n}{p^i} \right\rfloor, 
    
  kur :math:`\lfloor x \rfloor` apzīmē apakšējo veselo daļu. 
  (Izskatās, ka šajā vienādībā ir bezgalīga summa, bet jebkurām :math:`n` un :math:`p` vērtībām 
  šajā summā ir tikai galīgs skaits nenulles saskaitāmo.)

  .. image:: figs-ntjun05-valuations/legendre-example-2.png
     :width: 2.5in
     

**Piemērs:** 
  Ar kādu lielāko :math:`2` pakāpi dalās skaitlis :math:`36!`? 
  
  .. image:: figs-ntjun05-valuations/legendre-36-factorial.png
     :width: 3in
     
  Zīmējumā redzami visi reizinātāji, kuri veido :math:`36!`. 
  Tie, kuri dalās ar :math:`2`, attēloti ar klucīšu stabiņu, kas
  rāda, cik divniekus (kā pirmreizinātājus) šis skaitlis pievienojis
  faktoriālam. 
  
  .. image:: figs-ntjun05-valuations/legendre-36-expression.png
     :width: 3in
     
  Rēķinot faktoriālu, klucīši summējas pa kolonnām. 
  Ležandra formula tos saskaita pa rindiņām (vispirms sarkanos, tad oranžos, 
  utt.)




Kummera teorēma
^^^^^^^^^^^^^^^^

**Teorēma (Ernst Kummer)**
  Doti skaitļi :math:`n` un :math:`m`, kas apmierina nevienādības :math:`n \geq m \geq 0` un 
  arī pirmskaitlis :math:`p`. Tad binomiālajam koeficientam :math:`C_n^m` :math:`p`-valuācija 
  sakrīt ar pārnesumu skaitu, ja :math:`m` saskaita ar :math:`n-m` skaitīšanas sistēmā ar bāzi :math:`p`. 
  
Šo teorēmu var pierādīt, izsakot binomiālo koeficientu: 

.. math::

  C_n^m = \frac{n!}{m! (n-m)!}
  
un izmantojot Ležandra teorēmu. 


.. note:: 
  Par kombināciju jeb bionmiālo koeficientu skaitļu teorijas īpašībām ir 
  vēl arī citi derīgi rezultāti (sal. Lūkas teorēmu `<https://bit.ly/3Frc1pT>`_), bet 
  tie neattiecas uz veselo skaitļu funkciju tēmu.  



Kāpinātāja pacelšanas lemmas
-------------------------------

Kāpinātāja pacelšanas lemmas (Lifting the Exponent Lemmas) ir vairāki savstarpēji 
saistīti rezultāti, kuri ļauj atrast :math:`p`-valuācijas divu skaitļu pakāpju 
starpībai vai summai. 



Šajā nodaļā aplūkosim vienkāršāko gadījumu, ja :math:`p` ir nepāra skaitlis. 

**Piemērs (UKMO2013):**
  Skaitlis pierakstīts decimālās sistēmas bāzē satur :math:`3^{2013}` ciparus :math:`3`; 
  citu ciparu skaitļa pierakstā nav. Atrast augstāko skaitļa :math:`3` pakāpi, kas dala šo skaitli.

**Ieteikums:**
  Var aplūkot iesākumā mazāku skaitli, kura decimālpierakstā ir :math:`27` trijnieki (jeb :math:`3^3`): 
  
  .. math::
  
    N = 333\,333\,333\,\,333\,333\,333\,\,333\,333\,333
    
  Šo skaitli var sadalīt vairākos reizinātājos (katrs reizinātājs dalās ar :math:`3`, bet nedalās ar :math:`9`
  (var pārbaudīt ar ciparu summām). Tas ļauj droši noskaidrot, ar kādu :math:`3` pakāpi dalās :math:`N`.




**Apgalvojums 1:**
  Doti divi veseli skaitļi :math:`x` un :math:`y` un arī naturāls 
  skaitlis :math:`n \in \mathbb{N}`. 
  Dots arī pirmskaitlis :math:`p` (var būt arī :math:`p = 2`). 
  Izpildās šādi nosacījumi: 
  
  * :math:`n` nedalās ar :math:`p`. 
  * :math:`x,y` nedalās ar :math:`p`. 
  * :math:`x - y` dalās ar :math:`p`. 
  
  Tad izpildās vienādība: 
  
  .. math::
   
    \nu_p(x^n - y^n) = \nu_p(x - y). 
  
**Piemērs 1:** 
  :math:`x = 10`, :math:`y = 1`, :math:`n = 7`, bet :math:`p = 3`. 
  Tad skaitlis :math:`x^7 - y^7 = 10^7 - 1^7 = 9999999` dalās ar :math:`3^2 = 9`, 
  bet nedalās ar :math:`3^3 = 27`. (Tāpat kā skaitlis :math:`x - y = 10-1=9`.) 


**Pierādījums:** Apgalvojumu 1 pierāda, sadalot :math:`x^n - y^n` 
reizinātājos. Un tad pamatojot, ka summa 

.. math::

  x^{n-1} + x^{n-2}y + \ldots + xy^{n-2} + y^{n-1} \equiv nx^{n-1}
  
nedalās ar :math:`p`. :math:`\square`


**Apgalvojums 2:**
  Doti divi veseli skaitļi :math:`x` un :math:`y` un arī naturāls 
  skaitlis :math:`n \in \mathbb{N}`. 
  Dots arī pirmskaitlis :math:`p` (var būt arī :math:`p = 2`). 
  Izpildās šādi nosacījumi: 
  
  * :math:`n` ir nepāra skaitlis.
  * :math:`n` nedalās ar :math:`p`. 
  * :math:`x,y` nedalās ar :math:`p`. 
  * :math:`x - y` dalās ar :math:`p`.
  
  
  Tad izpildās vienādība: 
  
  .. math::
   
    \nu_p(x^n + y^n) = \nu_p(x + y). 

**Piemērs 2:** 
  :math:`x = 10`, :math:`y = 1`, :math:`n = 7`, bet :math:`p = 11`. 
  Tad skaitlis :math:`x^7 + y^7 = 10^7 + 1^7 = 10000001` dalās ar :math:`11^1 = 11`, 
  bet nedalās ar :math:`11^2 = 121`. (Tāpat kā skaitlis :math:`x + y = 11`.)
  
Turpmākajos piemēros nometam prasību, ka :math:`n` nedalās ar :math:`p`. 
Toties papildus prasām, lai pirmskaitlis :math:`p` būtu nepāra skaitlis.
Ir spēkā vairākas kāpinātāja pacelšanas lemmas: 


**Pierādījums:** Apgalvojumu 2 pierāda, ievietojot :math:`y` vietā 
:math:`-y` un lietojot iepriekšējo Apgalvojumu 1.  :math:`\square`


**Lemma 1 (Lifting the Exponent, LTE):** 
  Doti divi veseli skaitļi :math:`x` un :math:`y` un arī naturāls 
  skaitlis :math:`n \in \mathbb{N}`. 
  Dots arī **nepāra** pirmskaitlis :math:`p`. 
  Izpildās šādi nosacījumi: 
  
  * :math:`x,y` nedalās ar :math:`p`. 
  * :math:`x - y` dalās ar :math:`p`. 
  
  Tad izpildās vienādība: 
  
  .. math::
   
    \nu_p(x^n - y^n) = \nu_p(x - y) + \nu_p(n). 

**Piemērs 3:** 
  :math:`x = 10`, :math:`y = 1`, :math:`n = 27`, bet :math:`p = 3`. 
  Tad skaitlis 
  
  .. math::
  
    x^{27} - y^{27} = 10^7 - 1^7 = 999999999\,999999999\,999999999

  dalās ar :math:`3^k` pie :math:`k = \nu_3(10-1) + \nu_3(27) = 2 + 3 = 5`
  (t.i. dalās ar  :math:`3^6 = 243`). 
  Bet šis skaitlis nedalās ar :math:`3^{k+1}` (t.i. ar :math:`3^6 = 729`). 


Aplūkojot jebkādas :math:`n` vērtības, iegūstam grafiku funkcijai 
:math:`f(n) = \nu_3(10^n - 1)`, t.i. ar kādu augstāko trijnieka
pakāpi dalās skaitlis ":math:`n` deviņnieki": 

.. image:: figs-ntjun05-valuations/valuations-by-3.png
   :width: 3in


**Pierādījums:** Lemmu 1 pierāda, atkārtoti dalot reizinātājos 
izteiksmi :math:`x^n - y^n`, kur var izteikt :math:`n = k \cdot p^m`
(kur :math:`k` nedalās ar :math:`p`):

.. image:: figs-ntjun05-valuations/lte-lemma-proof.png
   :width: 3in



   


**Lemma 2 (Lifting the Exponent, LTE):** 
  Doti divi veseli skaitļi :math:`x` un :math:`y` un arī naturāls 
  skaitlis :math:`n \in \mathbb{N}`. 
  Dots arī **nepāra** pirmskaitlis :math:`p`. 
  Izpildās šādi nosacījumi: 
  
  * :math:`n` ir nepāra skaitlis.
  * :math:`x,y` nedalās ar :math:`p`. 
  * :math:`x + y` dalās ar :math:`p`. 
  
  Tad izpildās vienādība: 
  
  .. math::
   
    \nu_p(x^n + y^n) = \nu_p(x + y) + \nu_p(n). 


**Piemērs 4:** 
  :math:`x = 10`, :math:`y = 1`, :math:`n = 121`, bet :math:`p = 11`. 
  Tad skaitlis 
  
  .. math::
  
    x^{121} + y^{27} = 10^{121} + 1^{121} = 1\underbrace{00\ldots00}_{120 nulles}1

  dalās ar :math:`11^k` pie :math:`k = \nu_{11}(10+1) + \nu_{11}(121) = 1+2 = 3`
  (t.i. dalās ar  :math:`11^3 = 1331`). 
  Bet šis skaitlis nedalās ar :math:`{11}^{k+1}` (t.i. ar :math:`11^4 = 14641`). 


**Pierādījums:** 
  Lemmu 2 pierāda, aizstājot :math:`y` ar :math:(-y) un izmantojot iepriekšējo 
  Lemmu 1. (Šeit ir būtiski, lai :math:`n` ir nepāra; lai gan pats 
  :math:`y`, gan arī :math:`(-y)^{n}` maina zīmi. :math:`\square`







Skaitliski piemēri
^^^^^^^^^^^^^^^^^^^^

**1.jautājums:**
  Ar cik nullēm beidzas skaitlis :math:`2022!` (:math:`2022` faktoriāls, t.i. visu skaitļu no :math:`1` līdz :math:`2022` reizinājums)?
  
**2.jautājums:**  
  Ar kādu lielāko skaitļa :math:`2` pakāpi dalās kombinācija :math:`C^{415}_{2022}`? 

**3.jautājums:** 
  Atrast mazāko :math:`k` vērtību, kurai :math:`11^{k} - 1` beidzas ar :math:`4` nullēm. 
  
**4.jautājums:**
  Atrast :math:`5`-valuāciju reizinājumam
  
  .. math::
  
     (2-1) \cdot (2^2-1) \cdot (2^3 - 1) \cdot \ldots \cdot (2^{1000} - 1).
     
**5.jautājums:**
  Atrast :math:`7`-valuāciju reizinājumam
  
  .. math::
  
     (2-1) \cdot (2^2-1) \cdot (2^3 - 1) \cdot \ldots \cdot (2^{1000} - 1).
     

**6.jautājums:** 
  Neizmantojot Kummera teorēmu (bet izmantojot interpretāciju) 
  pamatot, ka :math:`C_{2012}^{17}`: dalās ar :math:`2012`. 
  (**Ieteikums:** Izmantot faktu, ka :math:`17` un :math:`2012` ir 
  savstarpēji pirmskaitļi un tādēļ kombinācijām :math:`C_{2012}^{17}`, 
  ko iztēlojas kā pa apli izvietotas :math:`2012` krellītes, no kurām 
  tieši :math:`17` ir nokrāsotas - būs simetriskas attiecībā pret 
  :math:`2012` pagriezieniem ap apļa centru.)
  
Diemžēl, šo nevar izspriest otrādi. No tā, ka :math:`k` un :math:`2012` 
ir kopīgi dalītāji vēl neseko, ka :math:`C_{2012}^{17}` nedalās ar :math:`2012`. 
  
     


.. image:: figs-ntjun05-valuations/kummer-binary-numbers.png
   :width: 1.5in
   
   


Sacensību uzdevumi
^^^^^^^^^^^^^^^^^^^

**1.uzdevums:**
  Pamatot, ka harmoniskas rindas pirmo :math:`n` locekļu summa: 
  
  .. math:: 
  
    1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \ldots + \frac{1}{n}
    
  nevar būt vesels skaitlis, ja :math:`n > 1`. 
  

**2.uzdevums (CGMO2012.8)**
  Cik kopā :math:`\{0,1,2,\ldots,2012\}` ir elementu :math:`k`, kam :math:`C_{2022}^k`: dalās ar :math:`2012`?
  Ar :math:`C_n^k` apzīmējam kombinācijas no :math:`n` pa :math:`k` jeb
  
  .. math:: 
  
    C_n^k = \frac{n!}{k!(n-k)!}
    
**3.uzdevums (IMO2019.P4)**
  Atrast visus naturālo skaitļu :math:`(k,n)` pārus, kuriem izpildās
  
  .. math::
  
    k! = (2^n - 1)(2^n - 2)(2^n - 4)\cdots(2^n - 2^{n-1}).
    
**4.uzdevums (IMO2000.5):**
  Vai eksistē naturāls :math:`n`, ka skaitlim :math:`n` ir tieši :math:`2000` dalītāji, kuri ir pirmskaitļi, un 
  :math:`2^n+1` dalās ar :math:`n`. (Skaitlis :math:`n` drīkst dalīties arī ar pirmskaitļu pakāpēm.)


**5.uzdevums (APMO1997.2):**
  Atrast veselu skaitli :math:`n`, kam :math:`100 \leq n \leq 1997`, ka :math:`n` dala :math:`2^n + 2`. 


**6.uzdevums (Sierpinski):**
  Pierādīt, ka nevienam :math:`n > 1` neizpildās 
  
  .. math:: 
  
    n \mid 2^{n-1} + 1. 
    
    
**7.uzdevums (IMO1990.3):**
  Noteikt visus veselos skaitļus :math:`n>1`, kam :math:`\frac{2^n + 1}{n^2}` ir vesels skaitlis. 






Atsauces
----------

1. `<https://cp4space.hatsya.com/2014/04/13/lifting-the-exponent/>`_. 
2. `<https://bit.ly/3KdtxBH>`_. 


