# 🧩 Funkce v Pythonu

Funkce nám umožňují rozdělit kód na menší části, které můžeme opakovaně používat. Díky nim je program přehlednější a lépe se udržuje.

---

## 🔧 Definice funkce

Funkce definujeme pomocí klíčového slova `def`.

```python
def pozdrav():
    print("Ahoj světe!")
```

Volání funkce:
```python
pozdrav()
```

---

## 📦 Parametry

Funkci můžeme předat vstupní hodnoty – tzv. parametry.

```python
def pozdrav_jmeno(jmeno):
    print("Ahoj", jmeno)

pozdrav_jmeno("Tereza")
```

---

## 🎁 Návratová hodnota (`return`)

Pomocí `return` může funkce vrátit výsledek výpočtu.

```python
def secti(a, b):
    return a + b

vysledek = secti(3, 4)
print("Součet je:", vysledek)
```

> Funkce může mít více parametrů, ale vrací vždy právě jednu hodnotu (může být např. `tuple`).

---

## ⚠️ Rozdíl mezi `print()` a `return`

- `print()` pouze něco vypíše na obrazovku – používá se při testování nebo komunikaci s uživatelem.
- `return` předává výsledek výpočtu dál do programu.

---

## 📌 Příklad: kontrola plnoletosti

```python
def je_plnolety(vek):
    return vek >= 18

vek = int(input("Zadej svůj věk: "))

if je_plnolety(vek):
    print("Jsi plnoletý.")
else:
    print("Jsi nezletilý.")
```

---

## ℹ️ Shrnutí

- Funkce definujeme pomocí `def`
- Parametry slouží k předání vstupních dat
- `return` vrací výsledek funkce
- Funkce zvyšují přehlednost a opakovatelnost kódu