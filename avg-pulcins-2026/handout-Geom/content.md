# Klasē analizējamie ģeometrijas uzdevumi

Tipiskas kļūdas:

<!-- 
1. RelyingOnDiagramAppearance
2. WrongAngleDecomposition
3. WrongTriangleSimilarityOrCongruence
4. SkippingCaseAnalysis
5. MisuseOfMidpointOrParallel/ConflatingPropertyAndCriterion
6. UnjustifiedAuxiliaryLineExists
-->

1. Paļaušanās uz zīmējumu (no 7.kl.)
2. Nekorekta leņķa "sadalīšana" vai "saskaitīšana" (no 7.kl.)
3. Nekorekti lietota vienādu vai līdzīgu trijstūru pazīme (no 7.kl.)
4. Nav gadījumu analīzes — apskata tikai vienu konfigurāciju (no 7.–8.kl.)
5. Sajaukta īpašība ar pazīmi (nepieciešamais vs. pietiekamais nosacījums)
   Tsk. nepareiza viduslīnijas vai paralelograma pazīme (no 8.–9.kl.). 
6. Palīglīnija vai palīgpunkts konstruēts, neparādot, 
   ka tas patiešām eksistē (no 8.kl.)




<!-- RelyingOnDiagramAppearance -->

## LV.AMO.2014.8.4 {-}

Rūtiņu lapā rūtiņu virsotnēs atzīmēti punkti $A, B, C, D, E$ un novilkti
nogriežņi $AB, BC, CD$ un $DE$ (skat. 8.zīm.). Kurš no leņķiem
$\sphericalangle ABC$ un $\sphericalangle CDE$ ir lielāks?

![](LV.AMO.2014.8.4.png)

<!--
Uzdevums tieši izaicina paļaušanos uz zīmējumu: leņķi rūtiņu lapā IZSKATĀS
gandrīz vienādi, bet faktiski ir jāaprēķina (piem., caur tangensiem vai
caur skalāriem reizinājumiem). Klases diskusijā uzsvērt: kas redzams uz acs
nav pierādījums.
-->


<!-- RelyingOnDiagramAppearance -->

## LV.NOL.2011.9.2 {-}

Kvadrātā $ABCD$ ir ievilkts riņķa līnijas loks $AC$ (riņķa līnijas centrs ir
$D$, bet rādiuss $DA$; skat. zīm.). Uz loka $AC$ atzīmēts tāds punkts $E$, ka
$\sphericalangle ADE = 2 \sphericalangle ABE$. Aprēķināt $\sphericalangle ABE$
lielumu.

![](LV.NOL.2011.9.2.png)

<!--
Skolēns var no zīmējuma "nolasīt", ka $E$ atrodas konkrētā loka vietā, vai
ka $\angle ABE$ ir konkrēts leņķis (piem., $45°$). Patiesībā vajag
aprēķināt, izmantojot ievilktā leņķa īpašības. Pārrunāt: kuri leņķi/garumi
ir doti tekstā, kuri jāatvasina, un kurus nedrīkst pieņemt no skices.
-->


<!-- WrongAngleDecomposition -->

## LV.NOL.2018.7.3 {-}

Aprēķināt $\sphericalangle BCD + \sphericalangle DEF + \sphericalangle FGH$
(skat. 8.att.), ja $AB \parallel GH$, $\sphericalangle ABC = 120^\circ$,
$\sphericalangle CDE = 90^\circ$ un $\sphericalangle EFG = 60^\circ$.

![](LV.NOL.2018.7.3.png)

<!--
Klasiskā "lauztā līnija starp paralēlām taisnēm". Skolēns velk palīgtaisnes
caur lūzuma punktiem un saskaita leņķus, bet viegli kļūdās ar virzieniem —
$\angle XOZ = \angle XOY + \angle YOZ$ nedarbojas, ja stars $OY$ neatrodas
leņķa iekšpusē. Pārrunāt katrā lūzuma punktā: vai pievienoju vai atņemu?
-->


<!-- WrongAngleDecomposition -->

## LV.AMO.2024.8.4 {-}

Uz riņķa līnijas ar centru $O$ ir atlikti punkti $A, B$ un $C$ tā, lai punkts
$O$ atrastos trijstūrī $ABC$. Pie tam zināms, ka $\sphericalangle AOC = \alpha$,
bet $\sphericalangle OAB = \beta$. Izteikt leņķi $\sphericalangle BCO$ ar
$\alpha$ un $\beta$!

<!--
Trijstūri $OAB$, $OBC$, $OAC$ ir vienādsānu (jo $OA=OB=OC$ — rādiusi).
Skolēns mēdz nepareizi saskaitīt vai atņemt leņķus pie virsotnēm $A$ un $C$,
nepamanot, ka leņķis $\angle BAC$ ir summa $\angle OAB + \angle OAC$ (jo $O$
atrodas trijstūra iekšpusē). Pārrunāt, kāpēc šis nosacījums ir kritisks.
-->


<!-- WrongTriangleSimilarityOrCongruence -->

## LV.AMO.2004.7.2 {-}

Taisnleņķa trijstūrī $ABC$ novilkts augstums $CH$ pret hipotenūzu $AB$. Punkts
$M$ atrodas uz hipotenūzas un $BM = BC$; punkts $N$ atrodas uz katetes $AC$ un
$CN = CH$. Pierādīt, ka $MN \perp AC$.

<!--
Klasiska uzdevuma struktūra: vairāki vienādi nogriežņi → trijstūru vienādība
vai līdzība. Skolēns var nepareizi sapārot atbilstošās virsotnes, raksta
"$\triangle BCM = \triangle CHN$ pēc malām" un secina nepareizu sakarību.
Pārrunāt: pirms pazīmes izsaukšanas vajag skaidri pierakstīt, kuras malas
un kuri leņķi ir atbilstošie.
-->


<!-- WrongTriangleSimilarityOrCongruence -->

## LV.AMO.2010.8.3 {-}

Astoņstūrī $ABCDEFGH$ visi iekšējie leņķi ir vienādi. Zināms arī, ka $ACEG$
ir kvadrāts. Pierādi, ka $BDFH$ arī ir kvadrāts!

<!--
Skolēns var "uz acu" pieņemt, ka astoņstūris ir regulārs (un tad rezultāts
ir triviāls) — bet uzdevums to neapgalvo. Pareizais ceļš: izmantot, ka visi
iekšējie leņķi ir $135°$, un pielietot trijstūru vienādības pazīmes pie
"griezuma" trijstūriem $ABC$, $CDE$, $EFG$, $GHA$. Pārrunāt, kāpēc nedrīkst
izlaist solis, kur pārbauda, ka šie trijstūri ir vienādi.
-->


<!-- SkippingCaseAnalysis -->

## LV.NOL.2022.8.3 {-}

Dots platleņķa vienādsānu trijstūris, kuram $\sphericalangle ABC = 20^\circ$.
Pierādīt, ka $3 \cdot AC > AB$.

<!--
Trijstūris ir vienādsānu, bet uzdevums nepasaka, kuras divas malas vienādas.
Skolēns parasti aplūko tikai vienu gadījumu (piem., $AB = AC$) un secina.
Patiesībā jāizšķir vismaz divi gadījumi: $AB = AC$ un $BC = AC$. Trešais
gadījums ($AB = BC$ ar virsotnes leņķi pie $B$) neder, jo tad $20°$ būtu
virsotnes leņķis un trijstūris nebūtu platleņķa. Pārrunāt: kā saraksts
"visi iespējamie gadījumi" pārklāj $100\%$ iespēju.
-->


<!-- SkippingCaseAnalysis -->

## LV.NOL.2021TEST.8.14 {-}

Vienādsānu trijstūra divu malu attiecība ir $2 : 4$ un tā perimetrs ir
$60~\mathrm{cm}$. Cik gara ir trijstūra pamata mala centimetros?

<!--
Vienkārša izskatīga uzdevuma slazds: vai attiecība $2:4$ ir starp pamatu
un sānu malu, vai starp sānu malu un pamatu? Vai trijstūris ar šādām malām
vispār eksistē (trijstūra nevienādība)? Skolēns mēdz aplūkot tikai vienu
gadījumu. Klases diskusijā: vienmēr izšķir gadījumus un pārbauda trijstūra
nevienādību abos.
-->


<!-- MisuseOfMidpointOrParallel -->

## LV.NOL.2023.9.3 {-}

Punkts $X$ ir izliekta četrstūra $ABCD$ diagonāles $AC$ viduspunkts. Zināms,
ka $CD \parallel BX$. Aprēķināt $AD$ garumu, ja $BX = 3$, $BC = 7$ un $CD = 6$.

<!--
Lielisks trijstūra viduslīnijas pielietojums. Skolēns var paspēlēties ar
"viduslīnija ir puse no pamata" formulu ($BX = \tfrac{1}{2} CD$?) — bet šeit
$BX = 3$, $CD = 6$, kas TIEŠĀM apmierina šo sakarību. Tas nozīmē, ka $X$ ir
trijstūra $ACD$ viduslīnija → $B$ ir $AD$ viduspunkts → $AD = 2 \cdot AB$
no atbilstošā trijstūra. Pārrunāt apgriezto teorēmu: ko nozīmē "puse" + "paralēla".
-->


<!-- MisuseOfMidpointOrParallel -->

## LV.AMO.2011.9.2 {-}

Trijstūrī $ABC$ $\sphericalangle ABC = 90^\circ$, bet punkts $P$ atrodas uz
malas $AB$. $M$ un $N$ ir attiecīgi $AC$ un $PC$ viduspunkti. Pierādi, ka
$\sphericalangle BAC = \sphericalangle BMN$.

<!--
$MN$ ir trijstūra $APC$ viduslīnija → $MN \parallel AP$. No tā un no
$\angle ABC = 90°$ var iegūt vajadzīgo leņķu vienādību. Skolēns var
nekorekti lietot viduslīnijas tieši uz trijstūra $ABC$ vai pieņemt, ka
$MN = \tfrac{1}{2} AB$ (kas šeit neder, jo $N$ nav uz $AB$). Pārrunāt:
kurā trijstūrī tieši $MN$ ir viduslīnija.
-->


<!-- ConflatingPropertyAndCriterion -->

## LV.NOL.2009.9.3 {-}

Divas riņķa līnijas krustojas. To rādiusu garumi ir $R$ un $r$, bet attālums
starp to centriem ir $d$. Vienā no abu riņķa līniju krustpunktiem tām abām
novilktas pieskares. Pierādīt: šīs pieskares ir perpendikulāras viena otrai
tad un tikai tad, ja $R^{2} + r^{2} = d^{2}$.

<!--
"Tad un tikai tad" prasa pierādīt ABAS virzienus (īpašība → pazīme un pazīme
→ īpašība). Skolēns mēdz pierādīt vienu virzienu un uzskatīt, ka apgrieztais
"automātiski" izriet. Pārrunāt: katra "iff" prasa atsevišķu pamatojumu abās
pusēs (vai eksplicītu ekvivalences ķēdi).
-->


<!-- ConflatingPropertyAndCriterion -->

## LV.NOL.2023.8.3 {-}

Dots vienādsānu trijstūris $ABC$, kuram $AB = BC$. Uz malas $AB$ izvēlēts
punkts $M$ un uz malas $BC$ izvēlēts punkts $K$ tā, ka $AM = AK = AC$.
Zināms, ka $AK \perp MC$. Aprēķināt trijstūra $ABC$ leņķus!

<!--
Daudzas vienādu nogriežņu sakarības ($AM = AK = AC$) un viens
perpendikularitātes nosacījums. Skolēns mēdz no $AM = AK$ "secināt", ka
$\triangle AMK$ ir vienādmalu, vai no $AK \perp MC$ — ka $K$ ir kāda
viduspunkts. Šie ir pazīmju nekorekti lietojumi (vienādsānu/vienādmalu
trijstūra īpašības nav pazīmes). Klases diskusijā: nodalīt "īpašības" no
"pazīmēm" un nekad nelietot tās savstarpēji.
-->


<!-- UnjustifiedAuxiliaryLineExists -->

## LV.AMO.2019.7.3 {-}

Izliektā četrstūrī $ABCD$ leņķu $BAD$ un $ADC$ bisektrises krustojas punktā
$M$. Pierādīt, ka $BM = CM$, ja zināms, ka $AD = AB + CD$.

*Piezīme.* Četrstūri sauc par izliektu, ja visi tā iekšējie leņķi ir mazāki
nekā $180^{\circ}$.

<!--
Tipiskā konstrukcija: atlikt uz $AD$ punktu $E$ tā, ka $AE = AB$. Tad
$ED = AD - AE = CD$. Skolēns var aizmirst pierādīt, ka šāds $E$ atrodas
uz $AD$ (nevis uz pagarinājuma) — tas izriet no $AB < AD$, jo $AB + CD = AD$
un $CD > 0$. Pārrunāt: kāpēc tieši šī konstrukcija eksistē, un kāpēc tā
ir noderīga (rada divus vienādus trijstūrus, kas dod $BM = CM$).
-->


<!-- UnjustifiedAuxiliaryLineExists -->

## LV.NOL.2021.8.3 {-}

Trijstūrī $ABC$ novilkta bisektrise $AE$. Uz taisnes $AE$ atlikts punkts $D$
tā, ka $AD = AB + AC$ un punkts $E$ atrodas starp punktiem $A$ un $D$.
Pierādīt, ka $\triangle BCD$ ir vienādmalu trijstūris, ja zināms, ka
$\sphericalangle BAC = 120^\circ$.

<!--
Konstrukcijas eksistence šeit ir vienkārša (taisne $AE$ ir bezgalīga,
$AB + AC$ ir konkrēts skaitlis), bet svarīgi pārbaudīt, ka tādu $D$ var
atlikt prasītajā pusē no $E$. Pēc tam jāpārbauda arī, ka iegūtā konstrukcija
(piem., palīgpunkts uz $AB$ vai $AC$, ar kuru pierāda vienādmalību) dod
divus trijstūrus, kuru attiecīgās malas ir vienādas.
-->

