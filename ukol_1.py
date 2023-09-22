# Zadání:
# Napiš program, který bude obsahovat jednu proměnnou jmeno. 
# Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). 
# Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše.


jmeno = "Hana"

print (f"{jmeno}@czechitas.cz")

# Nepovinný bonus:
    # Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. 
    # Obsah proměnné načti od uživatele pomocí funkce input. 
    # Tvůj program postupně vypíše několik způsobů formátování jména:
        # všechna písmena velká (vypíše např. JANA MALÁ)
        # všechna písmena malá (vypíše např. jana malá)
        # standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
        # iniciály (vypíše např. J. M.)
        # křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
# Zaexperimentuj s různými vstupy od uživatele (co třeba JaNA maLá?).

jmeno_a_prijmeni = input("Zadejte své jméno a následně příjmení: ")

if " " not in jmeno_a_prijmeni : # kontrola, která zachytí chybu v případě vynechání mezery
    print("Zadejte své jméno znovu a nezapomeňte jméno a příjmení oddělit mezerou.")
    jmeno_a_prijmeni = input("Zadejte své jméno a následně příjmení: ")

print(jmeno_a_prijmeni.upper()) #výpis jména velkými písmeny
print(jmeno_a_prijmeni.lower()) #výpis jména malými písmeny

rozdeleni = jmeno_a_prijmeni.split(" ") #rozdělení zadaného řetězce na seznam obsahující dva samostatné řetězce a to "jmeno" a "příjmení"

print (rozdeleni[0][0].upper()+rozdeleni[0][1:].lower()+" "+rozdeleni[1][0].upper()+rozdeleni[1][1:].lower()) #výpis prvního písmene jména velkám písmem a zbytek malým

print (rozdeleni[0][0].upper() + "." + rozdeleni[1][0].upper() + ".") #výpis iniciálu velkými písmeny

if len(rozdeleni[0]) > 5:
    print (rozdeleni[0][0] + ". "+ rozdeleni[1]) #zkrácení dlouho jména na iniciál
else:
    print (jmeno_a_prijmeni)
  
