from spellchecker import SpellChecker
from random import shuffle
import time

spell = SpellChecker()
wordInp = input('Enter a word: ')
times = 0

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

word = shuffle_word(wordInp)
s = time.time()
while True:
    word = shuffle_word(word)
    corrected = spell.correction(word)
    if corrected != word:
        times += 1 
        print(corrected)
        if len(corrected) == len(word):
            correctedL = list(corrected)
            if all(letter in correctedL for letter in word):
                if corrected == wordInp.lower():
                    c = time.time()
                    print('Seconds:', c - s)
                    print('Times:', times)
                    print('Word Is:', word)
                    break
