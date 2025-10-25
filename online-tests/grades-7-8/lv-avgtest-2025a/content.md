# <lo-sample/> LV.AVGTEST.2025A.7_8.1

(Attēlā **GND** un **V5** pieslēgti pie tās pašas līnijas - ar īssavienojumu. 
Starp abiem kontaktiem ir arī rezistors un LED diode - bet tie nesaņem 
strāvu.)

Elektriskās ierīces saslēgtas kā parādīts zīmējumā. 
Kas notiek tad, kad ieslēdz strāvas avotu?

A. Nekas nenotiek, jo elektriskā ķēde nav noslēgta. 
B. Strāvas avotam (piemēram Arduino) ir īssavienojums. 
C. Uz LED diodes ir pareizs spriegums, bet tā nevar degt, jo 
   ir iesprausta otrādi. 
D. Uz LED diodes ir pareizs spriegums un tā iedegas. 
E. LED diode ir pārslogota, strāvas stiprums pārsniedz 
   pieļaujamo vērtību -- $20$ miliampērus.


<small>

* Answer:`D`

</small>

## Atrisinājums

TBD


# <lo-sample/> LV.AVGTEST.2025A.7_8.2

Strāvas avota spriegums ir 3.5 volti. 
Atrast pretestību shēmā ieslēgtajam rezistoram, lai 
strāvas stiprums LED diodē būtu 20 miliampēri. 
Varat pieņemt, ka sprieguma kritums LED diodē
vienmēr ir 2 volti. 


# <lo-sample/> LV.AVGTEST.2025A.7_8.3

Strāvas avota spriegums ir 5 volti. 
Tam virknē pieslēgtas 2 diodes kā parādīts zīmējumā. 
Atrast pretestību shēmā ieslēgtajam rezistoram, 
lai strāvas stiprums LED diodē būtu 20 miliampēri.
Varat pieņemt, ka sprieguma kritums LED diodē
vienmēr ir 2 volti. 

(Ja divas diodes saslēdz virknē, tad spriegumu atšķirība visā virknē 
būs abu sprieguma kritumu summa.)





# <lo-sample/> LV.AVGTEST.2025A.7_8.4

LED displeja cipars ir pieslēgts maketēšanas platei kā attēlots 
zīmējumā (katrs no kontaktiem displeja augšpusē ir saslēgts kopā ar 
līdzīgu kontaktu displeja apakšpusē). 
Kāds būs rezultāts, ja šādi saslēgtas ierīces pieslēdz strāvai? 

A. Īssavienojums strāvas avotā. 
B. LED displejs paliek tumšs, jo tam pareizajā virzienā nepieplūst strāva.
C. Pārslogotas LED displeja diodes, strāvas stiprums pārsniedz 20 
   miliampērus.
D. LED displejs darbojas kā parasti, bet dažus displeja posmus nevar 
   atsevišķi kontrolēt; tie vienmēr ieslēdzas kopā. 




# <lo-sample/> LV.AVGTEST.2025A.7_8.5

Starp potenciometra **GND** un **OTA** 
kontaktiem spriegums var mainīties intervālā $[0V, 5V]$ 
(no nulles līdz pieciem voltiem). 
Starp šiem kontaktiem pieslēgts $220~\Omega$ ($220$ omu) 
rezistors un dažādu krāsu diodes paralēli. 

Potenciometra spriegumu pakāpeniski palielina. 
Kura diode iedegsies pirmā? 

A. Sarkanā
B. Dzeltenā
C. Zaļā
D. Zilā


# <lo-sample/> LV.AVGTEST.2025A.7_8.6

Pie Arduino pieslēgti divi LED displeji 
multipleksēšanas režīmā (kamēr uz viena zīmē cipariņu, 
otrs ir izslēgts un otrādi). 
Šiem displejiem visi astoņi 
posmi ir pieslēgti pie Arduino kontaktiem no 2.kontakta līdz 
9.kontaktam. 

Kas jāizdara, lai izslēgtu cipariņu pa labi, 
bet turpinātu zīmēt cipariņu pa kreisi?

A. Visi kontakti no 2. līdz 9.kontaktam jānoliek uz LOW. 
B. Visi kontakti no 2. līdz 9.kontaktam jānoliek uz HIGH. 
C. 11.kontakts (kas pieslēgts labā cipariņa katodam) jānoliek uz LOW. 
D. 11.kontakts (kas pieslēgts labā cipariņa katodam) jānoliek uz HIGH. 





# <lo-sample/> LV.AVGTEST.2025A.7_8.7

LED displeja cipars ir pieslēgts maketēšanas platei "guļus"
(sk. zīmējumu). 
Kāds būs rezultāts, ja šādi saslēgtas ierīces pieslēdz strāvai? 

A. Īssavienojums strāvas avotā. 
B. LED displejs paliek tumšs, jo tam pareizajā virzienā nepieplūst strāva.
C. Pārslogotas LED displeja diodes, strāvas stiprums pārsniedz 20 
   miliampērus.
D. LED displejs darbojas kā parasti, bet dažus displeja posmus nevar 
   atsevišķi kontrolēt; tie vienmēr ieslēdzas kopā. 




# <lo-sample/> LV.AVGTEST.2025A.7_8.8

Elektriskajā ķēdē ar 5 voltu sprieguma avotu 
saslēgti divi $220~\Omega$ rezistori paralēli un aiz tiem 
virknē divas LED diodes. 
Pieņemot, ka uz LED diodes sprieguma kritums ir 2 volti, 
cik liela strāva ies cauri LED diodēm (un vai tā nepārsniegs 
diodes specifikācijā atļautos 20 miliampērus)?  

(*Piezīme:* Ja divus rezistorus saslēdz paralēli, tad 
to kopīgā pretestība ir divreiz *mazāka* nekā būtu vienam rezistoram.)


# <lo-sample/> LV.AVGTEST.2025A.7_8.9

Attēlā redzamā elektriskā ķēde var ieslēgt  
sarkano vai zaļo LED diodi ar šādām komandām: 

```
writeDigital(10, HIGH); // ieslēdz sarkano
writeDigital(11, LOW); // izslēdz zaļo
```

vai 

```
writeDigital(10, LOW); // izslēdz sarkano
writeDigital(11, HIGH); // ieslēdz zaļo
```

Mēs gribam saglabāt šo uzvedību, bet izmantot tikai vienu rezistoru 
nevis divus. Kura no ķēdēm uzvedīsies tāpat kā sākotnējā (un ļaus 
atsevišķi ieslēgt sarkano vai zaļo LED diodi). 



# <lo-sample/> LV.AVGTEST.2025A.7_8.10

Mūsu mērķis ir regulēt LED diodes gaišumu ar potenciometru. 
Šai  nolūkā ir saslēgta elektriska ķēde ar rezistoru un 
LED diodi, uz kuras ar potenciometru (starp kontaktiem **GND** un **OTA**)
var padot jebkuru strāvu no 0 līdz 5 voltiem. 



# <lo-sample/> LV.AVGTEST.2025A.7_8.10

Filmas specefektu operators vēlas viļņveidīgi mainīt 
LED gaismiņas spožumu ar potenciometru, 
kura regulatoru viņš vienmērīgi bīda starp abiem galējiem 
stāvokļiem tā, ka spriegums starp kontaktiem **GND** un **OTA**
mainās robežās no 0 līdz 5 voltiem. Ķēde ar potenciometru 
ir attēlota zīmējumā (ieslēgta viena LED diode). 
Atzīmēt, kurš apgalvojums ir patiess: 

A. LED diodes spožums tiešām mainās viļņveidīgi 
   visā potenciometra kustības intervālā no 
   pavisam nodzisušas līdz spoži iedegtai un atpakaļ. 
B. LED diode aptuveni ceturtdaļu laika 
   (no 0 voltiem līdz 1.25 voltiem) nedarbojas vispār, pēc 
   tam tā ātri sasniedz maksimālo spožumu. 
C. Šādi regulēt spriegumu uz LED diodes nevar, jo kaut kādā 
   brīdī tiks pārsniegts atļautais strāvas stiprums (20 miliampēri). 
D. LED diode neieslēgsies vispār, jo ķēdē ir ievietota nepareizā virzienā. 


(Arī citi šī uzdevuma varianti - starp GND un VCC, starp 
GND un OTA, diode pretējā 
secībā; diode ar vai bez rezistora.)




# <lo-sample/> LV.AVGTEST.2025A.7_8.11

Filmas specefektu operators vēlas viļņveidīgi mainīt 
LED gaismiņas spožumu ar programmu, kura ciklā maina 
skaitli no 0 līdz 255 un izvada 
ar PWM (pulsa platuma modulāciju) uz 9.kontakta.
Ķēde ar potenciometru 
ir attēlota zīmējumā (virknē ieslēgts rezistors un LED diode). 

Atzīmēt, kurš apgalvojums ir patiess:

A. LED gaismiņas intensitāte mainīsies pakāpeniski 
   no pilnīgi izslēgtas līdz spoži degošai. 
B. LED diode aptuveni ceturtdaļu laika 
   nedarbojas vispār (ar pulsa platuma modulāciju nepietiek, 
   lai to iedegtu). Pēc 
   tam tā ātri sasniedz maksimālo spožumu. 
C. Šādi regulēt spriegumu uz LED diodes nevar, jo kaut kādā 
   brīdī tiks pārsniegts atļautais strāvas stiprums (20 miliampēri). 
D. LED diode neieslēgsies vispār, jo ķēdē ir ievietota nepareizā virzienā. 



# <lo-sample/> LV.AVGTEST.2025A.7_8.12

(Elektriskā ķēde nav noslēgta, jo zemes vadu pārrauj 
maketēšanas plates līniju atdalītājs.)

Pie maketēšanas plates pieslēgts Arduino kontrolieris, 
rezistors un LED gaismiņa. 
Kas notiek, kad Arduino kontrolieri pieslēdz strāvai? 

A. Nekas nenotiek, jo elektriskā ķēde nav noslēgta. 
B. Strāvas avotam rodas īssavienojums. 
C. Uz LED diodes ir pareizs spriegums, bet tā nevar degt, jo 
   ir iesprausta otrādi. 
D. Uz LED diodes ir pareizs spriegums un tā iedegas. 
E. LED diode ir pārslogota, strāvas stiprums pārsniedz 
   pieļaujamo vērtību ($20$ miliampērus). 




# <lo-sample/> LV.AVGTEST.2025A.7_8.13

Rezistors iesprausts vertikāli (LED pārslogots)



# <lo-sample/> LV.AVGTEST.2025A.7_8.14

LED iesprausta vertikāli (nesaņem nekādu strāvu)




# <lo-sample/> LV.AVGTEST.2025A.7_8.15


Kuri kontakti uz Arduino ir jāieslēdz, lai uz LED 
displeja parādītos cipars "2"?

A. Uz LOW, .... uz HIGH. 


# <lo-sample/> LV.AVGTEST.2025A.7_8.15






