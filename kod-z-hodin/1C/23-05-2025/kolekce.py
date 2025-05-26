# LIST - listy se mění, jsou uspořádané, obsahují prvky více datových typů
# ALTGR + F/G = [] - ALTGR je pravý ALT
#           0       1        2           3
students = ["Josef","Matyáš","František","Veronika","Alex"]
print(students[3])
students.append("Honza")
students[0] = "Pepa"
print(len(students))
print(students)
print(students[len(students)-1])
print(len(students))
students.remove("František")
print(students)
print(len(students))
students.append("Matyáš")
print(students)
print(len(students))
students.sort()
print(students)
print(len(students))

#TUPLE - jak ho jednou nadefinuji, tak se nedá změnit - drží uspořádání, definuje se ()
knihy = ("Učebnice češtiny", "Učebnice němčiny", "Obraz Doriana Graye")
print(knihy)
print(knihy[2])
print(len(knihy))
# knihy.sort() - přecházel by hodnoty - tuple je neměnitelný, hodí chybu

#SETS - mohu je měnit, organizují se samy, nemají duplicitní hodnoty - zbavíse jich sám
# {} => ALTGR + B/N
znamky = {2,1,1,4,2,4,3,4,2,1,3,5}
znamky.add(6)
print(znamky)

jmena = {"Pavel", "Honza","Karel", "Honza","Alex","Zungo"}
print(jmena)

#DICTIONARY - obsahuje klíče a hodnoty, klíče musí být unikátní, dají se přepisovat
slovnik = {
    #KEY      VALUES
    "english":"Happy",
    "czech":"šťastný",
    "englishDefinition":"feeling or showing pleasure or contentment",
    "czechDefinition":"naplněný pocitem štěstí, blaženosti"
}
print(slovnik["english"],slovnik["englishDefinition"])
slovnik["english"] = "The happiest person that has ever lived!"
print(slovnik["english"])
slovnik["explanation"] = "Proč potřebuješ vysvětlení, ty nevíš, co je to býti být šťastným"
print(slovnik["explanation"])
print(slovnik)

slovnikExt = [
    {
    #KEY      VALUES
    "english":"Happy",
    "czech":"šťastný",
    "englishDefinition":"feeling or showing pleasure or contentment",
    "czechDefinition":"naplněný pocitem štěstí, blaženosti"
},
{
    #KEY      VALUES
    "english":"Happy",
    "czech":"šťastný",
    "englishDefinition":"feeling or showing pleasure or contentment",
    "czechDefinition":"naplněný pocitem štěstí, blaženosti"
}
]
print(slovnikExt[0]["english"])