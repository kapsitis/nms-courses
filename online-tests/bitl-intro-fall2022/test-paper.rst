FYS Pre-assessment Test
=================================================

Welcome to the RBS Intro Week!
This test covers reading, reasoning and quantitative skills that
may appear in the First Year Seminar (FYS) and other classes.
It is a preliminary activity to estimate the
progress you have made during the study year.
This test does not entail any obligations
and will not affect your grades.

The total time for this test is **45 minutes**.
You may use Internet and calculators, but should not communicate with
other people during this test.

For each question enter a short answer (typically, a number) or select an answer variant (A,B,C,D).
The topics covered by this test include algorithmic procedures,
spatial reasoning, integer arithmetic, combinatorics and counting, probabilities and statistics.



**Question 1**

  There is a rectangle consisting of :math:`5 \times 7` little squares.
  How many little squares are cut by its diagonal?
  (A little square is cut by a line, iff the square is separated in two parts;
  touching a square's vertex does not count.)

  *Write an integer:* __________.

.. only:: Internal

  **Answer:**

  ``11``

  Note that numbers :math:`5` and :math:`7` are *mutually prime* --
  they are not divisible by any integer :math:`d > 1`.
  Therefore the diagonal does not go through any internal square vertices.
  Every time the diagonal crosses into another little square, it goes to
  a neighboring square to the right or upwards from the current one.
  Consequently, you will cross some grid-line exactly :math:`(5 - 1) + (7-1)`
  times -- the diagonal needs to go :math:`4` steps to the right and
  :math:`6` steps upwards -- to reach the top-right corner from the
  bottom left corner.

  Since the diagonal is in the lower left corner (before
  crossing any grid-lines), the number of crossed squares will be
  larger by one: :math:`(5 - 1) + (7-1) + 1 = 11`.

  .. figure:: figs-bitl-intro-fall2022/diagonals.png
     :width: 3in

     Diagonal in :math:`5 \times 7` in :math:`6 \times 9` rectangles.

  As shown in the figure, the number of crossed squares need to be
  counted differently, if there is a common divisor of width and height.
  For example, in :math:`6 \times 9` rectangle, the number of crossed little
  squares is not :math:`(6 - 1) + (9 -1) + 1 = 14`. Instead, it is smaller by
  :math:`2` (since in two places it can simultaneously cross the horizontal
  and vertical gridlines).


  :math:`\square`



**Question 2**
  There is a rectangle consisting of :math:`w \times h` little squares, where
  :math:`w` is the width and :math:`h` is the height.
  Let :math:`N` denote the number of squares cut by its diagonal?
  Which of the following statements is always true?

  .. image:: figs-bitl-intro-fall2022/question2-rectangle-diag.png
     :width: 1.7in


  **(A)**
    :math:`N = w + h - 1`

  **(B)**
    :math:`N \leq w + h - 1`

  **(C)**
    :math:`N \geq w + h - 1`

  **(D)**
    Either :math:`N = w + h - 1` or :math:`N = w + h + 1`

  *Select an answer (A,B,C,D):* __________.

.. only:: Internal

  **Answer:**

  ``(B)``

  The number of crossed squares must satisfy :math:`N \leq w + h -1`.
  If :math:`w` and :math:`h` do not have any common divisors (they are mutually prime),
  then :math:`N = w + h - 1`.

  If they do have common divisors, then the diagonal of the large rectangle
  goes through some square vertices -- i.e. it can proceed to the next level up or to the right
  without cutting any little squares. In those cases :math:`N < w + h - 1`.

  :math:`\square`





**Question 3**
  What digit should be written instead of :math:`y` so that the resulting number
  :math:`\overline{5783y1y0}` is divisible by :math:`90`?

  (The number has eight digits, and two of them
  are equal to some unknown digit :math:`y`.)

  *Write a digit (0 - 9):* __________.


.. only:: Internal

  **Answer:**

  ``6``

  Since the number ends with :math:`0` (and must be divisible by :math:`10`),
  it must be also divisible by :math:`9`. In that case it will be divisible by :math:`90` as well.
  A divisibility rule says that a number is divisible by :math:`9` if and only if
  the sum of its digits is divisible by :math:`9`.
  In our case :math:`5 + 7 + 8 + 3 + y + 1 + y + 0 = 24 + 2y` must be divisible by :math:`9`.
  The two closest candidates that are larger than :math:`24` and are still divisible by :math:`9`
  are :math:`27` and :math:`36`.

  We cannot solve :math:`24 + 2y = 27` for integer :math:`y`.
  But we can solve :math:`24 + 2y = 36` (we must have :math:`2y = 12` or :math:`y = 6`).

  :math:`\square`


**Question 4**

  Which statement expresses exactly the same property as this one:
  "A positive integer :math:`N` is divisible by :math:`144`"?


  **(A)**
    :math:`N` is divisible by both :math:`4` and :math:`36`.

  **(B)**
    :math:`N` is divisible by both :math:`6` and :math:`24`.

  **(C)**
    :math:`N` is divisible by both :math:`8` and :math:`18`.

  **(D)**
    :math:`N` is divisible by both :math:`9` and :math:`16`.

  *Select an answer (A,B,C,D):* __________.



.. only:: Internal

  **Answer:**

  ``(D)``

  If some number is simultaneously divisible by :math:`9` and :math:`16`,
  then it must also be divisible by their product :math:`9 \cdot 16 = 144`.
  This happens because :math:`9` and :math:`16` are mutually prime.

  Other answers do not work.
  For example, :math:`N = 36` is divisible by both :math:`4` and :math:`36`,
  but clearly :math:`N = 36` is not divisible by :math:`144`.

  :math:`\square`



**Question 5:**
  What is the least number of candies Joe needs, if he wants to distribute them to his :math:`10` friends
  so that every friend gets some candy and no two friends should get equal number of candies.
  (Only whole candies are handed out -- they cannot be cut into pieces.)

*Write a positive integer:* __________.


.. only:: Internal

  **Answer:**

  ``55``

  The smallest numbers of candies can be :math:`1,2,\ldots,10` respectively (nobody should get less than :math:`1` candy,
  and no two numbers can be equal).
  The total of all these numbers is :math:`1 + 2 + \ldots + 10 = 55`.

  :math:`\square`


**Quesiton 6:**
  In order to feed his pet rats, Joe needs either :math:`x` apples, or :math:`y` bananas or :math:`z` peaches.
  (Combining different types of fruit is not allowed.)
  Somebody brought Joe a random collection of :math:`N` fruit; every fruit in the collection
  is either an apple, a banana or a peach.
  What is the least value of :math:`N` to guarantee that Joe's rats can be fed (no matter what are the counts of
  apples, bananas and peaches).

  **(A)**
    :math:`N = x + y + z - 3`,

  **(B)**
    :math:`N = x + y + z - 2`,

  **(C)**
    :math:`N = x + y + z - 1`,

  **(D)**
    :math:`N = x + y + z`.

  *Select an answer (A,B,C,D):* __________.


.. only:: Internal

  **Answer:**

  ``(B)``

  The worst case scenario is when Joe gets :math:`x-1` apples, :math:`y-1` bananas and :math:`z-1` peaches
  (in this case he is one piece short for every kind of fruit).
  This adds up to :math:`(x-1) +  (y-1) + (z-1) = x+y+z - 3`. Such value :math:`N` clearly does not guarantee
  feeding the rats, so answer **(A)** does not work.

  As soon as Joe gets at least :math:`N = x+y+z-2` fruit, at least one kind of fruit will be sufficient to feed the rats.

  :math:`\square`


**Quesiton 7:**
  Consider the following inequalities between rational numbers:

  .. math::

    \frac{2}{5} < \frac{5}{12} < \frac{3}{7} < \frac{4}{9} < \frac{1}{2}.

  Find a fraction :math:`\frac{p}{q}` that is in-between the following two of these fractions:
  :math:`{\displaystyle \frac{3}{7} < \frac{p}{q} < \frac{4}{9}}`.
  Since there are many such fractions, try to find one with the smallest denominator :math:`q`.

  *Write your answer as a fraction p/q:* __________.


.. only:: Internal

  **Answer:**

  ``7/16``

  (Partial credit is also given for other numbers in this interval. For example, the
  average of both fractions: :math:`(3/7 + 4/9)/2 = 55/126`, which does not have the smallest
  denominator.)

  It is easy to check that :math:`\frac{3}{7} < \frac{7}{16}` (since :math:`3 \cdot 16 < 7 \cdot 7`).
  And also :math:`\frac{7}{16} < \frac{4}{9}` (since :math:`7 \cdot 9 < 4 \cdot 16`).

  Why is :math:`\frac{7}{16}` the "optimal" fraction? Could we have some other fraction :math:`\frac{p}{q}`
  where the denominator :math:`q < 16`?

  Any fraction :math:`\frac{p}{q}` in-between :math:`\frac{3}{7}` and :math:`\frac{4}{9}`
  needs to satisfy the system of inequalities:

  .. math::

    \left\{
    \begin{array}{l}
    3q < 7p \\
    9p < 4q \\
    \end{array}
    \right. \;\;\mbox{(multiply equations by :math:`9` and :math:`7` respectively)}\;\;
    \left\{
    \begin{array}{l}
    27q < 63p \\
    63p < 28q \\
    \end{array}
    \right.

  Combine both inequalities and get :math:`27q < 63p < 28q`.
  In other words, find some :math:`q` such that in the interval :math:`(27q,28q)` there is
  a number divisible by :math:`63`. These intervals :math:`(27q,28q)` have length :math:`q`
  (they become longer as :math:`q` grows).

  We can now build a little table, where in the first row
  :math:`q` takes all values :math:`1,2,\ldots`, but in the second row
  we find the remainders when :math:`28q` is divided by :math:`63`.
  In mathematical notation it is :math:`28q\,\text{mod}\,63`, where "mod" is the remainder operator.




  ===========================  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====
  :math:`q`                    1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18
  ===========================  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====  ====
  :math:`28q\,\text{mod}\,63`  28    56    21    49    14    42    7     35    0     28    56    21    49    14    42    7     35    0

  For :math:`q = 16` for the first time the remainder :math:`7` is smaller than :math:`q = 16`. Therefore
  the denominator :math:`q = 16` is the smallest possible for a fraction that satisfies
  :math:`{\displaystyle \frac{3}{7} < \frac{p}{q} < \frac{4}{9}}`.


  :math:`\square`


**Question 8:**
  You have two positive fractions :math:`{\displaystyle \frac{a}{b} < \frac{c}{d}}` (where all the integers
  :math:`a,b,c,d` are positive). How to estimate the smallest possible difference :math:`\Delta` between
  these fractions: :math:`{\displaystyle \Delta = \frac{c}{d} - \frac{a}{b}}`?

  **(A)**
    :math:`\Delta` may equal :math:`{\displaystyle \frac{1}{ac}}`, but is never smaller than that.

  **(B)**
    :math:`\Delta` may equal :math:`{\displaystyle \frac{1}{bd}}`, but is never smaller than that.

  **(C)**
    :math:`\Delta` may equal :math:`{\displaystyle \frac{1}{a^2 + c^2}}`, but is never smaller than that.

  **(D)**
    :math:`\Delta` may equal :math:`{\displaystyle \frac{1}{b^2 + d^2}}`, but is never smaller than that.

  *Select an answer (A,B,C,D):* __________.


.. only:: Internal

  **Answer:**

  ``(B)``

  Apply algebra to subtract two fractions:

  .. math::

    \frac{c}{d} - \frac{a}{b} = \frac{cb - ad}{bd} > 0.

  The smallest non-zero value of :math:`cb - ad` is :math:`1`, so the difference between
  the two fractions can never be smaller than :math:`\frac{1}{bd}`.
  It can be equal to that number. For example, :math:`\frac{1}{3} - \frac{1}{4} = \frac{1}{12}`.

  For other answer variants it is possible to find counterexamples -- differences between
  the two fractions that are smaller than
  the given number.


  :math:`\square`


**Question 9:**
  A robot moves along the perimeter :math:`ABC` (see image), the length of each side is :math:`2` cm.
  The robot starts at the vertex :math:`A` and travels exactly :math:`2023` centimeters.
  (Every time the robot reaches a vertex, it makes a :math:`120^{\circ}` turn to the right.)
  How many full rotations around the vertical axis were completed by the robot during this travel?
  (If robot completes some fractional number of rotations, then keep the integer part only.)

  .. image:: figs-bitl-intro-fall2022/triangle.png
     :width: 2in

  *Write your answer as an integer:* __________.

.. only:: Internal

  **Answer:**

  ``337``

  The perimeter of the triangle is :math:`6` centimeters.
  The robot does :math:`337` full circles around the triangle plus one more centimeter,
  since :math:`2023 = 337 \cdot 6 + 1`.

  This means that there were :math:`337` full rotations (as the robot traverses
  entire perimeter, it makes three :math:`120^{\circ}` turns which is one
  full rotation by :math:`360^{\circ}` degrees.)

  :math:`\square`



**Question 10:**
  In a factory there are boxes with screws.

  * The first box contains :math:`160` thousand screws.
  * The number of screws in the second box are fewer by one fifth compared to the first box.
  * The number of screws in the third box are fewer by one fifth compared to the second box.
  * The number of screws in the fourth box are fewer by one fifth compared to the third box.

  Estimate the difference of the number of screws in
  the first and the fourth box.

  **(A)**
    less than :math:`10000`,

  **(B)**
    from :math:`10000` to :math:`99999`

  **(C)**
    from :math:`100000` to :math:`999999`

  **(D)**
    At least :math:`1000000`.


  *Select an answer (A,B,C,D):* __________.

.. only:: Internal

  **Answer:**

  ``(B)``

  To verify do the calculation:

  .. math::

    160000 - 160000 \cdot \left( \frac{4}{5} \right)^3 = 160000 \cdot \left( 1 - \frac{64}{125} \right) = 160000 \cdot \frac{61}{125} = 1280 \cdot 61.

  It is easy to see that this product is a five-digit number; thus it belongs to :math:`{\displaystyle \left( 10000; 99999 \right)}`.

  :math:`\square`



**Question 11:**
  What is the area of the surrounding rectangle, if the perimeter of the shape made of six circles is :math:`18\pi`?

  .. image:: figs-bitl-intro-fall2022/circles.png
     :width: 2in

*Write your answer as a positive number:* __________.

.. only:: Internal

  **Answer:**

  ``54``

  A single circle has perimeter :math:`3\pi`; since the perimeter of any circle equals :math:`2\pi{}R`,
  so :math:`R = 1.5`. The diameter of the circle is :math:`3` -- and that is also the height of the
  rectangle.

  The width of the rectangle is :math:`6` times larger -- it is :math:`18`;
  so the area of the rectangle is :math:`3 \times 18 = 54`.

  :math:`\square`


**Question 12:**
  On a remote planet each month lasts exactly :math:`42` days; and each month starts on a Friday.
  Find a date (a number from :math:`1` to :math:`42`) which is simultaneously satisfies
  three properties: (A) It is odd, (B) it is divisible by :math:`3`, (C) it is on Tuesday.

  .. image:: figs-bitl-intro-fall2022/calendar.png
     :width: 2in

  *Write the date (as an integer number):* __________.


.. only:: Internal

  **Answer:**

  ``33``

  You can simply count the dates onwards (e.g. all dates on Tuesdays?) until you find it.

  In a more general sense, we want a date (number) :math:`N` to satisfy three mathematical properties:

  * Gives remainder :math:`1` when divided by :math:`2` (is odd)
  * Gives remainder :math:`0` when divided by :math:`3` (i.e. divisible by :math:`3`)
  * Gives remainder :math:`5` when divided by :math:`7`, since all the dates
    with this remainder (:math:`5,12,19,26,\ldots`) are on Tuesday.

  As it turns out, all the divisors :math:`2,3,7` are pairwise mutual primes (no two of them
  have any common divisor larger than :math:`1`).
  *Chinese Remainder theorem* guarantees that among the numbers :math:`\{1,2,\ldots,42\}`
  there must be exactly one which gives the remainders we need.

  Note that :math:`42` was chosen as :math:`2 \cdot 3 \cdot 7`.
  If you pick it that way, you can get **any** set of three remainders
  (when dividing by :math:`2`, :math:`3`, and :math:`7`).

  :math:`\square`
