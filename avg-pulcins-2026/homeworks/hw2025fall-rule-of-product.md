# Mājasdarbs A: Reizināšanas likums kombinatorikā

**A1.uzdevums:** Apskatām regulāru $(2n+1)$-stūri.
Cik ir trijstūru ar virsotnēm $(2n+1)$-stūra virsotnēs, 
kuri satur $(2n+1)$-stūra centru?

**Atrisinājums:** Fiksēsim vienu virsotni $A$. No tās uz dažādām 
pusēm atliksim lokus, kuru galapunktus uzskatīsim par trijstūra 
virsotnēm $B, C$. Par vienības loku uzskatīsim $2\pi/(2n+1)$.

Tātad lokus $AB$ un $AC$ raksturosim ar naturāliem skaitļiem 
$x$ un $y$, kas parāda, cik vienības lokus tie satur. Lai trijstūris 
$ABC$ saturētu daudzstūra centru, jāizpildās nevienādībām $x \le n$, $y \le n$, 
$x + y \ge n + 1$. Šos nosacījumus apmierina šādi pāri: 
$(1, n)$, $(2, n-1)$, $(2, n)$, $(3, n-2)$, $(3, n-1)$, $(3, n)$, $\ldots$, $(n, n)$. 
Viegli aprēķināt, ka to skaits ir $1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}$. 
Tātad prasīto trijstūru skaits ir $\frac{n(n+1)(2n+1)}{6}$.


**A2.uzdevums:** 
Atrast cik ir nedeģenerētu trijstūru, kam visas virsotnes pieder kopai 

$$\{(s,t)\in \mathbb{Z}\mid 0\le s\le 4,\ 0\le t\le 4\}.$$

![](5x5dots.png)

*Piezīme:* Trijstūri sauc par "nedeģenerētu", ja tam visas trīs virsotnes 
neatrodas uz vienas taisnes (ja tas ir parasts trijstūris ar pozitīvu laukumu). 

**Atrisinājums:** Trīs punktus norādītajā kvadrātā var izvēlēties 
$C_{25}^{3}$ veidos. Saskaitīsim, cik no šiem trijniekiem veido 
deģenerētu trijstūri, t.i., kur visi 3 punkti atrodas uz vienas taisnes. 

Vertikālajā un horizontālajā virzienā tādu trijnieku ir $10\cdot C_{5}^{3}$. 
Paralēli galvenajām diagonālēm ir vēl 
$2\cdot\bigl(2\cdot C_{3}^{3}+2\cdot C_{4}^{3}+C_{5}^{3}\bigr)$ trijnieki. 
Virzienos $(1,\pm2)$, $(2,\pm1)$ var izvēlēties vēl $4\cdot4=16$ trijniekus. 
Citos virzienos 3 punktus uz vienas taisnes izvēlēties nevar. 
Atņemot no kopīgā trijnieku skaita trijnieku skaitu, kas atrodas uz vienas 
taisnes, iegūstam kopējo nedeģenerēto trijstūru skaitu. Tas ir $2152$.