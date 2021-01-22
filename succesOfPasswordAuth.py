text = '''Anirudh--{}--pwd: A1Aajsjys\nAnirudhjajs--{}--pwd: A1Aajsjys\nAnirudhjajs--{}--pwd: A1Aajsjys'''
peda = 1
num = len(text.split('--{}--')) - 1 
text = text.split('\n')

for i in range(num):
    try:
        out = text[i].split('--{}--pwd: ')[0]
        print(out)
    except IndexError:
        print('IndexError: ', i, text)
    # print(text, i)
    # print('a:', text)
