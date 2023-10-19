#ÚKOL_5
#Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
#Vytvoř seznam průměrných teplot pro každý den.

import statistics
prumer = [statistics.mean(den) for den in teploty]
print(f"Průměrné teploty: po: {prumer[0]:0.2f}°C, út: {prumer[1]:0.2f}°C, st: {prumer[2]:0.2f}°C, čt: {prumer[3]:0.2f}°C, pá: {prumer[4]:0.2f}°C, so: {prumer[5]:0.2f}°C, ne: {prumer[6]:0.2f}°C")

#Vytvoř seznam ranních teplot.

rano = [rano[0] for rano in teploty]
print(f"Ranní teploty: po: {rano[0]}°C, út: {rano[1]}°C, st: {rano[2]}°C, čt: {rano[3]}°C, pá: {rano[4]}°C, so: {rano[5]}°C, ne: {rano[6]}°C")

#Vytvoř seznam nočních teplot.

noc = [noc[-1] for noc in teploty]
print(f"Noční teploty: po: {noc[0]}°C, út: {noc[1]}°C, st: {noc[2]}°C, čt: {noc[3]}°C, pá: {noc[4]}°C, so: {noc[5]}°C, ne: {noc[6]}°C")

#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

pol_noc = [[teplota[1], teplota[-1]] for teplota in teploty]
print(f"Polední a noční teploty: po: {pol_noc[0]}°C, út: {pol_noc[1]}°C, st: {pol_noc[2]}°C, čt: {pol_noc[3]}°C, pá: {pol_noc[4]}°C, so: {pol_noc[5]}°C, ne: {pol_noc[6]}°C")

#NEPOVINNÝ BONUS:
#Krom teplot máme k dispozici i informaci o dnu v týdnu:

teploty2 = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

#Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den. {den: průměrná teplota}
teploty_dict = {}

'''
for den in teploty: #vytvoření slovníku s průměnýma hodnotama za pomocí cyklu
    teploty_dict[den[0]] = f"{statistics.mean(den[1:]):0.2f}"
'''

for den in teploty2: #vytvořím si ze seznamu slovník, kdy klíčem jsou dny v týdnu a hodnotami teploty měřené během dne
    teploty_dict[den[0]] = den[1:]

print(teploty_dict)

prumer2 = {den:f"{statistics.mean(teplota):0.2f}°C" for den, teplota in teploty_dict.items()}
print(prumer2)