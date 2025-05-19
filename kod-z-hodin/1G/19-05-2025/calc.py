# Od uživatele vezmeme dvě čísla a operaci, kterou mezi čísly chce provést
# A provedeme správný výpočet

#WIN + . => 🍒😻

x = input("😉 Napiš své první číslo: ")
y = input("🤔 Napiš své druhé číslo: ")
operator = input("🤦‍♂️ Co chceš s čísly dělat [+,-,*,/]: ")

x = float(x)
y = float(y)

#ALTGR + F/G => []
#ALTGR + B/N => {}
if (operator == "+"):
    print(f"Výsledek sčítání čísel {x} a {y} je {x+y}");
elif (operator == "-"):
    print(f"Výsledek odčítání čísel {x} a {y} je {x-y}");
elif (operator == "*"):
    print(f"Výsledek násobení čísel {x} a {y} je {x*y}");
elif (operator == "/"):
    if(y == 0):
        print("Nelze dělit nulou, smůla!")
    else:
        print(f"Výsledek dělení čísel {x} a {y} je {x/y}")
else:
    print("Neznámý operátor, nemohu provést výpočet!")