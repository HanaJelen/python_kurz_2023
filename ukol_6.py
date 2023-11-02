#ÚKOL_6:
#Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:
    #Registrační značka	Značka a typ vozidla Počet najetých kilometrů
    #4A2 3020	Peugeot 403 Cabrio	47534
    #1P3 4747	Škoda Octavia	41253
#Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:
    #registrační značka automobilu registracni_znacka,
    #značka a typ vozidla typ_vozidla,
    #počet najetých kilometrů najete_km,
    #informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).
#Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. 
    #Poslední atribut rovnou nastav jako True, tj. na začátku je vozidlo vždy volné.

#Vytvoř objekty, které reprezentují oba automobily půjčovny.
#Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. 
#Pokud je volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". 
#Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".
#Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.
#Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. 
#Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().
#Otestuj, že program nedovolí půjčit stejné auto dvakrát.

#BONUS:
#Přidej třídě Auto metodu vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. 
# Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.
#Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. 
#Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return.

class Auto:
    def __init__(self,registracni_znacka, typ_vozidla, najete_km, dostupnost = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = dostupnost
    def pujc_auto(self):
        if self.dostupnost:
            self.dostupnost = False
            return f"Potvrzuji zapůjčení vozidla."
        return f"Vozidlo není k dispozici."
    def get_info(self):
        if self.dostupnost:
            return f"Automobil značky {self.typ_vozidla} s registrační značkou {self.registracni_znacka} je dostupný."
        return f"Automobil značky {self.typ_vozidla} s registrační značkou {self.registracni_znacka} je zapůjčený."
    def vrat_auto(self, stav_tachometr, doba_zapujceni):#bonusové cvičení
        if self.dostupnost == False:
            self.najete_km = stav_tachometr
            self.dostupnost = True
            cena = 400 * doba_zapujceni
            if doba_zapujceni >= 7:
                cena = 300 * doba_zapujceni
            return f"Cena za zapůjčení auta značky {self.typ_vozidla} s registrační začnou {self.registracni_znacka} činí {cena} Kč." 
        return f"Auto nebylo zapůjčeno. Jedná se o chybu."


peugeot = Auto("4A23020","Peugeot 403 Cabrio", 47534)
octavia = Auto("1P34747","Škoda Octavia", 41253)
auta = [peugeot, octavia] #vytvoření seznamu aut

car = input("Zadejte požadovaný typ vozidla: ") #dotaz k zakazníkovi, car = "Škoda"

for auto in auta:
    if car in auto.typ_vozidla:
        print (auto.get_info())
        if auto.dostupnost:
            print (auto.pujc_auto())
 
print(octavia.pujc_auto()) #ověření, zda znovu nepůjčí stejný vůz v případě zapůjčení Škoda Octavia

print(octavia.vrat_auto(41603,7))
print(octavia.najete_km) #ověření přepisu najeté km
print(octavia.get_info())#ověření, že auto je nastaveno k dispozici
