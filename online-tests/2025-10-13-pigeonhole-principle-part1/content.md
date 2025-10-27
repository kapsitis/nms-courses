---
title: "Dirihlē princips - 1"
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "Dirihlē princips - 1"
---
# Dirihlē princips - 1 {-}

## 1.uzdevums {-}

Tumšā skapī ir zeķes 12 krāsās - pa 20 zeķēm katrā no krāsām. Kāds mazākais zeķu skaits jāizvelk, lai starp tām noteikti atrastos divas zeķes vienādā krāsā?

**Atbilde:** `13`

**Atrisinājums:**  
Izvilktās zeķes ir objekti ("truši"), bet iespējamās krāsas ir grupas ("būri"). 
Tā kā grupu ir tieši $N=12$, tad izvelkot $N+1=13$ zeķes, starp tām noteikti 
būs divas vienādā krāsā. Ar $12$ zeķēm nepietiek, jo var neveikties: katra 
no pirmajām $12$ zeķēm var būt citā krāsā.

## 2.uzdevums {-}

Rūpnīca ražo ķieģeļus, no kuriem neviens nav smagāks par 3kg, neviens nav 
vieglāks par $2.9~\mathrm{kg}$.  Kāds mazākais ķieģeļu skaits jānopērk, 
lai starp tiem noteikti atrastos divi tādi, kuru masu starpība ir mazāka 
par $1~\mathrm{g}$ (masu starpību iegūst, no lielākās masas atņemot mazāko)?

**Atbilde:** `102`

**Atrisinājums:**  
Pārveidojam visas masas gramos. Tad intervālu $[2900;3000]$ var pārklāt 
ar $101$ maziem intervāliem $[2900.0;2900.5)$, $[2900.5;2901.5)$, 
$[2901.5;2902.5)$, utt., $[2999.5;3000.0]$. Katram intervālam, izņemot 
pēdējo, pieder kreisais galapunkts, bet nepieder labais galapunkts (ar apaļo iekavu). 

Ja izraudzīti jebkādi $102$ ķieģeļi, tad vismaz vienā no intervāliem 
nonāks divi ķieģeļi. Tā kā jebkurš intervāls (izņemot pirmo un pēdējo, 
kuri ir vēl īsāki) ir ar garumu $1$ un nesatur vienu galapunktu, 
tad abu ķieģeļu masu starpība būs mazāka par $1$ gramu. 

Ja izvēlas tieši 101 ķieģeļus, tad var ņemt $2900$, $2901$, utt. 
līdz $3000$. (Visas masu atšķirības ir tieši 1 grams.)

## 3.uzdevums {-}

Kāds mazākais skaits no astoņiem naturāliem skaitļiem $1,2,3,4,5,6,7,8$ 
jāizsvītro, lai starp palikušajiem skaitļiem neatrastos tādi divi, 
kuru summa ir $9$?

**Atbilde:** `4`

**Atrisinājums:**  
Ir pavisam $4$ "būrīši" 
$((1,8), (2,7), (3,6), (4,5))$, kuros esošie skaitļu pāri dod summā $9$. 
Izsvītrojot no katra vienu ir pietiekami. Ja svītro mazāk, 
tad paliek pāri būrītis ar diviem skaitļiem, kuri summā dod $9$.


## 4.uzdevums {-}

Uz galda ir $15$ spēļu kārtis. Pīķi ($\spadesuit$) un kreici ($\clubsuit$) 
ir melni; erci ($\heartsuit$) un kāravi ($\diamondsuit$) ir sarkani.  
Kāds lielākais skaits no $15$ kārtīm noteikti ir vienā krāsā?

**Atbilde:** `8`

**Atrisinājums:**  
Ja tikai septiņas būtu katrā no krāsām, tad to 
kopskaits nevarētu pārsniegt $2 \cdot 7=14$.  
Tāpēc vismaz 8 ir vienādā krāsā (nav zināms kādā). 

Nav obligāti, lai lielāks skaits būtu vienādā krāsā, jo var būt $8$ kārtis 
vienā krāsā, bet $7$ kārtis - otrā krāsā.


## 5.uzdevums {-}

Tumšā skapī ir 100 melnas, 100 zilas un 100 zaļas zeķes. Kāds mazākais skaits zeķu neskatoties ir jāizvelk, lai noteikti starp tām būtu divas melnas vai divas zilas zeķes?

**Atbilde:** `103`

**Atrisinājums:**  
Ar 102 izvilktām zeķēm nepietiek, jo var gadīties 100 zaļas,
viena melna un viena zila. Ar 103 izvilktām zeķēm vienmēr pietiek, jo vismaz 3 no tām nebūs zaļas un varēs lietot Dirihlē principu - jebkādi piekārtojot 3 zeķes divām krāsām,  divas no zeķēm nonāks vienā krāsā.


## 6.uzdevums {-}

Uz galda novietotas ļoti daudzas kartītes.  Uz katras kartītes rakstīta kāda 3-burtu virkne, kas satur burtus "A" un "B".  (Virknē vienādi burti drīkst atrasties blakus, piemēram, "AAA" vai "BBA"). Cik kartītes jāpaņem, lai uz divām no tām noteikti būtu divas vienādas virknītes.

**Atbilde:** `9`

**Atrisinājums:**  
Ir pavisam $8$ dažādas $3$ burtu virknītes. Paņemot 9 kartītes, vismaz viena no virknītēm atkārtosies.


## 7.uzdevums {-}

Sporta zālē ir 10 gari soli, uz kuriem kaut kā jau sasēdušās 100 meitenes. Kādu lielāko skaitu zēnu var sasēdināt šajā auditorijā, ja nekādi divi zēni nedrīkst sēdēt blakus?

**Atbilde:** `110`

**Atrisinājums:**  
Pirms meitenēm zālē bija $10$ "būrīši" (katrs no soliem), bet katras meitenes 
nosēdināšana "būrīšu" skaitu palielina par $1$ (pārdalot solu vai tā posmu 
divās daļās). Tādēļ būrīšu ir pavisam $110$. Lai nevienā būrītī nonāktu 
ne vairāk par vienu zēnu, to skaits nevar pārsniegt $110$.

$110$ zēnus var sasēdināt. Piemēram, var uz viena sola nosēdināt $11$ zēnus
un 10 meitenes: $(Z,M,Z,M,\ldots,M,Z,M,Z)$


## 8.uzdevums {-}

Makā ir 25 monētas. Monētu iespējamās vērtības ir $1,2,5,10,20,50$ centi 
kā arī $1$ eiro un $2$ eiro.  Kāds ir lielākais skaits vienādas vērtības 
monētu, ko no šī maka noteikti var izņemt?

**Atbilde:** `4`

**Atrisinājums:**  
Ja nebūtu vismaz $4$ monētas ar vienādu vērtību (vienalga kādas 
vērtības), tad to kopskaits nevarētu pārsniegt $3 \cdot 8=24$, jo ir tikai 
$8$ dažādu veidu monētas un no katra veida drīkst ņemt ne vairāk kā $3$.


## 9.uzdevums {-}

Auto dīlerim ir $20$ Audi, $20$ BMW, $20$ VW un $20$ Volvo automašīnas. 
Kāds mazākais mašīnu skaits jānopērk, lai varētu apgalvot, 
ka ir nopirktas vismaz piecas vienas markas automašīnas?

**Atbilde:** `17`

**Atrisinājums:**  
Ja nopirktas tikai $16$ mašīnas, tad var būt pa četrām no katras markas. 
Ja nopirktas 17 mašīnas, tad nevar gadīties, ka no katras markas 
nopirktas mazāk kā piecas, jo $4 \cdot 4<17$. 

## 10.uzdevums {-}

Tortes dekorēšanai nepieciešami vai nu divi apelsīni, vai trīs āboli, 
vai piecas aprikozes, vai septiņi ķirši. Mazā Mija atnesa no veikala 
$n$ augļus, katrs no tiem ir vai nu apelsīns, ābols, aprikoze vai ķirsis.

Kādam mazākajam n ar atnestajiem augļiem noteikti pietiek tortes dekorēšanai?

**Atbilde:** `14`

**Atrisinājums:**  
Skaits $n=(2−1)+(3−1)+(5−1)+(7−1)=2+3+5+7−4=13$ ir vislielākais, 
kuram var atnest augļus tā, lai katram no četriem paveidiem viens 
pietrūktu. Ja atnesīs par vienu vairāk, t.i. $14$, tad vismaz 
vienam paveidam tiks sasniegts vajadzīgais skaits.

