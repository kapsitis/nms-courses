---
title: "Algebra: Funkcijas"
show-solutions: true
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "Algebra: Funkcijas"
header-includes:
  - |
    \makeatletter
    \RedeclareSectionCommand[
      beforeskip=1.2ex plus 0.4ex minus 0.2ex,
      afterskip=0.4ex plus 0.2ex minus 0.2ex
    ]{subsection}
    \makeatother
---
# Algebra: Funkcijas {-}

## 1.uzdevums {-} 

Dota funkcija $f(x) = \frac{k-x}{1+x}$. Atrast tādu funkcijas $f$
kompozīciju pašai ar sevi, kur visiem $x$ (izņemot varbūt galīgu skaitu 
$x$, kam izteiksmes nav definētas), kompozīcija identiski vienāda ar $x$.
(Ja tādas ir vairākas, izvēlēties īsāko kompozīciju.)

**(A)** $f(f(x)) = x$,  
**(B)** $f(f(f(x))) = x$,  
**(C)** $f(f(f(f(x)))) = x$,  
**(D)** $f(f(f(f(f(x))))) = x$,  
**(E)** Neviena no minētajām kompozīcijām nav $x$.

::: solution
**Atbilde:** `A`

**Atrisinājums:**   
Ievietojam $f(f(x))$, lai izrēķinātu funkciju kompozīciju:  
$$f(f(x)) = \frac{k - f(x)}{1 + f(x)} = \frac{k - \frac{k-x}{1+x}}{1 + \frac{k-x}{1+x}}.$$

Pareizinām skaitītāju un saucēju ar $1+x$:  
$$\frac{k - \frac{k-x}{1+x}}{1 + \frac{k-x}{1+x}} = \frac{k+kx - k + x}{1+x+k-x} = \frac{(k+1)x}{k+1} = x.$$  
Tātad jau $f(f(x))$ ir identiski vienāds ar $x$, kas ir atbilde **(A)**. 
:::


## 2.uzdevums {-} 

Dota funkcija $f(x) = \frac{1}{1 - x}$. Atrast tādu funkcijas $f$
kompozīciju pašai ar sevi, kur visiem $x$ (izņemot varbūt galīgu skaitu 
$x$, kam izteiksmes nav definētas), kompozīcija identiski vienāda ar $x$.
(Ja tādas ir vairākas, izvēlēties īsāko kompozīciju.)

**(A)** $f(f(x)) = x$,  
**(B)** $f(f(f(x))) = x$,  
**(C)** $f(f(f(f(x)))) = x$,  
**(D)** $f(f(f(f(f(x))))) = x$,  
**(E)** Neviena no minētajām kompozīcijām nav $x$.


::: solution
**Atbilde:** `B`

**Atrisinājums:**  
Vispirms ievietojam $f(f(x))$. Iegūstam  
$$f(f(x)) = \frac{1}{1 - f(x)} = \frac{1}{1 - \frac{1}{1-x}} = \frac{1 - x}{1-x-1} = \frac{x-1}{x}.$$   
Tālāk, ievietojam šo $f(f(x))$ izteiksmi funkcijā $f$:  
$$f(f(f(x))) = \frac{1}{1 - \frac{x-1}{x}} = \frac{x}{x-x+1} = \frac{x}{1} = x.$$

Esam ieguvuši, ka $f(f(f(x)))$ ir identiski vienāds ar $x$ (atskaitot punktus $x=0$, $x=1$, 
kur izteiksmes $f(x)$ vai $f(f(x))$ nav definētas). Tā ir atbilde **(B)**.
:::


## 3.uzdevums {-}

Kīrs uzrakstīja sešus dažādus pirmskaitļus $p, q, r, s, t, u$, 
kas visi mazāki par $20$, un
$p+q = r+s = t+u$. Kāda ir $p + q$ vērtība?



<!--
UK.JMC.2010.22

Kiran writes down six different prime numbers, $p, q, r, s, t, u$, 
all less than $20$, such that
$p + q= r + s = t + u$. What is the value of $p + q$?

**(A)** $16$, **(B)** $18$, **(C)** $20$, **(D)** $22$, **(E)** $24$. 
-->

::: solution
**Atbilde:** `24`

**Atrisinājums:**  
Pirmskaitli $2$ nevar izmantot, jo tad viena no summām būtu nepāra 
skaitlis, bet citas būtu pāra skaitļi (pretruna). 

Nepāra pirmskaitļu ir pavisam $7$: $\{ 3,5,7,11,13,17,19 \}$. 
Ja atmet arī pirmskaitli $3$ un saliek pāros atlikušos - 
vismazāko ar vislielāko utt., tad iegūst
$5+19 = 7+17 = 11+13 = 24$.
:::



## 4.uzdevums {-}

Zināms, ka $4x-y=5$, $4y-z=7$ un $4z-x=18$. Kāda ir izteiksmes $x + y + z$ vērtība?

**(A)** $8$, **(B)** $9$, **(C)** $10$, **(D)** $11$, **(E)** $12$.

<!--
UK.IMC.2010.14
Given that $4x−y=5$, $4y− z = 7$ and $4z− x = 18$, what is the value of $x + y + z$?  
**(A)** $8$, **(B)** $9$, **(C)** $10$, **(D)** $11$, **(E)** $12$.
-->

::: solution
**Atbilde:** `10`

**Atrisinājums:**  
Saskaitām visas vienādības:  
$(4x - y) + (4y-z) + (4z - x) = 5+7+18,$ jeb $3(x+y+z) = 30$. 
Iegūstam, ka $x+y+z = 10$.
:::



## 5.uzdevums {-}

Pozitīvi skaitļi $x$ un $y$ apmierina sakarības $x^4 - y^4 = 2009$
un $x^2 + y^2 = 49$. Kāda ir $y$ vērtība?

**(A)** $1$, **(B)** $2$, **(C)** $3$, **(D)** $4$, **(E)** nepietiek informācijas.


<!--
UK.SMC.2009.16
The positive numbers $x$ and $y$ satisfy the equations $x^4 - y^4 = 2009$
and $x^2 + y^2 = 49$. What is the value of $y$?

**(A)** $1$, **(B)** $2$, **(C)** $3$, **(D)** $4$, **(E)** more information is needed.
-->

::: solution
**Atbilde:** `B`

**Atrisinājums:**  
Sadalām reizinātājos $x^4 - y^4 = (x^2 + y^2)(x^2 - y^2)$. 
Tā kā $2009 = 49 \cdot 41$, tad $x^2 - y^2 = 41$, kas kopā ar 
vienādību $x^2 + y^2 = 49$ ļauj secināt, ka $y^2 = (49 - 41)/2 = 4$. 
Tādēļ $y = \pm 2$, bet $y$ var būt tikai pozitīvs, tāpēc $y=2$. 
:::



## 6.uzdevums {-}

Reāli skaitļi $x$ un $y$ abi ir lielāki par $1$. Kurai no daļām ir vislielākā vērtība?

**(A)** $\dfrac{x}{y+1}$,   
**(B)** $\dfrac{x}{y-1}$,  
**(C)** $\dfrac{2x}{2y+1}$,   
**(D)** $\dfrac{2x}{2y-1}$,  
**(E)** $\dfrac{3x}{3y+1}$.

<!--
EU.PinkKangaroo.2011.17
The numbers $x$ and $y$ are both greater than $1$. Which of the following fractions has the greatest value?

**(A)** $\dfrac{x}{y+1}$  
**(B)** $\dfrac{x}{y-1}$  
**(C)** $\dfrac{2x}{2y+1}$  
**(D)** $\dfrac{2x}{2y-1}$  
**(E)** $\dfrac{3x}{3y+1}$
-->

::: solution
**Atbilde:** `B`

**Atrisinājums:**  
Ja divām daļām ir vienādi skaitītāji, tad lielākā ir tā, kurai mazāks saucējs. 
Tāpēc $\frac{x}{y-1} > \frac{x}{y+1}$ un $\frac{2x}{2y-1} > \frac{2x}{2y+1}$. 
Secinām, ka lielākā daļa ir viena no $\frac{x}{y-1}, \frac{2x}{2y-1}$. 
(Daļa $\dfrac{3x}{3y+1}$ nevar būt lielākā, jo tā ir mazāka par $\frac{3x}{3y} = \frac{x}{y}$.)

Pamatojam, ka $\frac{x}{y-1} > \frac{2x}{2y-1}$. Sareizinot daļas krustiski 
un noīsinot, iegūstam, ka jāpābauda, vai $-x > -2x$. Tas tiešām izpildās pozitīviem $x$. 
Tātad $\frac{x}{y-1}$ ir lielākā no visām uzrakstītajām daļām, kas 
ir atbilde **(B)**. 
:::


## 7.uzdevums {-}

Kura no izteiksmēm ir ekvivalenta izteiksmei $(x+y+z)(x-y-z)$?

**(A)** $x^2-y^2-z^2$,  
**(B)** $x^2-y^2+z^2$,  
**(C)** $x^2-xy-xz-z^2$,   
**(D)** $x^2-(y+z)^2$,   
**(E)** $x^2-(y-z)^2$.

<!--
UK.SMC.2010.8
Which of the following is equivalent to $(x+y+z)(x-y-z)$?

**(A)** $x^2-y^2-z^2$  
**(B)** $x^2-y^2+z^2$  
**(C)** $x^2-xy-xz-z^2$  
**(D)** $x^2-(y+z)^2$  
**(E)** $x^2-(y-z)^2$
-->

::: solution
**Atbilde:** `B`

**Atrisinājums:**  
Pārveidojam $(x+y+z)(x-y-z) = (x + (y+z))(x - (y+z)) = x^2 - (y+z)^2$, 
kas ir atbilde **(D)**. 
:::



## 8.uzdevums {-}

Divi skaitļi $x$ un $y$ ir tādi, ka $x+y=20$ un 
$\frac{1}{x}+\frac{1}{y}=\frac{1}{2}$. Kāda ir izteiksmes $x^2y+xy^2$ vērtība?

**(A)** $80$,  
**(B)** $200$,  
**(C)** $400$,  
**(D)** $640$,  
**(E)** $800$.

<!--
UK.SMC.2011.18
Two numbers $x$ and $y$ are such that $x+y=20$ and 
$\frac{1}{x}+\frac{1}{y}=\frac{1}{2}$. What is the value of $x^2y+xy^2$?

**(A)** $80$  
**(B)** $200$  
**(C)** $400$  
**(D)** $640$  
**(E)** $800$
-->

::: solution
**Atbilde:** `B`

**Atrisinājums:**  
Saskaitām daļas: $\frac{1}{x} + \frac{1}{y} = \frac{x+y}{xy}$.  
Ja $x+y = 20$, tad $xy = 40$. No šejienes var izteikt:  
$$x^2y+xy^2 = xy(x+y) = 40 \cdot 20 = 800,$$  
kas ir atbilde **(E)**. 
:::


## 9.uzdevums {-}

Ir zināms, ka $\left(a+\frac{1}{a}\right)^2=6$ un $a^3+\frac{1}{a^3}=N\sqrt{6}$ un $a>0$. 
Kāda ir $N$ vērtība?

<!--
UK.SeniorKangaroo.2011.19
Given that $\left(a+\frac{1}{a}\right)^2=6$ and $a^3+\frac{1}{a^3}=N\sqrt{6}$ and $a>0$, what is the value of $N$?
-->

::: solution
**Atbilde:** `B`

**Atrisinājums:**  

:::


## 10.uzdevums {-}

Ir zināms, ka $x + y + z = 1$, $x + y - z = 2$ un $x - y - z = 3$. 
Kāda ir $xyz$ vērtība?

**(A)** $-2$
**(B)** $-\frac{1}{2}$
**(C)** $0$
**(D)** $\frac{1}{2}$
**(E)** $2$

<!--
UK.SMC.2012.7
7. Given that $x + y + z = 1$, $x + y - z = 2$ and $x - y - z = 3$, what is the value of $xyz$?

**(A)** $-2$
**(B)** $-\frac{1}{2}$
**(C)** $0$
**(D)** $\frac{1}{2}$
**(E)** $2$
-->

::: solution
**Atbilde:** `D`

**Atrisinājums:**  
No pirmās un otrās vienādības $y = -1/2$. No otrās un trešās vienādības $z = -1/2$. 
Ievietojot tos pirmajā vienādībā, iegūstam $x = 2$. 
Tātad $xyz = 2 \cdot (-1/2) \cdot (-1/2) = 1/2$, kas ir atbilde **(D)**. 
:::





## 11.uzdevums {-}

Zināms, ka $a + b = 5$ un $ab = 3$. Kāda ir izteiksmes 
$a^4 + b^4$ vērtība?

**(A)** $129$
**(B)** $145$
**(C)** $150$
**(D)** $155$
**(E)** $160$

<!--
UK.SeniorKangaroo.2012.16
16. Given that $a + b = 5$ and $ab = 3$, what is the value of $a^4 + b^4$?

**(A)** $129$
**(B)** $145$
**(C)** $150$
**(D)** $155$
**(E)** $160$
-->

::: solution
**Atbilde:** `B`

**Atrisinājums:**    
No $a + b = 5$ un $ab = 3$ var izteikt $a^2 + b^2 = (a+b)^2 - 2ab = 25 - 6 = 19$. 
Tātad $a^4 + b^4 = (a^2 + b^2)^2 - 2a^2b^2 = 19^2 - 2 \cdot 3^2 = 361 - 18 = 343$, kas ir atbilde **(B)**. 
:::


## 12.uzdevums {-}

Ja dots, ka $\frac{3x + y}{x - 3y} = -1$, tad kāda ir izteiksmes $\frac{x + 3y}{3x - y}$ vērtība?

**(A)** $-1$
**(B)** $2$
**(C)** $4$
**(D)** $5$
**(E)** $7$


<!-- 
UK.SMC.2014.14
14. Given that $\frac{3x + y}{x - 3y} = -1$, what is the value of $\frac{x + 3y}{3x - y}$?

**(A)** $-1$
**(B)** $2$
**(C)** $4$
**(D)** $5$
**(E)** $7$
-->



## 13.uzdevums {-}

Skaitļi $x, y$ un $z$ apmierina vienādojumus $x + y + z = 15$ 
un $\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = 0$. Kāda ir izteiksmes 
$x^2 + y^2 + z^2$ vērtība?

<!--
UK.SeniorKangaroo.2014.16
16. The numbers $x, y$ and $z$ satisfy the equations $x + y + z = 15$ and $\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = 0$. What is the value of $x^2 + y^2 + z^2$?
-->


## 14.uzdevums {-}

Dota funkcija $f(x) = x + \sqrt{x^2 + 1} + \frac{1}{x - \sqrt{x^2 + 1}}$. 
Atrast vērtību $f(2015)$.

**(A)** $-1$
**(B)** $0$
**(C)** $1$
**(D)** $\sqrt{2016}$
**(E)** $2015$

<!--
UK.SMC.2015.22

22. Let $f(x) = x + \sqrt{x^2 + 1} + \frac{1}{x - \sqrt{x^2 + 1}}$. What is the value of $f(2015)$?

**(A)** $-1$
**(B)** $0$
**(C)** $1$
**(D)** $\sqrt{2016}$
**(E)** $2015$
-->



## 15.uzdevums {-}

Izteiksmi $1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{5}}}$ pārveidoja 
par daļu $\frac{a}{b}$, kur $a$ un $b$ ir naturāli skaitļi, 
kuru lielākais kopīgais dalītājs ir $1$. Atrast $a + b$ vērtību.

<!--
UK.SeniorKangaroo.2015.2

2. The value of the expression $1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{5}}}$ is $\frac{a}{b}$, where $a$ and $b$ are integers whose only common factor is $1$. What is the value of $a + b$?
-->


## 16.uzdevums {-}

Skaitļi $a$, $b$ un $c$ ir tādi, ka $\frac{a}{b + c} = \frac{b}{c + a} = \frac{c}{a + b} = k$. 
Cik dažādas $k$ vērtības ir iespējamas?

<!--
UK.SeniorKangaroo.2015.18
18. Numbers $a$, $b$ and $c$ are such that $\frac{a}{b + c} = \frac{b}{c + a} = \frac{c}{a + b} = k$. How many possible values of $k$ are there?
-->



## 17.uzdevums {-}

Kādā virknē $n$-to locekli iegūst, sareizinot visus skaitļus 
$\sqrt{1 + \frac{1}{k}}$, kur $k$ pieņem visas vērtības no $2$ līdz $n + 1$ ieskaitot. 
Piemēram, šīs virknes trešais loceklis ir 
$$\sqrt{1 + \frac{1}{2}} \cdot \sqrt{1 + \frac{1}{3}} \cdot \sqrt{1 + \frac{1}{4}}.$$

Kurai mazākajai $n$ vērtībai, $n$-tais loceklis šajā virknē būs vesels skaitlis?

**(A)** $3$
**(B)** $5$
**(C)** $6$
**(D)** $7$
**(E)** more than $7$

<!--
UK.IMC.2017.24
24. The $n$th term in a certain sequence is calculated by multiplying together all the numbers $\sqrt{1 + \frac{1}{k}}$, where $k$ takes all the integer values from $2$ to $n + 1$ inclusive. For example, the third term in the sequence is $\sqrt{1 + \frac{1}{2}} \times \sqrt{1 + \frac{1}{3}} \times \sqrt{1 + \frac{1}{4}}$.

Which is the smallest value of $n$ for which the $n$th term of the sequence is an integer?

- A. $3$
- B. $5$
- C. $6$
- D. $7$
- E. more than $7$
-->


## 18.uzdevums {-}

Kvadrāta virsotnes ir punkti ar koordinātēm $(0, 0)$, $(1, 0)$, 
$(1, 1)$ un $(0, 1)$. Tajā pašā koordinātu sistēmā doti 
arī vairāku vienādojumu grafiki:

$$x^2 + y^2 = 1,\quad y = x + 1,\quad y = -x^2 + 1,\quad y = x,\quad y = \frac{1}{x}.$$

Cik daudzi no grafikiem iet cauri tieši divām kvadrāta virsotnēm?

**(A)** $1$
**(B)** $2$
**(C)** $3$
**(D)** $4$
**(E)** $5$


<!--
UK.SMC.2016.9

9. A square has vertices at $(0, 0)$, $(1, 0)$, $(1, 1)$ and $(0, 1)$. Graphs of the following equations are drawn on the same set of axes as the square.

$x^2 + y^2 = 1,\quad y = x + 1,\quad y = -x^2 + 1,\quad y = x,\quad y = \frac{1}{x}$

How many of the graphs pass through exactly two of the vertices of the square?

**(A)** $1$
**(B)** $2$
**(C)** $3$
**(D)** $4$
**(E)** $5$
-->

::: solution
**Atbilde:** `A`

**Atrisinājums:**  
Cauri divām kvadrāta virsotnēm iet funkcijas $y = x$ grafiks; tātad tieši viens grafiks.

* $x^2 + y^2 = 1$ iet caur $(1;0)$. 
* $y = x + 1$ iet caur $(0;1)$.
* $y = -x^2 + 1$ iet caur $(0;1)$.
* $y = x$ iet caur $(0;0)$ un $(1;1)$.
* $y = \frac{1}{x}$ iet caur $(1;1)$.
:::

## 19.uzdevums {-}

Reāli skaitļi $x$, $y$ un $z$ ir atrisinājums $(x, y, z)$ 
vienādojumam $(x^2 - 9)^2 + (y^2 - 4)^2 + (z^2 - 1)^2 = 0$. 
Cik dažādas vērtības var būt izteiksmei $x + y + z$?

<!--
UK.SeniorKangaroo.2016.8
8. The real numbers $x$, $y$ and $z$ are a solution $(x, y, z)$ of 
the equation $(x^2 - 9)^2 + (y^2 - 4)^2 + (z^2 - 1)^2 = 0$. 
How many different possible values are there for $x + y + z$?
-->

::: solution
**Atbilde:** `7`

**Atrisinājums:**  
Ja vairāku skaitļu kvadrātu summa ir $0$, tad katrs atsevišķais skaitlis iekavās ir $0$. 
Tātad $x^2 = 9$, $y^2 = 4$ un $z^2 = 1$.

$x$, $y$ un $z$ iespējamās vērtības: $x = \pm 3$, $y = \pm 2$ un $z = \pm 1$.

Izveidojam $x + y + z$ izteiksmes iespējamās vērtības -- to ir pavisam $7$ (jo divas sakrīt):

$$
\begin{aligned}
x + y + z &= 3 + 2 + 1 = 6,\\
x + y + z &= 3 + 2 - 1 = 4,\\
x + y + z &= 3 - 2 + 1 = 2,\\
x + y + z &= 3 - 2 - 1 = 0,\\
x + y + z &= -3 + 2 + 1 = 0,\\
x + y + z &= -3 + 2 - 1 = -2,\\
x + y + z &= -3 - 2 + 1 = -4,\\
x + y + z &= -3 - 2 - 1 = -6.
\end{aligned}
$$
:::


## 20.uzdevums {-}

Divu pozitīvu skaitļu $x,y$ aritmētisko vidējo $A$
definē ar formulu $A = \frac{1}{2}(x + y)$, un ģeometrisko vidējo $G$
definē ar formulu $G = \sqrt{xy}$. Kaut kādiem diviem skaitļiem $x$ un $y$, 
kur $x > y$, izrādījās, ka attiecība $A : G = 5 : 4$. 
Kāda var būt dalījuma $x : y$ vērtība?

**(A)** $5 : 4$
**(B)** $2 : 1$
**(C)** $5 : 2$
**(D)** $7 : 2$
**(E)** $4 : 1$

<!--
UK.SMC.2017.18
18. The arithmetic mean, $A$, of any two positive numbers $x$ and $y$ is defined to be $A = \frac{1}{2}(x + y)$ and their geometric mean, $G$, is defined to be $G = \sqrt{xy}$. For two particular values $x$ and $y$, with $x > y$, the ratio $A : G = 5 : 4$. For these values of $x$ and $y$, what is the ratio $x : y$?

**(A)** $5 : 4$
**(B)** $2 : 1$
**(C)** $5 : 2$
**(D)** $7 : 2$
**(E)** $4 : 1$
-->

::: solution
**Atbilde:** `E`

**Atrisinājums:**    
Ievērojam, ka dažādiem $x,y$, vienmēr $A \geq G$ (vidējais aritmētiskais ir lielāks par 
vidējo ģeometrisko; vai arī tie ir vienādi, ja $x = y$). 

Ja $A : G = 5 : 4$, tad $A = \frac{1}{2}(x + y) = 5k$ un $G = \sqrt{xy} = 4k$
jeb $x + y = 10k$ un $xy = 16k^2$.
No $x + y = 10k$ un $xy = 16k^2$, iegūstam, ka $x$ un $y$ ir 
saknes vienādojumam $z^2 - 10kz + 16k^2 = 0$.
Izsakām abas saknes (zinot no dotajām attiecībām, ka $x > y$):

$$x,y = \frac{10k \pm \sqrt{100k^2 - 64k^2}}{2} = \frac{10k \pm 6k}{2} = 5k \pm 3k$$

Tātad $x = 5k + 3k = 8k$ un $y = 5k - 3k = 2k$. To attiecība $x:y$ ir $8:2 = 4:1$, 
kas ir atbilde **(E)**.
:::


