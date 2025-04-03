Loģika un algoritmi
======================

**Apgalvojums:** 
  Ja svēršanai uz sviras svariem ir divi iznākumi (vieglāks, smagāks), tad 
  pēc :math:`n` svēršanām ar šiem svariem var atšķirt ne vairāk kā :math:`2^n` dažādus stāvokļus. 
  Ja ir trīs iznākumi (vieglāks, vienāds, smagāks), tad 
  pēc :math:`n` svēršanām ar šiem svariem var atšķirt ne vairāk kā :math:`3^n` dažādus stāvokļus. 


**Apgalvojums:** 
  Ja doti :math:`n` objekti ar dažādu svaru un katrā svēršanā var salīdzināt 
  divus, tad objektu sakārtošanai minimāli nepieciešamo svēršanu skaits attēlots tabulā: 

  ==========  ============  ==========  ==========  ==========  ===========  =============  
  :math:`n`   :math:`1`     :math:`2`   :math:`3`   :math:`4`   :math:`5`    :math:`6`
  ==========  ============  ==========  ==========  ==========  ===========  =============
  :math:`n!`  :math:`1`     :math:`2`   :math:`6`   :math:`24`  :math:`120`  :math:`720`
  Svēršanas   :math:`0`     :math:`1`   :math:`3`   :math:`5`   :math:`7`    :math:`10`   
  ==========  ============  ==========  ==========  ==========  ===========  ============= 

  Sk. `Comparison sort <https://en.wikipedia.org/wiki/Comparison_sort>`_.
  (Ja neparasti veicas, tad :math:`n` objektus var sakārtot pat ar :math:`n-1` svēršanām.)

**Apgalvojums:** 
  Lai :math:`n` virsotnes savienotu sakarīgā grafā, jānovelk vismaz :math:`n-1` šķautnes.

**1.uzdevums:** 
  Milzis Lutausis noķēra 4 bērnus. Katram no viņiem aizsēja acis un uzlika galvā cepuri
  (ir zināms, ka diviem bērniem cepures ir melnas, diviem bērniem -- baltas). 
  Viņš nostāda trīs bērnus vienā pusē augstai sienai, bet ceturto -- otrā pusē sienai. 
  Faktiski viņš bērnus izvietojis, kā parādīts zīmējumā (bet konkrētais novietojums 
  pašiem bērniem nav zināms). 

  .. figure:: figs/hats-puzzle.png
     :width: 2in

  5 minūšu laikā kādam no bērniem ir pareizi jānosaka pašam savas cepures krāsa.
  Ja viņš nosaka to pareizi, tad visus bērnus atbrīvo, ja kāds nosauc cepures 
  krāsu nepareizi, tad visus bērnus apēd. 
  Bērni zina, cik minūšu vēl atlicis. 

  Atrast veidu, kā bērniem panākt, lai viņus vienmēr atbrīvo (iespēja nejauši 
  minēt savas cepures krāsu un izdzīvot 
  ar varbūtību :math:`0.5` viņus neapmierina). 




**LV.SOL.2010.8.4:** 
  Dotas :math:`2010` pēc ārējā izskata vienādas monētas; to masas visas ir atšķirīgas.
  Doti arī sviras svari bez atsvariem. Uz katra kausa uzliekot pa vienai monētai,
  smagākā no tām nosveras uz leju.
  
  **(A)** Pierādīt, ka gan smagāko monētu vienu pašu, gan vieglāko monētu vienu
  pašu var atrast, izdarot :math:`2009` svēršanas.

  **(B)** Vai abas šīs monētas -- gan smagāko, gan vieglāko -- var atrast, izdarot
  mazāk nekā :math:`4000` svēršanas? 


**LV.NOL.2010.7.5:** 
  Seši rūķīši katrs uzzinājuši vienu jaunu ziņu (katrs citu). Katram 
  mājās ir telefons, un viena saruna ilgst vienu stundu. Tās laikā abi 
  runātāji pagūst viens otram izstāstīt visus jaunumus.
  Kāds ir mazākais stundu skaits, kuru laikā visi rūķīši var uzzināt 
  visus jaunumus?


**LV.SOL.2014.7.4:** 
  Dotas :math:`8` pēc ārējā izskata vienādas monētas. No tām :math:`7` ir ar vienādu 
  masu, bet vienas monētas masa ir citāda. Doti arī sviras svari bez 
  atsvariem. Kā ar :math:`3` svēršanu palīdzību atrast atšķirīgo monētu?


**LV.NOL.2015.7.5:** 
  Uz galda rindā novietotas sešas monētas, zināms, ka starp tām ir vismaz 
  viena īsta un vismaz viena viltota monēta, kas ir vieglāka nekā īstā. 
  Visas īstās monētas sver vienādi, un arī visas viltotās monētas sver 
  vienādi, bet ir vieglākas par īstajām. No katras īstās monētas pa labi 
  (ne noteikti blakus) atrodas kāda viltota monēta, bet no katras viltotās 
  pa kreisi (ne noteikti blakus) atrodas kāda īsta monēta. Kā ar divām 
  svēršanām ar sviru svariem bez atsvariem var noteikt katra veida monētu skaitu?


**LV.NOL.2019.8.2:** 
  Zināms, ka no :math:`26` monētām viena ir viltota -- tā ir 
  vieglāka nekā pārējās, kurām visām ir vienāda masa. Kā ar trīs
  svēršanām uz sviras svariem bez atsvariem atrast viltoto monētu?


**LV.NOL.2019.9.2:** 
  Dotas divas melnas, divas sarkanas un divas zaļas lodītes. Vienas 
  lodītes masa ir :math:`99 \mathrm{~g}`, bet tādas pašas krāsas otras 
  lodītes masa ir :math:`101 \mathrm{~g}`. Pārējās četras lodītes katra 
  sver :math:`100 \mathrm{~g}`. Kā, lietojot sviras svarus bez atsvariem, 
  ar divām svēršanām atrast vieglāko lodīti?


**LV.NOL.2020.8.5:** 
  Dotas :math:`8` pēc ārējā izskata vienādas monētas. Ir zināms, ka vai 
  nu visām tām masas ir vienādas, vai arī :math:`4` monētām ir viena masa,
  bet :math:`4` monētām -- cita masa. Kā ar :math:`2` svēršanām uz sviras 
  svariem bez atsvariem var noskaidrot, kura no iespējām pastāv īstenībā?


**LV.NOL.2019.7.2:** 
  Dotas :math:`14` pēc ārējā izskata vienādas monētas. Zināms, ka 
  :math:`13` monētu masas ir vienādas savā starpā, bet vienas monētas 
  masa ir citāda. Kā ar divām svēršanām uz sviras svariem bez atsvariem 
  noskaidrot, vai atšķirīgā monēta ir vieglāka vai smagāka nekā pārējās? 
  (Pašu monētu atrast nav nepieciešams.)


**LV.AMO.2013.8.5:**
  Rūķītis ir iedomājies skaitļus :math:`x_{1}, x_{2}, x_{3}` un 
  :math:`x_{4}`, katrs no tiem 
  ir vai nu :math:`0`, vai :math:`1`. Ja rūķītim pajautā: "Kāds ir :math:`i`-tais skaitlis?" 
  (:math:`i=1,2,3` vai :math:`4` pēc izvēles), tad viņš pasaka :math:`x_{i}` vērtību.
  Pierādīt, ka ar :math:`3` jautājumiem pietiek, lai uzzinātu, vai virkne 
  :math:`x_{1},\ x_{2},\ x_{3},\ x_{4}` ir monotona.

  Skaitļu virkne :math:`x_{1},\ x_{2},\ x_{3},\ x_{4}` ir monotona, ja tā ir nedilstoša
  vai neaugoša (t. i., :math:`x_{1} \leq x_{2} \leq x_{3} \leq x_{4}` vai 
  :math:`x_{1} \geq x_{2} \geq x_{3} \geq x_{4}`).


**LV.AMO.2015.7.5:**
  Uz galda stāv četras pēc izskata vienādas bumbiņas, to masas attiecīgi ir
  :math:`10`, :math:`11`, :math:`12` un :math:`13` grami. Vai ar dažām svēršanām uz sviru svariem bez
  atsvariem, kur katrā kausā drīkst ielikt tieši divas bumbiņas, iespējams
  **(A)** atrast visvieglāko un vissmagāko bumbiņu;
  **(B)** noteikt katras bumbiņas masu?


**LV.AMO.2016.9.5:** 
  Sivēnam ir :math:`10` podi ar medu, kas pēc kārtas sanumurēti ar skaitļiem
  no :math:`1` līdz :math:`10`. Kādu dienu viņš uzzināja, ka Vinnijs Pūks slepeni 
  ir izēdis četrus no tiem, pie tam to numuri veido aritmētisko 
  progresiju. Katra poda saturu Sivēns var pārbaudīt. Pierādīt, ka 
  viņš var noskaidrot, kuri tieši ir izēstie podi, pārbaudot ne 
  vairāk kā četrus podus!


**LV.AMO.2017.8.4:**
  Doti pieci pēc izskata vienādi atsvari. Katra atsvara masa izsakāma veselā
  skaitā gramu, turklāt šie skaitļi ir pēc kārtas esoši naturāli skaitļi. Atsvaru masu
  salīdzināšanai atļauts izmantot sviru svarus, kur katrā svaru kausā drīkst likt
  tieši divus atsvarus. Vai iespējams
  **(A)** noteikt visvieglāko un vissmagāko no atsvariem;
  **(B)** sarindot visus atsvarus pēc kārtas no smagākā līdz vieglākajam?

  *Piezīme.* Ar sviru svariem nevar noteikt, tieši par cik gramiem viens 
  svaru kauss ir smagāks nekā otrs.

**LV.AMO.2023.8.5:**
  Uz palodzes sēž vairākas bizbizmārītes, katrai no tām uz muguras ir 
  vai nu trīs punktiņi, vai astoņi punktiņi. Tās
  bizbizmārītes, kurām uz muguras ir astoņi punktiņi, vienmēr saka patiesību, 
  bet tās bizbizmārītes, kurām uz
  muguras ir trīs punktiņi, vienmēr melo. Katra bizbizmārīte izteicās:

  * pirmā bizbizmārīte teica: "punktiņu skaits uz muguras mums visām ir vienāds";
  * otrā teica: "mums visām kopā uz muguras ir 38 punktiņi";
  * trešā teica: "nē, mums visām kopā uz muguras ir 48 punktiņi";
  * katra no atlikušajām bizbizmārītēm teica: "no pirmajām trijām bizbizmārītēm 
    tieši viena teica patiesību". 
    
  Cik bizbizmārītes sēž uz palodzes?