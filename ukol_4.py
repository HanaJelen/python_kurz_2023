#UKOL_4
#Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

#NEPOVINNÝ BONUS_1
#Zkus svoji první funkci upravit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš například tak, že použiješ metodu .replace(). 
#První parametr metody replace je znak, který chceš nahradit, a druhý parametr nový znak. Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem "".
#Odkaz na dokumentaci metody replace: https://docs.python.org/3/library/stdtypes.html#str.replace

#NEPOVINNÝ BONUS_2
#Přidej svým funkcím typování, aby bylo jasné, jaký typy mají parametry tvých funkcí a jaká je návratová hodnota tvých funkcí.
#K typování se dostaneme až v 5. lekci. Pokud chceš, můžeš úlohu řešit předem pomocí Čtení na doma.

import math

def overeni(cislo: int) -> bool:
    if " " in cislo: # prověřuji, zda se nevskytuje v řetězci mezera, která je brána taktéž jako znak, a popřípaději ji v dalším kroku odstaňuji
        cislo = cislo.replace(" ","")
    if len(cislo) == 9: #telefonní číslo zadáno bez předvolby
        return(True)
    elif len(cislo) == 13:
        if cislo[0:4] == "+420": #zadáno s předvolbou
            return(True)
        else:
            return(False)
    else:
        return(False)

def cena (zprava: str) -> int:
    cena = (math.ceil(len(zprava)/180))*3 #zaokrouhlení nahoru, pro správně nacenění zprávy
    return(cena)

overeni_cisla = overeni(input("Zadejte telefonní číslo: "))
if overeni_cisla == True:
    zprava = input("Zadejte svou zprávu: ")
    print(f"Cena zprávy je {cena(zprava)} Kč.")
else: 
    print("Špatně zadané telefonní číslo.")
