# Klasē analizējamie algebras uzdevumi

Tipiskas kļūdas:

<!-- 
1. IncorrectTranslationOfWordProblem
2. UnjustifiedCancellationOrCombination
3. RootLossByDivisionByExpression
4. CaseAnalysisIncomplete
5. UncheckedConsistencyOfFoundValues
-->

1. Nepareizi sastādīts vienādojums teksta uzdevumam (no 5.kl.)
2. Nepamatota daļu vai darbību "vienkāršošana" pēc analoģijas (no 7.kl.)
3. Sakņu pazaudēšana, dalot vienādojuma puses ar izteiksmi, kas var būt nulle (no 7.kl.)
4. Nepilnīga gadījumu šķirošana (piem., zīmes vai paritātes gadījumi) (no 5.kl.)
5. Atrasto vērtību nepārbaudīšana sākotnējā uzdevumā (no 7.kl.)

**Izvērsts kļūdu saraksts (izdales materiālam):**

1. Nepareizi sastādīts vienādojums teksta uzdevumam.
   "Par tik vairāk" sajauc ar "tik reižu vairāk"; "$a$ par 6 vairāk nekā $b$" pieraksta kā $a = 6b$, nevis $a = b + 6$; procenti "par 20% palielinās" tiek pārtulkoti kā "20% no sākotnējā".
2. Nepamatota daļu vai darbību "vienkāršošana" pēc analoģijas.
   $(a+b)^2 = a^2 + b^2$ (aizmirsts $2ab$); $\sqrt{a+b} = \sqrt{a} + \sqrt{b}$; $\frac{a+b}{a+c}$ "saīsina" $a$ — bet $a$ nav reizinātājs, bet saskaitāmais.
3. Sakņu pazaudēšana, dalot ar izteiksmi, kas var būt nulle.
   No $x^2 = 3x$ dala abas puses ar $x$ un raksta $x = 3$, aizmirstot, ka $x = 0$ arī ir sakne. Pareizi: $x(x-3) = 0$.
4. Nepilnīga gadījumu šķirošana.
   Salīdzinot $2a$ un $4a$, aizmirst gadījumu $a = 0$; vienādojumā ar moduļiem $|x-2| + |x+1| = 5$ neuzšķir visus trīs intervālus uz skaitļu ass.
5. Atrasto vērtību nepārbaudīšana:
   Teksta uzdevumā atrod $x = -0{,}8$ stundas darba laiku un pieraksta atbildē; pēc kvadrātēšanas $\sqrt{x+4} = x-2$ saknei $x = 0$ neder, jo $\sqrt{4} = 2 \neq -2$.



<!-- IncorrectTranslationOfWordProblem -->

## LV.NOL.2018.7.1 {-}

Četrstāvu mājai ir vairāk nekā $200$ logu. Zināms, ka pirmajā stāvā ir nepāra
skaits logu, bet katrā no nākamiem stāviem to ir tieši par diviem mazāk nekā
stāvu zemāk. Kāds mazākais logu skaits var būt šīs mājas ceturtajā stāvā?

<!--
Klasiskā "par X mazāk" konstrukcija. Skolēns var izteikt katra stāva logu
skaitu kā $x, x-2, x-4, x-6$, bet bieži kļūdās — pieraksta "par 2 mazāk" kā
"$2x$" vai sajauc, kurš stāvs ir augstāks. Pārrunāt: kura mainīgā uzskatīt
par pamata mainīgo? Kā formulēt nosacījumu "vairāk nekā $200$ logu"?
-->


<!-- IncorrectTranslationOfWordProblem -->

## LV.NOL.2017.8.1 {-}

Slidotavai "Pa plānu ledu" ir taisnstūrveida forma un tās perimetrs ir $120$
metri. Pie slidotavas vienas malas atrodas kvadrātveida laukums, kurā uzbūvēta
slidu noma, bet pie blakus malas atrodas kvadrātveida stāvlaukums.
Stāvlaukuma platība ir par $1200~\mathrm{m}^2$ lielāka nekā slidu nomas
platība. Aprēķini slidotavas platību!

<!--
Pārveidošana no teksta uz vienādojumu prasa pareizi pārtulkot: (a) "perimetrs
$120$" → $2(a+b) = 120$, (b) "kvadrātveida laukums pie vienas malas" — laukuma
mala ir slidotavas malas garums, (c) "platība par $1200$ lielāka" → $a^2 - b^2
= 1200$, NEVIS $a^2 = 1200 \cdot b^2$. Šis ir tieši "par X vairāk" trap.
-->


<!-- UnjustifiedCancellationOrCombination -->

## LV.NOL.2018.8.1 {-}

Zināms, ka $a$ ir tāds reāls skaitlis, ka $a + \frac{1}{a} = 3$. Aprēķināt
**(a)** $a^{2} + \frac{1}{a^{2}} + 2$; **(b)** $a^{4} + \frac{1}{a^{4}}$.

<!--
Klasiskais "(a+b)^2 = a^2 + b^2 (bez vidus locekļa)" trap. Skolēns var
rēķināt $a^2 + 1/a^2 = (a + 1/a)^2 = 9$, aizmirstot $2 \cdot a \cdot 1/a = 2$.
Pareizi: $(a + 1/a)^2 = a^2 + 2 + 1/a^2$, no kā $a^2 + 1/a^2 = 7$. Pārrunāt:
"saskaitāmā kvadrāts nav saskaitāmo kvadrātu summa".
-->


<!-- UnjustifiedCancellationOrCombination -->

## LV.AMO.2015.8.1 {-}

Nosaki, vai izteiksmes $\sqrt{6 + 2\sqrt{5}} - \sqrt{6 - 2\sqrt{5}}$ vērtība ir
racionāls skaitlis!

<!--
Trap: skolēns mēģina rakstīt $\sqrt{6 + 2\sqrt{5}} = \sqrt{6} + \sqrt{2\sqrt{5}}$
vai citas "sadalīšanas". $\sqrt{a+b} \neq \sqrt{a} + \sqrt{b}$. Pareizi:
$6 \pm 2\sqrt{5} = (\sqrt{5} \pm 1)^2$, tātad izteiksme $= (\sqrt{5}+1) -
(\sqrt{5}-1) = 2$. Pārrunāt, kāpēc "atvienot sakni summā" neder.
-->


<!-- RootLossByDivisionByExpression -->

## LV.NOL.2005.8.5 {-}

Atrisināt vienādojumu $x^{3}(x^{2}-7)^{2} - 36x = 0$.

<!--
Sakni $x = 0$ viegli pazaudēt: skolēns var dalīt abas puses ar $x$ un raksta
$x^2(x^2-7)^2 = 36$. Tas izmet $x = 0$ — vienu no saknēm. Pareizi: iznest $x$
priekšā: $x \big( x^2(x^2-7)^2 - 36 \big) = 0$, no kā vai nu $x = 0$, vai
$x^2(x^2-7)^2 = 36$. Pārrunāt: kāpēc nedrīkst dalīt ar $x$ bez gadījuma
$x = 0$ pārbaudes.
-->


<!-- RootLossByDivisionByExpression -->

## LV.AMO.2008.8.2 {-}

Dots, ka $\frac{a}{b} = \frac{b}{c} = \frac{c}{a}$. Pierādīt, ka $a = b = c$.

<!--
Te skolēns var sareizināt visas trīs daļas (vai sākt dalīt) bez pārbaudes, ka
saucēji nav nulle, vai nepareizi pārvietot mainīgos. Pareizi: no
$\tfrac{a}{b} = \tfrac{c}{a}$ seko $a^2 = bc$ utt. Pārrunāt arī: kāpēc no
$\tfrac{a}{b} = \tfrac{b}{c}$ NEseko tieši $a = b$.
-->


<!-- CaseAnalysisIncomplete -->

## LV.AMO.2018.9.1 {-}

Dots vienādojums $(a-3)x^{2} + 5x - 2 = 0$.
**(A)** Kādām $a$ vērtībām vienādojumam ir tieši viena sakne?
**(B)** Kādām $a$ vērtībām vienādojumam ir divas dažādas reālas saknes?

<!--
Bieži pielaista kļūda — skolēns uzreiz lieto diskriminantu $D = 25 + 8(a-3)$,
neapsverot gadījumu $a = 3$, kurā vienādojums kļūst lineārs ($5x - 2 = 0$,
viena sakne $x = 2/5$). Pārrunāt: pirms diskriminanta lietošanas vienmēr
jāpārbauda, vai augstākā koeficienta nav nulle.
-->


<!-- CaseAnalysisIncomplete -->

## LV.AMO.2003.7.1 {-}

Dots, ka $|x+y| + |x-y| = 10$. Kāda ir lielākā iespējamā $x$ vērtība?

<!--
Klasiskā moduļu kļūda: skolēns aplūko tikai vienu gadījumu (piem.,
$x + y \geq 0$, $x - y \geq 0$), iegūst $2x = 10$, $x = 5$ un atstāj atbildi.
Trūkst pārējie trīs zīmju gadījumi un pārbaude, ka katrā no tiem $x$ tiešām
sasniedz $5$. Pārrunāt: kā nodrošināt, ka visi $4$ gadījumi pārklāj plakni.
-->


<!-- UncheckedConsistencyOfFoundValues -->

## LV.NOL.2015.9.1 {-}

Atrisināt vienādojumu $\frac{5}{x^{2}-9} - \frac{1}{3-x} = \frac{1}{2}$.

<!--
Pirms ķeršanās pie reizināšanas ar $2(x^2-9)$ jāpiezīmē, ka $x \neq \pm 3$.
Skolēns var iegūt kandidātes un aizmirst pārbaudīt, vai kāda no tām nesakrīt
ar $3$ vai $-3$ — tad tas būtu jāizslēdz. Pārrunāt: definīcijas apgabals
vienmēr jānosaka pirms ekvivalences pārveidojumiem.
-->


<!-- UncheckedConsistencyOfFoundValues -->

## LV.NOL.2010.7.2 {-}

Dots, ka $x^{3} = y^{4}$ un $x^{11} = y^{15}$. Atrast $x$ un $y$, ja tie ir
pozitīvi skaitļi.

<!--
Pēc pārveidojumiem skolēns var iegūt vairākas kandidātes un nepārbaudīt, vai
katra atbilst abām dotajām vienādībām un nosacījumam "pozitīvi". Pārrunāt:
ja pārveidojuma laikā kāpina pakāpēs, jāpārbauda, vai netiek ieviestas
svešsaknes (un vai nepazūd saknes), un visbeidzot — atbilstoši uzdevuma
ierobežojumiem.
-->

