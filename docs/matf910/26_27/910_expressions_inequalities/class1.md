---
layout: default
title: "9.2.A. Izteiksmes un nevienādības: Identitātes un pilnais kvadrāts"
permalink: /matf910/26_27/910_expressions_inequalities/class1/

docx_header: "9.2.A. Izteiksmes un nevienādības: Identitātes un pilnais kvadrāts"
docx_footer: "ĀVĢ 9.-10.klašu matemātikas fakultatīvs"
docx_font: "Calibri"
docx_fontsize: 10
docx_heading_font: "Calibri Light"
docx_heading_color: "2F5496"
docx_heading1_size: 14
geometry: "a4paper, top=2.54cm, bottom=2.54cm, left=2.54cm, right=2.54cm"
---

# 9.2.A. Izteiksmes un nevienādības: Identitātes un pilnais kvadrāts

Izteiksmes pārveido, lai *vienkāršotu* vai *pierādītu* nevis gari rakstītu. Formulas (lieto abos virzienos):

* $(a \pm b)^2 = a^2 \pm 2ab + b^2$, $\quad a^2-b^2 = (a-b)(a+b)$,
* $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$,
* $(a+b+c)^2 = a^2+b^2+c^2+2(ab+bc+ca)$.

Ja izteiksmē atkārtojas kāds fragments (liels skaitlis, $x^3$ u.c.), ievieš jaunu mainīgo.
Vienīgā nevienādība, kas šajā nodarbībā vajadzīga, ir $t^2 \geq 0$. Taktikas:

1. Visu pārnes uz vienu pusi: jāpierāda "izteiksme $\geq 0$" (vai $> 0$).
2. Atdala pilnos kvadrātus - izteiksmi uzraksta kā kvadrātu (un skaitļu) summu.
3. Pamana, **kad iestājas vienādība** ar $0$ (visi kvadrāti kļūst $0$).

**1.piemērs (LV.NOL.2025.9.1):** Aprēķināt izteiksmes
$\frac{20252024^{2}}{20252023^{2}+20252025^{2}-2}$ vērtību!

* *Pārformulēšana:* Kāda ir sakarība starp skaitļiem $20252023$, $20252024$, $20252025$?
  Apzīmē vidējo ar $n$ un pārraksti saucēju.
* *Atskats:* Kur spriedumā izmantots tieši skaitlis $20252024$? Formulē vispārīgu apgalvojumu.

**2.piemērs (LV.NOL.2017.9.2):** Pierādīt, ka $9x^{6}-x^{3}+1 > 0$ visiem reāliem $x$.

* *Pārformulēšana:* $x^6 = (x^3)^2$. Apzīmē $t = x^3$ un atdali pilno kvadrātu izteiksmē
  $9t^2-t+1$.
* *Atskats:* Kurš saskaitāmais nodrošina, ka nevienādība ir **stingra** ($>$, nevis $\geq$)?

**3.piemērs (LV.NOL.2023.9.4):** Atrast visus tādus reālu skaitļu pārus $(x;y)$, kuriem
$\left(x^{4}+1\right)\left(y^{4}+1\right)=4 x^{2} y^{2}$.

* *Izpēte:* Salīdzini $x^4+1$ un $2x^2$ (apskati starpību). Ko tad var teikt par kreiso pusi?
* *Risināšana:* Dotā vienādība nozīmē, ka abās nevienādībās **vienlaikus** iestājas vienādība.
  Kad tas notiek? Neaizmirsti pārbaudīt atrastos pārus.

---

## 1.uzdevums

> **LV.NOL.2014.9.1:**
> Vai vienādojumam $2x^{2}+a^{2}+b^{2}=2x \cdot(a+b)$ ir atrisinājums, ja $a$ un
> $b$ ir dažādi skaitļi?

## 2.uzdevums

> **LV.NOL.2026.9.2:**
> Vai izteiksmi $(2 + 1)(2^2 + 1)(2^4 + 1)(2^8 + 1) \cdots (2^{128} + 1)$ var izteikt formā
> $2^a - 2^b$, kur $a$ un $b$ ir veseli skaitļi?

## 3.uzdevums

> **LV.VOL.2023.9.1:**
> Vai eksistē tādi naturāli skaitļi $x$ un $y$, ka izteiksmes
> $x^{2}-x-y^{2}+y$ vērtība ir **(A)** $10$, **(B)** $2023$?
