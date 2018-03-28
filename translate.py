import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en')

# https://spacy.io/usage/linguistic-features
doc = nlp(u'I will take you to him')

for token in doc:
    print(token, token.pos_)
