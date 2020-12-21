from spellchecker import SpellChecker
from random import shuffle

spell = SpellChecker()
wordInp = input('Enter a word: ')
times = 0

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

word = shuffle_word(wordInp)
while True:
    word = shuffle_word(word)
    corrected = spell.correction(word)
    if corrected != word:
        times += 1 
        print(corrected)
        if len(corrected) == len(word):
            correctedL = list(corrected)
            if all(letter in correctedL for letter in word):
                if corrected == wordInp:
                    print('Times: ', times)
                    print('Word Is:', word)
                    break
