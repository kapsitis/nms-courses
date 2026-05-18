---
title: "Klasē analizējamie kombinatorikas uzdevumi"
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "Klasē analizējamie kombinatorikas uzdevumi"
header-includes:
  - |
    \makeatletter
    \RedeclareSectionCommand[
      beforeskip=1.2ex plus 0.4ex minus 0.2ex,
      afterskip=0.4ex plus 0.2ex minus 0.2ex
    ]{subsection}
    \makeatother
  - \setcounter{section}{0}
  - |
    \usepackage{etoolbox}
    \AtBeginEnvironment{footnotesize}{\footnotesize}
---

# Klasē analizējamie kombinatorikas uzdevumi {-}

Tipiskas kļūdas:

<!-- 
1. ConfusingExistenceVsUniversalityQuantifier
2. MissingConstructionPartInOptimalProblems
3. ConfusingOrderedVsUnorderedSelections
4. MisusingPigeonholeWithWrongCounts
5. DoubleCountingTheSameObject
-->

1. Sajauc "Vai eksistē?" ar "Vai vienmēr?" uzdevumus (no 6.kl.)
2. "Kāds lielākais/mazākais" uzdevumos nav vai nu 
   piemēra vai novērtējuma (no 7.kl.)
3. Sajauc sakārtotas un nesakārtotas izlases (no 7.kl.)
4. Dirihlē principa nepareiza lietošana (no 7.kl.)
5. Viena un tā paša objekta saskaitīšana divreiz (no 5.kl.)


<!-- ConfusingExistenceVsUniversalityQuantifier -->

## LV.NOL.2018.5.2 {-}

Tautas deju kolektīvā ir $18$ dejotāji, jaunākajam no tiem ir $11$ gadi, bet
vecākajam — $15$ gadi.

**(A)** Vai noteikti šajā kolektīvā ir dejotājs, kuram ir $13$ gadi?
**(B)** Vai varētu gadīties, ka šajā kolektīvā ir tikai četru dažādu vecumu
dejotāji?
**(C)** Vai noteikti šajā kolektīvā ir vismaz pieci dejotāji, kam ir vienāds
gadu skaits?
**(D)** Vai noteikti šajā kolektīvā ir vismaz četri dejotāji, kam ir vienāds
gadu skaits?

<!--
Vienā uzdevumā skolēns sastopas ar abiem tipiem: "Vai noteikti...?"
(universalitāte — "jā" prasa pierādījumu visiem gadījumiem, "nē" — pretpiemēru)
un "Vai varētu gadīties...?" (eksistence — "jā" prasa vienu piemēru, "nē" —
vispārīgu pierādījumu). Pārrunāt katras daļas struktūru atsevišķi.
-->


<!-- ConfusingExistenceVsUniversalityQuantifier -->

## LV.NOL.2018.6.2 {-}

Koru finālskatē piedalījās desmit zēnu kori, kopā $291$ dalībnieks. Katrs
dalībnieks dzied tieši vienā korī.

**(A)** Vai noteikti ir tāds koris, kurā ir tieši $20$ dalībnieki?  
**(B)** Vai var gadīties, ka ir tāds koris, kurā ir tieši $32$ dalībnieki?  
**(C)** Vai var apgalvot, ka ir tieši viens tāds koris, kurā ir vismaz $30$
dalībnieki?  
**(D)** Vai noteikti ir tāds koris, kurā ir vismaz $30$ dalībnieki?

<!--
Brīnišķīga "kombinētā" problēma — visas četras daļas izmanto dažādus
kvantorus: "Vai noteikti..." (jā/nē + pierādījums), "Vai var gadīties..."
(jā/piemērs vai nē/pierādījums), "Vai var apgalvot..." (universalitāte).
Klases diskusijā skaidri jānošķir, ko prasa katra daļa.
-->


<!-- MissingConstructionPartInOptimalProblems -->

## LV.NOL.2010.6.4 {-}

Klases šaha turnīrā piedalās $10$ dalībnieki; katrs spēlē ar katru vienu
reizi. Par uzvaru piešķir $1$ punktu, par neizšķirtu $1/2$ punkta, par
zaudējumu $0$ punktus. Nolemts, ka klases lielmeistara nosaukumu piešķirs
tiem, kas izcīnīs vismaz $7$ punktus. Kāds lielākais skolēnu skaits šajā
turnīrā var iegūt lielmeistara nosaukumu?

<!--
Klasisks "Kāds lielākais...?" uzdevums. Skolēns mēdz vai nu uzrakstīt
piemēru ar, teiksim, $5$ lielmeistariem un secināt "atbilde: $5$", nepierādot,
ka $6$ nav iespējami; vai otrādi — pierādīt $\leq 5$, neuzkonstruējot
piemēru ar $5$. Klases diskusijā uzsvērt: vajag ABUS soļus.
-->


<!-- MissingConstructionPartInOptimalProblems -->

## LV.NOL.2004.6.4 {-}

Kvadrāts sastāv no $3 \times 3$ rūtiņām. Katrā rūtiņā ierakstīts kaut kāds
naturāls skaitlis (starp tiem var būt arī vienādi). Visās rindās un visās
kolonnās ierakstīto skaitļu summas ir dažādas. Kāda ir mazākā iespējamā visā
tabulā ierakstīto skaitļu summa?

<!--
Mazākā vērtība — vajag (a) piemēru, kas to sasniedz, un (b) pamatojumu, ka
mazāks neder. Iesācēji atrod piemēru ar mazu summu un izlaiž (b) daļu; vai
otrādi — pierāda apakšējo robežu, bet neuzrāda piemēru, kas to sasniedz.
-->


<!-- ConfusingOrderedVsUnorderedSelections -->

## LV.AMO.2019.9.1 {-}

Plaknē novilktas $5$ vertikālas, $4$ horizontālas un $3$ savstarpēji paralēlas
slīpas taisnes. Cik paralelogramu izveido šīs taisnes?

<!--
Paralelogramu veido divas vertikālās un divas horizontālās malas (vai cita
paralēlu pāru kombinācija). Skolēns var rakstīt $5 \cdot 4 = 20$ pāru
vertikāliem (kā sakārtotas izlases), bet patiesībā taišņu pāris $\{t_1, t_2\}$
ir tas pats kas $\{t_2, t_1\}$ — pareizi $C(5,2) = 10$. Pārrunāt atšķirību
starp izvēli un sakārtošanu.
-->


<!-- ConfusingOrderedVsUnorderedSelections -->

## LV.AMO.2018.9.2 {-}

Cik dažādos veidos basketbolā var gūt $18$ punktus, izmantojot tikai $1$
punkta un $3$ punktu metienus? Veidi, kas atšķiras tikai ar $1$ punkta un $3$
punktu metienu secību, tiek uzskatīti par dažādiem. Piemēram, $4$ punktus var
iegūt trīs dažādos veidos: $4 = 1+1+1+1 = 1+3 = 3+1$.

<!--
Šis uzdevums skaidri pasaka, ka secībai IR nozīme ("$1+3$ un $3+1$ ir dažādi"),
un tas ļauj salīdzināt ar uzdevumu, kur secībai nav nozīmes (cik veidos no
1 un 3 punktu metieniem var savākt $18$ — sakārtotas izlases). Pārrunāt:
kā uzdevuma formulējumā saprast, vai secībai ir nozīme.
-->


<!-- MisusingPigeonholeWithWrongCounts -->

## LV.AMO.2024.5.2 {-}

Kastē ir $7$ zaļas, $3$ sarkanas, $11$ melnas un $9$ baltas bumbiņas. Kāds ir
mazākais skaits bumbiņu, kas Aleksandram jāizvelk no kastes, lai garantētu,
ka viņam:

**(A)** ir vismaz divas vienādas krāsas bumbiņas;
**(B)** ir vismaz divas melnas bumbiņas;
**(C)** ir vismaz viena bumbiņa no katras krāsas?

<!--
Klasiskais Dirihlē uzdevums ar trim variantiem. Trap: (A) tikai krāsas skaits
ir svarīgs ($4$ krāsas → $4+1=5$ pietiek); (B) bumbiņu kopskaits, no kā
jāatņem melnās ($30-11+2 = 21$); (C) "sliktākais" gadījums — visas, izņemot
vienu krāsu ($30-3+1 = 28$). Skolēns mēdz lietot vienu un to pašu paņēmienu
visās trīs daļās.
-->


<!-- MisusingPigeonholeWithWrongCounts -->

## LV.AMO.2024.9.2 {-}

Katrs no $28$ klases skolēniem kontroldarbā saņēma atzīmi, kas ir vesels
skaitlis robežās no $0$ līdz $10$ ballēm. Pamatot, ka vai nu vismaz $4$
skolēniem ir vienāda atzīme, vai arī vismaz $4$ skolēni ieguva atzīmi, kas ir
augstāka nekā $7$.

<!--
Vispārinātais Dirihlē. Skolēns var tiešā veidā rēķināt $28/11 \approx 2{,}5$
un secināt "vismaz $3$ ar vienādu atzīmi" — bet vajag $4$. Pareizais paņēmiens:
izšķirt atzīmes $8, 9, 10$ vs. $0, \ldots, 7$ un pielietot principu pa daļām.
Pārrunāt: kā pārgrupēt būrus, lai sasniegtu vajadzīgo robežu.
-->


<!-- DoubleCountingTheSameObject -->

## LV.NOL.2014.6.4 {-}

Grāmatas lappuses ir sanumurētas ar naturāliem skaitļiem 
no $1$ līdz $2014$ pēc kārtas. Cik lappušu numuros 
ir sastopams vismaz viens no cipariem $3$ vai $7$?

<!--
Klasiskā ieslēgšanas–izslēgšanas piemērs. Skolēns var rakstīt $|A| + |B|$,
kur $A$ — ar $3$, $B$ — ar $7$, neatņemot $|A \cap B|$ — lappuses, kurās
parādās GAN $3$, GAN $7$. Pareizi: $|A \cup B| = |A| + |B| - |A \cap B|$.
-->


<!-- DoubleCountingTheSameObject -->

## LV.NOL.2021.5.1 {-}

Šogad uz Novadijas $5$.klašu matemātikas olimpiādi ir 
reģistrējušies $1270$ skolēni, kuriem jautāja par 
mācību priekšmetiem (matemātika, sociālās zinības,
latviešu valoda), kuri tiem patīk:

- $400$ dalībniekiem patīk matemātika un arī latviešu valoda, bet nepatīk sociālās zinības;
- $100$ dalībniekiem patīk matemātika un arī sociālās zinības, bet nepatīk latviešu valoda;
- $40$ dalībniekiem patīk latviešu valoda un arī sociālās zinības, bet nepatīk matemātika;
- $90$ dalībniekiem patīk tikai sociālās zinības;
- latviešu valoda patīk $531$ dalībniekam;
- visi trīs priekšmeti patīk $71$ dalībniekam.

Zināms, ka katram no skolēniem patīk vismaz viens no šiem priekšmetiem.
Cik dalībniekiem patīk tikai matemātika?

<!--
Trīs kopu Eilera–Venna diagramma. Skolēns var saskaitīt visu doto skaitļu summu
($400 + 100 + 40 + 90 + 71 + \ldots$) un secināt, ka palikušie ir "tikai
matemātika" — neapsverot, ka $71$ (visi trīs) ir jau ieskaitīts $400$, $100$,
$40$, ja tie ir formulēti citādi. Šeit teksts skaidri pasaka "bet nepatīk...",
tādējādi gadījumi ir disjunkti — bet skolēns to var pārskatīt.
-->

