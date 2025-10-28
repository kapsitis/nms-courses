---
title: "Skaitļu teorija: Dalāmība - 1"
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "Skaitļu teorija: Dalāmība - 1"
header-includes:
  - |
    \makeatletter
    \RedeclareSectionCommand[
      beforeskip=1.2ex plus 0.4ex minus 0.2ex,
      afterskip=0.4ex plus 0.2ex minus 0.2ex
    ]{subsection}
    \makeatother
---
# Skaitļu teorija: Dalāmība - 1 {}

## 1.uzdevums {-}

Cik daudzi pozitīvi trīsciparu skaitļi dalās gan ar 11, gan ar 5? 

**Atbilde:** `17`

<!--
Sal. [AOPS.INT.1.1](AOPS.INT.1.1)
-->

**Atrisinājums:**  
Ar $11$ un ar $5$ dalās visi tie skaitļi, kas dalās ar $11 \cdot 5 = 55$, 
jo $11$ un $5$ ir savstarpēji pirmskaitļi.  
Mazākais trīsciparu skaitlis, kas dalās ar $55$ ir $2 \cdot 55 = 110$, 
bet lielākais šāds skaitlis ir $18 \cdot 55 = 990$.  
Tātad $55$ var reizināt ar jebko intervālā $[2;18]$, lai iegūtu trīsciparu 
skaitli. Šādu reizinājumu būs $18 -2 + 1=17$. 


## 2.uzdevums {-}

Kurš ir mazākais pozitīvais skaitļa 25 daudzkārtnis, kura ciparu reizinājums 
arī ir pozitīvs skaitļa 25 daudzkārtnis?  
(*Piezīme:* Par skaitļa $25$ *daudzkārtni* sauc skaitli, kas dalās ar $25$.)

**Atbilde:** `525`

<!--
Sal. [AOPS.INT.1.2](AOPS.INT.1.2)
-->

**Atrisinājums:**  
Skaitļi, kuri dalās ar $25$, var beigties ar cipariem "00", 
"25", "50" vai "75". (Mums neder "00" un "50", jo tad 
ciparu reizinājums ir "0", kas nav pozitīvs.)

Ja skaitlis beidzas ar cipariem "25", tad tam vajag vēl vismaz 
vienu ciparu, kas dalās ar $5$, lai reizinājums dalītos ar $5 \cdot 5= 25$. 
Tāds ir skaitlis $525$.  
(Līdzīgi der arī $575$, bet $525$ ir mazākais.)


## 3.uzdevums {-}

Atrast mazāko naturālo skaitli, kas ir skaitļa $120$ dalītājs, 
bet nav skaitļa $300$ dalītājs. 

**Atbilde:** `8`

**Atrisinājums:**  
Sadalām abus pirmreizinātājos: $120 = 2^3 \cdot 3 \cdot 5$ un 
$300 = 2^2 \cdot 3 \cdot 5^2$.  
Skaitlī $300$ visi pirmreizinātāji ir ar lielākām pakāpēm, izņemot, 
divnieka pakāpi (jo $120$ dalās ar $2^3 = 8$, bet $300$ dalās tikai 
ar $2^2 = 4$). 

Iegūstam, ka mazākais skaitlis, kas dala $120$, bet ne $300$ ir $8$.



## 4.uzdevums {-}

Visi skaitļa $175$ pozitīvie dalītāji, izņemot $1$, ir izrakstīti pa apli tā, 
ka jebkuriem diviem skaitļiem blakus uz apļa ir kopīgs reizinātājs, 
kas lielāks par $1$. Kāda ir summa abiem skaitļiem, kuri uzrakstīti blakus skaitlim $7$?

**Atbilde:** `210`

<!--
Sal. [AOPS.INT.1.4](AOPS.INT.1.4)
-->

**Atrisinājums:**  
Lai kādam skaitlim būtu kopīgs reizinātājs ar $7$ (kas lielāks par $1$), pašam 
skaitlim ir jādalās ar $7$, jo $7$ ir pirmskaitlis un citu reizinātāju, izņemot 
sevi, viņam nav. 

Ar $7$ dalās vēl vienīgi $7 \cdot 5 = 35$ un $7 \cdot 25 = 175$, 
jo skaitlim $175 = 5^2 \cdot 7$ ir pavisam seši dalītāji ($1,5,7,35,35,175$)
un tikai trīs no tiem satur pirmreizinātāju $7$.  
Iegūstam, ka skaitlim $7$ blakus uzrakstīto skaitļu summa ir $175+35 = 210$. 



## 5.uzdevums {-}

Orķestrī spēlē $72$ skolēni, kuri visi soļos dziesmu svētku gājienā. 
Viņiem jāsoļo rindās -- ar vienādu skolēnu skaitu katrā rindā. 
Vienā rindā jābūt no $5$  līdz $20$ skolēniem. 
Cik dažādus rindu garumus orķestra dalībnieki var izveidot?

**Atbilde:** `5`

<!--
Sal. [AOPS.INT.1.5](AOPS.INT.1.5)
-->

**Atrisinājums:**  
Skaitlim $72 = 2^3 \cdot 3^2$ ir pavisam $(3+1)(2+1) = 12$ dažādi pozitīvi dalītāji -- 
tie ir visi skaitļi formā $2^a \cdot 3^b$, kur $a \leq 3$ un $b \leq 2$.

Starp visiem divpadsmit skaitļa $72$ dalītājiem pirmie seši ir "mazie" dalītāji: $1,2,3,4,6,8$.   
Atlikušie seši ir "lielie" dalītāji (ko iegūst $72$ izdalot ar kādu no "mazajiem"): $72, 36, 24, 18, 12, 9$. 

Starp visiem šiem dalītājiem ir tikai $6,8,9,12,18$ ir tādi, kas atrodas intervālā $[5;20]$. 
Tāpēc var izveidot piecus dažādus rindu garumus.


## 6.uzdevums {-}

Pieņemsim, ka $a$ un $b$ ir veseli pozitīvi skaitļi, kur skaitlim $a$ 
ir 3 pozitīvi dalītāji, bet skaitlim $b$ ir $a$ pozitīvi dalītāji. 
Ja $b$ dalās ar $a$, tad kāda var būt skaitļa $b$ mazākā iespējamā vērtība? 

**Atbilde:** `8`

<!--
AOPS.INT.1.6
-->

**Atrisinājums:**  
Ja skaitlim $a$ ir $3$ dažādi dalītāji, tad tas ir kāda pirmskaitļa kvadrāts $p^2$
(dalītāji ir $1, p, p^2$). Mazākais šāds skaitlis ir $2^2 = 4$.  
Tālāk jāatrod skaitlis, kuram ir tieši $4$ dažādi dalītāji un kurš dalās ar $4$. 

Tas nevar būt $2$ reizinājums ar kādu citu pirmskaitli (piemēram $2 \cdot 3 = 6$), 
jo tādam ir četri dalītāji, bet tas nedalās ar $4$. 
Vienīgā iespēja ir izvēlēties $b$ kā divnieka pakāpi: $b = 2^3 = 8$. 
Šim skaitlim ir četri dalītāji ($1,2,4,8$) un tas dalās ar $4$. 




## 7.uzdevums {-}

Kāds ir lielākais veselais skaitlis, ar kuru dalās jebkuru trīs 
pēc kārtas sekojošu naturālu skaitļu reizinājums?

**Atbilde:** `6`

<!--
Sal. [AOPS.INT.1.7](AOPS.INT.1.7)
-->

**Atrisinājums:**  
Šāds skaitlis ir $6$. Lielāka šāda skaitļa nav, jo trīs pēc 
kārtas sekojošu naturālu skaitļu reizinājums $1 \cdot 2 \cdot 3 = 6$ 
nedalās ne ar kādu lielāku skaitli. 

Kāpēc arī katrs cits reizinājums $n \cdot (n+1) \cdot (n+2)$ dalās ar $6$? 
Starp skaitļiem $n, n+1, n+2$ viens vai divi ir pāra skaitļi, tāpēc 
reizinājums noteikti dalās ar $2$.  
Un arī starp skaitļiem $n,n+1,n+2$, kuri seko pēc kārtas, tieši viens dalās ar $3$.
Tāpēc reizinājums dalās arī $3$. 

Ja skaitlis dalās ar $2$ un ar $3$, tad tas dalās ar $6$. 



## 8.uzdevums {-}

Naturāli skaitļi $A$, $B$, $A-B$ un $A+B$ visi ir pirmskaitļi. 
Atrast šo četru pirmskaitļu summu. 

**Atbilde:** `17`

<!--
Sal. [AOPS.INT.1.8](AOPS.INT.1.8)
-->

**Atrisinājums:**  
Skaitļi $A-B$, $A$, $A+B$ veido aritmētisku progresiju. 
Tā kā visi pirmskaitļi (izņemot pašu mazāko) ir nepāra skaitļi, 
tad $A$ un $A+B$ abi ir nepāra skaitļi. Tādēļ to starpība $B$ ir 
pāra skaitlis un tas var būt vienīgi $B=2$. 

Vienīgā aritmētiskā progresija no trim pirmskaitļiem ar diferenci $2$
ir $3, 5, 7$. (Neviena cita nevar būt, jo tieši viens skaitlis šādā 
progresijā dalās ar $3$ -- un vienīgais pirmskaitlis, kurš var dalīties ar $3$ 
ir pats $3$.) Esam ieguvuši, ka progresijas vidējais loceklis ir $A=5$. 

Esam ieguvuši, ka $A=5$, $B=2$, $A-B=3$, $A+B=7$. To summa ir $17$. 



## 9.uzdevums {-}

Ar $m$ un $n$ apzīmējam attiecīgi lielāko un mazāko skaitļa $7$ 
daudzkārtni starp visiem trīsciparu skaitļiem. 
Kāda ir $m + n$ vērtība?  
(*Piezīme:* Par skaitļa $7$ *daudzkārtni* sauc skaitli, kas dalās ar $7$.)

**Atbilde:** `1099`

<!--
Sal. [AOPS.INT.1.9](AOPS.INT.1.9)
-->

**Atrisinājums:**  
Mazākais trīsciparu daudzkārtnis skaitlim $7$ ir $105 = 15 \cdot 7$, bet
lielākais trīsciparu daudzkārtnis ir $994 = 142 \cdot 7$. 
To summa ir $105 + 994 = 1099$.  


## 10.uzdevums {-}

Pirms priekšnesuma $105$ orķestra dalībnieki sastājās "Taisnstūrī $A$" 
(visās rindās vienāds skaits dalībnieku). 
Pēc tam viņi pārkārtojās "Taisnstūrī $B$", kam rindu ir par $6$ vairāk, 
bet katrā no rindām ir par diviem dalībniekiem mazāk. 
Cik rindu ir "Taisnstūrī $A$"? 

**Atbilde:** `15`

<!--
Sal. [AOPS.INT.1.10](AOPS.INT.1.10)
-->

**Atrisinājums:**  
Sadalām $105$ pirmreizinātājos: $105 = 3 \cdot 5 \cdot 7$. 
No skaitļiem $3$, $5$ un $7$ (un to savstarpējiem reizinājumiem) var iegūt visus 
$105$ dalītājus. Izrakstīsim visus šos dalītājus:

$$1,\; 3,\; 5,\; 7,\; 15,\; 21,\; 35,\; 105.$$

Vienīgie divi dalītāji, kuri atšķiras par $6$ ir $15$ un $21$. 
Tāpēc taisnstūrī $A$ bija $15$ rindas (pa $7$ dalībniekiem katrā), 
bet taisnstūrī $B$ bija $21$ rindas (pa $5$ dalībniekiem katrā).

