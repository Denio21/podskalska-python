def weather(temperature):
    if(temperature<=10):
        print("Dneska je zima")
    elif(temperature<=20):
        print("Vem si mikinu")
    elif(temperature<=35):
        print("Dneska je hezky :)")
    else:
        print("🔥🔥🔥")

def menu():
    print("Vítej v hlavním menu, vyber si, co chceš dělat")
    print("1) Zjistit počasí na základě teploty")
    print("2) Ukončit aplikaci")
    print("--------------------")
    choice = input("Napiš číslo, co chceš dělat: ")
    return choice


while True:
    choice = menu()
    if(int(choice) == 1):
        temp = input("Kolik je venku stupňů: ")
        weather(int(temp))
    elif(int(choice)==2):
        exit();
    else:
        print("Nebyla vybrána správná možnost")