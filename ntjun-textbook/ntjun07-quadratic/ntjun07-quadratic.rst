NMS Skaitļu teorija #7: Kvadrātiskas kongruences
========================================================




Lineāras rekurences
---------------------

Ievads
^^^^^^^

Iracionāli skaitļi 
reizēm dabiski parādās uzdevumos par veselu skaitļu aritmētiku. Un arī otrādi -- iracionālu 
skaitļu aritmētika algebras un analīzes likumsakarību dēļ noved atpakaļ pie rezultātiem 
veselos skaitļos. Šajā nodaļā aplūkosim dažus piemērus ar rekurentām virknēm, 
kur tas izpaužas. Sāksim ar piemēriem. 

**Definīcija:** 
  Fibonači skaitļu virkni definē šādi: 
  
  .. math:: 
    
    F(n) = \left\{ \begin{array}{ll}
    0, & \mbox{ja $n = 0$},\\
    1, & \mbox{ja $n = 1$},\\
    F(n-1) + F(n-2), & \mbox{ja $n \geq 2$}.\\
    \end{array} \right.
    
  Virknes pirmie locekļi ir šādi: 
  
  .. math:: 
  
    0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,\ldots
    
Vērtībām :math:`n \geq 1` var aprēķināt attiecības :math:`\frac{F(n+1)}{F(n)}`. 
Ja :math:`n \rightarrow \infty`, šīs attiecības konverģē uz iracionālu skaitli, kas pazīstams kā zelta griezums. 

**Apgalvojums:** 
  Fibonači skaitļiem izpildās sekojoša robeža:
  
  .. math:: 
  
    \lim_{n \rightarrow \infty} \frac{F(n+1)}{F(n)} = \frac{1 + \sqrt{5}}{2} \approx 1.618033988749895
    

Zelta griezums, kas iegūstams no :math:`\sqrt{5}`, nav izņēmums. 
Daudzas citas izteiksmes ar kvadrātsaknēm ir iegūstamas no veselu skaitļu virknēm. 


**Piemērs:**
  Aprēķinām ģeometriskas progresijas :math:`b_n = (1 + \sqrt{2})^n` locekļus.
  Labākai lasāmībai noapaļojam ar precizitāti līdz :math:`10^8`. 

  .. code-block:: python

    >>> import math
    >>> [round((1+math.sqrt(2))**n,8) for n in range(0,20)]
    [1.0, 2.41421356, 5.82842712, 14.07106781, 
    33.97056275, 82.01219331, 197.99494937, 478.00209204, 
    1153.99913345, 2786.00035894, 6725.99985132, 16238.00006158, 
    39201.99997449, 94642.00001057, 228485.99999562, 551614.00000181, 
    1331713.99999925, 3215042.00000031, 7761797.99999986, 18738638.00000003]
 
  Noapaļojot virknes locekļus līdz tuvākajiem veselajiem skaitļiem, iegūsim jau veselu skaitļu virkni 

  .. code-block:: python
  
    >>> import math
    >>> [round((1+math.sqrt(2))**n) for n in range(0,20)] 
    [1, 2, 6, 14, 34, 82, 198, 478, 1154, 2786, 
    6726, 16238, 39202, 94642, 228486, 551614, 1331714, 3215042, 7761798, 18738638]
    
  Šīs virknes divu pēc kārtas sekojošu locekļu dalījuma robeža ir :math:`1 + \sqrt{2}`. 
  Šai virknei ļoti līdzīgu (atšķiras tikai pats pirmais loceklis) var definēt ar rekurentu sakarību: 
  
  .. math:: 
  
    Q(n) = \left\{ \begin{array}{ll}
    2, & \mbox{ja $n = 0$},\\
    2, & \mbox{ja $n = 1$},\\
    2Q(n-1) + Q(n-2), & \mbox{ja $n \geq 2$}.\\
    \end{array} \right.
  
  Sākot ar trešo locekli, katru nākamo iegūst pieskaitot divkāršotam pēdēam loceklim pirmspēdējo.
  Šīs virknes locekļus sauc par Pella-Lūkasa skaitļiem, sk. `<https://bit.ly/3JDiTU9>`_.
  



Otrās kārtas lineārās rekurences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aplūkosim rekurentu virkni (virkni, kurā nākamos locekļus var izrēķināt no iepriekšējiem locekļiem). 

**Definīcija:** 
  Otrās kārtas lineāru homogēnu rekurenci definē ar diviem sākumnosacījumiem un sakarību,
  kas nākamos locekļus izsaka kā lineāru izteiksmi no diviem iepriekšējiem:

  .. math:: 

    x_n = \left\{ \begin{array}{ll}
    c_0, & \mbox{ja $n = 0$,}\\
    c_1, & \mbox{ja $n = 1$,}\\
    ax_{n-1} + bx_{n-2}, & \mbox{ja $n \geq 2$.}\\
    \end{array} \right.
    

**Apgalvojums:** 
  Ja kvadrātvienādojumam :math:`r^2 - a - b = 0` ir divas dažādas reālas saknes 
  :math:`r_1` un :math:`r_2`, tad virknes :math:`x_n` vispārīgo locekli var izteikt ar sakarību

  .. math:: 

    x_n = \alpha_1 \cdot r_1^n + \alpha_2 \cdot r_2^n,

  kur :math:`\alpha_1` un :math:`\alpha_2` var izteikt, zinot virknes sākumnosacījumus :math:`c_1` un :math:`c_2`. 



**Piemērs:** 
  Aplūkosim kvadrātvienādojumu, kuram ir divas saknes:
  
  .. math:: 
  
    r_1 = 1 + \sqrt{2}\;\;\mbox{un}\;\; r_2 = 1 - \sqrt{2}.
    
  Pēc Vjeta teorēmas, kvadrātvienādojums ar šādām saknēm ir :math:`r^2 - 2r - 1 = 0`. 
  Ievietojam konstantes :math:`\alpha_1 = \alpha_2 = 1`. 
  Uzrakstām formulu :math:`\alpha_1 r_1^n + \alpha_2 r_2^n`, ievietojot šīs konstantes:
  
  .. math:: 

    x_n = (1 + \sqrt{2})^n + (1 - \sqrt{2})^n. 

  Šāda formula izsaka rekurentu sakarību: 

  .. math:: 
  
    x_n = \left\{ \begin{array}{ll}
    2, & \mbox{if $n=0$,}\\
    2, & \mbox{if $n=1$,}\\
    2 x_{n-1} + x_{n-2}, & \mbox{if $n \geq 2$.}\\
    \end{array} \right.
    
    
  Šīs virknes piemērs bija minēts arī ievadā -- tie ir Pella-Lūkasa skaitļi.
  
  
**Piemērs:** 
  Aplūkosim Fibonači skaitļu virkni, kas definēta jau augstāk ar šādu sakarību: 
  
  .. math:: 
    
    F(n) = \left\{ \begin{array}{ll}
    0, & \mbox{ja $n = 0$},\\
    1, & \mbox{ja $n = 1$},\\
    F(n-1) + F(n-2), & \mbox{ja $n \geq 2$}.\\
    \end{array} \right.

  Mēģināsim izteikt Fibonači virknes locekļus kā ģeometriskas progresijas :math:`F(n) = r^n` locekļus. 
  (Beigās izrādīsies, ka Fibonači virkne ir nevis viena ģeometriska progresija, bet gan divu 
  ģeometrisku progresiju summa, turklāt otrā no ģeometriskajām progresijām strauji tiecas uz :math:`0`.)
  
  Apzīmējam :math:`F(n) = r^n`. Pārrakstām Fibonači skaitļu rekurento sakarību: 
  
  .. math:: 
  
    F(n) = F(n-1) + F(n-2),\;\;\mbox{jeb}\;\; r^n = r^{n-1} + r^{n-2},\;\;\mbox{jeb}\;\; r^2 = r + 1. 
    
    
  Risinām kvadrātvienādojumu :math:`r^2 - r - 1 = 0`. 
  
  .. math:: 
  
    r_{1,2} = \frac{1 \pm \sqrt{1 - 4 \cdot 1 \cdot (- 1)}}{2} = \frac{1 \pm \sqrt{5}}{2}.
    
  Atbilstoši augstāk minētajai teorēmai, varam izteikt vispārīgo Fibonači virknes locekli sekojoši: 
  
  .. math:: 
  
    F(n) = \alpha_1 \left( \frac{1 + \sqrt{5}}{2} \right)^n + \alpha_2 \left( \frac{1 - \sqrt{5}}{2} \right)^n. 
    
    
  Lai izpildītos abi sākumnosacījumi (:math:`F(0) = 0` un :math:`F(1) = 1`), nepieciešams lai :math:`\alpha_1 = \alpha_2 = \frac{1}{\sqrt{5}}`. 
  Ievietojam abas šīs vērtības, lai iegūtu Fibonači skaitļu izteiksmi:
  
  .. math:: 
  
    F(n) = \frac{1}{\sqrt{5}} \left( \frac{1 + \sqrt{5}}{2} \right)^n + \frac{1}{\sqrt{5}} \left( \frac{1 - \sqrt{5}}{2} \right)^n.
  




**Piemērs:**
  Aprēķinām Fibonači virknes locekļus, izmantojot formulu ar kvadrātsaknēm un eksponentfunkciju:
  
  .. code-block python

    >>> import math
    >>> [round((1/math.sqrt(5))*((1 + math.sqrt(5))/2)**n) for n in range(0,20)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
    
  Šajā aprēķinā otru kvadrātsaknes izteiksmi :math:`{\displaystyle \left( \frac{1 - \sqrt{5}}{2} \right)^n}` var nemaz nerakstīt, var uzreiz 
  noapaļot līdz tuvākajam veselajam skaitlim. 

.. note:: 
  Precīzai Fibonači skaitļu rēķināšanai lieliem :math:`n`, augšminētā metode nav optimāla, 
  jo reālo skaitļu (ts. *peldošā punkta*) aritmētika neizbēgami saistīta ar noapaļošanas kļūdām. 
  Ļoti lieliem skaitļiem kāpināšānas rezultāts izmantos peldošā punkta reizinātāju :math:`10^k`, 
  un jaunākie cipari tā pierakstā būs noapaļoti. Var notikt arī peldošā punkta reģistra pārpildīšanās.   
  Tāpēc Fibonači skaitļus praktiskāk rēķināt ar rekurento formulu (saskaitot abus iepriekšējos virknes locekļus).
  
  
  
