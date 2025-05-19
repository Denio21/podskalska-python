# Od uživatele vezmeme dvě čísla a operaci, kterou mezi čísly chce provést
# A provedeme správný výpočet

#WIN + . => 🍒😻

validationX = True;
while validationX:
    x = input("😉 Napiš své první číslo: ")
    if(not x.isdigit()):
        print("Zadané číslo není číslem!")
    else:
        validationX = False;

    
validationY = True;
while validationY:
    y = input("🤔 Napiš své druhé číslo: ")
    if(not y.isdigit()):
        print("Zadané číslo není číslem!")
    else:
        validationY = False


x = float(x)
y = float(y)


validationOperator = True
while validationOperator:
    operator = input("🤦‍♂️ Co chceš s čísly dělat [+,-,*,/]: ")
    if (operator == "+"):
        print(f"Výsledek sčítání čísel {x} a {y} je {x+y}");
        validationOperator = False
    elif (operator == "-"):
        print(f"Výsledek odčítání čísel {x} a {y} je {x-y}");
        validationOperator = False
    elif (operator == "*"):
        print(f"Výsledek násobení čísel {x} a {y} je {x*y}");
        validationOperator = False
    elif (operator == "/"):
        if(y == 0):
            print("Nelze dělit nulou, smůla!")
        else:
            print(f"Výsledek dělení čísel {x} a {y} je {x/y}")
            validationOperator = False
    else:
        print("Neznámý operátor, nemohu provést výpočet!")