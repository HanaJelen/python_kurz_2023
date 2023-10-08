#ÚKOL_3
#Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.
#Soubor si ulož a načti do slovníku.
#Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. 
#Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".
#Výsledný slovník ulož jako JSON do souboru prospech.json.

import json

with open ("body.json", mode = "r", encoding = "utf-8") as file:
    body = json.load(file)

vysledky = {}

for student, value in body.items():
    if value >= 60:
        vysledky[student] = "Pass"
    else:
        vysledky[student] = "Fail"

with open("prospech.json",mode = "w", encoding="utf-8") as file:
    json.dump(vysledky,file, ensure_ascii=False, indent = 4)

#NEPOVINNÝ BONUS
#Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.
#Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:
#1: 90 a více, 2: 70-89, 3: 50-69, 4: 30-49, 5: 29 a méně
#Výsledný slovník ulož jako JSON do souboru znamky.json

with open("bonusy.json", mode = "r", encoding = "utf-8") as file2:
    bonus = json.load(file2)

vysledky_s_bonusy = {}

for student, value in bonus.items():
    if student in body:
        body[student] +=  value

znamky = {}

for student in body:
    if body[student] >= 90:
        znamky[student] = "1"
    elif body[student] >= 70:
        znamky[student] = "2"
    elif body[student] >= 50:
        znamky[student] = "3"
    elif body[student] >= 30:
        znamky[student] = "4"
    else:
        znamky[student] = "5"

with open("znamky.json", mode = "w", encoding = "utf-8") as file:
    json.dump(znamky, file, ensure_ascii = False, indent = 4)

