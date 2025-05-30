students = ["Honza","Pepa","Terka","Verča"]

print(students)

# for item in students:
#     print("Právě uložené jméno je: " + item);
#     newName = input("Zadejte jméno k přepisu: ")
#     students[students.index(item)] = newName #students.index(item) vyheldá index (číselnou pozici) v poli v závislosti na vyhledávání

# cislo = input("Napiš náhodné číslo: ")
# while not cislo.isdigit():
#     print(f"Specifikované číslo není číslo: {cislo}")
#     cislo = input("Napiš náhodné číslo: ")

# print(cislo)

# for i in range(25):
#     if i == 18:
#         break
#     print(f"{i} Ahoj"*i)

for i in range(20):
    if(i == 10):
        print("Byla detekována 10!")
        continue
    print("😯"*i)
    
    
print("Cyklus byl roztrhnut")