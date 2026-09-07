# Matemātikas olimpiāžu fakultatīvs 7.–8. klasei — programmas paraugs (B gads)

**10 temati × 2 nodarbības (90 min) + fiksētie notikumi; kopā 28 nedēļas (12 rudenī, 16 pavasarī).**

Programma veidota kā **rotācijas otrais gads** attiecībā pret iepriekšējā gada 12 tematu programmu:

* **Mugurkaula temati atgriežas ar jaunu slāni.** Invarianti (pērn — izteiksmes un P/N pozīcijas) šogad turpinās ar krāsojumiem un monovariantiem; Dirihlē princips (pērn — atsevišķs temats) šogad parādās sapārots ar ekstremālā elementa metodi novērtējumu uzdevumos; spēles (pērn — P/N pozīciju analīze) šogad — simetrijas un pārošanas stratēģijas. Tā skolēns, kurš apmeklē abus gadus, metodi redz divreiz dažādos rakursos (noturībai), bet neredz vienus un tos pašus uzdevumus.
* **Jaunie temati aizpilda pērn neskartās jomas:** uzdevumu "gramatika" (atbilžu tipi un pamatojuma struktūra), ekstremālais elements, divkāršā skaitīšana, trijstūra nevienādība, laukumi koordinātu plaknē, loģikas uzdevumi, vienādojumi veselos skaitļos.
* **Domēnu līdzsvars** atbilst 7.–8. klases NOL/AMO uzdevumu korpusa proporcijām: ~5 kombinatorikas rakstura temati, 2 skaitļu teorijas, 2 ģeometrijas, 1 jaukts (algebra iestrādāta 1., 8. un 10. tematā).

Katram tematam norādīti 2–4 sasniedzamie rezultāti (SR), atbilstošās klasifikatoru birkas (models.csv / methods.csv / questionTypes.csv) un piemēru uzdevumi no NOL/AMO korpusa (temata kartes izejmateriāls).

---

## Gada karkass

| Nedēļas | Saturs |
|---|---|
| R1–R2 | 1. temats. Olimpiādes uzdevuma "gramatika" |
| R3 | **Skolas olimpiāde** + analīze |
| R4–R5 | 2. temats. Krāsojumi un invarianti procesos |
| R6–R7 | 3. temats. Dirihlē princips un ekstremālais elements |
| R8–R9 | 4. temats. Dalāmība un atlikumu klases |
| R10–R11 | **AMO sprints** (iepriekšējo gadu komplektu izspēles laika kontrolē) |
| R12 | **AMO analīze** |
| P1–P2 | 5. temats. Spēles: simetrijas un pārošanas stratēģijas |
| P3–P4 | 6. temats. Divkāršā skaitīšana un grafu modeļi |
| P5–P6 | 7. temats. Trijstūra nevienādība un garumu novērtējumi |
| P7–P8 | **NOL sprints** (komplektu izspēles, individuālā stratēģija) |
| P9 | **NOL analīze** |
| P10–P11 | 8. temats. Taisnes, koordinātas un laukumi |
| P12 | **Ķengurs** + ātro atbilžu treniņš |
| P13–P14 | 9. temats. Loģikas uzdevumi: patiesie un meļi |
| P15–P16 | 10. temats. Vienādojumi veselos skaitļos un skaitļu konstrukcijas |

Katra temata materiāli pēc tā beigām atgriežas nākamo nodarbību atsaukšanas testiņos (+2 un +6 nedēļas) un sprintu jauktajās lapās.

---

## Rudens semestris

### 1. temats. Olimpiādes uzdevuma "gramatika": atbilde un pamatojums

Caurviju temats, ko atkārto katru gadu (jaunajiem septītklasniekiem tas ir jauns, pērnajiem — padziļinājums ar citiem uzdevumiem). Ievieš jautājumu tipu valodu, ko pēc tam lieto visos pārējos tematos.

* a. SR: Atšķir olimpiāžu jautājumu pamattipus — "atrast visus", "vai var?", "lielākā/mazākā vērtība", "pierādīt", "konstruēt piemēru" — un zina katram atbilstošo pilnas atbildes struktūru (piem., "atrast visus" = atrast + pamatot, ka citu nav).
* b. SR: Apgalvojumu "var / eksistē" pamato ar konkrētu piemēru, bet "nevar / vienmēr" — ar vispārīgu spriedumu; optimizācijas uzdevumā uzraksta abas daļas: piemēru un novērtējumu.
* c. SR: Sistemātiski izmanto mazos gadījumus un sakārtotu pilno pārlasi; pieraksta gadījumu sadalījumu tā, lai no pieraksta redzams, ka neviens gadījums nav izlaists.

Birkas: questionTypes (FindAll, ProveDisprove, FindOptimal, FindExample, Prove); MTH_ExhaustiveAlgorithms; ExhaustiveCaseEnumeration; hintLabels fāzes (Understand → Explore → Attack → Review) kā risināšanas rituāls.
Piemēri: LV.NOL.2024.7.2 (FindOptimal — piemērs + novērtējums), LV.AMO.2023.7.1 (ProveDisprove ar A/B daļām), LV.NOL.2024.7.3 (FindAll ar abu robežu pārbaudi).

### 2. temats. Krāsojumi un invarianti procesos

Turpina pērnā gada invariantu līniju ar jaunu slāni: krāsojumi kā invarianta speciālgadījums un monovariants.

* a. SR: Procesam (gājienu virknei, pārveidojumu spēlei) formulē paritātes vai atlikuma invariantu un korekti uzraksta neiespējamības pamatojumu ("invarianta vērtība sākumā atšķiras no vērtības mērķa stāvoklī").
* b. SR: Izvēlas piemērotu krāsojumu (šaha, joslu, trīs krāsu) pārklāšanas, sagriešanas vai apstaigāšanas neiespējamības pamatošanai un saprot, ka krāsojums ir invarianta konstruēšanas paņēmiens.
* c. SR: Pazīst monovariantu — lielumu, kas katrā gājienā tikai aug vai tikai dilst, — un lieto to procesa apstāšanās vai galīguma pamatošanai.

Birkas: ParityInvariant, ColoringInvariant, ModularInvariant, MonovariantArgument, TilingByDominoesAndColoring; MTH_FixedInvariant, MTH_AuxiliaryColoring.
Piemēri: LV.AMO.2022A.7.2 un LV.AMO.2022A.8.2 (gabalu skaita paritāte procesā), LV.AMO.2024.7.3 (virkne ar ×2, ×3, :2, :3), LV.NOL.2023.7.5 (lodīšu krāsu maiņa — atlikuma invariants).

### 3. temats. Dirihlē princips un ekstremālais elements

Dirihlē princips atgriežas no pērnā gada, bet uzsvars ir uz pāreju no principa uz pilnu novērtējuma pierādījumu, sapārojot to ar ekstremālā elementa metodi (abas metodes korpusā bieži sastopamas vienā uzdevumā).

* a. SR: Lieto vienkāršo un vispārināto Dirihlē principu, patstāvīgi izvēloties "kastes" (atlikumu klases, krāsas, rindas/kolonnas, ģeometriskus apgabalus).
* b. SR: Sāk spriedumu no ekstremālā elementa ("aplūkojam lētāko / lielāko / malējo...") un iegūst novērtējumus, sakārtojot elementus augošā secībā.
* c. SR: Uzraksta pilnu optimizācijas uzdevuma atrisinājumu abās daļās — konstruē piemēru un pierāda, ka labāks nav iespējams — un saprot, kura daļa dod kurus punktus olimpiādes vērtējumā.

Birkas: PigeonholeBasic, PigeonholeGeneralized, ExtremalPrincipleArgument; MTH_PigeonholePrincipleBasic, MTH_PigeonholePrincipleGeneralized, MTH_ExtremeElements, MTH_OrderingElements.
Piemēri: LV.NOL.2024.7.5 un LV.NOL.2024.8.4 (toršu pirkšana — ekstremālais elements + novērtējums), LV.NOL.2024.8.3 (punkti režģī — Dirihlē pa rindām).

### 4. temats. Dalāmība un atlikumu klases

Turpina pērnā gada decimālpieraksta un virkņu tematus: no dalāmības pazīmēm pie skaitīšanas ar atlikumiem.

* a. SR: Aprēķina lielu pakāpju un rekurentu virkņu atlikumus, izmantojot pēdējo ciparu / atlikumu periodiskumu.
* b. SR: Sadala naturālos skaitļus atlikumu klasēs pēc dotā moduļa un lieto šo sadalījumu gan skaitīšanas, gan neiespējamības uzdevumos (piem., kvadrāta atlikums dalot ar 4 ir tikai 0 vai 1).
* c. SR: Kombinē dalāmības pazīmes ar sadalīšanu pirmreizinātājos; lieto savstarpēju pirmskaitļu īpašību (ja skaitlis dalās ar m un n, kas savstarpēji pirmskaitļi, tad tas dalās ar mn) un atšķir to no nepareiziem vispārinājumiem.

Birkas: LastDigitOfPower, ModularArithmeticForRemainders, ResidueClassesPartition, DigitSumAndDivisibility, PrimeFactorizationStructure; topics: Divisibility, IntegerCongruence.
Piemēri: LV.NOL.2024.7.2 (ciparu summa un dalāmība ar 18), LV.NOL.2022.7.2 (vai ciparu summas dalāmība ar 27 garantē skaitļa dalāmību?), LV.AMO.2023.7.2 (septiņciparu skaitlis ar dalāmības nosacījumiem).

---

## Pavasara semestris

### 5. temats. Spēles: simetrijas un pārošanas stratēģijas

Papildina pērnā gada P/N pozīciju analīzi ar otru lielo spēļu uzdevumu instrumentu — stratēģijas konstruēšanu bez pozīciju pārlases.

* a. SR: Precīzi formulē, kas ir uzvaroša stratēģija ("apraksta, kā uzvarēt neatkarīgi no pretinieka gājieniem"), un atšķir stratēģijas aprakstu no vienas partijas piemēra.
* b. SR: Konstruē simetrijas (centrālās vai ass) stratēģiju un pamato tās korektumu — kāpēc atbildes gājiens vienmēr ir iespējams.
* c. SR: Konstruē pārošanas stratēģiju, sadalot laukuma rūtiņas vai pozīcijas pāros, un pamato, ka pāru sadalījums aptver visas iespējas.

Birkas: SymmetryStrategyInGames, PairingStrategyInGames, WinningLosingPositionAnalysis (atkārtojums); MTH_SymmetryWLOG.
Piemēri: LV.AMO.2019.7.2 (riņķis ar 15 daļām — simetrija ar korekcijas gājienu), LV.AMO.2019.8.2 (kauliņi 6×6 tabulā — pārošana), LV.NOL.2021.7.3 (tortes gabaliņu spēle).

### 6. temats. Divkāršā skaitīšana un grafu modeļi

Pērnā gada grafu temata turpinājums ar skaitīšanas rakursu — vieglāk pieejams arī tiem, kas grafu tematu nav dzirdējuši.

* a. SR: Attēlo attiecību situācijas ("draudzējas", "savienots ar vadu", "spēlēja pret") ar grafu un lieto rokasspiedienu lemmu: nepāra pakāpes virsotņu skaits ir pāra skaitlis.
* b. SR: Saskaita vienu lielumu divos veidos (pa rindām un kolonnām; pa dalībniekiem un pa pāriem) un no iegūtās vienādības vai nevienādības izdara secinājumu.
* c. SR: Pamato konfigurācijas neiespējamību ar kopsummas paritātes vai dalāmības argumentu.

Birkas: HandshakeLemmaApplication, GraphRepresentationOfRelations, TournamentDoubleCounting; MTH_DoubleCounting, MTH_GraphModel.
Piemēri: LV.NOL.2023.7.2 (90 vai 73 lampiņas ar 5 vadiem katrai), LV.NOL.2023.8.2 (draudzība ar tieši 3 cilvēkiem), LV.AMO.2024.7.5 (dziesmas, ko dzied pa trim), LV.AMO.2024.8.2 (skaitļi pa apli — blakusskaitļu summas).

### 7. temats. Trijstūra nevienādība un garumu novērtējumi

Ģeometrijas metriskā puse — pērn bija leņķi un vienādība, šogad garumu salīdzināšana un novērtēšana.

* a. SR: Lieto trijstūra nevienādību abos virzienos (summa un starpība), pārbaudot arī deģenerēto gadījumu (punkti uz vienas taisnes), un pamato, kuras robežvērtības ir sasniedzamas.
* b. SR: Novērtē lauztu līniju, perimetru un nogriežņu summu garumus, kombinējot vairākas trijstūra nevienādības.
* c. SR: Lieto sakarību "lielākajam leņķim pretī atrodas lielākā mala" un vienādsānu trijstūra īpašības garumu salīdzināšanas pierādījumos.

Birkas: TriangleInequalityModel; topics: GeometricInequalities, MetricComputations; questionTypes: FindAll, Prove.
Piemēri: LV.NOL.2024.7.3 (AC garuma iespējamās vērtības četru punktu konfigurācijā), LV.NOL.2022.8.3 (pierādīt 3AC > AB vienādsānu trijstūrī).

### 8. temats. Taisnes, koordinātas un laukumi

Tieša sasaiste ar 8. klases standartkursa lineāro funkciju — parāda, kā skolas viela kļūst par olimpiādes instrumentu; 7. klases skolēniem lineārās funkcijas pamatus dod nodarbības A bloka paraugpiemērs.

* a. SR: Atrod taišņu krustpunktus un attēlo uzdevuma konfigurāciju koordinātu plaknē.
* b. SR: Aprēķina daudzstūra laukumu koordinātu plaknē, sadalot figūru taisnstūros un trijstūros vai izmantojot aptverošo taisnstūri.
* c. SR: Lieto laukumu attiecības caur kopīgu pamatu vai augstumu un pazīst vienlielas (bet ne vienādas) figūras.

Birkas: LinearFunctionGraphAnalysis, AreaRatiosFromCommonHeight, AreaPreservingTransformation; topics: Area; models: GeometricFormulaApplication.
Piemēri: LV.NOL.2022.7.1 (četrstūra laukums starp taisnēm), LV.AMO.2022A.8.1 (trijstūris starp taišņu krustpunktiem un asīm).

### 9. temats. Loģikas uzdevumi: patiesie un meļi

Jauns temats — loģiska gadījumu analīze, kas trenē to pašu pamatojuma disciplīnu bez tehniskām priekšzināšanām (labi noder arī nodarbībām ar jauktu sastāvu).

* a. SR: Veic gadījumu analīzi pēc pieņēmuma ("pieņemsim, ka X saka patiesību...") un katru zaru noved vai nu līdz pretrunai, vai konsekventam scenārijam.
* b. SR: Pamato, ka atrasti visi iespējamie scenāriji, t. i., apvieno gadījumu analīzi ar pilnās pārlases pierakstu.
* c. SR: Sistematizē informāciju tabulā un pazīst pašreferences apgalvojumu ("es esmu melis") īpatnības.

Birkas: TruthTellersAndLiarsModel, LogicalCaseAnalysisFromAssumptions; MTH_ContradictionMethod; topics: LogicProblems.
Piemēri: LV.AMO.2022B.7.5 (272 ciema iedzīvotāji), LV.AMO.2022B.8.5 (piecu draugu strīds), LV.AMO.2023.7.5 un 8.5 (bizbizmārītes ar punktiem).

### 10. temats. Vienādojumi veselos skaitļos un skaitļu konstrukcijas

Pērn šī viela bija tikai pirmsolimpiādes atkārtojumā; šogad — pilnvērtīgs temats, kas apvieno algebriskos pārveidojumus ar skaitļu teoriju.

* a. SR: Risina vienādojumus veselos skaitļos, sadalot reizinātājos un veicot sakārtotu dalītāju pārlasi (ievērojot arī negatīvos dalītājus un simetriju).
* b. SR: Ierobežo atrisinājumu meklēšanas apgabalu ar novērtējumiem (augšanas ātruma salīdzināšana, atlikumu analīze) un tikai tad pārlasa atlikušos gadījumus.
* c. SR: Konstruē skaitļus ar prasītām ciparu un dalāmības īpašībām un pamato konstrukcijas optimalitāti vai vienīgumu.

Birkas: topics: IntegerEquations (DOM_IntegerEquations), DigitManipulation; MTH_Transformations, MTH_ExhaustiveAlgorithms; questionTypes: FindAll, FindOptimal.
Piemēri: LV.NOL.2019.7.4 (vai ab(a+5b)=150015 atrisināms veselos skaitļos), LV.AMO.2022B.8.2 (punktu bilance ar 20 uzdevumiem), LV.AMO.2023.8.2 (trīsciparu skaitlis ar ciparu nosacījumiem).

---

## Caurviju sasniedzamie rezultāti (mēra visu gadu)

Šie SR neattiecas uz vienu tematu, bet tiek trenēti un vērtēti katrā nodarbībā, testiņos un mock-olimpiādēs:

* a. SR: Patstāvīgi izvēlas risināšanas fāzes (noskaidro doto un prasīto → mazie gadījumi / zīmējums → metodes izvēle → pieraksts → pārbaude) un spēj nosaukt, kurā fāzē "iestrēdzis".
* b. SR: Uzraksta pamatojumu, kas atbilst jautājuma tipam un ko var novērtēt ar olimpiādes kritērijiem (piemērs bez novērtējuma vai novērtējums bez piemēra dod tikai daļu punktu).
* c. SR: Izstāsta savu risinājumu citiem un atrod nepilnības (izlaistus gadījumus, nepamatotus soļus) gan savā, gan cita risinājumā.
* d. SR: Olimpiādē racionāli sadala laiku starp 5 uzdevumiem — sāk ar pieejamākajiem, fiksē daļējus rezultātus rakstiski.

---

*Piezīme par lietošanu: katram tematam pirms nodarbībām sagatavo 6 vienību komplektu (temata karte ar šeit dotajām birkām un uzdevumu ID; 2–3 anotēti paraugpiemēri; 8–12 uzdevumu kāpnes ar uzvednēm; 1 lapas atgādne; atsaukšanas jautājumu banka; sprinta mājas komplekts). Norādītie uzdevumu ID ir kāpņu izejmateriāls — tos papildina ar tā paša tipa uzdevumiem no citiem gadiem un citu klašu (5.–6. kl. iesildei, 9. kl. izaicinājumam) komplektiem.*
