# ⌨️ Uživatelský vstup

Pomocí funkce `input()` můžeme získat data od uživatele během běhu programu. Vstup je vždy typu `str` (řetězec), a pokud potřebujeme číslo, musíme ho převést.

---

## 🧾 Základní použití

```python
jmeno = input("Zadej své jméno: ")
print("Ahoj,", jmeno)
```

- `input()` vypíše zprávu a čeká na zadání od uživatele
- Hodnota se uloží jako řetězec

---

## 🔁 Převod vstupu na číslo

```python
vek = input("Kolik ti je let? ")
vek = int(vek)  # převedeme řetězec na celé číslo

print(f"Za 5 let ti bude {vek + 5}.")
```

> POZOR: Pokud uživatel zadá nečíselný vstup, program skončí chybou (`ValueError`)

---

## 🔒 Ověření vstupu pomocí `isdigit()`

Místo zpracování výjimky můžeme nejprve zkontrolovat, zda vstup obsahuje pouze číslice pomocí metody `isdigit()`:

```python
vek_text = input("Zadej svůj věk: ")

if vek_text.isdigit():
    vek = int(vek_text)
    print("Zadaný věk:", vek)
else:
    print("Zadaná hodnota není číslo. Program se ukončuje.")
```

Tato metoda funguje dobře pro celá čísla (kladná). Pokud bys chtěl opakovat zadávání, dokud nebude vstup správně, lze to řešit pomocí cyklu – k tomu se dostaneme později.

---

## 📋 Shrnutí

- `input()` vrací vždy řetězec
- Číselný vstup je potřeba převádět (např. `int()`, `float()`)
