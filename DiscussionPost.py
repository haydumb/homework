import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Process a sentence using the model
sentence = "This is an introduction to spaCy"
doc = nlp(sentence)

# Print the word and its corresponding POS tag
for token in doc:
    print(token.text, token.pos_)
