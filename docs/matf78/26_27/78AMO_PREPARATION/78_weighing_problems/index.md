---
layout: default
title: "7.AMO.temats. Svēršanas uzdevumi"
permalink: /matf78/26_27/78AMO_PREPARATION/78_weighing_problems/
---
# 7.AMO.temats. Svēršanas uzdevumi

Lēmumu koki un procedūru apraksti. Temats atbilst
`curriculum_7_8.md` 9. tematam *"Svēršanas un algoritmi: Kā uzzināt vairāk ar
mazāk jautājumiem"*. *Standarta līnijas: K6, M2.*

* **Uzdevumu lapa:** {% include doc_links.html url="/matf78/26_27/78AMO_PREPARATION/78_weighing_problems/problems/" %}
* **1.nodarbības materiāls:** {% include doc_links.html url="/matf78/26_27/78AMO_PREPARATION/78_weighing_problems/class1/" %}
* **2.nodarbības materiāls:** {% include doc_links.html url="/matf78/26_27/78AMO_PREPARATION/78_weighing_problems/class2/" %}
{: .small}

* SR: Apraksta svēršanas vai minēšanas procedūru pa soļiem, ietverot visus
  iespējamos iznākumus (lēmumu koks), nevis tikai "veiksmīgo" scenāriju.
* SR: Novērtē, cik informācijas dod viens jautājums vai svēršana (divi vai trīs
  iznākumi), un pamato, kāpēc ar mazāku darbību skaitu nepietiek.
* SR: Plāno darbību secību pēc sliktākā gadījuma analīzes un pieraksta
  algoritmu tā, lai to var izpildīt cits cilvēks.


## SPARQL vaicājums

Vaicājums pilnā apjomā (ar komentāriem) glabājas failā `problems.rq`;
zemāk - tā būtiskā daļa.

```sparql
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

SELECT ?problemID ?grade ?family ?diff
       (GROUP_CONCAT(DISTINCT ?domain;       separator="/") AS ?domains)
       (GROUP_CONCAT(DISTINCT ?questionType; separator="/") AS ?questionTypes)
WHERE {
  ?p a eliozo:Problem ;
     eliozo:problemID ?problemID ;
     eliozo:problemGrade ?grade ;
     eliozo:problemYear ?year ;
     eliozo:problemText ?text .
  OPTIONAL { ?p eliozo:domain ?domain }
  OPTIONAL { ?p eliozo:questionType ?questionType }
  OPTIONAL { ?p eliozo:_readingDifficulty ?diff }

  {
    # ---- (A) teksta zars: svēršanas uzdevumi ----------------------------
    ?p eliozo:problemText ?text .
    FILTER (CONTAINS(?text, "svēršan") || CONTAINS(?text, "sviras svar")
            || CONTAINS(?text, "sviru svar")
            || (CONTAINS(?text, "atsvar") && !CONTAINS(?text, "īpatsvar")))
    BIND (
      IF (CONTAINS(?text, "viltot") || CONTAINS(?text, "atšķirīg"), "Counterfeit",
      IF (CONTAINS(?text, "vieglāko") || CONTAINS(?text, "smagāko")
          || CONTAINS(?text, "visvieglāk") || CONTAINS(?text, "vissmagāk")
          || CONTAINS(?text, "sarindot"), "Extremes",
                                          "Weights")) AS ?family )
  }
  UNION
  {
    # ---- (B) birku zars: informācija bez svariem -------------------------
    ?p eliozo:problemText ?text .
    { ?p eliozo:_hasSolutionConcept "DecisionTree" }
    UNION
    { ?p eliozo:topic ?topicIRI .
      FILTER (CONTAINS(STR(?topicIRI), "SearchProblems")
              || CONTAINS(STR(?topicIRI), "ProblemsWithHiddenInformation")) }
    FILTER (!CONTAINS(?text, "svēršan") && !CONTAINS(?text, "sviras svar")
            && !CONTAINS(?text, "sviru svar"))
    FILTER (CONTAINS(?text, "jautājum") || CONTAINS(?text, "pārbaud")
            || CONTAINS(?text, "uzminēt") || CONTAINS(?text, "noskaidrot")
            || CONTAINS(?text, "ierīc"))
    BIND ("Questions" AS ?family)
  }

  FILTER (LANG(?text) = "" || LANGMATCHES(LANG(?text), "lv"))
  FILTER (?grade >= 5 && ?grade <= 12)
  FILTER (?year >= 2003 && ?year <= 2026)
}
GROUP BY ?problemID ?grade ?family ?diff
ORDER BY ?family ?grade ?problemID
```

**Kāpēc tieši tā atlasīts.**

* **Birku slānis šim tematam praktiski neeksistē.** Visā krātuvē nav nevienas
  birkas, kuras nosaukumā būtu "Weigh", "Balance", "Coin" vai "Scale".
  Vistuvākās ir jēdziens `DecisionTree` (30 uzdevumi), tēmas `SearchProblems`
  un `ProblemsWithHiddenInformation` (kopā 3 uzdevumi) un apakšdomēns
  `DOM_CombinatorialAlgorithms` (14 uzdevumi). Ar tām vien pietrūktu: temata
  kodola sērija - `LV.NOL.2019.7.2`, `LV.NOL.2019.8.2`, `LV.SOL.2020.9.3`,
  `LV.NOL.2016.7.4` - nav apbirkota nemaz. Tāpēc **galvenais ir teksta zars**,
  un birkas dod tikai papildinājumu.
* **Šis žanrs ir ļoti stabili formulēts.** Latviešu olimpiāžu tekstos gandrīz
  vienmēr parādās "svēršanām", "sviras svari bez atsvariem" vai "sviru svari".
  Tāpēc četri atslēgvārdi (`svēršan`, `sviras svar`, `sviru svar`, `atsvar`)
  noķer visu sēriju no 2003. līdz 2026. gadam. Precizitāte ir neparasti augsta:
  no $51$ atrastā uzdevuma tikai divi ir apšaubāmi (`LV.NOL.2026.12.4` -
  spēle ar atsvariem, `LV.NOL.2009.8.4` - līdzsvara identitāte, drīzāk algebra).
* **Viena viltus sakritība, ko izslēdzam atsevišķi:** vārds "**īp**atsvars"
  satur "atsvar" un ievelk `LV.NOL.2017.6.5` (par liepu un ozolu īpatsvaru
  parkā). To izmet `!CONTAINS(?text, "īpatsvar")`.
* **`?family` sadala pēc tā, *kas* jānoskaidro** - un tas sakrīt ar abu
  nodarbību dalījumu: `Counterfeit` (atrast viltoto vai pateikt, vai tā ir
  vieglāka/smagāka) ir $1.$ nodarbība; `Extremes` (vieglākais, smagākais,
  sarindošana) un `Questions` (informācija bez svariem) - $2.$ nodarbība;
  `Weights` (atsvari ar zināmām masām) der abām.
* **Otrais zars ievelk radniecīgos "informācijas" uzdevumus bez svariem** -
  mēģenes ar reaģentiem, minēšana ar jautājumiem, pārbaudes ierīce. Bez
  papildu teksta filtra (`jautājum`/`pārbaud`/`uzminēt`/`noskaidrot`/`ierīc`)
  `DecisionTree` birka ievelk arī lodīšu maiņas un skaitļu dzēšanas
  invariantu uzdevumus, kas šim tematam neder.
* **Attēlus NEIZSLĒDZAM.** Citos tematos noderīgais filtrs `!CONTAINS(?text,
  "![")` šeit tikai kaitētu: zīmējums gandrīz vienmēr ir sviras svaru
  ilustrācija (`LV.NOL.2025.6.5`), nevis uzdevuma nesējs.
* **Klases 5.-12.** Uzdevuma klase šeit gandrīz neko nenozīmē: tā pati
  $7$ monētu konstrukcija ir $5.$ klases komplektā (`LV.AMO.2003.5.2`), bet
  $25$ monētu variants - $9.$ klasē (`LV.SOL.2020.9.3`). Tāpēc ņemam plašu
  diapazonu un šķirojam ar roku.
* **Noderīgs blakusatradums:** šim tematam datubāzē ir savs `questionType`
  vērtība `Algorithm` ($9$ no atlasītajiem uzdevumiem). Tas ir vājāks signāls
  nekā teksts, bet der kā pārbaude.

Vaicājums atgriež **51 kandidātu**.

**Ko no garā saraksta apzināti neņēmām nodarbībās.** Prompta "pozitīvo
piemēru" sarakstā ir arī klasiskie $9$ monētu ($2$ svēršanas), $80$ monētu
($4$ svēršanas), $7$ monētu un $16$ radioaktīvo akmeņu uzdevumi. **Latvijas
olimpiāžu datubāzē to nav** - tie ir mācību grāmatu klasika, nevis olimpiāžu
uzdevumi. To vietā tīro $3^k$ ideju nes `LV.NOL.2019.8.2` ($26$ monētas, $3$
svēršanas), bet "radioaktīvā akmens" ideju - `LV.NOL.2022.6.5` ($64$ mēģenes,
$6$ pārbaudes). Ja šos klasiskos uzdevumus vajag nodarbībā, tie jāpievieno ar
roku no cita avota.

### Atlasītie uzdevumu ID

Garais saraksts, sagrupēts pēc `?family` (51 uzdevums).

**Counterfeit** - atrast viltoto/atšķirīgo priekšmetu vai noteikt tā virzienu

* LV.AMO.2003.5.2
* LV.AMO.2005.5.2
* LV.AMO.2006.5.2
* LV.AMO.2015.5.5
* LV.VOL.2026.5.4
* LV.NOL.2019.6.2
* LV.NOL.2015.7.5
* LV.NOL.2016.7.4
* LV.NOL.2019.7.2
* LV.NOL.2019.8.2
* LV.SOL.2020.9.3
* LV.VOL.2011.9.4
* LV.VOL.2025.9.4
* LV.NOL.2006.10.5
* LV.NOL.2007.10.1
* LV.VOL.2004.10.5
* LV.VOL.2025.11.1
* LV.AMO.2006.12.4
* LV.AMO.2016.12.5

**Extremes** - vieglākais, smagākais, sarindošana

* LV.NOL.2019.5.2
* LV.NOL.2016.6.4
* LV.AMO.2015.7.5
* LV.AMO.2017.8.4
* LV.NOL.2019.9.2
* LV.AMO.2017.11.4
* LV.NOL.2026.12.4

**Weights** - atsvari ar zināmām masām, līdzsvars, bilance

* LV.AMO.2007.5.4
* LV.NOL.2025.5.5
* LV.AMO.2003.6.5
* LV.AMO.2005.6.3
* LV.AMO.2006.6.2
* LV.NOL.2009.6.5
* LV.NOL.2025.6.5
* LV.NOL.2005.7.5
* LV.NOL.2006.7.2
* LV.NOL.2009.8.4
* LV.NOL.2020.8.5
* LV.VOL.2023.9.2
* LV.NOL.2019.10.2
* LV.VOL.2020.10.5
* LV.VOL.2023.10.2
* LV.AMO.2008.11.5
* LV.NOL.2012.11.5
* LV.NOL.2013.11.3

**Questions** - informācija bez svariem: jautājumi, testi, ierīces

* LV.AMO.2008.6.5
* LV.NOL.2012.6.5
* LV.NOL.2022.6.5
* LV.NOL.2007.7.5
* LV.AMO.2013.8.5
* LV.NOL.2005.8.3
* LV.AMO.2016.9.5


## 1.nodarbības saturs

Pirmā nodarbība ir par **procedūras uzbūvi**: kā atrast atšķirīgo priekšmetu
un - galvenais - kā to pierakstīt tā, lai der **visos** gadījumos. Sākam ar
novērojumu, ka sviras svariem ir *trīs* iznākumi, nevis divi: kreisais
smagāks, labais smagāks, līdzsvars. Tāpēc dabiskais gājiens ir dalīt priekšmetus
**trijās** daļās, nevis uz pusēm, un pēc katras svēršanas viena daļa paliek kā
"aizdomās turamā". No tā uzreiz izriet skaitļi $3, 9, 27$, un $26$ monētu
uzdevums kļūst caurskatāms. Otrā nodarbības puse ir veltīta biežākajai kļūdai:
skolēns apraksta tikai to zaru, kurā svari nosveras uz vienu pusi, un aizmirst
pateikt, ko darīt līdzsvara gadījumā. Tāpēc katru risinājumu pierakstām kā
**lēmumu koku** - katrai svēršanai visi trīs zari, katram zaram nākamais solis.
Pa ceļam parādās otra svarīga doma: dažreiz uzdevums prasa **mazāk**, nekā
šķiet ("noskaidrot, vai atšķirīgā monēta ir vieglāka vai smagāka, pašu monētu
atrast nav nepieciešams"), un tieši tāpēc pietiek ar divām svēršanām tur, kur
monētas atrašanai vajadzētu trīs.

*Aptuvenais 90 minūšu plāns:* $10$ min - sviras svaru trīs iznākumi un
dalīšana trijās daļās; $20$ min - $1.1$ piemērs pie tāfeles ar pilnu lēmumu
koku; $15$ min - iesildīšanās uzdevumi patstāvīgi; $20$ min - $1.2$ piemērs
(vājākais jautājums); $15$ min - $1.3$ piemērs; $10$ min - kopsavilkums un
mājasdarba trepes izskaidrošana.

Šai nodarbībai specifiski sasniedzamie rezultāti:

* SR: Pamato, ka viena svēršana dod **trīs** iznākumus, un izvēlas dalījumu
  trijās (nevis divās) daļās; nosauc, cik priekšmetu paliek katrā zarā.
* SR: Pieraksta risinājumu kā lēmumu koku: katrai svēršanai apraksta **visus
  trīs** iznākumus un katram - nākamo soli, nevis tikai "veiksmīgo" zaru.
* SR: Pārliecinās, ka procedūra strādā arī sliktākajā gadījumā, un pārbauda to
  uz zara ar vislielāko palikušo priekšmetu skaitu.
* SR: Izšķir uzdevumus "atrast priekšmetu" un "noskaidrot tikai virzienu
  (vieglāks/smagāks)" un paskaidro, kāpēc otrajam pietiek ar mazāk svēršanām.

### Skaidrojamie piemēri

#### 1.1. LV.NOL.2019.8.2 - kāpēc tieši trijās daļās

Zināms, ka no $26$ monētām viena ir viltota - tā ir vieglāka nekā pārējās,
kurām visām ir vienāda masa. Kā ar trīs svēršanām uz sviras svariem bez
atsvariem atrast viltoto monētu?

* *Saprašana:* Atbilde ir **procedūra**, nevis skaitlis. To var uzskatīt par
  pabeigtu tikai tad, ja cits cilvēks to var izpildīt, nekā vairāk nezinot.
* *Izpēte:* Cik dažādus iznākumus dod viena svēršana? Trīs. Cik dažādas
  atbildes ir jāatšķir? $26$. Kāda ir mazākā $k$ vērtība, ar kuru $3^k \geq 26$?
* *Pārformulēšana:* Katrai svēršanai jāsadala aizdomās turamās monētas trijās
  pēc iespējas vienādās daļās; divas no tām liek uz kausiem, trešā paliek malā.
* *Risināšana:* $26 = 9+9+8$. Sveram $9$ pret $9$. Ja viens kauss vieglāks -
  viltotā ir tur ($9$ monētas); ja līdzsvars - viltotā ir malā atstātajā
  kaudzītē ($8$ monētas). Tālāk tāpat: $9 = 3+3+3$, tad $3 = 1+1+1$. Trīs
  svēršanas. (*Piezīme:* $8$ monētu gadījumu var nepētīt atsevišķi - pievieno
  tai vienu jau zināmu īsto monētu.)
* *Atskats:* Cik monētas šī procedūra izturētu ar trim svēršanām? Ar četrām?
  Kur spriedumā tika izmantots tas, ka viltotā ir **vieglāka**, nevis vienkārši
  citāda?

#### 1.2. LV.NOL.2016.7.4 - vājāks jautājums maksā mazāk

Dotas $13$ pēc ārējā izskata vienādas monētas. No tām $12$ monētas ir ar
vienādu masu, bet viena - ar atšķirīgu. Kā ar divām svēršanām noskaidrot, vai
atšķirīgā monēta ir vieglāka vai smagāka par pārējām? Pašu monētu atrast nav
nepieciešams.

* *Saprašana:* Salīdzini ar $1.1$: tur bija zināms virziens un jāatrod monēta,
  šeit - otrādi. Cik dažādas atbildes tagad jāatšķir? Tikai **divas**.
* *Izpēte:* Ar divām svēršanām var atšķirt līdz $9$ gadījumiem. Atrast monētu
  starp $13$ nevarētu - bet atbildēt uz jautājumu "vieglāka vai smagāka" var.
* *Risināšana:* Liekam $6$ pret $6$.
  * Līdzsvars - atšķirīgā ir tā, kas nebija uz svariem. Otrā svēršana: salīdzini
    to ar jebkuru nosvērto monētu, un virziens ir redzams.
  * Nav līdzsvara - pieņemsim, ka kreisais kauss vieglāks. Otrā svēršana:
    ņemam **kreisā kausa** $6$ monētas un liekam $3$ pret $3$. Ja līdzsvars -
    visas sešas ir vienādas, tātad atšķirīgā bija labajā kausā un ir
    **smagāka**. Ja nav līdzsvara - atšķirīgā ir kreisajā sešiniekā un ir
    **vieglāka**.
* *Atskats:* Kur risinājumā izmantots, ka monētu skaits ir tieši $13$? Gandrīz
  nekur - tāpēc tas pats spriedums bez izmaiņām der $14$ monētām
  (`LV.NOL.2019.7.2`) un $25$ monētām (`LV.SOL.2020.9.3`). Kāds ir lielākais
  monētu skaits, kuram šī metode vēl strādā?

#### 1.3. LV.NOL.2020.8.5 - kad viens zars vēl nav atbilde

Dotas $8$ pēc ārējā izskata vienādas monētas. Ir zināms, ka vai nu visām tām
masas ir vienādas, vai arī $4$ monētām ir viena masa, bet $4$ monētām - cita
masa. Kā ar $2$ svēršanām uz sviras svariem bez atsvariem var noskaidrot, kura
no iespējām pastāv īstenībā?

* *Saprašana:* Atbilde ir "jā/nē" par diviem scenārijiem. Uzmanību: ja svari
  **nav** līdzsvarā, atbilde ir gatava uzreiz - bet ja ir līdzsvarā, tas vēl
  neko nenozīmē.
* *Izpēte:* Sveram $3$ pret $3$. Kādos gadījumos $3+3$ var būt līdzsvarā, ja
  monētas tomēr ir divu veidu? (Ja katrā kausā ir divas vienas un viena otras
  masas monēta.) Kas tad ir abas nesvērtās monētas?
* *Risināšana:* Ja pirmajā svēršanā nav līdzsvara - ir divu veidu monētas,
  gatavs. Ja ir līdzsvars, tad vai nu visas astoņas ir vienādas, vai arī abas
  nesvērtās ir viena veida, bet katrā kausā ir $2+1$. Otrā svēršana: no viena
  kausa noņemam divas monētas un to vietā liekam abas nesvērtās. Līdzsvars -
  visas astoņas vienādas; nav līdzsvara - divu veidu monētas.
* *Atskats:* Šis ir tipisks gadījums, kad **līdzsvars nav atbilde, bet
  jautājums**. Pārbaudi savu pierakstu: vai tajā ir teikts, ko darīt katrā no
  abiem pirmās svēršanas iznākumiem?


## 2.nodarbības saturs

Otrā nodarbība maina skatpunktu: nevis "kā izdarīt", bet **"cik ar to var
uzzināt"**. Sākam ar pretējo galu - ar uzdevumiem, kur svēršanu skaits ir liels
un pats par sevi ir atbilde ($20$ monētas, $28$ svēršanas), un parādām
turnīra ideju: vispirms sadala pa pāriem, tad atsevišķi meklē uzvarētāju starp
"uzvarētājiem" un zaudētāju starp "zaudētājiem". Tālāk apskatām gadījumu, kad
viens mērījums dod tikai **divus** iznākumus (reaģents rāda vai nerāda vīrusu),
un tad dabiskie skaitļi ir nevis $3^k$, bet $2^k$: $64$ mēģenes un $6$
pārbaudes ir tieši $2^6$. Nodarbības kulminācija ir uzdevums, kurā izrādās, ka
ar svariem **principā nevar** uzzināt visu: ja katrā kausā jāliek tieši divas
bumbiņas, tad iespējamas tikai trīs dažādas svēršanas, un divas no četrām
bumbiņām paliek neatšķiramas. Tā ir pirmā reize, kad skolēni redz, ka atbilde
"nav iespējams" pamatojama, **uzskaitot visu, ko mērinstruments spēj pateikt**,
un ka atšķirība var objektīvi pastāvēt, bet nebūt izmērāma.

*Aptuvenais 90 minūšu plāns:* $10$ min - atkārtojums: cik iznākumu dod viena
svēršana, un kāpēc tas nosaka skaitļus $3^k$; $20$ min - $2.1$ piemērs
(turnīra ideja $10+9+9$); $15$ min - iesildīšanās uzdevumi patstāvīgi;
$15$ min - $2.2$ piemērs ($2^k$ un dalīšana uz pusēm); $20$ min - $2.3$
piemērs ar pilno pārlasi un secinājumu "nav iespējams"; $10$ min -
kopsavilkums: novērtējums un konstrukcija ir **divas** atsevišķas atbildes
daļas.

Šai nodarbībai specifiskie sasniedzamie rezultāti:

* SR: Saskaita, cik dažādas atbildes uzdevumā jāatšķir, un salīdzina to ar
  $3^k$ (sviras svari) vai $2^k$ (jā/nē pārbaude), lai novērtētu vajadzīgo
  darbību skaitu.
* SR: Atšķir divas atbildes daļas - **konstrukciju** ("lūk, procedūra") un
  **novērtējumu** ("ar mazāk nepietiek") - un zina, ka katrai vajag savu
  pamatojumu.
* SR: Lieto turnīra shēmu ($n/2$ svēršanas pāriem, tad atsevišķi vieglākais un
  smagākais) un saskaita kopējo svēršanu skaitu.
* SR: Pamato, ka kaut ko noskaidrot **nav iespējams**, uzskaitot visus
  mērinstrumenta iespējamos iznākumus un parādot, ka diviem dažādiem
  stāvokļiem tie sakrīt.

### Skaidrojamie piemēri

#### 2.1. LV.NOL.2016.6.4 - turnīrs divos virzienos

Dotas $20$ pēc ārējā izskata vienādas monētas, bet visas to masas ir dažādas.
Kā, izmantojot sviras svarus bez atsvariem, ar $28$ svēršanām atrast gan pašu
vieglāko, gan pašu smagāko monētu?

* *Saprašana:* Šeit svari vienmēr nosveras (visas masas dažādas) - tātad viena
  svēršana dod tikai **divus** iznākumus, nevis trīs.
* *Izpēte:* Cik svēršanu vajag, lai atrastu tikai smagāko? ($19$ - kā izslēgšanas
  turnīrā.) Un tikai vieglāko? Arī $19$. Kopā būtu $38$ - par daudz. Kur ir
  lieks darbs?
* *Pārformulēšana:* Ja $A$ vienreiz zaudējis, tas nevar būt smagākais. Tātad
  pēc vienas svēršanas kandidātu skaits **abiem** meklējumiem samazinās uzreiz.
* *Risināšana:* Sadala $20$ monētas $10$ pāros un salīdzina katru pāri - $10$
  svēršanas. Smagākās liek vienā kaudzītē, vieglākās - otrā. Smagākā ir
  jāmeklē tikai starp $10$ "uzvarētājiem" - tur pietiek ar $9$ svēršanām
  (svaros paliek smagākā, nākamā nāk klāt). Tāpat vieglākā - starp $10$
  "zaudētājiem", vēl $9$ svēršanas. Kopā $10+9+9 = 28$.
* *Atskats:* Uzraksti formulu $n$ monētām: $\frac{n}{2} + (\frac{n}{2}-1) +
  (\frac{n}{2}-1)$. Pārbaudi ar $n=15$ (`LV.NOL.2019.5.2`, kur viena monēta
  paliek bez pāra) - vai sanāk uzdevumā prasītās $21$ svēršanas?

#### 2.2. LV.NOL.2022.6.5 - kad iznākumu ir tikai divi

Laboratorijā $64$ mēģenēs atrodas siekalu paraugi. Zināms, ka viens paraugs ir
inficēts ar vīrusu. Laborantam ir $6$ testa trauki un $6$ reaģenti; reaģents,
ielejot to traukā ar siekalu maisījumu, uzrāda vai neuzrāda vīrusa klātbūtni un
pēc tam kļūst neaktīvs. Kā ar $6$ pārbaudēm noskaidrot, kurā paraugā ir vīruss?

* *Saprašana:* Svaru te nav, bet uzdevums ir tas pats: cik daudz var uzzināt ar
  sešiem mērījumiem. Cik iznākumu dod viena pārbaude? **Divi** - rāda vai nerāda.
* *Izpēte:* Cik atbildes jāatšķir? $64$. Un $2^6 = 64$ - tieši tik. Tātad
  procedūrai jābūt tādai, kurā **katra** pārbaude nogriež tieši pusi.
* *Risināšana:* Pirmajā traukā sajauc siekalas no $32$ mēģenēm. Ja reaģents
  rāda vīrusu - tas ir starp šīm $32$; ja ne - starp pārējām $32$. Pārējās
  noliek malā. Tālāk tāpat: $32 \to 16 \to 8 \to 4 \to 2 \to 1$. Sešas
  pārbaudes.
* *Atskats:* Kāpēc šeit dalām uz **pusēm**, bet $1.1$ uzdevumā dalījām
  **trijās** daļās? Kas mainītos, ja mēģeņu būtu $65$? Un ja būtu $100$?

#### 2.3. LV.AMO.2015.7.5 - kad svari principā nevar pateikt

Uz galda stāv četras pēc izskata vienādas bumbiņas, to masas attiecīgi ir
$10, 11, 12$ un $13$ grami. Vai ar dažām svēršanām uz sviru svariem bez
atsvariem, kur katrā kausā drīkst ielikt tieši divas bumbiņas, iespējams
**(A)** atrast visvieglāko un vissmagāko bumbiņu; **(B)** noteikt katras
bumbiņas masu?

* *Saprašana:* "Ar dažām svēršanām" nozīmē, ka svēršanu skaits nav ierobežots.
  Tātad jautājums ir nevis par ātrumu, bet par to, ko svari **vispār** spēj
  pateikt.
* *Izpēte:* Ja katrā kausā jāliek tieši divas bumbiņas, tad svēršanā piedalās
  visas četras. Cik dažādu svēršanu vispār eksistē? Sadali četras bumbiņas
  pāros - tādu sadalījumu ir tikai **trīs**.
* *Risināšana:* Izdarām visas trīs: $10+11 < 12+13$; $10+12 < 11+13$;
  $10+13 = 11+12$. **(A)** Smagākā ir tā bumbiņa, kas abās nevienādajās
  svēršanās bija uz smagākā kausa; vieglākā - tā, kas abās bija uz vieglākā.
  Tātad jā. **(B)** Bumbiņas $11$ un $12$ visos trīs rezultātos uzvedas
  vienādi - tās apmainot vietām, visi trīs rezultāti paliek tie paši. Tātad nē.
* *Atskats:* Šis ir pierādījums, ka kaut kas **nav iespējams**, un tas
  neizmanto nekādu triku - tikai visu iespējamo mērījumu uzskaitījumu.
  Salīdzini ar `LV.AMO.2017.8.4`, kur atsvaru ir pieci, katrā kausā atkal tieši
  divi - un tur atbilde abām daļām ir "jā". Kas mainās, kad atsvaru ir pieci,
  nevis četri?
