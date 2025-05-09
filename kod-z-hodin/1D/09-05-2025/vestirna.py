# Aplikace věštírna bude získávat:
# - Jméno uživatele
# - Příjmení uživatele
# - Věk uživatele
# A spočítá, kolik bude uživateli za 10 let

# EMOJI = WIN + .
# "" = SHIFT + Ů (vedle L)
# () = SHIFT + ) (klávasea vedle enteru pod backspace)
# | = ALTGR + W
# <> = ALTGR + ./,
# ; = klávesa mezi ESC a TAB
# \ = ALTGR + Q

divider = "--------------"

print("🧙‍♂️ VĚŠTECKÁ SUPER TAJNÁ APLIKACE")
print(divider)
print("Získá uživatelovi údaje a vypíše, kolik mu bude za počet let, který definuje uživatel!")
print(divider+"\n")

# ÚKOL: Přepsat tak, aby uživatel napsal, za kolik let chce vědět svůj věk


#Získat uživatelovi údaje a vypočítat věk
name = input("😅 | Napiš svoje jméno: ") # Získám od uživatele jméno a uložím do name
print("🧙‍♂️ > Chápu, tvé jméno je "+name); # Vypíšu hodnoty od uživatele a potvrzení

lastname = input("😎 | Napiš svoje příjmení: ");
print("🧙‍♂️ > Chápu, tvé příjmení je "+lastname);

age = input("😎 | Napiš svůj věk: ");
print("🧙‍♂️ > Chápu, tvůj věk je "+age);

addition = input("😎 | Napiš, za kolik let chceš vyvěštit tvůj budoucí věk: ")
print("🧙‍♂️ > Chápu, chceš vyvěštit svůj věk za  "+addition+" let.");

futureAge = int(age) + int(addition);

# {} = ALTGR + B/N
print(f"🧙‍♂️ > Tvé jmeno je {name} {lastname}. Teď ji je {age} let, ale za {addition} let ti bude {futureAge}.");
