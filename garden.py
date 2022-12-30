import spacy
nlp = spacy.load('en_core_web_sm')
# Use some Garden Path sentences or think up your own (at least 5).Store them in a list.
sentence_list = ['I told the girl the cat scratched Bill would help her.',
        'The barge floated down the river sank.',
        'Because he always jogs a mile seems a short distance to him.',
        'The cotton clothing is made of grows in Mississippi.',
        'Ricky knew the answer to the question was yes, but wouldn\'t speak the word out loud.']
sentence_to_compare = "The old man the boat."
# Tokenise and perform Entity recognition for each of the sentences.
for sentence in sentence_list:
     #tokenisation
     print([(token.orth_) for token in nlp(sentence)])
     #identity recognisition
     print([(i, i.label_, i.label) for i in nlp(sentence).ents])
# write a comment about two unusual entities you found that spaCy gave one of the words of your sentences:
# spaCy identified:Bill as a  'PERSON', Mississippi as a location

