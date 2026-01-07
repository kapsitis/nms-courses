---
title: "Polinomi (2026-01-05 .. 2026-01-09)"
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "Polinomi (2026-01-05 .. 2026-01-09)"
header-includes:
  - |
    \makeatletter
    \RedeclareSectionCommand[
      beforeskip=1.2ex plus 0.4ex minus 0.2ex,
      afterskip=0.4ex plus 0.2ex minus 0.2ex
    ]{subsection}
    \makeatother
  - \setcounter{section}{11}
  - |
    \usepackage{etoolbox}
    \AtBeginEnvironment{footnotesize}{\footnotesize}
---
# 12. Polinomi un racionālas izteiksmes (2026-01-05 .. 2026-01-09) {-}

1. Polinomu dalīšana ar atlikumu. Praktisks lietojums: 
   Ja $a$ ir $P(x)$ sakne, tad $P(x) = (x − a)Q(x)$ ($P(x)$ dalās ar $x-a$ bez atlikuma). 
2. Polinomam $P(x)$ (ja tas nav identiski $0$) ir ne vairāk kā $n$ reālas saknes.
   Un ja diviem $n$-tās pakāpes polinomiem sakrīt vērtības vairāk nekā $n$ punktos, tad tie ir identiski. Nepāra pakāpes polinomiem ir vismaz viena reāla sakne.
3. Vjeta teorēma 2. un 3.pakāpes polinomiem. 


**Definīcija:**   
Skaitlis $a$ ir polinoma $P(x)$ sakne, ja $P(a)=0$.  
Piedevām, ja skaitlis $a$ ir polinoma $P(x)$ sakne, tad
$$P(x)=(x-a)Q(x),$$
kur $Q(x)$ ir kaut kāds polinoms.

Svarīgi sekot līdzi, kādai skaitļu kopai pieder polinoma saknes. Iespējami 
dažādi gadījumi:

* Polinomam $P(x)=x^2-1$ ir 2 **veselas** saknes $x = 1$ un $x = -1$. 
* Polinomam $P(x)=4x^2-1$ nav **veselu** sakņu, taču tam ir 2 
  racionālas saknes $\frac12$ un $-\frac12$.
* Polinomam $P(x)=x^2-2$ nav **racionālu** sakņu, taču tam ir 2 reālas saknes $\sqrt2$ un $-\sqrt2$.
* Polinomam $P(x)=x^2+1$ nav **reālu** sakņu, taču tam ir 2 kompleksas saknes $i$ un $-i$.

**Sofijas Žermēnas identitāte:**   
Uzdevums - sadalīt reizinātājos polinomu $x^4 + 4$. Reālu sakņu tam nav, ar $x-a$ izdalīt 
nevar nevienam reālam $a$. Bet reizinātājos var sadalīt:  
$$x^4 + 4 = (x^2 + 2)^2 - 4x^2 = (x^2 + 2 - 2x)(x^2 + 2 - 2x).$$

**Vjeta teorēma 2.pakāpes polinomam:**  
Ja polinomam $x^2 + px + q = 0$ ir saknes $x_1,x_2$, tad izpildās
$x_1+x_2 = -p;\quad\quad{}x_1 \cdot x_2 = q.$

**Vjeta teorēma 3.pakāpes polinomam:**  
Ja polinomam $x^2 + px^2 + qx + r = 0$ ir saknes $x_1,x_2,x_3$, tad izpildās
$$x_1+x_2 +x_3 = -p;\quad\quad{}x_1x_2 + x_1 x_3 + x_2 x_3 = q;\quad\quad{}x_1x_2x_3 = -r.$$  
Vjeta teorēma pārbaudāma, atverot iekavas izteiksmē:
$(x-x_1)(x-x_2)(x-x_3) = 0.$



**Uzdevums 1:**  
Definējam šādu funkciju ${\displaystyle f(x) = \frac{2x-3}{x-1}}$.  
**(A)** Izteikt funkcijas $f(f(x))$ (divreiz pielieto šo funkciju)
un arī $f(f(f(x)))$ (trīsreiz pielieto šo funkciju).  
**(B)** Kāds ir funkciju $f(f(x))$ un 
$f(f(f(x)))$ definīcijas apgabals un vērtību apgabals?

**Uzdevums 2:**  
Robotam uz vēdera ir displejs, kas var attēlot jebkuru racionālu 
daļskaitli $x=P/Q$, izņemot $x=0=0/1$ un $x=1=1/1$. 
Kad robots kustina kreiso kāju (**K**), tad daļskaitlis $x$ uz 
šī displeja pārvēršas par $1/x$. Kad robots kustina labo kāju (**L**), 
tad daļskaitlis $x$ pārvēršas par $1-x$.

Robots pagāja 100 soļus uz priekšu ($100$ reizes izdarīja kustību pāri **K,L**). 
Izrādījās, ka beigās viņam uz vēdera ir skaitlis $\frac{22}{7}$. 
Kāds skaitlis tur bija pašā sākumā?


**Uzdevums 3:**  
Vienādojumam $x^2 + ax + b = 0$ (kur $a$ un $b$ ir dažādi) 
ir divas saknes $x = a$ un $x=b$. Cik daudzus šādus vienādojumus 
var uzrakstīt?

**Uzdevums 4:**  
Dots kubisks vienādojums $2x^3 - x^2 - 6x + 5 = 0$.  
**(A)** Uzminēt kādu tā sakni $a$.   
**(B)** Izdalīt $P(x) = 2x^3 - x^2 - 6x + 5$ ar $(x-a)$ atrastajai saknei $a$ un 
atrast arī pārējās saknes.

**Uzdevums 5:**  
Vienādojuma $x^3−14x^2 + 63x−91 = 0$ saknes ir trijstūra malu garumi centimetros.
Aprēķināt šī trijstūra laukumu.  
*Piezīme:* Trijstūrim ar malām $a,b,c$ 
laukums $S = \sqrt{p(p-a)(p-b)(p-c)}$, kur 
$p=(a+b+c)/2$ ir trijstūra pusperimetrs (*Hērona formula*).

**Uzdevums 6:**  
Vienādojumam $x^3 - px + 2019 = 0$, kur $p$ — naturāls skaitlis, 
ir trīs reālas saknes $x_1, x_2, x_3$. Kāda var būt izteiksmes 
$x_1^3 + x_2^3 + x_3^3$ vērtība?


**Uzdevums 7:**  
$a,b$ ir reāli skaitļi. Zināms, ka 
$$a+b\in\mathbb Q,\qquad a^2+b^2\in\mathbb Q.$$
Pierādīt, ka $ab \in \mathbb{Q}$. Vai arī $a,b$ ir racionāli skaitļi?


**Uzdevums 8:**  
$a,b$ ir reāli skaitļi un $b\ne 0$. Zināms, ka 
$$a+b\in\mathbb Q,\qquad ab\in\mathbb Q,\qquad \frac{a}{b}\in\mathbb Q.$$
Pierādīt, ka no $a+b\ne 0$ seko arī $a,b\in\mathbb Q$.

