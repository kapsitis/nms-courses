---
layout: default
title: Arhīvs
---
# ĀVĢ rezultātu tabula

| Segvārds | <a href="{{ 'socrative_archive/2025-10-13-comb-rule-of-product.pdf' | relative_url }}" title="Kombinatorika: Reizināšanas likums">T1.1</a> | <a href="{{ 'socrative_archive/2025-10-13-geom-finding-angles.pdf' | relative_url }}" title="Ģeometrija: Leņķu atrašana">T1.2</a> | <a href="{{ 'socrative_archive/2025-10-13-pigeonhole-principle-part1.pdf' | relative_url }}" title="Dirihlē princips-1">T1.3</a> | <a href="{{ 'socrative_archive/2025-10-13-pigeonhole-principle-part2.pdf' | relative_url }}" title="Dirihlē princips-2">T1.4</a> | <a href="{{ 'socrative_archive/2025-10-27-nt-divisibility-part1.pdf' | relative_url }}" title="Skaitļu teorija: Dalāmība-1">T2.1</a> | <a href="{{ 'socrative_archive/2025-10-27-alg-recurrences.pdf' | relative_url }}" title="Algebra: Rekurentas virknes">T2.2</a> |
| ------------------ | ---- | ---- | ---- | ---- | ---- | ---- | 
| `123`              | -    | -    | -    | -    |    - |  9.0 |
| `ba5dec24`         | -    | -    | -    | -    |    - |  4.0 |
| `bebebite`         | -    | -    | -    | -    |  9.0 |  8.0 |
| `Cube`             | 7.0  | 9.0  | 8.0  | 6.0  | -    | 10.0 |
| `fc65db56`         | -    | -    | -    | -    |  6.0 | -    |
| `ju hu`            | -    | -    | -    | -    |  8.0 |  3.0 |
| `Sarkanasēne`      | 2.0  | 0.0  | 7.0  | 3.0  | -    | -    |
| `t0mats`           | -    | -    | 1.0  | 2.0  | -    | -    |
| `teko`             | -    | -    | -    | -    | 10.0 |  5.0 |
| `Proboscis Monkey` | -    | -    | -    | -    |  9.0 |  9.0 |
| `Tasargarosnuķi`   | -    | -    | -    | -    |  7.0 | -    |
| `Zeķe`             | -    | -    | -    | -    |    - |  4.0 |
| `zvaigzne`         | -    | -    | 6.0  | -    | -    | -    |



## Ja tas pats lietotājs testu kārtojis vairākkārt

No vairākiem rezultātiem ieraksta skaitliski lielāko, 
citus neņem vērā.

## Ja tests aizpildīts ļoti nepilnīgi

Ja ir redzamas tikai 1-2 iesūtītas atbildes no 10 vai arī 
testa rezultāts ir 0, to tabulā neraksta, lai nebūtu 
rezultātu tabulā jāieraksta cilvēki, kuri nejauši uzsākuši 
testu un nav domājuši to pabeigt.


## Ja Socrative ierakstīts īstais vārds 

Lai ievērotu testa dalībnieku privātumu, īstos vārdus 
nerakstām un aicinām visus izvēlēties segvārdus, ko norāda 
aiz daļsvītras.

Ja kāds Socrative testā norādījis īsto vārdu, tad 
pārliecināmies, ka tas uzrakstīts pilnā formā 
(piemēram, "Vārds", "Vārds Uzvārds" - 
ar lielo sākuma burtu un arī garumzīmēm un mīkstinājumzīmēm); 
to pārveidojam par CRC32 hešvērtību; tabulā rakstām pirmos 4 baitus.
Šāds attēlojums nedod iespēju nevienam no ārpuses atjaunot vārdu, 
cilvēks pats var savu hešvērtību pārbaudīt un 
gandrīz noteikti diviem dažādiem vārdiem hešvērtības 
nesakritīs.

```
import sys
import zlib

def string_to_8hex(s):
    val = '{:08x}'.format(zlib.crc32(s.encode('utf-8')) & 0xffffffff)
    print(f"hash({s}) = {val}")

string_to_8hex("Vārds")
```