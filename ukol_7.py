#DOMÁCÍ ÚKOL_7: Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:
'''
platná data:
2.2.2022
13. 8. 1999
4/5/2001
 
neplatná data:
5.123.458.91
21.4
8./9
'''
# VÝSLEDNÝ regulární výraz: (\d|\d\d)\W ?(\d|\d\d)\W ?\d{4}
 
#Zkopíruj si obsah souboru posta.txt do regex101 jako testovací řetězec. Vymysli regulární výraz, který označí všechny "poslední řádky adresy" v textu. 
#Poslední řádka adresy zpravidla obsahuje PSČ a název obce, například 190 16 PRAHA 916 nebo 742 45 FULNEK. Celkem by jich mělo být 18.

# VÝSLEDNÝ regulární výraz: \d{3} \d{2} \D.*

#NEPOVINNÝ BONUS:
# Napiš program, který se zeptá uživatele na jeho přihlašovací jméno, e-mailovou adresu a heslo. 
# Po každém zadaném údaji program ověří jeho správnost podle následujících pravidel:
    #uživatelské jméno smí obsahovat malá a velká písmena (nesmí obsahovat žádné jiné znaky), jeho minimálná délka je 6 znaků a jeho maximální délka je 10 znaků.
    #heslo smí obsahovat malá a velká písmena, číslice, a následující speciální znaky: _, -, ., +, =. Jeho minimálná délka je 12 znaků a jeho maximální délka je 30 znaků.
    #e-mail by měl být validním e-mailem 🙂 Tady jsou nějaké testovací příklady (viz zdroj)

#Zkuste se zaměřit na to, aby program pokryl co nejvíce platných e-mailových adres. Cílem není pokrýt všechny platné, a vyloučit všechny neplatné, 
# ale zkusit si napsat regex, který to zvládne co nejlépe, i když třeba ne perfektně! Bonus odevzdej, i když nebude dokonalý.

import re

jmeno = input("Zadejte jméno: ")
heslo = input("Zadejte heslo: ")
mail = input("Zadejte e-mail: ")

#vložení txt dokumentu pro ověřování zadých adres i ve VSC
'''
soubor = open("mail.txt", mode = "r", encoding="utf-8")
maily = soubor.read()
mail = maily.split("\n")
soubor.close()
'''

regularni_vyraz = re.compile(r"\w{6,10}")#vyraz hledá v UNICODE
rv_jmeno = regularni_vyraz.fullmatch(jmeno)
if rv_jmeno:
    print("Zadané jméno je v pořádku.")
else:
    print("Jméno bylo zadáno špatně.")

regularni_vyraz2 = re.compile(r"[\w\-\.\+\=]{12,30}")#vyraz hledá v UNICODE
rv_heslo = regularni_vyraz2.fullmatch(heslo)
if rv_heslo:
    print("Zadané heslo je v pořádku.")
else:
    print("Heslo bylo zadáno špatně.")

regularni_vyraz3 = re.compile(r"^\"?\w+[\.\+\-]?\w+\"?@(\w+\.?\-?\w+\.\w+[^w.b]$|\[?(\d\d\d\.){3}\d\d\d]?$)",flags=re.ASCII)#výraz hledá pouze v ASCII
rv_mail = regularni_vyraz3.match(mail)
if rv_mail:
    print("Zadaný e-mail je v pořádku.")
else:
    print("E-mail byl zadán špatně.")

#zde je cyklus pro prověřovní zadaných adres ve VSC
'''    
for item in mail:
    rv_mail = regularni_vyraz3.match(item)
    print(rv_mail)
'''
