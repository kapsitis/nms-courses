1. Ievads skaitļu teorijā
==========================

**Sasniedzamie rezultāti un prasmes:** 

  1. Kopu un funkciju apzīmējumi. Injektīvas, sirjektīvas un bijektīvas funkcijas.
  2. Algebriskas identitātes. Pakāpju starpības formula, Sofijas-Žermēnas identitāte.
  3. Pirmskaitļu ir bezgalīgi daudz. Faktoriāli un atstarpes pirmskaitļu virknē. 
  4. Pierādījumi no pretējā. Labās sakārtotības (*Well-ordering*) princips. 
     Multiplikatīvā inversā eksistence ar Dirihlē principu. Nekonstruktīvi pierādījumi. 


.. raw:: latex

	\arrayrulecolor[HTML]{DB5800}
	\renewcommand{\arraystretch}{1.2}
	\begin{table}[ht!]\centering
	{\footnotesize    
	\begin{tabular*}{14.87cm}{@{}|p{5cm}p{9.00cm}|@{}} \hline    
	\headcol \multicolumn{2}{|c|}{\bf \normalsize Kopu un funkciju īpašības} \\ \hline 

  $f(n) = n^3 \pmod 7$. \newline
  $3 \not\equiv 5 \not\equiv 6 \pmod 7$, bet \newline
  $3^3 \equiv 5^3 \equiv 6^3 \equiv 6 \pmod 7$.
	&  
	\cellcolor[HTML]{FFFFEE} 
  Funkcijai $f$ argumentu pāris $(a_1,a_2)$ ir \textcolor{teal}{\em kolīzija}, ja $a_1 \neq a_2$, bet $f(a_1) = f(a_2)$, 
  t.i. dažādiem argumentiem vērtības "saskrienas".
	\\ \hline 


  $f(n) = 3n \pmod 7$. \newline
  Ja $n_1 \not\equiv n_2 \pmod 7$, tad arī \newline
  $3n_1 \not\equiv 3n_2 \pmod 7$.
	&  
	\cellcolor[HTML]{FFFFEE} 
	Funkcija $f$ ir \textcolor{teal}{\em injektīva}, ja no $a_1 \neq a_2$ seko, ka $f(a_1) \neq f(a_2)$, t.i. 
  nav kolīziju. 
	\\ \hline 

  Rotācijas funkcija, kas virknē pirmo ciparu aiznes uz beigām: 
  $\text{rot}(\mathtt{"1023"}) = \mathtt{"0231"}$ ir bijekcija, jo 
  var rotēt atpakaļ. 

	&  
	\cellcolor[HTML]{FFFFEE} 
	Funkcija $f$ ir \textcolor{teal}{\em bijektīva}, ja katram $b \in B$ ir tieši viens $a \in A$, 
  kam $f(a) = b$. \newline
  Vienāda izmēra kopām katra injektīva funkcija ir arī bijektīva.
	\\ \hline 


  Rotācijas funkcijai inversā atgriež pēdējo ciparu skaitļa sākumā:  \newline
  $\text{rot}^{-1}(\mathtt{"1234"}) = \mathtt{"4123"}$. 

	&  
	\cellcolor[HTML]{FFFFEE} 
	Par $f$ \textcolor{teal}{\em inverso funkciju} sauc $f^{-1}\,:\,B \mapsto A$, kas 
  katram $b \in B$ piekārto to $a \in A$, kam $f(a) = b$. \newline
  Tikai bijektīvām funkcijām eksistē inversās.
  \\ \hline 



  \headcol \multicolumn{2}{|c|}{\bf \normalsize Algebriskas identitātes} \\ \hline 
	
	$a^3 - b^3 = (a-b)(a^2 + ab + b^2)$. 
	&  
	\cellcolor[HTML]{FFFFEE} 
	\textbf{Pakāpju starpība (homogēnā forma):} $a^{n} - b^{n} =$ \newline 
	$=(a-b)(a^{n-1}+a^{n-2}b+\cdots+ab^{n-2}+b^{n-1})$. 
	\\ \hline 
	


	$a^3 - 1 = (a-1)(a^2 + a + 1)$. 
	&  
	\cellcolor[HTML]{FFFFEE} 
	\textbf{Pakāpju starpība (nehomogēnā forma):} $a^n - 1 =$ \newline 
	$ = (a-1)( a^{n-1} + a^{n-2} + \ldots + a + 1)$. 
	\\ \hline 

	
	$a^3 + b^3 = (a+b)(a^2 - ab + b^2)$. &
	\cellcolor[HTML]{FFFFEE}
	\textbf{Nepāru pakāpju summa:} $a^{2n+1} + b^{2n+1} =$ \newline 
  $ = (a+b)(a^{2n}-a^{2n-1}b+\cdots-ab^{2n-1}+b^{2n})$. 
	\\ \hline 
	
		
	$a^4 + 4 = $ \newline $=(a^2 - 2a + 2) \cdot  (a^2 + 2a + 2)$
	& 
	\cellcolor[HTML]{FFFFEE}
	{\bf Sofijas-Žermēnas identitāte (homogēnā forma):}\newline 
  ${\displaystyle a^4 + 4b^4 = \left( (a+b)^2 + b^2 \right)  \cdot \left( (a-b)^2 + b^2 \right)}$ jeb \newline
  ${\displaystyle a^4 + 4b^4 = \left( a^2 + 2ab + b^2 \right)  \cdot \left( a^2 -2ab + 2b^2 \right)}$
	
	\\ \hline  

  \headcol \multicolumn{2}{|c|}{\bf \normalsize Pirmskaitļi} \\ \hline 

  \multicolumn{2}{|l|}{
  Pirmskaitļu $2,3,5,\ldots$ ir bezgalīgi daudz. 
  } \\
  \multicolumn{2}{|l|}{
  (No pretējā: ja būtu galīgs skaits, tad $p_1p_2\cdots{}p_k+1$ nedalītos ne ar vienu no tiem.)
  }
	\\ \hline  


  \multicolumn{2}{|l|}{
  Eksistē cik patīk garas $\mathbb{N}$ apakšvirknes bez pirmskaitļiem.
  } \\
  \multicolumn{2}{|l|}{
  (Piemēram, $(m+1)!+2, (m+1)!+3, (m+1)!+(m+1)$ satur $m$ saliktus skaitļus.)
  }
	\\ \hline  

	$2023 = 7^117^2$, \newline 
  $2024 = 2^311^123^1$, \newline 
  $2025=3^45^2$.
	& 
	\cellcolor[HTML]{FFFFEE}
	\textbf{Aritmētikas pamatteorēma:} Katru $n \in \mathbb{N}$ var tieši vienā veidā izteikt kā pirmskaitļu 
  pakāpju reizinājumu: $n=p_1^{a_1}p_2^{a_2}\cdots{}p_k^{a_k}$. 	
	\\ \hline  



	\end{tabular*}
	}
	\end{table}
	


Kopas un funkcijas
---------------------


Kopas parasti apzīmē ar lielajiem burtiem, piemēram, :math:`A,B,X,Y`, 
kopu elementus apzīmējam ar mazajiem burtiem.
Pazīstamās skaitļu kopas apzīmējam ar treknajiem burtiem, piemēram, 
:math:`\mathbb{N} = \{1,2,3,\ldots \}` ir naturālo skaitļu kopa, 
:math:`\mathbb{Z} = \{ \ldots, -3,-2,-1,0,1,2,3,\ldots \}` ir veselo skaitļu 
kopa, :math:`\mathbb{Q}` ir visu racionālo skaitļu kopa (skaitļi, kas uzrakstāmi 
kā racionālās daļas), 
:math:`\mathbb{R}` ir visu reālo skaitļu kopa (uzrakstāmi kā bezgalīgās decimāldaļas). 

**Definīcija:** 
  Par *funkciju* no kopas :math:`A` kopā :math:`B` 
  sauc attiecību starp šo kopu elementiem, kas katram :math:`a \in A` piekārto 
  tieši vienu elementu :math:`b \in B`.  Šādu funkciju pieraksta :math:`f\,:\,A\mapsto{}B`.


**Piemēri:** 
  Ja katram Latvijas pastāvīgajam iedzīvotājam (cilvēku kopā :math:`A`) 
  ir piešķirts personas kods (11-ciparu ciparu virknīšu kopā :math:`B`), 
  tad attēlojums :math:`f`, kas katram cilvēkam piekārto personas kodu, ir 
  funkcija. Savukārt, tāds attēlojums, kas katram cilvēkam piekārto viņa vārdu, nav 
  funkcija, ja pieļaujam, ka cilvēkam var būt vairāki vārdi. (Toties funkcija ir tāds 
  attēlojums, kas katram cilvēkam piekārto visus viņa vārdus.)

**Definīcija:** 
  Par *injektīvu funkciju* :math:`f\,:\,A\mapsto{}B` sauc tādu funkciju, kas uz katru 
  :math:`b \in B` attēlo ne vairāk kā vienu elementu :math:`a \in A`. 
  Tātad, ja :math:`a_1 \neq a_2`, tad :math:`f(a_1) \neq f(a_2)`.

**Definīcija:** 
  Par *kolīziju* funkcijai :math:`f\,:\,A\mapsto{}B` sauc tādus divus elementus 
  :math:`a_1,a_2 \in A`, kam :math:`a_1 \neq a_2`, bet :math:`f(a_1) = f(a_2)`.
  (Injektīvām funkcijām atbilstoši definīcijai kolīziju nevar būt.)

**Piemērs:** 
  Ja Latvijas iedzīvotājam piešķirtais personas kods ir unikāls, 
  tad funkcija, kas piekārto personas kodus ir injektīva. 
  Kolīzija šajā funkcijā rastos vienīgi tad, ja diviem dažādiem cilvēkiem izsniegtu 
  vienādus personas kodus -- cilvēku pēc viņa koda nevarētu viennozīmīgi noteikt. 

**Definīcija:** 
  Par *bijektīvu funkciju* :math:`f\,:\,A\mapsto{}B` sauc tādu funkciju, kas uz katru 
  :math:`b \in B` attēlo tieši vienu elementu :math:`a \in A`. 

**Piemērs:** 
  Personas koda piešķiršanas funkcija nav bijektīva, ja aplūko visus 
  11-ciparu skaitļus kā iespējamos kodus -- eksistē neizmantoti kodi. 
  No 11 cipariem varētu izveidot 100 miljardus dažādu kodu -- daudz vairāk nekā ir iedzīvotāju. 
  Šo funkciju varētu padarīt par bijektīvu vienīgi tad, ja kopa :math:`B` ir 
  faktiski izsniegtie personas kodi nevis visas ciparu virknes vajadzīgajā garumā.


**Definīcija:**
  Par bijektīvas funkcijas :math:`f\,:\,A\mapsto{}B` *inverso funkciju* 
  :math:`f^{-1}\,:\,B\mapsto{}A` sauc tādu funkciju, kas attēlo kopu :math:`B` atpakaļ 
  kopā :math:`A` un katram :math:`b \in A` atrod to :math:`a \in A`, 
  kuram :math:`f(a) = b`. 

**Piemēri:**

  **(A)**
    Kvadrātfunkcija, :math:`f\,:\,\mathbb{R} \mapsto \mathbb{R}`, kas definēta ar formulu 
    :math:`f(x) = x^2` katru reālu skaitli kāpina kvadrātā. 
    Šī funkcija nav injektīva, jo tai eksistē kolīzijas: :math:`f(-2) = f(2) = 4`. 

  **(B)**
    Ja kvadrātfunkciju definē tikai nenegatīviem argumentiem :math:`\mathbb{R}_{0+} = [0;+\infty)`, 
    tad tā ir injektīva, jo nenegatīvu skaitļu kvadrāti visi atšķiras (parabolas labais zars). 
    Tomēr kvadrātfunkcija :math:`f\,:\,\mathbb{R}_{0+}\mapsto{}\mathbb{R}` nav bijektīva: 
    ne katrs reāls skaitlis ir kāda skaitļa kvadrāts: kolīziju šai funkcijai nav 
    (katram reālam skaitlim iedur ne vairāk kā viena bultiņa), bet uz negatīviem reāliem skaitļiem 
    nekas neattēlojas -- tiem neiedur neviena bultiņa. 

  **(C)** 
    Visbeidzot, ja kvadrātfunkciju definē kā attēlojumu no reāliem nenegatīviem uz reāliem nenegatīviem 
    skaitļiem :math:`f\,:\,\mathbb{R}_{0+}\mapsto{}\mathbb{R}_{0+}`, tad tā ir bijektīva. 
    Šīs funkcijas inversā funkcija ir kvadrātsakne: :math:`f^{-1}(x) = \sqrt{x}`. 
    Tādēļ kvadrātsakne ir definēta tikai nenegatīviem skaitļiem un pieņem nenegatīvas vērtības. 


  **(D)** 
    Ir iespējama bijektīva funkcija no vaļēja intervāla 
    :math:`(-\pi/2;\pi/2)` uz visu reālo skaitļu taisni: :math:`\mathbb{R} = (-\infty;\infty)`. 
    Šāda funkcija ir, piemēram, tangenss: :math:`f\,:\,(-\pi/2;\pi/2)\mapsto(\mathbb{R})`, 
    kas definēts ar formulu :math:`{\displaystyle f(x) = \tan x = \frac{\sin x}{\cos x}}`. 
    (Tangenss ir definēts arī citām reālām :math:`x` vērtībām, ja tās nav vienādas ar 
    :math:`\pi/2 + \pi \cdot k` veseliem :math:`k`, kur saucējā esošais kosinuss ir :math:`0`.)

    Inversajai funkcijai, ko sauc par *arktangensu* izmanto tikai vienu no šīs funkcijas zariem. 
    Tā ir bijektīva funkcija, kas attēlo taisni :math:`\mathbb{R}` par galīgu intervālu 
    :math:`(-\pi/2;\pi/2)`. Katrs reāls skaitlis ar arktangensa funkciju attēlojas par unikālu skaitli 
    šajā galīgajā intervālā. 


  **(E)** 
    Funkcija, kas reizina ar nenulles atlikumu pēc pirmskaitļa moduļa ir bijektīva. 
    Piemēram, reizināšana ar :math:`a \neq 0` pēc pirmskaitļa :math:`p=7` moduļa ir bijektīva: 

    ================  ====  ====  ====  ====  ====  ====  ====  
    :math:`n`         0     1     2     3     4     5     6
    :math:`f(n)=3n`   0     3     6     2     5     1     4
    :math:`f(n)=4n`   0     4     1     5     2     6     3
    ================  ====  ====  ====  ====  ====  ====  ====  

    Ievērojiet, ka vienalga, vai reizina ar :math:`3` vai ar :math:`4` (vai jebkuru citu 
    atlikumu, kas nedalās ar :math:`7`) reizināšanas tabulas rindiņā visi atlikumi ir dažādi. 

  **(F)** 
    Funkcija, kas reizina ar nenulles atlikumu :math:`a \neq 0` pēc salikta skaitļa moduļa ir bijektīva tad 
    un tikai tad, ja :math:`a` un modulis ir savstarpēji pirmskaitļi. 
    Piemēram, reizināšana pēc :math:`p=9` moduļa var būt un var nebūt bijektīva: 

    ================  ====  ====  ====  ====  ====  ====  ====  ====  ==== 
    :math:`n`         0     1     2     3     4     5     6     7     8
    :math:`f(n)=3n`   0     3     6     0     3     6     0     3     6
    :math:`f(n)=4n`   0     4     8     3     7     2     6     1     5
    ================  ====  ====  ====  ====  ====  ====  ====  ====  ====

    Reizinot ar :math:`3` pēc moduļa :math:`9`, iegūstam nevis deviņus, bet tikai trīs atlikumus 
    (:math:`0,3,6`) un daudzas kolīzijas. Savukārt, reizinot ar :math:`4` iegūstam bijektīvu attēlojumu,
    kas ir 


**Apgalvojums:** 
  Dotas divas galīgas kopas :math:`A` un :math:`B`, kurās ir vienāds skaits elementu (:math:`|A|=|B|`). 
  Ja funkcija :math:`f\,:\,A\mapsto{}B` ir injektīva, tad šī funkcija ir arī bijektīva. 

**Pierādijums:** 
  Ja eksistētu tāds :math:`b \in B`, par kuru neattēlojas neviens :math:`a \in A`, 
  tad kopā :math:`B` būtu mazāk nekā :math:`|B| = |A|` elementu, par kuriem attēlojas 
  kopas :math:`A` elementi. Pēc Dirihlē principa būs divi tādi elementi :math:`a_1,a_2 \in A`, 
  kuri attēlosies par vienu un to pašu elementu no :math:`B`, jo kopas :math:`A`
  elementu ir vairāk nekā iespējamo attēlu. Tā ir kolīzija un tāpēc šāda funkcija 
  :math:`f` nevar būt arī injektīva. Iegūta pretruna. :math:`\blacksquare`



**Definīcija:** 
  Par skaitļa :math:`a` *multiplikatīvi inverso* pēc moduļa :math:`m` saucam tādu 
  skaitli :math:`a^{-1}`, kas apmierina sakarību :math:`a \cdot a^{-1} \equiv 1 \pmod m`. 

  Multiplikatīvi inversie eksistē tikai tad, ja :math:`m` un :math:`a` ir savstarpēji pirmskaitļi. 
  (Ja :math:`m` ir pirmskaitlis, tad multiplikatīvi inversais eksistē katram :math:`a \neq 0`). 

**Piemēri:** 

  **(A)**
    Pēc pirmskaitļa moduļa :math:`m=7` ir seši multiplikatīvi inversie: 

    .. math::
    
      1^{-1} \equiv 1,\;\; 2^{-1} \equiv 4,\;\; 3^{-1} \equiv 5,\;\; 4^{-1} \equiv 2, \;\; 5^{-1} \equiv 3,\;\; 6^{-1} \equiv 6 \pmod 7. 

    Multiplikatīvi inversais :math:`0^{-1}` pēc moduļa :math:`7` nav definēts, jo :math:`0` reizinot 
    ar jebko, nevar iegūt atlikumu :math:`1`. 

  **(B)**
    Pēc moduļa :math:`m=10` ir četri multiplikatīvi inversie: 

    .. math::

      1^{-1} \equiv 1,\;\; 3^{-1} \equiv 7,\;\; 7^{-1} \equiv 3,\;\; 9^{-1} \equiv 9 \pmod {10}.


**Apgalvojums:** 
  Katram pirmskaitlim :math:`p` un katram :math:`a \not\equiv 0 \pmod p` eksistē 
  inversais :math:`a^{-1}`. 

**Pierādījums:** 
  Pamatosim, ka funkcija :math:`f(n) = an`, kas katram atlikumam pēc moduļa :math:`p`
  (:math:`n \in \{ 0,\ldots,p-1 \}`) piekārto citu atlikumu no tās pašas kopas 
  :math:`\{ 0,\ldots,p-1 \}`, ir bijektīva. 

  Šī funkcija ir injektīva, jo pieņemot, ka :math:`a n_1 \equiv a n_2 \pmod p` iegūsim, ka 
  :math:`a n_1 - a n_2 \equiv 0 \pmod p` jeb :math:`a(n_1 - n_2)` dalās ar :math:`p`. 
  Tā kā :math:`a \not\equiv 0 \pmod p`, tad vienīgi :math:`(n_1 - n_2) \equiv 0 \pmod p`, jeb
  iegūstam, ka :math:`n_1` un :math:`n_2` ir viens un tas pats atlikums. 

  Pēc agrāka apgalvojuma šī funkcija  :math:`f(n) = an` ir arī bijektīva. 
  Tātad katram skaitlim (tai skaitā arī :math:`1 \in \{ 0,\ldots,p-1 \}`) eksistē 
  kāds skaitlis :math:`n'`, kurš par viņu attēlojas: :math:`f(n') \equiv 1 \pmod p`. 
  Šis arī ir multiplikatīvi inversais skaitlim :math:`a` pēc moduļa :math:`p`. 
  :math:`\blacksquare`





Pirmskaitļi
-----------------------

**Definīcija:**
  Naturālu skaitli :math:`p>1` sauc par *pirmskaitli*, 
  ja vienīgie tā dalītāji ir :math:`1` un :math:`p`.
  Naturālus skaitļus :math:`n>1`, kas nav pirmskaitļi, sauc par
  *saliktiem skaitļiem*.


  .. note:: 
     Skaitlis :math:`1` nav ne pirmskaitlis, ne arī salikts skaitlis.
     Tas ir *vienības elements* naturālu skaitļu reizināšanā.
     Veselo skaitļu pasaulē arī :math:`-1` ir vienības elements.


**Piemērs:** 
  Intervālā :math:`[1;100]` ir :math:`25` pirmskaitļi:

  ===  ===  ===  ===  ===
    2    3    5    7   11
   13   17   19   23   29
   31   37   41   43   47
   53   59   61   67   71
   73   79   83   89   97
  ===  ===  ===  ===  ===


**Teorēma (Eiklīds):**
  Pirmskaitļu ir bezgalīgi daudz.

**Pierādījums:**
  No pretējā. Ja pirmskaitļu būtu
  galīgs skaits, tad eksistētu lielākais pirmskaitlis
  :math:`p_K`. Sareizinām visus pirmskaitļus, pieskaitām :math:`1`:

  .. math::

    P = p_1 \cdot p_2 \cdot p_3 \cdot \ldots \cdot p_K + 1.

  :math:`P` nedalās ne ar vienu no pirmskaitļiem, kuri ir galīgajā
  sarakstā: vienmēr atlikums :math:`1`. Vai nu :math:`P` pats ir pirmskaitlis
  vai kādu (sarakstā neesošu) pirmskaitļu reizinājums. Pretruna.
  :math:`\blacksquare`



**Apgalvojums:**
  Katram naturālam :math:`N` eksistē :math:`N` pēc kārtas sekojoši skaitļi, kuri visi ir salikti. 

**Pierādījums:**
  :math:`N` pēc kārtas sekojošus saliktus skaitļus var
  atrast šādi: Aprēķinām :math:`(N+1)!` un izrakstām šādus skaitļus: 

  .. math:: 

    (N+1)! + 2,\; (N+1)! + 3,\; \ldots,\; (N+1)! + (N+1). 

  Šie ir :math:`N` pēc kārtas sekojoši skaitļi, no kuriem pirmais dalās ar :math:`2`
  (jo :math:`(N+1)!` un :math:`2` dalās ar :math:`2`), otrais dalās ar :math:`3` utt. 
  Pēdējais no skaitļiem dalās ar :math:`(N+1)`. Tātad neviens no tiem nav pirmskaitlis.
  :math:`\blacksquare` 


**Piemērs:** 
  Pietiekami lielas atstarpes starp pirmskaitļiem novērojamas arī daudz mazākiem skaitļiem. 
  Piemēram, :math:`113` un :math:`127` abi ir pirmskaitļi, bet starp tiem ir :math:`13` 
  salikti skaitļi intervālā :math:`[114;126]`. 

  Var izmantot :math:`14! = 87178291200` kā apgalvojuma pierādījumā, un tad intervālā 
  :math:`[87178291202;87178291214]` arī būs :math:`13` pēc kārtas sekojoši salikti skaitļi. 



Pierādījumi no pretējā
------------------------

**Definīcija:** 
  Skaitļu kopa :math:`A` ir *labi sakārtota* (*well-ordered*) ja katrai tās 
  netukšai apakškopai :math:`S \subseteq A` ir mazākais elements. 

**Piemēri:** 

  **(A)** 
    Naturālo skaitļu kopa :math:`\mathbb{N}` ir labi sakārtota. 
    Jebkurā netukšā naturālu skaitļu apakškopā :math:`S \subseteq \mathbb{N}` atradīsies mazākais skaitlis. 
    (To var pārbaudīt, izvēloties jebkuru :math:`n_1 \in S`. Vai nu :math:`n_1` jau ir mazākais kopas 
    :math:`S` elements, vai arī eksistē kāds :math:`n_2 \in S`, kas ir par to vēl mazāks: :math:`n_2 < n_1`. 
    Atkārto to pašu spriedumu skaitlim :math:`n_2` un tā tālāk. Pēc kāda laika būsim atraduši mazāko kopas 
    :math:`S` skaitli, jo nevar eksistēt bezgalīgi dilstoša virkne :math:`n_1 > n_2 > n_3 > \ldots` tikai 
    no naturāliem skaitļiem). 

  **(B)** 
    Veselo skaitļu kopa :math:`\mathbb{Z}` nav labi sakārtota. 
    Ja izvēlas netukšu :math:`\mathbb{Z}` apakškopu, kurā ir bezgalīgi daudz negatīvu skaitļu, tad 
    starp tiem nevarēs atrast pašu mazāko. Par katru negatīvu skaitli eksistēs 
    vēl mazāks. 

  **(C)** 
    Reālo skaitļu nogrieznis :math:`[0;1]` nav labi sakārtots. 
    Pašā nogrieznī :math:`[0;1]` eksistē mazākais elements :math:`0`. Bet izvēloties 
    vaļēju intervālu kā apakškopu, piemēram, :math:`(0;1) \subseteq [0;1]`, vairs nevarēs 
    izvēlēties mazāko pozitīvo skaitli. Ja izvēlamies :math:`\varepsilon \in (0;1)`, tad 
    izdalot ar :math:`2`, iegūsim :math:`\varepsilon/2 \in (0;1)`, kas arī ir pozitīvs 
    skaitlis un :math:`\varepsilon/2 < \varepsilon`. Var konstruēt bezgalīgu 
    virkni ar skaitļiem, kuri kļūst arvien mazāki un tuvojas nullei -- neviens starp tiem 
    nebūs vismazākais. 

Labās sakārtotības īpašība naturālajiem skaitļiem ļauj veidot pierādījumus, kuri 
līdzīgi matemātiskās indukcijas metodei, bet atklātas indukcijas vietā izmanto 
pierādījumu no pretējā. 


**Apgalvojums:** 
  Katram naturālam skaitlim :math:`n > 1` eksistē kāds pirmreizinātājs :math:`p`, t.i. pirmskaitlis
  kurš dala skaitli :math:`n` bez atlikuma. 


**Pierādījums:** 
  No pretējā. Iedomāsimies, ka eksistē tāda netukša kopa :math:`S \in \mathbb{N}`, kas satur tādus 
  skaitļus :math:`n > 1`, kuriem nav neviena pirmreizinātāja. 
  No kopas :math:`\mathbb{N}` labās sakārtotības secinām, ka netukšajā kopā :math:`S` eksistē 
  mazākais elements :math:`n \in S`. 

  Skaitlis :math:`n` nevar būt pirmskaitlis, jo citādi tas būtu pats sev pirmreizinātājs. 
  Tāpēc tas ir salikts skaitlis :math:`n=ab`. Bet tādā gadījumā arī skaitļiem :math:`a` un 
  :math:`b` nevar būt pirmreizinātāji (citādi ar tiem dalītos arī skaitlis :math:`n`). 
  Tāpēc arī :math:`a,b \in S`. Bet šie abi skaitļi ir mazāki nekā :math:`n`, kas ir pretruna ar to, 
  ka :math:`n` bija izraudzīts kā kopas :math:`S` mazākais elements. :math:`\blacksquare`






Uzdevumi
---------

**1.1.uzdevums:**
  (*Multiplikatīvi inversie*) 
  
    **(A)**
      Aplūkot rēbusu  :math:`\mathtt{XX???} \cdot 13 = \mathtt{XXX001}`, kur 
      "X" un "?" vietā var būt jebkādi cipari. Kuri cipari jāliek jautājumzīmju vietā, lai vienādība 
      būtu pareiza?

    **(B)**
      Izmantojot punktā (A) atrastos ciparus, atrisināt arī citus līdzīgus rēbusus, piemēram, 
      :math:`\mathtt{XX???} \cdot 13 = \mathtt{XXX123}`.


**1.2.uzdevums:** 
  (*Labā sakārtojuma princips.*)  Katrā netukšā naturālu skaitļu kopā ir mazākais elements. 
  (Kopa var būt galīga vai bezgalīga; tajā var neeksistēt lielākais elements, bet mazākais vienmēr eksistē.)

  **(A)** 
    Kurš ir lielākais naturālais skaitlis :math:`S`, 
    ko nevar izteikt formā :math:`S = 3n + 5m`, kur :math:`n,m` ir veseli nenegatīvi skaitļi.

  **(B)**
    Kādā valstī ir trīs veidu monētas: 
    :math:`6`, :math:`9` un :math:`20` centu vērtībā. Kāda ir lielākā naudas summa :math:`S`, 
    ko nevar samaksāt tikai ar šādām monētām? Ar monētām maksā tikai pircējs, atlikumu izdot nedrīkst.

  **(C)**
    Izmantot labā sakārtojuma principu, lai pamatotu, ka :math:`S` tiešām ir mazākā summa, ko nevar 
    samaksāt ar norādīto vērtību monētām. 


**1.3.uzdevums:**
  (*Bezgalīga 2D tabula ar neparastu īpašību*)

  .. figure:: figs-intro-to-number-theory/infinite-quadrant.png
     :width: 1.5in

  **(A)**
    Bezgalīgajā rūtiņu kvadrantā iekrāsot daļu no rūtiņām zilas tā, lai 
    katrā kolonnā visas, izņemot galīgu skaitu, rūtiņas nebūtu iekrāsotas zilas, bet katrā 
    rindiņā visas, izņemot galīgu skaitu, rūtiņas būtu zilas. 

  **(B)**
    Vai eksistē bezgalīga 
    stingri augoša naturālu skaitļu virkne :math:`a_1 < a_2 < a_3 <\ldots`, 
    ka jebkuram fiksētam naturālam skaitlim :math:`a` virknē :math:`a_1+a, a_2+a, a_3 + a,\ldots` 
    ir tikai galīgs skaits pirmskaitļu? 


**1.4.uzdevums (AMO1987.10.5):** 
  (*Stratēģijas nozagšana un nekonstruktīvi pierādījumi.*)
  Divi spēlētāji pēc kārtas raksta uz tāfeles naturālus skaitļus, kas nepārsniedz 10. 
  Aizliegts rakstīt tādus skaitļus, kas ir jau uzrakstīto skaitļu dalītāji. 
  Zaudē tas, kas nevar izdarīt gājienu. 
  
  **(A)**
    Vai uz tāfeles var rakstīt skaitli 1? 
    Kurš spēlētājs to var rakstīt? Vai šis skaitlis ir kāds no gājieniem uzvarošajā stratēģijā?
    Pamatot, kurš no abiem spēlētājiem, pareizi spēlējot, uzvar. Stratēģija **nav** jānorāda. 
  
  **(B)**
    Noskaidrot, kuram spēlētājam ir uzvaroša stratēģija, un atrast to.
	

**1.5.uzdevums (Mersenna skaitļi):**
  Apzīmējam :math:`M_n = 2^n -1`. Pierādīt, ka :math:`M_n` var būt pirmskaitlis tikai tad, ja 
  arī :math:`n` ir pirmskaitlis. (Tas ir *nepieciešamais*, bet ne *pietiekamais* nosacījums. 
  Piemēram, :math:`M_{11} = 2047 = 23 \cdot 89` nav pirmskaitlis.)


.. only:: Internal 

  **Atbilde:** 

    Ja :math:`n = km` ir divu naturālu
    skaitļu reizinājums (turklāt :math:`k>1` un :math:`m>1`),
    tad var sadalīt reizinātājos kā :math:`a^m - b^m`:

    .. math::

      \begin{gathered}
      M_n = 2^{km} - 1 = \left( 2^k \right)^m - 1^m = \\
      = (2^k - 1) \left( (2^k)^{m-1} + \ldots + 1 \right).
      \end{gathered}

  :math:`\square`


**1.6.uzdevums (A.Engel 6.E1):**
  Ja :math:`n > 1`, tad :math:`n^4 + 4^n` nevar būt pirmskaitlis. 



