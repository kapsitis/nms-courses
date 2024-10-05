4. Progresijas, Eiklīda algoritms
==================================


.. raw:: latex

	\arrayrulecolor[HTML]{DB5800}
	\renewcommand{\arraystretch}{1.2}
	\begin{table}[ht!]\centering
	{\footnotesize    
	\begin{tabular*}{12.87cm}{@{}|p{3cm}p{9.00cm}|@{}} \hline    
	\headcol \multicolumn{2}{|c|}{\bf \normalsize Aritmētiskas progresijas} \\ \hline 
	
	
	$(a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$. &
	\cellcolor[HTML]{FFFFEE}
	\textbf{Binomiālie koeficienti:} $(a+b)^n = a^n + \binom{n}{1}a^{n-1}b + \cdots + \binom{n}{n-1}ab^{n-1}+b^n$, 
	kur $\binom{n}{k} = C_n^k = \frac{n!}{k!(n-k)!}$. 
	\\ \hline  
	
	$(a+b+c+d)^4 = \ldots + 12a^2bc + \ldots$, jo 
	$\frac{4!}{2!1!1!}=12$. &  \cellcolor[HTML]{FFFFEE} 
	\textbf{Polinomiālie koeficienti:} $(a_1+a_2+\cdots{}+a_m)^n$ izvirzījums satur $a_1^{k_1}a_2^{k_2}\cdots{}a_m^{k_m}$ ar 
	koeficientu $\frac{n!}{k_1!k_2!\cdots{}k_m!}$, ja $k_1+k_2+\cdots+k_m=n$. 
	\\ \hline  
	
	
	$a^3 + b^3 = (a+b)(a^2 - ab + b^2)$. &
	\cellcolor[HTML]{FFFFEE}
	\textbf{Nepāru pakāpju summa:} $a^{2n+1} + b^{2n+1} = (a+b)(a^{2n}-a^{2n-1}b+\cdots-ab^{2n-1}+b^{2n})$. 
	\\ \hline 
	
	$a^3 - b^3 = (a-b)(a^2 + ab + b^2)$. 
	&  
	\cellcolor[HTML]{FFFFEE} 
	\textbf{Pakāpju starpība:} $a^{n} - b^{n} =$ \newline 
	$=(a-b)(a^{n-1}+a^{n-2}b+\cdots+ab^{n-2}+b^{n-1})$. 
	\\ \hline 
	
	
	$ax^2+bx+c=0$ ir $3$ saknes $\Rightarrow$ $a=b=c=0$ &
	\cellcolor[HTML]{FFFFEE}
	\textbf{Identiski polinomi:} Ja $P(x)$ un $Q(x)$ ir $n$-tās pakāpes polinomi un to vērtības sakrīt $n+1$ dažādiem 
	$x_i$, tad $P(x)=Q(x)$. 
	\\ \hline  
	
	$P(x)=4x^3-3x^2-25x-6$ dalās ar $(x-3)$. 
	&  
	\cellcolor[HTML]{FFFFEE}
	Polinoms $P(x)$ dalās ar $(x-a)$ tad un tikai tad, ja $a$ ir $P(x)$ sakne. 
	\\  \hline
	
	
	$x^4 + 4 = $ \newline $=(x^2 - 2x + 2) \cdot$ \newline $\cdot (x^2 + 2x + 2)$
	& 
	\cellcolor[HTML]{FFFFEE}
	{\bf Sofijas-Žermēnas identitāte:}\newline ${\displaystyle a^4 + 4b^4 = \left( (a+b)^2 + b^2 \right)  \cdot \left( (a-b)^2 + b^2 \right)}$ 
	
	\\ \hline  
	Ja $a + b + c = 0$, tad \newline $a^3 + b^3 + c^3 = 3abc$. 
	& 
	\cellcolor[HTML]{FFFFEE}
	\textbf{3 kubu identitāte:} \newline
	${\displaystyle a^3 + b^3 + c^3 - 3abc = (a + b + c) \left( a^2 + b^2 + c^2 - ab - bc - ca \right).}$ \newline
	\textbf{Sekas:} $(x-y)^3 + (y-z)^3 + (z-x)^3 = 3(x-y)(y-z)(z-x)$.

	\\ \hline 
	
	\end{tabular*}
	}
	\end{table}
	



1. Novērtēt aritmētisko, ģeometrisko progresiju un progresiju summu augšanas ātrumu un attiecīgo formulu izvedumus. 
2. Pildīt Eiklīda algoritmu :math:`\operatorname{LKD}(a,b)` atrašanai, pamanīt atšķirības, 
   ja :math:`a`, :math:`b` ir/nav savstarpēji pirmskaitļi.   


Ievaduzdevumi
---------------

**4.1. Uzdevums (IMO1959.1):** 
  Pierādīt, ka daļa :math:`{\displaystyle \frac{21n + 4}{14n + 3}}` ir nesaīsināma katram naturālam :math:`n`.
  (Vispārinājums: kādus nosacījumus jāizpilda :math:`(a,b,c,d)`, 
  lai daļas :math:`{\displaystyle \frac{an+b}{cn+d}}` būtu nesaīsināmas.)

**4.2. Uzdevums (IMO1964.1):** 

  a. Atrast visus naturālos :math:`n`, kuriem :math:`2^n - 1` dalās ar :math:`7`. 
  b. Pierādīt, ka neeksistē tāds naturāls :math:`n`, kuram :math:`2^n+1` dalās ar :math:`7`. 




Spriedumu un aprēķinu piemēri
-------------------------------

1. Aritmētiskas progresijas atlikumi pēc fiksēta moduļa. 
2. Bezū identitāte.
3. LKD un savstarpēju pirmskaitļu jēdziens. 
4. MKD un LKD sakarību formulas. 
5. Eiklīda algoritms efektīvai LKD atrašanai, tā ātrdarbība. 
6. Eksponentfunkcijas veidotie atlikumi. 
7. Skaitļa :math:`a` multiplikatīvā kārta pēc moduļa :math:`m`.
8. Eiklīda algoritms LKD atrašanai. Bezū identitātes atrisināšana.  
9. Uzdevuma pārveidošana, reducējot uz citu uzdevumu.





Uzdevumi
-----------

**4.3. Uzdevums:** 
  Pierādīt, ka virkne :math:`1,11,111,\ldots` satur bezgalīgu apakšvirkni, 
  kuras katri divi locekļi ir savstarpēji pirmskaitļi.

**4.4. Uzdevums (AT_PL1980.1):** 
  Dotas trīs bezgalīgas aritmētiskas progresijas no naturāliem skaitļiem, 
  kurām katrs skaitlis :math:`1,2,3,4,5,6,7` un :math:`8` pieder vismaz vienai no tām. 
  Pierādīt, ka arī skaitlis :math:`1980` pieder vismaz vienai no tām.
	
**4.5. Uzdevums (IMO1996.1):** 
  Dots naturāls skaitlis :math:`r` un taisnstūrveida laukums :math:`ABCD` ar 
  izmēriem :math:`AB = 20`, :math:`BC = 12`. 
  Taisnstūris sadalīts ar režģa līnijām :math:`20 \times 12` vienības kvadrātos. 
  Atļauti sekojoši gājieni - var pārvietoties no viena kvadrāta uz citu tikai tad, 
  ja šo kvadrātu centru attālums ir :math:`sqrt{r}`. Uzdevums ir atrast gājienu virkni, 
  kas aizved no kvadrāta, kas satur virsotni "A" uz kvadrātu, kas satur virsotni "B".
	
  **(A)**
    Pierādīt, ka uzdevums nav izpildāms, ja :math:`r` dalās ar :math:`2` vai ar :math:`3`. 

  **(B)**
    Pierādīt, ka uzdevums ir izpildāms, ja :math:`r=73`. 
  
  **(C)**
    Vai uzdevums ir izpildāms, ja :math:`r=97`?

**4.6. Uzdevums:** 
  Aplūkojam naturālu skaitļu kopu:

  .. math::
	
    S = \{ ax+by \,\mid\, \mbox{$x,y$ ir veseli un $ax+by>0$} \}.
	
  Pamatot, ka šajā kopā eksistē minimālais elements :math:`d^{\ast}=ax^{\ast}+by^{\ast}` un 
  :math:`(x^{\ast},y^{\ast})` ir viens no Bezū identitātes atrisinājumiem. 


**4.7. Uzdevums (IMO1979.1):**
  Pieņemsim, ka :math:`p` un :math:`q` ir naturāli skaitļi, kuriem izpildās 
  :math:`\frac{p}{q}=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+ \ldots  -\frac{1}{1318}+\frac{1}{1319}`.
  Pierādīt, ka p dalās ar 1979.

**4.8. Uzdevums (IMO1981.4):** 

  **(A)** 
    Kuriem :math:`n>2` eksistē :math:`n` pēc kārtas sekojoši naturāli skaitļi, 
	kuriem lielākais skaitlis ir dalītājs mazākajam kopīgajam dalāmajam no pārējiem :math:`n-1` skaitļiem? 

  **(B)** 
    Kurai :math:`n>2` vērtībai ir tieši viena kopa ar šo īpašību?

**4.9. Uzdevums (IMO1991.4):**
  Pieņemsim, ka :math:`G` ir sakarīgs grafs ar :math:`k` šķautnēm. Pierādīt, 
  ka šķautnes var sanumurēt ar skaitļliem :math:`1,2,\ldots{},k` tā, ka jebkurā virsotnē, 
  kas pieder vismaz divām šķautnēm, visu tajā ienākošo šķautņu lielākais kopīgais dalītājs ir :math:`1`.

**4.10. Uzdevums:** 
  Visiem veseliem pozitīviem skaitļiem m>n pierādīt, ka 
  :math:`{\displaystyle MKD(m,n) + MKD(m+1,n+1) > \frac{2mn}{\sqrt{m-n}}}`.

