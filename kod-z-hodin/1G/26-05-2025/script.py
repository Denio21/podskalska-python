#LIST - měnitelný, uspořádaný, může obsahovat duplicity, []
# ALTGR + F/G => []
#        0      1       2       3      4          5
jmena = ["Pepa","Pepa","Honza","Filip","Kateřina","Sofie"]
print(jmena[4])
jmena.append("Jana")
jmena.remove("Pepa")
jmena[4] = "Josef"
jmena.append("Alex")
jmena.append("Zungi")
jmena.sort()
jmena.reverse()
print(jmena[len(jmena)-1])
print(jmena)
print(len(jmena))

#TUPLE - neměnitelný, uspořádaný, může obsahovat duplicity, ()
#           0         1            2     3
subjects = ("Čeština","Matematika","ZSV","ICT","Čeština")
print(subjects[0])
print(subjects[len(subjects)-1])
print(subjects.count("Čeština"))

#SET - měnitelná, není uspořadná, nedá se volat přes indexy, bez duplicit, {}
knihovna = {"HP KM", "Dášenka","Obraz DG", "Dášenka"}
print(knihovna)
knihovna.add("Hobit")
knihovna.remove("Dášenka")
#{'Dášenka', 'Hobit', 'Obraz DG', 'HP KM'}

#DICTIONARY - klíč:hodnota, není uspořádaný
# Klíč by měl být unikátní, dá se měnit
slovnik={
    "english":"Happy",
    "czech":"Šťastný"
}
print(slovnik["czech"])
#KOMBINACE KOLEKCÍ - LIST + DICTIONARY
slovnik = [
    {
        "english":"Sad",
        "czech":"Smutný"
    },
    {
        "english":"Happy",
        "czech":"Šťastný"
    }
]
print(slovnik[0]["english"])
slovnik = {
    "sad":{
        "czech":"Smutný",
        "czechDescription": "Pocit smutku nebo neštěstí"
    }
}
print(slovnik["sad"]["czechDescription"])