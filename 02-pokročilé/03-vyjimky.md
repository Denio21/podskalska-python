# ⚠️ Výjimky a ošetření chyb v Pythonu

Při běhu programu může dojít k chybám – tzv. **výjimkám** (angl. *exceptions*). Pokud je neošetříme, program spadne. Python umožňuje tyto situace zachytit a zareagovat pomocí bloku `try-except`.

---

## 🧨 Co je výjimka?

Výjimka je speciální chyba, která přeruší běh programu, např.:

```python
cislo = int("abc")  # ValueError
```

---

## ✅ Ošetření pomocí `try` a `except`

```python
try:
    cislo = int(input("Zadej číslo: "))
    print("Zadal jsi:", cislo)
except ValueError:
    print("To nebylo číslo!")
```

---

## ➕ Blok `else` a `finally`

- `else`: spustí se, když nenastane výjimka
- `finally`: spustí se vždy, i při chybě

```python
try:
    x = int(input("Zadej číslo: "))
except ValueError:
    print("Neplatný vstup.")
else:
    print("Zadal jsi:", x)
finally:
    print("Hotovo.")
```

---

## 📋 Časté typy výjimek

| Výjimka          | Kdy nastává                           |
|------------------|----------------------------------------|
| `ValueError`     | neplatná konverze (`int("abc")`)       |
| `ZeroDivisionError` | dělení nulou (`1/0`)                 |
| `IndexError`     | přístup mimo rozsah seznamu            |
| `FileNotFoundError` | pokus o otevření neexistujícího souboru |

---

## 🔁 Příklad s cyklem – opakovaný vstup

```python
while True:
    vstup = input("Zadej celé číslo: ")
    try:
        cislo = int(vstup)
        break
    except ValueError:
        print("Zkus to znovu.")

print("Zadal jsi:", cislo)
```

---

## 🎯 Bonus: vlastní výjimka

```python
vek = int(input("Zadej svůj věk: "))

if vek < 0:
    raise ValueError("Věk nemůže být záporný!")
```

---

## 🧪 Shrnutí

- Výjimky zachytáváš pomocí `try` a `except`
- Pomáhá to zabránit pádu programu
- Můžeš kombinovat s `else`, `finally`
- Pomocí `raise` můžeš vyvolat chybu ručně