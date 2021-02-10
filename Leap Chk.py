year = int(input('Enter a year: ')) # 2021
leap = False
year = year / 4
year = int(str(year).split('.')[1])
if not year: leap = True
print('Leap: ', leap) # False
