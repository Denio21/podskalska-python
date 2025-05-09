# 🔁 Cykly v Pythonu

Cykly umožňují opakovat určitou činnost – například projít seznam, nebo něco opakovat, dokud platí podmínka.

---

## 🔄 `for` cyklus

`for` cyklus slouží k procházení kolekcí, jako jsou seznamy nebo řetězce.

```python
ovoce = ["jablko", "banán", "hruška"]

for item in ovoce:
    print(item)
```

### Použití s `range()`

```python
for i in range(5):
    print(i)
```

- `range(5)` vytvoří čísla `0, 1, 2, 3, 4`

---

## 🔁 `while` cyklus

`while` cyklus opakuje kód, dokud je podmínka pravdivá.

```python
cislo = 1

while cislo <= 5:
    print(cislo)
    cislo += 1
```

> POZOR: Pokud se podmínka nikdy nestane nepravdivou, cyklus poběží navždy (tzv. nekonečný cyklus).

---

## ⏹ Klíčová slova `break` a `continue`

- `break` – okamžitě ukončí cyklus
- `continue` – přeskočí zbytek těla cyklu a pokračuje další iterací

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 🧪 Praktický příklad

```python
# Výpis sudých čísel do 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

---

## ℹ️ Shrnutí

- `for` cyklus – prochází kolekce nebo rozsahy (`range`)
- `while` cyklus – opakuje, dokud je podmínka pravdivá
- `break` a `continue` – ovlivňují tok cyklu
