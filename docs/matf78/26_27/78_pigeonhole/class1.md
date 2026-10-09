---
layout: default
title: "7.3.A. Dirihlē princips: Truši un būri"
permalink: /matf78/26_27/78_pigeonhole/class1/

docx_header: "7.3.A. Dirihlē princips: Truši un būri"
docx_footer: "ĀVĢ 7.-8.klašu matemātikas fakultatīvs"
docx_font: "Calibri"
docx_fontsize: 10
docx_heading_font: "Calibri Light"
docx_heading_color: "2F5496"
docx_heading1_size: 14
geometry: "a4paper, top=2.54cm, bottom=2.54cm, left=2.54cm, right=2.54cm"
---

# 7.3.A. Dirihlē princips: Truši un būri

> Ja $n+1$ trusis ir sasēdināts $n$ būros, tad kādā būrī ir vismaz divi truši.

**Vispārinātais princips:** Ja vairāk nekā $k \cdot n$ trušu ir sasēdināti
$n$ būros, tad kādā būrī ir vismaz $k+1$ trusis.

Risinājumā to pieraksta kā **pierādījumu no pretējā**: "Ja katrā būrī būtu
ne vairāk kā $k$ truši, tad pavisam būtu ne vairāk kā $k \cdot n$ trušu —
pretruna."

* Galvenais ir pašam izvēlēties **būrus**: krāsas, iespējamie komplekti,
  atlikumi, skaitļu grupas. Labi būri ir tādi, kur **divi truši vienā būrī
  jau dod** vajadzīgo īpašību.
* Uzdevumā "kāds mazākais skaits jāizvelk, lai noteikti..." atbildei ir
  **divas daļas**: ar $N$ pietiek (Dirihlē) un ar $N-1$ var nepietikt
  (sliktākā gadījuma piemērs).

**1.piemērs:** Katra no $11$ balvām satur $6$ rudens labumus: ābolus,
bumbierus un bietes, katru vismaz vienu. Pamatot, ka divām balvām ir
vienāds saturs.

* *Izpēte:* Būri ir visi iespējamie balvu saturi. Uzraksti tos sistemātiski
  (piem., sakārtojot pēc ābolu skaita). Cik to ir?

<!--
LV.AMO.2024.7.2 — būri ir visi iespējamie komplekti (10 komplekti, 11 balvas).
-->

**2.piemērs:** Dotas deviņas kārtis ar cipariem no $1$ līdz $9$. Kāds
mazākais skaits kāršu jāizvelk (nezinot to vērtības), lai no tām noteikti
varētu izveidot divciparu skaitli, kurš dalās ar $7$ (katru kārti drīkst
izmantot ne vairāk kā vienu reizi)?

* *Pārformulēšana:* Sadali ciparus grupās tā, lai **jebkuri divi** vienas
  grupas cipari veido skaitli, kas dalās ar $7$. Cik grupu sanāk?
* *Atskats:* Vai atbildē ir gan novērtējums, gan piemērs ar par vienu kārti
  mazāk?

<!--
LV.NOL.2021.6.3 — grupas {1,2,4}, {3,5,6}, {8,9}, {7}; atbilde 5; piemērs 1,3,7,8.
-->

**3.piemērs:** Katrs no $28$ klases skolēniem kontroldarbā saņēma atzīmi no
$0$ līdz $10$ ballēm. Pamatot, ka vai nu vismaz $4$ skolēniem ir vienāda
atzīme, vai arī vismaz $4$ skolēni ieguva atzīmi, kas ir augstāka nekā $7$.

* *Saprašana:* Ar $11$ būriem (atzīmēm) nepietiek: $28 \le 3 \cdot 11$. Kā
  samazināt būru skaitu, izmantojot uzdevuma otro iespēju?

<!--
LV.AMO.2024.9.2 — apvieno atzīmes 8, 9, 10 vienā būrī; 28 > 3·9.
-->


---

## 1.uzdevums (LV.NOL.2018.9.2)

Skolas ēdnīcas pusdienu piedāvājumā ir divas dažādas zupas, divi dažādi
pamatēdieni un divi dažādi deserti. Pusdienās aizgāja $30$ vienas klases
skolēni, no katra ēdienu veida (zupa, pamatēdiens, deserts) katrs skolēns
izvēlējās ne vairāk kā vienu ēdienu, pie tam nebija tāda skolēna, kurš neēda
vispār neko. Vai noteikti ir divi skolēni, kas pasūtīja vienu un to pašu?

<!--
3·3·3 − 1 = 26 komplekti < 30 skolēni.
-->


## 2.uzdevums

Pierādīt, ka no jebkuriem astoņiem naturāliem skaitļiem var izvēlēties divus,
kuru starpība dalās ar $7$.

(Klasisks uzdevums; sk. A. Engel. *Problem-Solving Strategies*, Springer,
1998, 4. nodaļa "The Box Principle".)

<!--
Būri — 7 atlikumi, dalot ar 7. Divi skaitļi ar vienādu atlikumu: starpība dalās ar 7.
Turpinājums: vai pietiktu ar septiņiem skaitļiem? (Nē: 1, 2, ..., 7.)
-->


## 3.uzdevums

No skaitļiem $1, 2, 3, \ldots, 20$ izvēlas jebkurus $11$. Pierādīt, ka
starp izvēlētajiem ir divi skaitļi, no kuriem viens dalās ar otru.

(P. Erdős; sk. A. Engel. *Problem-Solving Strategies*, Springer, 1998,
4. nodaļa "The Box Principle".)

<!--
Katru skaitli izsaka kā 2^k · m, kur m nepāra. Būri — 10 nepāra "kodoli"
m = 1, 3, ..., 19. Diviem skaitļiem ar vienādu m mazākais dala lielāko.
Ar 10 skaitļiem nepietiek: 11, 12, ..., 20.
-->
