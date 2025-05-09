# Jsem fiktivní banka, musím ověřit zda klient je pro mě vhodným příjemcem úvěru
# Pokud klient vydělává < 10 000/měsíčně - nepujčím mu nic, je rizikový
# Pokud klient vydělává <= 20 000/měsíčně - pujčím mu max 10k
# Pokud klient vydělává <= 50 000/měsíčně - pujčím mu max 100k
# Pokud klient vydělává > 50 000/měsíčně - pujčím mu max 1 mega

# Definice proměnné oddělovač
divider = "------------------------";

# Vypasání úvodu aplikace a jejího popisu
print("🐧 BANKA TUČŇÁK A.S. - APLIKACE VYHODNOCENÍ KLIENTA");
print(divider); # Vypisujeme oddělovač prostřednictvím proměnné
print("Aplikace má za úkol vyhodnotit rizikovst klienta na základě jeho měsičního příjmu");
print(divider);


name = input("😉 | Napište své jméno: ") # Zeptáme se uživatele na jméno
print("👍 | Potvrzuji, vaše jméno je: "+name) # Vypíšeme potvrzení jména

lastname = input("😉 | Napište své příjmení: ") # Zeptáme se uživatele na příjmení
print("👍 | Potvrzuji, vaše příjmení je: "+lastname);# Vypíšeme potvrzení příjmení

income = input("😉 | Napište svůj měsíční příjem: ") # Zeptáme se uživatele na jeho příjem
print("👍 | Potvrzuji, váš měsíční příjem je: "+income); # Vypíšeme potvrzení příjmu

# {} = ALTGR + B/N
print(f"Dobrý den, pane/paní {name} {lastname}. Váš měsíční příjem je {income} Kč.");

# Pokud klient vydělává < 10 000/měsíčně - nepujčím mu nic, je rizikový
# Pokud klient vydělává <= 20 000/měsíčně - pujčím mu max 10k
# Pokud klient vydělává <= 50 000/měsíčně - pujčím mu max 100k
# Pokud klient vydělává > 50 000/měsíčně - pujčím mu max 1 mega

income = int(income);

# Definice podmínky úvěru
if (income<10000):
    print("😂👉 Jsi chudý, jdi makat. Tobě nic nedáme!")
    print("HAHAHA")
elif (income <= 20000):
    print("Vám můžeme půjčit maximálně 10 000 Kč")
elif (income<=50000):
    print("Vám můžeme půjčit maximálně 100 000 Kč")
elif (income > 500000):
    print("Vám můžeme půjčit maximálně 1 000 000 Kč")
