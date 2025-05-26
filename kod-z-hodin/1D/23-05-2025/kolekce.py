# Listy - měnit dají, uspořadané, [] - ALTGR + FG
#           0      1 2  3     4    5
studenti = ["Pepa",0,27,21.42,True,0]
print(studenti[0])
print(studenti)
studenti.append("Honza")
studenti.remove(0)

studenti[0] = "Josef"

print(studenti)
print(studenti[len(studenti)-1]) #len(studenti) - počet prvků v listu

#Tuple - to stejný jako list, ale nedá se měnit, značí se ()
sortiment = ("Rohlík","Banán","BMW")
print(sortiment)
print(sortiment[len(sortiment)-1])
#sortiment[0] = "Houska" - error, nejde měnit

#Set - to stejný jako list, dá se měnit, ale nemůže obsahovat duplicity
#Set nedodržuje uspořádání, uspořádá dle abecedy sám
knihovna = {"Harry Potter 1", "Obraz Doriana", "Obraz Doriana", "Abeceda hrou"}
print(knihovna)

#Sortění listů
jmena = ["Zungi","Pepa","Honza","Alex","Jakub"]
jmena.sort()
print(jmena)

#Dictionary - klíče/hodnoty, klíče musí být unikátní
slovnik = {
    "english":"Happy",
    "czech":"Šťastný",
    "czechDescription": "naplněný pocitem štěstí, blaženosti",
    "englishDescription":"feeling or showing pleasure or contentment",
    "czech":"haha"
}

print(slovnik["czech"])

#Dictionary ale s více slovy, protože jedno slovo bad
slovnik = [{
    "english":"Happy",
    "czech":"Šťastný",
    "czechDescription": "naplněný pocitem štěstí, blaženosti",
    "englishDescription":"feeling or showing pleasure or contentment",
    "czech":"haha"
},{
   "english":"Happy",
    "czech":"Šťastný",
    "czechDescription": "naplněný pocitem štěstí, blaženosti",
    "englishDescription":"feeling or showing pleasure or contentment",
    "czech":"haha" 
}
]
print(slovnik[1]["czech"])
