# 📝 Komentáře a výstup

## Komentáře
Komentáře v Pythonu slouží k vysvětlení kódu a začínají znakem `#`. Python je při běhu programu ignoruje. Používají se např. pro popis toho, co jednotlivé části kódu dělají.

```python
# Toto je komentář
```

## Výstup – funkce `print()`
Funkce `print()` slouží k vypsání informací do konzole. Můžeme vypisovat text, čísla i proměnné.

```python
print("Dobrý den")
print("Součet 2 + 3 je:", 2 + 3)
```

## Spojování řetězců

V Pythonu můžeme text (řetězce) spojovat několika způsoby:

### 1. Pomocí operátoru `+`
Spojuje řetězce bez mezer, vše musí být typu `str`:
```python
jmeno = "Eva"
print("Ahoj " + jmeno + "!")  # výstup: Ahoj Eva!
```

### 2. Pomocí čárky v `print()`
Automaticky přidá mezery, nemusíme převádět čísla na text:
```python
vek = 30
print("Je ti", vek, "let.")  # výstup: Je ti 30 let.
```

### 3. Pomocí formátování `f""` (f-string)
Moderní a přehledný způsob:
```python
print(f"{jmeno} za 10 let oslaví {vek + 10}.")  # f-string: moderní způsob spojování textu s proměnnými
```

### Kdy co použít?
- `+`: jednoduché spojování krátkých textů stejného typu
- `,`: nejjednodušší pro rychlý výpis různých typů (např. čísla)
- `f""`: doporučeno pro přehledný zápis složitějších výpisů s proměnnými

## Praktický příklad
Vytvořme jednoduchý program, který zobrazí uvítání pro uživatele a jeho věk:

```python
# Uvítací program
jmeno = "Eva"
vek = 30

print("Vítej,", jmeno)
print("Je ti", vek, "let.")
print(f"{jmeno} za 10 let oslaví {vek + 10}.")  # f-string: moderní způsob spojování textu s proměnnými
```