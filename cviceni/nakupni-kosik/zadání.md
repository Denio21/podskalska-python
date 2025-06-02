# 🧮 Cvičení: Kalkulačka nákupního seznamu

Vytvoř program, který umožní uživateli vytvořit nákupní seznam a spočítat celkovou útratu.

---

## 🧾 Zadání

1. Program se uživatele opakovaně ptá:
   - **název položky** (např. "mléko")
   - **cena položky** v Kč
2. Pokud uživatel zadá jako název `konec`, zadávání se ukončí.
3. Každou položku uloží jako **slovník** do seznamu:
```python
{"nazev": "mléko", "cena": 25}
```
4. Na konci program:
   - vypíše všechny položky se jménem a cenou
   - spočítá celkovou útratu
   - zjistí, zda uživatel **nepřekročil rozpočet 300 Kč**

---

## 🔁 Ukázka chování programu

```
Zadej název položky: chléb
Zadej cenu: 40

Zadej název položky: máslo
Zadej cenu: 50

Zadej název položky: čokoláda
Zadej cenu: 60

Zadej název položky: konec

Nákupní seznam:
- chléb: 40 Kč
- máslo: 50 Kč
- čokoláda: 60 Kč

Celkem: 150 Kč
Rozpočet nebyl překročen.
```

---

## 💡 Tipy

- Použij `while` cyklus s podmínkou (`while True:` a `break`)
- Cena bude `int()` nebo `float()`
- Kolekce: seznam položek, každá položka jako slovník
- Po skončení použij `for` cyklus k výpisu a výpočtu

---

## 🎯 Bonus

- Umožni zadat rozpočet uživatelem
- Upozorni na položky dražší než 100 Kč