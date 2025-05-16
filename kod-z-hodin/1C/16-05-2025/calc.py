# Vypočti od uživatele pomocí zvolené operace číslo na základě dvou zvolených čísel

# ALTGR + F/G => []
while True: # Nekonečný cyklus, zrušen řádkem 57
    resultX = True # Nastavíme hodnoty pro nekonečný cyklus validace čísel
    resultY = True

    while resultX: # Nekonečný cyklus pro validaci X
        x = input("Zadej první číslo: ") # Získáme číslo X a uložíme ho do promměné 
        if(not x.isdigit()): # Pokud X není číslo
            print(f"Neplatná hodnota prvního čísla. {x} není číslo.") # Vypíšeme chybovou hlášku
        else:
            resultX = False # Pomocí hodnoty False zrušíme cyklus
        
    while resultY:
        y = input("Zadej druhé číslo: ") 
        if(not y.isdigit()):
            print(f"Neplatná hodnota druhého čísla. {y} není číslo.")
        else:
            y = float(y) # Převod y na čísla pro validaci a výpočet
            if(y==0): # Řešení validace, jestli je druhé číslo 0
                print(f"Výsledek dělení čísel {x} a {y} nelze spočítat, jelikož {y} je roven nule.") 
            else: 
                resultY = False # Pomocí hodnoty False zrušíme cyklus

    x = float(x) # Převod x pro výpočet
   

    resultOperator = True # Hodnota pro nekončený cyklus validace operátoru
    while resultOperator:
        operator = input("Zadej, co chceš s číslama dělat [+,-,*,/]: ") # Zeptáme se a uložíme do proměnné operátor

    # ALTGR + B/N => {}
    # ALTGR + W => |

        if(operator=="+"): # Podmínky pro výpočet
            print(f"Výsledek sčítání čísel {x} a {y} je {x+y}")
            resultOperator = False # Rušíme cyklus
        elif(operator=="-"):
            print(f"Výsledek odečtu čísel {x} a {y} je {x-y}")
            resultOperator = False
        elif(operator=="*"):
            print(f"Výsledek násobení čísel {x} a {y} je {x*y}")
            resultOperator = False
        elif(operator=="/"):
                print(f"Výsledek dělení čísel {x} a {y} je {x/y}")
                resultOperator = False
        else:
            print(f"CHYBA | Operátor {operator} není platný!") # Pokud se operátor neschoduje ani v jedné podmínce, vypisujeme chybu
    
    result = True # Nastavení hodnoty pro result
    while result: # Nekončený cyklus dotazu na pokračovní
        choice = input("Chceš pokračovat? [ANO/NE] ")
        choice = choice.upper() # Převedu uživatelský vstup na velká písmena aaa => AAA
        if(choice == "NE"):
            print("Tak se měj!")
            exit(); # Ukončíme aplikaci
        elif (choice == "ANO"):
            result = False # Ukončíme cyklus a opakujeme aplikaci
        else:
            print("Nevím, co po mně chceš!") # Pokud ani jedno, zeptáme se uživatele, co chce
