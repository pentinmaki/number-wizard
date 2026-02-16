# 🎩 Number Wizard

**Number Wizard** on interaktiivinen numeroarvauspeli komentoriville, jossa on vaikeustasot, pistejärjestelmä ja uudelleenpelattavuus!

## 🎮 Ominaisuudet

✨ **Vaikeustasot:**
- 🟢 **Easy** (1-50) - Helppo aloittelijoille
- 🟡 **Medium** (1-100) - Normaali tasapaino
- 🔴 **Hard** (1-500) - Haastavaa pelaajille

📊 **Pistejärjestelmä:**
- Ansaitse pisteitä vähemmien yritysten perusteella
- Vaikeustaso vaikuttaa pistemäärään
- Näet tilastot pelin lopussa

🔄 **Pelaa uudelleen:**
- Pelaa useita pelejä yhdessä istunnossa
- Seuraa kokonaispisteitä
- Näe keskimääräinen pistemäärä per peli

💡 **Älykäs palaute:**
- Näet erotuksen oikeaan numeroon
- Yritysraja kullekin vaikeustasolla
- Loukkaavat kommentit onnistumisen jälkeen

---

## 📋 Kuinka peli toimii?

1. Valitse vaikeustaso (1, 2 tai 3)
2. Tietokone arpoo satunnaisen luvun
3. Arvaa numeroa - saat palautteen liian pieni/suuri
4. Kun arvaat oikein, saat pisteitä
5. Pelaa uudelleen tai poistu

---

## ▶️ Käynnistys

### 🔧 Vaatimukset

- **Python 3.8+**

### 🟢 Asentaminen ja käynnistys

```bash
# Siirry projektikansion
cd number-wizard

# Aja peli
python game.py
# tai
py game.py
```

### 🧪 Testaus

Automaattisten testien ajaminen:

```bash
python test_game.py
# tai
py test_game.py
```

Testit varmistavat:
- ✓ Pistejärjestelmä
- ✓ Vaikeustasot
- ✓ Yritysrajoitukset
- ✓ Pistelaskenta logiikka
- ✓ Vaikeuden kertoimet

---

## 📊 Esimerkki pelistä

```
========================================
  🧙 WELCOME TO NUMBER WIZARD! 🧙
========================================

=== SELECTA DIFFICULTY ===
1. Easy   (1-50)
2. Medium (1-100)
3. Hard   (1-500)
Choose difficulty (1-3): 2

→ I'm thinking of a number between 1 and 100...
Guess (attempts left: 20): 50
↓ Too high! (difference: ~25)
Guess (attempts left: 19): 25
↑ Too low! (difference: ~2)
Guess (attempts left: 18): 27
✓ Congratulations! You guessed it in 3 tries!
Points earned: 142
Total score: 142

⭐ Amazing! You're a true wizard!
```

---

## 🎯 Pisteistä

Kaava:
- **Base Score:** 100 - (yritykset × 5)
- **Vaikeuden kerroin:**
  - Easy: ×1
  - Medium: ×1.5
  - Hard: ×2

Esimerkki: Medium-tasolla 10 yrityksellä = (100 - 50) × 1.5 = **75 pistettä**

---

## 📁 Projektirakenteen

```
number-wizard/
├── game.py           # Pääohjelma
├── test_game.py      # Automaattisten testit
├── README.md         # Tämä tiedosto
└── LICENSE           # Lisenssitiedosto
```

---

## 🧑‍💻 Kehittäjälle

### Pelin funktiot:

- `select_difficulty()` - Valitse vaikeustaso
- `calculate_score()` - Laske pisteet
- `play_game()` - Pääpelifunktio

### Muokkaamisideat:

- Lisää korkeimpien pisteiden tallennus
- Verkon yli pelaava versio
- Graafinen käyttöliittymä
- Eri pelitilat

---

## 📘 Lisenssi

Tämä projekti on avoimen lähdekoodin alle MIT-lisenssillä. Vapaasti käytettävissä, muokattavissa ja jakelussa!

Kehitys: 2026 | Python 3.12+ | Windows/Linux/Mac

