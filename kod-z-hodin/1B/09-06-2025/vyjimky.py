try: #Blok kódu, který chceme otestovat na chyby, neodchytává syntax chyby
    promena = x
except: #Co se stane, pokud nastane chyba
    print("X není definováno")
    x=0
else: #Co se stane, pokud chyba nenastane
    print("Vše v pořádku")
finally: #Vykonání věci v případě chyby i v případě žádného problému
    print("Hotovo ", x)

if x == 0:
    raise ValueError("Kámo, x je nula, to není úplně ok") #Vyvolá chybu