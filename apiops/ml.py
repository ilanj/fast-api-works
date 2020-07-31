import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple buys UK startup for 1 billion $")

for ent in doc.ents:
    print(ent.label_, ent.text, ent.label)