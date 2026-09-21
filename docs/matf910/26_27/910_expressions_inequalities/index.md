---
layout: default
title: "9.2.temats: Izteiksmes un nevienādības"
permalink: /matf910/26_27/910_expressions_inequalities/
---
# 9.2.temats. Izteiksmes un nevienādības


Algebriskie pārveidojumi kā pierādīšanas instruments, nevis kā rēķināšana.
Nevienādību pierādīšana bez matemātiskās analīzes.
*Standarta līnijas: A1, A3.*
(Sk. [Matemātikas olimpiāžu satura standarts]({{ '/common_olympiad_program/olimpiazu_standarts/' | relative_url }})

* **Uzdevumu lapa:** {% include doc_links.html url="/matf910/26_27/910_expressions_inequalities/problems/" %}
{: .small}

* SR: Lieto saīsinātās reizināšanas formulas abos virzienos, arī identitātes
  $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$ un
  $(a+b+c)^2 = a^2+b^2+c^2+2(ab+bc+ca)$; saskata izteiksmē atkārtotu fragmentu
  un apzīmē to ar jaunu mainīgo.
* SR: Atdala pilno kvadrātu un lieto pamatnevienādību $t^2 \geq 0$ (arī vairākos
  saskaitāmajos vienlaikus), lai pierādītu, ka izteiksme ir pozitīva, un lai
  noskaidrotu, kad iestājas vienādība.
* SR: Lieto nevienādības $a+\frac{1}{a} \geq 2$ un
  $\frac{a}{b}+\frac{b}{a} \geq 2$ (ar $a,b>0$) un pamato tās, nevis atsaucas uz
  tām kā uz "zināmām formulām".
* SR: Veic darbības ar daļveida izteiksmēm un kvadrātsaknēm; nosaka definīcijas
  apgabalu un pārbauda, vai reizināšana ar saucēju nemaina nevienādības zīmi.

**Piemēri:** [LV.NOL.2025.9.1](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2025.9.1)
(izteiksme ar $20252024^2$ - apzīmējums $n$ un starpības kvadrāts),
[LV.NOL.2017.9.2](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2017.9.2)
(pierādīt $9x^6-x^3+1>0$),
[LV.AMO.2023.10.2](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2023.10.2)
(divu mainīgo izteiksme kā kvadrātu summa),
[LV.NOL.2023.9.4](https://eliozo.dudajevagatve.lv/problem?problemid=LV.NOL.2023.9.4)
($(x^4+1)(y^4+1)=4x^2y^2$ - vienādības gadījums nevienādībā),
[LV.AMO.2025.10.1](https://eliozo.dudajevagatve.lv/problem?problemid=LV.AMO.2025.10.1)
($\frac{a}{b}+\frac{b}{a} \geq 2+\frac{1}{ab}$ dažādiem naturāliem skaitļiem).


### SPARQL vaicājums

Vaicājums pilnā apjomā (ar komentāriem) glabājas failā `problems.rq`;
zemāk - tā būtiskā daļa.

```sparql
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

SELECT ?problemID ?grade ?diff
       (GROUP_CONCAT(DISTINCT ?family;       separator="+") AS ?families)
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
    # ---- (A) birku zars ------------------------------------------------
    ?p eliozo:problemText ?text .
    {
      { ?p eliozo:_hasSolutionConcept ?tag }
      UNION
      { ?p eliozo:_hasReasoningMethod ?tag }
      UNION
      { ?p eliozo:topic  ?topicIRI  . BIND(REPLACE(STR(?topicIRI),  "^.*#", "") AS ?tag) }
      UNION
      { ?p eliozo:method ?methodIRI . BIND(REPLACE(STR(?methodIRI), "^.*#", "") AS ?tag) }
    }
    BIND (
      IF (CONTAINS(?tag, "CompleteTheSquare") || CONTAINS(?tag, "CompletingSquare"), "Square",
      IF (CONTAINS(?tag, "AMGM") || CONTAINS(?tag, "AmGm")
          || ?tag = "UseTrivialInequalitiesAndAddThem" || ?tag = "AddingOrMultiplyingInequalities"
          || ?tag = "InequalityProvingStronger" || ?tag = "ProvingInequalities", "Mean",
      IF (CONTAINS(?tag, "Identit") || CONTAINS(?tag, "SquareOfSum") || CONTAINS(?tag, "DiffOfSquares")
          || ?tag = "FactoringAlgebraicExpressions" || ?tag = "ExpressionRegrouping", "Ident",
      IF (CONTAINS(?tag, "Substitut") || ?tag = "SystemsSubstituteVariables", "Subst",
      IF (?tag = "IrrationalAndReals" || ?tag = "RationalOperations" || ?tag = "FunctionDomainRange", "Frac",
      IF (CONTAINS(?tag, "PolynomialTransformations") || ?tag = "AlgebraicTransformations"
          || ?tag = "SymmetricAlgebraicExpressions"
          || ?tag = "InequalitiesEquivalentTransformations"
          || ?tag = "InequalitySolvingWithTransformations", "Transf",
                                                            "")))))) AS ?family )
    FILTER (?family != "")
    FILTER EXISTS { ?p eliozo:domain "Alg" }
    FILTER NOT EXISTS { ?p eliozo:domain "Comb" }
    FILTER (!CONTAINS(?text, "!["))
    FILTER NOT EXISTS { ?p eliozo:questionType "ShortAnswer" }
  }
  UNION
  {
    # ---- (B) teksta zars: uzdevumi bez birkām ---------------------------
    ?p eliozo:problemText ?text .
    FILTER NOT EXISTS { ?p eliozo:_hasSolutionConcept ?anyConcept }
    FILTER NOT EXISTS { ?p eliozo:method             ?anyMethod }
    BIND ("ByText" AS ?family)
    FILTER NOT EXISTS { ?p eliozo:domain "Comb" }
    FILTER NOT EXISTS { ?p eliozo:domain "Geom" }
    FILTER NOT EXISTS { ?p eliozo:domain "NT" }
    FILTER (!CONTAINS(?text, "![") && !CONTAINS(?text, "sphericalangle"))
    FILTER (STRLEN(?text) <= 320)
    FILTER (CONTAINS(?text, "nevienādīb")
            || (CONTAINS(?text, "ierād") && (CONTAINS(?text, "geq") || CONTAINS(?text, "leq")))
            || (CONTAINS(?text, "izteiksm")
                && (CONTAINS(?text, "frac") || CONTAINS(?text, "sqrt") || CONTAINS(?text, "^"))))
  }

  FILTER (LANG(?text) = "" || LANGMATCHES(LANG(?text), "lv"))
  FILTER (?grade >= 8 && ?grade <= 11)
  FILTER (?year >= 2003 && ?year <= 2026)
}
GROUP BY ?problemID ?grade ?diff
ORDER BY ?families ?grade ?problemID
```

**Kāpēc tieši tā atlasīts.**

* **Divi zari.** Šī temata uzdevumi datubāzē ir atrodami divos pilnīgi
  atšķirīgos veidos. Vecākajiem uzdevumiem ir piešķirtas *birkas* (zars **A**),
  bet ievērojamai daļai - it īpaši visai `LV.VOL` sērijai un jaunākajiem
  `LV.AMO` komplektiem - birku **nav vispār** (zars **B**). Ja rakstītu tikai
  birku vaicājumu, sarakstā netiktu, piemēram, `LV.AMO.2025.10.1`
  ($\frac{a}{b}+\frac{b}{a} \geq 2+\frac{1}{ab}$), kas ir viens no šī paša
  temata aprakstā minētajiem piemēriem. Tāpēc zars **B** meklē pēc
  formulējuma: "nevienādīb", "Pierādīt ... $\geq$/$\leq$", vai "izteiksm" kopā
  ar daļu, sakni vai pakāpi.
* **Birkas ir izkaisītas četros slāņos** (`_hasSolutionConcept`,
  `_hasReasoningMethod`, `eliozo:topic`, `eliozo:method`), tāpēc tās ar `UNION`
  apvieno vienā tekstiskā mainīgajā `?tag`, no `topic`/`method` IRI nogriežot
  daļu līdz `#`.
* **`?family` grupē kandidātus pēc metodes**, lai no garā saraksta būtu ērti
  veidot abu nodarbību "trepes": `Ident` (saīsinātās reizināšanas formulas,
  sadalīšana reizinātājos), `Square` (pilnais kvadrāts un $t^2 \geq 0$),
  `Mean` ($a+\frac{1}{a} \geq 2$, AM-GM, nevienādību saskaitīšana), `Subst`
  (atkārtota fragmenta apzīmēšana ar jaunu mainīgo), `Frac` (daļas, saknes,
  definīcijas apgabals), `Transf` (ekvivalenti pārveidojumi), `ByText`
  (atrasts teksta zarā). `Square` pārbaudām pirms `Ident`, jo pilnā kvadrāta
  uzdevumi gandrīz vienmēr nes līdzi arī birku `SquareOfSumIdentity`.
* **Birka `ArithmeticMean` apzināti netiek lietota viena pati.** Datubāzē tā
  apzīmē arī "vidējais aritmētiskais" tipa teksta uzdevumus (vidējais punktu
  skaits olimpiādē, vidējais koku vecums rezervātā), kam ar
  $\frac{a}{b}+\frac{b}{a} \geq 2$ nav nekāda sakara. Tāpēc `Mean` dod tikai
  `AmGm*`/`AMGM*` un nevienādību saskaitīšanas birkas.
* **Domēns.** Birku zarā prasām, lai uzdevumam būtu `domain = "Alg"`, un
  izmetam tos, kam blakus ir arī `"Comb"` - citādi sarakstā ielien
  kombinatorikas uzdevumi, kam algebriska birka pielipusi tikai kā
  blakusefekts. Teksta zarā, kur domēns bieži nav norādīts vispār, izmetam
  `Comb`, `Geom` un `NT`.
* **Attēli un īsās atbildes.** Uzdevumi ar `![`, ar `sphericalangle` un ar
  `questionType = "ShortAnswer"` šim tematam neder: tie prasa zīmējumu vai
  tikai skaitlisku atbildi, nevis pierakstītu pārveidojumu ķēdi. Teksta zarā
  papildus prasām `STRLEN(?text) <= 320`, jo garš teksts parasti nozīmē
  "ietērptu" uzdevumu, nevis tīru algebru.
* **Klases 8.-11.** - 9.-10. klases līmenis ar rezervi uz abām pusēm:
  8. klases uzdevumi der iesildīšanās pakāpienam, 11. klases - pēdējam.
* **UNION un mainīgo tvērums.** Uzmanību: `?p` un `?text` katrā `UNION` zarā
  jāsaista atkārtoti. Ja tos atstāj tikai ārējā `BGP`, zaru iekšējie
  `FILTER`/`NOT EXISTS` strādā ar nesaistītiem mainīgajiem, un vaicājums
  atgriež $0$ rindu.
* **Oxigraph īpatnība:** virknēs nevar rakstīt `\\geq`, tāpēc teksta zarā
  meklējam fragmentus `geq` un `leq`.

Vaicājums atgriež **113 kandidātus**. Tas ir garais saraksts, nevis gatava
nodarbību lapa: tajā ir palicis arī neliels troksnis (piem., `LV.NOL.2009.8.4`
par Maijas akmeņiem, `LV.NOL.2005.11.5` par zēniem un meitenēm,
`LV.AMO.2017.11.1` ar trigonometriju), ko atsijā ar roku.


### Atlasīto uzdevumu ID

Garais saraksts, sagrupēts pēc `?families` (113 uzdevumi).

**Ident** - saīsinātās reizināšanas formulas, sadalīšana reizinātājos

* LV.AMO.2004.8.1
* LV.AMO.2005.8.1
* LV.AMO.2006.8.1
* LV.AMO.2015.8.1
* LV.AMO.2016.8.1
* LV.AMO.2018.8.1
* LV.AMO.2024.8.1
* LV.NOL.2005.8.5
* LV.NOL.2006.8.1
* LV.NOL.2007.8.2
* LV.NOL.2008.8.3
* LV.NOL.2009.8.2
* LV.NOL.2013.8.4
* LV.NOL.2018.8.1
* LV.NOL.2019.8.1
* LV.AMO.2005.9.4
* LV.AMO.2009.9.2
* LV.AMO.2013.9.4
* LV.AMO.2019.9.5
* LV.AMO.2022A.9.4
* LV.AMO.2024.9.1
* LV.NOL.2004.9.1
* LV.NOL.2005.9.1
* LV.NOL.2007.9.2
* LV.NOL.2008.9.4
* LV.NOL.2010.9.1
* LV.NOL.2014.9.1
* LV.NOL.2015.9.1
* LV.NOL.2017.9.2
* LV.NOL.2022.9.1
* LV.NOL.2023.9.4
* LV.NOL.2024.9.2
* LV.NOL.2025.9.1
* LV.VOL.2016.11.3

**Mean** - $a+\frac{1}{a} \geq 2$, AM-GM, nevienādību saskaitīšana

* LV.NOL.2016.8.1
* LV.AMO.2017.9.2
* LV.AMO.2022B.9.2
* LV.NOL.2009.9.4
* LV.AMO.2019.11.4

**Subst** - atkārtota fragmenta apzīmēšana ar jaunu mainīgo

* LV.AMO.2013.8.3
* LV.NOL.2009.8.4
* LV.NOL.2011.8.5
* LV.AMO.2017.9.1

**Frac** - daļas, kvadrātsaknes, definīcijas apgabals

* LV.AMO.2016.9.1
* LV.NOL.2006.9.3
* LV.NOL.2011.9.1
* LV.NOL.2012.9.1
* LV.NOL.2015.9.5

**Transf** - ekvivalenti polinomu un nevienādību pārveidojumi

* LV.AMO.2003.10.1
* LV.AMO.2022B.10.4
* LV.AMO.2023.10.2
* LV.NOL.2024.10.2
* LV.VOL.2023.10.1
* LV.VOL.2024.10.3
* LV.AMO.2022B.11.2
* LV.AMO.2023.11.2
* LV.NOL.2023.11.1
* LV.NOL.2024.11.2
* LV.VOL.2023.11.1

**ByText** - atrasts teksta zarā, birku datubāzē nav

* LV.SOL.2020.8.1
* LV.NOL.2026.9.2
* LV.VOL.2004.9.5
* LV.VOL.2006.9.2
* LV.VOL.2014.9.1
* LV.VOL.2015.9.5
* LV.VOL.2020.9.1
* LV.VOL.2022.9.1
* LV.VOL.2023.9.1
* LV.AMO.2009.10.4
* LV.AMO.2010.10.1
* LV.AMO.2012.10.3
* LV.AMO.2013.10.1
* LV.AMO.2017.10.2
* LV.AMO.2025.10.1
* LV.NOL.2008.10.4
* LV.NOL.2010.10.1
* LV.NOL.2011.10.1
* LV.NOL.2012.10.1
* LV.NOL.2021.10.4
* LV.VOL.2004.10.1
* LV.VOL.2008.10.1
* LV.VOL.2009.10.4
* LV.VOL.2010.10.1
* LV.VOL.2015.10.1
* LV.VOL.2015.10.3
* LV.VOL.2016.10.3
* LV.VOL.2018.10.1
* LV.VOL.2019.10.5
* LV.AMO.2004.11.4
* LV.AMO.2009.11.5
* LV.AMO.2010.11.2
* LV.AMO.2016.11.3
* LV.AMO.2017.11.1
* LV.AMO.2019.11.1
* LV.NOL.2005.11.5
* LV.NOL.2006.11.4
* LV.NOL.2007.11.2
* LV.NOL.2009.11.3
* LV.NOL.2010.11.3
* LV.NOL.2011.11.1
* LV.NOL.2014.11.5
* LV.NOL.2016.11.1
* LV.NOL.2017.11.2
* LV.NOL.2018.11.5
* LV.NOL.2019.11.4
* LV.VOL.2004.11.1
* LV.VOL.2010.11.1
* LV.VOL.2011.11.1
* LV.VOL.2012.11.4
* LV.VOL.2014.11.1
* LV.VOL.2018.11.1
* LV.VOL.2024.11.1
* LV.VOL.2026.11.2


### 1.nodarbības saturs

Pirmajā nodarbībā izteiksmi pārveido nevis tāpēc, lai iegūtu atbildi, bet
tāpēc, lai kaut ko **pierādītu**. Sākam ar diviem rēķinu uzdevumiem, kuros
lielie skaitļi ir tikai maskēšanās: kad atkārtoto fragmentu apzīmē ar $n$,
paliek $(n-1)^2+(n+1)^2-2 = 2n^2$ un $(N+16)(N-16) = N^2-256$, un atbilde
iznāk bez neviena garā reizinājuma. Tā ir šī temata pamatkustība - *vispirms
pārveido, tikai tad rēķini*. Tālāk pārejam pie galvenās tehnikas: izteiksmi
pārraksta kā **nenegatīvu saskaitāmo summu** un tad atsaucas uz vienīgo
patiešām vajadzīgo nevienādību $t^2 \geq 0$. Viena mainīgā gadījumā tā ir
pilnā kvadrāta atdalīšana ($9x^6-x^3+1$ ar apzīmējumu $t=x^3$), divu mainīgo
gadījumā - kvadrātu summa ($x^2+5y^2+4xy-6y+9 = (x+2y)^2+(y-3)^2$). Katru
reizi uzstājam uz diviem pierakstīšanas soļiem, ko skolēni parasti izlaiž:
(1) visu pārnes uz vienu pusi un raksta $\ldots \geq 0$, (2) nosauc, **kad
iestājas vienādība**, jo tieši tas atšķir $\geq$ no $>$. Nodarbības beigās divi
uzdevumi, kuros kvadrātu summa vairs nav atbilde, bet tikai instruments: viens
prasa pierādīt **nevienādību** $a^2+b^2+c^2 \neq ab+ac+bc$, otrs - atrast
**visus** atrisinājumus, izmantojot to, ka nevienādībā iestājas vienādība.

Šai nodarbībai specifiski sasniedzamie rezultāti:

* SR: Izteiksmē saskata atkārtotu fragmentu, apzīmē to ar jaunu mainīgo un
  pamato, ka pēc apzīmējuma uzdevums kļūst par standarta kvadrātisku izteiksmi.
* SR: Pierādāmo nevienādību pārraksta formā "izteiksme $\geq 0$" un tikai tad
  meklē pārveidojumu; nepārveido nevienādību "no abām pusēm uz priekšu".
* SR: Atdala pilno kvadrātu un uzraksta izteiksmi kā vairāku kvadrātu (un
  nenegatīvas konstantes) summu; katram saskaitāmajam pamato nenegativitāti.
* SR: Nosaka, kad iestājas vienādība, un pārbauda, vai atrastais gadījums ir
  reāli sasniedzams; atšķir secinājumus "$\geq$" un "$>$".

#### Skaidrojamie piemēri

##### 1.1. LV.NOL.2025.9.1 - apzīmējums pirms rēķina

Aprēķināt izteiksmes $\frac{20252024^{2}}{20252023^{2}+20252025^{2}-2}$ vērtību!

* *Saprašana:* Atbilde ir viens skaitlis, bet "izrēķināt ar roku" nav
  iespējams - tātad uzdevums ir par pārveidojumu, nevis par rēķināšanu.
* *Izpēte:* Kāda ir sakarība starp trim skaitļiem $20252023$, $20252024$ un
  $20252025$? Kurš no tiem ir "vidējais"?
* *Pārformulēšana:* Apzīmē $n = 20252024$. Tad saucējs ir $(n-1)^2+(n+1)^2-2$.
* *Risināšana:* $(n-1)^2+(n+1)^2-2 = n^2-2n+1+n^2+2n+1-2 = 2n^2$, tātad
  vērtība ir $\frac{n^2}{2n^2} = \frac{1}{2}$.
* *Atskats:* Kur spriedumā tika izmantots tieši skaitlis $20252024$? Nekur -
  tātad tāda pati atbilde sanāk jebkuram $n$. Formulē vispārīgo apgalvojumu.

##### 1.2. LV.NOL.2017.9.2 - pilnais kvadrāts pēc apzīmējuma

Pierādīt, ka $9x^{6}-x^{3}+1 > 0$ visiem reāliem $x$.

* *Saprašana:* Jāpierāda apgalvojums par **visiem** $x$; dažu vērtību
  pārbaude nav pierādījums.
* *Izpēte:* Kuras $x$ pakāpes izteiksmē parādās? $x^6$ un $x^3$ - un
  $x^6 = (x^3)^2$.
* *Pārformulēšana:* Apzīmē $t = x^3$; jāpierāda, ka $9t^2-t+1 > 0$ visiem
  reāliem $t$ (jo $x^3$ pieņem visas reālās vērtības).
* *Risināšana:* $9t^2-t+1 = 9\left(t-\frac{1}{18}\right)^2 + 1 - \frac{1}{36}
  = 9\left(t-\frac{1}{18}\right)^2 + \frac{35}{36}$. Pirmais saskaitāmais ir
  $\geq 0$, otrais - stingri pozitīvs, tātad summa ir $> 0$.
* *Atskats:* Kāpēc šeit sanāk stingrā nevienādība $>$, nevis $\geq$? Kurš
  saskaitāmais to nodrošina? Un kāpēc bija svarīgi pateikt, ka $t=x^3$ pieņem
  **visas** reālās vērtības?

##### 1.3. LV.NOL.2023.9.4 - vienādības gadījums kā atbilde

Atrast visus tādus reālu skaitļu pārus $(x;y)$, kuriem
$\left(x^{4}+1\right)\left(y^{4}+1\right)=4 x^{2} y^{2}$.

* *Saprašana:* "Atrast visus" prasa divas daļas: parādīt, ka citu nav, un
  pārbaudīt atrastos.
* *Izpēte:* Novērtē katru reizinātāju atsevišķi. Ko var pateikt par $x^4+1$ un
  $2x^2$? ($x^4-2x^2+1 = (x^2-1)^2 \geq 0$.)
* *Pārformulēšana:* $x^4+1 \geq 2x^2 \geq 0$ un $y^4+1 \geq 2y^2 \geq 0$, tātad
  kreisā puse ir $\geq 4x^2y^2$ - vienmēr. Dotā vienādība nozīmē, ka abas
  nevienādības **vienlaikus** ir vienādības.
* *Risināšana:* Vienādība $x^4+1=2x^2$ iestājas tikai tad, ja $x^2=1$; tāpat
  $y^2=1$. Atrisinājumi: $(\pm 1; \pm 1)$ - četri pāri. Pārbauda, ievietojot.
* *Atskats:* Nevienādība šeit neko "nenovērtē" - tā **atrisina** vienādojumu.
  Kāpēc bija svarīgi, ka abas puses ir nenegatīvas, pirms tās sareizinājām?


### 2.nodarbības saturs

Otrā nodarbība ir par nevienādībām, kurās parādās **daļas un saknes**.
Pamatakmens ir viena vienīga nevienādība $a+\frac{1}{a} \geq 2$ (ar $a>0$) un
tās otra seja $\frac{a}{b}+\frac{b}{a} \geq 2$. Sākumā to nevis "atgādinām",
bet izvedam: reizinot ar $a$, tā pārvēršas par $a^2-2a+1 = (a-1)^2 \geq 0$ -
tātad tas ir tas pats $t^2 \geq 0$, ko lietojām $1.$ nodarbībā, tikai citā
ietērpā. Šeit parādās jauns disciplīnas punkts: **reizināt ar saucēju drīkst
tikai tad, kad zināma tā zīme**, un tāpēc katra uzdevuma sākumā jāpasaka, kādas
vērtības mainīgais vispār drīkst pieņemt. Standarta pakāpienā pārbaudām, ka
viena un tā pati kustība der ļoti dažādos ietērpos: nevienādībai ar naturāliem
skaitļiem (kur $(a-b)^2 \geq 1$, nevis tikai $\geq 0$), reizinājumam
$\left(\frac{3a}{b}+1\right)\left(\frac{3b}{a}+1\right)$ pēc iekavu atvēršanas,
un nevienādības atrisināšanai, kur saucējs maina zīmi un atbilde ir intervālu
apvienojums. Nodarbības beigās divi uzdevumi, kuros temats ir tikai puse no
darba: vienā vispirms jāatpazīst pilnie kvadrāti zem saknēm un jāpamato, ka
$\sqrt{A^2}=\lvert A \rvert$, otrā - jāievieš jauns mainīgais
$t=\frac{x+y}{x-y}$ un jāpamana, ka arī meklētā izteiksme ir tā pati
$t+\frac{1}{t}$ konstrukcija.

Šai nodarbībai specifiskie sasniedzamie rezultāti:

* SR: Pierāda nevienādību $a+\frac{1}{a} \geq 2$ (un
  $\frac{a}{b}+\frac{b}{a} \geq 2$), to reducējot uz $(a-1)^2 \geq 0$, un
  nelieto to kā "zināmu formulu" bez pamatojuma.
* SR: Pirms reizināšanas ar saucēju nosaka tā zīmi un paskaidro, kāpēc
  nevienādības zīme nemainās (vai mainās).
* SR: Nosaka daļveida izteiksmes definīcijas apgabalu un nevienādības atbildi
  pieraksta kā intervālu apvienojumu, atsevišķi pārbaudot galapunktus.
* SR: Vienkāršo divkāršas kvadrātsaknes, zem saknes atdalot pilno kvadrātu, un
  lieto $\sqrt{A^2}=\lvert A \rvert$, nevis $\sqrt{A^2}=A$.

#### Skaidrojamie piemēri

##### 2.1. LV.AMO.2025.10.1 - kad $(a-b)^2 \geq 0$ ir par vāju

Doti divi dažādi naturāli skaitļi $a$ un $b$. Pierādīt, ka
$\frac{a}{b}+\frac{b}{a} \geq 2+\frac{1}{ab}$.

* *Saprašana:* Kur uzdevumā izmantots nosacījums, ka skaitļi ir **naturāli** un
  **dažādi**? Bez tā apgalvojums nav patiess - pārbaudi ar $a=b=1$.
* *Izpēte:* Kāda ir $ab$ zīme? ($a,b \geq 1$, tātad $ab > 0$ - drīkst reizināt,
  un nevienādības zīme nemainās.)
* *Pārformulēšana:* Reizinot ar $ab$: $a^2+b^2 \geq 2ab+1$, tas ir
  $(a-b)^2 \geq 1$.
* *Risināšana:* $a$ un $b$ ir dažādi veseli skaitļi, tātad
  $\lvert a-b \rvert \geq 1$ un $(a-b)^2 \geq 1$. Ejot soļus atpakaļ (visi
  pārveidojumi ir ekvivalenti, jo $ab>0$), iegūstam pierādāmo.
* *Atskats:* Salīdzini ar $\frac{a}{b}+\frac{b}{a} \geq 2$: tur pietiek ar
  $(a-b)^2 \geq 0$. Ko tieši pielika klāt vārds "dažādi naturāli"?

##### 2.2. LV.AMO.2017.10.2 - atver iekavas, tad atpazīsti

Pierādīt, ka visiem pozitīviem skaitļiem $a$ un $b$ izpildās
$\left(\frac{3a}{b}+1\right)\left(\frac{3b}{a}+1\right) \geq 16$.

* *Saprašana:* Nosacījums $a,b>0$ ir dots - tātad visas daļas ir definētas un
  pozitīvas.
* *Izpēte:* Kas notiek, ja reizinājumu atver? $\frac{3a}{b} \cdot
  \frac{3b}{a} = 9$ - mainīgie saīsinās.
* *Pārformulēšana:* $\left(\frac{3a}{b}+1\right)\left(\frac{3b}{a}+1\right)
  = 9 + 3\left(\frac{a}{b}+\frac{b}{a}\right) + 1
  = 10 + 3\left(\frac{a}{b}+\frac{b}{a}\right)$.
* *Risināšana:* Pierādi atsevišķi, ka $\frac{a}{b}+\frac{b}{a} \geq 2$
  (reizini ar $ab>0$ un iegūsti $(a-b)^2 \geq 0$). Tad izteiksme ir
  $\geq 10+3 \cdot 2 = 16$. Vienādība iestājas, ja $a=b$.
* *Atskats:* Kāpēc nedrīkst katru iekavu novērtēt atsevišķi, piemēram,
  $\frac{3a}{b}+1 \geq 4$? Pārbaudi ar $a=1$, $b=100$.

##### 2.3. LV.NOL.2024.11.2 - jauns mainīgais daļu nevienādībā

Reāliem skaitļiem $x$ un $y$ ir spēkā vienādība
$\frac{x+y}{x-y}+\frac{x-y}{x+y}=5$. Pierādīt, ka
$\frac{x^{2}+y^{2}}{x^{2}-y^{2}}+\frac{x^{2}-y^{2}}{x^{2}+y^{2}}<3$.

* *Saprašana:* Vispirms pieraksti, kas vispār drīkst būt: $x \neq y$ un
  $x \neq -y$ - citādi nav definēta ne dotā, ne pierādāmā izteiksme.
* *Izpēte:* Abas izteiksmes ir vienādas formas $u+\frac{1}{u}$. Kāds ir $u$
  katrā no tām?
* *Pārformulēšana:* Apzīmē $t=\frac{x+y}{x-y}$; dots, ka $t+\frac{1}{t}=5$.
  Saskaiti $t$ un $\frac{1}{t}$ kā daļas:
  $t+\frac{1}{t} = \frac{(x+y)^2+(x-y)^2}{(x-y)(x+y)}
  = \frac{2(x^2+y^2)}{x^2-y^2}$.
* *Risināšana:* Tātad $\frac{x^2+y^2}{x^2-y^2} = \frac{5}{2}$, un meklētā
  izteiksme ir $\frac{5}{2}+\frac{2}{5} = \frac{29}{10} = 2{,}9 < 3$.
* *Atskats:* Vai kaut kur bija vajadzīgs, lai $x$ un $y$ būtu pozitīvi? Kā šis
  uzdevums saistās ar nevienādību $u+\frac{1}{u} \geq 2$ - vai šeit tā vispār
  tika lietota?
