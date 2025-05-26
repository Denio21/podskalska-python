# ALTGR + F/G => []
#           0       1       2          3          4
studenti = ["Pavel","Honza","Veronika","Karolína","Zinger"]
print(studenti)
print(len(studenti))
print(studenti[0]) # Vypíše Pavel
studenti.remove("Honza")
studenti.append("Alex")
studenti.sort()
print(studenti)


subjects = ("Matematika","Čeština","Informatika","Matematika")
print(subjects)
subjects = ("Čeština")
print(subjects)

setNames = {"Honza","Pepa","Honza"}
print(setNames)
setNames.add("Honza")
print(setNames)

sortiment = [
    {
        "name":"Rohlík",
        "description":"Levná svačina, která se hodí do každé situace",
        "cena":5,
        "ammount":10,
        "location":["První řada vlevo", "Pátá řada uprostřed"]
    },
    {
        "name":"Houska",
        "description": "Trošku lepší rohlík",
        "cena":10,
        "ammount":5             
    }
]

print(sortiment[0]["location"])