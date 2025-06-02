kosik = []
divider = "------------------"
print("Aplikace nákupního košíku 🤷‍♂️")
print(divider)

while True:
    rozpocet = input("Zadej svůj rozpočet: ")
    print(divider)
    if(rozpocet.isdigit()):
        rozpocet = float(rozpocet)
        break
    else:
        print(f"Zadaný rozpočet {rozpocet} není platná hodnota.")
    
while True:
    nazev = input("Napiš název položky: ");
    if nazev == "konec":
        print("Ukončuji zápis produktů")
        break;
 

    while True:
        cena = input(f"Napiš cenu položky [{nazev}]: ")
        if cena.isdigit():     
            cena = float(cena)
            break;
        else:
            print(f"Zadaná hodnota {cena} není platnou cenou!")
    if cena > 100:
        print(f"Položka {nazev} je moc drahá, přesahuje 100 Kč")

    #ALTGR + B/N
    
    polozka = {"nazev":nazev,"cena":cena}
    kosik.append(polozka)
    print(divider)

print("Váš nákupní košík:")
print(divider)
for item in kosik:
    print(f"{item["nazev"]} - {item["cena"]} Kč") 

suma = 0
for item in kosik:
    suma += item["cena"]

print(divider)

print(f"Celková útrata je {suma} Kč")

if suma > rozpocet:
    print(f"Překročil jsi rozpočet {rozpocet} Kč")
else:
    print("V pořádku, cash ještě máš")