---
layout: default
title: "9.1.B. Atrisinājumu struktūras: Pierādījumi no pretējā"
permalink: /matf910/26_27/910_solution_structure/handout_class1/

docx_header: "9.1.B. Atrisinājumu struktūras: Pierādījumi no pretējā"
docx_footer: "ĀVĢ 9.-10.klašu matemātikas fakultatīvs"
docx_font: "Calibri"
docx_fontsize: 10
docx_heading_font: "Calibri Light"
docx_heading_color: "2F5496"
docx_heading1_size: 14
geometry: "a4paper, top=2.54cm, bottom=2.54cm, left=2.54cm, right=2.54cm"
---
# 9.1.B. Atrisinājumu struktūras: Pierādījumi no pretējā

Pierādījums no pretējā sākas ar noliegumu. 
Kurš no apgalvojumiem ir patiess un kāpēc?

* "Ja $a = b$, tad $ac = bc$".
* "Ja šodien ir trešdiena, tad rīt ir sestdiena".
* "Visas manas pildspalvas ir zilas" (pieņemot, ka runātājam vispār nav pildspalvu).
* "Ja naturāls skaitlis $n$ nav pirmskaitlis, tad tas ir salikts skaitlis".
* "Ja virkne $a_1,a_2,a_3,a_4$ nav augoša, tad tā ir dilstoša".


**1.piemērs:** Vai var atrast tādus veselus skaitļus $a$ un $b$, ka $ab(a+43b)=434343$?

* *Saprašana:* "Vai var" - atbildei "jā" pietiek ar vienu piemēru, bet atbildei "nē" 
  vajag spriedumu par **visiem** $a$ un $b$.
* *Izpēte:* Ievieto dažus mazus $a$ un $b$. Kādus rezultātus var iegūt?
* *Pārformulēšana:* Kādu skaitļu reizinājums var būt nepāra skaitlis $434343$?
  Kādas ir prasības par $a,b,a+43b$? 
* *Risināšana:* Var šķirot dažādus gadījumus, kamēr atrod $a,b$ ar vēlamajām 
  īpašībām vai arī iegūst pretrunu.
* *Atskats:* Vai gadījumi aptver arī nulli un negatīvus veselus skaitļus?

<!--
LV.AMO.2016.8.2 — "Vai var?" (atbilde: nē)
-->

**2.piemērs:** Katrs no $28$ klases skolēniem kontroldarbā saņēma atzīmi, 
kas ir vesels skaitlis robežās no $0$ līdz $10$ ballēm. Pamatot, ka vai nu 
vismaz $4$ skolēniem ir vienāda atzīme, vai arī 
vismaz $4$ skolēni ieguva atzīmi, kas ir augstāka nekā $7$.

* *Saprašana:* Jāpierāda "A vai B". Pieņem pretējo - pēc De Morgana likuma noliegums ir 
  "ne A **un** ne B", t.i., jāpieņem abas daļas reizē.
* *Saprašana:* Ko nozīmē "Ne A" (pateikt vienkāršāk šo: "nav taisnība, ka vismaz $4$ skolēniem 
  ir vienāda atzīme").
* *Saprašana:* Ko nozīmē "Ne B" (pateikt vienkāršāk šo: "nav taisnība, ka vismaz $4$ skolēni 
  ieguva atzīmi, kas augstāka par $7$").

<!-- 
LV.AMO.2024.9.2 — "Vai nu A, vai B" (pieņem pretējo)
-->

---

## 1.uzdevums

> **LV.AMO.2003.7.3:**  
> Divi spēlētāji pamīšus raksta uz tāfeles pa vienam naturālam skaitlim no 1 līdz 9 ieskaitot.
> Nedrīkst rakstīt skaitļus, ar kuriem dalās kaut viens jau uzrakstīts skaitlis. 
> Kas nevar izdarīt gājienu, zaudē.
> Parādiet, kā tas, kas izdara pirmo gājienu, var uzvarēt.

Pirms šo risināt, pierakstiet, kādas daļas būtu jāsatur pilnam šī uzdevuma atrisinājumam.
Kad tas pierakstīts, var spēlēt šo spēli ar blakussēdētāju (vai patstāvīgi analizējot 
abu pušu gājienus) un saprast, kurš un kā var uzvarēt.

## 2.uzdevums

Kā mainīsies iepriekšējā uzdevuma atrisinājums, ja pēdējā teikumā "Parādiet" nomainītu uz "Pierādiet": 
*Pierādiet, kā tas, kas izdara pirmo gājienu, var uzvarēt.*

Vai vieglāk ir "parādīt" vai "pierādīt"?
