# Získá od uživatele maximální počet studentů ve třídě
# Získá jména studentů
# Vyhodnotí absenci ve třídě a zobrazí seznam přítomných
# \ => ALTGR+Q , [] => ALTGR + F/G , {} => ALTGR+B/N

divider = "----------------"
print("🙂 | Aplikace pro kontrolu absence ve třídě")
print(divider)
print("Aplikace má za úkol na základě zapsaných informací vypočítat míru absence ve třídě");
print(divider,"\n")

while True:
    maxCount = input("Napiš mi maximální počet studentů ve třídě: ")
    if maxCount.isdigit():
        print(f"> Hodnota [{maxCount}] byla zanesena.")
        break
    else:
        print(f"Byla zadána hodnota [{maxCount}], která není číslem.")

students = []
counter = 1;

print(divider,"\n")
while True:
    print("Program můžeš ukončit napsáním slova EXIT.")
    name = input(f"Napiš jmeno studenta/studentky [{counter}]: ")
    if name.strip() == "":
        print("Nebylo specifikováno jméno.")
        continue
    elif name == "EXIT":
        print("Zaznamenáno slovo EXIT, ukončuji zápis.")
        break
    else:
        if(not name.isdigit()):
            students.append(name)
        else:
            print("Nebylo specifikováno jméno.")
            continue
    counter += 1;

students.sort()
print(divider)

counter = 1;

for student in students:
    print(f"{counter} |\t{student}")
    counter += 1
    
print(divider,"\n")

maxCount = int(maxCount)
if(maxCount<len(students)):
    print(f"Kapacita třídy byla překročena - maximální kapacita je {maxCount} přičemž bylo zapsáno {len(students)} studentů.")
    print(f"Statistika přítomnosti ve třídě je {len(students)/maxCount*100}%")
    print(f"Přebývá {len(students)-maxCount} studentů.")
elif(maxCount>len(students)):
    print(f"Ve třídě chybí žáci, maximální kapacita je {maxCount} studentů, přičěmž jich bylo zapsáno pouze {len(students)}.")
    print(f"Statistika přítomnosti ve třídě je {len(students)/maxCount*100}%")
    print(f"Chybí {maxCount-len(students)} studentů.")
else:
    print(f"Ve třídě jsou všichni, maximální kapacita je {maxCount} studentů a bylo zapsáno {len(students)}.")
    print(f"Statistika přítomnosti ve třídě je {len(students)/maxCount*100}%")