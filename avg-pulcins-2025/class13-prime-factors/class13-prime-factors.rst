Pirmskaitļi un pirmreizinātāji
================================

**Iesildīšanās:** 
  Izteikt dažus skaitļus (piemēram, :math:`90, 210, 630, 1000, 1600`) kā divu skaitļu 
  reizinājumus :math:`a \cdot b` (:math:`a \leq b`) visos iespējamajos veidos. 
  Katram skaitlim saskaitīt veidus; arī pamanīt, kuri divi ir savstarpēji "tuvākie" reizinātāji.

**Definīcija:** 
  Naturālu skaitli :math:`p>1` sauc par *pirmskaitli*, ja tas dalās 
  tikai ar :math:`1` un ar pašu :math:`p`. 

  Piemēram, :math:`2027` ir pirmskaitlis -- tas nedalās ne ar vienu pirmskaitli, 
  kas nepārsniedz :math:`\sqrt{2027} \approx 45`.  
  Skaitlis :math:`2025 = 45^2` nav pirmskaitlis. 

**Teorēma:** 
  Katru naturālu skaitli :math:`n > 1` var tieši vienā veidā izteikt kā pirmskaitļu reizinājumu
  (tos sauc par pirmreizinātājiem).  

  :math:`90 = 6 \cdot 15 = (2 \cdot 3) \cdot (3 \cdot 5)`. Arī :math:`90 = 9 \cdot 10 = (3 \cdot 3) \cdot (2 \cdot 5)`. 
  :math:`2025 = 45^2 = (5 \cdot 9)^2 = 5^2 \cdot 9^2 = 3^4 \cdot 5^2`. 

**Definīcija:** 
  Par naturāla skaitļa :math:`n` *dalītāju skaita funkciju* sauc :math:`d(n)` -- visu 
  skaitļa :math:`n` pozitīvo dalītāju skaitu.

  Piemēram, :math:`d(1) = 1`; :math:`d(p) = 2` (katram pirmskaitlim :math:`p` ir divi pozitīvi dalītāji), 
  :math:`d(90) = 12` (skaitļa :math:`90` dalītāji ir :math:`1,2,3,5,6,9,10,15,18,30,45,90`). 


**Apgalvojums:**
  Skaitlim, kas izteikts kā pirmreizinātāju pakāpes :math:`n = p_1^{a_1}p_2^{a_2}\cdots{}p_k^{a_k}`, 
  pozitīvo dalītāju skaits: 

  .. math:: 
  
    d(n) = \left(a_1+1\right) \cdot \left( a_2+1 \right) \cdot \cdots \cdot \left( a_k + 1 \right). 
  
**Apgalvojums:** 
    Lai skaitlis :math:`n` būtu pilns kvadrāts (izsakāms kā :math:`n = k^2`) ir nepieciešami 
    un pietiekami, lai tā sadalījumā pirmreizinātājos :math:`n = p_1^{a_1}p_2^{a_2}\cdots{}p_k^{a_k}`
    visi :math:`a_1,a_2,\ldots,a_k` būtu pāra skaitļi. 
    
    Līdzīga pazīme: pilniem kvadrātiem pozitīvo dalītāju funkcija :math:`d(n)` ir ar nepāra vērtību.


**Definīcija:**
  Par veselu skaitļu :math:`m` un :math:`n` **lielāko kopīgo dalītāju (LKD)** sauc
  lielāko naturālo skaitli, ar kuru tie abi dalās. To apzīmē ar :math:`\text{LKD}(m,n)`.

  Skaitļus :math:`m` un :math:`n` sauc par *savstarpējiem pirmskaitļiem*, ja
  :math:`\text{LKD}(m,n)=1`.

**Apgalvojums:** 
  Ja divi skaitļi sadalīti pirmreizinātājos, tad to 
  lielākais kopīgais dalītājs iegūstams, katru pirmreizinātāju kāpinot 
  mazākajā no abām pakāpēm: 

  =======================  =============================  =============================  =============================  =============================
  Pirmreizinātājs          :math:`2`                      :math:`3`                      :math:`5`                      :math:`7`
  :math:`300`              :math:`\textcolor{red}{2^2}`   :math:`\textcolor{blue}{3^1}`  :math:`\textcolor{red}{5^2}`   :math:`\textcolor{blue}{7^0}`
  :math:`630`              :math:`\textcolor{blue}{2^1}`  :math:`\textcolor{red}{3^2}`   :math:`\textcolor{blue}{5^1}`  :math:`\textcolor{red}{7^1}`
  =======================  =============================  =============================  =============================  =============================

  No šī piemēra redzam, ka :math:`\text{LKD}(300,630) = \textcolor{blue}{2^1}\cdot \textcolor{blue}{3^1}\cdot\textcolor{blue}{5^1}\cdot\textcolor{blue}{7^0} = 30`.

**Eiklīda algoritms:** 
  Praksē divu skaitļu LKD var atrast ar *Eiklīda algoritmu* -- lielāko skaitli atkārtoti
  aizstāj ar atlikumu, kas rodas, dalot lielāko ar mazāko. Tad, kad izdalās bez atlikuma, 
  pēdējais dalītājs ir LKD: 

  .. math:: 
    
    \text{LKD}(300, 210) = \text{LKD}(210, 90) = \text{LKD}(90, 30) = \text{LKD}(30, 0) = 30.


**LV.SOL.2020.8.3:** 
  Atrast tādu divpadsmitciparu skaitli (kas nesatur ciparu 0) tā, lai katri 
  divi blakus uzrakstīti cipari veidotu pirmskaitli un visi šie pirmskaitļi būtu dažādi!

**LV.SOL.2017.8.1:** 
  Atrast mazāko naturālo skaitli, kura ciparu reizinājums ir :math:`210` un kas dalās ar :math:`9`.

**LV.SOL.2014.7.3:** 
  Vai var atrast tādus trīs naturālus skaitļus :math:`a`, :math:`b` un :math:`c`, ka
  :math:`(a+b)(b+c)(c+a)=20142013`?

**LV.SOL.2014.8.4:** 
  Ar :math:`\overline{xyz}` apzīmēsim trīsciparu skaitli ar cipariem
  :math:`x` (simti), :math:`y` (desmiti) un :math:`z` (vieni). 
  
  Pierādīt: ja :math:`\overline{abc}` dalās ar :math:`37`, tad arī
  :math:`\overline{bca} + \overline{cab}` dalās ar :math:`37`.


**LV.SOL.2013.7.5:** 
  Vai naturāla skaitļa kvadrāts (reizinājums pašam ar sevi) var būt skaitlis 
  **(A)** :math:`\overline{AABB}`, **(B)** :math:`\overline{ABAB}`, kur 
  :math:`A` un :math:`B` ir dažādi cipari. 

**LV.SOL.2013.8.1:** 
  Cik starp pirmajiem :math:`2012` naturāliem skaitļiem ir tādi, kas 
  nedalās ne ar :math:`5`, ne ar :math:`7`?

**LV.SOL.2011.8.5:** 
  Pie sienas ir lampiņas, kas pēc kārtas sanumurētas ar naturāliem 
  skaitļiem no :math:`2` līdz :math:`N`. Vadības panelī ir slēdži, kuri numuri ir 
  pēc kārtas sekojoši pirmskaitļi, sākot no :math:`2` (pēdējā slēdža 
  numurs ir pirmskaitlis, kas pārsniedz :math:`N`). Kad pārslēdz slēdzi ar 
  numuru :math:`K`, visas lampiņas, kuru numuri dalās ar :math:`K`, maina savu stāvokli 
  (no ieslēgtas uz izslēgtu vai no izslēgtas uz ieslēgtu). Sākumā visas 
  lampiņas ir izslēgtas. Zināms, ka ar slēdžu palīdzību var panākt, ka visas 
  lampiņas vienlaicīgi ir ieslēgtas. Kādai lielākajai :math:`N` vērtībai tas ir
  iespējams?

**LV.SOL.2010.7.1:**
  Kāds lielākais daudzums pirmskaitļu var būt starp :math:`12` 
  pēc kārtas ņemtiem naturāliem skaitļiem?

**LV.SOL.2010.8.2:**
  Ir zināms, ka no apgalvojumiem ":math:`x^3` dalās ar :math:`2`"; 
  ":math:`x^3` dalās ar :math:`4`"; 
  ":math:`x^3` dalās ar :math:`8`"; 
  ":math:`x^3` dalās ar :math:`16`". 
  vismaz viens ir patiess un vismaz viens ir aplams 
  (:math:`x` ir naturāls skaitlis). 
  Kuri apgalvojumi ir patiesi, kuri -- aplami? 

**LV.SOL.2009.8.1:**
  Kādu lielāko daudzumu no naturāliem skaitļiem 
  :math:`1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12` var sadalīt divās grupās tā, 
  lai abās grupās ietilpstošo skaitļu reizinājumi būtu vienādi savā starpā? 