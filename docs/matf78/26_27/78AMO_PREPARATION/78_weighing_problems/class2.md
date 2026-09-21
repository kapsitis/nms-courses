---
layout: default
title: "7.AMO.B. Svēršanas uzdevumi: Cik informācijas dod viens mērījums"
permalink: /matf78/26_27/78AMO_PREPARATION/78_weighing_problems/class2/

docx_header: "7.AMO.B. Svēršanas uzdevumi: Cik informācijas dod viens mērījums"
docx_footer: "ĀVĢ 7.-8.klašu matemātikas fakultatīvs"
docx_font: "Calibri"
docx_fontsize: 10
docx_heading_font: "Calibri Light"
docx_heading_color: "2F5496"
docx_heading1_size: 14
geometry: "a4paper, top=2.54cm, bottom=2.54cm, left=2.54cm, right=2.54cm"
---

# 7.AMO.B. Svēršanas uzdevumi: Cik informācijas dod viens mērījums

> Nevis "kā izdarīt", bet "cik daudz ar to vispār var uzzināt".

Pirms meklēt procedūru, saskaiti divus skaitļus: **cik dažādas atbildes
jāatšķir** un **cik iznākumu dod viens mērījums**.

| Mērījums | Iznākumi | Ar $k$ mērījumiem atšķir |
|---|---|---|
| Sviras svari, iespējams līdzsvars | $3$ | $3^k$ |
| Sviras svari, kad visas masas dažādas | $2$ | $2^k$ |
| Pārbaude "jā/nē" (reaģents, jautājums) | $2$ | $2^k$ |

Ja atbilžu skaits ir tieši $2^k$ vai $3^k$, tad **katram** mērījumam jāstrādā
pilnā spēkā: katram jānogriež tieši puse (vai trešdaļa) atlikušo iespēju.
Rezerves nav.

Pilna atbilde optimizācijas uzdevumā sastāv no **divām** daļām:

1. **konstrukcija** - lūk, procedūra, kas to paveic ar tik soļiem;
2. **novērtējums** - ar mazāk soļiem nepietiek.

Katrai daļai vajag savu pamatojumu; viena no tām vien nav atbilde.

Noderīga shēma, kad jāatrod **gan** vieglākais, **gan** smagākais: vispirms
sadali priekšmetus pa pāriem un salīdzini katru pāri. Tad smagākais jāmeklē
tikai starp "uzvarētājiem", bet vieglākais - tikai starp "zaudētājiem".

$$\frac{n}{2} + \left(\frac{n}{2}-1\right) + \left(\frac{n}{2}-1\right)$$

Visbeidzot - dažreiz atbilde ir "**nav iespējams**". To pierāda, uzskaitot
**visus** mērījumus, ko instruments vispār spēj izdarīt, un parādot, ka diviem
dažādiem stāvokļiem visi rezultāti sakrīt. Atšķirība var objektīvi pastāvēt,
bet nebūt izmērāma.


**1.piemērs:** Dotas $20$ pēc ārējā izskata vienādas monētas, bet visas to
masas ir dažādas. Kā, izmantojot sviras svarus bez atsvariem, ar $28$
svēršanām atrast gan pašu vieglāko, gan pašu smagāko monētu?

* *Izpēte:* Tikai smagākajai vajadzētu $19$ svēršanas, tikai vieglākajai - arī
  $19$. Kopā $38$ ir par daudz. Kurš darbs tiek izdarīts divreiz?
* *Pārformulēšana:* Ja monēta vienu reizi izrādījusies smagākā, vai tā vēl var
  būt visvieglākā? Sadali monētas pa pāriem un saskaiti, cik kandidātu paliek
  katram no abiem meklējumiem.

<!--
LV.NOL.2016.6.4 — turnīrs divos virzienos, 10+9+9
-->


**2.piemērs:** Laboratorijā $64$ mēģenēs atrodas siekalu paraugi; viens
paraugs ir inficēts ar vīrusu. Laborantam ir $6$ testa trauki, kuros var
ieliet siekalas no vairākām mēģenēm, un $6$ reaģenti; reaģents uzrāda vai
neuzrāda vīrusa klātbūtni traukā un pēc tam kļūst neaktīvs. Kā ar $6$
pārbaudēm noskaidrot, kurā paraugā ir vīruss?

* *Saprašana:* Cik iznākumu dod viena pārbaude? Salīdzini ar sviras svariem.
* *Izpēte:* Aprēķini $2^6$. Cik lielu daļu mēģeņu katrai pārbaudei jāizslēdz,
  lai ar sešām pietiktu?

<!--
LV.NOL.2022.6.5 — kad iznākumu ir tikai divi
-->


**3.piemērs:** Uz galda stāv četras pēc izskata vienādas bumbiņas, to masas
attiecīgi ir $10, 11, 12$ un $13$ grami. Vai ar dažām svēršanām uz sviru
svariem bez atsvariem, kur katrā kausā drīkst ielikt tieši divas bumbiņas,
iespējams **(A)** atrast visvieglāko un vissmagāko bumbiņu; **(B)** noteikt
katras bumbiņas masu?

* *Izpēte:* Svēršanu skaits nav ierobežots - tātad izdari **visas**. Cik
  dažādu svēršanu te vispār eksistē? Sadali četras bumbiņas divos pāros.
* *Pārformulēšana:* Izraksti visu svēršanu rezultātus. Vai ir divas bumbiņas,
  kuras savstarpēji apmainot, **neviens** rezultāts nemainās?

<!--
LV.AMO.2015.7.5 — ko svari principā nevar pateikt
-->
