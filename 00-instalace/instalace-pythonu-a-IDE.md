

# Instalace Pythonu a Visual Studio Code

Tento návod vás provede instalací Pythonu a editoru Visual Studio Code (VS Code) pro pohodlné programování v jazyce Python.

---

## 🐍 Instalace Pythonu

### Windows

1. Navštivte oficiální stránky: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Stáhněte aktuální verzi pro Windows.
3. Rozklikněte instalační balíček a dodržujte pokyny instalátoru. (**Důležité:** Zaškrtněte políčko `Add Python to PATH`.)

 Ověření instalace:
   ```bash
   python --version
   ```

### macOS

1. Zkontrolujte, zda již Python máte:
   ```bash
   python3 --version
   ```
2. Pokud není:
   ```bash
   brew install python
   ```

### Linux (Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## 🛠 Instalace Visual Studio Code

1. Navštivte: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Stáhněte a nainstalujte VS Code podle vašeho operačního systému.
3. Otevřete VS Code a přejděte do sekce **Extensions** (Ctrl+Shift+X).
4. Vyhledejte a nainstalujte plugin **Python** (vývojář: Microsoft).

---

## ✅ První spuštění a test

1. Otevřete VS Code a vytvořte složku pro váš projekt.
2. Vytvořte nový soubor `hello.py`.
3. Zadejte do něj:
   ```python
   print("Python je připraven!");
   ```
4. Klikněte na tlačítko přehrávání, program by se měl správně spustit.