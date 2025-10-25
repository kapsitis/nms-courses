FYS Pre-assessment Test
=================================================

Welcome to the RBS Intro Week! 
This test is a preliminary activity and could help to reveal the 
progress you will make during the study year.
It does not entail any obligations
and will not affect your grades in any way.
Please, do not use Internet or calculators and and do not communicate with 
other people during this test!

For each question enter a short answer. 
It is highly recommended that you also provide a brief explanation, 
how did you arive to that answer.
The topics covered by this test include logic and algorithmic processes,
integer arithmetic, combinatorics, probabilities and statistics. 



**Question 1**

  .. image:: figs/function-graphs.png
     :width: 200 px

  Graphs of functions :math:`f(x)=x^2 - 7x + 10` and :math:`g(x) = x - 4` are shown. 
  Define function :math:`h(x)`:
  
  .. math::
  
     h(x) = \sqrt{\left( x^2 - 7x + 10 \right) \left( x - 4 \right)}.

  Find the domain of :math:`h(x)`.
  (The *domain* of a function is the set of all those :math:`x` for which the function is defined.)
  Write your answer as a set -- number intervals or their unions.
      
  **Answer:** :math:`x \in [2;4] \cup [5; +\infty)`  
  
  **Analysis:** The expression :math:`f(x)g(x)` under square root should be non-negative.

    * Either the graphs of :math:`f(x)` and :math:`g(x)` are both :math:`\geq 0` (true for :math:`x \in [5; +\infty)`)
    * Or the graphs of both functions are both :math:`\leq 0` (true for :math:`x \in [2;4]`)
  
  Zero argument is also fine for the square root, so all interval endpoints (2,4, and 5) are included.

  :math:`\square`
  
  .. note:: 
    Question is more about sorting the cases than it is about polynomials 
    (what is the product of two positive numbers, two negative numbers, a positive and a negative number).


  **Grading Criteria:**
  
    * Wrong answers, no explanation -- 0 points. 
    * Misunderstood problem (substituded one polynomial into another, solved equation :math:`f(x)=g(x)`, 
      required that :math:`f(x) \neq 0`) -- 0 or 1 points.
    * Roots :math:`x=2,x=4,x=5` found, but not used to find domain -- 1 point. 
    * Solved inequality :math:`f(x) \geq 0` (instead of :math:`f(x)g(x) \geq 0`) -- 2 points. 
    * Factorized the expression as :math:`f(x)g(x) = (x-2)(x-4)(x-5)` -- 2 points. 
    * Drawings that show signs of :math:`f(x)`, :math:`g(x)`, but no intervals -- 3 points. 
    * Intervals correct, but some interval endpoints (:math:`x=2,4,5`) not included -- 4 points. 
    * Just a correct answer -- 4 points.
    * Everything correct and a minimal explanation (e.g. :math:`f(x)g(x) \geq 0`) -- 5 points.
  


**Question 2**

  We are given the following facts:
  
  1. Some theropod dinosaurs make gurgling sounds.
  2. All theropod dinosaurs are creatures. 
  3. No gurgling creatures relieve stress. 
  
  
  Mark all the statements that are necessarily true as they logically follow from the given facts.
  
  **Answer A:**
    Some theropod dinosaurs do not make gurgling sounds. 
	
  **Answer B:**
    Some gurgling creatures do not relieve stress.
	
  **Answer C:**
    Some theropod dinosaurs do not relieve stress.
	
  **Answer D:** 
    Some creatures that relieve stress are theropod dinosaurs.
	
  **Answer E:**
    Some creatures that relieve stress are not theropod dinosaurs.

  **Answer:** B, C.

  **Analysis:**
  
    * (A) does not follow from the facts --- nothing was known about non-gurgling dinosaurs.
    * (B) follows from the facts: There are some gurgling dinosaurs, they are also gurgling creatures and they do not relieve stress.
    * (C) follows from the facts: Once again, some gurgling dinosaurs must exist and they do not relieve stress.
    * (D) does not follow from the facts --- existence of non-gurgling dinosaurs was never stated (even if there were such dinosaurs, 
      they still could be unable to relieve stress for some other reason)
    * (E) does not follow from the facts --- one cannot imply that there are any stress-releaving creatures at all.

  :math:`\square`

  .. note:: 
    See exercises in `The Game of Logic <https://etc.usf.edu/lit2go/136/the-game-of-logic/2517/chapter-4/>`_ (1886) by Lewis Carroll. 
    (*Some oysters are silent; No silent creatures are amusing.* etc.)

  **Grading Criteria:**
  
    * At least one answer :math:`B,C` marked as correct, but no explanation (and some wrong answers added) -- 1 point. 
    * Some explanation, why any given statement is true or false -- 1--2 points per any single explanation. 

  **Frequent Misconceptions:**

    * The fact "Some A are B" does not imply that "Some A are not B" (For example, the fact that there are 
      some gurgling dinosaurs does not prove that there must be some non-gurgling dinosaurs as well.)
    * The fact "Gurgling creatures do not relieve stress" does not imply that "Non-gurgling creatures
      do relieve stress". Gurgling is a *sufficient condition* for a creature to be stressful, 
      but it is not a *necessary condition*. For all we know, the inability to relieve stress may be caused
      by many other reasons beside gurgling. 



**Question 3**

  In some country there are 1 million porcupines. 
  A new virus is infecting them: 
  Initially just one porcupine is infected; after one day the 
  number of infected porcupines is two. 
  In one more day the number of infected porcupines doubles again 
  and so on. 
  
  Assume that after :math:`N` days all 1 million porcupines are infected. 
  How many porcupines were infected :math:`10` days prior to that?
  You can give an estimate, if precise number is hard to compute.
  
  **Answer:** :math:`1024`
  
  **Analysis:** The number of infected porcupines grows geometrically: 
  :math:`1,2,4,8,16,32,64,128,256,512,1024,\ldots`
  
  Namely, after the first 10 days there are :math:`1024` infected porcupines. 
  The process keeps going, and after 10 more days there are already :math:`1024 \cdot 1024` 
  (slightly more than a million). Therefore :math:`N=20`; it takes twenty days to  
  infect them all. And ten days prior to that there were :math:`1024` infected.

  :math:`\square`

  .. note:: 
    An example of exponential growth (as in a pandemic, in nuclear fission reactions etc.) --- 
    after initial phase of slow growth, the process picks up and becomes very fast:
    It takes about the same time to infect the first 1000 porcupines as it takes to infect
    nearly a million after that. 

  **Grading Criteria:** 

    * Some initial members of geometric series (1,2,4,8,16) written, but no conclusions -- 1 point. 
    * Computations where 1000000 is repetitively divided by 2 (but big mistakes in the final estimate) -- 2 points.	
    * Number of days (:math:`N=20`) found, but no estimate for the number of porcupines -- 3 points.	
    * Estimates that are somewhat close to 1000 (but without explanation) -- 3 points.
    * Explained estimates that are wrong by 1-2 orders of magnitude (such as 500 or 2000) - 4 points.
    * Roughly correct estimate (near 1000) with some explanation -- 5 points. 
    * Computation "from the other end":  :math:`1000000 \rightarrow 500000 \rightarrow \ldots \rightarrow 975` -- 5 points
    * Exact formula with logarithm, e.g. :math:`2^{\log_2 1000000 - 10}` -- 5 points.
    * The precise answer :math:`1024` -- 5 points. 

.. Note - for this problem unclear, if they computed 10 days from the beginning or from the end... (Should be
..   other number of porcupines - not 1000000.




**Question 4**
  Initially Jane stands in the point :math:`O(0;0)` of a coordinate plane. 
  After that she does all stages :math:`1` through :math:`10`:
  
  **Stage 1:** 
    She walks :math:`1` meter to the north and reaches point :math:`A_1(1;0)`. 
    Then she turns :math:`90^{\circ}` to the right and walks one more meter to the east reaching point :math:`B_1(1;-1)`

  **Stage 2:**
    She turns left, walks :math:`2` meters, and reaches :math:`A_2`. Then she turns left again and walks 2 more meters
    reaching  :math:`B_2`.

  **Stage 3:**
    She turns right and walks :math:`3` meters, then turns right again and walks 3 more meters.	

  **(and so on)**
    . . .

  **Stage 10:**
    She turns left and walks 10 meters, then turns left again and walks 10 more meters. 

  At every stage she increases both distances by 1 meter; 
  on even stages she turns :math:`90^{\circ}` to the left twice; on odd 
  stages she turns :math:`90^{\circ}` to the right twice.
  
  What are the coordinates :math:`(x;y)` of the final point :math:`B_{10}` where she arrives after all ten stages?

  **Answer:** :math:`B_{10}(x;y) = (55;5)`

  
  .. image:: figs/coordinate-path.png
     :width: 300 px

  
  **Analysis:** Consider all the even stages (#2, #4, #6, #8, #10) and their 
  endpoints :math:`B_2`, :math:`B_4`, :math:`B_6`, :math:`B_8`, :math:`B_{10}`.
  Their coordinates can be computed by adding (or sometimes subtracting the 
  lengths of the steps from each other:
  
  .. math:: 
    \left\{ \begin{array}{l}
    x = (1 + 2) + (3+4)+(5 + 6) + (7+8) + (9+10) = 55,\\
    y = (-1 + 2) + (-3 + 4) + (-5 + 6) + (-7 + 8) + (-9 + 10) = 5.
    \end{array} \right.  

  :math:`\square`
  
  .. note:: 
    The multiple steps in this problem illustrate a concept of *loop* (as in computer programming) consisting of 
    same activities repeated with a loop variable that changes over time.
	
  **Grading Criteria:** 

    * Two or three stages computed correctly; after that there is no continued expression -- 1 point 
    * One coordinate found correctly, but no explanation -- 1-2 points.
    * Explanation with a wrong computation along one of the axes -- 4 points.
    * :math:`(55;-5)` or a similar "rotated" or "flipped" variant of the original response -- 5 points
      (Some confusion could reasonably happen because of the typo in this problem or the 
      direction "North" showing to the right.) 


**Question 5**

  How many among the numbers :math:`1,2,3,\ldots,30` can be expressed 
  as a sum of three different numbers taken from the set :math:`\{ 1,2,3,\ldots,10\}`. 

  **Answer:** :math:`22`
  
  **Analysis:** The smallest number we can get this way is :math:`1+2+3 = 6`, but 
  the largest one is :math:`8+9+10 = 27`. All the numbers in-between can be obtained
  by choosing three intermediate numbers to add up. (But eight numbers: 
  :math:`1,2,3,4,5,28,29,30` are impossible to obtain.)

  :math:`\square`

  .. note:: 
    Useful information can sometimes be obtained by looking at the *extremal values*
    (the largest or the smallest numbers in a set and so on). 

  **Grading Criteria:** 
  
    * A few examples, why specific values are impossible to obtain -- 1 point. 
    * Answer differs from :math:`22` by one (but no explanation -- 2 points. 
    * Answer :math:`[6;30]` (just the first values excluded, but not the last ones) -- 2 points. 
    * The computation :math:`27 - 6 = 21` used (but did not account for both included endpoints) -- 4 points. 
    * Correctly found that there are 22 integers in the interval :math:`[6;27]`. 
	
	
	

 
**Question 6**

  .. image:: figs/square-rectangles.png
     :width: 140 px

  A square was divided into four smaller squares; 
  each square is further divided into several equal rectangles
  as shown in the figure. 
  Find the smallest length of the side of the original square 
  :math:`a` such that all the rectangles in the figure
  have integer sizes in centimeters (*integer size* means 
  that the side has whole number of centimeters rather than 
  a fraction). 

  **Answer:** :math:`120` centimeters.
  
  **Analysis:** Half of the side of this square :math:`a/2` should be 
  divisible by 2, by 3, by 4 and by 5 (and every number divisible by 4 is also divisible 
  by 2). In fact, we need to insure divisibility by :math:`3`, :math:`4`, :math:`5`.
  The smallest such number is :math:`3 \cdot 4 \cdot 5 = 60`. The side of the 
  square should be two times longer, so :math:`a = 120` centimeters.

  :math:`\square`

  .. note:: 
    This problem illustrates the concept of *least common multiple*. (Similar reasoning 
    would be needed, when you add fractions. For example, in :math:`1/3 + 1/4 + 1/5`, number
    :math:`60` is the smallest common denominator.)

  **Grading Criteria:** 
  
    * One particular value of :math:`a` analyzed, but it does not cause all integers -- 1 point.
    * Division requirements listed, but no value found - 1-2 points.
    * Some answer that gives one fraction size (say, 24 is not divisible by 5) -- 3 points. 
    * A feasible (but not the minimal) answer such as :math:`240`, but no explanation -- 3 points
    * A feasible (but not the minimal) answer such as :math:`240`, but no explanation -- 3 points
    * Forgot to double the value :math:`a` (left the value :math:`60`) -- 4 points. 
    * A feasible answer such as :math:`240` with an explanation -- 4 points. 
    * Correct answer :math:`120` without explanation -- 4 points. 
    * Correct answer with an explanation -- 5 points. 


.. (Note: Should avoid numbers, where you can simply multiply 2*3*4*5 = 120.)



**Question 7**
  In a hospital there is a row of :math:`100` empty paper cups with numbers :math:`\#1,\#2,\ldots,\#100`.
  Alex passes this row one hundred times from the left to the right. 
  During the first pass he adds one pill in every cup. During 
  the 2nd pass he adds one pill in every other cup (cups with numbers :math:`\#2,\#4,\ldots`). During the 
  third pass he adds one pill in every 3rd cup, and so on. During the 100th pass he adds one pill to 
  every 100th cup (it is the cup :math:`\#100`).
  
  
  .. image:: figs/cups.png     
     :width: 300 px
	 
  How many pills were added to the cup :math:`\#60`?

  **Answer:** :math:`12` pills.
  
  **Analysis:** A new pill is added to the cup #60 every time when the step size divides the number :math:`60`. 
  (This happens on the first pass, on the second, third, fourth, fifth and sixth pass. 
  It does not happen on the seventh pass --- as :math:`60` is not divisible by :math:`7`. 
  In general, number :math:`60` has twelve divisors: 
  
  .. math::
    1,2,3,4,5,6,10,12,15,20,30,60.

  :math:`\square`
	
  .. note:: 
    To ensure that we do not forget any divisors of :math:`60`, we can arrange them in pairs so that every pair multiplies to :math:`60`:
    :math:`(1, 60),\;(2, 30),\;(3, 20),\;(4, 15),\;(5, 12),\;(6, 10)`.
	
  **Grading Criteria:** 
  
    * Exactly half of the divisors is forgotten -- 2 points. 
    * Two divisors missing, but still properly explained -- 3 points.
    * Answer with missing explanation -- 3 points. 
    * One divisor missing (but the divisors listed) -- 4 points. 

  **Frequent Misconceptions:** 
  
    * Some problems (including this) are well suited for writing short explanations. Listing
      divisors of 60 or offering some other justification shows the understanding of the underlying process.
  

  
**Question 8**

  As you may know, the number of days in a year can be divided by :math:`7` with a remainder. 
  In particular, 
  
  .. math::
  
     \left\{ \begin{array}{l}
	 365 = 52 \cdot 7 + 1,\\
	 366 = 52 \cdot 7 + 2.\\
	 \end{array} \right.
	   
  In year 2021 the date September 1 was on Wednesday. What is the nearest year in the future when 
  September 1 will also be on Wednesday?

  **Answer:** Year 2027.
  
  **Analysis:** This would happen again exactly 6 years from now. Since the remainder of dividing :math:`365` 
  by :math:`7` equals :math:`1`, the weekday for September 1 "jumps ahead" by one on regular years, 
  and it "jumps ahead" by two on leap years. We have the following days for September 1: 
  
  * September 1, 2022 is on Thursday, 
  * September 1, 2023 is on Friday, 
  * September 1, 2024 is on Sunday (because of February 29, 2024 we skipped one more day),
  * September 1, 2025 is on Monday,
  * September 1, 2026 is on Tuesday,
  * September 1, 2027 is on Wednesday. 

  :math:`\square`

  .. note::
    Days of the week follow each other in an unending cycle of seven days per week; so 
    it is often easy to compute future dates by looking at remainders by :math:`7`.

  **Grading Criteria:** 
  
    * The answer is off by 1 year, without an explanation -- 1 point.
    * The answer is fine (2027), but no good explanation -- 4 points.
    * It is mentioned that during leap years the weekdays "leap" by 2, but the year count is off by more than 1 year -- 3 points
    * It is mentioned that during leap years the weekdays "leap" by 2, but the count is off by 1 year -- 4 points.




**Question 9**

  Three vertices :math:`K,L,M` of a rhombus have the following coordinates: 
  :math:`K(1,3)`, :math:`L(4,0)` and :math:`M(5,4)`. 
  Let :math:`N` be the fourth vertex of that rhombus. 
  (A rhombus is a quadrilateral whose four sides all have the same length.)
  
  Write the coordinates :math:`(x,y)` of the vertex :math:`N`. 
  If there are multiple answers, list all the possibilities.
  
  **Answer:** :math:`N(0;-1)`
  
  .. image:: figs/rhombus.png
     :width: 180 px
  
  **Analysis:** Among the points :math:`K,L,M` there are two equal distances:
  :math:`KM = ML = \sqrt{4^2 + 1^2} = \sqrt{17}`. The distance :math:`KL = \sqrt{3^2 + 3^2} = \sqrt{18}`
  is different. So there is just one way how to add the remaining point :math:`N` to get a rhombus
  with all 4 equal sides. We have :math:`N(0;-1)`. 

  :math:`\square`
  
  .. note:: 
    This problem is about case analysis; if we relax the requirement and allow a parallelogram instead of 
    a rhombus, then there are two more possible answers (see red dots in the picture).

  **Grading Criteria:** 
  
    * Correct picture with one to three possible locations for :math:`N`, but the coordinates have mistakes - 1 point
    * The answer shows some parallelogram vertex -- 3 points
    * The answer lists all three variants (one rhombus, two parallelograms) -- 4 points. 

 
 
**Question 10**

  .. image:: figs/grid-2x5.png     
     :width: 100 px
	 
  Integer numbers from :math:`1` to :math:`10` are filled into grid as shown in the figure. 
  How many rectangles on this grid contain exactly one even number?

  **Answer:** :math:`21`
  
  **Analysis:** Every little square containing an even number ("2", "4", "6", "8", "10") is a rectangle itself. 
  Little squares "6" and "10" can also combine with any of their two neighboring (odd) squares 
  to form a rectangle. On the other hand, the little squares "2", "4", and "8" have three neighboring (odd) squares each
  (so they add three rectangles of size two; and also one rectangle of size three). 
  
  Now, let us group them by size.
  Altogether there are :math:`1+1+1+1+1 = 5` rectangles of size :math:`1 \times 1` --- all the little squares with an even number. And also 
  :math:`2 + 2 + 3 + 3 + 3 = 13` rectangles of size :math:`1 \times 2` and :math:`3` rectangles of size three. 
  Together this gives :math:`21`.

  :math:`\square`
  
  .. note:: 
    Counting the rectangles is convenient, if we combine them into categories
    (depending on which even number is used, or based on the rectangle size). 
    Grouping may help to find all possibilities and avoid counting anything twice.

  **Grading Criteria:** 
  
    * Only 13 rectangles counted (apparently, :math:`1 \times 2` or :math:`2 \times 1`), but no explanation -- 1 point
    * Squares not counted, unclear explanation (such as some unlabeled numbers added) -- 2 points
    * Rectangles :math:`1 \times 3` not counted, unclear explanation -- 2 points
    * Useful attempt to classify rectangles by size, but wrong counting -- 3 points
    * Correct answer 21, but no explanation - 4 points.


  **Frequent Misconceptions:** 
  
    * It is easy to "forget" about certain types of rectangles; in particular, :math:`1 \times 1` and :math:`1 \times 3`. 
  


**Question 11**

  How many different 3-letter "words" can be formed from the letters of a 4-letter word "FALL"?
  (By a "word" we mean any sequence of letters, it does not need to have a meaning.)

  **Answer:** :math:`12`
  
  **Analysis:** We could create a full (alphabetically sorted) list of all the possibilities:
  
  .. math::
    \mathtt{AFL}, \mathtt{ALF}, \mathtt{ALL}, \mathtt{FAL}, \mathtt{FLA}, \mathtt{FLL}, \mathtt{LAF}, \mathtt{LAL}, \mathtt{LFA}, \mathtt{LFL}, \mathtt{LLA}, \mathtt{LLF}.
  
  :math:`\square`
  
  .. note:: 
    There is one more possible interpretation of this: What if we allow to repeat other letters? (This would 
    still use the letters of "FALL" - even though it would exceed their original count.) 
	
    In this case the answer is :math:`27` --- every of the three slots in a 3-letter word can be filled in three 
    different ways, so we get :math:`3 \cdot 3 \cdot 3 = 3^3 = 27`.

  **Grading Criteria:** 
  
    * Some application of "product rule" (decision tree or some numbers multiplied), but wrong answer -- 2 or 3 points.
    * Uses answer :math:`4 \cdot 3 \cdot 2 = 24`, but two identical letters "L" not taken into account -- 3 points.
    * Exhaustive search, but misses one or two words -- 4 points.
    * Correct answer without explanation -- 4 points. 
    * Correct answer with explanation -- 5 points.


**Question 12**

  There are 6 students. In how many ways can they be assigned into 3 teams, two students per team? 
  Two assigments differ if some student is paired with somebody else (the order of students 
  in a given team or the order of the teams themselves is irrelevant). 

  **Answer:** :math:`15`
  
  **Analysis:** Denote the students by different letters :math:`A,B,C,D,E,F`. 
  Consider the student :math:`A`. S/he can be grouped any of the five remaining students (so there are
  five "large cases"). 
  
  Lets inspect one of these large cases: Assume that :math:`A` is paired with :math:`B`. The remaining four students
  can be paired in three different ways (:math:`(C,D),(E,F)`, or :math:`(C,E),(D,F)`, or :math:`(C,F),(D,E)`). 
  
  We get five "large cases" with three subcases each. So the total is :math:`5 \cdot 3 = 15`. 

  :math:`\square`
  
  .. note:: 
    Expressions that compute products like :math:`5 \cdot 3 \cdot 1` are sometimes useful, the are 
    named `Double factorials <https://en.wikipedia.org/wiki/Double_factorial>`_. (In this exercise one could 
    count variants without such theory; just by listing all the possibilities.)

  **Grading Criteria:** 

    * Answer close (such as 14), but examples not listed and unclear explanation -- 1 point. 
    * Strange answer that was a popular misconception: :math:`6 \cdot 5 + 4 \cdot 3 + 2 \cdot 1 = 44` -- 1 point.
    * Correct answer (15) without explanation -- 4 points.
    * First pair counted as :math:`6 \cdot 5` or :math:`6 \cdot 5/2`, but the reimaing four people ignored -- 2 points.


**Question 13**

  Assume that there is a :math:`12.5\%` excise tax on coffee. 
  At some point the tax rate was raised to :math:`15.0\%`. 
  At the same time the consumption of coffee decreased by :math:`10\%`. 
  What is the change in the revenue (the money collected by the government
  from this tax) after both these events? Express the change as percentage.

  **Answer:** :math:`+8\%` (revenue increases by :math:`8\%`).
  
  **Analysis:** For every unit of coffee sold the tax increases by a factor :math:`15\%/12.5\% = 1.2` (i.e. by 20 percent). 
  Since the change in tax is also accompanied by reduced demand in coffee by :math:`10\%`, we need to multiply 
  this by another factor :math:`0.9`. 
  
  We get the overall change by the factor :math:`1.2 \cdot 0.9 = 1.08` or increase by :math:`8` percents.
   
  :math:`\square`
  
  .. note:: 
    If unsure, you can always plug in some numbers. For example, assume that before the tax reform 100 EUR worth of pre-tax coffee was sold
    (generating revenue 12.50 EUR). After the tax reform only 90 EUR worth of pre-tax coffee can be sold, but the tax rate is 
    higher (revenue is 90 times 0.15 which gives 13.50 EUR). The ratio 13.5/12.5 is 27/25 = 108/100. Revenue increases by 8%.
  
    It is also good to specify, if the the revenue change by :math:`8\%` is upwards 
    or downwards (as this may not be obvious from the problem itself).


  **Grading Guidelines:** 
  
    * Percentages very large or very small, does not match common sense -- 0 points
    
.. 
.. 
.. Replace percentages with tax rate on kilograms or other physical amount.
.. 
    * Just the correct answer -- 4 points. 
    * Reasoning involving :math:`20\%-10\% = 10\%` (unjustified subtraction or percentages) -- 1   point.
    * :math:`13.5\%` is found as a ratio of new revenue against the old amount of coffee sold.
  
**Question 14**

  There are two archers :math:`A` and :math:`B`. Archer :math:`A` hits some target
  with probability :math:`p=0.9`, but another one hits that target with 
  probability :math:`p=0.5`. What is the probability that exactly one of the archers
  will hit the target?

  **Answer:** :math:`0.5`
  
  **Analysis:** There are two subcases: 
  
    1. The archer :math:`A` hits the target (probability 0.9), but the archer :math:`B` misses the target (probability 0.5). 
    2. The archer :math:`A` misses the target (probability 0.1), but the archer :math:`B` hits the target (probability 0.5). 
	
  In the first subcase the probabilities multiply to :math:`0.9 \cdot 0.5 = 0.45`, in the second subcase they are :math:`0.1 \cdot 0.5 = 0.05`.
  (We need to assume that both events were *independent* to multiply --- namely, the success or failure of one archer did not 
  affect the other archer's success probability.)   
  Both subcases can never happen at the same time, so we add their probabilities: :math:`0.45 + 0.05 = 0.5`. 

  :math:`\square`

  .. note:: 
    Situations, when exactly one archer hits the target (but not both!) can be described
    as *exclusive or* between the two events (as in English expression "either"-"or"). 
    But one can easily avoid concepts like this --- just analyze and add both subcases.


  **Grading Criteria:**
  
    * Wrong answers without a valid explanation (including invalid probability values like :math:`p=1.4>1`) -- 0 points
    * Answer 0.7 as arithmetic mean -- 1 points. 
    * Answer 0.95 with explanation (in fact, solving a different problem - at least one archer hits the target) -- 1 point. 
    * Answer 0.45 or other evidence that probablities of independent events where multiplied -- 2 points
    * Answer 0.45 with an explanation how it was obtained (ignoring the case when A misses, but B hits) -- 3 points. 
    * Just the correct answer p=0.5 without an explanation -- 3 points

  **Frequent Misconceptions:** 
  
    * Using a formula :math:`(0.9 + 0.5)/2 = 0.7` was often used. This does not answer the original question 
      (where **both** archers shoot and exactly one of them hits the target); 
      it solves a different problem -- select a random archer and see, if s/he hits the target.
    * Using another formula :math:`(0.9 + 0.5) - 0.9 \cdot 0.5 = 0.95`:
      first add both probabilities, and then subtract the probability of the event where
      they overlap where both archers hit the target. In fact, you would need to subtract :math:`0.9 \cdot 0.5`
      the second time.


**Question 15**

  .. image:: figs/histogram-for-age.png
     :width: 200 px
	 

  The histogram shows the distribution of people in some company by age groups.
  Each age group is a half-open interval :math:`[20;30)`, :math:`[30;40)`, and so on.
  Specifically, the leftmost bar in the histogram means that there are exactly two people of ages 
  from the interval :math:`[20;30)`. 
  
  Some employee Joe is such that 70% of the employees have ages not exceeding Joe's age.
  
  What is the smallest possible age of Joe?
  
  **Answer:** :math:`50` years
  
  **Analysis:** From the histogram we see that there are altogether :math:`2+4+4 + 5 + 3 + 1 + 1 = 20` people 
  in the company. 70% equals 14 employees (younger than Joe or the same age including Joe itself). 
  The age of Joe should be in the bucket :math:`[50;60)`. 
  
  Indeed, if he is younger than :math:`50`, there are at most :math:`2+4+4 = 10`
  people not exceeding his age. If he is at least :math:`60` years old, there are :math:`2+4+4+5 = 15`
  such people. 
  
  The youngest age for Joe is exactly :math:`50` years (in this case we would need three more people who are exactly 
  :math:`50` years old). 

  :math:`\square`
  
  .. note:: 
    Reading data from histograms is not always intuitive, but data points are often grouped into 
    some "buckets" (age intervals in demography, income brackets and many more). 

  **Grading Criteria:**

    * Total of all people (20) counted correctly  -- 1 point; 70% of them (14) counted correctly -- 1 more point. 
    * Value 51, 52, 59 (not equal to 50) -- 3 points
    * The whole bucket [50;60) specified -- 4 points

.. So few buckets that [50;60) could be simply guessed....


**Question 16**

  There were six people in some room.
  The following numbers denote their annual income in USD:
  
  .. math::
  
    40000, 50000, 60000, 70000, 80000, 3000000.
  
  The person with annual income of 3 million USD walked away leaving just five people in the room.
  
  1. By how much did the average income in this room decrease? (*Average* is the arithmetic mean.)
  2. By how much did the median income in this room decrease?
  
  
  **Answer:** The *average income* decreases by :math:`490000` USD (nearly half a million); 
  the *median income* decreases by :math:`5000` USD. 
  
  **Analysis:** The arithmetic mean for all six people: 
  
  .. math::
    (40000 + 50000 + 60000 + 70000 + 80000 + 3000000)/6 = 3300000/6 = 550000.
	
  Subtracting from this the average of the bottom five people (:math:`60000`), we get :math:`490000`.
  
  On the other hand, the median initially was between the values :math:`60000` and :math:`70000`
  (it equals :math:`65000`). After one person left, we got one middle value :math:`60000`. The difference
  is :math:`5000`. 

  :math:`\square`

  .. note:: 
    Income distribution often has outliers (unusual data points). So arithmetic mean is less stable
    than median, even though arithmetic mean is easier to operate with. 
    Still, in practice nearly every macroeconomical report speaks of
    *median income* rather than *average income*, since the average income is prone to sudden jumps as 
    shown by this question.


  **Grading Criteria:** 

    * Some discussions unrelated to the questions asked -- 0 points
    * Median or average computations containing mistakes (division by 2, not by 5 or 6, and so on) -- 1 or 2 points.
    * Median computed, but average not complete -- 3 points.  


  



  
  


  
