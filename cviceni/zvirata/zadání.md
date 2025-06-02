# 🧠 Cvičení: Inteligentní hádání zvířete (rozšířená verze)

Tento program napodobuje jednoduchou „umělou inteligenci“, která se pomocí otázek snaží zjistit, na jaké zvíře uživatel myslí.

---

## 🎯 Cíl

- Uživatel si tajně myslí **jedno ze zvířat v seznamu**.
- Program pokládá **otázek na vlastnosti** a postupně **zužuje výběr**.
- Jakmile zůstane **jedno zvíře**, program se zeptá:
  > „Je to [zvíře]?“  
  A čeká na odpověď „ano“ nebo „ne“.

---

## 🧠 Přednastavená databáze zvířat

```python
zvirata = [
    {"nazev": "pes",       "srst": True,  "voda": False, "lita": False, "domaci": True,  "divoke": False, "savec": True,  "zobak": False, "les": False, "velke": False},
    {"nazev": "kočka",     "srst": True,  "voda": False, "lita": False, "domaci": True,  "divoke": False, "savec": True,  "zobak": False, "les": False, "velke": False},
    {"nazev": "kráva",     "srst": True,  "voda": False, "lita": False, "domaci": True,  "divoke": False, "savec": True,  "zobak": False, "les": False, "velke": True},
    {"nazev": "vlk",       "srst": True,  "voda": False, "lita": False, "domaci": False, "divoke": True,  "savec": True,  "zobak": False, "les": True,  "velke": False},
    {"nazev": "lišák",     "srst": True,  "voda": False, "lita": False, "domaci": False, "divoke": True,  "savec": True,  "zobak": False, "les": True,  "velke": False},
    {"nazev": "kapr",      "srst": False, "voda": True,  "lita": False, "domaci": False, "divoke": True,  "savec": False, "zobak": False, "les": False, "velke": False},
    {"nazev": "delfín",    "srst": False, "voda": True,  "lita": False, "domaci": False, "divoke": True,  "savec": True,  "zobak": False, "les": False, "velke": True},
    {"nazev": "žralok",    "srst": False, "voda": True,  "lita": False, "domaci": False, "divoke": True,  "savec": False, "zobak": False, "les": False, "velke": True},
    {"nazev": "papoušek",  "srst": False, "voda": False, "lita": True,  "domaci": True,  "divoke": False, "savec": False, "zobak": True,  "les": False, "velke": False},
    {"nazev": "orel",      "srst": False, "voda": False, "lita": True,  "domaci": False, "divoke": True,  "savec": False, "zobak": True,  "les": True,  "velke": True},
    {"nazev": "sova",      "srst": False, "voda": False, "lita": True,  "domaci": False, "divoke": True,  "savec": False, "zobak": True,  "les": True,  "velke": False},
    {"nazev": "žába",      "srst": False, "voda": True,  "lita": False, "domaci": False, "divoke": True,  "savec": False, "zobak": False, "les": True,  "velke": False},
    {"nazev": "netopýr",   "srst": True,  "voda": False, "lita": True,  "domaci": False, "divoke": True,  "savec": True,  "zobak": False, "les": True,  "velke": False},
    {"nazev": "krokodýl",  "srst": False, "voda": True,  "lita": False, "domaci": False, "divoke": True,  "savec": False, "zobak": False, "les": False, "velke": True},
    {"nazev": "kůň",       "srst": True,  "voda": False, "lita": False, "domaci": True,  "divoke": False, "savec": True,  "zobak": False, "les": False, "velke": True}
]
```

---

## 🔍 Otázky, které můžeš pokládat

Program se uživatele ptá:

- „Má to srst?“  
- „Žije to ve vodě?“  
- „Létá to?“  
- „Je to domácí zvíře?“  
- „Je to divoké zvíře?“

---

## ✅ Chování programu

- Uživatel odpovídá pouze `ano` / `ne`
- Program si odpovědi ukládá a filtruje seznam zvířat podle shody
- Jakmile zbyde 1 zvíře → dotaz „Je to [zvíře]?“
- Pokud žádné zvíře nezbyde → výstup: **"Nevím, na co myslíš 😕"**

---

## 💡 Tipy k řešení

- Ukládej vlastnosti jako `True/False` a převeď odpověď `ano/ne` na boolean
- Použij `list comprehension` pro filtrování seznamu
- Proměnné: `moznosti = zvirata[:]`
- Cyklus, dokud `len(moznosti) > 1`

---

## 🔁 Ukázka průběhu

```
Mysli si zvíře ze seznamu: pes, kočka, kráva, vlk, kapr, delfín, papoušek, orel, žába, netopýr

Má to srst? ano  
Létá to? ano  
Je to domácí zvíře? ne  

Je to netopýr? ano

🎉 Uhodl jsem!
```

---

## 🎯 Bonusové úkoly

- Zobrazuj, kolik zvířat ještě zbývá
- Nabídni možnost restartovat hru
- Umožni přidat nové zvíře (interaktivně) – výzva pro pokročilé

---

## 🧪 Shrnutí, co si procvičíš

- Práce s kolekcemi (`list` + `dict`)
- Uživatelský vstup + logika s `if/else`
- Cykly `while`, `for`, `break`
- Filtrace dat podle podmínek