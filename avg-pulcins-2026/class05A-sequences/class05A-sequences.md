# Skaitļu teorija un virknes (5A: 2025-10-09)

* Dalāmības pazīmes ar $2,4,8,\ldots$: Skaitlis dalās ar $2$, 
  ja pēdējais cipars dalās ar $2$. Skaitlis dalās ar $4$, 
  ja pēdējo divu ciparu veidotais skaitlis dalās ar $4$, utt.
* Dalāmības pazīmes ar $5,25,125,\ldots$: 
  Skaitlis dalās ar $5$, 
  ja pēdējais cipars dalās ar $5$. Skaitlis dalās ar $25$, 
  ja pēdējo divu ciparu veidotais skaitlis dalās ar $25$, utt.
* Dalāmības pazīmes ar $3$ un $9$: Skaitlis dalās ar $3$ vai ar $9$, 
  tad un tikai tad, ja tā ciparu summa dalās ar $3$ vai ar $9$.
* Dalāmības pazīme ar $11$: 
  Skaitlis dalās ar $11$ tad un tikai tad, ja tā ciparu summas, kas atrodas
  nepāra pozīcijās, un ciparu summas, kas atrodas pāra
  pozīcijās, starpība dalās ar $11$. 
  Piemēram, $108647$ dalās ar $11$, jo $(1 + 8 + 4) − (0 + 6 + 7) = 0$
  un $0$ dalās ar $11$.
* Skaitlis $n$ dalās ar divu savstarpēju pirmskaitļu reizinājumu 
  $a \cdot b$ tad un tikai tad, ja $n$ dalās ar $a$ un $n$
  dalās ar $b$. 
* *Rekurentas virknes* ir virknes, kurās kārtējo locekli $a_n$ var 
  izrēķināt no iepriekšējiem locekļiem $a_{n-1}, a_{n_2}$ utt.

**1.uzdevums:** 
Zināms, ka skaitlis $n$ dalās ar $50$, $60$ un $135$.
Cik ir šādu skaitļu intervālā $[1;10000]$? 

**2.uzdevums (LV.AMO.2016.8.3):** 
Zināms, ka skaitlis dalās ar $2016$ un ka visi tā cipari ir dažādi. 
Kāds ir lielākais ciparu skaits, kas var būt šajā skaitlī?

**3.uzdevums (LV.AMO.2019.8.5):** 
Kādai mazākajai naturālai $n$ vērtībai skaitli $10^n$
iespējams izteikt kā sešu naturālu skaitļu reizinājumu tā, ka neviens no tiem 
nav mazāks kā $10$ un to visu pēdējie cipari ir dažādi 
(tas ir, nevienam no tiem pēdējais cipars nesakrīt ar kāda cita skaitļa pēdējo ciparu)?


**4.uzdevums (no gatavošanās materiāla):** 
Kādi cipari var būt burtu $a$ un $b$ vietā, lai piecciparu skaitlis 
$\overline{a543b}$ dalītos ar $36$?

**5.uzdevums (LV.NOL.2012.8.3):** 
Vai naturāla skaitļa ciparu reizinājums var būt skaitlis 
$\overline{aabbcc}$? 
(Pieraksts $\overline{kmn}$ nozīmē, ka skaitļa 
simtu cipars ir $k$, desmitu cipars ir $m$ un vienu cipars ir $n$.)


**6.uzdevums (No gatavošanās materiāla):** 
Rindā salikti 10 krēsli, uz katra no tiem sēž pa skolēnam. 
Skolēni vienu reizi pieceļas un tad apsēžas, 
pie tam katrs drīkst apsēsties vai nu uz sava agrākā krēsla, 
vai uz cita krēsla, kurš ir tieši blakus agrākajam krēslam. Cik
dažādi skolēnu izvietojumi iespējami pēc pārsēšanās?

**7.uzdevums:** Ciparu virknīti sauksim par "labu", ja tajā ir 
pāra skaits nuļļu. Piemēram, "11" vai "0407869" ir labas virknītes, 
bet "0" vai "120987045608" nav labas.  
Ar $a_n$ apzīmējam, cik ir "labu" virkņu ar tieši $n$ cipariem.  
**(A)** Uzrakstīt $a_2$, $a_3$, $a_4$, $a_5$, $a_6$ ar reizināšanas likumu.
**(B)** Atrast rekurentu sakarību virknei $a_n$.  


**8.uzdevums:** Dota josla, kuras izmērs ir $2 \times n$ rūtiņas. 
Ar $a_n$ apzīmē, cik veidos to var pārklāt ar flīzēm, kuru 
izmēri ir vai nu $2 \times 1$ (domino figūras) 
vai arī $2 \times 2$ (kvadrāti).   
**(A)** Izteikt $a_n$ ar *rekurentu sakarību*.  
**(B)** Atrast $a_8$ - cik veidos taisnstūri $2 \times 8$
var pārklāt ar šīm flīzēm.  
**(C)** Pārbaudīt, ka ir spēkā formula $a_n = \frac{2^n - (-1)^n}{3}$.
(Parasti izmantot formulu ir ērtāk, jo katru $a_n$ var izrēķināt tieši, 
neveidojot tabulu.)

**Atrisinājums:**  
**(A)** Ievērosim, ka $a_1 = 1$ (joslu $2 \times 1$ var noklāt ar 1 domino kauliņu un 
nekā citādi). Un $a_2 = 3$ (joslu $2 \times $ var noklāt ar 2 domino kauliņiem 
vertikāli, vai diviem kauliņiem horizontāli vai arī ar vienu kvadrātu). 

Apskatām joslu $2 \times n$, ja $n > 2$. Tad eksistē 3 veidi, kā šajā joslā noklāt, 
piemēram, abas rūtiņas kreisajā joslas galā: 

* Tās var nosegt ar vertikālu domino kauliņu. Tad 
  paliek vēl josla $2 \times (n-1)$, ko var noklāt $a_{n-1}$ dažādos veidos.
* Kreiso apakšējo rūtiņu var nosegt ar horizontālu domino kauliņu, bet tad 
  tai virsū jāliek otrs horizontāls kauliņš. Tad paliek josla $2 \times (n-2)$, 
  ko var noklāt $a_{n-2}$ dažādos veidos. 
* Visbeidzot kreisajā galā esošās rūtiņas var nosegt ar vienu kvadrātiņu. Arī tad
  paliek josla $2 \times (n-2)$, ko var noklāt $a_{n-2}$ dažādos veidos. 

Visus šos variantus saskaitot, iegūstam, ka $a_n = a_{n-1} + a_{n-2} + a_{n-2} = a_{n-1} + 2 \cot a_{n-2}$.  

**(B)** Var izveidot tabuliņu ar $a_n$ vērtībām pie $n \leq 8$: 

| $n$     | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |   
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| $a_n$   | 1    | 3    | 5    | 11   | 21   | 43   | 85   | 171  |

**(C)** Var ievietot dažas vērtības un pārbaudīt, ka $a_n = \frac{2^{n+1} + (-1)^{n+1}}{3}$, 
ja $n=1,2,3$ (*Indukcijas bāze*).  
Lielākiem $n$ apskata divus gadījumus. Ja $n$ ir pāra skaitlis, tad 
jāpārbauda, ka $a_n = \frac{2^{n+1} + 1}$. Ievieto šajā formulā $a_{n-1}$ un $a_{n-2}$
(izdara *induktīvo pieņēmumu, ka šiem locekļiem formula jau izpildās), un tad 
pārbauda ka līdzīga izteiksme ir spēkā arī priekš $a_n$. 
Ja $n$ ir nepāra, tad šo gadījumu apskata līdzīgi.


**9.uzdevums:** Ir uzrakstīta izteiksme ar $n+1$ skaitļiem vai burtiem un 
operāciju $\circ$ (aplītis), kuru raksta starp diviem skaitļiem 
vai divām izteiksmēm, kas liktas iekavās. 
Ar $C_n$ apzīmē atšķirīgo veidu skaitu, kuros var salikt iekavas. 
(Iekavu salikšanas veidus uzskata par atšķirīgiem, ja tie 
izraisa citādu darbību secību.) 
Ievērojam, ka $C_0 = C_1 = 1$ (ja ir tikai viens skaitlis vai arī ir divi skaitļi, 
tad iekavas var salikt tikai vienā veidā).
Bet, piemēram, $C_3 = 5$, jo ir 
pavisam pieci veidi, kā salikt iekavas, ja izteiksmē ir $3$ aplīši:

$$((a \circ b) \circ c) \circ d,\;\; (a \circ (b \circ c)) \circ d,\;\;
(a \circ b) \circ (c \circ d),\;\; a \circ ((b \circ c) \circ d),\;\; 
a \circ (b \circ (c \circ d)).$$

**(A)** Atrast rekurentu sakarību, kā izteikt $C_n$, izmantojot $C_0, C_1, \ldots, C_{n-1}$.  
**(B)** Izveidot tabulu ar vērtībām $C_0,\cdots,C_6$. 

**10.uzdevums:** Monētu met $n$ reizes un katrreiz pieraksta 
rezultātu "C" (cipars) vai "Ģ" (ģerbonis). 
Pirmais spēlētājs uzvar, ja visu metienu virknītē nekad nav 
divi ģerboņi pēc kārtas (virknīte nesatur "ĢĢ").
Apzīmējam ar $a_n$ to, cik ir virknīšu garumā $n$ bez "ĢĢ" 
(jeb cik dažādos veidos 1.spēlētājs var uzvarēt).  
**(A)** Atrast rekurentu sakarību, kas $a_n$ izsaka
ar iepriekšējiem virknes locekļiem.  
**(B)** Atrast varbūtību, ar kuru pirmais spēlētājs uzvar, ja 
monētu met tieši $6$ reizes (par varbūtību saucam 
dalījumu starp to monētas uzmešanas veidu skaitu, kuros uzvar 1.spēlētājs, 
pret visu iespējamo monētu uzmešanas veidu skaitu).



