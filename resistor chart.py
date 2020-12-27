import os
import cv2

os.chdir(os.path.dirname(__file__))

img = cv2.imread('resistor chart.png')
cv2.imshow('chart', img)
cv2.waitKey(0)

b1 = input('1st Band: ')
b2 = input('2nd Band: ')
b3 = input('3rd Band: ')

def exp(bas, expN):
    N = 1000000007 
    if (expN == 0): 
        return 1; 
    if (expN == 1): 
        return bas % N
      
    t = exp(bas, int(expN / 2))
    t = (t * t) % N

    if (expN % 2 == 0): 
        return t
    else: 
        return ((bas % N) * t) % N

expS = ''
expL = list(str(exp(10, int(b3))))

for num in range(1, len(expL)):
    expS += expL[num]

print(f'{int(b1 + b2)}{expS}')
