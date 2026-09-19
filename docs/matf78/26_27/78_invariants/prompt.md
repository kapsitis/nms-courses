# Uzdevumu atlasīšanas uzvedne/prompts

**Ievads:** 
Jūsu uzdevums ir atlasīt piemērotākos uzdevumus tematam, 
`78_invariants` - tas ir 7. un 8.klasei domāts temats, kurā stāsta 
par invariantiem. 
Sk. `nms-courses\docs\matf78\26_27\78_invariants\index.md` - šī 
temata tvērumu, motivāciju un sasniedzamos rezultātus. 
Temats ir daļa no apmācību kursa 
`nms-courses\docs\matf78\26_27\curriculum_7_8.md`

**Kas jāizdara:** 

Veiciet šādas izmaiņas direktorijā `nms-courses\docs\matf78\26_27\78_invariants`:

1. Izveidojiet tajā jaunu failu `problems.rq` ar SPARQL vaicājumu, kas izveido 
   garo sarakstu ar tiem uzdevumiem, kuri (pēc formulējuma vai kāda no atrisinājumiem)
   varētu atbilst tematam. 
   Sal. `nms-courses\docs\matf910\26_27\910STRUCT_solution_structure\problems.rq`, kas ir piemērs par 
   citu tematu. Vai `nms-courses\docs\matf78\26_27\78STRUCT_solution_structure\problems.rq`

2. Aizpildiet **TODO** sadaļas failā `nms-courses\docs\matf78\26_27\78_invariants\index.md`: 

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
[LV.AMO.2022A.7.2](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2022A.7.2) un [LV.AMO.2022A.8.2](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2022A.8.2)
(gabalu skaita paritāte procesā), 
[LV.AMO.2024.7.3](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2024.7.3) 
(virkne ar ×2, ×3, :2, :3), 
[LV.NOL.2023.7.5](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2023.7.5)
(lodīšu krāsu maiņa — atlikuma invariants).





