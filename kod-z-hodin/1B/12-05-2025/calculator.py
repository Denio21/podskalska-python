divider = "--------------";  # Definice proměnné oddělovač pro hezčí výpis (slouží jako vizuální oddělení sekcí)

# Vypíše úvod aplikace
print("😎 VELMI CHYTRÁ KALKULAČKA");  # Úvodní hláška kalkulačky
print(divider);  # Vytiskne oddělovač
print("Jsem kalkulačka, která ti provede libovolný výpočet mezi dvěmi čísly");  # Krátké info o funkcionalitě

# Spustí nekonečný cyklus - program se opakuje, dokud uživatel nezvolí konec
while True:
    print(divider,"\n");  # Vytiskne oddělovač a prázdný řádek pro přehlednost

    x = input("Napiš první číslo: ");  # Načte první vstup od uživatele
    if (not(x.isdigit())):  # Kontrola, zda vstup je celé číslo (jinak konec)
        print("Zadaná hodnota není číslem, ukončuji program")  # Upozornění
        exit()  # Ukončí program

    y = input("Napiš druhé číslo: ");  # Načte druhé číslo
    if (not(y.isdigit())):  # Stejná kontrola jako výše
        print("Zadaná hodnota není číslem, ukončuji program")
        exit()

    operation = input("Zvol operaci, kterou chceš provést (+, -, *, /): ")  # Zeptá se na matematickou operaci

    x = float(x);  # Převede první vstup na desetinné číslo
    y = float(y);  # Převede druhý vstup na desetinné číslo

    print(divider,"\n");  # Znovu oddělovač a nový řádek

    # Nyní podle zadané operace provede příslušný výpočet
    if(operation == "+"):
        print(f"Výsledek sčítání mezi čísly {x} a {y} je {x+y}");  # Pokud je operace sčítání
    elif(operation=="-"):
        print(f"Výsledek odečítání mezi čísly {x} a {y} je {x-y}");  # Odečítání
    elif(operation=="*"):
        print(f"Výsledek násobení mezi čísly {x} a {y} je {x*y}");  # Násobení
    elif(operation == "/"):
        if(float(y) != 0):  # Kontrola, jestli nedělíme nulou
            print(f"Výsledek dělení mezi čísly {x} a {y} je {x/y}");  
        else:
            print(f"Nelze dělit nulou");  # Výpis chyby při dělení nulou
    else:
        print(f"Byla zadána neplatná operace");  # Pokud operace není žádná z očekávaných

    cont = input("Chceš pokračovat (Y/N): ");  # Zeptá se uživatele, jestli chce pokračovat

    if(cont.lower() == "n"):  # Pokud zadá "n" nebo "N", ukončí se cyklus
        break;
    else:
        print("Dobrá, pojedeme dál")  # Jinak se program spustí znovu

print("Díky za využití kalkulačky 😎")  # Závěrečné poděkování při ukončení
