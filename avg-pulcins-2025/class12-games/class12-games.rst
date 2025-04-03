Kombinatoriskas spēles
============================

**Definīcijas:**
  *Kombinatoriskas spēles* stāvoklim eksistē galīgs apraksts; katrā stāvoklī eksistē 
  galīgs skaits iespējamo gājienu; pēc noteikta skaita gājienu spēle beidzas un 
  katrs spēlētājs iegūst rezultātu.
  Kombinatoriskas spēles atšķirībā no futbola utml. var analizēt matemātiski.
  Kombinatoriskām spēlēm ir vairāki varianti: 

  * Par *secīgu spēli* (*sequential game*) sauc spēli, kurā vairāki spēlētāji 
    pārmaiņus veic gājienus un var atbildēt uz citu spēlētāju gājieniem.  
    (Akmens-papīrs-šķēres ir *vienlaicīga*/*simultaneous* nevis secīga.)
  * Par *pilnas informācijas spēli* (*perfect information game*)
    sauc spēli, kuras stāvoklis ir visiem zināms. 
    (Spēles, kur nerāda viens otram savas kārtis, nav ar pilnu informāciju.)
  * Par *deterministisku spēli* sauc spēli, kurā izdarāmie gājieni nav atkarīgi no 
    varbūtiskiem procesiem. 
    (Spēles, kur gājienus nosaka metamais kauliņš utml. **nav** deterministiskas.
    Kāršu spēlēs sākumstāvoklis ir varbūtisks, bet gājieni var būt arī deterministiski.)
  * Par *nulles summas spēli* sauc spēli, kurā viens spēlētājs uzvar tad un tikai 
    tad, ja otrs spēlētājs tikpat daudz zaudē. 
    (Šahs ir nulles summas spēle: arī ja par uzvaru ieskaita :math:`1` punktu, bet
    par zaudējumu :math:`0` punktus, tomēr uzvara vienam nozīmē zaudējumu otram. 
    Tirdzniecība, uzņēmējdarbība, karš, "cietumnieku dilemma" **nav** nulles summas 
    spēles - spēlētāju rezultātu summa nav vienmēr nulle.)


**Definīcija:** 
  Pirmajam spēlētājam ir *uzvaroša stratēģija* spēles stāvoklī :math:`s \in S`, 
  ja viņš var panākt uzvaru neatkarīgi no tā, kā spēlē otrais spēlētājs. 
  Šos sauc par :math:`N`-stāvokļiem (tajos uzvaru var panākt *Nākošais* spēlētājs jeb *Next*) 
  un parasti krāso sarkanus. Tos stāvokļus, no kuriem neeksistē uzvaroša stratēģija sauc par 
  :math:`P`-stāvokļiem (tajos uzvaru var panākt *iePriekšējais* spēlētājs jeb *Previous*), 
  tos krāso zilus. 

  .. figure:: figs/p-n-positions.png
     :width: 3in


**LV.AMO.2002.7.4:**
  Divi spēlētāji pamīšus raksta uz tāfeles pa vienam naturālam skaitlim no 
  1 līdz 8 ieskaitot. Nedrīkst rakstīt skaitļus, ar kuriem dalās kaut viens 
  jau uzrakstīts skaitlis. Kas nevar izdarīt gājienu, zaudē.
  **(A)** Pierādiet, ka pirmais spēlētājs var uzvarēt.
  **(B)** Parādiet, kā pirmais spēlētājs var uzvarēt.

**Piemērs (Chomp/Šņak):**
  Šokolādes tāfelītei ir :math:`m \times n` kvadrātiņi. Divi spēlētāji pārmaiņus 
  izdara gājienus - izvēlas spēles taisnstūrī neaiztiktu kvadrātiņu un to 
  "apēd" -- atdala no taisnstūra kopā ar visām rūtiņām, kas no izvēlētās 
  atrodas uz leju vai pa labi. Kvadrātiņš kreisajā augšējā stūrī ir saindēts - spēlētājs, 
  kuram tas jāizvēlas, zaudē. Kurš uzvar pareizi spēlējot? 

  .. figure:: figs/chocolate-bar.png
     :width: 1.2in

**LV.NOL.2018.5.5:**
  Divi spēlētāji pēc kārtas ņem konfektes no konfekšu kaudzes. Katrā 
  gājienā jāpaņem vismaz viena, bet ne vairāk kā septiņas konfektes. 
  Uzvar tas spēlētājs, kurš paņem pēdējo konfekti. Kurš no spēlētājiem 
  (pirmais vai otrais) vienmēr var uzvarēt (neatkarīgi no pretinieka 
  gājieniem), ja sākumā konfekšu kaudzē ir **(A)** :math:`64` konfektes, 
  **(B)** :math:`2018` konfektes?



**LV.NOL.2003.9.5:**
  Uz galda atrodas :math:`n` konfektes. Andris un Pēteris pēc kārtas izdara
  gājienus; pirmais iet Andris. Ar vienu gājienu tiek paņemtas dažas
  konfektes; pie tam jāņem vismaz :math:`1` konfekte, bet nedrīkst ņemt vairāk
  par pusi uz galda esošo konfekšu. Tas zēns, pēc kura gājiena uz galda
  paliek :math:`1` konfekte, zaudē. Kas uzvar, pareizi spēlējot, ja
  **(A)** :math:`n = 47`, **(B)** :math:`n = 2003`? 


**LV.NOL.2014.7.1:**
  Dots vienādojums

  .. figure:: figs/LV.NOL.2014.7.1.png
     :width: 0.9in

  Ariadne vienā (jebkurā) rūtiņā ieraksta vienu skaitli, pēc tam Eleonora 
  citā rūtiņā ieraksta vienu skaitli un beidzot Ariadne ieraksta skaitli 
  atlikušajā tukšajā rūtiņā. Pierādīt, ka Ariadne var panākt jebkuru no 
  trim situācijām:

  **(A)** vienādojumam ir tieši viens atrisinājums;
  **(B)** vienādojumam nav atrisinājumu;
  **(C)** vienādojumam ir bezgalīgi daudz atrisinājumu.
  (Spēles sākumā jau zināms, kuru situāciju jāiegūst.)


**LV.NOL.2008.7.2:**
  Ir :math:`4` tortes gabali ar masām :math:`x, y, z, t`; dots, ka 
  :math:`x < y < z < t`. Andris un Maija spēlē šādu spēli. Andris 
  izvēlas vienu tortes gabalu, pēc tam Maija -- otru; abi
  bērni nekavējoties sāk ēst. Tikko kāds savu gabalu apēdis, viņš 
  nekavējoties izvēlas kādu gabalu no atlikušajiem un sāk ēst to, utt. 
  Spēles mērķis ir apēst vairāk tortes nekā otram. Abi bērni torti 
  ēd vienmērīgi un ar vienādiem ātrumiem.
  Vai var gadīties, ka Andris uzvar, no sākuma izvēloties gabalu :math:`x`? 
  Uzskatām, ka Maija noteikti ēd torti sev visizdevīgākajā veidā. 





**LV.NOL.2021.7.3:** 
  Torte sagriezta 12 gabaliņos (skat. 8. att.). Brālītis un Karlsons 
  pēc kārtas izdara gājienus, Brālītis sāk pirmais. Vienā gājienā var 
  apēst vai nu vienu tortes gabaliņu, vai divus blakus esošus gabaliņus 
  (blakus esoši gabaliņi ir gabaliņi, kam ir kopīga mala). Uzvar tas, 
  kurš apēd pēdējo gabaliņu. Kurš uzvarēs, pareizi spēlējot, un kā
  viņam jārīkojas?

  .. figure:: figs/LV.NOL.2021.7.3.png
     :width: 1.0in



**LV.NOL.2017.11.5:**
  Antra un Baiba spēlē spēli uz :math:`3 \times 3` rūtiņu laukuma. 
  Spēlētājas gājienus izdara pēc kārtas, katrā gājienā
  kādā no tukšajām rūtiņām ierakstot vai nu nullīti, vai krustiņu 
  (katra spēlētāja katrā gājienā var rakstīt jebkuru no šiem simboliem). 
  Kad viss laukums aizpildīts, tiek saskaitīts spēles rezultāts. Par 
  katru rindu, kolonnu un diagonāli (tādu, kas satur :math:`3` rūtiņas), 
  ja tajā ir pāra skaits krustiņu, punktu saņem Antra, bet, ja
  krustiņu skaits ir nepāra, tad punktu saņem Baiba. Uzvar spēlētāja, 
  kuras punktu kopsumma ir lielāka. Pierādīt, ka spēlētājai, kura sāk spēli, 
  ir uzvaroša stratēģija, un aprakstīt to!
  

**LV.NOL.2000.12.5:**
  Pa apli novietotas :math:`2000` konfektes. Divi spēlētāji pārmaiņus apēd pa trim patvaļīgām
  konfektēm, kamēr aplī paliek 2 konfektes. Ja tās spēles sākumā atradās blakus, 
  uzvar otrais spēlētājs; ja tās spēles sākumā neatradās blakus, uzvar pirmais spēlētājs.
  Kas uzvar, pareizi spēlējot?


**LV.NOL.2002.8.2:**
  Andris un Jānis spēlē spēli. Viņi pamīšus izdara pa vienam gājienam;
  sāk Andris. Andris ar katru savu gājienu uzraksta vienu no cipariem
  septiņciparu skaitlī (vispirms pirmo, tad otro, trešo, ...), izmantojot
  tikai ciparus :math:`1` un :math:`2`. 
  Savukārt Jānis pēc katra Andra gājiena ar savu
  gājienu vai nu nedara neko, vai arī apmaina vietām divus jau
  uzrakstītus ciparus. Vai Jānis var panākt, ka beigās iegūtais
  septiņciparu skaitlis ir simetrisks (t.i., šis skaitlis ir viens 
  un tas pats, lasot to "no sākuma" un "no gala")?



**LV.NOL.2006.9.5:**
  Gunārs un Dzintars pamīšus raksta uz tāfeles pa vienam naturālam skaitlim,
  kas nepārsniedz :math:`1000`. Sāk Dzintars, uzrakstot skaitli :math:`1`. Neviens jau uzrakstīts
  skaitlis netiek nodzēsts; nevienu skaitli nedrīkst rakstīt otrreiz.
  Ja kaut kāds skaitlis x jau ir uz tāfeles, tad ar kārtējo gājienu drīkst uzrakstīt
  vai nu :math:`x+1`, vai :math:`2x` (ja izvēlētais rakstāmais skaitlis 
  nepārsniedz :math:`1000`). Tas, kurš uzraksta :math:`1000`, uzvar. Kurš no zēniem uzvar, 
  pareizi spēlējot? 






