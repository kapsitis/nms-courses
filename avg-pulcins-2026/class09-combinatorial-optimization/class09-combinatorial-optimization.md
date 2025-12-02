---
title: "AMO olimpiāde (2025-11-08)"
numbersections: true
mainfont: "TeX Gyre Pagella"
fontsize: 11pt
geometry: "margin=1in"
header-left: "AMO olimpiāde (2025-11-08)"
header-includes:
  - |
    \makeatletter
    \RedeclareSectionCommand[
      beforeskip=1.2ex plus 0.4ex minus 0.2ex,
      afterskip=0.4ex plus 0.2ex minus 0.2ex
    ]{subsection}
    \makeatother
  - \setcounter{section}{7}
  - |
    \usepackage{etoolbox}
    \AtBeginEnvironment{footnotesize}{\footnotesize}
---
# Kombinatoriskā optimizācija (2025-11-08)

## 1.uzdevums {-} 

<!--
98299

а) К любому ли шестизначному числу, начинающемуся с цифры 5, можно приписать еще 6 цифр так, чтобы полученное 12-значное число было полным квадратом?
б) Тот же вопрос про число, начинающееся с 1.
в) Найдите для каждого n такое наименьшее  k = k(n),  что к каждому n-значному числу можно приписать еще k цифр так, чтобы полученное (n+k)-значное число было полным квадратом.
-->

**(A)** Vai jebkuram sešciparu skaitlim, kas sākas ar ciparu $5$, 
var pievienot vēl 6 ciparus tā, lai iegūtais 12-ciparu skaitlis 
būtu pilns kvadrāts?  
**(B)** Tas pats jautājums par skaitli, kas sākas ar $1$.  
**(C)** Atrodiet katram $n$ tādu mazāko $k = k(n)$, ka jebkuram $n$-ciparu skaitlim var pievienot vēl $k$ ciparus tā, lai iegūtais 
$(n+k)$-ciparu skaitlis būtu pilns kvadrāts.  
*Piezīme:* Pieraksts $k=k(n)$ uzsver, ka $k$ ir 
*funkcija* no $n$ (skaitlis $k$ ir atkarīgs no $n$ un 
to var izrēķināt katram dotajam naturālam skaitlim $n$).


## 2.uzdevums {-} 

<!--
66545	

На витрине ювелирного магазина лежат 15 бриллиантов. Рядом с ними стоят таблички с указанием масс, на которых написано 1, 2, ..., 15 карат. У продавца есть чашечные весы и четыре гирьки массами 1, 2, 4 и 8 карат. Покупателю разрешается только один тип взвешиваний: положить один из бриллиантов на одну чашу весов, а гирьки — на другую и убедиться, что масса на соответствующей табличке указана верно. Однако за каждую взятую гирьку нужно заплатить продавцу 100 монет. Если гирька снимается с весов и в следующем взвешивании не участвует, продавец забирает её. Какую наименьшую сумму придётся заплатить, чтобы проверить массы всех бриллиантов?
-->

Rotaslietu veikala vitrīnā novietoti $15$ dimanti. 
Blakus katram no tiem atrodas plāksnītes ar norādītām masām, 
uz kurām rakstīts $1$, $2$, $\ldots$, $15$ karāti. 
Pārdevējam ir svari ar diviem svaru kausiem un četri atsvari ar 
masām $1$, $2$, $4$ un $8$ karāti. Pircējam atļauts uz viena 
kausa uzlikt kādu no dimantiem, un uz otra kausa - atsvarus, lai 
pārliecinātos, ka uz plāksnītes norādītā masa ir pareiza. 

Par katru paņemto atsvaru ir jāsamaksā pārdevējam 1 EUR. 
Ja atsvaru noņem no svariem un nākamajā svēršanā vairs neizmanto, tas 
atgriežas pie pārdevēja (un par tā atkārtotu paņemšanu jāmaksā vēlreiz 
1 EUR). Kāda ir minimālā summa, kas pircējam jāsamaksā, lai pārbaudītu visu dimantu masas?



## 3.uzdevums {-} 

<!--
67315

У математика есть 19 различных гирь, массы которых в килограммах равны ln2, ln3, ln4,…,ln20, и абсолютно точные двухчашечные весы. Он положил несколько гирь на весы так, что установилось равновесие. Какое наибольшее число гирь могло оказаться на весах?
-->

No $19$ skaitļiem $2,3,\ldots,20$ izvēlējās $k$ skaitļus, 
ko sadalīja divās grupās tā, ka skaitļu reizinājumi 
abās grupās ir vienādi. 
Kādam lielākajam $k$ to var izdarīt?





## 4.uzdevums {-} 

<!--
110032

Среди пяти внешне одинаковых монет 3 настоящие и две фальшивые, одинаковые по весу, но неизвестно, тяжелее или легче настоящих. Как за наименьшее число взвешиваний найти хотя бы одну настоящую монету?
-->

Starp piecām ārēji vienādām monētām ir 3 īstas un 2 viltotas. 
Viltotās ir savstarpēji vienādas pēc svara, bet nav zināms, vai
viltotas monētas masa ir lielāka vai mazāka par īstas 
monētas masu. Kā ar vismazāko svēršanu skaitu var atrast 
vismaz vienu īstu monētu?  
(Svēršanā atļauts uz diviem svaru kausiem uzlikt jebkādu 
skaitu monētu un noskaidrot, vai pirmais kauss ir mazāks, vienāds 
vai lielāks par otro.)


## 5.uzdevums {-} 


<!--
64508

В сумме  + 1 + 3 + 9 + 27 + 81 + 243 + 729  можно вычеркивать любые слагаемые и изменять некоторые знаки перед оставшимися числами с "+" на "–". Маша хочет таким способом сначала получить выражение, значение которого равно 1, затем, начав сначала, получить выражение, значение которого равно 2, затем (снова начав сначала) получить 3, и так далее. До какого наибольшего целого числа ей удастся это сделать без пропусков?
-->

Summā $+ 1 + 3 + 9 + 27 + 81 + 243 + 729$ var izsvītrot jebkurus saskaitāmos un mainīt pirms atlikušajiem saskaitāmajiem 
darbību zīmes no "$+$" uz "$-$". Marija vēlas šādā veidā iegūt 
dažādas izteiksmes ar vērtībām $1$, $2$, $3$ utt., ikreiz sākot 
izsvītrošanu un zīmju maiņu no sākuma.
Kuram vislielākajam $n$ var šādi izteikt visus skaitļus no $1$ 
līdz $n$, nevienu neizlaižot?


## 6.uzdevums {-} 

<!--
64608


По кругу стоят 99 детей, изначально у каждого есть мячик. Ежеминутно каждый ребёнок с мячиком кидает свой мячик одному из двух соседей; при этом, если два мячика попадают к одному ребёнку, то один из этих мячиков теряется безвозвратно. Через какое наименьшее время у детей может остаться только один мячик?
-->

Aplī stāv $99$ bērni, katram sākumā ir balons. Katru minūti katrs bērns, kuram ir balons, met to kādam no diviem saviem 
kaimiņiem. Ja pie viena bērna vienlaikus nonāk divi baloni, 
tad viens no tiem neatgriezeniski pazūd. Kāds ir 
mazākais minūšu skaits, pēc kura bērniem var palikt 
tikai viens balons?


## 7.uzdevums {-} 

<!--
66904


В отель ночью приехали 100 туристов. Они знают, что в отеле есть одноместные номера 1, 2,…,n, из которых k на ремонте (но неизвестно какие), а остальные свободны. Туристы могут заранее договориться о своих действиях, после чего по очереди уходят заселяться: каждый проверяет номера в любом порядке, находит первый свободный номер не на ремонте и остаётся там ночевать. Но туристы не хотят беспокоить друг друга: нельзя проверять номер, куда уже кто-то заселился. Для каждого k укажите наименьшее n, при котором туристы гарантированно смогут заселиться, не потревожив друг друга.
-->


Viesnīcā naktī ieradās $100$ tūristi. Viņi zina, ka viesnīcā ir vienvietīgi numuri ar numuriem $1, 2, \ldots, n$, no 
kuriem $k$ ir remontā (bet nav zināms, kuri); pārējie 
numuri ir pieejami. Tūristi var iepriekš vienoties par savām darbībām,
pēc tam viņi pa vienam dodas apmesties: katrs pārbauda numurus jebkādā
secībā, atrod pirmo brīvo numuru, kas nav remontā, un paliek 
tur pa nakti. Tūristiem nav atļauts traucēt citam citu: nav atļauts
pārbaudīt numuru, kurā jau kāds apmeties. Katram $k$ norādiet mazāko
$n$, pie kura tūristi garantēti varēs apmesties, netraucējot viens otru.



## 8.uzdevums {-} 

<!--
66710

Король решил поощрить группу из n мудрецов. Их поставят в ряд друг за другом (чтобы все смотрели в одном направлении), на каждого наденут чёрную или белую шляпу. Каждый будет видеть шляпы всех впереди стоящих. Мудрецы по очереди (от последнего к первому) назовут цвет (белый или чёрный) и натуральное число по своему выбору. В конце подсчитывается число мудрецов, которые назвали цвет, совпадающий с цветом своей шляпы: ровно столько дней всей группе будут платить надбавку к жалованью. Мудрецам разрешили договориться заранее, как отвечать. При этом мудрецы знают, что ровно k из них безумны (кто именно – им неизвестно). Безумный мудрец называет белый или чёрный цвет и число вне зависимости от договорённостей. Какое максимальное число дней с надбавкой к жалованью могут гарантировать группе мудрецы, независимо от местонахождения безумных в очереди?
-->

Karalis nolēma apbalvot grupu ar $n$ padomniekiem. Viņus nostādīs 
rindā vienu aiz otra, lai visi skatās vienā virzienā. Katram uzvilks
melnu vai baltu cepuri. Katrs redzēs visu priekšā stāvošo cepures
(bet ne savējo vai cepures sev aiz muguras).
Padomnieki pēc kārtas (no pēdējā līdz pirmajam) nosauc krāsu 
(balta vai melna) un jebkuru pašu izvēlētu naturālu skaitli. 
Beigās saskaita, cik padomnieku ir nosaukuši krāsu, kas sakrīt ar viņu cepures krāsu: tieši tik daudz eiro katram no viņiem izmaksās 
kā prēmiju. Padomnieki var iepriekš vienoties, kā atbildēt. Turklāt viņi zina, ka tieši $k$ no padomniekiem ir provokatori (kuri tieši – viņi nezina). Provokators var nosaukt balto vai melno krāsu un skaitli neatkarīgi no vienošanās. Kādu maksimālo 
prēmijas apjomu var garantēt neatkarīgi no provokatoru atrašanās rindā?








<!--
## 9.uzdevums {-} 

32896

Сто мудрецов хотят проехать на электричке из 12 вагонов от первой до 76-й станции. Они знают, что на первой станции в два вагона электрички сядут два контролёра. После четвёртой станции на каждом перегоне один из контролёров будет переходить в соседний вагон, причём они "ходят" по очереди. Мудрец видит контролёра, только если он в соседнем вагоне или через вагон. На каждой станции каждый мудрец может перебежать по платформе не далее чем на три вагона (например, из 7-го вагона мудрец может добежать до любого вагона с номером от 4 до 10 и сесть в него). Какое максимальное число мудрецов сможет ни разу не оказаться в одном вагоне с контролёром, как бы контролёры ни перемещались? (Никакой информации о контролёрах, кроме указанной в задаче, мудрец не получает. Мудрецы договариваются о стратегии заранее.)


Simts gudrie vēlas braukt ar vilcienu, kurā ir 12 vagoni, no pirmās līdz 76. stacijai. Viņi zina, ka pirmajā stacijā divos vagonos iekāps divi kontrolieri. Pēc ceturtās stacijas katrā posmā viens no kontrolieriem pāries uz blakus vagonu, turklāt viņi "staigā" pārmaiņus. Gudrais redz kontrolieri tikai tad, ja tas ir blakus vagonā vai vēl vienu vagonu tālāk. Katrā stacijā katrs gudrais var pārrāpot pa peronu ne tālāk kā uz trim vagoniem (piemēram, no 7. vagona gudrais var aizskriet uz jebkuru vagonu ar numuru no 4 līdz 10 un iesēsties tajā). Kāds ir maksimālais gudro skaits, kas ne reizi neatradīsies vienā vagonā ar kontrolieri, lai arī kā kontrolieri pārvietotos? (Citas informācijas par kontrolieriem, izņemot uzdevumā doto, gudrajiem nav. Gudrie par stratēģiju vienojas iepriekš.)

-->



## 9.uzdevums {-} 

<!--
111837

Фокусник с помощником собираются показать такой фокус. Зритель пишет на доске последовательность из N цифр. Помощник фокусника закрывает две соседних цифры чёрным кружком. Затем входит фокусник. Его задача – отгадать обе закрытые цифры (и порядок, в котором они расположены). При каком наименьшем N фокусник может договориться с помощником так, чтобы фокус гарантированно удался?
-->

Burvju mākslinieks ar palīgu gatavojas demonstrēt šādu triku. Skatītājs uz tāfeles uzraksta virkni no $N$ cipariem. Burvju mākslinieka palīgs aizklāj divus blakus esošus ciparus ar melnu apli. Tad ienāk burvju mākslinieks. Viņa uzdevums – uzminēt abus aizklātos ciparus (un to secību). Pie kāda mazākā $N$ burvju mākslinieks var ar palīgu vienoties tā, ka triks noteikti izdosies?


## 10.uzdevums {-} 

<!--
64362

На каждой из 2013 карточек написано по числу, все эти 2013 чисел различны. Карточки перевёрнуты числами вниз. За один ход разрешается указать на десять карточек, и в ответ сообщат одно из чисел, написанных на них (неизвестно, какое).
Для какого наибольшего t гарантированно удастся найти t карточек, про которые известно, какое число написано на каждой из них?
-->

Uz katras no $2013$ kartītēm ir uzrakstīts skaitlis, visi šie $2013$ skaitļi ir dažādi. Kartītes ir apgrieztas ar skaitli uz leju. Vienā gājienā drīkst norādīt uz desmit kartītēm, un kā atbildi paziņo vienu no tām uzrakstīto skaitli (nav zināms, kuru tieši). Kādam lielākajam $t$ noteikti varēs atrast $t$ kartītes, par kurām būs zināms, kāds skaitlis uz katras no tām ir uzrakstīts?