


--

## <lo-theory/>Skaitlis e

**Definīcija:** Par <emblue>naturālo 
logaritmu bāzi</emblue> jeb skaitli :math:`e` sauksim 
konstanti :math:`e = 2.7182818284\ldots`, uz kuru 
tiecas bezgalīgā summa:

.. math::

  e = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \ldots = 

.. math::

  = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \ldots.


--

## <lo-theory/>Naturālais logaritms

<hgroup>

![Graph of natural logarithm](natural-logarithm.png)<!-- .element: width="400px" -->

</hgroup>
<hgroup>

**Definīcija:** Par <emblue>naturālo logaritmu</emblue>
saucam logaritma funkciju ar bāzi :math:`e = 2.7182818284\ldots`:

.. math::

  \ln x = \log_{e} x.

:math:`y = \ln x` ir 
augoša funkcija, definēta visiem :math:`x > 0`.   
Naturālais logaritms ir īpašs ar to, ka 
tā grafiks :math:`x` asi krusto :math:`45^{\circ}` leņķī.

</hgroup>


--

## <lo-summary/>Mazākie 101-ciparu pirmskaitļi

<div style="font-size:70%">

![Marcis Bendiks](marcis-bendiks.png)<!-- .element: width="500px" -->

Ja saldējumu ar rozīnēm (vidēji :math:`5` rozīnes
uz vienu saldējuma masas vienību) vienmērīgi izmaisa, 
tad rozīņu skaits saldējuma vienībā pakļaujas
<emblue>Puasona sadalījumam</emblue>
(*Poisson distribution*) ar parametru :math:`\lambda=5`). 

Ja aplūkojam skaitļu porcijas pa :math:`100`, tad 
pie :math:`N=e^{20} \approx 485\,165\,195` 
šim skaitlim :math:`N` tuvajos :math:`100` skaitļu komplektos
būs vidēji :math:`5` pirmskaitļi (bet mēdz būt arī vairāk 
vai mazāk).

</div>


<!--

## <lo-summary/>Vizualizācija ar simtniekiem

TODO: Uzzīmēt tabuliņā :math:`5 \times 10` režģi
ar visiem nepāru skaitļiem. Iekrāsot tajā pirmskaitļus. 

-->

--

## <lo-yellow/>Mazākie 101-ciparu pirmskaitļi

* "Varbūtība", ka skaitlis, kas tuvu :math:`10^{100}` ir 
pirmskaitlis, apgriezti proporcionāla 
naturālajam logaritmam: :math:`\frac{1}{\ln 10^{100}}`. 

* Vidēji :math:`1000` skaitļu intervālā 
netālu no :math:`10^{100}` pirmskaitļu skaits:

.. math::

  1000 \cdot \frac{1}{\ln 10^{100}} = 
  1000 \cdot \frac{1}{100 \ln 10} \approx 
  \frac{10}{\ln 10} = 4.34.


--

## <lo-yellow/>Mazākie 101-ciparu pirmskaitļi

*Piemērs:* Intervālā 
:math:`{\displaystyle \left[ 10^{100},10^{100} + 1000 \right)}`
ir tikai :math:`2` pirmskaitļi: 
:math:`10^{100} + 267` un :math:`10^{100} + 949`.

Garākos intervālos pirmskaitļu īpatsvars
maz atšķiras no prognozes ar apgriezto naturālo 
logaritmu (t.i. vidēji 4.34 pirmskaitļi
uz katru tūkstoti): 

<table>
<tr><th>Intervāls</th><th>Pirmskaitļu skaits</th><th>Prognoze</th></tr>
<tr><td>:math:`[10^{100},10^{100} + 10^5)`</td>
<td>407</td><td>434.2945</td></tr>
<tr><td>:math:`[10^{100},10^{100} + 10^6)`</td>
<td>4248</td><td>4342.945</td></tr>
<tr><td>:math:`[10^{100},10^{100} + 10^7)`</td>
<td>43271</td><td>43429.45</td></tr>
</table>


Note:

Intervālā :math:`[x,x + \Delta x)` ir svarīgi, 
ka intervāla garums :math:`\Delta x`
ir daudz mazāks par :math:`x` (citādi 
pirmskaitļu blīvums intervāla iekšienē būtiski mainās). 
No otras puses, :math:`\Delta x` jābūt pietiekoši 
lielam, lai pirmskaitļu skaitu 
mazāk iespaidotu nejaušības.







--

## <lo-theory/>Bezū identitātes pierādījums - 1

**Bezū identitāte:**  Dots, ka :math:`a` un :math:`b` ir veseli un :math:`\text{LKD}(a,b)=d`. Tad eksistē
veseli skaitļi :math:`x` un :math:`y`, ka :math:`ax + by = d`.

**Pierādījums:** Aplūkojam kopu no visiem skaitļiem 
:math:`ax + by > 0`, kur :math:`x,y \in \mathbb{Z}`. Apzīmējam vismazāko pozitīvo šīs kopas locekli ar 
:math:`d^{\ast} = ax^{\ast} + by^{\ast}`, kur :math:`x^{\ast}` un :math:`y^{\ast}` ir tās :math:`x,y` vērtības, kurām 
šo minimumu izdevās sasniegt.



--

## <lo-theory/>Bezū identitātes pierādījums - 2

Pamatosim, ka minimālais :math:`d = ax^{\ast} + by^{\ast}` ir skaitļu 
:math:`a` un :math:`b` lielākais kopīgais dalītājs. 

* :math:`a` dalās ar :math:`d^{\ast}` bez atlikuma. Pretējā gadījumā būtu pozitīvs atlikums :math:`a` dalot ar :math:`r`:  
:math:`r = a - qd^{\ast}` (kur :math:`r < d^{\ast}`). Tas ir pretrunā ar to, ka :math:`d^{\ast}` 
bija *vismazākais* pozitīvais skaitlis formā :math:`ax+by`. 
Jo :math:`r` sanāktu vēl mazāks, ko arī var izteikt šādā formā. 
(Ar :math:`b` pamato līdzīgi.)
* Pieņemsim, ka :math:`c` arī ir skaitļu :math:`a,b` kopīgs dalītājs: :math:`a = cu` un :math:`b=cv`. Tad 

.. math::

  d^{\ast} = ax^{\ast} + by^{\ast} = cux^{\ast} + cvy^{\ast} = c(ux^{\ast} + vy^{\ast}).
  
Redzam, ka :math:`d^{\ast}` dalās ar :math:`c`. 

Tātad :math:`d^{\ast}` ir :math:`a` un :math:`b` lielākais kopīgais dalītājs. 


--

## <lo-summary/>Bezū identitātes interpretācija

**Apgalvojums:** Ja pircējam un pārdevējam pieejams
neierobežots daudzums monētu ar vērtībām 
:math:`n_1,n_2,\ldots,n_k` eirocenti (kuri visi :math:`n_i` ir 
naturāli skaitļi), tad ar tām 
var nomaksāt :math:`d`, kas ir visu skaitļu 
:math:`n_1,n_2,\ldots,n_k` lielākais kopīgais dalītājs.

**Pierādījums:** Šis apgalvojums diviem skaitļiem 
:math:`n_1` un :math:`n_2` tieši izriet no Bezū identitātes.  
Ja :math:`k>2`, var pamatot vispārīgāku Bezū identitātes
variantu (trim un vairāk skaitļiem), ko pierāda 
līdzīgi kā gadījumu :math:`k=2`. 


--

## <lo-summary/>Bezū identitātes interpretācija

**Piemērs:** Ar <red>:math:`13`</red> un <red>:math:`8`</red> 
centu monētām var nomaksāt 
:math:`1` centu (turklāt dažādos veidos - atkarībā no tā, 
kādas monētas lieto pircējs un kādas pārdevējs 
izdod kā atlikumu): 

.. math::

  \color{#F00}{13}\cdot{}5 - \color{#F00}{8}\cdot{}8 = 
  \color{#F00}{8}\cdot{}5 - \color{#F00}{13}\cdot{}3 = 1.

Atkārtojot šo operāciju, var nomaksāt arī jebkuru 
citu summu.

**Piemērs:** Ar <red>:math:`9`</red> un <red>:math:`15`</red> 
centu monētām var nomaksāt jebkuru summu :math:`3a`, kas
dalās ar <red>:math:`3`</red>, jo :math:`3 = \text{LKD}(9,15)`. 

