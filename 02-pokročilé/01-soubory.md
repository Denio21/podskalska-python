# 📁 Práce se soubory v Pythonu

Python umí velmi jednoduše pracovat s textovými soubory – číst je, zapisovat do nich a vytvářet nové. To se hodí např. pro ukládání výsledků, nastavení, poznámek a dat.

---

## 🧰 Otevření souboru

Funkce `open()` slouží k otevření souboru.

```python
soubor = open("data.txt", "r", encoding="utf-8")
obsah = soubor.read()
soubor.close()
```

Tento způsob funguje, ale **lepší je používat `with`**, který soubor automaticky zavře:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    obsah = f.read()
    print(obsah)
```

---

## 📚 Režimy otevření souboru

| Režim | Popis                             |
|-------|-----------------------------------|
| `"r"` | čtení (read) – soubor musí existovat |
| `"w"` | zápis (write) – smaže původní obsah |
| `"a"` | přidání (append) na konec         |
| `"x"` | vytvoření nového souboru (chyba, pokud existuje) |

---

## ✍️ Zápis do souboru

```python
with open("zprava.txt", "w", encoding="utf-8") as f:
    f.write("Toto je moje první zpráva.\n")
    f.write("A další řádek.")
```

- Pokud soubor neexistuje, vytvoří se.
- Pokud existuje, bude přepsán.

---

## ➕ Přidání do souboru

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Záznam 1\n")
    f.write("Záznam 2\n")
```

---

## 📖 Čtení po řádcích

```python
with open("zprava.txt", "r", encoding="utf-8") as f:
    for radek in f:
        print(radek.strip())  # odstraní \n na konci
```

---

## 📋 Zápis seznamu do souboru

```python
nákup = ["chleba", "máslo", "mléko"]

with open("nakup.txt", "w", encoding="utf-8") as f:
    for polozka in nákup:
        f.write(polozka + "\n")
```

---

## 🔁 Vstup od uživatele a zápis

```python
with open("poznamky.txt", "a", encoding="utf-8") as f:
    while True:
        text = input("Zapiš poznámku (nebo 'konec'): ")
        if text.lower() == "konec":
            break
        f.write(text + "\n")
```

---

## ⚠️ Ošetření chyby – soubor neexistuje

```python
try:
    with open("neexistuje.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Soubor neexistuje.")
```

---

## 🧪 Praktický příklad: poznámkový blok

```python
def pridej_poznamku():
    text = input("Zadej poznámku: ")
    with open("poznamky.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

def vypis_poznamky():
    try:
        with open("poznamky.txt", "r", encoding="utf-8") as f:
            print("📄 Poznámky:")
            for radek in f:
                print("- " + radek.strip())
    except FileNotFoundError:
        print("Zatím žádné poznámky.")

while True:
    volba = input("\nCo chceš udělat? [1] Přidat, [2] Zobrazit, [3] Konec: ")
    if volba == "1":
        pridej_poznamku()
    elif volba == "2":
        vypis_poznamky()
    elif volba == "3":
        break
    else:
        print("Neplatná volba.")
```

---

## ℹ️ Shrnutí

- `open("soubor", "r/w/a", encoding="utf-8")` otevře soubor
- `with` je bezpečný způsob – automaticky zavře
- `write()`, `read()`, `readline()`, `writelines()` umožňují práci s obsahem
- vhodné pro logy, poznámky, konfigurace, exporty