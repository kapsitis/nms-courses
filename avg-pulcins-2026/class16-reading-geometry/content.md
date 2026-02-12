---
title: "Ģeometrijas uzdevuma lasīšana (2026-02-09)"
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "Ģeometrijas uzdevuma lasīšana (2026-02-09)"
header-includes:
  - |
    \makeatletter
    \RedeclareSectionCommand[
      beforeskip=1.2ex plus 0.4ex minus 0.2ex,
      afterskip=0.4ex plus 0.2ex minus 0.2ex
    ]{subsection}
    \makeatother
  - \setcounter{section}{11}
  - |
    \usepackage{etoolbox}
    \AtBeginEnvironment{footnotesize}{\footnotesize}
---
# Ģeometrijas uzdevuma lasīšana (2026-02-09) {-}

**Koordinātu ģeometrijas formulas:** 

* Attālums starp punktiem $A(x_1, y_1)$ un $B(x_2, y_2)$ ir 
  $AB^2 = (x_2-x_1)^2 + (y_2-y_1)^2$
* Nogriežņa $AB$ viduspunkts $M = (\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2})$. 
* Paritātes pārbaude: Ja viduspunktam ir nepieciešamas veselu skaitļu koordinātas, 
  $x_1$ un $x_2$ ir jābūt vienādai paritātei (abi ir pāra vai abi ir nepāra skaitļi).
  Tas pats par $y_1$ un $y_2$.



**Trijstūru kongruences un līdzības pazīmes:** 

* $mmm$ -- ja trīs malas ir vienādas (vai proporcionālas), 
* $m \ell m$ -- ja divas malas ir vienādas (vai proporcionālas) un leņķis starp tām ir vienāds, 
* $\ell m \ell$ -- ja divi leņķi ir vienādi un viena mala sakrīt (līdzīgiem trijstūriem 
  pietiek ar to, ka sakrīt divi leņķi, pazīme $\ell \ell$).


**Taisnleņķa trijstūri:**

* Pitagora teorēma: $a^2 + b^2 = c^2$. 
* Taisnleņķa trijstūrī ar $30^\circ$ leņķi, 
  leņķim $30^\circ$ pretējā katete ir puse no hipotenūzas jeb $\sin 30^\circ = \frac{1}{2}$.
* Tallesa teorēma: Ievilkts leņķis, kas balstās uz riņķa diametru, vienmēr ir taisns. 

Praktisks ieteikums 4R (Read, Restate, Represent, Roadmap):  
(1) **Izlasīt** uzdevumu un atrast visus nosacījumus;  
(2) **Pārformulēt** īsāk un saviem vārdiem;  
(3) **Attēlot** situāciju zīmējumā, tabulā utt.  
(4) **Izplānot** sagaidāmās risinājuma darbības.


## 1.uzdevums (LV.VOL.2023.9.4) {-}

Plaknē atzīmēti punkti $A(5;2), $B(m;5)$ un $C(3;m)$. 
Kādām reālām $m$ vērtībām trijstūris $ABC$ ir taisnleṇka trijstūris?




::: solution
**Atrisinājums:**

Apskatām taisnleṇka trijstūri $ADB$, kur $D(m;2)$, $AD=|5-m|$ un 
$BD=|5-2|=3$ (skat. 1.att.). Izmantojot Pitagora teorēmu $\triangle ADB$, 
aprēķinām nogriežṇa $AB$ garuma kvadrātu:

$$AB^{2} = AD^{2}+BD^{2}=(5-m)^{2}+(2-5)^{2}=m^{2}-10m+34$$

![](LV.VOL.2023.9.4A.png){ width=150px }

Līdzīgi, katram nogrieznim konstruējot taisnleṇka trijstūri, iegūstam, ka

$$\begin{gathered}
AC^{2} = (5-3)^{2} + (2-m)^{2} = m^{2}-4m+8 \\
BC^{2} = (m-3)^{2} + (5-m)^{2} = 2m^{2}-16m+34
\end{gathered}$$

Lai trijstūris $ABC$ būtu taisnlenka, divu malu garumu kvadrātu summai 
jābūt vienādai ar trešās malas garuma kvadrātu. Aplūkojam trīs iespējamos gadījumus.

1. Ja $AB^{2}+AC^{2}=BC^{2}$, tad

   $$\begin{gathered}
   m^{2}-10 m+34+m^{2}-4 m+8=2 m^{2}-16 m+34 \\
   2m+8=0 \\
   m=-4
   \end{gathered}$$

2. Ja $AC^{2}+BC^{2}=AB^{2}$, tad

   $$\begin{gathered}
   m^{2}-4 m+8+2 m^{2}-16 m+34=m^{2}-10 m+34 \\
   m^{2}-5 m+4=0 \\
   m_{1}=1, \quad m_{2}=4
   \end{gathered}$$

3. Ja $A B^{2}+B C^{2}=A C^{2}$, tad

   $$\begin{gathered}
   m^{2}-10 m+34+2 m^{2}-16 m+34=m^{2}-4 m+8 \\
   m^{2}-11 m+30=0 \\
   m_{1}=5, \quad m_{2}=6
   \end{gathered}$$

Esam ieguvuši, ka trijstūris $ABC$ ir taisnleṇka ja $m$ ir $-4;1;4;5;6$.
::: 

## 2.uzdevums (LV.VOL.2013.9.2) {-}

Doti trīs regulāri trijstūri $OAB, OCD$ un $OEF$ (virsotnes norādītas
pulksteņrādītāja secībā), kuru malu garumi var atšķirties. Punkti $A, C, E$
neatrodas uz vienas taisnes; punkti $B, D, F$ arī neatrodas uz vienas taisnes.
Pierādīt, ka $\triangle ACE=\triangle BDF$.




::: solution
**Atrisinājums:**

Ievērosim, ka
$\sphericalangle BOC=\sphericalangle BOD+60^{\circ}=60^{\circ}+\sphericalangle AOC$
(skat. 1.zīm.). Tāpēc $\sphericalangle BOD=\sphericalangle AOC$. Līdz ar to
$\triangle BOD=\triangle AOC \quad$ pēc pazīmes $m \ell m$: $BO=AO$,
$\sphericalangle BOD=\sphericalangle AOC$ un $DO=CO$. Bet tad $BD=AC$, jo
vienādos trijstūros pret vienādiem leņķiem atrodas vienādas malas. Līdzīgi
secinām, ka arī $DF=CE$ un $FB=EA$, tāpēc $\triangle ACE=\triangle BDF$ pēc
pazīmes $m m m$.

![](LV.VOL.2013.9.2A.png)
::: 

## 3.uzdevums (LV.VOL.2011.9.2) {-}

Uz taisnleņķa trīsstūra garākās katetes kā diametra konstruēta riņķa līnija, 
kas no hipotenūzas atšķeļ nogriezni, kura garums vienāds ar īsākās katetes 
garumu. Aprēķināt hipotenūzas un īsākās katetes garumu attiecību!




::: solution
**Atrisinājums:**

Pieņemsim, ka $\sphericalangle C=90^{\circ}$, $AC>BC$ (skat. 1.zīm.). 
$\sphericalangle CDA=90^{\circ}$ (ievilkts leņķis, kas balstās uz diametru), 
tātad $CD$ ir $\triangle ABC$ augstums un 
$\triangle ABC-\triangle ACD-\triangle CBD$. Apzīmēsim 
$AC=b,\ BC=a,\ AB=c,\ CD=h$, $a^{2}+b^{2}=c^{2}$. Nevar būt, ka $BD=BC$ (tad 
$\triangle CBD$ būtu vienādsānu ar taisnu leņķi pie pamata - nav iespējams), 
tāpēc $AD=BC=a$. No $\triangle ABC-\triangle ACD$ seko 

$$\frac{AB}{AC}=\frac{BC}{CD} \Rightarrow \frac{AB}{BC}=\frac{AC}{CD} \Rightarrow \frac{c}{a}=\frac{b}{h} \tag{1}$$

No $\triangle ACD-\triangle CBD$ seko 
$\frac{CD}{BD}=\frac{DA}{CD} \Rightarrow \frac{h}{c-a}=\frac{a}{h} \Rightarrow h^{2}=a(c-a)$.
Ievietojot šo sakarību un vienādībā (1), iegūstam 
$\frac{c}{a}=\frac{\sqrt{c^{2}-a^{2}}}{\sqrt{a(c-a)}}=\sqrt{\frac{(c-a)(c+a)}{a(c-a)}}=\sqrt{\frac{c}{a}+1}$.
Apzīmējot $\frac{c}{a}=k$, iegūstam $k=\sqrt{k+1} \Rightarrow k^{2}=k+1$. 
Iegūtā vienādojuma saknes ir $\frac{1 \pm \sqrt{5}}{2}$. Tā kā $k>0$, tad 
meklētā attiecība ir $\frac{c}{a}=k=\frac{1+\sqrt{5}}{2}$.

![](LV.VOL.2011.9.2A.png)
::: 



## 4.uzdevums (LV.VOL.2010.9.4) {-}

Rūtiņu lapā novietoti divi taisnstūri (var būt sakrītoši) tā, ka to malas iet pa rūtiņu
malām. Teiksim, ka punkts pieder taisnstūrim, ja tas atrodas taisnstūra iekšpusē vai
uz tā kontūra.  
Cik no $8$ šo divu taisnstūru virsotnēm var vienlaicīgi piederēt arī otram taisnstūrim?




::: solution
**Atrisinājums:**

**Atbilde:** no astoņām divu taisnstūru virsotnēm vienlaicīgi otram arī taisnstūrim var
piederēt $0, 2, 3$, $4, 5, 6$ vai $8$ virsotnes, skat., piem., 2.zīm.

![](LV.VOL.2010.9.4A.png)

**Pierādījums.** (A) Pierādīsim, ka otram taisnstūrim nevar piederēt tieši viena
virsotne.

Pieņemsim pretējo, ka šāda (*īpaša*) virsotne tomēr atrodas- tā ir vienīgā no astoņām
virsotnēm, kas vienlaicīgi pieder arī otram taisnstūrim. Šī virsotne nevar sakrist ar
kādu no otra taisnstūra virsotnēm, jo tad arī otra taisnstūra virsotnei, ar kuru sakrīt
*īpašā* virsotne, būtu spēkā šī īpašība, t.i., būtu vismaz divas virsotnes ar minēto
īpašību. Tātad *īpašā* virsotne var atrasties tikai otra taisnstūra iekšpusē vai arī uz
kādas no tā malām. 3.zīmējumā ir parādīta situācija, kad īpašā virsotne ir otra
taisnstūra iekšpusē.

![](LV.VOL.2010.9.4B.png)

Aplūkosim, kur var atrasties tās divas virsotnes, kurām ar īpašo virsotni ir kopīga
mala. Vienai virsotnei $(V_{x})$ jāatrodas uz tās pašas horizontāles, uz kuras atrodas
īpašā virsotne. $V_{x}$ nevar atrasties otra taisnstūra iekšpusē vai uz tā malas, jo
tad arī $V_{x}$ būtu ar meklēto īpašību. Citai virsotnei $(V_{y})$ jāatrodas uz tās
pašas vertikāles, uz kuras atrodas īpašā virsotne. $V_{y}$ nevar atrasties otra
taisnstūra iekšpusē vai uz tā malas, jo tad arī $V_{y}$ būtu ar minēto īpašību. Tātad
gan $V_{x}$, gan $V_{y}$ atrodas ārpus otra taisnstūra. Bet tādā gadījumā pirmā
taisnstūra (kura trīs virsotnes ir *īpašā* virsotne, $V_{x}$ un $V_{y}$ iekšpusē
atrodas kāda no otrā taisnstūra virsotnēm.

Līdzīgi analizē gadījumu, kad $īpašā$ virsotne atrodas uz otra taisnstūra kontūra.

Esam ieguvuši pretrunu, tātad nevar būt tieši viena virsotne, kas pieder arī otram
taisnstūrim.

(B) Pierādīsim, ka otram taisnstūrim nevar piederēt tieši septiņas virsotnes.

Ieviesīsim koordinātu sistēmu un apskatīsim doto taisnstūru virsotņu koordinātes.
Pieņemsim, ka viena taisnstūra $ABCD$ virsotnes ir ar koordinātām
$A\left(x_{11}; y_{11}\right), B\left(x_{11}; y_{12}\right), C\left(x_{12}; y_{12}\right)$
un $D\left(x_{12}; y_{11}\right)$; un ir spēkā sakarības
$x_{11} < x_{12}$ un $y_{11} < y_{12}$, bet otra
taisnstūra ($KLMN$) virsotnes ir ar koordinātām
$K\left(x_{21}; y_{21}\right), L\left(x_{21}; y_{22}\right), M\left(x_{22}; y_{22}\right)$
un $N\left(x_{22}; y_{21}\right)$.

Pieņemsim pretējo- ir iespējams divus taisnstūrus novietot tā, ka tieši septiņas no
astoņām virsotnēm vienlaikus pieder arī otram taisnstūrim. Šis apgalvojums ir
līdzvērtīgs apgalvojumam, ka var novietot divus taisnstūrus tā, ka **tieši viena** no
astoņām virsotnēm **nepieder** otram taisnstūrim. Varam pieņemt, ka šī vienīgā
"nepiederošā" virsotne ir virsotne $M\left(x_{22}; y_{22}\right)$.

Tātad virsotņu koordinātas vienlaicīgi saista šādas sakarības:

$x_{11} \leq x_{21} \leq x_{12}$ un $y_{11} \leq y_{21} \leq y_{12}$ (jo
$K \left(x_{21} ; y_{21}\right)$ pieder taisnstūrim $ABCD$)

$x_{11} \leq x_{21} \leq x_{12}$ un $y_{11} \leq y_{22} \leq y_{12}$ (jo
L( $x_{21}; y_{22}$ ) pieder taisnstūrim $ABCD$)    

$x_{11} \leq x_{22} \leq x_{12}$ un $y_{11} \leq y_{21} \leq y_{12}$ (jo
$N\left(x_{22}; y_{21}\right)$ pieder taisnstūrim $ABCD$)

Bet no (2) un (3) nosacījumiem seko, ka vienlaicīgi


$x_{11} \leq x_{22} \leq x_{12}$ un $y_{11} \leq y_{22} \leq y_{12}$

tātad arī virsotne $M \left(x_{22}; y_{22}\right)$ pieder taisnstūrim $ABCD$. Esam
ieguvuši pretrunu, tātad pieņēmums, ka tieši viena virsotne nepieder otram taisnstūrim,
ir aplams, tāpēc tieši septiņas no astoņām abu taisnstūru virsotnēm nevar vienlaikus
piederēt arī otram taisnstūrim.
::: 

## 5.uzdevums (LV.AMO.2023.9.3) {-}

Trijstūrī viens leņķis ir par $120^{\circ}$ lielāks nekā otrs. 
Pierādīt, ka bisektrise, kas vilkta no trešā leņķa
virsotnes, ir divas reizes garāka nekā augstums no tās pašas virsotnes!




::: solution
**Atrisinājums:**

Apzīmējam trijstūra virsotnes ar $A, B, C$ un pieņemsim, ka 
$\sphericalangle B = \sphericalangle C + 120^{\circ}$ (skat.
17. att.). Apzīmējam $\sphericalangle C = x$, tad 
$\sphericalangle B = 120^{\circ} + x$ un 
$\sphericalangle A = 180^{\circ} - \sphericalangle B − 
\sphericalangle C = 60^{\circ} − 2x$.

No virsotnes $A$ novelkam augstumu $AH$ un bisektrisi $AM$. 
Tā kā $AM$ ir bisektrise, tad 
$\sphericalangle MAC = \frac{1}{2}\sphericalangle A = 30^{\circ} - x$. 
Leņķis $\sphericalangle AMH$ ir trijstūra $MCA$ ārējais leņķis, 
tātad 
$\sphericalangle AMH = \sphericalangle MAC + \sphericalangle MCA = 30^{\circ} − x + x = 30^{\circ}$. Tas nozīmē, ka taisnleņķa trijstūrī 
$AHM$ katete $AH$ atrodas pret $30^{\circ}$ leņķi, tātad
tā ir vienāda ar pusi no hipotenūzas $AM$ jeb $AM = 2AH$.

![](LV.AMO.2023.9.3A.png)
::: 



## 6.uzdevums (LV.AMO.2017.8.3) {-}

Taisnstūrveida papīra lapu pārlocīja tā, ka pārlocītais lapas stūris atrodas uz
pretējās malas (skat. 20.att.). Trijstūri $AFE$ un $CBE$ ir vienādi un 
$CB=7~\mathrm{cm}$, bet $BD=3~\mathrm{cm}$. Kādi ir sākotnējās papīra lapas 
malu garumi?

![](LV.AMO.2017.8.3.png){ width=90pt }





::: solution
**Atrisinājums:**

Sākotnējās lapas vienas malas garums $CD=CB+BD=10~\mathrm{cm}$ (skat. 21.att.).
Ievērojam, ka $AB=CD=10~\mathrm{cm}$ kā pārlocītās taisnstūrveida lapas pretējā
mala.

Tā kā pēc dotā trijstūri $AFE$ un $CBE$ ir vienādi, tad to atbilstošie elementi
arī ir vienādi: $\sphericalangle AEF=\sphericalangle BEC$, 
$AF=CB=7~\mathrm{cm}$, $AE=EC$ un $EF=BE$. Saskaitot vienādus lielumus, iegūstam
vienādas summas, tas ir, $CE+EF=AE+EB=AB=10~\mathrm{cm}$. Nogriežņa $KF$ garums
sakrīt ar $AF$ garumu. Tātad taisnstūra otras malas garums ir 
$10+7=17~\mathrm{cm}$. Līdz ar to sākotnējās papīra lapas malu garumi ir 
$10~\mathrm{cm}$ un $17~\mathrm{cm}$.

![](LV.AMO.2017.8.3A.png)
::: 

## 7.uzdevums (LV.NOL.2014.8.5) {-}

Trijstūra virsotnes atrodas kvadrātiska rūtiņu režģa punktos. Pierādīt, ka kāda
no trijstūra malām iet vai nu caur kādu citu rūtiņu režģa punktu, vai kādas 
rūtiņas centru. 



::: solution
**Atrisinājums:**

Ieviesīsim koordinātu sistēmu tā, ka koordinātu asis iet pa rūtiņu malām un $1$
vienība ir vienas rūtiņas malas garums. Varam ievērot, ka rūtiņu krustpunktu 
koordinātas ir $\left(\frac{n_{1}}{2}, \frac{n_{2}}{2}\right)$, kur $n_{1}$ un 
$n_{2}$ ir nepāra skaitļi. Punktu $(a, b)$ un $(c, d)$ viduspunkta koordinātas 
ir $\left(\frac{a+c}{2}, \frac{b+d}{2}\right)$.

![](LV.NOL.2014.8.5A.png)

Aplūkosim trijstūra virsotnu koordinātas $(x, y)$ pēc to paritātes. Katra 
virsotne ietilpst kādā no grupām

$$(p, p), \quad(p, n), \quad(n, p), \quad \mathbf{(n, n)}$$

kur ar $p$ apzīmēts pāra skaitlis, ar $n$ - nepāra.

Iespējami divi gadījumi:

- Ja divas trijstūra virsotnes ietilpst vienā grupā, tad izvēlamies šos divus 
  punktus un šo punktu viduspunkta koordinātas abi būs veseli skaitļi, kas 
  nozīmē, ka šis viduspunkts atrodas kādā citā rūtiņu režģa krustpunktā.
- Ja nekādas divas virsotnes neietilpst vienā grupā, tad var izvēlēties divas 
  virsotnes tā, ka abām koordinātām ir pretēja paritāte. Šo punktu viduspunkta 
  koordinātas būs formā $\left(\frac{n_{1}}{2}, \frac{n_{2}}{2}\right)$, kur 
  $n_{1}$ un $n_{2}$ - nepāra skaitļi, kas nozīmē, ka šis viduspunkts atrodas 
  kādas rūtiņas centrā jeb trijstūra mala iet caur rūtiņas centru. Līdz ar to 
  esam pierādījuši prasīto.
::: 

## 8.uzdevums (LV.NOL.2012.8.4) {-}

Uzzīmēt plaknē sešus punktus tā, lai no katra uzzīmētā punkta tieši trīs citi 
uzzīmētie punkti atrastos tieši $1~\mathrm{cm}$ attālumā.


::: solution
**Atrisinājums:**

Skat., piem., 9.zīm.; katra novilktā nogriežņa garums ir $1~\mathrm{cm}$, bet 
pārējie attālumi starp šiem punktiem ir lielāki vai mazāki nekā 
$1~\mathrm{cm}$.

![](LV.NOL.2012.8.4A.png)
::: 

