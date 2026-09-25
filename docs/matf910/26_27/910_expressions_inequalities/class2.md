---
layout: default
title: "9.2.B. Izteiksmes un nevienādības: Daļas un saknes"
permalink: /matf910/26_27/910_expressions_inequalities/class2/

docx_header: "9.2.B. Izteiksmes un nevienādības: Daļas un saknes"
docx_footer: "ĀVĢ 9.-10.klašu matemātikas fakultatīvs"
docx_font: "Calibri"
docx_fontsize: 10
docx_heading_font: "Calibri Light"
docx_heading_color: "2F5496"
docx_heading1_size: 14
geometry: "a4paper, top=2.54cm, bottom=2.54cm, left=2.54cm, right=2.54cm"
---

# 9.2.B. Izteiksmes un nevienādības: Daļas un saknes

Reizināt ar saucēju drīkst tikai tad, kad zināma tā zīme. Galvenā nevienādība: ja $a > 0$, tad
$$a+\frac{1}{a} \geq 2, \qquad \text{un arī} \qquad \frac{a}{b}+\frac{b}{a} \geq 2 \quad (a,b>0).$$
To var **pierādīt**: reizina ar $a>0$ un iegūst $a^2-2a+1 = (a-1)^2 \geq 0$.
Vienādība iestājas tikai tad, ja $a=1$ (attiecīgi $a=b$).
Tas ir tas pats $t^2 \geq 0$ no iepriekšējās nodarbības.

Darbā ar daļām un saknēm:

* Vispirms pieraksta, kādas vērtības mainīgie drīkst pieņemt (saucējs $\neq 0$, zem kvadrātsaknes $\geq 0$).
* Reizinot nevienādību ar pozitīvu skaitli, zīme nemainās; ar negatīvu - mainās. Ja saucēja
  zīme nav zināma, **nereizina**, bet veido zīmju tabulu.
* $\sqrt{A^2} = \lvert A \rvert$, nevis $A$. Divkāršu sakni $\sqrt{p \pm q\sqrt{r}}$ mēģina
  uzrakstīt kā $\sqrt{(u \pm v)^2}$.

**1.piemērs (LV.AMO.2025.10.1):** Doti divi dažādi naturāli skaitļi $a$ un $b$. Pierādīt, ka
$\frac{a}{b}+\frac{b}{a} \geq 2+\frac{1}{ab}$.

* *Pārformulēšana:* Kāda ir $ab$ zīme? Reizini ar $ab$ un pārnes visu uz vienu pusi.
* *Atskats:* Iegūsi $(a-b)^2 \geq 1$. Kur izmantots, ka skaitļi ir **dažādi** un **veseli**?
  Pārbaudi $a=b=1$.

**2.piemērs (LV.AMO.2017.10.2):** Pierādīt, ka visiem pozitīviem skaitļiem $a$ un $b$ izpildās
$\left(\frac{3a}{b}+1\right)\left(\frac{3b}{a}+1\right) \geq 16$.

* *Izpēte:* Atver iekavas. Kas notiek ar $\frac{3a}{b} \cdot \frac{3b}{a}$? Kur parādās
  $\frac{a}{b}+\frac{b}{a}$?

**3.piemērs (LV.NOL.2024.11.2):** Reāliem skaitļiem $x$ un $y$ ir spēkā vienādība
$\frac{x+y}{x-y}+\frac{x-y}{x+y}=5$. Pierādīt, ka
$\frac{x^{2}+y^{2}}{x^{2}-y^{2}}+\frac{x^{2}-y^{2}}{x^{2}+y^{2}}<3$.

* *Pārformulēšana:* Abas izteiksmes ir formā $u+\frac{1}{u}$. Apzīmē $t=\frac{x+y}{x-y}$ un
  saskaiti $t+\frac{1}{t}$ kā vienu daļu. Kur tajā parādās $x^2+y^2$ un $x^2-y^2$?

---

## 1.uzdevums

> **LV.NOL.2016.8.1:**
> Aprēķini izteiksmes $\sqrt{a-b}+\sqrt{b-c}+\sqrt{c-d}+\sqrt{d-a}$ vērtību!

## 2.uzdevums

> **LV.NOL.2010.9.1:**
> Atrodiet kaut vienu kvadrātvienādojumu ar veseliem koeficientiem, kam viena no saknēm ir
> **(A)** $\sqrt{2}+1$,
> **(B)** $\sqrt{7+4 \sqrt{3}}$.
>
> **Piezīme.** Katrā uzdevuma daļā runā par **citu** kvadrātvienādojumu.

## 3.uzdevums

> **LV.AMO.2017.9.2:**
> Pierādīt, ka $x^{6}+y^{6}+\frac{2}{x^{3}y^{3}}-4 \geq 0$, ja $x>0$, $y>0$.
