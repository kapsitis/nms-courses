Apsveikuma lapa, 2022-11-18
========================================

.. ...............
.. TODO for tests.
.. ...............
.. Daži aprēķini - tsk. ar pakāpēm
.. Kongruenču vienādojumi
.. Pretrunas modulis

.. Eiklīda lemma
.. Bezū identitāte.


**Uzdevums:**

  Aplūkojam visas bezgalīgās naturālu skaitļu virknes

  .. math::

    f(1),f(2),f(3),\ldots.

  Formāli runājot, tās ir funkcijas no naturāliem skaitļiem uz naturāliem skaitļiem:
  Katra virkne ir funkcija :math:`f\,:\,\mathbb{N}\rightarrow\mathbb{N}$, where $\mathbb{N}=\{1,2,3,\ldots\}`.
  Atrast, kvantoru izteiksmēm atbilstošos vārdiskos aprakstus.
  (*Tulkošana no predikātu un kvantoru valodas uz cilvēku valodu.*)





  **(A)**
    :math:`\exists a \in \mathbb{N}\ \exists b \in \mathbb{N}\ \forall c \in \mathbb{N}\ (c \geq a\ \rightarrow\ f(c+b)=f(c))`

  **(B)**
    :math:`\exists a \in \mathbb{N}\ \exists b \in \mathbb{N}\ \forall c \in \mathbb{N}\ \left( f(c+b)=f(c)\ \rightarrow\ c \geq a \right)`

  **(C)**
    :math:`\forall a \in \mathbb{N}\ \exists b \in \mathbb{N}\ \forall c \in \mathbb{N}\ (c \geq a\ \rightarrow\ f(c+b)=f(c))`.


  **(D)**
    :math:`\forall c \in \mathbb{N}\ \forall a \in \mathbb{N}\ \exists b \in \mathbb{N}\ (c > a\ \rightarrow f(c+b) = f(c))`.

  **(E)**
    :math:`\exists a \in \mathbb{N}\ \forall b \in \mathbb{N}\ \forall c \in \mathbb{N}\ \left( b \leq a \rightarrow f(c+b) = f(c) \right)`.

  **(F)**
    :math:`\forall a \in \mathbb{N}\ \forall c \in \mathbb{N}\ \exists b \in \mathbb{N}\ (c \geq a\ \rightarrow\ f(c+b)=f(c))`.

  **(G)**
    :math:`{\displaystyle \forall n \in \mathbb{N}\ \exists i \in \mathbb{N}\ \exists j \in \mathbb{N} \Big( a_i = n \wedge a_j = n \wedge i \neq j \bigwedge \forall k \in \mathbb{N} \big(a_k = n \rightarrow (k = i \vee k = j \big) \Big). }`


  **(H)**
      :math:`{\displaystyle \forall n \in \mathbb{N}\ \forall i \in \mathbb{N}\ \Big( a_i = n \rightarrow \forall M \in \mathbb{N}\ \exists k \in \mathbb{N}\ \big(k > M \wedge a_k = n \big) \Big).}`


  **(I)**
      :math:`\exists b_0 \in \mathbb{Z}\ \exists d \in \mathbb{N}\ \exists M \in \mathbb{N}\ \forall k \in \mathbb{N} \big( k > M \rightarrow a_k = b_0 + k \cdot d \big).`





**Daži atbilžu varianti:**

Atbildes uz iepriekšējiem punktiem var izskatīties, piemēram, šādi (dažreiz virkņu apraksti
nav doti; tad tie jāformulē no jauna).

1. Virknes, kurās katrs naturāls skaitlis ir sastopams vismaz divas reizes.
2. Virknes, kurās katrs naturāls skaitlis ir sastopams bezgalīgi daudzas reizes.
3. Virknes, kurās katrs naturāls skaitlis ir sastopams tieši divas reizes.
4. Virknes, kuras vai nu vispār nesatur attiecīgo naturālo skaitli kā locekli, vai arī
   satur to bezgalīgi daudzas reizes.
5. Virknes, kuras sakrīt ar kādu aritmētisku progresiju (izņemot, varbūt, galīgu skaitu locekļu).
6. Virknes, kuras, sākot ar kādu vietu ir periodiskas.
7. Visas naturālo skaitļu virknes
8. Virknes, kuras ir konstantas.
9. Virknes, kuras ir konstantas (izņemot, varbūt, galīgu skaitu locekļu).
10. Virknes, kuras ir injektīvas (katrs naturāls skaitlis tajās sastopams ne vairāk kā vienreiz jeb
    nekādas divas vērtības tajās neatkārtojas).
11. Virknes, kuras ir sirjektīvas (katrs naturāls skaitlis tajās sastopams vismaz vienreiz).
12. Virknes, kuras ir bijektīvas (katrs naturāls skaitlis tajās sastopams tieši vienreiz).
13. Tukša kopa (attiecīgajai definīcijai neatbilst neviena virkne).
14. Virknes, kuras ir stingri augošas (katrs nākamais loceklis lielāks par iepriekšējo).
15. Virknes, kuras ir neaugošas (katrs nākamais loceklis nepaŗsniedz iepriekšējo).
16. Virknes, kurām ir robeža, ja :math:`n` tiecas uz bezgalību.
17. Stingri augošas virknes, kurās bezgalīgi bieži var atrast blakusesošus locekļus,
    kuru starpība ir :math:`2` (kā *dvīņu pirmskaitļu* hipotēzē).
18. Virknes, kuras ir neperiodiskas (neeksistē tāds periods, ka virkne no kādas vietas ir periodiska
    ar šo periodu).
