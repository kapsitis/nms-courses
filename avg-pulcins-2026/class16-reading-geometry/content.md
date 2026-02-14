---
title: "Ģeometrijas uzdevumu lasīšana (2026-02-09)"
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "Ģeometrijas uzdevumu lasīšana (2026-02-09)"
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
# Ģeometrijas uzdevumu lasīšana (2026-02-09) {-}

Praktisks ieteikums (4R: Read, Restate, Represent, Roadmap):  
(1) **Izlasīt** uzdevumu un atrast visus nosacījumus;  
(2) **Pārformulēt** īsāk un saviem vārdiem;  
(3) **Attēlot** situāciju zīmējumā, tabulā utt.  
(4) **Izplānot** sagaidāmās risinājuma darbības.


Jautājumi par lasīšanu un uzdevuma modeli: 

* Cik un kādos veidos var uzzīmēt uzdevumā aprakstīto situāciju?
* Ja uzdevumā minēts, ka trijstūris ir vienādsānu vai taisnleņķa, kādi veidi ir jāapskata?
* Vai nav ieviesti papildu pieņēmumi, kuru uzdevuma nosacījumos nav 
  (piemēram, punkts atrodas daudzstūra iekšpusē, aplūkojamais daudzstūris 
  ir izliekts, utml.)


## 1.piemērs {-}

Dots trijstūris $ABC$ un punkts $P$ apmierina nosacījumus $\sphericalangle PAB=30^\circ$, $\sphericalangle PBA=30^\circ$, 
$\sphericalangle PBC=40^\circ$, $\sphericalangle PCB=40^\circ$. 
Noteikt, vai $P$ atrodas trijstūra $ABC$ iekšpusē, uz tā robežas vai ārpusē.


## 2.piemērs {-}

Vai trijstūrim var būt malu garumi $a=4$, $b=7$ un mediāna, kas vilkta pret malu $b$ ar garumu $m_b = 3$?



## 3.piemērs {-}

Plaknē atzīmēti punkti $A,B,C,D$ un nekādi trīs no tiem neatrodas uz vienas taisnes. 
Zināms, ka leņķi $\sphericalangle DAB = 70^{\circ}$ un $\sphericalangle BCD=110^{\circ}$. 
Kāda var būt leņķu summa $\sphericalangle ABC + \sphericalangle CDA$?



## 1.uzdevums (LV.VOL.2023.9.4) {-}

Plaknē atzīmēti punkti $A(5;2)$, $B(m;5)$ un $C(3;m)$. 
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

Doti trīs regulāri trijstūri $OAB$, $OCD$ un $OEF$ (virsotnes norādītas
pulksteņrādītāja secībā), kuru malu garumi var atšķirties. Punkti $A, C, E$
neatrodas uz vienas taisnes; punkti $B, D, F$ arī neatrodas uz vienas taisnes.
Pierādīt, ka $\triangle ACE=\triangle BDF$.


## 3.uzdevums (LV.VOL.2011.9.2 variants) {-}

Uz taisnleņķa trīsstūra katetes $b$ kā diametra konstruēta riņķa līnija, 
kas no hipotenūzas $c$ atšķeļ nogriezni, kura garums vienāds ar otras katetes $a$
garumu. Aprēķināt attiecību $c/a$.

::: solution
**Uzdevuma oriģinālteksts:** 
Uz taisnleņķa trīsstūra garākās katetes kā diametra konstruēta riņķa līnija, 
kas no hipotenūzas atšķeļ nogriezni, kura garums vienāds ar īsākās katetes 
garumu. Aprēķināt hipotenūzas un īsākās katetes garumu attiecību!"
:::


## 4.uzdevums (LV.VOL.2010.9.4) {-}

Rūtiņu lapā novietoti divi taisnstūri (var būt sakrītoši) tā, ka to malas iet pa rūtiņu
malām. Teiksim, ka punkts pieder taisnstūrim, ja tas atrodas taisnstūra iekšpusē vai
uz tā kontūra.  
Cik no $8$ šo divu taisnstūru virsotnēm var vienlaicīgi piederēt arī otram taisnstūrim?


## 5.uzdevums (LV.AMO.2017.8.3) {-}

Taisnstūrveida papīra lapu pārlocīja tā, ka pārlocītais lapas stūris atrodas uz
pretējās malas (skat. 20.att.). Trijstūri $AFE$ un $CBE$ ir vienādi un 
$CB=7~\mathrm{cm}$, bet $BD=3~\mathrm{cm}$. Kādi ir sākotnējās papīra lapas 
malu garumi?

![](LV.AMO.2017.8.3.png){ width=90pt }


## 6.uzdevums (LV.NOL.2014.8.5) {-}

Trijstūra virsotnes atrodas kvadrātiska rūtiņu režģa punktos. Pierādīt, ka kāda
no trijstūra malām iet vai nu caur kādu citu rūtiņu režģa punktu, vai kādas 
rūtiņas centru. 


## 7.uzdevums (LV.NOL.2012.8.4) {-}

Uzzīmēt plaknē sešus punktus tā, lai no katra uzzīmētā punkta tieši trīs citi 
uzzīmētie punkti atrastos tieši $1~\mathrm{cm}$ attālumā.



