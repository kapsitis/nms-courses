---
layout: default
title: "7.2.B. Invarianti: Rūtiņu krāsojumi"
permalink: /matf78/26_27/78_invariants/class2/

docx_header: "7.2.B. Invarianti: Rūtiņu krāsojumi"
docx_footer: "ĀVĢ 7.-8.klašu matemātikas fakultatīvs"
docx_font: "Calibri"
docx_fontsize: 10
docx_heading_font: "Calibri Light"
docx_heading_color: "2F5496"
docx_heading1_size: 14
geometry: "a4paper, top=2.54cm, bottom=2.54cm, left=2.54cm, right=2.54cm"
---
# 7.2.B. Invarianti: Rūtiņu krāsojumi

Īsa teorija

**1.piemērs:** Skaitļu virknes pirmais loceklis ir $12$. Katru nākamo iegūst iepriekšējo vai
nu reizinot ar $2$ vai $3$, vai arī izdalot ar $2$ vai $3$ (ja dalās bez
atlikuma). Vai virknes $61.$ loceklis var būt $54$?

* *Izpēte:* Uzraksti dažus pirmos locekļus. Vai pats skaitlis aug vai dilst?
  Nē — tātad jāmeklē cits lielums.
* *Pārformulēšana:* Sadali pirmreizinātājos: $12 = 2 \cdot 2 \cdot 3$ (trīs
  reizinātāji), $54 = 2 \cdot 3 \cdot 3 \cdot 3$ (četri). Par cik mainās
  reizinātāju skaits vienā gājienā?
* *Risināšana:* Katrā gājienā $\pm 1$, tātad reizinātāju skaita **paritāte**
  mainās katrā solī. No $1.$ līdz $61.$ loceklim ir $60$ gājieni — pāra skaits,
  tātad $61.$ loceklim reizinātāju skaits ir nepāra, kā $12$. Bet $54$ tas ir
  pāra. Nevar.
* *Atskats:* Šeit invariants nav "lielums, kas nemainās", bet "lielums, kas
  mainās pilnīgi regulāri". Kāds ir vispārīgais secinājums par $n$-to locekli?



<!--
LV.AMO.2024.7.3 — invariants, kas nav pats skaitlis
-->

**2.piemērs:** 

Kastē atrodas baltas, sarkanas un zaļas lodītes. Ar vienu gājienu var izņemt
divas dažādu krāsu lodītes un ielikt vienu trešās krāsas lodīti. Vai var
panākt, ka paliek tikai viena lodīte, ja sākumā ir **(A)** $10$ baltas, $12$
sarkanas, $16$ zaļas; **(B)** $10$ baltas, $12$ sarkanas, $15$ zaļas?

* *Saprašana:* Divas daļas — atbildes var būt dažādas, un katrai vajag savu
  pamatojuma veidu.
* *Izpēte:* Viens gājiens: divi skaiti $-1$, viens skaits $+1$. Tātad **visas
  trīs** paritātes mainās vienlaikus. Kas tad paliek nemainīgs? Jebkuru divu
  skaitu **starpība** pēc moduļa $2$.
* *Risināšana (A):* Sākumā visi trīs skaiti pāra — visas starpības pāra. Beigu
  stāvoklī $(1,0,0)$ divas starpības ir nepāra. Pretruna, tātad nevar.
* *Risināšana (B):* Paritātes $(\text{p}, \text{p}, \text{n})$ neizslēdz
  rezultātu $(0,0,1)$ — bet tas vēl nenozīmē, ka var! Jāuzrāda gājienu virkne:
  trīs gājieni *bs*, *bz*, *sz* samazina visus trīs skaitus par $1$; ar tiem
  nonāk pie $(1,3,6)$ un tālāk pabeidz ar rokām.
* *Atskats:* Formulē vienā teikumā, kāpēc invariants nekad nevar pierādīt "jā".

<!--
LV.NOL.2023.7.5 — kad invarianta vien nepietiek
-->



#### 1.2. LV.NOL.2023.7.5 — kad invarianta vien nepietiek

Kastē atrodas baltas, sarkanas un zaļas lodītes. Ar vienu gājienu var izņemt
divas dažādu krāsu lodītes un ielikt vienu trešās krāsas lodīti. Vai var
panākt, ka paliek tikai viena lodīte, ja sākumā ir **(A)** $10$ baltas, $12$
sarkanas, $16$ zaļas; **(B)** $10$ baltas, $12$ sarkanas, $15$ zaļas?

* *Saprašana:* Divas daļas — atbildes var būt dažādas, un katrai vajag savu
  pamatojuma veidu.
* *Izpēte:* Viens gājiens: divi skaiti $-1$, viens skaits $+1$. Tātad **visas
  trīs** paritātes mainās vienlaikus. Kas tad paliek nemainīgs? Jebkuru divu
  skaitu **starpība** pēc moduļa $2$.
* *Risināšana (A):* Sākumā visi trīs skaiti pāra — visas starpības pāra. Beigu
  stāvoklī $(1,0,0)$ divas starpības ir nepāra. Pretruna, tātad nevar.
* *Risināšana (B):* Paritātes $(\text{p}, \text{p}, \text{n})$ neizslēdz
  rezultātu $(0,0,1)$ — bet tas vēl nenozīmē, ka var! Jāuzrāda gājienu virkne:
  trīs gājieni *bs*, *bz*, *sz* samazina visus trīs skaitus par $1$; ar tiem
  nonāk pie $(1,3,6)$ un tālāk pabeidz ar rokām.
* *Atskats:* Formulē vienā teikumā, kāpēc invariants nekad nevar pierādīt "jā".

#### 1.3. LV.AMO.2024.7.3 — invariants, kas nav pats skaitlis




---

## 1.uzdevums



## 2.uzdevums

