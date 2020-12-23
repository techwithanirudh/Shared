# from spellchecker import SpellChecker
# import os

# os.chdir(os.path.dirname(__file__))

# def createDictionary():
#     spell = SpellChecker()
#     open('dictionary.txt', 'a')
#     with open('dictionary.txt', 'w') as dictionary:
#         dictionary.write(str(spell.word_frequency.dictionary.keys()))

# createDictionary()

import spacy

nlp = spacy.load("en_core_web_sm")

doc1 = nlp('an apparatus with rotating blades that creates a current of air for cooling or ventilation:')
doc2 = nlp('a blade that blows air')

confidence = doc1.similarity(doc2)

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

confidence = truncate(confidence, 1)
confidence = int(str(confidence).split('0.')[1])
print(confidence)

if confidence > 4:
    print('yeah')
else:
    print('nope')
