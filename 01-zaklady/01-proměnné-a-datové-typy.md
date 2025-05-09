# 🧠 Proměnné a datové typy

## Co je to proměnná?

Proměnná je pojmenované místo v paměti, do kterého ukládáme nějakou hodnotu. V Pythonu nemusíme uvádět typ – Python ho odvodí automaticky.

### Zápis:
```python
jmeno = "Anna"
vek = 25
```

- `jmeno` je proměnná obsahující text (řetězec)
- `vek` je proměnná obsahující číslo (celé číslo – integer)

---

## Pravidla pojmenování proměnných

- Název může obsahovat písmena, čísla a podtržítka (_)
- Nesmí začínat číslem
- Nerozlišují se klíčová slova (např. `for`, `if`, `class`)
- Python je case-sensitive: `vek` a `Vek` jsou dvě různé proměnné

```python
# platné názvy
cislo1 = 10
_jmeno = "Eva"
adresa_domu = "Praha"

# neplatné názvy
# 1cislo = 5      # začíná číslem
# for = "text"    # klíčové slovo
# obvykle je dobré nepsat do názvů proměnných diakritiku, proto je lepší, když využíváme anglické názvy
```

---

## Základní datové typy

| Typ          | Příklad            | Popis                          |
|--------------|--------------------|---------------------------------|
| `int`        | `10`               | Celé číslo                     |
| `float`      | `3.14`             | Desetinné číslo                |
| `str`        | `"text"`           | Řetězec (text)                 |
| `bool`       | `True`, `False`    | Logická hodnota                |

### Ukázky:
```python
vek = 30               # int
teplota = 22.5         # float
jmeno = "Tereza"       # str
je_dospely = True      # bool
```

---

## Funkce `type()`

Pomáhá zjistit, jaký typ má hodnota v proměnné:
```python
print(type(jmeno))        # <class 'str'>
print(type(vek))          # <class 'int'>
print(type(teplota))      # <class 'float'>
print(type(je_dospely))   # <class 'bool'>
```

---

## Přetypování (konverze mezi typy)

Python umožňuje převádět typy pomocí vestavěných funkcí:

```python
# číslo na text
vek = 25
text = str(vek)
print("Věk: " + text) # zde musí dojít k přetypování, nelze spojovat string a int

# text na číslo
cislo = int("100")
desetinne = float("3.14")

# číslo na boolean
print(bool(0))    # False
print(bool(1))    # True
```

---

## Praktický příklad
```python
jmeno = "Lukáš"
vek = 20

print(jmeno + " má " + str(vek) + " let.")
print(f"Za 5 let mu bude {vek + 5}.")  # nemusíme přetypovávat – f-string automaticky převede čísla na text
print("Typ proměnné 'vek':", type(vek))
```

---

✅ **Shrnutí:**
- Proměnné ukládají hodnoty různého typu
- Není třeba uvádět datový typ – Python ho určí automaticky
- Používej srozumitelné názvy
- Funkce `type()` a konverzní funkce (`str()`, `int()`, `float()`) jsou užitečné při práci s daty

