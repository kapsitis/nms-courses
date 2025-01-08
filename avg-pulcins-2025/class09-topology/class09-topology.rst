Topoloģija
=============

**Definīcija:** 
  Funkciju :math:`f`, kas attēlo punktu kopu :math:`A` par 
  punktu kopu :math:`B` sauc par *nepārtrauktu punktā* :math:`x_0 \in A`, 
  ja katrai punkta :math:`f(x_0)` epsilon-apkārtnei 
  (:math:`\varepsilon >0`) eksistē tik maza punkta :math:`x_0` 
  delta-apkārtne (:math:`\delta > 0`), ka visi punkti no šīs delta-apkārtnes 
  ar funkciju :math:`f` attēlojas uz punkta :math:`f(x_0)` epsilon-apkārtni. 
  Funkciju :math:`f` sauc par *nepārtrauktu*, ja tā ir nepārtraukta visos 
  punktos :math:`x_0 \in A`.
  (Epsilon-apkārtne ir vai nu nogrieznis :math:`(x_0 - \varepsilon; x_0 + \varepsilon))`
  vai aplītis ar rādiusu :math:`\varepsilon`

Nepārtrauktai  funkcijai :math:`f` nedrīkst būt *pārtraukuma punkti*, kur
ļoti tuvas vērtības ar funkciju :math:`f` attēlojas uz vērtībām, 
kas ir tālu viena no otras.

**Piemērs:** 
  Fizikā par "materiālu punktu" sauc nelielu ķermeni ar masu.
  (Neliela ķermeņa izmērus uzdevumā var neņemt vērā.)
  Vai materiāla punkta koordinātes mainās nepārtraukti? 
  Vai materiāla punkta ātrums mainās nepārtraukti?  
  *Punkta koordinātes nemēdz mainīties ar lēcienu (punkts nevar sasniegt 
  bezgalīgu ātrumu). Arī ātrums nevar 
  mainīties ar lēcienu, jo ātruma izmaiņas izraisa spēks, kas piešķir paātrinājumu.*


**Piemērs:**
  Kādā valstī iedzīvotāju ienākumu nodoklim (IIN) ir neapliekamais minimums 
  :math:`500` EUR mēnesī (ar nodokli neapliek). Par darba algas daļu no 
  :math:`500` līdz :math:`1667` savāc :math:`20\%` nodokli, 
  bet par darba algas daļu virs :math:`1667` mēnesī savāc :math:`23\%` 
  nodokli.  Uzzīmēt funkciju, kas parāda uz vertikālās ass
  darba samaksu pēc nodokļa ("uz rokas"), ja zināms, cik ir 
  darba samaksa pirms šī nodokļa (bruto jeb "uz papīra").
  Ar `Desmos Calculator <https://www.desmos.com/calculator>`_ 
  var iekopēt izteiksmi:

  .. code-block:: text
  
    y = { 0 <= x <= 500:x, 500 < x <= 1667: 500 + 0.8 * (x-500) }

  *Var zīmēt grafiku arī citiem skaitļiem, ja šie izskatās piņķerīgi.*
  Latvijā faktiskie nodokļi nedaudz atšķiras no šīs kārtības.  
  Sk. `IIN likmes <https://www.vid.gov.lv/lv/iedzivotaju-ienakuma-nodokla-likmes>`_. 

**1.uzdevums:** 
  Latīņu alfabēta burtus sadalīt grupās, kur katrā grupā burti ir savstarpēji 
  homeomorfi (vienu burtu var deformēt par otru burtu, izmantojot nepārtrauktu 
  funkciju)? 

  .. figure:: figs/letters.png
     :width: 3in


**2.uzdevums:** 
  Vai var savienot mazos kvadrātiņus zīmējuma augšpusē ar
  tāda paša burta kvadrātiņiem zīmējuma apakšpusē tā, lai 
  taciņas nekrustotos un arī neizietu ārpus lielā taisnstūra?

  .. figure:: figs/zeitz-paths.png
     :width: 1.8in

**3.uzdevums:**
  **(A)** 
    Uzzīmēt zīmējumā attēloto "atvērto aploksni", neatraujot 
    pildspalvu no papīra un nevelkot nevienu posmu divreiz. 
    Kur sākas un kur beidzas pildspalvas maršruts?

    .. figure:: figs/envelope.png
       :width: 1in

  **(B)**
    Vai eksistē pastaigas maršruts, kas katru no 7 tiltiem 
    šķērso tieši vienreiz (pastaigai nav jāatgriežas sākumpunktā). 

    .. figure:: figs/koenigsberg.png
       :width: 1.8in


**4.uzdevums:** 
  Izgriezt papīra joslu (platuma attiecība pret garumu apmēram :math:`1:8`) 
  un salīmēt no tās Mēbiusa lentu. Veikt kādu no sekojošiem vingrinājumiem: 

  **(A)** 
    Vilkt pa Mēbiusa lentas vidu viļņainu līniju līdz tā apiet apkārt papīra 
    gredzenam un atgriežas sākumpunktā. Vai Mēbiusa lentai var nokrāsot 
    vienu tās pusi?

  **(B)** 
    Vilkt līniju gar Mēbiusa lentas maliņu līdz tā atgriežas sākumpunktā. 
    Vai skudriņa var apiet visapkārt lentai gar vienu Mēbiusa lentas malu, neaiztiekot 
    otru šīs lentas malu?

  **(C)** 
    Ar šķērēm griezt Mēbiusa lentu gareniski pa tās viduslīniju. Kāda veida lenta vai lentas 
    izveidojas? Par cik pusapgriezieniem ir savērpta šī lenta vai lentas? 
    (Mēbiusa lenta pati ir savērpta ar **vienu** pusapgriezienu par :math:`180^{\circ}`). 

  **(D)** 
    Ar šķērēm griezt Mēbiusa lentu gareniski pa līniju, kas ir aptuveni :math:`1/3` 
    attālumā no tās sānu malas. (Pieņemam, ka lentas platums ir :math:`1` vienība.)
    Kāda veida lenta vai lentas izveidojas?

  .. figure:: figs/moebius-strips.png
     :width: 4in


**5.uzdevums:** 
  Iezīmēt "Mēbiusa lentu" savā burtnīcā kā parastu taisnstūri 
  (šoreiz neko negriežot un nelīmējot). 
  Lai taisnstūrim būtu "Mēbiusa lentas topoloģija" iedomāties, ka 
  tā ir taisnstūris, kuram (apgrieztā secībā) salīmētas pretējās malas. 
  Uz Mēbiusa lentas ir :math:`3` raganu mājiņas (atzīmēt kvadrātiņus) un 
  tur ir arī :math:`3` akas (atzīmēt aplīšus). 
  Novilkt taciņas no katras raganu mājiņas uz katru aku tā, 
  lai tās nekrustotos. Taciņas drīkst iet arī pāri salīmētajai malai
  (bet jāņem vērā, ka taciņas ienāks atpakaļ taisnstūrī apgrieztā secībā).



**6.uzdevums:** 
  Izmantojot kādu apaļu priekšmetu, uzzīmējiet precīzu pusapli un 
  zem pusapļa novelciet taisnu līniju. Pusapli sadaliet 8 vienādos lokos. 
  Pusapļa centrā iztēlojieties iedegtu spuldzīti. 
  Parādiet, kur uz taisnes "kritīs ēna" katram no 8 atzīmētajiem lokiem. 
  Vai katram punktam uz pusapļa atbilst punkts uz taisnes un arī otrādi? 
  Vai šis attēlojums ir nepārtraukts?
  Vai galīgu intervālu :math:`(-90^{\circ}, 90^{\circ})` var homeomorfi attēlot 
  par bezgalīgu taisni :math:`(-\infty, +\infty)`? 
  Sk. arī `Azimutāla projekcija <https://en.wikipedia.org/wiki/Azimuthal_equidistant_projection>`_, 
  kas Zemeslodi (vai vienu tās puslodi) projicē plaknē.




