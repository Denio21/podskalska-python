# 🔀 Podmínky a operátory v Pythonu

V této lekci se naučíš, jak v Pythonu rozhodovat pomocí podmínek a jak používat operátory pro porovnání a logické výrazy.

---

## ✅ Podmínky `if`, `elif`, `else`

Podmínky umožňují vykonat určitý blok kódu pouze tehdy, když je splněna daná podmínka.

```python
vek = 18

if vek >= 18:
    print("Jsi dospělý.")
else:
    print("Jsi nezletilý.")
```

Můžeme použít i více větví pomocí `elif`:

```python
znamka = 2

if znamka == 1:
    print("Výborně")
elif znamka == 2:
    print("Chvalitebně")
elif znamka == 3:
    print("Dobře")
else:
    print("Zlepši se")
```

---

## 🧮 Porovnávací operátory

Porovnávají dvě hodnoty a vrací `True` nebo `False`.

| Operátor | Význam                 | Příklad (`x = 5`, `y = 3`) |
|----------|------------------------|----------------------------|
| `==`     | rovnost                | `x == y` → `False`         |
| `!=`     | nerovnost              | `x != y` → `True`          |
| `>`      | větší než              | `x > y` → `True`           |
| `<`      | menší než              | `x < y` → `False`          |
| `>=`     | větší nebo rovno       | `x >= 5` → `True`          |
| `<=`     | menší nebo rovno       | `x <= 3` → `True`          |

---

## 🧠 Logické operátory

Umožňují spojovat více podmínek dohromady.

| Operátor | Význam        | Příklad                   |
|----------|---------------|---------------------------|
| `and`    | a zároveň     | `x > 0 and x < 10`        |
| `or`     | nebo          | `x < 0 or x > 100`        |
| `not`    | negace (ne)   | `not (x == 5)`            |

### Použití `not`

Operátor `not` převrací logickou hodnotu výrazu – pokud je `True`, stane se `False`, a naopak.

```python
je_admin = False

if not je_admin:
    print("Nemáš oprávnění.")  # i když jsme deklarovali False, negace nám změní na True
```

V tomto případě je výraz `not je_admin` pravdivý, protože `je_admin` je `False`. Výstup tedy bude `"Nemáš oprávnění."`.

---

## 🧪 Příklady

```python
# Kombinace podmínek
jmeno = "Anna"
vek = 17

if jmeno == "Anna" and vek >= 18:
    print("Vítej, Anna.")
else:
    print("Nemáš přístup.")

# Logická negace
prihlasen = False

if not prihlasen: # i když jsme deklarovali False, negace nám změní na True
    print("Prosím, přihlas se.")
```

---

## ℹ️ Shrnutí

- `if`, `elif`, `else` používáme k větvení programu podle podmínek
- Porovnávací operátory slouží ke srovnávání hodnot
- Logické operátory spojují více podmínek dohromady