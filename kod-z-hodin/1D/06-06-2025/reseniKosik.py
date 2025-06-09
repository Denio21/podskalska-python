kosik = []
celkovaCena = 0

rozpocet = input("Napiš svůj celkový rozpočet: ")
rozpocet = float(rozpocet)

while True:
    nazev = input("Napiš název položky: ")
    if nazev.lower() == "konec":
        break
    cena = input(f"Napiš cenu produktu {nazev}: ")
    cena = float(cena)

    if cena > 100:
        print("Věc je drahá, přesahuje 100 kč")

    polozka = {"nazev":nazev,"cena":cena}
    kosik.append(polozka)

print("\nVáš nákupní košík vypadá takto\n------------------")
for item in kosik:
    print(f"{item["nazev"]} - {item["cena"]} kč")
    celkovaCena += item["cena"]
print("------------------\n")
print(f"Celková cena činí {celkovaCena} kč")

if(celkovaCena > rozpocet):
    print("Přesáhl jsi rozpočet")
else:
    print("Nepřesáhl jsi celkový rozpočet")