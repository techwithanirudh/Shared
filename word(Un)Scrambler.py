from spellchecker import SpellChecker
from random import shuffle
import time

spell = SpellChecker()
word = input('Enter a word: ')
times = 0
sGen = input('Do you want to scramble it? (Y/N)')

if sGen == 'y': sGen = True
if sGen == 'n': sGen = False

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

if sGen:
    word = word
    wordShu = shuffle_word(word)
s = time.time()

while True:
    word = shuffle_word(word)
    corrected = spell.correction(word)
    if corrected != word:
        times += 1 
        print('Trying: ', corrected)
        if len(corrected) == len(word):
            correctedL = list(corrected)
            if all(letter in correctedL for letter in word):
                c = time.time()
                print('Seconds:', c - s)
                print('Times:', times)
                if not sGen:
                    print('Word Is:', corrected)
                if sGen:
                    print('Scrambled Word Is:', wordShu)
                break