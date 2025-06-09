kosik = []
celkovaCena = 0

rozpocet = input("Napiš, kolik máš peněz: ")
rozpocet = float(rozpocet)
while True:
    nazev = input("Napiš název položky: ")
    if nazev == "konec":
        break
    cena = input("Napiš cenu položky: ")
    cena = float(cena)

    if cena >= 100:
        print("Položka je docela drahá, přesahuje nebo je rovna 100 Kč")

    polozka = {"jmeno":nazev,"hodnota":cena}
    kosik.append(polozka)

print("\nTvůj nákupní košík vypadá takto: ")

for item in kosik:
    print(f"{item["jmeno"]} - {item["hodnota"]} Kč")
    celkovaCena += item["hodnota"]

print(f"Celková cena je {celkovaCena} Kč")
if celkovaCena > rozpocet:
    print("Přesáhl jsi rozpočet")
else:
    print("Nepřesáhl jsi rozpočet")