from spellchecker import SpellChecker
from random import shuffle
import time, os

# ansW = 'moon'
# dog, cat
spell = SpellChecker()
os.system('cls')
word = input('Enter a word: ')
wordInp = word
times = 0
sGen = input('Do you want to scramble it (Y/N)? ')
sGenInp = sGen

sGen, word = sGen.lower(), word.lower()

if sGen == 'y': sGen = True
if sGen == 'n': sGen = False
wordInp = word

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

if sGen:
    wordShu = shuffle_word(wordInp)

s = time.time()

while True:
    try:
        word = shuffle_word(word)
        corrected = spell.correction(word)
        if corrected != word:
            times += 1 
            print('Trying:', corrected)
            if len(corrected) == len(word):
                correctedL = list(corrected)
                if all(letter in correctedL for letter in word):
                    c = time.time()
                    print('Seconds:', c - s)
                    print('Times:', times)
                    print('Unscrambled Word Is:', corrected)
                    if sGen: print('Scrambled Word Is:', wordShu)
                    correct = input('Is this correct (Y/N)? ').lower()
                    # correct = 'n'
                    # if corrected == ansW: correct = 'y'
                    if correct == 'y': correct = True
                    if correct == 'n': correct = False
                    if correct: break
                    os.system('cls')
                    print('Enter a word:', wordInp)
                    print('Do you want to scramble it (Y/N)?', sGenInp)
    except KeyboardInterrupt:
        os.system('cls')
        print('Exiting Program...')
        break
