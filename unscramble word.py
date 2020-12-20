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
    corrected = spell.correction(word)
    if corrected != word:
        if len(corrected) == len(word):
            correctedL = list(corrected)
            if all(letter in correctedL for letter in word):
                print(corrected)
                print('Word Is:', spell.correction(word))
                break
