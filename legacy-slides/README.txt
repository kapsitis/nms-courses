An unknown number is divisible by just four numbers from the set {6, 15, 20, 21, 70}. Determine which ones.
https://www.hackmath.net/en/problem/7137?tag_id=149,161






# <lo-theory/> LKD saglabājas

**Apgalvojums:** Ja $\mbox{LKD}(a_1,d) = k$, 
tad arī $\mbox{LKD}(a_1+d,d)=k$ un 
$\mbox{LKD}(a_1 - d, d) = k$. 

Šis ir apgalvojums par invariantu: 
lielākais kopīgais dalītājs progresijas loceklim 
un diferencei saglabājas. 

## <lo-summary/> Piemērs: Kalendārs

TODO: Tabulkalendārs, kur nemainās atlikumi


TODO: Attēls, kur $9k$ un $15k$ uzzīmētas tā, lai $\mbox{LKD}(9,15) =3$ ir
sasniegta kā starpība.



## <lo-sample/> BBK2012.P1.104

Skaitļu virkne $(a_i)$ tiek definēta šādi: 
$$a_1=19,\;a_2=90,\;a_{n+2}=a_n+a_{n+1},\;\mbox{ja}\;n=1,2,3,\ldots.$$
Atrast skaitļu $a_{1989}$ un $a_{1990}$ lielāko kopīgo dalītāju.


## <lo-hints/> BBK2012.P1.104

* Kādi ir daži pirmie locekļi virknē? 
* Vai tā ir aritmētiska progresija?
* Kāda ir 

## <lo-soln/> BBK2012.P1.104

* Ievērojam, ka $\mbox{LKD}(a_1,a_2)=\mbox{LKD}(19,90)=1$. 
* Pamatojam ar indukciju, ka $\mbox{LKD}(a_n,a_{n+1})=1$ katram $n=1,2,\ldots$. 

Jāpamato tikai indukcijas pāreja: 

* Ja $\mbox{LKD}(a_k,a_{k+1})=1$, tad arī $\mbox{LKD}(a_{k+1},a_{k+2})=1$, 
jo $a_{k+2} = a_{k} + a_{k+1}$ un skaitļiem $(a_{k+1}, a_{k}+a_{k+1})$ 
lietojam Eiklīda algoritmu - atņemam mazāko no lielākā:

$$\mbox{LKD}(a_{k+1},a_{k+2}) = \mbox{LKD}(a_k,a_{k+1})=1.$$












## <lo-sample/> LT.LKMMO.2009.15

Pierādiet vai atspēkojiet, ka skaitlis 
${\underbrace{99\ldots9}_{2005}}^{2009}$
var tikt iegūts, izsvītrojot kaut kādus skaitļa
${\underbrace{99\ldots9}_{2008}}^{2009}$
ciparus.

LKMMO - *Lietuvos komandinė mokinių matematikos olimpiada prof. Jono Kubiliaus taurei laimėti* 
(Lietuvas komandveida skolēnu matemātikas olimpiāde, lai laimētu profesora 
Jona Kubiļa kausu). 



## <lo-yellow/> Gliemežu uzdevums - 1


Kvadrāta malas garums ir $1$. Tā virsotnēs novietoti $4$ gliemeži. 
Tie vienlaicīgi sāk pārvietoties ar vienādiem ātrumiem $v$; katrs gliemezis ikbrīdi 
kustas turp, kur ir tā tuvākais kaimiņš (pret pulksteņa rādītāju virzienam attiecībā 
pret kvadrāta centru). 

* Pēc cik ilga laika gliemeži satiksies? 
* Cik reizes viņi apriņķo ap kvadrāta centru? 

**Līdzīgs uzdevums:** Pa kādu trajektoriju kustas ceļotājs, kurš visu laiku pārvietojas
uz ziemeļaustrumiem?


## <lo-yellow/> Gliemežu uzdevums - 2

* Minētais ir fizikas (kinemātikas) uzdevums, kur var izmantot
atskaites sistēmu - Dekarta koordinātes, kas griežas līdzi gliemežiem. 
* Katra gliemeža ātrumu veido divas komponentes - viena no tām projicēta
uz $4$ gliemežu veidotā kvadrāta centru, otra - rotē pa kvadrātam apvilktā riņķa pieskari. 
* Ātrums centra virzienā ir $v/\sqrt{2}$, bet attālums šajā pašā virzienā ir puse
no kvadrāta diagonāles, t.i. $1/\sqrt{2}$. 







# <lo-sample/> LV.VO.2003.10.2

Dots, ka $a$ un $b$ ir naturāli skaitļi, pie tam $a$ nedalās ar $5$. 
Skaitļu virkni $x_1, x_2, x_3, \ldots$ 
veido sekojoši: $x_1 = 5$, $x_{n+1} = ax_n + b$, ja $n=1;2;3;\ldots$. 
Kādai lielākajai $k$ vērtībai iespējams, ka visi skaitļi
$x_1;x_2;x_3;\ldots;x_k$ ir pirmskaitļi?






