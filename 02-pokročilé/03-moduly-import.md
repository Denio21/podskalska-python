# 📦 Moduly a import v Pythonu

Moduly nám umožňují rozdělit kód do samostatných souborů nebo používat předpřipravené funkce z Python knihoven. Importem si do programu přidáme nové funkce, proměnné nebo třídy.

---

## 🔹 Co je modul?

Modul je soubor s kódem v Pythonu (`.py`) nebo knihovna, kterou lze znovu použít. Python má:

- 🔧 **Standardní moduly** – součástí instalace (např. `math`, `random`, `datetime`)
- 🧰 **Vlastní moduly** – soubory, které sami vytvoříme
- 🌐 **Externí balíčky** – instalujeme pomocí `pip` (např. `requests`, `pandas`)

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

Externí balíčky nejsou součástí základní instalace Pythonu. Instalujeme je pomocí příkazu:

```bash
pip install nazev_balicku
```

Příklad:

```bash
pip install requests
```

Pak je můžeme použít v programu:

```python
import requests
```

Další balíčky najdeš na oficiálním katalogu:  
🔗 [https://pypi.org/](https://pypi.org/)

---

## 📚 Dokumentace modulů

Pokud si nejsi jistý, co modul obsahuje nebo jak se používá, můžeš:

- použít funkci `help()`:

```python
import math
help(math)
```

- použít `dir()` pro seznam funkcí a atributů:

```python
import datetime
print(dir(datetime))
```

---

## 🧰 Nejznámější balíčky z praxe

| Balíček     | Účel použití                          |
|-------------|----------------------------------------|
| `requests`  | HTTP požadavky (např. API)            |
| `pandas`    | práce s tabulkami a daty              |
| `numpy`     | matematika a pole                     |
| `matplotlib`| grafy a vizualizace                   |
| `flask`     | webové aplikace (server)              |
| `pygame`    | tvorba 2D her                         |

> Tyto balíčky je třeba doinstalovat pomocí `pip`.

---

## 🧪 Cvičení

1. Použij `random` a generuj náhodná čísla 3×.
2. Vytvoř soubor `nastroje.py` s funkcí `obvod_kruhu(r)`, importuj a použij.
3. Vyzkoušej modul `datetime` – vypiš aktuální čas a datum.

---

## ℹ️ Shrnutí

- `import` načte celý modul
- `from modul import funkce` – vybraná funkce
- `as` vytvoří zkrácený alias
- Umíme pracovat se standardními, vlastními i externími moduly