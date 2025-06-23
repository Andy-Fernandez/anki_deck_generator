# build_deck.py
import genanki, csv, pathlib

BASE = pathlib.Path(__file__).parent
MODEL_ID = 24092025
DECK_ID  = 24092026

model = genanki.Model(
    MODEL_ID,
    'Gen-Z Tenses Model',
    fields=[{'name': 'Front'}, {'name': 'Back'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div class="front">{{Front}}</div>',
        'afmt': '{{FrontSide}}<hr id=answer><div class="back">{{Back}}</div>',
    }],
    css=(BASE / 'genz_style.css').read_text(encoding='utf-8'),
)

deck = genanki.Deck(DECK_ID, 'Verb Tenses — Gen-Z')

with open(BASE / 'english_verb_tenses.csv', encoding='utf-8') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        deck.add_note(genanki.Note(model=model, fields=[row['Front'], row['Back']]))

out = BASE / 'Verb_Tenses_GenZ.apkg'
genanki.Package(deck).write_to_file(out)
print(f'Deck compilado → {out}')
