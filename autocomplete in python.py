# pip install autocomplete
import autocomplete

text = input('Type: ')
spaces = len(text.split(' ')) - 2
words = [text.split(' ')[spaces], text.split(' ')[spaces + 1]]
autocomplete.load()
print(autocomplete.predict(words[0], words[1]))