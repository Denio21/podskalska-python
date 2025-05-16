# Vezme dvě čísla od uživatele, zjístí, co s nimi chce dělat a provede výpočet

# ALTGR + X => #
# ALTGR + F/G => []

# Úvod
divider = "---------------------"

while True:
    print("😣 Extrémně chytrá super kalkulačka")
    print("Vezme dvě čísla a vypočítá operaci dle definovaného operátoru")
    print(divider,"\n")

    # Získám dvě čísla
    x = input("Napiš první číslo: ") # Brané jako text
    if(not x.isdigit()):
        print(f"{x} není číslo :(")
        exit();

    y = input("Napiš druhé čislo: ")
    if(not y.isdigit()):
        print(f"{y} není číslo :(")
        exit();

    # Získám operátor
    operator = input("Napiš, co chceš s číslama dělat [+,-,*,/]: ")

    # Převedu si text na číslo
    x = float(x)
    y = float(y)

    # ALTGR + B/N => {}
    # Provedu výpočet
    if (operator == "+"):
        print(f"Výsledek sčítání mezi čísly {x} a {y} je {x + y}")
    elif (operator == "-"):
        print(f"Výsledek odčítání mezi čísly {x} a {y} je {x - y}")
    elif (operator == "*"):
        print(f"Výsledek násobení mezi čísly {x} a {y} je {x * y}")
    elif (operator == "/"):
        if(y==0):
            print("Nulou se dělit nedá")
        else:
            print(f"Výsledek dělení mezi čísly {x} a {y} je {x / y}")
    else:
        print(f"😥 Operátor [{operator}] není platným operátorem!")

    print(divider,"\n")

    result = True

    while result:
        choice = input("Chceš pokračovat? [ANO/NE]: ")
        if(choice.upper() == "ANO"):
            result = False
        elif(choice.upper() == "NE"):
            print("Tak ahoj!")
            exit()
        else:
            print("Nerozumím, napiš znovu, co chceš!")
    print(divider,"\n")
