Skaitļu pieraksts
=====================

**Dalāmības pazīmes:** 
  Dalāmības pazīmes ļauj no skaitļa pieraksta ātri noskaidrot, vai tas
  dalās ar citu skaitli, neveicot pašu dalīšanu.

.. list-table:: 
   :header-rows: 1
   :align: center

   * - Dalāmības pazīme
     - Piemēri
   * - Skaitlis dalās ar :math:`2`, ja tā pēdējais cipars ir pāra 
       (:math:`0`, :math:`2`, :math:`4`, :math:`6` vai :math:`8`).
     - :math:`2024` dalās ar :math:`2`, jo :math:`4` ir pāra.
   * - Skaitlis dalās ar :math:`3`, ja tā ciparu summa dalās ar :math:`3`.
     - :math:`2025` dalās ar :math:`3`, jo :math:`2+0+2+5=9` dalās ar :math:`3`.
   * - Skaitlis dalās ar :math:`4`, ja tā pēdējo divu ciparu veidotais skaitlis dalās ar :math:`4`.
     - :math:`2024` dalās ar :math:`4`, jo :math:`24` dalās ar :math:`4`.
   * - Skaitlis dalās ar :math:`4`, ja tā pēdējo divu ciparu veidotais skaitlis dalās ar :math:`4`.
     - :math:`2024` dalās ar :math:`4`, jo :math:`24` dalās ar :math:`4`.
   * - Skaitlis dalās ar :math:`5`, ja tā pēdējais cipars dalās ar :math:`5` (ir :math:`0` vai :math:`5`).
     - :math:`2025` dalās ar :math:`5`, jo tā pēdējais cipars ir :math:`5`.
   * - Skaitlis dalās ar :math:`6`, ja tas dalās gan ar :math:`2`, gan ar :math:`3`.
     - :math:`2022` dalās ar :math:`6`, jo tas dalās ar :math:`2` (beidzas ar pāra ciparu) 
       un ar :math:`3` (ciparu summa dalās ar :math:`3`).
   * - Skaitlis dalās ar :math:`8`, ja tā pēdējo trīs ciparu veidotais skaitlis dalās ar :math:`8`.
     - :math:`1124` nedalās ar :math:`8`, jo :math:`124` nedalās ar :math:`8`. 
       Bet :math:`1024` dalās ar :math:`8`, jo :math:`24` dalās ar :math:`8`. 
   * - Skaitlis dalās ar :math:`9`, ja tā ciparu summa dalās ar :math:`9`.
     - :math:`2025` dalās ar :math:`9`, jo :math:`2+0+2+5=9` dalās ar :math:`9`.
   * - Skaitlis dalās ar :math:`10`, ja tā pēdējais cipars ir :math:`0`.
     - :math:`150` dalās ar :math:`10`, jo tā pēdējais cipars ir :math:`0`.
   * - Skaitlis dalās ar :math:`11`, ja tā ciparu summa nepāra pozīcijās mīnus 
       ciparu summa pāra pozīcijās dalās ar :math:`11`. 
     - :math:`108647` dalās ar :math:`11`, jo :math:`(1+8+4)-(0+6+7)=0`, kas dalās ar :math:`11`.
       :math:`94831` dalās ar :math:`11`, jo :math:`(9+8+1)-(4+3)=11`, kas dalās ar :math:`11`.

Dalāmības pazīmēm parasti ir divi varianti -- par pašu dalāmību (dalās vai nedalās) vai arī 
par dalīšanas atlikumu. 

Apgalvojums 1:
  Naturāls skaitlis :math:`n` dalās ar :math:`9` tad un tikai tad, ja skaitļa :math:`n` 
  ciparu summa dalās ar :math:`9`. 

Apgalvojums 2: 
  Naturāls skaitlis :math:`n` un tā ciparu summa :math:`S(n)` dod vienādus atlikumus, dalot ar :math:`9`. 

*Piemērs:* Otrajam apgalvojumam nevajag, lai skaitlis :math:`n` dalītos ar 
:math:`9`; tas ir spēkā visiem skaitļiem. 
Piemēram, :math:`n = 2024` ir ar ciparu summu :math:`S(n) = 2 + 0 + 2 + 4 = 8`. 
Gan :math:`2024 = 224 \cdot 9 + 8` gan :math:`8` dod atlikumu :math:`8`, dalot ar :math:`9`. 



**Piemēri**



Dalāmība ar 144:
  Skaitli :math:`6` var izteikt kā :math:`6 = 2 \cdot 3`. Ir spēkā apgalvojums: 
  Ja skaitlis dalās ar :math:`2` un ar :math:`3`, tad tas dalās arī ar :math:`6`. 

  Izteikt arī skaitli :math:`144` kā reizinājumu :math:`144 = a \cdot b` tā, lai 
  jebkurš skaitlis :math:`N`, kas dalās gan ar :math:`a`, gan ar :math:`b` 
  dalītos arī ar :math:`144`.

Dalāmība ar 99:
  Pierādiet apgalvojumu: ja skaitlis dalās ar :math:`99`, tad 
  tā ciparu summa ir ne mazāka kā :math:`18`. 


Divreiz atkārtots 3-ciparu skaitlis:
  Vienu otram galā uzrakstīja divus vienādus trīsciparu skaitļus,
  iegūstot 6-ciparu skaitli. Pierādīt, ka iegūtais skaitlis 
  **(A)** dalās ar :math:`11`, **(B)** dalās ar :math:`7` un 
  arī ar :math:`13`. 


.. 109595

Dalīšana uz pusēm:
  Klasē ir :math:`16` skolēni. Angļu valodas apgūšanai viņus 
  dala divās grupās. Katru mēnesi grupas sadala citādi. 
  Cik mēneši nepieciešami, lai katri divi skolēni vismaz vienā
  no mēnešiem nonāktu dažādās grupās?

..  30278

Visu summu salikšana:
  Kā salikt septiņās aizsietās zeķēs :math:`127` eiro monētas tā, lai jebkuru veselu skaitu eiro 
  no :math:`1` līdz :math:`127` varētu nomaksāt, neatraisot zeķes? 

.. 117004

Visu taisnstūru salikšana:
  Kā sagriezt kvadrātu :math:`7 \times 7` deviņos taisnstūros (ne obligāti dažādos) tā, 
  lai no tiem varētu salikt jebkuru taisnstūri, kura malu garumi ir veseli skaitļi, 
  kas nepārsniedz :math:`7`? 


Vienādojums veselos skaitļos:
  Karlsons sev pusdienām nopirka :math:`8` pīrādziņus un :math:`15` magoņmaizītes, 
  bet Brālītis - vienu pīrādziņu un vienu magoņmaizīti. 
  Karlsons par savām pusdienām samaksāja tieši divus eiro 
  (katra maizīte un pīrādziņš maksā veselu skaitu centu). Cik samaksāja Brālītis?



**Uzdevumi**



.. 41. lpp.

**1.uzdevums:** 
  Dots naturāls skaitlis, kas dalās ar :math:`99` un kura pēdējais cipars nav :math:`0`. 
  Pierādi, ka, uzrakstot šī skaitļa ciparus pretējā secībā,
  arī iegūst skaitli, kas dalās ar :math:`99`.


.. 43.lpp. 

**2.uzdevums:** 
  Leonards izvēlējās patvaļīgu trīsciparu skaitli, reizināja to ar :math:`2` un 
  rezultātam galā pierakstīja sākotnējo skaitli. 
  Vai viņa iegūtais skaitlis noteikti dalās ar :math:`23`?



.. LV.AMO.2022A.8.5; 

**3.uzdevums:** 
  Mārtiņš augošā secībā pēc kārtas sāka rakstīt skaitļus, kuru pirmie četri cipari ir "3321":

  .. math:: 

    3321; 33210; 33211; 33212; 33213; 33214; \ldots 

  Kāds ir 3321. skaitlis šajā virknē?

.. LV.AMO.2022B.7.1; 

**4.uzdevums:** 
  Uz tāfeles bija uzrakstīts šāds teksts: :math:`A869B`. 
  Katrs no burtiem :math:`A` un :math:`B` jāaizstāj ar vienu ciparu (tie var būt arī
  vienādi) tā, lai iegūtais piecciparu skaitlis dalītos ar :math:`15`. 
  Cik dažādos veidos to var izdarīt?

.. LV.AMO.2022B.8.1;

**5.uzdevums:** 
  Uz tāfeles bija uzrakstīts šāds teksts: :math:`N597M`. Katrs no burtiem 
  :math:`N` un :math:`M` jāaizstāj ar vienu ciparu (tie var būt arī
  vienādi) tā, lai iegūtais piecciparu skaitlis dalītos ar :math:`12`. 
  Cik dažādos veidos to var izdarīt?


.. LV.AMO.2023.7.2; 

**6.uzdevums:** 
  Kāds ir lielākais iespējamais septiņciparu skaitlis, kuram vienlaicīgi 
  izpildās šādi nosacījumi:

  * tas dalās ar :math:`12`;
  * skaitļa pirmais cipars ir tāds pats kā pēdējais cipars;
  * skaitļa 2., 4. un 6. cipars ir vienādi un tie ir divas reizes lielāki nekā pirmais cipars;
  * skaitļa trešais cipars ir tāds pats kā piektais cipars?

.. LV.AMO.2023.8.2

**7.uzdevums:** 
  Trīsciparu skaitļa :math:`x` ciparu summa ir :math:`12`. 
  Ja šim skaitlim nodzēš pēdējo ciparu, tad atlikušais divciparu skaitlis
  dalās ar :math:`9`. Zināms, ka skaitlis :math:`x` ir par :math:`99` lielāks 
  nekā trīsciparu skaitlis, ko iegūst, uzrakstot tā ciparus pretējā
  secībā. Kāds var būt skaitlis :math:`x`?

