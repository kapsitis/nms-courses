---
title: Pārskats
date: "December 15, 2017"
output: pdf_document
---


```r
id
```

```
## [1] "000001"
```



# Algebriskas metodes skaitļu teorijā

* **Anotācija:** Tests par mainīgo apzīmējumu un algebras metožu izmantošanu skaitļu teorijas uzdevumos.
* **Pēdējās izmaiņas:** 2017-12-12

**nt-R4.q1:** <!--questionType=INPUT|length=5--> Kāds ir mazākais skaitlis, kas dod atlikumu $8$, dalot ar $9$, bet šī skaitļa ciparu summa ir lielāka nekā $8$?

**Atbilde:** `89`

**Skaidrojums:** Saskaņā ar skaitļa $9$ dalāmības pazīmi, atlikumu $8$ dalot ar $9$ dod tie skaitļi $n$, 
kuru ciparu summa $S(n)$ dod atlikumu $8$ dalot ar $9$. Tātad $S(n)$ var būt $8, 17, 26,\ldots$. 
Pēc uzdevuma nosacījuma $S(n)$ nevar būt $8$. Mazākā iespējamā ciparu summa ir $17$. To var iegūt 
kā divciparu skaitli divos veidos: $8 + 9$ vai $9 + 8$ (t.i. $89$ un $98$). 
Mazākais no šiem skaitļiem ir $89$.  

**nt-R4.q2:** <!--questionType=INPUT|length=15--> Kāds ir mazākais skaitlis $n$, kura ciparu summa $S(n)=89$?

**Atbilde:** `8999999999`

**Daļējs kredīts:** Ja atbilde ir 10-ciparu skaitlis ar ciparu summu $89$, bet nav mazākais iespējamais.  
<!--"""[0-9]{10}""".r|"""9*89*""".r-->

**Skaidrojums:** Skaitli $89$ var iegūt kā ciparu summu ļoti daudzos veido. Ar deviņiem cipariem nepietiek
(pat ja visi tie ir deviņnieki, tad $9 \cdot 9$ ir tikai $81$). 
Ar desmit cipariem var: jāizmanto deviņi cipari "9" un viens cipars "8". Mazākais no šiem skaitļiem būs tas, 
kur cipars "8" ir pašā sākumā: $8999999999$. 


**nt-R4.q3:** <!--questionType=INPUT|length=20--> Naturāliem $n$ lielākais kopīgais dalītājs ar $50$: 
$\operatorname{gcd}(n,50)$ var pieņemt dažādas vērtības. Uzrakstīt, kuras tās ir.  
(**Norāde:** *Ierakstīt visas iespējamās lielākā kopīgā dalītāja vērtības, atdalot ar komatiem. Secība nav svarīga.*)

**Atbilde:** `1,2,5,10,25,50`

**Skaidrojums:** Lai skaitlis $x$ būtu lielākais kopīgais dalītājs skaitļiem $n$ un $50$, tam jābūt skaitļa $50$ 
dalītājam. Skaitlim $50 = 2 \cdot 5^2$ ir tieši seši dalītāji ($1,2,5,10,25,50$) - tie iegūstami kā 
dažādas kombinācijas pakāpju reizinājumiem $2^a \cdot 5^b$, kur $a = 0,1$ un $b = 0,1,2$ (t.i. $a$ divas 
vērtības kombinējot ar $b$ trim vērtībām iegūstam sešas kombinācijas).  
Acīmredzot, visas šīs vērtības ir iegūstamas. Piemēram, ja $n=10$, tad $\operatorname(10,25) = 10$. 


**nt-R4.q4:** <!--questionType=INPUT|length=5--> Kāds ir lielākais kopīgais dalītājs visiem četrciparu palindromiem?  
(Par palindromiem sauc skaitļus, kurus vienādi lasa no abiem galiem, piemēram '1001')  
(**Norāde:** Ierakstīt veselu pozitīvu skaitli.)

**Atbilde:** `11`

**Skaidrojums:** Aplūkosim divus pēc kārtas sekojošus četriciparu palindromus $1001$ un $1111$. 
Atradīsim to lielāko kopīgo dalītāju. Pēc Eiklīda algoritma: 
$$\operatorname{gcd}(1001,1111) = \operatorname{gcd}(1111-1001,1001) = \operatorname{gcd}(110,1001) = $$
$$ = \operatorname{gcd}(1001 - 9 \cdot 110, 110) = \operatorname{gcd}(11,110) = 11. $$
Ja visi četrciparu palindromi dalās ar $11$, tad visu šo palindromu lielākais kopīgais dalītājs ir $11$
un nevar būt lielāks, jo $1001$ un $1111$ abi dalās tikai ar $11$. Ja 
turpretī ir daži palindromi, kas ar $11$ nedalās, tad lielākais kopīgais dalītājs var būt tikai $1$.  
Varam viegli pārliecināties, ka visi palindromi dalās ar $11$, jo katram četrciparu skaitlim $\overline{abba}$:
$$ \overline{abba} = 1001 \cdot a + 110 \cdot b = 11 \cdot (91 \cdot a + 10 \cdot b). $$


**nt-R4.q5:** <!--questionType=MC--> Atrast algebrisku izteiksmi, kur mainīgajiem piešķirot 
naturālas vērtības, iegūsim sekojošu skaitļu kopu:  
$A$: 'Visi 6-ciparu skaitļi, kuru decimālpierakstā 3-ciparu grupa divreiz atkārtojas'. 

a. $6n \pm 1$,
b. $2^m \cdot 3^n$, kur $m \leq 4$, $n \leq 2$,
c. $10n+1$,
d. $2^n$,
e. $1001 \cdot n$, kur $n \in [100; 999]$,
f. $11n$; kur $n \geq 6$.

**Skaidrojums:** Apzīmējam sešciparu skaitli $\overline{abcabc}$, kur "a", "b", "c" ir pirmie trīs cipari. 
Tad skaitli var izteikt kā desmitnieka pakāpju summu:  
$$ \overline{abcabc} = 100000a + 10000b + 1000c + 100a + 10b + c = 1001 \cdot 100a + 1001 \cdot 10b + 1001c = 1001 \cdot \overline{abc}.$$
Ja skaitlis $\overline{abc}$ ir lielāks par $999$ vai mazāks par $100$, tad tas nav trīsciparu skaitlis (un 
to atkārtojot divas reizes neiegūsim sešciparu skaitli).   
Ievietojot $n$ vietā $100, 101, 102, \ldots$, iegūsim $100100$, $101101$, $102102$ utml., kas arī ir visi 
sešciparu skaitļi, kuros ciparu grupa divreiz atkārtojas.


**nt-R4.q6:** <!--questionType=MC--> Atrast algebrisku izteiksmi, kur mainīgajiem 
piešķirot naturālas vērtības, iegūsim sekojošu skaitļu kopu:  
$B$: 'Skaitļi, kam pēdējais cipars ir $1$'.

a. $6n \pm 1$,
b. $2^m \cdot 3^n$, kur $m \leq 4$, $n \leq 2$,
c. $10n+1$,
d. $2^n$,
e. $1001 \cdot n$, kur $n \in [100; 999]$,
f. $11n$; kur $n \geq 6$.

**Atbilde:** `c`

**Skaidrojums:** Skaitļa decimālpierakstā pēdējais cipars apzīmē atlikumu, dalot ar $10$. Tādēļ 
skaitlis, kura pieraksts beidzas ar $1$, ir izsakāms $10n+1$. 


**nt-R4.q7:** <!--questionType=MC--> Atrast algebrisku izteiksmi, kur mainīgajiem piešķirot naturālas vērtības, iegūsim sekojošu skaitļu kopu:  
$C$: 'Visi skaitļa $144$ pozitīvie dalītāji'.

a. $6n \pm 1$,
b. $2^m \cdot 3^n$, kur $m \leq 4$, $n \leq 2$,
c. $10n+1$,
d. $2^n$,
e. $1001 \cdot n$, kur $n \in [100; 999]$,
f. $11n$; kur $n \geq 6$.

**Atbilde:** `b`

**Skaidrojums:** Skaitļa $144$ dalījums pirmreizinātājos: $144 = 2^4 \cdot 3^2$. Lai skaitlis $d$ 
būtu $144$ dalītājs ir nepieciešami un pietiekami, lai $d$ saturētu tikai pirmreizinātājus $2$ un $3$, turklāt
pakāpes nepārsniegtu tās pakāpes, kuras ir skaitlī $144$ (t.i. attiecīgi $2^4$ un $3^2$). 
Tādēļ $d = 2^m \cdot 3^n$, kur $0 \leq m \leq 4$ un $0 \leq n \leq 2$" (t.i. ir pavisam $5 \cdot 3 = 15$ 
kombinācijas $(m,n)$, kas atbilst visiem $144$ dalītājiem). 


**nt-R4.q8:** <!--questionType=MC--> Atrast algebrisku izteiksmi, kur mainīgajiem piešķirot 
naturālas vērtības, iegūsim sekojošu skaitļu kopu:  
$D$: 'Naturāli skaitļi, kam nav kopīgu dalītāju ar $6$, izņemot $1$'. 

a. $6n \pm 1$,
b. $2^m \cdot 3^n$, kur $m \leq 4$, $n \leq 2$,
c. $10n+1$,
d. $2^n$,
e. $1001 \cdot n$, kur $n \in [100; 999]$,
f. $11n$; kur $n \geq 6$.

**Atbilde:** `a`

**Skaidrojums:** Naturāli skaitļi, kuriem nav kopīgu dalītāju ar $6$ ir sekojoši: $1,5,7,11,13,17,\ldots$. 
Šie skaitļi veido divas aritmētiskas progresijas (abas ar diferenci $d = 6$) - viena satur skaitļus $1,7,13,19,\ldots$, 
kuri dod atlikumu $1$, dalot ar $6$, bet otra satur skaitļus $5,11,17,\ldots$, kuri dod atlikumu $5$, dalot ar $6$. 
Abas šīs skaitļu virknes var īsi pierakstīt kā $6n \pm 1$ (t.i. skaitļa $6$ daudzkārtņiem $6n$ pieskaita vai atņem vieninieku). 

**nt-R4.q9:**  <!--questionType=MC--> Atrast algebrisku izteiksmi, kur mainīgajiem piešķirot naturālas vērtības, 
iegūsim sekojošu skaitļu kopu:  
$E$: '11 pēc kārtas ņemtu naturālu skaitļu summa'.

a. $6n \pm 1$,
b. $2^m \cdot 3^n$, kur $m \leq 4$, $n \leq 2$,
c. $10n+1$,
d. $2^n$,
e. $1001 \cdot n$, kur $n \in [100; 999]$,
f. $11n$; kur $n \geq 6$.

**Atbilde:** `f`

**Skaidrojums:** Aritmētiskai progresijai $a_1,\ldots,a_n$ summas formula ir  
$$ S_n = a_1 + a_2 + \ldots + a_n = \frac{a_1 + a_n}{2}\cdot n, $$
kur $a_1$ un $a_n$ ir pirmais un pēdējais progresijas loceklis, bet $n$ - saskaitīto locekļu skaits. 
Tā kā $11$ ir nepāru skaitlis, tad $a_1$ un $a_{11}$ abi ir pāru (vai abi ir nepāru), 
un to aritmētiskais vidējais būs vesels skaitlis, kurš nevar būt mazāks par $(1+11)/2 = 6$. 
Savukārt reizinātājs $n$ summas formulā nozīmē, ka $S_n$ vienmēr dalīsies ar $n=11$. 
Tādēļ $11$ pēc kārtas ņemtu naturālu skaitļu summa būs $11n$, kur $n \geq 6$.  
Viegli pamanīt, ka jebkuru skaitli $11n$ var izteikt kā $11$ pēc kārtas ņemtu 
naturālu skaitļu summu, ja to progresijas vidējais loceklis $n = (a_1 + a_{11})/2$ vienāds ar $n$. 

**nt-R4.q10:**  <!--questionType=MC--> Atrast algebrisku izteiksmi, kur mainīgajiem piešķirot naturālas vērtības, 
iegūsim sekojošu skaitļu kopu:  
$F$: 'Skaitļi, kam nav nepāru dalītāju, izņemot $1$'. 

a. $6n \pm 1$,
b. $2^m \cdot 3^n$, kur $m \leq 4$, $n \leq 2$,
c. $10n+1$,
d. $2^n$,
e. $1001 \cdot n$, kur $n \in [100; 999]$,
f. $11n$; kur $n \geq 6$.

**Atbilde:** `d`

**Atbilde:** Ja skaitļa $N$ dalījumā pirmreizinātājos ir kaut viens pirmskaitlis $p \neq 2$, tad tas arī 
ir skaitļa nepāru dalītājs, kas lielāks par $1$. Tātad skaitlim nevar būt nepāru pirmreizinātāju, un 
vienīgais pāru pirmreizinātājs ir $2$. Tātad skaitlis $N$ izsakāms kā divnieka pakāpe $2^n$. 






# Dirihlē princips

* **Anotācija:** Tests par Dirihlē principu.
* **Pēdējās izmaiņas:** 2017-12-12


**nt-R5.q1:** <!--questionType=MC--> Makā ir $25$ monētas (eiro vai centu). Vai makā noteikti ir vismaz $4$ 
vienādas vērtības monētas?

a. true
b. false

**Atbilde:** `a`

**Skaidrojums:** Pavisam ir astoņu vērtību monētas $1,2,5,10,20,50$ centu, $1$ un $2$ eiro.
No pretējā: Ja nebūtu vismaz $4$ monētu ar vienādu vērtību (vienalga kādas vērtības), tad
varētu būt ne vairāk kā $3$ monētu katrai no astoņām vērtībām, t.i. to kopskaits nevarētu 
pārsniegt $3 \cdot 8 = 24$. 




**nt-R5.q2:** <!--questionType=MC--> Autobusā brauc $50$ cilvēki. Vai var apgalvot, ka vismaz $6$ 
no tiem dzimuši vienā mēnesī?

a. true
b. false

**Atbilde:** `b`

**Skaidrojums:** Tā kā ir pavisam $12$ mēneši, var gadīties, ka katrā no tiem dzimuši $4$ vai $5$ cilvēki 
no autobusā klātesošajiem (desmit mēnešos dzimuši $4$, bet divos mēnešos dzimuši $5$). 
Tad $50 = 10 \cdot 4 + 2 \cdot 5$. Šajā gadījumā nebūs neviena mēneša, kurā dzimuši vismaz $6$ cilvēki. 


**nt-R5.q3:** <!--questionType=INPUT|length=5--> Auto dīlerim ir $20$ Audi, $20$ BMW, $20$ VW un $20$ Volvo 
automašīnas. Kāds mazākais mašīnu skaits jānopērk, lai varētu apgalvot, ka ir nopirktas vismaz piecas vienas markas automašīnas?

**Atbilde:** `17`

**Skaidrojums:** Ja nopirktas tikai $16$ mašīnas, tad var būt pa četrām no katras markas. 
Ja nopirktas $17$ mašīnas, tad nevar gadīties, ka no katras markas nopirktas mazāk kā piecas, jo 
$4 \cdot 4 < 17$. 


**nt-R5.q4** <!--questionType=INPUT|length=5--> Kāds ir mazākais skaits skolēnu, kam jābūt klasē,
lai varētu apgalvot, ka vismaz 5 no tiem ir dzimuši vienā nedēļas dienā?
(**Norāde:** *Ierakstīt veselu pozitīvu skaitli.*)

**Atbilde:** `29`

**Skaidrojums:** Ja skolēnu ir $28$, tad katrā no septiņām nedēļas dienām var būt dzimuši tikai $4$ skolēni. 
Ja skolēnu ir $29$, tad nevar gadīties, ka katrā nedēļas dienā dzimuši mazāk kā $5$ skolēni, jo 
$7 \cdot 4 < 29$. 


**nt-R5.q5:** <!--questionType=INPUT|length=5--> Uz galda ir $15$ spēļu kārtis. 
Kāds lielākais skaits no tām noteikti ir vienā krāsā?
(**Norāde:** *Ierakstīt veselu pozitīvu skaitli.*)

**Atbilde:** `8`

**Skaidrojums:** Spēļu kārtīm ir divas krāsas (melna un sarkana). Ja tikai septiņas būtu katrā no krāsām, 
tad to kopskaits nevarētu pārsniegt $2 \cdot 7 = 14$. Tāpēc vismaz $8$ ir vienādā krāsā (nav zināms kādā). 
Nav obligāti, lai lielāks skaits būtu vienādā krāsā, jo var būt $8$ kārtis vienā krāsā, bet $7$ kārtis - otrā krāsā.



**nt-R5.q6** <!--questionType=INPUT|length=5--> Kāds ir mazākais skaits skolēnu, kam jābūt skolā,
lai divi no tiem noteikti būtu dzimuši vienā datumā (dd.mm). Arī tikai 
garajos gados esošie datumi (29.februāris) ir iespējami. 
(**Norāde:** *Ierakstīt veselu pozitīvu skaitli.*)

**Atbilde:** `367`

**Skaidrojums:** Garajos gados ir $366$ datumi (parastajos gados $365$ datumi). 
Ja skolēnu skaits būs $367 > 366$, tad noteikti kāds no datumiem atkārtosies, jo 
katram skolēnam nevarēs iedot "savu" datumu. Ja skolēnu ir tikai $366$, tad 
var gadīties, ka katrs dzimis citā datumā. 



**nt-R5.q7:** <!--questionType=MC--> Taisnstūrim $ABCD$ ir šāda īpašība: ja to pārgriež pa nogriezni, 
kas savieno tā garāko malu viduspunktus iegūst divus vienādus taisnstūrus, 
kas abi līdzīgi $ABCD$. Kāda ir $ABCD$ garākās un īsākās malas attiecība?

a. $2/1$,
b. $\sqrt{2}/1$,
c. $\frac{\sqrt{5}+1}{2}$,
d. $3/2$.

**Atbilde:** `b`

**Skaidrojums:** Ja $AB$ un $CD$ ir garākās malas, apzīmēsim to viduspunktus ar $M$ un $N$. 
Sākotnējā taisnstūrī garākās un īsākās malas attiecība ir $AB/AD$. Pēc pārgriešanas
uz pusēm iegūtajā taisnstūrī $AMND$ malu attiecība ir $AD/AM$. Tā kā $AM = 0.5 \cdot AB$, tad
$$ \frac{AB}{AD} = \frac{AD}{AM} = \frac{AD}{0.5 \cdot AB} = \frac{2AD}{AB}.$$
Apzīmēsim $x=\frac{AB}{AD}$, tad $x = 2/x$ jeb $x^2 =2$. Tādēļ $x = \sqrt{2}$. 



**nt-R5.q8:** <!--questionType=MC--> Taisnstūrim $ABCD$ ir šāda īpašība: ja tam nogriež kvadrātu, 
kura malas garums vienāds ar $ABCD$ īsākās malas garumu, tad paliek pāri taisnstūris, kurš līdzīgs $ABCD$. 
Kāda ir $ABCD$ garākās un īsākās malas attiecība?

a. $2/1$,
b. $\sqrt{2}/1$,
c. $\frac{\sqrt{5}+1}{2}$,
d. $3/2$.

**Atbilde:** `c`

**Skaidrojums:** Ja $AB$ un $CD$ ir garākās malas, atzīmēsim uz šīm malām nogriežņus attiecīgi 
$AM$ un $DN$ tā, lai $AM = DN = AD$. Tad pēc kvadrāta $AMND$ nogriešanas paliks taisnstūris
$MBCN$. Tā kā $AB = AM + MB = AD + MB$, tad 
$$ \frac{AD}{MB} = \frac{AB}{AD} = \frac{AD+MB}{AD} = 1 + \frac{MB}{AD}.$$
Apzīmēsim $x = \frac{AD}{MB}$, tad $x = 1+(1/x)$ jeb $x^2 = x + 1$. Vienīgā sakne $x>1$ vienādojumam
$$ x^2 - x - 1 = 0$$ 
ir $x = \frac{1+\sqrt{5}}{2}$. 




**nt-R5.q9:** <!--questionType=INPUT|length=20--> Dots bezgalīgs decimāldaļskaitlis $0.222\ldots$. 
Uzrakstīt nesaīsināmu racionālu daļu, ar ko tas vienāds.
(**Norāde:** *Ierakstīt atbildi formā `a/b`.*)

**Atbilde:** `2/9`

**Skaidrojums:** Varam sasummēt bezgalīgu ģeometrisku progresiju: 
$$ 0.222\ldots = 0.2 + 0.02 + 0.002 + \ldots = \frac{0.2}{1-0.1} = \frac{0.2}{0.9}=\frac{2}{9}. $$
Šeit izmantota formula $\frac{b_1}{1-q}$, kur $b_1$ - ģeometriskās progresijas pirmais loceklis, 
bet $q$ ir kvocients.  
Varam šo pašu rezultātu iegūt arī apzīmējot $x = 0.222\ldots$. Tad $0.1x = 0.0222\ldots$. 
Atņemot šos abus skaitļus, iegūsim $x - 0.1x = 0.2$. No šejienes var izteikt $x$. 


**nt-R5.q10** <!--questionType=INPUT|length=20--> Dots bezgalīgs decimāldaļskaitlis 
$0.(114)=0.114114114\\ldots$. Uzrakstīt nesaīsināmu racionālu daļu, ar ko tas vienāds.
(**Norāde:** *Ierakstīt atbildi formā `a/b`.*)

**Skaidrojums:** Varam sasummēt bezgalīgu ģeometrisku progresiju: 
$$ 0.114114114\ldots = 0.114 + 0.000114 + 0.000000114 + \ldots = \frac{0.114}{1-0.001} = \frac{0.114}{0.999}=\frac{114}{999}=\frac{38}{333}. $$






# Dalāmības pazīmes

**nt-R6.q1** <!--questionType=MC--> Skaitlis dod atlikumu $3$, dalot ar $9$, tad un tikai tad, ja

a. tas ir nepāra un tā pēdējais cipars dalās ar $3$,
b. tā ciparu summa dalās ar $3$,
c. tā ciparu summa dod atlikumu $3$, dalot ar $9$,
d. tā pēdējo divu ciparu veidotais skaitlis dod atlikumu $3$, dalot ar $9$.

**Atbilde:** `c`

**Skaidrojums:** Dots skaitlis $N$ ar decimālpierakstu $\overline{c_nc_{n-1}\ldots{}c_1c_0}$. 
Šajā gadījumā var izteikt skaitli $N$ sekojošā veidā:
$$ N = c_n10^n + c_{n-1}10^{n-1} + \ldots + c_110^1 + c_0. $$
Ja kādu no saskaitāmajiem $c_k10^k$ šajā summā aizstāj ar $c_k$, tad summa samazinās
par $10^kc_k - c_k = (10^k-1)c_k$. Ievērosim, ka skaitlis $10^k-1$ satur decimālpierakstā tikai 
deviņniekus, t.i. šis skaitlis dalās ar $9$.  
Tātad aizstājot $10^kc_k$ ar $c_k$, nemainās atlikums, dalot ar $9$.
Ja aizstājam visus saskaitāmos ar attiecīgajiem cipariem, iegūsim, ka 
skaitļa $N$ ciparu summa $S(N) = c_n+c_{n-1} + \ldots + c_1 + c_0$ dod tādu pašu atlikumu, dalot ar $9$, 
kā pats skaitlis $N$. Tātad pazīme skaitļiem $N$, kuri dod atlikumu $3$, dalot ar $9$, 
ir tā, ka ciparu summa $S(N)$ dod atlikumu $3$, dalot ar $9$.


**nt-R6.q2:** <!--questionType=MC--> Skaitlis dalās ar $6$ tad un tikai tad, ja

a. tas ir pāra skaitlis un tā ciparu summa dalās ar $6$,
b. tas ir pāra skaitlis un tā pēdējais cipars dalās ar $3$,
c. tā pēdējo divu ciparu veidotais skaitlis dalās ar $6$,
d. tā pēdējais cipars dalās ar $2$ un tā ciparu summa dalās ar $3$.

**Atbilde:** `d`

**Skaidrojums:** Lai skaitlis dalītos ar $6$ ir nepieciešami un pietiekami, lai tas 
dalītos ar $2$ un $3$. Tādēļ var kombinēt attiecīgās dalāmības pazīmes: skaitļa pēdējais 
cipars dalās ar $2$ (dalāmības pazīme ar $2$) un ciparu summa dalās ar $3$
(dalāmības pazīme ar $3$). 


**nt-R6.q3:** <!--questionType=MC--> Kurš no dotajiem skaitļiem dalās ar $6$?

a. $1114$,
b. $1124$,
c. $1134$,
d. $1144$. 

**Atbilde:** `c`

**Skaidrojums:** Visi dotie skaitļi dalās ar $2$. Tādēļ jāpārbauda dalāmība ar $3$: 
kuram no skaitļiem ciparu summa dalās ar $3$. Tas izpildās tikai skaitlim 
$1134$, jo $1+1+3+4 = 9$, kas dalās ar $3$. 


**nt-R6.q4:** <!--questionType=MC--> Kurš no dotajiem skaitļiem dalās ar $24$?

a. $232200$,
b. $232324$,
c. $1524$,
d. $2550$".

**Atbilde:** `a`

**Skaidrojums:** Lai skaitlis dalītos ar $24$ ir nepieciešams, lai tas dalītos ar 
$3$ un $8$. Skaitlis $232324$ nedalās ar $3$. Savukārt $1524$ vai $2550$ nedalās ar $8$. 
Atliek vienīgi $232200$.


**nt-R6.q5:** <!--questionType=MC--> Skaitlis dalās ar $12$, ja

a. tas dalās ar $3$ un $4$,
b. tā pēdējo divu ciparu veidotais skaitlis dalās ar $12$,
c. tas ir pāra un dalās ar $6$,
d. tas ir pāra un dalās ar $3$.

**Atbilde:** `a`

**Skaidrojums:** Skaitlis $12$ izsakāms kā divu savstarpēju pirmskaitļu $3$ un $4$ reizinājums. 
Tādēļ ar $12$ dalās tad, ja tas dalās ar $3$ un $4$. 


**nt-R6.q6:** <!--questionType=MC--> Kurš no dotajiem skaitļiem nedalās ar $36$? 

a. $484848484848484848$,
b. $4848484848484848$,
c. $444444444444444444$,
d. $888888888$.

**Atbilde:** `b`

**Skaidrojums:** Ar $36$ dalās tieši tie skaitļi, kas dalās ar $4$ un $9$. Visi uzrakstītie
skaitļi dalās ar $4$. Bet ne visi dalās ar $9$: ja ciparu grupa "48" atkārtojas astoņas 
reizes, tad ciparu summa ir $(4+8)\cdot 8 = 96$, kas dalās ar $3$, bet ne ar $9$. 

**nt-R6.q7:** <!--questionType=MC--> Lai pārbaudītu, vai skaitlis dalās ar $360$, jāpārbauda, vai tas dalās ar

a. $5$, $8$ un $9$,
b. $4$ un $90$,
c. $3$, $5$ un $15$,
d. $12$ un $30$.

**Atbilde:** `a`

**Skaidrojums:** Skaitlis $360$ dalās pirmreizinātājos šādi: $360 = 2^3\cdot 3^2 \cdot 5$. 
Skaitļi $2^3 = 8$, $3^2 = 9$ un $5$ ir savstarpēji pirmskaitļi, tādēļ ar $360$ dalīsies tieši 
tie skaitļi, kas dalās ar $8$, $9$ un $5$. 


**nt-R6.q8:** <!--questionType=MC--> Kurš no dotajiem skaitļiem dalās ar $360$?

a. $1984851280$,
b. $645624560$,
c. $635624660$,
d. $111111111000$.

**Atbilde:** `d`

**Skaidrojums:** Skaitlis, kas beidzas ar "660" nedalās ar $8$ 
(dalāmības pazīme ar $8$ - skaitļa pēdējiem trim cipariem jādalās ar $8$). 
Savukārt skaitļi $1984851280$, $635624660$ nedalās ar $9$, jo ciparu 
summas $1+9+8+4+8+5+1+2+8+0=46$ un $6+4+5+6+2+4+5+6+0=38$ nedalās ar $9$. 


**nt-R6.q9:** <!--questionType=MC--> Kurš no dotajiem skaitļiem dalās ar $11$? 

a. $11851848$,
b. $1086419752$,
c. $1000000000000$,
d. $11111$.

**Atbilde:** `b`

**Skaidrojums:** Skaitlis $1086419752$ apmierina $11$ dalāmības pazīmi - ciparu summas
pāru un nepāru pozīcijās $(1+8+4+9+5) - (0+6+1+7+2) = 27 - 16 = 11$ dalās ar $11$. 
Citi skaitļi neapmierina šo dalāmības pazīmi:  
Skaitlim $11851848$: $(1+8+1+4)-(1+5+8+8)=14-22=8$ nedalās ar $11$.  
Skaitlim $1000000000000$: $(1+0+0+0+0+0+0)-(0+0+0+0+0+0)=1$ nedalās ar $11$.  
Skaitlim $11111$: $(1+1+1)-(1+1) = 1$ nedalās ar $11$. 


**nt-R6.q10:** <!--questionType=MC--> Kurš no dotajiem skaitļiem dalās ar visiem skaitļiem no $1$ līdz $10$?

a. $330$,
b. $720000$,
c. $362880$,
d. $1176$. 

**Atbilde:** `c`

**Skaidrojums:** Skaitlis $362880$ dalās ar $5, 7, 8, 9$. (Dalāmību ar $7$ pārbauda tieši dalot; ar $5$ un $8$ izmantojam 
dalāmības pazīmi par pēdējo ciparu un pēdējiem trim cipariem; ar $9$ izmantojam dalāmības pazīmi par ciparu summu.)  
Starp citu, $362880 = 9! = 1\cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 \cdot 7 \cdot 8 \cdot 9$  
Citi skaitļi ar kaut ko nedalās:  
$330$ nedalās ar $8$.  
$720000$ nedalās ar $7$.  
$1176$ nedalās ar $9$.


**nt-R6.q11:** <!--questionType=MC--> Kāds cipars jāievieto $\ast$ vietā 
skaitlī $235\!\ast{}\!870$, lai tas dalītos ar $90$?

a. $9$,
b. $3$,
c. $2$,
d. $0$,
e. $11$. 

**Atbilde:** `c`

**Skaidrojums:** Skaitlis beidzas ar $0$, tātad, acīmredzot, dalās ar $2 \cdot 5 = 10$. Tam jādalās arī 
ar $9$, t.i. $2 + 3 + 5 + \ast + 8+7+0 = 10 + \ast + 15 = 25 + \ast$ jādalās ar $9$. 
Tātad $\ast$ vietā var ievietot $2$ vai $11$, bet tikai $2$ ir cipars. 


**nt-part1-04.q12:** <!--questionType=INPUT|length=4--> Sareizināja visus naturālos skaitļus, 
kas mazāki par $100$. Kādi ir pēdējie četri cipari reizinājumā: 
$$1 \cdot 2 \cdot 3 \cdot \ldots \cdot 97 \cdot 98 \cdot 99.$$

**Atbilde:** `0000`

**Skaidrojums:** Starp skaitļiem no $1$ līdz $99$ būs pietiekami daudzi skaitļi, kas dalās ar $10$. 
Tos sareizinot iegūsim skaitli, kas dalās ar $10^4 = 10000$. Tātad reizinājums beidzas ar četrām nullēm. 


**nt-part1-04.q13:** <!--questionType=INPUT|length=1--> Sareizināja visus nepāru divciparu skaitļus, 
kas mazāki par $30$. Kāds ir pēdējais cipars reizinājumā 
$$11 \cdot 13 \cdot \ldots \cdot 27 \cdot 29.$$

**Atbilde:** `5`

**Skaidrojums:** Starp nepāru skaitļiem atradīsies tie, kas dalās ar $5$, tādēļ arī reizinājums dalīsies
ar $5$ (turklāt ir nepāru skaitlis kā nepāru skaitļu reizinājums). Tātad reizinājums beidzas ar ciparu $5$
(nevis ar $0$). 









