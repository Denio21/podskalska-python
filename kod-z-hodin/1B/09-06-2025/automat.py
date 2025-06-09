# Automat, který uživatel spouští, dává peníze a vyhrává v závislosti na
# kombinaci
# Všechny 3 - 1000 JACKPOT
# Pouze 2 - 100
import random
import winsound
symboly = ["🍒", "🎲","💸","🍌","🤔","😎","👌","🎂"]


print("ZÁZRAČNÝ AUTOMAT 😎💸👌")
try:
    budget = input("Kolik máš peněz? ")
    budget = float(budget)
except:
    print("To není číslo! Zkus to znovu!")
else:
    if(budget<50):
        print("Nemáš prachy na to, abys mohl hrát!")
    else:
        while True:
            vyber = []
            budget = budget - 50;
            print(f"💸 Vhodil jsi 50 Kč do automatu. Tvůj rozpočet je nyní {budget}")


            for item in range(0,3):
                vyber.append(symboly[random.randint(0,len(symboly)-1)])

            print("\nAUTOMAT VYLOSOVAL TYTO SYMBOLY")
            print(f"#    {vyber}    #")
            vyber.sort()
            print("\n")
            if(vyber[0] == vyber[1]):
                if(vyber[1] == vyber[2]):
                    winsound.Beep(300,250)
                    winsound.Beep(500,250)
                    winsound.Beep(300,250)
                    print("🤑 JACKPOT, vyhráváš 1000 peněz")
                    budget+= 1000
                else:
                    print("😎 Vyhráváš 100 Kč")
                    budget += 100
            elif (vyber[1] == vyber[2]):
                print("Vyhráváš 100 Kč")
                budget += 100
            else:
                print("🤦‍♂️ Nevyhráváš nic, smůla")
            

            print(f"\nAktuálně máš {budget} pěnez")
            if(budget <= 0):
                print("KONEC, nemáš prachy :)")
                exit()
            choice = input("\nChceš hrát znovu? Pokud ne, napiš ne: ")
            if(choice.lower() == "ne"):
                print(f"Díky za hru. Odcházíš s {budget}")
                exit()