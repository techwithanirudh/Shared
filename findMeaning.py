# import re
# import requests
# from bs4 import BeautifulSoup

# def get_bs4_obj(url, parser='html.parser'):
#     return BeautifulSoup(requests.get(url).text, parser)

# def getMeaning(word):
#     try:
#         html = get_bs4_obj('http://wordnetweb.princeton.edu/perl/webwn?s={0}'.format(word))
#         types = html.findAll('h3')
#         lists = html.findAll('ul')
#         out = {}
#         for a in types:
#             reg = str(lists[types.index(a)])
#             meanings = []
#             for x in re.findall(r'\((.*?)\)', reg):
#                 if 'often followed by' in x:
#                     pass
#                 elif len(x) > 5 or ' ' in str(x):
#                     meanings.append(x)
#             name = a.text
#             out[name] = meanings
#         return out
#     except Exception as e:
#         print('Error: The Following Error occured: {}'.format(e))

# def printMeaning(word):
#     meaning = getMeaning(word)
#     meaningK = list(meaning.keys())
#     meaningV = list(meaning.values())
#     for num in range(len(meaningK)):
#         meaningStr = ''
#         for num1 in range(len(meaningV[num])):
#             meaningStr += '\n' + str(num1 + 1) + '. ' + meaningV[num][num1].capitalize()
#         print('As a', meaningK[num], 'The Word', word, 'Is Usassly Defind as', meaningStr, '\n')

# word = input('Enter a word: ')
# printMeaning(word)


# new

from spellchecker import SpellChecker
import os
import random

os.chdir(os.path.dirname(__file__))

def loadDictionary():
    spell = SpellChecker()
    return list(spell.word_frequency.dictionary.keys())

def genrateWord():
    pass

genrateWord()

# import spacy

# nlp = spacy.load("en_core_web_sm")

# doc1 = nlp('an apparatus with rotating blades that creates a current of air for cooling or ventilation:')
# doc2 = nlp('a blade that blows air')

# confidence = doc1.similarity(doc2)

# def truncate(n, decimals=0):
#     multiplier = 10 ** decimals
#     return int(n * multiplier) / multiplier

# confidence = truncate(confidence, 1)
# confidence = int(str(confidence).split('0.')[1])
# print(confidence)

# if confidence > 4:
#     print('yeah')
# else:
#     print('nope')
