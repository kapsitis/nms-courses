2. Modulārā aritmētika
=========================

**Sasniedzamie rezultāti un prasmes:** 

  1. Vienkāršu lineāru kongruenču risināšana, piereizināšana ar multiplikatīvi inverso. 
  2. Modulārās aritmētikas funkciju apraksts ar tabulām. 
  3. Multiplikatīvi inversā atrašana ar uzminēšanu vai gadījumu pārlasi. 
  4. Vienādojumu risināšana veselos skaitļos ar pretrunas moduli. 
  5. Dalāmības pazīme ar :math:`9` modulārās aritmētikas pierakstā. 

.. raw:: latex

	\arrayrulecolor[HTML]{DB5800}
	\renewcommand{\arraystretch}{1.2}
	\begin{table}[ht!]\centering
	{\footnotesize    
	\begin{tabular*}{14.87cm}{@{}|p{5cm}p{9.00cm}|@{}} \hline    
	\headcol \multicolumn{2}{|c|}{\bf \normalsize Pretrunas moduļi} \\ \hline 

  $a^2 = 8b + 5$ nav atrisinājumu, \newline
  jo $a^2 \equiv 0,1,4 \pmod 8$, bet \newline 
  $8b + 5 \equiv 5 \pmod 8$. 
	&  
	\cellcolor[HTML]{FFFFEE} 
  Vienādojumam $f(a,b,c) = g(a,b,c)$ nav atrisinājumu veselos skaitļos, ja var atrast moduli $m$, 
  kuram $f(a,b,c)$ jebkurām $a,b,c$ vērtībām dod citu atlikumu (mod $m$) nekā $g(a,b,c)$.  
	\\ \hline 

  $a^2 \equiv 0,1 \pmod 3$ \newline
  $a^2 \equiv 0,1,4 \pmod 5$ \newline
  $a^2 \equiv 0,1 \pmod 4$ \newline
  $a^2 \equiv 0,1,4 \pmod 8$. 
	&  
	\cellcolor[HTML]{FFFFEE} 
  Pilniem kvadrātiem $a^2$ piemēroti pretrunas moduļi -- visi nepāra pirmskaitļi 
  vai $m=4$ un $m=8$.   
	\\ \hline 

  $a^3 \equiv 0,1,6 \pmod 7$ \newline
  $a^3 \equiv 0,1,8 \pmod 9$. 
	&  
	\cellcolor[HTML]{FFFFEE} 
  Pilniem kubiem $a^3$ piemēroti pretrunas moduļi -- $m=7$ un $m=9$.   
	\\ \hline 



  \end{tabular*}
	}
	\end{table}
	


Uzdevumi
---------

**2.1.uzdevums:** 
  Atrast moduli, pie kura dotajam vienādojumam veselos skaitļos nav atrisinājuma. 
  Atrisinājumā minēt moduli :math:`m` kas ļauj atrast pretrunu. 
  Norādīt, kuriem atlikumiem (pēc `m` moduļa) var būt kongruenta kreisā puse, 
  kuriem atlikumiem var būt kongruenta labā puse un kāpēc tās nevar būt vienādas.

    (A) :math:`x^2 - 5y^2 = 6`,
    (B) :math:`15x^2 - 7y^2 = 9`,
    (C) :math:`x^2 - 2y^2 + 8z = 19`,
    (D) :math:`x^3 + y^3 + z^3 = 1969^2`,
    (E) :math:`x^2 + y^2 = 8z + 6`,
    (F) :math:`x^2 + 8z = 2y^2 + 3`,
    (G) :math:`x^4 - 12y^4 = 24`,
    (H) :math:`11^x - 8^y = 1`.

**2.2.uzdevums:** 
  Vai pilna kvadrāta ciparu summa var būt (A) :math:`3`, (B) :math:`7`, (C) :math:`2024`?

**2.3.uzdevums:** 
  Dots polinoms :math:`P(n)` ar veseliem koeficientiem un pirmskaitlis :math:`p`. 
  Pierādīt, ka jebkuram naturālam :math:`n` skaitlis :math:`P(n)+P(n+1)+\ldots{}+P(n+p-1)` dalās ar :math:`p`.


**2.4.uzdevums (BW.2018.18):** 
  Dots tāds naturāls skaitlis :math:`n \geq 3`, ka :math:`4n+1` ir pirmskaitlis. 
  Pierādiet, ka :math:`n^{2n}-1` dalās ar :math:`4n+1`.

**2.5.uzdevums (BW.2016.1):** 
  Atrast visus pirmskaitļu pārus :math:`(p,q)`, kuriem :math:`p^3 - q^5 = (p+q)^2`.
	
**2.6.uzdevums (BWTST.2018.13):** 
  Vai eksistē tāds pirmskaitlis :math:`q`, ka nevienam pirmskaitlim :math:`p` skaitlis 
  :math:`\sqrt[3]{p^2 + q}`  nav naturāls?


