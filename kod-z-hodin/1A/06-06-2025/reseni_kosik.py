kosik = []
celkova_cena = 0

rozpocet = input("Napiš, kolik jsi schopen utratit: ")
rozpocet = float(rozpocet)

while True:
    nazev = input("Napiš název položky: ")
    if nazev == "konec":
        break
    cena = input("Napiš cenu položky: ")
    cena = float(cena)
    celkova_cena += cena
    polozka = {"nazev":nazev,"cena":cena}
    kosik.append(polozka)

for item in kosik:
    print(f"{item["nazev"]} - {item["cena"]} kč")


print(f"Celková cena je {celkova_cena} kč")

# ALTGR + ,/. <><><>
#screenshot = WIN + SHIFT + S
if(celkova_cena > rozpocet):
    print("Překročil jsi rozpočet")
else:
    print("Rozpočet jsi nepřekročil")