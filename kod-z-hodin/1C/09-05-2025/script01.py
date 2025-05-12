# Budeme chít vylepšit appku, aby byla hezčí a srozumitelnější
# Přidáme podmínky na věk:
# age < 18 => "Jsi moc mladý."
# age < 25 => Za chvilku ti bude třicet
# age < 35 => Už se těšíš na krizi středního věku?
# age < 70 => Jsi starý, pamatuješ si i minulej režim 
# age > 70 => Smrtka čeká :)
# {} = ALTGR + B/N
# ALTGR + ./, = <><><><>

divider = "--------------"

# ÚKOL: Uprav kód tak, aby získal od uživatele, kolik let chce předpovídat do budoucna

print("🧙‍♂️ VĚŠTECKÁ SUPER TAJNÁ APLIKACE")
print(divider)
print("Získá uživatelovi údaje a vypíše, kolik mu bude za počet let, který definuje uživatel!")
print(divider+"\n")

# Získat uživatelovi údaje a vypočítat věk
name = input("😅 | Napiš svoje jméno: ") # Získám od uživatele jméno a uložím do name
print("🧙‍♂️ > Chápu, tvé jméno je "+name); # Vypíšu hodnoty od uživatele a potvrzení

lastname = input("😎 | Napiš svoje příjmení: ");
print("🧙‍♂️ > Chápu, tvé příjmení je "+lastname);

age = input("😎 | Napiš svůj věk: ");
print("🧙‍♂️ > Chápu, tvůj věk je "+age);

addition = input("😎 | Napiš, za kolik let chceš předpovídat: ");
print("🧙‍♂️ > Chápu, chceš předpovídat za  "+addition+" let.");

futureAge = int(age) + int(addition);


print(f"🧙‍♂️ > Tvé jmeno je {name} {lastname}. Teď ji je {age} let, ale za {addition} let ti bude {futureAge}.");

age = int(age)

if (age < 18):
    print("Jsi moc mladý.")
elif(age < 25):
    print("Za chvilku ti bude třicet")
elif(age < 35):
    print("Už se těšíš na krizi středního věku?")
elif(age < 70):
    print("Jsi starý, pamatuješ si i minulej režim ")
elif(age > 70):
    print("Smrtka čeká :)")
