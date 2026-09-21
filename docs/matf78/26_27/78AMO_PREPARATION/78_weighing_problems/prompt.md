# Uzdevumu atlasīšanas uzvedne/prompts

**Ievads:** 
Jūsu uzdevums ir atlasīt piemērotākos uzdevumus tematam, 
`78_weighing_problems` - tas ir 7. un 8.klasei domāts temats, kurā stāsta 
par svēršanas uzdevumiem. 

Temats ir radniecīgs A-gada 9.tematam  - sk. 
`nms-courses\docs\matf78\26_27\curriculum_7_8.md` 


**Kas jāizdara:** 

Veiciet šādas izmaiņas direktorijā `nms-courses\docs\matf78\26_27\78AMO_PREPARATION/78_weighing_problems/`:

1. Izveidojiet tajā jaunu failu `problems.rq` ar SPARQL vaicājumu, kas izveido 
   garo sarakstu ar tiem uzdevumiem, kuri (pēc formulējuma vai kāda no atrisinājumiem)
   varētu atbilst tematam. 
   Sal. `nms-courses\docs\matf910\26_27\910_solution_structure\problems.rq`, kas ir piemērs par 
   citu tematu. Vai `nms-courses\docs\matf78\26_27\78_solution_structure\problems.rq` vai 
   `nms-courses\docs\matf78\26_27\78_invariants\problems.rq` utt. 

2. Aizpildiet **TODO** sadaļas failā `nms-courses\docs\matf78\26_27\78AMO_PREPARATION/78_weighing_problems/index.md`: 

  * Zem H3 virsraksta "SPARQL vaicājums" kā koda bloks; zem tā paskaidrojumi, kāpēc tieši tā atlasīts.
  * Zm H3 virsraksta "Atlasītie uzdevumu ID" ievietot uzdevumu ID kā sarakstu pa vienam ID katrā rindiņā; tas var būt "garais saraksts" - visi uzdevumi par invariantiem. 
  * Zem H3 virsraksta "1.nodarbības saturs" - aprakstīt 1.nodarbības saturu 1 rindkopā un tai specifiskos sasniedzamos rezultātus. (Un atlasīt 2-3 klasē skatāmos uzdevumus - katram pievienot 
  dažus ieteikumus/analīzes soļus). 
  * Zem H3 virsraksta "2.nodarbības saturs" - aprakstīt 2.nodarbības saturu 1 rindkopā un tai specifiskos sasniedzamos rezultātus. (Un atlasīt 2-3 klasē skatāmos uzdevumus  - katram pievienot 
  dažus ieteikumus/analīzes soļus). 

3. Izveidojiet jaunu failu `problems.md` - atlasītas divas uzdevumu "trepes" 
   (pa 8 uzdevumiem katrā) - katrai no abām nodarbībām sava. 
   Katrā no trepēm ir divām nodarbībām pa 8 uzdevumiem (pirmie divi ir iesildīšannās; 
   tad 4 uzdevumi - standarts veids, kā pielietot tematu; visbeidzot 2 uzdevumi, 
   kuros bez temata ir arī citu tematu metodes un zināšanas būtiski izmantotas.)

```
# 7.3. temats: Temata nosaukums

## 1. daļa: Temata nosaukums. Apakšvirsraksts

| Kāpnes | Uzdevumi |
|---|---|
| Iesildīšanās | LV.AMO.2015.6.2 (šaha krāsojums un domino), LV.NOL.2015.7.3 (krāsojums palīdz uzbūvēt piemēru) |
| Viennozīmīga metode | LV.AMO.2015.7.2 (melno rūtiņu skaita paritāte), LV.AMO.2015.8.2 (tas pats solis lielākā taisnstūrī), LV.AMO.2016.7.5 (varde maina krāsu katrā lēcienā), LV.AMO.2016.8.5 (uzvarošo/zaudējošo rūtiņu krāsojums) |
| Neviennozīmīga metode | LV.AMO.2022A.7.3 (novērtējums + konstrukcija), LV.NOL.2013.8.5 (monovariants un piemērs) |



* *Izpēte*: Cik melnas un cik baltas rūtiņas noklāj **viens** domino kauliņš?
Cik melnas rūtiņas ir vienā izgrieztajā $3 \times 5$ taisnstūrī?


```


## Pieejamie resursi


**Kā ātri atrast uzdevumus par doto tematu (text search):**

Var meklēt pēc atslēgvārdiem šajās uzdevumu direktorijās 

* `./math/problembase/LV.AMO/`
* `./math/problembase/LV.NOL/`
* `./math/problembase/LV.VOL/`
* `./math/problembase/LV.SOL/`

Uzdevumu failus parasti sauc `content_lv.md` - tie atrodami apakšdirektorijās atbilstoši 
gadiem. Katra uzdevuma ID norāda klasi - piemēram, `LV.AMO.2024.8.5` ir 2024.g. atklātās 
olimpiādes komplekta 8.klases 5.uzdevums.

**Kā ātri atrast uzdevumus par doto tematu (metainformācija):**
Jums var noderēt `./nms-courses/scripts/select_problems.py` - skripts, 
ar kuru var darbināt SPARQL. 
**Birkas (topic, method) meklēšanai ar SPARQL:** ParityInvariant, ColoringInvariant, ModularInvariant, MonovariantArgument, TilingByDominoesAndColoring; MTH_FixedInvariant, MTH_AuxiliaryColoring.

**Daži uzdevumu piemēri:**

Šie ir "pozitīvie piemēri" par svēršanu - uzdevumi, kuri labi piemēroti 7.-8.klasēm.
```
1. Dotas 20 pēc ārējā izskata vienādas monētas, bet visas to masas ir dažādas. Kā, izmantojot sviras svarus bez
atsvariem, ar 28 svēršanām atrast gan pašu vieglāko, gan pašu smagāko monētu?
2. Dotas 9 pēc ārējā izskata vienādas monētas, no kurām viena ir viltota – tā ir vieglāka nekā citas. Kā ar divām
svēršanām uz sviras svariem bez atsvariem atrast viltoto monētu, ja zināms, ka visu īsto monētu masas ir
vienādas?
3. Zināms, ka no 80 monētām viena ir viltota – tā ir vieglāka nekā pārējās, kurām visām ir vienāda masa. Kā ar
četrām svēršanām uz sviras svariem bez atsvariem atrast viltoto monētu?
4. Dotas 25 pēc ārējā izskata vienādas monētas. Zināms, ka 24 monētu masas ir vienādas savā starpā, bet vienas
monētas masa ir citāda. Kā ar divām svēršanām uz sviras svariem bez atsvariem noskaidrot, vai atšķirīgā
monēta ir vieglāka vai smagāka nekā pārējās? (Pašu monētu atrast nav nepieciešams.)
5. Grozā ir 16 akmeņi – 15 parasti, 1 radioaktīvs. Tie visi izskatās vienādi. Ir dota ierīce, ar kuras palīdzību var
noteikt, vai starp apskatāmajiem akmeņiem ir vai nav radioaktīvais akmens (ar ierīci var pārbaudīt arī vairākus
akmeņus reizē, bet ierīce nenorāda, kurš tieši ir radioaktīvais akmens). Kā ar 4 pārbaudēm atrast radioaktīvo
akmeni?
6. No 7 monētām vienai monētai masa ir mazāka nekā pārējām. Kā ar divām svēršanām noskaidrot, kura ir
vieglākā monēta?
7. Dotas 13 pēc ārējā izskata vienādas monētas. No tām 12 monētas ir ar vienādu masu, bet viena – ar atšķirīgu.
Doti arī sviras svari bez atsvariem. Kā, izmantojot 2 svēršanas, noskaidrot, vai atšķirīgā monēta ir vieglāka vai
smagāka nekā pārējās? (Pašu monētu atrast nav nepieciešams.)
```


Šie piemēri jāuztver nedaudz kritiskāk - ja to atrisināšanai ir pietiekami ar 
7.-8.klašu zināšanām - arī tos var izvēlēties (arī tad, ja olimpiādes uzdevums
bija 9.-12.klašu komplektā). 
Tomēr, var izrādīties, ka tajos ir kādas sarežģītākas tēmas (izpratne par 
lēmumu kokiem/decision trees, logaritmiem utml.) - un tad šādi uzdevumi (ja sākotnējais 
SPARQL tos atlasa) tomēr ir no rezultātu kopas jāizņem.

```
Tālāk dotie piemēri vairāk paredzēti 9.-12. klases skolēniem, bet tos var izmantot arī jaunāku klašu skolēni.
8. Doti 16 akmeņi ar dažādām masām. Pierādiet, ka ar 18 svēršanām uz sviru svariem bez atsvariem var atrast
pašu smagāko un otru smagāko akmeni!
9. Dotas 5 pēc ārējā izskata vienādas bumbas, kuru masas ir 1000 g, 1001 g, 1002 g, 1004 g un 1007 g. Doti arī
elektroniskie svari, kas rāda masu gramos. Kā ar trīs svēršanām atrast bumbu, kuras masa ir 1000 g?
10. Dotas 4 pēc ārējā izskata vienādas monētas, kuru masas ir 1 g, 2 g, 3 g un 4 g. Kā ar četrām svēršanām uz
sviras svariem bez atsvariem noskaidrot katras monētas masu?
11. Četru pēc ārējā izskata vienādu monētu masas veido ģeometrisko progresiju, kas nav konstanta. Atrast
smagāko monētu, veicot divas svēršanas uz sviru svariem bez atsvariem!
```