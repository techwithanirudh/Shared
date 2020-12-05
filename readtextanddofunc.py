import os

os.chdir(os.path.dirname(__file__))

cmds = {'Hello': 'do hello thing', 'hi': 'do hi thing', 'sleep': 'do sleep thing'}
file = 'Text.txt'

data_html_r = open(file, 'r')
data_html_w = open(file, 'a')
data_html_r.text = data_html_r.read()
keys = list(cmds.keys())
values = list(cmds.values())

for i in range(len(cmds)):
    try:
        # print(keys[i], data_html_r.text.split('\n')[i])
        if keys[i] == data_html_r.text.split('\n')[i]:
            print(values[i])
    except IndexError:
        pass
