---
title: "Ģeometrija: Līdzīgi trijstūri"
show-solutions: true
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "Ģeometrija: Līdzīgi trijstūri"
header-includes:
  - |
    \makeatletter
    \RedeclareSectionCommand[
      beforeskip=1.2ex plus 0.4ex minus 0.2ex,
      afterskip=0.4ex plus 0.2ex minus 0.2ex
    ]{subsection}
    \makeatother
---
# Ģeometrija: Līdzīgi trijstūri {-}

## 1.uzdevums {-} 

Zīmējumā attēlots trijstūris $FHG$, kur $FH=6$, $GH=8$ un $FG=10$. 
Punkts $I$ ir $FG$ viduspunkts un $HIJK$ ir kvadrāts. 
Nogriežņi $IJ$ un $GH$ krustojas punktā $L$. Cik liels ir iekrāsotā četrstūra laukums?
**(A)** 124/8, **(B)** 125/8, **(C)** 126/8, **(D)** 127/8, **(E)** 128/8.

![](problem1.png){ width=108pt }


::: solution
**Atbilde:** `B`

**Atrisinājums:**  
Trijstūris ar malu garumiem $6,8,10$ ir taisnleņķa, jo $6^2 + 8^2 = 10^2$. 
No taisnā leņķa virsotnes $H$ vilkta mediāna $HI$ -- un tā sadala 
taisnleņķa trijstūri divos vienādsānu trijstūros jeb mediānas garums ir 
puse no hipotenūzas. 

*Pierādījums apgalvojumam par taisnleņķa trijstūra mediānu:* Taisnleņķa 
trijstūrim $FGH$ piezīmējam klāt otru tādu pašu simetriski pret centru $I$, 
iegūstam taisnstūri. Taisnstūrī abas diagonāles ir vienāda garuma, 
tās krustpunktā dalās uz pusēm. Tāpēc $HI$ ir puse no 
taisnstūra diagonāles un $HI = HG/2 = 5$.

Kvadrāta $HIJK$ laukums ir $5 \cdot 5 = 25$. No tā jāatņem $\triangle HIL$ 
laukums. Ievērojam, ka $\triangle FGH \sim \triangle LHI$ 
(abi ir taisnleņķa trijstūri un šaurie leņķi $\sphericalangle IHL = \sphericalangle HGF$, 
jo trijstūris $HGI$ ir vienādsānu).
$\triangle LHI$ un $\triangle FGH$ līdzības koeficients ir $k = 5/8$, 
jo $LHI$ garākā katete $HI = 5$, bet $FGH$ garākā katete $GH=8$.

Izsakām abu trijstūru laukumus, izmantojot līdzības koeficientu:
$S(FGH) = \frac{1}{2} \cdot 6 \cdot 8 = 24$ un  
$S(LHI) = 24 \cdot k^2 = 24 \cdot \frac{25}{64} = \frac{75}{8}$. 

Visbeidzot iekrāsotās figūras laukums:  
$S(HKJL) = 25 - \frac{75}{8} = \frac{200 - 75}{8} = \frac{125}{8}$, 
kas ir atbilde **(B)**.
:::

<!--
EU.PinkKangaroo.2014.24

The diagram shows a triangle $FHG$ with $FH=6$, $GH=8$ and $FG=10$. 
The point $I$ is the midpoint of $FG$ and $HIJK$ is a square. 
The line segment $IJ$ intersects $GH$ at $L$. What is the area 
of the shaded quadrilateral?
**(A)** 124/8, **(B)** 125/8, **(C)** 126/8, **(D)** 127/8, **(E)** 128/8.
-->

## 2.uzdevums {-} 

Attēlā dots taisnstūris $PQRS$, kurā $PQ:QR = 1:2$. Punkts $T$ 
atrodas uz $PR$ tā, ka $ST$ ir perpendikulārs taisnei $PR$. 
Kāda ir trijstūra $RST$ laukuma un taisnstūra $PQRS$ laukuma attiecība?
**(A)** $1:(4\sqrt{2})$, **(B)** $1:6$, **(C)** $1:8$, **(D)** $1:10$, **(E)** $1:12$. 

![](problem2.png){ width=54pt }

::: solution
**Atbilde:** `D`

**Atrisinājums.** Pēc Pitagora teorēmas, taisnstūra 
diagonāle $PR = \sqrt{1^2 + 2^2} = \sqrt{5}$. 
Tā ir hipotenūza taisnleņķa trijstūrim $\triangle PQR$. 
Trijstūris $\triangle RST$ ir līdzīgs $\triangle PRQ$ un tam hipotenūza 
ir $1$. Tādēļ $\triangle RST$ līdzības koeficients attiecībā 
pret $\triangle PRQ$ ir $\frac{1}{\sqrt{5}}$ -- trijstūra 
$\triangle RST$ elementi (malas, augstumi) ir apmēram $2.236$ reizes īsāki par 
atbilstošajiem elementiem trijstūrī $PRQ$.

Laukumu attiecība abiem trijstūriem:   
$$\frac{S(\triangle RST)}{S(\triangle PRQ)} = \left( \frac{1}{\sqrt{5}} \right)^2 = \frac{1}{5}.$$

Tā kā taisnstūra laukums $S(PQRS)$ ir divreiz lielāks nekā 
trijstūra laukums $S(PRQ)$, tad $\triangle RST$ laukuma attiecība pret taisnstūra 
laukumu ir puse no $1/5$ jeb $\frac{1}{10}$, kas ir atbilde **(D)**. 
:::


<!--
UK.SMC.2014.14

The diagram shows a rectangle PQRS in which PQ : QR = 1 : 2. The point T on PR is such that ST is perpendicular to PR. What is the ratio of the area of the triangle RST to the area of the rectangle PQRS?
-->


## 3.uzdevums {-} 

Uz katras trijstūra malas ir atzīmēts punkts, kas atrodas vienu ceturtdaļu no malas garuma (sk. attēlu).
Kāda daļa no trijstūra laukuma ir iekrāsota? **(A)** $\dfrac{7}{16}$, **(B)** $\dfrac{1}{2}$, **(C)** $\dfrac{9}{16}$, **(D)** $\dfrac{5}{8}$, **(E)** $\dfrac{11}{16}$.

![](problem3.png){ width=108pt }


::: solution
**Atbilde:** `D`

**Atrisinājums:**  
Katram no abiem baltajiem trijstūriem pamats ir $3/4$ no sākotnējā trijstūra pamata, 
bet augstums ir četrreiz īsāks par sākotnējā trijstūra augstumu. Šo pēdējo faktu 
var pamatot, aplūkojot līdzīgus trijstūrus (piemēram, $\triangle BDJ$ un 
$\triangle BCK$ zīmējumā).  

![](problem3a.png){ width=108pt }

Ja sākotnējā trijstūra laukumu apzīmē ar $S = \frac{1}{2}ah$, tad katram no baltajiem 
trijstūriem laukums:  
$$S' = \frac{1}{2} \left(\frac{3}{4} a \right) \left( \frac{1}{4}h \right) = \frac{3}{16}S.$$

Atņemot divus šādus trijstūrus, iegūstam $S - \frac{3}{16}S - \frac{3}{16}S = \frac{5}{8}S$, 
kas ir atbilde **(D)**.

*Piezīme:* Ja izmanto trijstūra laukuma formulu $S = \frac{1}{2}ab \sin \gamma$, tad 
balto trijstūrīšu laukumus var izteikt uzreiz (pamatot, ka tie ir $3/16$ no sākotnējā trijstūra laukuma), 
neizmantojot spriedumus par līdzīgiem trijstūriem.
:::

<!--
UK.IMC.2015.25

A point is marked one quarter of the way along each side of a triangle, as shown.
What fraction of the area of the triangle is shaded?

**(A)** $\dfrac{7}{16}$, **(B)** $\dfrac{1}{2}$, **(C)** $\dfrac{9}{16}$, **(D)** $\dfrac{5}{8}$, **(E)** $\dfrac{11}{16}$.
-->


## 4.uzdevums {-}

Trijstūrī $FGH$ var novilkt taisni, kas ir paralēla tā pamatnei $FG$, caur punktu $X$ vai $Y$. Ieēnoto daļu laukumi ir vienādi. 
Dotā attiecība ir $HX : XF = 4 : 1$. Kāda ir attiecība $HY : YF$?  
**(A)** $1 : 1$, **(B)** $2 : 1$, **(C)** $3 : 1$, **(D)** $3 : 2$, **(E)** $4 : 3$

![](problem4.png){ width=180pt }


::: solution
**Atbilde:** `D`

**Atrisinājums:**  
Apzīmējam trijstūra pamata malu ar $a$ un augstumu ar $h$. 
Tad kreisā attēla trapecei apakšējais pamats ir $a$, bet augšējais pamats ir $\frac{4}{5} a$; trapeces augstums ir $\frac{1}{5}h$. Tad trapeces laukums:  
$$S = \frac{a + \frac{4}{5}a}{2} \cdot \left( \frac{1}{5} h \right) = \left( 1 + \frac{4}{5} \right) \cdot \frac{1}{5} \cdot \frac{ah}{2} = \frac{9}{25} \cdot \frac{ah}{2}.$$

Iekrāsotās trapeces laukums ir $\frac{9}{25}$ no trijstūra laukuma. Lai labajā pusē iekrāsotajam trijstūrim arī būtu tāds laukums, vajag, 
lai līdzības koeficients būtu $\frac{3}{5}$. Tad $\frac{HY}{YF}=\frac{3}{5}$, kas ir atbilde **(D)**. 
:::


<!--
EU.PinkKangaroo.2015.20

In the triangle $FGH$, we can draw a line parallel to its base $FG$, through point $X$ or $Y$. The areas of the shaded regions are the same. The ratio $HX : XF = 4 : 1$. What is the ratio $HY : YF$?

A $1 : 1$   B $2 : 1$   C $3 : 1$   D $3 : 2$   E $4 : 3$
-->



## 5.uzdevums {-}

Zīmējumā dots kvadrāts ar diagonāli un nogriezni, kas savieno 
virsotni ar malas viduspunktu. Kāda ir $P$ un $Q$ laukumu attiecība?
**(A)** $1 : \sqrt{2}$,
**(B)** $2 : 3$,
**(C)** $1 : 2$,
**(D)** $2 : 5$,
**(E)** $1 : 3$.

![](problem5.png){ width=72pt }

::: solution
**Atbilde:** `D`

**Atrisinājums-1:**  
Apzīmējam kvadrāta malu ar $1$.
Novelkam $GE$ -- trijstūra $ABC$ viduslīniju; tās garums ir $1/2$. 
Trapeces $ABEG$ laukums ir viduslīnijas un augstuma reizinājums: 

$$S_{ABEG} = \frac{1 + 1/2}{2} \cdot \frac{1}{2} = \frac{3}{8}.$$

Trijstūri $CDF$ un $GEF$ ir līdzīgi, jo tiem visi leņķi ir pa pāriem vienādi. 
Līdzības koeficients ir $2$, jo $CD$ ir divreiz garāks nogrieznis nekā $GE$. 
Abu šo trijstūru vertikālajiem augstumiem jābūt $1/3$ un $1/6$
(vienīgie skaitļi, kuru summa ir $1/2$ un pirmais ir divreiz lielāks kā otrais). 
Trijstūra $FDC$ laukums -- puse no pamata un augstuma reizinājuma:

$$S_{CDF} = \frac{DC \cdot \frac{1}{3}}{2} = \frac{1}{6}.$$

Savukārt $S_{GEF} = \frac{1}{24}$, jo tas ir četras reizes mazāks. 
Meklējamā laukumu attiecība: 

$$\frac{P}{Q} = \frac{S_{CDF}}{S_{ABEG} + S_{GEF}} = \frac{\frac{1}{6}}{\frac{3}{8} + \frac{1}{24}} = \frac{\frac{1}{6}}{\frac{10}{24}} = \frac{24}{60} = \frac{2}{5}.$$

Tā ir atbilde **(D)**


![](problem5A.png){ width=90pt }

**Atrisinājums-2:**  
Apzīmējam trijstūra $CEF$ laukumu ar $S$. Ievērojam, ka $\sphericalangle AFD = \sphericalangle CFE$ (krustleņķi) un 
$\sphericalangle DAF = \sphericalangle ECF$ (iekšējie šķērsleņķi), tādēļ trijstūri $ADF$ un $CEF$ ir līdzīgi.
Līdzības koeficients $k=2$, jo mala $AD$ ir divreiz garāka par attiecīgo malu $CE$. Tātad:

i. trijstūrim $ADF$ ir laukums $k^2 \cdot S = 4S$,
ii. mala $AF$ ir divreiz garāka nekā attiecīgā mala $CF$.

Apskatām $AF$ un $CF$ kā trijstūru $ADF$ un $CDF$ pamatus (tiem ir vienāds augstums). Saskaņā ar (ii), 
trijstūrim $ADF$ ir divreiz lielāks laukums nekā trijstūrim $CDF$ (laukums $P$), tātad tas ir $2S$.

Trijstūra $ACD$ laukums ir $6S$; tātad arī trijstūra $ABC$ laukums ir $6S$, bet $Q$ ir $6S-S = 5S$. 
Tātad meklētā attiecība ir $2 : 5$, 
kas ir atbilde **(D)**.

![](problem5B.png){ width=90pt }
:::

<!--
UK.IMC.2011.25

The diagram shows a square, a diagonal and a line joining a vertex
to the midpoint of a side. What is the ratio of area to area ? P Q
A B 2 : 3 C 1 : 2 D 2 : 5 E 1 : 3 
-->





## 6.uzdevums {-}

Zīmējumā attēlotajā taisnleņķa trijstūrī malu garumi 
ir $5~\mathrm{cm}$, 
$12~\mathrm{cm}$ un $13~\mathrm{cm}$.
Kāds ir ievilktā pusriņķa rādiuss centimetros, ja tā 
diametrs atrodas uz malas ar garumu $12~\mathrm{cm}$?  
**(A)** $8/3$, **(B)** $10/3$, **(C)** $11/3$, **(D)** $4$,
**(E)** $13/3$.

![](problem6.png){ width=162pt }


*Ieteikums:* Ja neesat pazīstami ar formulu $S=pr$ ievilktā 
riņķa rādiusa atrašanai, var savienot riņķa centru ar pieskaršanās
punktu uz hipotenūzas un aplūkot līdzīgus trijstūrus.

<!--
UK.PinkKangaroo.2012.13

The right-angled triangle shown has sides of length $5~\mathrm{cm}$, 
$12~\mathrm{cm}$ and $13~\mathrm{cm}$. What, in cm, is the 
radius of the inscribed semicircle whose diameter lies on the side 
of length $12~\mathrm{cm}$? 

**(A)** $8/3$, **(B)** $10/3$, **(C)** $11/3$, **(D)** $4$,
**(E)** $13/3$.


Let $H$, $I$, $J$ be the vertices of the triangle, $C$ the centre of the circle, and $K$ the point where the semicircle touches the edge $HI$ as shown. The angle $\sphericalangle CKH$ is a right angle because $HI$ is tangent to the circle and so perpendicular to the radius $CK$. The two triangles $HKC$ and $HJI$ are similar since they each have a right angle and they share the angle at $H$. Let $r$ be the radius of the semicircle, then $CK = r$ and $CH = 12 - r$. Then by similar triangles we have
$\dfrac{12 - r}{r} = \dfrac{13}{5}$.

So $5(12 - r) = 13r$.

Then $60 - 5r = 13r$.

So $18r = 60$ hence $r = \dfrac{10}{3}$.
-->

::: solution
**Atbilde:** `B`

**Atrisinājums-1:**  
Apzīmējam trijstūra virsotnes ar $H$, $I$, $J$, ar $C$ – riņķa centru un $K$ ir punkts, kur pusriņķis 
pieskaras malai $HI$, kā redzams zīmējumā. Leņķis $\sphericalangle CKH$ ir taisns, 
jo nogrieznis $HI$ pieskaras riņķim un tādēļ ir perpendikulārs rādiusam $CK$. 
Trijstūri $HKC$ un $HJI$ ir līdzīgi, jo tiem ir katram taisns leņķis un arī kopīgs leņķis virsotnē $H$. 
Apzīmējam pusriņķa rādiusu ar $r$; tad $CK = r$ un $CH = 12 - r$. No trijstūru līdzības iegūstam
$\dfrac{12 - r}{r} = \dfrac{13}{5}$.

![](problem6A.png)

Tātad $5(12 - r) = 13r$ un $60 - 5r = 13r$.
No šejienes $18r = 60$, tātad $r = \dfrac{10}{3}$, kas ir atbilde **(B)**.

**Atrisinājums-2:**  
Simetriski pret kateti garumā $12$ uzzīmējam otru taisnleņķa trijstūri. 
Esam ieguvuši jaunu vienādsānu trijstūri $HIJ$, kurā ievilkta riņķa līnija. 
Šī trijstūra laukums ir divkāršots $\frac{1}{2} \cdot 5 \cdot 12 = 30$, 
tātad $60$. 

No otras puses, trijstūra laukumu var izteikt ar formulu $S = pr$, kur 
$p$ ir pusperimetrs un $r$ - ievilktā riņķa līnija. 
Trijstūra $HIJ$ pusperimetrs ir $(13 + 13 + 10)/2 = 18$. Tāpēc pielīdzinām:
$$S = pr,\;\;60 = 18r,\;\;r = 60/18 = 10/3.$$

Tā ir atbilde **(B)**.

![](problem6B.png)
:::




## 7.uzdevums {-}

Trīs apļi un taisnes $PQ$ un $QR$ savstarpēji pieskaras, 
kā attēlots zīmējumā. Attālums starp mazākā un lielākā
riņķa centriem ir $16$ reizes lielāks par mazā riņķa 
rādiusu. Kāds ir leņķis $\sphericalangle PQR$?
**(A)** $45^{\circ}$, **(B)** $60^{\circ}$, **(C)** $75^{\circ}$,
**(D)** $90^{\circ}$, **(E)** $135^{\circ}$.

<!--
UK.SMC.2011.24

Three circles and the lines $PQ$ and $QR$ touch as shown.
The distance between the centres of the smallest and
the biggest circles is $16$ times the radius of the smallest
circle. What is the size of $\sphericalangle PQR$?  
**(A)** $45^{\circ}$, **(B)** $60^{\circ}$, **(C)** $75^{\circ}$,
**(D)** $90^{\circ}$, **(E)** $135^{\circ}$.
-->

![](problem7.png){ width=128pt }




## 8.uzdevums {-}

Zīmējumā attēloti divi kvadrāti: Vienam malas 
garums ir $20$, un otram malas garums ir $10$. 
Kāds ir ieēnotā apgabala laukums?

*Ierakstīt atbildē veselu skaitli vai parastu daļu P/Q.*

![](problem8.png){ width=108pt }

<!--
UK.SeniorKangaroo.2011.4

The diagram below includes two squares: one has sides
of length 20 and the other has sides of length 10.
What is the area of the shaded region?
-->



## 9.uzdevums {-}


Attēlā redzams taisnstūris $ABCD$, kam $AB=16$ un
$BC=12$.  $\sphericalangle ACE$ ir taisns leņķis un 
$CE=15$. Nogriežņi $AE$ un $CD$ krustojas punktā $F$.
Kāds ir $\triangle ACF$ laukums?

*Ierakstīt atbildē veselu skaitli vai parastu daļu P/Q.*

<!--
UK.SeniorKangaroo.2011.14

The diagram shows a rectangle $ABCD$ with $AB=16$ and
$BC=12$. Angle $ACE$ is a right angle and $CE=15$. The
line segments $AE$ and $CD$ meet at $F$.
What is the area of triangle ACF?
-->

![](problem9.png){ width=72pt }



## 10.uzdevums {-}

Riņķa diametra $AD$ garums ir $4$. Punkti 
$B$ un $C$ atrodas uz riņķa, kā attēlots zīmējumā, un $AB=BC=1$.
Atrast $CD$ garumu.

*Ierakstīt atbildē veselu skaitli vai parastu daļu P/Q.*

<!--
UK.Maclaurin.2010.4

The diameter $AD$ of a circle has length $4$. The points
$B$ and $C$ lie on the circle, as shown, so that $AB=BC=1$.
Find the length of $CD$.
-->

![](problem10.png){ width=126pt }



## 11.uzdevums {-}

Četras vienādas vienādsānu trapeces novietotas tā, ka to garākās 
pamata malas veido kvadrāta $PQRS$ diagonāles, kā parādīts attēlā. 
Punkts $X$ dala $PQ$ attiecībā $3:1$. Kāda daļa no kvadrāta 
ir iekrāsota?

**(A)** $\frac{5}{16}$, **(B)** $\frac{3}{8}$, **(C)** $\frac{7}{16}$,
**(D)** $\frac{5}{12}$, **(E)** $\frac{1}{2}$.

<!--
Four congruent isosceles trapeziums are placed so that their longer
parallel sides form the diagonals of a square $PQRS$, as shown. The point $X$
divides $PQ$
in the ratio $3:1$. What fraction of the square is shaded?
-->

![](problem11.png){ width=108pt }



## 12.uzdevums {-}

Trapeces perimetrs ir $5$ vienības un katras malas garums ir 
vesels skaitlis. Kādi ir divi mazākie trapeces leņķi?

**(A)** $30^{\circ}$ un $30^{\circ}$,
**(B)** $60^{\circ}$ un $60^{\circ}$,
**(C)** $45^{\circ}$ un $45^{\circ}$,
**(D)** $30^{\circ}$ un $60^{\circ}$,
**(E)** $45^{\circ}$ un $90^{\circ}$.



<!--
The perimeter of a trapezium is 5 units and the length of each of its sides is an integer number
of units. What are the two smallest angles of the trapezium?
A and B and C and D and E and 
-->



## 13.uzdevums {-}

Četrstūrī $PQRS$, $\sphericalangle PQR = 59^{\circ}$, 
$\sphericalangle RPQ = 60^{\circ}$, 
$\sphericalangle PRS = 61^{\circ}$ un 
$\sphericalangle RSP = 60^{\circ}$, kā redzams attēlā. 
Kurš no nogriežņiem ir garākais?
**(A)** $PQ$,
**(B)** $PR$, 
**(C)** $PS$, 
**(D)** $QR$, 
**(E)** $RS$.

![](problem13.png){ width=126pt }


<!--

In quadrilateral $PQRS$, $\sphericalangle PQR = 59^{\circ}$, 
$\sphericalangle RPQ = 60^{\circ}$, 
$\sphericalangle PRS = 61^{\circ}$ and 
$\sphericalangle RSP = 60^{\circ}$, as shown. 
Which of the following line segments is the longest?

**(A)** $PQ$,
**(B)** $PR$, 
**(C)** $PS$, 
**(D)** $QR$, 
**(E)** $RS$.
-->


## 14.uzdevums {-}

Attēlā redzams trijstūris $XYZ$. Malām
$XY$, $YZ$ un $XZ$ ir attiecīgi garumi $2$, $3$ un $4$. 
Taisnes $AMB$, $PMQ$ un $SMT$ 
vilktas paralēli trijstūra malām tā, ka 
nogriežņu $AP$, $QS$ un $BT$ garumi ir vienādi.
Kāds ir $AP$ garums?
**(A)** $\frac{10}{11}$, **(B)** $\frac{11}{12}$, **(C)** $\frac{12}{13}$,
**(D)** $\frac{13}{14}$, **(E)** $\frac{14}{15}$.

<!--
The diagram shows a triangle $XYZ$. The sides
$XY$, $YZ$ and $XZ$ have lengths $2$, $3$ and $4$
respectively. The lines $AMB$, $PMQ$ and $SMT$ 
are drawn parallel to the sides of triangle
$XYZ$ so that $AP$, $QS$ and $BT$ are of equal length.
What is the length of $AP$?
-->


![](problem14.png){ width=180pt }



## 15.uzdevums {-}

Attēlā dots trīsstūris $ABC$ ar laukumu $12~\mathrm{cm}^2$. 
Trijstūra malas ir pagarinātas līdz punktiem $P, Q, R, S, T$ 
un $U$ tā, kā parādīts, tā ka $PA = AB = BS$, 
$QA = AC = CT$ un $RB = BC = CU$.
Kāds ir sešstūra $PQRSTU$ laukums kvadrātcentimetros?

*Ierakstīt atbildē veselu skaitli vai parastu daļu P/Q.*

![](problem15.png){ width=126pt }

<!--
UK.SeniorKangaroo.2015.7

The diagram shows a triangle $ABC$ with area $12\text{ cm}^2$. 
The sides of the triangle are extended to points $P, Q, R, S, T$ 
and $U$ as shown so that $PA = AB = BS$, $QA = AC = CT$ and $RB = BC = CU$.

What is the area (in $\text{cm}^2$) of hexagon $PQRSTU$?

*Answer:* `156`
-->



## 16.uzdevums {-}

Taisnstūrī $JKLM$ leņķa $\angle KJM$ bisektrise krusto diagonāli 
$KM$ punktā $N$, kā parādīts. Attālumi no $N$ līdz malām $LM$ un 
$KL$ ir attiecīgi $8~\mathrm{cm}$ un $1~\mathrm{cm}$. Malas $KL$ garums 
ir $(a + \sqrt{b})~\mathrm{cm}$. Kāda ir $a + b$ vērtība?

*Ierakstīt atbildē veselu skaitli vai parastu daļu P/Q.*

![](problem16.png){ width=162pt }

<!--
UK.SeniorKangaroo.2015.17

In rectangle $JKLM$, the bisector of angle $\angle KJM$ cuts the 
diagonal $KM$ at point $N$ as shown. The distances between $N$ and 
sides $LM$ and $KL$ are $8\text{ cm}$ and $1\text{ cm}$ respectively. 
The length of $KL$ is $(a + \sqrt{b})\text{ cm}$. What is the value of $a + b$?
-->



## 17.uzdevums {-}

Attēlā dots četrstūris $PQRS$, kas veidots no diviem līdzīgiem 
taisnleņķa trīsstūriem $PQR$ un $PRS$. Malas $PQ$ garums ir $3$, 
malas $QR$ garums ir $4$, un $\angle PRQ = \angle PSR$. 
Kāds ir četrstūra $PQRS$ perimetrs?
**(A)** $22$, **(B)** $22\frac{5}{6}$, **(C)** $27$, 
**(D)** $32$, **(E)** $45\frac{1}{3}$.

![](problem17.png){ width=108pt }

<!--
UK.IMC.2017.13

The diagram shows a quadrilateral $PQRS$ made from two similar right-angled triangles, $PQR$ and $PRS$. The length of $PQ$ is $3$, the length of $QR$ is $4$ and $\angle PRQ = \angle PSR$. What is the perimeter of $PQRS$?

A $22$  \quad B $22\frac{5}{6}$  \quad C $27$  \quad D $32$  \quad E $45\frac{1}{3}$
-->


## 18.uzdevums {-}

Attēlā dots trīsstūris $FHI$, un punkts $G$ atrodas uz nogriežņa $FH$ tā, ka $GH = FI$. Punkti $M$ un $N$ ir attiecīgi nogriežņu $FG$ un $HI$ viduspunkts. Leņķis $NMH = \alpha^\circ$. Kurš no sekojošajiem dod izteiksmi leņķim $\angle IFH$?  
**(A)** $2\alpha^\circ$, **(B)** $(90 - \alpha)^\circ$, **(C)** $(45 + \alpha)^\circ$,
**(D)** $\left(90 - \tfrac12\alpha\right)^\circ$, **(E)** $60^\circ$.

![](problem18.png){ width=144pt }

<!--
UK.PinkKangaroo.2017.25

The diagram shows a triangle $FHI$, and a point $G$ on $FH$ such that $GH = FI$. The points $M$ and $N$ are the midpoints of $FG$ and $HI$ respectively. Angle $NMH = \alpha^\circ$. Which of the following gives an expression for $\angle IFH$?

A $2\alpha^\circ$
B $(90 - \alpha)^\circ$
C $(45 + \alpha)^\circ$
D $\left(90 - \tfrac12\alpha\right)^\circ$
E $60^\circ$
-->



## 19.uzdevums {-}

Attēlā dots kvadrāts $PQRS$ ar malu garumu $2$. Punkts $T$ ir malas $RS$ viduspunkts, un punkts $U$ atrodas uz nogriežņa $QR$ tā, ka $\angle SPT = \angle TPU$.
Kāds ir nogriežņa $UR$ garums?

*Ierakstīt atbildē veselu skaitli vai parastu daļu P/Q.*

![](problem19.png){ width=108pt }

<!--
UK.Maklaurin.2017.4

The diagram shows a square $PQRS$ with sides of length $2$. The point 
$T$ is the midpoint of $RS$, and $U$ lies on $QR$ so that 
$\angle SPT = \angle TPU$.
What is the length of $UR$?
-->



## 20.uzdevums {-}

Attēlā dots kvadrāts $ABCD$ un taisnleņķa trījstūris $ABE$. 
Malas $BC$ garums ir $3$. Malas $BE$ garums ir $4$. 
Kāds ir iekrāsotās daļas laukums?
**(A)** $5\frac{1}{4}$, **(A)** $5\frac{3}{8}$, **(C)** $5\frac{1}{2}$,
**(D)** $5\frac{5}{8}$, **(E)** $5\frac{3}{4}$.

![](problem20.png){ width=108pt }

<!--
UK.SMC.2017.6

The diagram shows a square $ABCD$ and a right-angled triangle $ABE$. The length of $BC$ is $3$. The length of $BE$ is $4$. What is the area of the shaded region?

A $5\frac{1}{4}$ \quad B $5\frac{3}{8}$ \quad C $5\frac{1}{2}$ \quad D $5\frac{5}{8}$ \quad E $5\frac{3}{4}$
-->



