Skaitļu Teorija 2021-09-20
==========================

Par šo LU NMS atbalstīto pasākumu atbild ``kalvis.apsitis@gmail.com``.

*Atbildes uz testa uzdevumiem ir nelieli veseli skaitļi. Drīkst izmantot datorprogrammas, kalkulatoru, Internetu,
grmāmatas, pierakstus un citus palīglīdzekļus, bet nedrīkst sazinaties ar citiem cilvēkiem.*

**LV.IK2022.NT1.01**
  Dots taisnstūra paralēlskaldnis :math:`ABCDA_1B_1C_1D_1` ar
  izmēriem :math:`30 \times 72 \times 100`, tas salikts no vienības kubiņiem
  ar izmēriem :math:`1 \times 1 \times 1`.
  Cik daudzus no šiem kubiņiem šķērso diagonāle :math:`AC_1`?
  (Ja diagonāle tikai pieskaras vienības kubiņa virsotnei vai šķautnei, to neuzskata par šķērsošanu.)

  **Atbilde:** :math:`184`

  :math:`\mbox{LKD}(30,72,100) = 2`, tāpēc lielā paralēlskaldņa vietā var aplūkot
  divus mazākus: :math:`15 \times 36 \times 50`. 

  **Apgalvojums 1:** Taisnstūra paralēlskaldņa gabarītus apzīmējam ar
  :math:`L`, :math:`W`, :math:`H` (garums, platums, augstums).
  Ja :math:`L,W,H` ir *pa pāriem savstarpēji pirmskaitļi*, tad diagonāle
  šķērso :math:`(L+W+H) - 2` kubiņus, lai no kreisā, apakšējā, priekšējā kubiņa
  tiktu līdz labajam, augšējam, aizmugurējam kubiņam.

  **Pierādījums:** Jauns kubiņš tiek šķērsots tad, ja
  kāda no koordinātēm :math:`x`, :math:`y`, :math:`z` palielina savu veselo daļu (piemēram,
  :math:`\lfloor x \rfloor` pāriet uz nākamo veselo skaitli). Pirmajam kubiņam koordināšu veselās daļas ir
  :math:`(x,y,z) = (0,0,0)`, bet pēdējam kubiņam (īsi pirms diagonāle iziet no paralēlskaldņa)
  koordinātes ir :math:`(x,y,z) = (L-1,W-1,H-1)`.
  Tā kā L,W,H ir pa pāriem savstarpēji pirmskaitļi, tad nav iespējama situācija, ja
  diagonāle paralēlskaldņa iekšpusē **vienlaikus** palielina vairāku koordinātu veselās daļas
  (ja, teiksim, kādam diagonāles punktam :math:`(x,z)` ir abi veseli skaitļi, tad projicējot
  attēlu plaknē :math:`xOz`, iegūsim, ka :math:`x` gabarītizmērs (garums :math:`L`) un
  :math:`z` gabarītizmērs (paralēlskaldņa augstums :math:`H`) nav savstarpēji pirmskaitļi. Pretruna.

  Tāpēc koordināšu palielināšanās vienmēr notiek pa vienai. Pavisam ir :math:`(L-1) + (W-1) + (H-1)`
  palielināšanās reižu (pa ceļam no kubiņa :math:`(x,y,z) = (0,0,0)` līdz kubiņam
  :math:`(x,y,z) = (L-1,W-1,H-1)`). Bet šai summai :math:`(L-1) + (W-1) + (H-1)` vēl jāpieskaita :math:`1`,
  jo abi malējie kubiņi ir ieskaitīti. :math:`\blacksquare`


  Šo apgalvojumu sākotnējā veidā tomēr izmantot nevar, jo
  mūsu aplūkojamiem paralēlskaldņu izmēriem :math:`15 \times 36 \times 50` ir
  lielākie kopīgie dalītāji :math:`>1`. Konkrēti: :math:`\mbox{LKD}(15,36) = 3`,
  :math:`\mbox{LKD}(15,50) = 5`, :math:`\mbox{LKD}(36,50) = 2`.
  
  Aplūkojam materiālu punktu, kurš pārvietojas trīsdimensiju telpā (pa paralēlskaldna :math:`15 \times 36 \times 50` diagonāli), 
  ja laiks :math:`t \in [0;1]`, 
  bet koordinātes nosaka šādi vienādojumi: 
  
  .. math::
    
	\left\{
    \begin{array}{l}
    x = 15t\\
    y = 36t\\
    z = 50t\\
    \end{array} \right.

  Tā kā :math:`\mbox{LKD}(15,36) = 3`, tad laika momentos :math:`t = 1/3` un :math:`t = 2/3`, 
  abas koordinātes :math:`x` un :math:`y` vienlaikus kļūs veselas (tātad paralēlskaldņa diagonāle
  "pieskarsies šķautnei", kas atdala divus kubiņus, tādēļ tā šajos laika momentos šķērsos par 
  vienu kubiņu mazāk nekā paredzētu apgalvojums (kur :math:`x,y,z` bija pa pāriem savstarpēji pirmskaitļi). 
  Līdzīgi (bet ar citiem koordinātu pāriem) notiks arī tad, ja :math:`t \in \{ 1/5, 2/5, 3/5, 4/5 \}`
  kā arī tad, ja :math:`t = 1/2`. 
  
  Pavisam šādu :math:`t` vērtību ir 
  
  .. math:: 
    
    (\mbox{LKD}(15,36) -1 ) + (\mbox{LKD}(15,50) -1 ) + (\mbox{LKD}(36,50) - 1) = (3 - 1) + (5 - 1) + (2 - 1) = 7.
	
  Tātad, paralēlskaldnī :math:`15 \times 36 \times 50` šķērsoto kubiņu skaits:
  
  .. math::
   
    (L + W + H - 2) - \left( (\mbox{LKD}(L,W) -1 ) + (\mbox{LKD}(L,H) -1 ) + (\mbox{LKD}(W,H) - 1) \right) = 99 - 7 = 92.
	
  Sākotnējā paralēlskaldnī  :math:`30 \times 72 \times 100` tiks šķērsoti :math:`2 \cdot 92 = 184` kubiņi.

  :math:`\square`



**LV.IK2022.NT1.02**
  Aplūkosim :math:`700` skaitļu reizinājumu :math:`(2-1)(4-1)\ldots{}(2^{700} - 1)`:

  .. math::

    N = \prod\limits_{k=1}^{700} \left( 2^k - 1 \right).

  Apzīmēsim ar :math:`\nu_5(N) = a` lielāko skaitļa :math:`5` pakāpi, ar ko dalās `N`
  (t.i. :math:`N` dalās ar :math:`5^{a}`, bet vairs nedalās ar :math:`5^{a+1}`).
  Līdzīgi apzīmējam ar :math:`\nu_7(N)` lielāko skaitļa :math:`7` pakāpi, ar ko dalās :math:`N`
  (to sauc par skaitļa :math:`N` :math:`7`-valuāciju).

  .. math::

    \Delta = \nu_5(N) - \nu_7(N).

  Ierakstīt atbildē veselu skaitli :math:`\Delta`: abu valuāciju starpību.

  **Atbilde:** :math:`\mathtt{-52}`

  Pamatosim, ka :math:`\Delta = \nu_5(N) - \nu_7(N) = 218 - 270 = -52`.
  Rakstām kāpinātāja pacelšanas lemmu:

  **Lemma:** Ja :math:`p` ir nepāra pirmskaitlis un
  :math:`p \mid (x-y)` (bet paši :math:`x,y` ar :math:`p` nedalās),
  tad :math:`\nu_p(x^n-y^n) = \nu_p(x-y)+\nu_p(n)`.
  (Sk. pierādījumu `<https://bit.ly/3jvJZkW>`_)

  * Pirmskaitlim :math:`p = 5` var lietot šo lemmu skaitļiem :math:`x = 16` un
    :math:`y = 1`, jo :math:`16 - 1` dalās ar :math:`5`.
  * Pirmskaitlim :math:`p = 7` var lietot šo lemmu jau skaitļiem :math:`x = 8` un
    :math:`y = 1`, jo :math:`8 - 1` dalās ar :math:`7`.

  Šis novērojums izskaidro, kāpēc 7-valuācijas skaitļiem :math:`N` (sk. uzdevuma formulējumu)
  aug straujāk nekā 5-valuācijas, ja :math:`k` pieaug.
  
  Sākam izrakstīt pēc šīs lemmas tās 5-valuācijas, kuras lielākas par nulli (nerakstām 
  tos reizinātājus, kuriem :math:`2^k - 1` vispār nedalās ar :math:`5`: 
  
  .. math::
  
    \begin{array}{l}
    \nu_5(2^4 -1) = \nu_5(16^1 - 1^1) = \nu_5(16 - 1) + \nu_5(1) = 1 + 0 = 1\\
    \nu_5(2^8 -1) = \nu_5(16^2 - 1^2) = \nu_5(16 - 1) + \nu_5(2) = 1 + 0 = 1\\
    \nu_5(2^{12} -1) = \nu_5(16^3 - 1^3) = \nu_5(16 - 1) + \nu_5(3) = 1 + 0 = 1\\
    \nu_5(2^{16} -1) = \nu_5(16^4 - 1^4) = \nu_5(16 - 1) + \nu_5(4) = 1 + 0 = 1\\
    \nu_5(2^{20} -1) = \nu_5(16^5 - 1^5) = \nu_5(16 - 1) + \nu_5(5) = 1 + 1 = 2\\
    \nu_5(2^{24} -1) = \nu_5(16^6 - 1^6) = \nu_5(16 - 1) + \nu_5(6) = 1 + 0 = 1\\
    \ldots\\
    \nu_5(2^{96} -1) = \nu_5(16^{24} - 1^{24}) = \nu_5(16 - 1) + \nu_5(24) = 1 + 0 = 1\\
    \nu_5(2^{100} -1) = \nu_5(16^{25} - 1^{25}) = \nu_5(16 - 1) + \nu_5(25) = 1 + 2 = 3\\
    \ldots\\
    \nu_5(2^{500} -1) = \nu_5(16^{125} - 1^{125}) = \nu_5(16 - 1) + \nu_5(125) = 1 + 3 = 4\\
    \ldots\\
    \nu_5(2^{700} -1) = \nu_5(16^{175} - 1^{175}) = \nu_5(16 - 1) + \nu_5(175) = 1 + 2 = 3\\
    \end{array}
	
  No šīm vienādībām redzam, ka katrs ceturtais reizinātājs pievieno 700 reizinātāju izteiksmei :math:`\nu_5(N)`
  vienu piecinieku jeb :math:`5^1`, katrs divdesmitais pievieno divus pieciniekus jeb :math:`5^2`, 
  katrs simtais pievieno trīs pieciniekus, bet katrs piecsimtais pievieno četrus pieciniekus: 
  
  .. math:: 
  
    \nu_5(N) = \left\lfloor \frac{700}{4} \right\rfloor + \left\lfloor \frac{700}{20} \right\rfloor + 
    \left\lfloor \frac{700}{100} \right\rfloor + \left\lfloor \frac{700}{500} \right\rfloor  = 175 + 35 + 7  + 1 = 218.
	
  Līdzīgi atrod 7-valuāciju: 

  .. math::
  
    \nu_5(N) = \left\lfloor \frac{700}{3} \right\rfloor + \left\lfloor \frac{700}{21} \right\rfloor + 
    \left\lfloor \frac{700}{147} \right\rfloor = 233 + 33 + 4 = 270.
  
  Abu šo lielumu starpība ir :math:`218 - 270 = -52`.

  :math:`\square`

  .. note::
    Šis testa jautājums ir iedvesmojies no 2019.g.\ Starpautiskās olimpiādes uzdevuma:

    **IMO2019.P4.** Atrast visus naturālo skaitļu :math:`(k,n)` pārus, kuriem izpildās

    .. math::

      k! = (2^n - 1)(2^n - 2)(2^n - 4) \cdots (2^n - 2^{n-1}).

    *Ieteikums:* Zinot kāpinātāja pacelšanas lemmu, var pamanīt, ka vienādības labajā
    pusē ir izteiksme, kas (pietiekami lieliem :math:`n`) dalās ar augstāku skaitļa :math:`7` pakāpi
    nekā skaitļa :math:`5` pakāpi. Tāpēc šīs izteiksmes vērtība nevar būt :math:`k!` nevienam
    pietiekami lielam :math:`k`, jo faktoriālam :math:`\nu_5(n!) \geq \nu_7(n!)` katram :math:`n`.
    Cēloni, kādēļ faktoriāliem 5-validācija aug straujāk, sk. Ležandra formulu -- `<https://bit.ly/30N0EtL>`_.






**LV.IK2022.NT1.03**
  Attēlā dots "Kantora kvadrants", kas režģa punktus
  :math:`(0,0)`, :math:`(1,0)` :math:`(0,1)`, :math:`\ldots` pēc
  kārtas aizpilda ar skaitļiem  :math:`0,1,2,\ldots`.
  Šajā kvadrantā katram veselam nenegatīvam skaitlim ir divas
  "Dekarta koordinātes" (kas arī ir veselas nenegatīvas).
  Piemēram, skaitļa :math:`17` koordinātes ir :math:`(x,y) = (3,2)`.

  .. figure:: figs/pairing_function.png
     :width: 2.7 in
     :alt: Kantora kvadrants.

     Kantora kvadrants.

  Atzīmēsim šajā kvadrantā kvadrāttrinoma
  :math:`{\displaystyle f(z) = \frac{z^2 + z + 356}{2}}` vērtības
  veseliem argumentiem :math:`z`. Zināms, ka visas (izņemot galīgu skaitu) no šīm vērtībām
  atrodas uz horizontālas taisnes: tām :math:`y` koordināte ir viena un tā pati.
  Atrast šo :math:`y` koordināti.


  **Atbilde:** :math:`\mathtt{178}`.

  Aplūkojam Kantora "pāru iekodēšanas" funkciju, kas ikvienu divu veselu nenegatīvu skaitļu pāri 
  :math:`(x,y)` attēlo par vienu veselu nenegatīvu skaitli: 

  .. math::
    
    z = \pi(x, y) = \frac{(x + y + 1)(x + y)}{2} + y 

  Šī funkcija neparasta ar to, ka tā ir bijekcija (katram pārim atbilst unikāls vesels nenegatīvs skaitlis). 
  Tāpēc eksistē arī divas "atpārošanas funkcijas". 
  Sk. `<https://bit.ly/2ZfOvgb>`_. Ievietojot tajā mūsu dotās funkcijas :math:`f(z)` vērtības, 
  redzēsim, ka :math:`y`, sākot ar kādu vietu, vienmēr ir :math:`178`.

  :math:`\square`
  
  .. note::
    Starp funkcijas :math:`f(z)` vērtībām ir neparasti daudz pirmskaitļu 
    (starp pirmajām :math:`1000` vērtībām to ir :math:`292` no 1000). 
    Ar kongruencēm var pamatot, ka :math:`f(z)` nedalās ar vairākiem nelieliem 
    pirmskaitļiem -- tātad, :math:`f(z)` nav garantēti pirmskaitlis (bet ja tas 
    nav pirmskaitlis, tad tam visi pirmreizinātāji ir diezgan lieli). 
    Izrādās arī, ka visas šīs vērtības atrodas uz vienas horizontāles
    Kantora kvadrantā.
	
    Ja Kantora kvadrantā kāds iekrāsotu visus pirmskaitļus, tad uz taisnes :math:`y = 178`
    iekrāsoto pirmskaitļu koncentrācija būtu neparasti augsta, šī taisne izceltos zīmējumā. 
    Kas dod iespēju zīmēt Kvantora kvadrantā "pirmskaitļu musturus" līdzīgi kā Ulama spirālei: 
    `<https://bit.ly/3Bcy5ma>`_.


**LV.IK2022.NT1.04**
  :math:`F_n` apzīmē Fermā skaitli: :math:`{\displaystyle F_n = 2^{2^n} + 1}`, kur :math:`n = 0,1,2,\ldots`.
  Zināms, ka pirmskaitlis :math:`p` ir ar sekojošu īpašību:
  :math:`F_{n+3} - F_{n}` dalās ar :math:`p` visiem naturāliem :math:`n` (iespējams, izņemot galīgu skaitu
  :math:`n` vērtību).

  Atrast kādu šāda pirmskaitļa :math:`p` piemēru.


  **Atbilde:** :math:`\mathtt{2}` (un arī :math:`\mathtt{29}`, :math:`\mathtt{43}`).


  Ir viena triviāla atbilde :math:`p = 2` (jo visas Fermā skaitļu starpības dalās ar :math:`2`).
  (Uzdevuma sastādītājam tā bija neuzmanības kļūda: Ja var ar mazu pirmskaitli panākt, ka
  :math:`F_{n+1} - F_{n}` dalās ar :math:`p`, tad automātiski izpildīsies arī :math:`F_{n+3} - F_{n}` dalās ar :math:`p`.)

  Ja vēlamies, lai atlikumi veidotu ciklu garumā tieši trīs,
  var izvēlēties :math:`p` vērtības :math:`\mathtt{29}` (arī :math:`43, 113, 449` un daži citi piemēri).

  **Apgalvojums:** Katram pirmskaitlim :math:`p`, atlikumi, ko dod :math:`F_n` cikliski atkārtojas
  (iespējams, izņemot galīgu skaitu :math:`n` vērtību).

  **Pierādījums:** Atlikumu ir tikai galīgs skaits, un tos fiksētam pirmskaitlim var iegūt
  ar rekurentu sakarību:

  .. math::

    F_{n+1} \equiv (F_n - 1)^2 + 1  \pmod {p}.

  Piemēram, pirmskaitlim :math:`p = 29`, iegūstam (pēc moduļa 29):

  .. math::

    F_0 = 3 \equiv 3,\;\; F_1 = 5 \equiv 5,\;\; F_2 = 17 \equiv 17,\;\; F_3 = 257 \equiv 25,\;\; F_4 = 65537 \equiv 26,\;\;
	F_5 \equiv (26 - 1)^2 + 1 \equiv 17.

  Ieguvām, ka :math:`F_2 \equiv F_5 \pmod {29}` (un turpmāk rekurentās sakarības dēļ būs arī
  :math:`F_3 \equiv F_6 \pmod {29}`, utt.). Tātad, atmetot pirmās divas vērtības :math:`F_0` un
  :math:`F_1`, rodas atlikumu cikls garumā 3.

  :math:`\square`

  .. note::
    Šis ir tipisks piemērs, kas parāda, ka jebkura rekurenta sakarība ar moduļiem (jeb atlikumiem,
    dalot ar vienu un to pašu skaitli) noved pie cikliskas atkārtošanās, ja vien iepriekšējais modulis
    ļauj viennozīmīgi izrēķināt nākamo.





**LV.IK2022.NT1.05**
  Naturālam skaitlim ar sadalījumu pirmreizinātājos
  :math:`n = p_1^{a_1}p_2^{a_2}\ldots{}p_k^{a_k}` definējam :math:`\omega(n) = k`:
  tas ir visu skaitļa :math:`n` dažādo pirmreizinātāju skaits.
  (Piemēram, :math:`\omega(1) = 0`, :math:`\omega(2) = \omega(3) = \omega(5) = \ldots = 1`,
  :math:`\omega(4) = \omega(8) = 1`, :math:`\omega(6) = \omega(12) = 2`, :math:`\omega(210) =4`, utml.)

  Atrast sekojošas summas vērtību:

  .. math::

     2^{\omega(d_1)} + 2^{\omega(d_2)} + 2^{\omega(d_3)} + \ldots + 2^{\omega(d_k)},

  kur :math:`d_1,\ldots, d_k` ir visi skaitļa :math:`2016` pozitīvie dalītāji.

  **Atbilde:** :math:`\mathtt{165}`

  **Apgalvojums:** Ar :math:`n` apzīmēts naturāls skaitlis. Ir spēkā sakarība:

  .. math::

    \sum\limits_{r \mid n} 2^{\omega(r)} = d(n^2),

  kur ar :math:`d(n^2)` apzīmēts skaitļa :math:`n^2` dažādo pozitīvo dalītāju skaits.

  **Ieteikums:** Sk. `<https://handwiki.org/wiki/Prime_omega_function>`_ -- :math:`\omega(n)` funkcijas īpašības.
  Lai šo vienādību pamatotu, var pielietot indukciju (vispirms pēc :math:`n` pirmreizinātāju skaita, pieņemot, ka
  ikviens pirmreizinātājs ir tikai pirmajā pakāpē). Pēc tam vispārina arī gadījumiem, kad pirmreizinātājs
  ir augstākā pakāpē par pirmo.

  Tā kā :math:`2016^2 = (2^5  \cdot 3^2 \cdot 7)^2 = 2^{10} 3^4 7^2`,
  tam ir :math:`11 \cdot 5 \cdot 3 = 165` pozitīvi dalītāji.

  Ja nevēlamies izmantot šādu mazpazīstamu formulu, varam summēt arī tieši:

  * Skaitlim :math:`2016` ir :math:`10` dalītāji :math:`d`, kuriem :math:`\omega(d) = 3`
    (cik dažādos veidos var kombinēt kāpinātājus dalītājam :math:`d = 2^a  \cdot 3^b \cdot 7^c` tā, lai
    visi kāpinātāji būtu lielāki par nulli).
  * Skaitlim :math:`2016` ir :math:`17` dalītāji :math:`d`, kuriem :math:`\omega(d) = 2`
    (cik dažādos veidos var kombinēt kāpinātājus dalītājam :math:`d = 2^a  \cdot 3^b \cdot 7^c` tā, lai
    tieši divi kāpinātāji būtu lielāki par nulli).
  * Skaitlim :math:`2016` ir :math:`8` dalītāji :math:`d`, kuriem :math:`\omega(d) = 1`
    (cik dažādos veidos var kombinēt kāpinātājus dalītājam :math:`d = 2^a  \cdot 3^b \cdot 7^c` tā, lai
    tieši viens kāpinātājs būtu lielāks par nulli).
  * Skaitlim :math:`2016` ir :math:`1` pozitīvs dalītājs :math:`d`, kuram :math:`\omega(d) = 0`. Tas ir :math:`d = 1`
    (cik dažādos veidos var kombinēt kāpinātājus dalītājam :math:`d = 2^a  \cdot 3^b \cdot 7^c` tā, lai
    visi kāpinātāji būtu nulles).

  Saskaitot šo visu iegūst:

  .. math::

    10 \cdot 2^3 + 17 \cdot 2^2 + 8 \cdot 2^1 + 1 \cdot 2^0 = 165.

  :math:`\square`







**LV.IK2022.NT1.06**
  Atvērtas iekavas izteiksmē :math:`(x + y)^{2020}` un polinomā sagrupēti līdzīgie locekļi:

  .. math::

    (x + y)^{2020} = x^{2020} + 2020 x^{2019}y + \ldots  + 2020 x y^{2019} + y^{2020}.

  Atrast, cik daudzi no šī polinoma koeficientiem dalās ar :math:`2020`.


  **Atbilde:** :math:`\mathtt{1718}`.

  
  
  Vispirms sadalām skaitli :math:`2020` kā pirmreizinātāju reizinājumu: :math:`2020 = 2^2 \cdot 5 \cdot 101`. 
  Tad lietojam Kummera teorēmu -- mums interesē tie binomiālie koeficienti :math:`C_{2020}^k`, kuriem
  saskaitot :math:`k` un :math:`(2020 - k)` visās skaitīšanas sistēmās ar bāzēm 2, 5 un 101 -- rodas kaut kādi 
  pārnesumi (turklāt skaitīšanas sistēmā ar bāzi :math:`2` rodas vismaz divi pārnesumi).
  
  Sk. Kummera teorēmas formulējumu un pierādījumu -- `<https://bit.ly/3vTPS0x>`_.

  :math:`\square`
  
  .. note:: 
  
    Jautājums aizgūts no Ķīnas meiteņu olimpiādes: 
	
    **CGMO2012.8:** Cik starp skaitļiem :math:`\{0,1,2,\ldots,2012\}` ir elementu :math:`k`, 
    kam :math:`C_{2012}^k` ir skaitļa :math:`2012` daudzkārtnis?
    (Ar :math:`C_n^k` apzīmējam kombinācijas no :math:`n` pa :math:`k` 
    jeb :math:`{\displaystyle C_n^k = \frac{n!}{k! \cdot (n-k)!}}`.)





**LV.IK2022.NT1.07**

  .. https://artofproblemsolving.com/community/c6h2342235p18895780

  Cik ir pirmskaitļu :math:`p < 100` ar sekojošu īpašību:
  Jebkuriem veseliem :math:`x,y`
  no dalāmības :math:`p \mid x^2 + y^2` izriet :math:`p \mid xy`?
  (T.i. :math:`x^2 + y^2` var dalīties ar :math:`p` vienīgi tad, ja :math:`xy` dalās ar :math:`p`.)

  **Atbilde:** :math:`\mathtt{13}`.

  Tie ir visi pirmskaitļi formā :math:`4n+3`:

  .. math::

    3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83.

  **Apgalvojums:** Visiem pirmskaitļiem formā :math:`p = 4n+3` ir spēkā apgalvojums:
  ja vienādojumu :math:`z^2 \equiv a \pmod{p}` var
  atrisināt veselam :math:`z`, tad vienādojumu :math:`z^2 \equiv -a \pmod{p}` nevar atrisināt
  (vienīgais izņēmums ir tad, ja :math:`a = 0`). 
  
  **Ieteikums:** Pierādījumu sk. `<https://bit.ly/3Bag0VU>`_.
  Tas izriet no fakta, ka divu kvadrātisko atlikumu reizinājums un dalījums arī ir kvadrātiskais atlikums. 
  Bet pirmskaitļiem :math:`p = 4n+3` atlikums :math:`-1` nevar būt kvadrātiskais atlikums: 
  vienādojumu :math:`z^2 \equiv -1 \pmod {p}` nevar atrisināt veselos skaitļos.
  
  
  Tātad, ja 
  :math:`p \mid x^2 + y^2` un tādēļ :math:`x^2 + y^2 \equiv 0 \pmod {p}`. 
  Pieņemot, ka :math:`x` nedalās ar :math:`p`, apzīmējam :math:`a = x^2`. 
  Iegūstam, ka var atrisināt gan vienādojumu :math:`z^2 \equiv a \pmod {p}` (sakne ir :math:`z=x`), 
  gan arī vienādojumu :math:`z^2 \equiv -a \pmod {p}` (sakne ir :math:`z=y`). Pretruna ar apgalvojumu.
  
  No otras puses, ja :math:`p=2`, tad var izvēlēties :math:`x,y` -- jebkurus divus nepāra skaitļus. 
  Un ja :math:`p=4n+1` ir pirmskaitlis, kas dod atlikumu :math:`1`, dalot ar :math:`4`, 
  tad var izvēlēties :math:`x = 1`, bet :math:`y = m^{n}`, kur :math:`m` ir jebkura primitīvā sakne 
  pēc :math:`p` moduļa. (Piemēram, ja :math:`p = 5 = 4 \cdot 1 + 1`, var izvēlēties :math:`m = 2` un 
  :math:`y = 2^1`. 
  Tad :math:`(x,y) = (1,2)`, un :math:`1^2 + 2^2` dalās ar :math:`5`, kaut arī neviens no skaitļiem 
  :math:`1` vai :math:`2` nedalās ar :math:`5`. 
  
  

  :math:`\square`
  
  .. note:: 
    Dažus augšminētā apgalvojuma lietojumus sk. arī 
    `<https://bit.ly/3Gb1Ozs>`_.
    Vēl dažas līdzīgas kvadrātisko atlikumu ilustrācijas: 
    `<https://bit.ly/3E3ntI6>`_.


**LV.IK2022.NT1.08**
  Dots naturāls skaitlis :math:`n`. Apzīmēsim ar :math:`\nu_2(n)` lielāko divnieka pakāpi, ar kuru tas dalās.
  (Piemēram, :math:`\nu_2(1) = \nu_2(3) = \nu_2(5) = \ldots = 0`, :math:`\nu_2(2) = \nu_2(6) = \nu_2(10) = \ldots = 1`,
  :math:`\nu_2(4) = \nu_2(12) = 2`.)

  Atrast mazāko naturālo :math:`n`, kam :math:`n - \nu_2(n!)` un :math:`(n+1) - \nu_2((n+1)!)` ir dažādi veseli
  skaitļi, kas abi dalās ar :math:`3`.


  **Atbilde:** :math:`\mathtt{111}`.


  **Apgalvojums:** 2-valuācija faktoriālam :math:`\nu_2(n!)` vienāda ar skaitļa :math:`n` un tā binārā pieraksta
  ciparu summas starpību. (Piemēram :math:`\nu_2(10!) = 8`, jo :math:`10! = 3628800` dalās ar :math:`2^8 = 256`, bet
  vairs nedalās ar :math:`2^9 = 512`. No otras puses, starpība starp :math:`10` un tā binārā pieraksta (:math:`\mathtt{1010}_2`)
  ciparu summu arī ir :math:`10-2 = 8`.

  **Pierādījums.** Šo apgalvojumu var pierādīt ar matemātisko indukciju. :math:`\blacksquare`

  Mums jāatrod mazākie pēc kārtas sekojošie skaitļi, kuru ciparu summa binārajā pierakstā dalās ar 3.

  * Skaitļa :math:`111` binārais pieraksts ir :math:`\mathtt{1101111}_2`
  * Skaitļa :math:`112` binārais pieraksts ir :math:`\mathtt{1110000}_2`.

  Vēl mazāki skaitļi ar šo īpašību neeksistē, jo pieskaitot vieninieku četriem vieniniekiem jāpārvēršas par nullēm
  (t.i :math:`n+1` noteikti dalās ar 16). Turklāt arī skaitlim :math:`n+1` jābūt ar ciparu summu, kas ir 3 (vai 6, vai 9, utml.)
  Mazākais šāds skaitlis ir pierakstāms kā trīs vieninieki, kuriem seko četras nulles. T.i. :math:`\mathtt{1110000}_2`,
  kas decimālajā pierakstā ir :math:`112`.

  :math:`\square`





**LV.IK2022.NT1.09**
  Dots vienādojums veselos skaitļos:

  .. math::

    x^4 - 12 y^4 = 24.

  Atrast naturālu skaitli :math:`m`, kas ir *pretrunas modulis*
  šim vienādojumam: Jebkuram veselu skaitļu pārim :math:`(x,y)`
  izteiksmes :math:`x^4 - 12 y^4` un :math:`24` dod atšķirīgus atlikumus, dalot ar :math:`m`
  (tātad tās nevar būt vienādas).
  Ja tādi :math:`m` ir vairāki, centieties atrast mazāko iespējamo.


  **Atbilde:** :math:`\mathtt{13}`.


    Izvēloties :math:`p = 13` varam iegūt pretrunu, jo vesela skaitļa
    ceturtā pakāpe :math:`x^4` var būt kongruenta ar skaitļiem 0,1,3,9 (pēc 13 moduļa).
    No otras puses, :math:`-12` ir kongruents ar ``1``, bet ``24`` ir kongruents ar ``11``.
    Aplūkojot visas iespējamās summas :math:`x^4 - 12 y^4 \equiv x^4 + y^4``,
    kur abas ceturtās pakāpes pieņem kādu no vērtībām 0,1,3, vai 9, nekad neiegūsim
    vērtību :math:`11`.

  :math:`\square`

  .. note::
    Vienādojums :math:`x^4 - 12 y^4 = 24` (atrisināt veselos skaitļos) aizgūts no
    A.Bērziņa, A.Bērziņas, D.Bonkas grāmatas "Skaitļu teorija" (4.nodaļa, 4.1.5. uzdevums).


**LV.IK2022.NT1.10**
  Ciparu virkni :math:`D = d_{n-1}d_{n-2}\ldots{}d_0` sauksim par *stabilu skaitļa
  nobeigumu*, ja jebkuram naturālam skaitlim :math:`m`, kas beidzas ar virkni :math:`D`,
  arī jebkura tā pakāpe :math:`m^k` beidzas ar šo pašu virkni :math:`D`.
  Atrast to stabilo skaitļa nobeigumu :math:`D`, kas sastāv no astoņiem cipariem
  un ir lielākais iespējamais (kā astoņciparu skaitlis).


  **Atbilde:** :math:`\mathtt{87109376}`.

  Ir arī trīs citas atbildes: :math:`\mathtt{00000000}`, :math:`\mathtt{00000001}` un
  :math:`\mathtt{12890625}`, bet tie ir mazāki skaitļi.

  **Apgalvojums:** Lai virkne :math:`D = d_{n-1}d_{n-2}\ldots{}d_0` būtu stabils skaitļa
  nobeigums no :math:`n` cipariem ir nepieciešami un pietiekami, lai skaitlim :math:`D` izpildītos kongruence:

  .. math::

    D^2 \equiv D \pmod {10^n}

  **Pierādījums:** Nepieciešamība izriet no tā, ka otrajai pakāpei :math:`D^2` jābeidzas
  ar tiem pašiem :math:`n` cipariem ar ko skaitlim :math:`D`.
  Pietiekamība izriet no tā, ka jebkuru augstāku pakāpi :math:`D^2` var izteikt kā atkārtotu :math:`D`
  reizinājumu pašam ar sevi. Ja pēc vienas piereizināšanas pēdējo ciparu virkne nemainās,
  tad (pēc indukcijas) arī vēlāk šī pēdējo :math:`n` ciparu virkne nemainīsies.
  Piemēram, ja :math:`D = 376^1 = 376`, tad :math:`376^2 = 141376`, :math:`376^3 = 53157376`, utt. --
  visas šīs virknes beidzas ar trim cipariem :math:`376`. :math:`\blacksquare`

  Stabilas ciparu virknes var konstruēt induktīvi, sākot ar skaitļa beigām.
  Ir, teiksim, četras stabilas virknes 1 cipara garumā: ``0,1,5,6`` --
  kāpinot kvadrātā skaitli, kas beidzas ar kādu no šiem cipariem, arī rezultāts beigsies ar to pašu ciparu.
  (Un arī visas tālākās pakāpes beigsies ar to pašu ciparu

  No diviem cipariem tieši tāpat var izveidot četras stabilas virknes: ``00, 01, 25, 76``.
  No trim cipariem attiecīgi virknes ``000, 001, 376, 625``.

  **Kāpēc virkņu dotajā garumā nevar būt vairāk kā četras?**
  Pamatosim šo ar indukciju. Pieņemsim, ka :math:`n` ir lielākais naturālais skaitlis,
  kuram stabilo virkņu garumā :math:`n` ir tieši četras.
  Jebkura stabila virkne garumā :math:`n+1` būs tāda, ka tās pēdējie :math:`n` cipari arī veido
  stabilu virkni. Pamatosim, ka :math:`n`-ciparu virknes (ko apzīmēsim ar skaitli :math:`x`)
  kreisajā pusē jaunu ciparu var "pieaudzēt"
  ne vairāk kā vienā veidā tā, lai virkne joprojām būtu stabila.

  Tā kā virkne :math:`x` ir stabila (kā :math:`n` ciparu virkne), tad
  starpības :math:`x^2 - x` decimālpieraksts beidzas vismaz ar :math:`n` nullēm.
  Apzīmējam dalījumu :math:`(x^2 - x)/(10^n)` ar :math:`M`.
  Apskatīsim kādu ciparu :math:`d` var pierakstīt virknes :math:`x` priekšā tā,
  lai iegūtā virkne būtu stabila jau kā :math:`n+1` ciparu virkne.

  Pēc apgalvojuma :math:`(10^n d + x)^2 \equiv 10^n d + x \pmod {10^{n+1}}`, jo
  pēc :math:`d` pierakstīšanas virkne :math:`\overline{dx}` ir stabila.

  .. math::

    \begin{array}{l}
    (10^n d + x)^2 \equiv 10^n d + x \pmod {10^{n+1}}\\
    10^{2n}d^2 + 2 \cdot 10^n \cdot x \cdot d + x^2 \equiv 10^n d + x \pmod {10^{n+1}}\\
    2 \cdot 10^n \cdot x \cdot d + x^2 \equiv 10^n d + x \pmod {10^{n+1}}\\
    (2x - 1) \cdot 10^n \cdot d + \left( x^2 - x \right) \equiv 0 \pmod {10^{n+1}}\\
	(2x - 1) \cdot 10^n \cdot d + M \cdot 10^n \equiv 0 \pmod {10^{n+1}}\\
	(2x - 1) \cdot d + M \equiv 0 \pmod {10}\\
    \end{array}

  Pēdējā kongruence ir spēkā, jo var abās vienādībās (un arī modulī) noīsināt ar
  :math:`10^n`. :math:`\blacksquare`

  Piemēram, ja :math:`x = 76` ir stabila virkne un :math:`n=2` ir tās garums, tad
  nākamo ciparu, ko pierakstīt pa kreisi no ``76``, iegūstam sekojoši:
  Atrodam :math:`M = (x^2 - x)/10^2 = (5776 - 76)/100 = 57`.
  Risinām sakarību:

  .. math::

    \begin{array}{l}
    (2x - 1) \cdot d + 57 \equiv 0 \pmod {10}\\
	151 \cdot d + 57 \equiv 0 \pmod {10}\\
	d \equiv 3 \pmod {10}\\
	\end{array}

  Iegūstam, ka nākamais cipars :math:`d = 3` un nākamā stabilā virkne ir :math:`376`.
  Eksistē viens un tieši viens veids kā tai pierakstīt priekšā jaunu ciparu.

  Lai atrastu, kura ir lielākā stabilā virkne no 8 cipariem,
  audzējam ciparus klāt stabilajām virknēm ``76`` un arī ``25``. Un beigās izvēlamies lielāko
  no abiem astoņciparu skaitļiem.

  :math:`\square`

  .. note::
    Šis jautājums aizgūts no Baltic Way atlases sacensību uzdevuma:
	
    **BW.TST.2017.15** Ciparu virkni :math:`D = d_{n-1}d_{n-2}\ldots{}d_0`  sauksim par stabilu skaitļa
    nobeigumu, ja jebkuram naturālam skaitlim :math:`m`, kas beidzas ar :math:`D`, 
    arī jebkura tā naturāla pakāpe :math:`m^k`
    beidzas ar :math:`D`. Pierādīt, ka katram naturālam :math:`n` ir tieši četri 
    stabili skaitļa nobeigumi, kuru garums ir :math:`n`.




**LV.IK2022.NT1.11**

  Ar :math:`S(a)` apzīmēsim skaitļa :math:`a` ciparu summu.
  Atrast iespējami mazu naturālu :math:`n`, kuram

  .. math::

    \frac{S(n^2)}{S(n)} = 10.


  **Atbilde:** :math:`\mathtt{10111111111}`.

  **Skaitļa atrašana.**
  Skaitli var kāpināt kvadrātā, izmantojot skolas algoritmu (reizināšanu stabiņā).
  Ja vajag iegūt attiecības :math:`\frac{S(n^2)}{S(n)} = d` (kur :math:`d = 1,\ldots,9`),
  var izvēlēties :math:`n=1`, :math:`n=11`, :math:`n=111`, utt. līdz pat :math:`n=111\,111\,111`.

  Savukārt, ja :math:`\frac{S(n^2)}{S(n)} = 10`, tad
  skaitlis :math:`n = 1111111111` vairs neapmierina nosacījumu: to kāpinot kvadrātā rodas
  divi pārnesumi (katrā no pārnesumiem ciparu summa vienā skaitļu šķirā samazinās par :math:`10`, lai
  nākamajā skaitļu šķirā palielinātos par :math:`1` -- t.i. kopīgā ciparu summa samazinās par :math:`9`).

  .. code-block:: text

             1111111111
           * 1111111111
           ------------
             1111111111
            1111111111
           1111111111
          1111111111
         1111111111
        1111111111
       1111111111
      1111111111
     1111111111
    1111111111
    -------------------
    1234567900987654321


  Tā kā notiek divi pārnesumi, iegūtā skaitļa ciparu summa ir :math:`S(n^2) = 100 - 2 \cdot 9 = 82`,
  kas ir mazāk nekā :math:`10\cdot S(n) = 100`.

  Aplūkojam mazāko :math:`11`-ciparu skaitli, kuram ir :math:`10` nenulles cipari: :math:`n = 10111111111`.
  Kāpinot to kvadrātā, izrādās, ka pārnesumu nav vispār:
  :math:`n^2 = 102234567898987654321`. Ciparu summa :math:`S(n^2) = 100`, kas tiešām ir desmit reizes lielāka par :math:`S(n)`.

  **Optimalitātes pamatojums.** TBD


  :math:`\square`

  .. note::
    Šis jautājums iedvesmojies no Baltic Way atlases sacensību uzdevuma:

    **BW.TST.2015.14.**
    Ar :math:`S(a)` apzīmēsim skaitļa :math:`a` ciparu summu. Kādām naturālām :math:`R` vērtībām var
    atrast tādu naturālu :math:`n`, ka

    .. math::

       \frac{S(n^2)}{S(n)} = R?



**LV.IK2022.NT1.12**
  Matemātiķis :math:`A` iečukstēja ausī matemātiķiem :math:`B,C,D` un :math:`E` četrus pēc kārtas sekojošus divciparu skaitļus :math:`n,n+1,n+2,n+3`.
  (Pašiem :math:`B,C,D,E` nav zināms, kuram iečukstēts lielākais, mazākais utml.)
  Matemātiķis turklāt pateica viņiem visiem, ka visi skaitļi ir pēc kārtas sekojoši, ka
  viens no kopas :math:`S = \{ n,n+1,n+2,n+3 \}`
  skaitļiem dalās ar :math:`6`, bet kāds cits skaitlis dalās ar :math:`7`.
  Matemātiķis :math:`A` tad jautāja četriem pārējiem, vai iespējams izsecināt :math:`n` vērtību, visi reizē atbildēja "Nē".
  Bet tūlīt pēc tam katrs no viņiem jau zināja :math:`n` vērtību.

  Atrast lielāko iespējamo divciparu skaitli :math:`n`, kuram izpildās aprakstītā īpašība.

  **Atbilde:** :math:`\mathtt{89}`.

  Pamatosim, ka šie divciparu skaitļi ir :math:`\{ 89,90,91,92 \}` (tātad mazākais no viņiem ir :math:`n=89`).

  Ir nepieciešams, lai
  abi vidējie skaitļi būtu tādi, ka viens no tiem dalās ar :math:`6`, bet otrs ar :math:`7`
  (nav svarīgi, kurā secībā). Ja ar :math:`6` vai ar :math:`7` dalās kāds no malējiem skaitļiem (piemēram, :math:`n`
  vai :math:`n+3`), tad tas matemātiķis, kuram iečukstēja skaitli intervāla otrajā galā (attiecīgi :math:`n+3` vai :math:`n`),
  pārbaudot dalāmību ar :math:`6` un ar :math:`7` varēs viennozīmīgi atjaunot visu intervālu
  :math:`S = \{ n,n+1,n+2,n+3 \}`.

  Izrakstām visus tos blakusesošos pārus :math:`(n+1,n+2)`, kur viens no skaitļiem dalās ar :math:`6`, bet otrs ar :math:`7`:

  .. code-block:: text

    35,36
    48,49
    77,78
    90,91

  Lielākais no šiem pāriem ir :math:`(n+1,n+2) = (90,91)`. Tātad lielākais iespējamais
  :math:`n` ir :math:`n=89` un četri iečukstētie skaitļi ir :math:`\{ 89,90,91,92 \}`.


  :math:`\square`

  .. note::
    Sk. arī `<https://bit.ly/3jqQRjq>`_ -- AIME2021_2P11, citu šī uzdevuma variantu.



