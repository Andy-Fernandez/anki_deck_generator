# 📚 Anki Deck Builder – Verb Tenses (Gen‑Z Edition)

> **Goal:** Give you a reusable, hacker‑friendly starter kit for crafting English‑grammar decks (and any other topic) with spaced repetition. Clone it, swap the CSV, rerun — profit. 💸

---

## 🗂️ Project Layout

```text
anki_tenses/
├── english_verb_tenses.csv   # ✨ Your data (Front,Back)
├── genz_style.css            # 🎨 Card look & feel
├── build_deck.py             # 🐍 Deck compiler (CSV → .apkg)
└── README.md                 # 📖 You are here
```

*Feel free to rename folders/files — just update the paths inside `build_deck.py`.*

---

## 🚀 Quick‑Start (macOS M‑chip & friends)

```bash
# 1. Grab the repo / files
mkdir anki_tenses && cd anki_tenses
# (copy the CSV, CSS & build_deck.py here)

# 2. Optional: create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows ▶ .venv\Scripts\activate

# 3. Install dependency
pip install --upgrade pip genanki

# 4. Compile the deck
python build_deck.py
# → Verb_Tenses_GenZ.apkg appears

# 5. Open Anki → Import → select the .apkg
```

> **Heads‑up:** `genanki` is pure‑Python; no Apple‑silicon hassles. ✌️

---

## 📝 CSV Schema

| Column    | Required | Description                                         |
| --------- | -------- | --------------------------------------------------- |
| **Front** | ✔        | What the learner sees first (e.g. *Present Simple*) |
| **Back**  | ✔        | Answer side – key concept + max 3 examples          |
| *Extra X* | ✖        | Add more fields if you extend the model             |

### Example (comma‑separated, UTF‑8):

```csv
Front,Back
"Present Simple","<b>Uso clave:</b> Verdades, hábitos...<ul><li>Water boils...</li>...</ul>"
...
```

> ⚠️ **Rule of thumb:** One atomic fact per card — keeps reviews painless.

---

## 🐍 `build_deck.py` TL;DR

```python
MODEL_ID = 24092025   # MUST be unique across all your decks
DECK_ID  = 24092026
# ...
css = Path('genz_style.css').read_text()
```

Change `MODEL_ID` / `DECK_ID` if you fork multiple decks to avoid clashes in Anki.

### Add reverse cards

```python
note = genanki.Note(
    model=model,
    fields=[front, back],
    tags=["tenses"]
)
# Duplicate with fields swapped if wanted
```

### Pack extra media (e.g. TTS audio)

```python
package = genanki.Package(deck, media_files=["audio/I_brush.mp3", ...])
```

---

## 🎨 The Gen‑Z CSS

`genz_style.css` gives you a neon gradient, rounded corners & Poppins font. Copy‑paste it, or swap colors/fonts to taste.

```css
body{font-family:'Poppins',sans-serif;line-height:1.4;color:#f2f2f2;background:#0f0c29;background:linear-gradient(135deg,#24243e 0%,#302b63 50%,#0f0c29 100%);} .card{padding:24px;border-radius:18px;box-shadow:0 4px 14px rgba(0,0,0,.4);} .front{font-size:2.2rem;font-weight:600;text-align:center;} .back{font-size:1.1rem;} ul{margin-top:10px;padding-left:20px;} li{margin:4px 0;}
```

---

## 🛠️ Extending: Build New Decks in 4 Easy Steps

1. **Clone** this folder → give it a new project name.
2. **Swap** `english_verb_tenses.csv` with your own (same column headers).
3. *Optionally* tweak CSS & script IDs.
4. **Run** `python build_deck.py` → new `.apkg` pops out.

### Shortcut: Python‑generate the CSV

```python
import pandas as pd
cards = [
    {"Front":"My Term","Back":"Definition &lt;br&gt;<ul><li>Ex1...</li></ul>"},
    ...
]
pd.DataFrame(cards).to_csv('my_deck.csv',index=False)
```

---

## 🐞 Troubleshooting

| Problem                        | Likely Cause                               | Fix                                                       |
| ------------------------------ | ------------------------------------------ | --------------------------------------------------------- |
| `ModuleNotFoundError: genanki` | Forgot venv / pip install                  | Activate venv → `pip install genanki`                     |
| IDs duplicate warning in Anki  | Reused `MODEL_ID`/`DECK_ID`                | Pick new random integers (> 1e8)                          |
| CSS not applying               | Wrong path read                            | Check `genz_style.css` exists & correct case              |
| Card shows raw HTML            | Forgot `allowHTML` in card or missing tags | Ensure you import as **Basic (Front‑Back)** or equivalent |

---

## 🤔 FAQ

> **Q:** ¿Necesito audio?
> **A:** Not mandatory, but you can batch‑generate mp3 via gTTS and add them to `media_files`.

> **Q:** Can I add Cloze cards?
> **A:** Yes. Swap the model to `genanki.CLOZE_MODEL` and adjust your CSV with {{c1::word}} syntax.

---

## ✨ License & Credits

* MIT License — use freely, remix wildly.
* Built with ♥ by you (and ChatGPT‑o3).

---

Happy hacking — and may your *due* count always stay low. 🧠💪
