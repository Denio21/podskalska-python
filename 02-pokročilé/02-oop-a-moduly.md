# 📦 Moduly a import v Pythonu

Moduly nám umožňují rozdělit kód do samostatných souborů nebo používat předpřipravené funkce z Python knihoven. Importem si do programu přidáme nové funkce, proměnné nebo třídy.

---

## 🔹 Co je modul?

Modul je soubor s kódem v Pythonu (`.py`) nebo knihovna, kterou lze znovu použít. Python má:
- 🔧 **standardní moduly** – jsou součástí instalace (např. `math`, `random`, `datetime`)
- 🧰 **vlastní moduly** – soubory, které sami vytvoříme
- 🌐 **externí balíčky** – instalujeme pomocí `pip` (např. `requests`, `numpy`)

---

## ✅ Základní import

```python
import math

odmocnina = math.sqrt(16)
print(odmocnina)  # výstup: 4.0
```

---

## 📌 Import vybrané funkce

```python
from random import randint

cislo = randint(1, 10)
print(cislo)
```

---

## ✍️ Přejmenování modulu (alias)

```python
import datetime as dt

dnes = dt.date.today()
print(dnes)
```

---

## 📄 Vlastní modul (soubor)

1. Vytvoř soubor `mujmodul.py`:

```python
def pozdrav(jmeno):
    print(f"Ahoj, {jmeno}!")
```

2. V hlavním souboru:

```python
import mujmodul

mujmodul.pozdrav("Eva")
```

> Soubor musí být ve stejné složce jako hlavní program.

---

## 📦 Externí balíčky

Instalují se přes příkaz:

```bash
pip install nazev_balicku
```

Poté importujeme stejně jako jiné moduly:

```python
import requests
```

---

## 🧪 Cvičení

1. Použij `random` a generuj náhodná čísla 3×.
2. Vytvoř soubor `nastroje.py` s funkcí `obvod_kruhu(r)`, importuj a použij.
3. Vyzkoušej modul `datetime` – vypiš aktuální čas a datum.

---

## ℹ️ Shrnutí

- `import` vkládá modul do programu
- `from modul import funkce` importuje jen vybranou část
- `as` vytváří alias (zkrácený název)
- Umíme používat standardní, vlastní i externí moduly