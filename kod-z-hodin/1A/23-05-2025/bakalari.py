# Aplikace bude zjišťovat absenci ve třídě dle zadaných parametrů
# Učitel zadá max počet žáků ve třídě, jejich jména a aplikace spočítá, kolik jich chybí
# \n - newline - zalomí to řádek

divider = "----------------"
print("😑 BAKALÁŘI 0.5")
print(divider)
print("Aplikace bude zjišťovat absenci ve třídě dle zadaných parametrů\nUčitel zadá max počet žáků ve třídě, jejich jména a aplikace spočítá, kolik jich chybí")
print(divider)

maxClass = input("Kolik žáků má být ve třídě?: ")
maxClass = int(maxClass)

students = []

while True:
    print("Pokud chceš zápis studentů ukončit, napiš EXIT.")
    student = input(f"Napiš jméno studenta/studentky [{len(students)+1}]: ")
    if(student == "EXIT"):
        break
    else:
        students.append(student)

print(f"Jména studentů, kteří jsou ve třídě: {students}")

if(len(students) < maxClass):
    print(f"Ve třídě chybí studenti, počet chybějicích studentů je {maxClass-len(students)}.")
elif (len(students) == maxClass):
    print(f"Všichni studenti jsou přítomní, počet studentů je {len(students)}.")
else:
    print(f"Ve třídě je více studentů, než by mělo být. Počet studentů je {len(students)}.")