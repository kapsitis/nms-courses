---
layout: default
title: "7.2.A. Invarianti: Skaitliski invarianti"
permalink: /matf78/26_27/78_invariants/class1/

docx_header: "7.2.A. Invarianti: Skaitliski invarianti"
docx_footer: "ĀVĢ 7.-8.klašu matemātikas fakultatīvs"
docx_font: "Calibri"
docx_fontsize: 10
docx_heading_font: "Calibri Light"
docx_heading_color: "2F5496"
docx_heading1_size: 14
geometry: "a4paper, top=2.54cm, bottom=2.54cm, left=2.54cm, right=2.54cm"
---

# 7.2.A. Invarianti: Skaitliski invarianti

> Vai no stāvokļa $A$ var pāriet uz stāvokli $B$ ar noteikta veida gājieniem?

Invarianti ir "nezūdamības likumi" matemātikā. 
(Piemēram, ja pārvieto plaknes figūras daļas bez pārklāšanās, tad figūras laukums nemainās.)
Šajā nodarbībā par invariantiem algebrā (izteiksmju vērtības, atlikumu, kopskaits). 
Olimpiādēs invariants parasti jādefinē pašam risinātājam. 
Pēc invarianta definēšanas, risinājumā var iekļaut šo 3 soļu shēmu:

1. Nosauc invariantu (pasaka, ka vēlamies aplūkot kaut kādu lielumu). 
2. Katram atļautā gājiena veidam parāda, ka Jūsu invariants nemainās 
   (jāapskata **visi** atļautie gājieni, visi figūriņu novietošanas veidi utml.), 
3. Salīdzina vērtību sākumā un beigās. Un iegūst pretrunu, ja nesakrīt. 

Invariantu var izveidot arī tad, ja izteiksme mainās, bet to dara "ritmiski". 
Ar invariantu var pierādīt neiespējamību, bet nevar pierādīt iespējamību
(ja no stāvokļa $A$ **var** nonākt stāvoklī $B$, tad jākonstruē piemērs; 
nepietiek pateikt, ka "sakrita invariants"). 

**1.piemērs:** Skaitļu virknes pirmais loceklis ir $12$. Katru nākamo iegūst iepriekšējo vai
nu reizinot ar $2$ vai $3$, vai arī izdalot ar $2$ vai $3$ (ja dalās bez
atlikuma). Vai virknes $61.$ loceklis var būt $54$?

* *Izpēte:* Var izdarīt dažus gājienus. Vai rezultāts aug vai dilst? 
* *Izpēte:* Kā var sadalīt reizinātājos $12$ vai $54$?
* *Pārformulēšana:* Kas mainās un kas saglabājas reizinot/dalot ar $2$ vai $3$?
  Vai pirmreizinātāju skaitu (t.i. pašreizējo stāvokli) var attēlot citādi?

<!--
LV.AMO.2024.7.3 — invariants, kas nav pats skaitlis
-->

**2.piemērs:** 
Kastē atrodas baltas, sarkanas un zaļas lodītes. Ar vienu gājienu var izņemt
divas dažādu krāsu lodītes un ielikt vienu trešās krāsas lodīti. Vai var
panākt, ka paliek tikai viena lodīte, ja sākumā ir  
**(A)** $10$ baltas, $12$ sarkanas, $16$ zaļas;  
**(B)** $10$ baltas, $12$ sarkanas, $15$ zaļas?

* *Saprašana:* Ir divas daļas, katrai var vajadzēt citu pamatojuma veidu.
* *Izpēte:* Vienā gājienā **visas trīs** paritātes mainās vienlaikus. 
  Ja diviem skaitļiem reizē mainās paritāte - kas tad paliek nemainīgs?

<!--
LV.NOL.2023.7.5 — kad invarianta vien nepietiek
-->


---

## 1.uzdevums
Ieslēdzot kalkulatoru, uz tā ekrāna redzams skaitlis $1$; kalkulatoram ir divas 
pogas -- nospiežot zilo pogu, uz ekrāna redzamajam skaitlim pieskaita 
$15$, bet nospiežot zaļo pogu, skaitli pareizina ar $4$.  
**(A)** Vai kaut kādā secībā spiežot pogas var iegūt skaitli $1234$?  
**(B)** Vai uz šī kalkulatora var iegūt skaitli $12341234$?

<!--
Jauns. 
((1 * 4 * 4 + 3) * 4 * 4  + 3) * 4 + 3 + 3 = 1234

(1 * 4 * 4 * 4 * 4 + 15 + 15 + 15) * 4 + 15 + 15


12341234 nevar dabūt (atlikums, dalot ar 3). 
-->


## 2.uzdevums
Uz galda ir divas konfekšu kaudzītes ar $3$ un $5$ konfektēm. Vienā gājienā 
jebkurai no kaudzītēm var pievienot tik daudz konfekšu, cik ir otrā kaudzītē
(pieņemsim, ka mums vienmēr pietiek konfekšu, ko pielikt). 
Vai pēc vairākiem gājieniem var iegūt kaudzītes, kurās ir attiecīgi 
$34$ un $144$ konfektes? 


<!--
Jauns. 
No (41, 62) ejam atpakaļ. (41, 62) -> (41, 21) -> (21, 20)

(34, 144) -> (34, 110) -> (34, 76) -> (34, 42) -> (34, 6) -> 
(28, 6) -> (22, 6) -> (16, 6) -> (10,6) -> (4,6) -> (4,2) -> (2,2) 


0,1,1,2,3,5,8,13,21,34,55,89,144
0,1,3,4,7,11,18,29,
-->

## 3.uzdevums (LV.NOL.2026.10.3)
No $24$ melniem un $25$ baltiem kubiņiem ir izveidots "tornis", saliekot 
kubiņus vienu virs otra. Uz katra melnā kubiņa ir uzrakstīts balto 
kubiņu skaits, kas atrodas virs tā, bet uz katra baltā kubiņa 
ir uzrakstīts melno kubiņu skaits, kas atrodas virs tā. 
Kāda var būt visu uzrakstīto skaitļu summa?