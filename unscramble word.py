from spellchecker import SpellChecker
from random import shuffle

spell = SpellChecker()
word = input('Enter a word: ')

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

while True:
    word = shuffle_word(word)
    if spell.correction(word) != word:
        print('Word Is:', spell.correction(word))
        break
