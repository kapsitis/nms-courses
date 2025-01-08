Virknes un atlikumi
======================

**Definīcija:** 
  Par *aritmētisku progresiju* sauc galīgu vai bezgalīgu virkni 
  :math:`a_1, a_2, a_3, \ldots`, kam katra divu blakusesošu locekļu 
  starpība :math:`a_2 - a_1 = a_3 - a_2 =  \ldots = a_{k+1} - a_k` 
  vienāda ar to pašu skaitli :math:`d`, ko sauc par *diferenci*. 

Progresiju piemēri: :math:`4,11,18,25` (datumi, kas 2024.g. decembrī ir 
trešdienās); :math:`10, 20, 30, \ldots` (visi skaitļi, kas dalās ar 10), 
:math:`1,3,5,7,\ldots` (visi nepāra skaitļi). 

**Definīcija:** 
  Par *ģeometrisku progresiju* sauc galīgu vai bezgalīgu virkni 
  :math:`b_1, b_2, b_3, \ldots`, kam katru divu blakusesošu locekļu 
  dalījums :math:`b_2/b_1 = b_3/b_2 =  \ldots = q` 
  vienāds  ar to pašu skaitli :math:`q`, ko sauc par *kvocientu*. 

**Definīcija:** 
  Par *Fibonači virkni* sauc virkni, ko definē šādi: :math:`F_0 = 0`, 
  :math:`F_1 = 1`, :math:`F_{k+2} = F_{k+1} + F_k` (katram :math:`k \geq 0`) -- 
  t.i. katru nākamo locekli iegūst, saskaitot divus iepriekšējos. 

  ===========  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====
  :math:`k`    0     1     2     3     4     5     6     7     8     9     10
  ===========  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====
  :math:`F_k`  0     1     1     2     3     5     8     13    21    34    55
  ===========  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====
  
**Definīcija:** 
  Par *periodisku virkni* sauc tādu virkni :math:`a_1, a_2, a_3, \ldots`, 
  kuras locekļi atkārto vienus un tos pašus skaitļus: eksistē tāds skaitlis :math:`T`, 
  kam :math:`a_{k+T} = a_k` jebkuram :math:`k`.
  Ja virknes periods parādās tikai pēc kāda laika, tad locekļus, kuri bija 
  pirms šī perioda, sauc par *priekšperiodu*. 


**Piemērs:** 
  Skaitlim :math:`1/13 = 0.076923076923076923\ldots`  cipari aiz komata 
  veido virkni :math:`0,7,6,9,2,3,\ldots`, kas ir periodiska ar periodu 6; 
  tā ir *tīri periodiska* bez priekšperioda.

  Skaitlim :math:`1/12 = 0.08333333333333333\ldots` cipari aiz komata 
  veido virkni :math:`0,8,3,3,3,\ldots`, kas ir periodiska ar periodu 1; 
  pirmie divi tās cipari "0" un "8" ir priekšperiods.

**Definīcija:** 
  Virkni :math:`a_1, a_2, a_3, \ldots` sauc par *ierobežotu*, ja 
  eksistē tāds intervāls :math:`[M;N]`, ka ikviens virknes loceklis 
  atrodas šajā intervālā. 
  (Piemēram jebkāda ciparu virkne ir ierobežota, jo cipari ir 
  intervālā :math:`[0;9]`.)



**Uzdevumi:** 

**10.1. Uzdevums:** 
  Par trijstūra skaitli :math:`T_k` sauc aplīšu skaitu, 
  ko var salikt trijstūrītī, ja uz katras no trijstūra 
  malām ir :math:`k` aplīši. 

  .. figure:: figs/triangle_numbers.png
     :width: 2in



**10.2. Uzdevums:** 
  Aplūkojam virkni :math:`a_k`, kuras loceklis :math:`a_k`
  vienāds ar Fibonači skaitļa :math:`F_k` atlikumu, dalot ar :math:`2`. 
  Aplūkojam arī virkni :math:`b_k`, kuras loceklis :math:`b_k`
  vienāds ar Fibonači skaitļa :math:`F_k` atlikumu, dalot ar :math:`5`. 

  **(A)**
    Vai virknes :math:`a_k` un :math:`b_k` ir periodiskas? 
    Ja jā, tad cik lieli ir to periodi? 
  
  **(B)**
    Ik pēc cik skaitļiem Fibonači 
    virknes locekļi :math:`F_k` beigsies ar ciparu :math:`0`?

**10.3. Uzdevums:** 
  Skaitlim :math:`1/7 = 0.142857(142857)\ldots` cipari aiz
  komata veido periodu garumā seši cipari.

  **(A)**
    Atrast periodus ciparu virknēm šādu skaitļu pierakstos: 
    :math:`1/11`, :math:`1/37`, :math:`1/41`, :math:`1/101`. 
    
  **(B)**
    Vai eksistē skaitlis :math:`1/n`, kura cipari aiz komata 
    veido periodu tieši no septiņiem cipariem?

.. 1111111 = 239 * 4649

**LV.NOL.2009.8.3**
  Atrodiet skaitļa :math:`113^{113} - 19^{19}` pēdējo ciparu.


**LV.NOL.2010.7.3**
  Cik ir tādu naturālu skaitļu :math:`x` 
  robežās no :math:`1` līdz :math:`2010` ieskaitot, ka 
  :math:`(x+1)(x+2)(x+3)` dalās ar :math:`343`? 




**LV.NOL.2005.7.1**
  Kādu mazāko daudzumu no skaitļiem :math:`1,2,3,\ldots,12,13`
  var izsvītrot, lai katru divu atlikušo summa būtu salikts skaitlis?




**LV.NOL.2004.8.2**
  Ir zināms, ka skaitļa :math:`2^{200}` decimālajā pierakstā ir 
  :math:`61` cipars. Cik daudziem no skaitļiem :math:`2^1, 2^2, 2^3,\ldots, 2^{199}, 2^{200}`
  decimālais pieraksts sākas ar ciparu :math:`1`? 

**LV.NOL.2006.8.3**
  Vai var izrakstīt rindā visus naturālos skaitļus no 
  :math:`1` līdz :math:`2006` ieskaitot katru vienu reizi tā, lai katru 
  :math:`3` pēc kārtas uzrakstīto skaitļu summa dalītos ar :math:`4`?


**LV.NOL.2008.6.4**
  Vai eksistē tāds naturāls skaitlis :math:`n`, ka reizinājums 
  :math:`n \cdot n` sākas ar :math:`1234567\ldots`?

**LV.NOL.2009.7.2**
  Rindā no sākuma bija uzrakstīti :math:`2009`
  vieninieki. Ar vienu gājienu nodzēš divus pirmos rindā esošos 
  skaitļus un tās otrā galā pieraksta abu nodzēsto skaitļu summu. 
  Šādus gājienus atkārto, līdz rindā paliek tikai viens skaitlis.

  **(A)** cik gājienu tiks izdarīti?
  **(B)** atrast vienīgo palikušo skaitli.


