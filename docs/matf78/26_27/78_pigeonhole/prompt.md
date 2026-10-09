# Uzdevumu atlasīšanas uzvedne/prompts

**Ievads:** 
Jūsu uzdevums ir atlasīt piemērotākos uzdevumus tematam, 
`78_pigeonhole` - tas ir 7. un 8.klasei domāts temats par Dirihlē principu. 
Sk. `nms-courses\docs\matf78\26_27\78_pigeonhole\index.md` - šī 
temata tvērumu, motivāciju un sasniedzamos rezultātus. 
Temats ir daļa no apmācību kursa 
`nms-courses\docs\matf78\26_27\curriculum_7_8.md`

**Kas jāizdara:** 

Veiciet šādas izmaiņas direktorijā `nms-courses\docs\matf78\26_27\78_pigeonhole`:

1. Izveidojiet tajā jaunu failu `problems.rq` ar SPARQL vaicājumu, kas izveido 
   garo sarakstu ar tiem uzdevumiem, kuri (pēc formulējuma vai kāda no atrisinājumiem)
   varētu atbilst tematam. Dažreiz labāk meklēt uzdevumus pēc a
   Varat apskatīt `problems.rq` 
   Sal. `nms-courses\docs\matf910\26_27\910STRUCT_solution_structure\problems.rq`, kas ir piemērs par 
   citu tematu. Vai `nms-courses\docs\matf78\26_27\78STRUCT_solution_structure\problems.rq`
   Vaicājumus var izpildīt lokālajā Oxigraph krātuvē (`$env:OXIGRAPH_DB_PATH`). 
   Tajā  ielādēti uzdevumi no `./math/problembase` apakšdirektorijām - `LV.AMO`, 
   `LV.NOL`, `LV.VOL`.

2. Aizpildiet **TODO** sadaļas failā `nms-courses\docs\matf78\26_27\78_invariants\README.md`: 

  * Zem H2 virsraksta "Tvērums" (scope) ierakstīt dažus teikumus, kuri ieskicē to Dirihlē 
    principa temata izklāsta plašumu, kas ir optimāls mācīšanai 7. un 8.klasē.
    Piemēram, vai uz šo tematu attiecas arī uzdevumi, kuros pamato to, ka attēlojums starp 
    divām vienāda izmēra kopām ir bijekcija? (Ja attēlojums/mapping nebūtu bijekcija un dažiem elementiem nebūtu 
    inversā, tad neizbēgami rastos kolīzijas - bet tās dotajā situācijā nav iespējamas.)
    Ja šādi spriedumi nemēdz būt 7.-8.klases uzdevumos, tad šādu Dirihlē lietojumu paredzam tvērumā, 
    ja nē - atliekam uz vecākām klasēm.
  * Zem H2 virsraksta "SPARQL vaicājums" kā koda bloks; zem tā paskaidrojumi, kāpēc tieši tā atlasīts.
  * Zem H2 virsraksta "Atlasītie uzdevumu ID" ievietot uzdevumu ID kā sarakstu pa vienam ID katrā rindiņā; 
    tas var būt "garais saraksts" - visi uzdevumi par tematu. 


3. Aizpildiet **TODO** sadaļas failā `nms-courses\docs\matf78\26_27\78_invariants\index.md`: 

  * Zem H2 virsraksta "1.nodarbības saturs" - aprakstīt 1.nodarbības saturu 1 rindkopā un tai specifiskos sasniedzamos rezultātus. 
    Atlasīt trīs klasē skatāmos uzdevumus - katram pievienot dažus ieteikumus/analīzes soļus. 
  * Zem H2 virsraksta "2.nodarbības saturs" - aprakstīt 2.nodarbības saturu 1 rindkopā un tai specifiskos sasniedzamos rezultātus. 
    Atlasīt trīs klasē skaidrojamos piemērus  - katram pievienot dažus ieteikumus/analīzes soļus. 

4. Izveidojiet jaunu failu `problems.md` - atlasītas divas uzdevumu "trepes" 
   (pa 8 uzdevumiem katrā) - katrai no abām nodarbībām sava. 
   Katrā no trepēm ir divām nodarbībām pa 8 uzdevumiem (pirmie divi ir iesildīšanās; 
   tad 4 uzdevumi - standarts veids, kā pielietot tematu; visbeidzot 2 uzdevumi, 
   kuros bez temata ir arī citu tematu metodes un zināšanas būtiski izmantotas.

5. Izveidojiet arī failus `class1.md` un `class2.md` (līdzīgi citiem class1.md un class2.md failiem zem 
   `.\nms-courses\docs` apakšdirektorijām ar analoģiski aizpildītu "front-matter"). 
   Failā `class1.md` ierakstīt īsu teorijas atgādni + skaidrojamos piemērus (līdzīgi kā `index.md`, bet īsāk - 
   jo šīs lapas `classN.md` iecerētas kā drukāts izdales materiāls). Teorijas+uzdevumu
   atgādne uzsver tikai svarīgāko. Arī skaidrojamie piemēri pasniedzami īsāk, atstājot no 4-5 
   ieteikumiem/hints tikai 1-2 svarīgākos - var būt no jebkurām risināšanas fāzēm (no
   "saprašanas" līdz "atskatam" pēc Jūsu ieskatiem).
   Aiz teorijas atgādnes un skaidrojamiem piemēriem ievietot 
   horizontālu svītru ("---") un aiz tās piemeklēt vēl 2-3 uzdevumus. 
   Tos var ņemt no SPARQL atlasītajiem uzdevumiem (sk. `README.md`), ja tie nav jau salikti `problems.md`
   vai varat piedāvāt kādu citu sev zināmu uzdevumu, kāda Latvijas olimpiādēs nav (tad nepieciešama atsauce uz avotu). 

## Pieejamie resursi

### Tematam specifiskie resursi

Var izmantot piemērus, uzdevumus un materiālus no `./nms-courses/avg-pulcins-2025/class03-pigeonhole/" - 
class03-pigeonhole.rst un apakšdirektorijām ar zīmējumiem u.c.


### Latvijas olimpiāžu uzdevumi

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


