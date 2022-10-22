1. Skaitļu teorijas lapa, 2022-10-22
========================================

Iesildīšanās
--------------


**1.piemērs:**
  Atrast vismaz :math:`13` pēc kārtas sekojošus saliktus skaitļus.
  Vai var atrast :math:`N` pēc kārtas sekojošus saliktus skaitļus jebkuram naturālam :math:`N`?


**Dirihlē Teorēma (Dirichlet):**
  Ja :math:`a` un :math:`d` ir savstarpēji pirmskaitļi,
  tad bezgalīgā aritmētiskā progresijā
  :math:`a, a+d, a+2d, a+3d, \ldots` ir bezgalīgi daudz pirmskaitļu.

**2.piemērs:**
  Pamatot, ka ir bezgalīgi daudzi pirmskaitļi formā :math:`4n+3` (un arī formā :math:`6n+5`).


**3.piemērs:**
  Kādā no Eratostena režģa veidošanas
  soļiem tiek izsvītroti visi tie saliktie skaitļi, kuri
  ir pirmskaitļa :math:`13`
  daudzkārtņi. Kurš no šajā solī
  izsvītrotajiem skaitļiem ir pirmais?

**4.piemērs:**
  (A) Pamatot pakāpju starpības formulu visiem :math:`n \geq 2`. Formula ir sekojoša:

    .. math::

      \textcolor{red}{a^n - b^n} =
      \textcolor{red}{(a-b)}\left( a^{n-1}+a^{n-2}b^1 + \ldots +
      a^1b^{n-2} + b^{n-1} \right).


  (B) Pamatot pakāpju summas formulu visiem :math:`n \geq 1`:

    .. math::

      \textcolor{red}{a^{2n+1} + b^{2n+1}} =
      \textcolor{red}{(a+b)}\left( a^{2n} - a^{2n-1}b^1 +
      a^{2n-2}b^2 - \cdots - a^1b^{2n-1} + b^{2n} \right).

**5.piemērs:**
  Pamatot, ka jebkuriem diviem naturāliem :math:`m,n` ir spēkā vienādība:
  :math:`m \cdot n = \gcd(m,n) \cdot \operatorname{lcm}(m,n)`.

**6.piemērs:**
  Par Gausa veselajiem skaitļiem sauc skaitļus formā :math:`a + bi`.
  Daži no tiem ir pirmskaitļi (tos nevar izteikt kā divu Gausa veselo skaitļu
  reizinājumu, ja vien kāds no reizinātājiem nav :math:`1`, :math:`-1`,
  :math:`i` vai :math:`-i`). Piemēram :math:`1+i` ir Gausa pirmskaitlis.
  Bet :math:`2` nav Gausa pirmskaitlis, jo :math:`2 = (1 + i)(1 - i)`.

  Pamatot, ka ir Gausa pirmskaitļu ir bezgalīgi daudz.

  **Ieteikums 1:** Pietiek aplūkot tos Gausa pirmskaitļus, kuri ir vienlaikus
  naturāli skaitļi.

  **Ieteikums 2:** Ja apzīmējam :math:`|a+bi| = \sqrt{a^2 + b^2}`, tad
  komplekso skaitļu reizināšanai izpildās sakarība:

  .. math::

    |(a + bi)(c + di)| = |a + bi| \cdot |c + di|.



Klases uzdevumi
-------------------

**1.jautājums**
  Rindā novietoti :math:`30` slēdži ar numuriem no :math:`1` līdz :math:`36`.
  Katrs slēdzis var būt ieslēgts vai izslēgts; sākumā tie visi ir izslēgti.
  Pirmajā solī pārslēdz pretējā stāvoklī visus slēdžus, kuru
  numuri dalās ar :math:`1`. Otrajā solī pārslēdz visus tos, kuru
  numuri dalās ar :math:`2`. Un tā tālāk - līdz 30.solī pārslēdz pretējā
  stāvoklī slēdžus, kuru numuri dalās ar :math:`30`.
  Cik daudzi slēdži kļūst ieslēgti pēc visu soļu pabeigšanas?

**2.jautājums:**
  Dots skaitlis :math:`N = 60`.
  Atrast visu pozitīvo dalītāju skaitu,
  visu pozitīvo dalītāju summu un visu pozitīvo dalītāju kvadrātu summu.

**3.jautājums:**
  Atrast mazāko naturālo skaitli :math:`M`, kam ir tieši :math:`16` dalītāji.

**4.jautājums:**
  Naturālam skaitlim :math:`n` ir tieši :math:`125` pozitīvi
  dalītāji (ieskaitot :math:`1` un pašu :math:`n`).
  Kādu visaugstākās pakāpes sakni noteikti var izvilkt no
  :math:`n`, iegūstot naturālu rezultātu?


**Definīcija:**
  Par :math:`n`-to Fermā skaitli
  (:math:`n \geq 0`) sauc :math:`F_n = 2^{2^n}+1`.

**5.jautāums:**
  Pierādīt, ka naturāliem skaitļiem :math:`m` un :math:`n`,
  kam :math:`m > n`, Fermā skaitlis :math:`F_m - 2` noteikti
  dalās ar :math:`F_n`.


**6.jautājums (BW.TST.2016.16):**
    Kāda ir izteiksmes

    .. math::

      \text{LKD}\left( n^2 + 3, (n+1)^2 + 3 \right)

    lielākā iespējamā vērtība naturāliem :math:`n`?





Mājasdarba uzdevumi
---------------------

**Iesniegšanas termiņš:**
  2022.g. 5.novembris.

**Kam iesūtīt:**
  ``kalvis.apsitis``, domēns ``gmail.com``

**1.uzdevums:**
  Naturālu skaitli sauksim par *elegantu*, ja tā decimālajā pierakstā nav nevienas nulles un šis skaitlis dalās ar
  savu ciparu summu. (Eleganti ir visi viencipara skaitļi, kā arī, piemēram, skaitļi :math:`36` un :math:`322`.)
  Pierādīt, ka ir bezgalīgi daudz elegantu skaitļu!

**2.uzdevums:**
  Zināms, ka trīsciparu skaitlis :math:`\overline{abc}` ir pirmskaitlis un ka vienādojumam
  :math:`ax^2 + bx + c = 0` ir divas reālas saknes. Vai var
  gadīties, ka šīs saknes ir **(a)** veseli skaitļi, **(b)** racionāli skaitļi?

**3.uzdevums:**
  Divi spēlētāji pamīšus raksta uz tāfeles naturāla skaitļa :math:`N` naturālos dalītājus.
  Katrā gājienā jāievēro šādi noteikumi:

    * nedrīkst atkārtoti rakstīt jau uzrakstītu dalītāju;
    * nedrīkst rakstīt dalītāju, kurš ir tieši :math:`2` vai :math:`3` reizes lielāks vai mazāks nekā kāds jau uzrakstītais dalītājs.

  Zaudē tas spēlētājs, kurš nevar izdarīt gājienu. Kurš spēlētājs – pirmais vai
  otrais – vienmēr var uzvarēt?

  Pamatot atbildi šādām vērtībām: :math:`N = 144` un :math:`N = 216`.

**4.uzdevums:**
  Skaitļi :math:`p,q` ir pirmskaitļi un :math:`p>q`. Definējam :math:`t = \gcd(p!-1,q!-1)`.
  Pierādīt, ka :math:`t \leq p^{\frac{p}{3}}`.

**5.uzdevums:**
  A. Atrast visus naturālos skaitļus :math:`n`, ka jebkuram nepāra skaitlim :math:`a` izpildās :math:`4 \mid a^n-1`.
  B. Atrast visus naturālos skaitļus :math:`n`, ka jebkuram nepāra skaitlim :math:`a`, izpildās :math:`2^{2017} \mid a^n-1`.

**6.uzdevums:**
  Atrast visus veselo skaitļu trijniekus :math:`(a, b, c)`, kas apmierina vienādojumu:

  .. math::

    5 a^2 + 9 b^2 = 13 c^2.
