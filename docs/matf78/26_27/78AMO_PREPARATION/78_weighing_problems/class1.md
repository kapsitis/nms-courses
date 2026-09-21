---
layout: default
title: "7.AMO.A. Svēršanas uzdevumi: Viena svēršana - trīs iznākumi"
permalink: /matf78/26_27/78AMO_PREPARATION/78_weighing_problems/class1/

docx_header: "7.AMO.A. Svēršanas uzdevumi: Viena svēršana - trīs iznākumi"
docx_footer: "ĀVĢ 7.-8.klašu matemātikas fakultatīvs"
docx_font: "Calibri"
docx_fontsize: 10
docx_heading_font: "Calibri Light"
docx_heading_color: "2F5496"
docx_heading1_size: 14
geometry: "a4paper, top=2.54cm, bottom=2.54cm, left=2.54cm, right=2.54cm"
---

# 7.AMO.A. Svēršanas uzdevumi: Viena svēršana - trīs iznākumi

> Kā atrast atšķirīgo priekšmetu un pierakstīt procedūru, kas strādā **vienmēr**?

Sviras svariem ir **trīs** iznākumi: kreisais kauss smagāks, labais kauss
smagāks, līdzsvars. Tāpēc priekšmetus dala nevis uz pusēm, bet **trijās**
daļās: divas liek uz kausiem, trešā paliek malā. Pēc svēršanas viena no šīm
trim daļām paliek kā "aizdomās turamā".

No tā uzreiz izriet, cik daudz ar svēršanām vispār var uzzināt:

| Svēršanu skaits $k$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|
| Cik gadījumus var atšķirt ($3^k$) | $3$ | $9$ | $27$ | $81$ |

Atbilde šajos uzdevumos ir **procedūra**, nevis skaitlis. To var uzskatīt par
pabeigtu tikai tad, ja to var izpildīt cits cilvēks, neko vairāk nezinot.
Tāpēc risinājumu pieraksta kā **lēmumu koku**: katrai svēršanai apraksta
**visus trīs** iznākumus un katram - nākamo soli.

> **Biežākā kļūda:** aprakstīts tikai tas zars, kurā svari nosveras uz vienu
> pusi, bet nav pateikts, ko darīt līdzsvara gadījumā.

Procedūra jāpārbauda **sliktākajā gadījumā** - tajā zarā, kurā paliek
visvairāk neizšķirto iespēju.

Un vēl viens noderīgs novērojums: dažreiz uzdevums prasa **mazāk**, nekā
šķiet. Ja jānoskaidro tikai, vai atšķirīgā monēta ir vieglāka vai smagāka
(pašu monētu atrast nevajag), tad atbilžu ir tikai divas - un tāpēc pietiek ar
mazāk svēršanām.


**1.piemērs:** Zināms, ka no $26$ monētām viena ir viltota - tā ir vieglāka
nekā pārējās, kurām visām ir vienāda masa. Kā ar trīs svēršanām uz sviras
svariem bez atsvariem atrast viltoto monētu?

* *Izpēte:* Cik dažādas atbildes jāatšķir? Cik iznākumu dod viena svēršana?
  Atrodi mazāko $k$, kuram $3^k \geq 26$.
* *Pārformulēšana:* $26 = 9 + 9 + 8$. Sver $9$ pret $9$. Cik monētu paliek
  katrā no trim zariem - un vai **visos** trijos zaros ir pietiekami maz?

<!--
LV.NOL.2019.8.2 — kāpēc tieši trijās daļās
-->


**2.piemērs:** Dotas $13$ pēc ārējā izskata vienādas monētas. No tām $12$
monētas ir ar vienādu masu, bet viena - ar atšķirīgu. Kā ar divām svēršanām
noskaidrot, vai atšķirīgā monēta ir vieglāka vai smagāka par pārējām? Pašu
monētu atrast nav nepieciešams.

* *Saprašana:* Cik atbildes šeit jāatšķir - $13$ vai $2$? Tieši tāpēc pietiek
  ar divām svēršanām, lai gan monētas atrašanai to būtu par maz.
* *Izpēte:* Sver $6$ pret $6$. Ja svari nosveras - kurā kausā tu skatīsies
  otrajā svēršanā, lai noskaidrotu tieši **virzienu**, nevis monētu?

<!--
LV.NOL.2016.7.4 — vājāks jautājums maksā mazāk
-->


**3.piemērs:** Dotas $8$ pēc ārējā izskata vienādas monētas. Ir zināms, ka vai
nu visām tām masas ir vienādas, vai arī $4$ monētām ir viena masa, bet $4$
monētām - cita masa. Kā ar $2$ svēršanām uz sviras svariem bez atsvariem var
noskaidrot, kura no iespējām pastāv īstenībā?

* *Izpēte:* Sver $3$ pret $3$. Ja svari **nav** līdzsvarā, atbilde ir gatava.
  Bet kādi **divi** dažādi stāvokļi var dot līdzsvaru?
* *Izpēte:* Otrajā svēršanā jāatšķir tieši šie divi gadījumi. Kuras monētas
  līdz šim vēl nav bijušas uz svariem?

<!--
LV.NOL.2020.8.5 — kad līdzsvars nav atbilde, bet jautājums
-->
