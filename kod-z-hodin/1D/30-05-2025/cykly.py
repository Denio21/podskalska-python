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