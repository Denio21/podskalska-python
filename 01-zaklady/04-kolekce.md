

# 📦 Kolekce v Pythonu

Kolekce slouží k ukládání více hodnot do jediné proměnné. Python nabízí několik základních typů kolekcí: seznamy, n-tice, množiny a slovníky.

---

## 🔢 Seznamy (`list`)

Seznamy jsou měnitelné (mutable), uchovávají hodnoty v daném pořadí a mohou obsahovat různé datové typy.

```python
ovoce = ["jablko", "banán", "hruška"]
print(ovoce[0])       # výstup: jablko

ovoce.append("meloun")  # přidání prvku
ovoce.remove("banán")   # odstranění prvku
print(len(ovoce))       # délka seznamu
```

---

## 📐 N-tice (`tuple`)

N-tice jsou neměnitelné (immutable) a slouží k uchování pevných skupin dat.

```python
osoba = ("Anna", 30)
print(osoba[0])       # výstup: Anna
```

- N-tice nelze měnit (např. přidávat prvky)

---

## 🎯 Množiny (`set`)

Množiny jsou neuspořádané kolekce unikátních hodnot.

```python
cisla = {1, 2, 3, 2, 1}
print(cisla)          # výstup: {1, 2, 3}

cisla.add(4)
cisla.remove(2)
```

---

## 📖 Slovníky (`dict`)

Slovníky obsahují dvojice klíč–hodnota. Klíče musí být unikátní.

```python
student = {
    "jmeno": "Karel",
    "vek": 18
}

print(student["jmeno"])    # výstup: Karel

student["trida"] = "4.B"   # přidání nové položky
```

---

## 🧪 Shrnutí

| Typ    | Uspořádané | Měnitelné | Unikátní prvky | Syntaxe           |
|--------|------------|-----------|----------------|-------------------|
| list   | Ano        | Ano       | Ne             | `[]`              |
| tuple  | Ano        | Ne        | Ne             | `()`              |
| set    | Ne         | Ano       | Ano            | `{}`              |
| dict   | Ne         | Ano       | Klíče: Ano     | `{klíč: hodnota}` |
