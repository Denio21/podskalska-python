
#0-9 WIN+. CTRL+C
# for i in range(10000):
#     print("🍌"*i)
#[] = ALTGR+F/G, {} ALTGR+B/N, \ - ALTGR+Q, ALTGR+./, =<>

pivo = ["Braník","Plzeň","Svijany","Primátor","Staropramen"]
hodnoceni = ["⭐⭐⭐⭐","⭐⭐⭐⭐⭐","⭐⭐⭐","⭐⭐⭐⭐⭐","⭐⭐"]

for item in pivo:
    print(f"Pivo: {item} - {hodnoceni[pivo.index(item)]}")

counter = 1;
input("");

while len(pivo)>0:
    print(f"{counter} Piva je hodně!")

    if(counter == 10000):
        break
    counter+=1;

print("Ahoj")