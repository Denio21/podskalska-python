students = ["Pepa","Honza","Emílie","Františka"]
for item in students:
    print(item)
    
for i in range(50):
    students.append("Karolína")

print(students)

for i in range(10):
    if i == 3:
        break
    print("😶"*i)
    
    
while True:
    print("Nekonečný cyklus AAAAAAAAAA")
    end = input("Napiš ano, aby byl už konec: ")
    if end == "ano":
        break

while len(students)>0:
    for item in students:
        print(item)

for i in range(20):
    if(i == 10):
        print("Byla detekována 10!")
        continue
    print("😯"*i)
    
    
print("Cyklus byl roztrhnut")