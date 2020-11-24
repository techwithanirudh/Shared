import cv2
import numpy as np
from calibration import Calibration, Transform
import os

os.chdir(os.path.dirname(__file__))

vc = cv2.VideoCapture(0)

# Step 1: Capture background image
print('Press any key once suitable background has been obtained: ')
while cv2.waitKey(2) == -1:
	frame = vc.read()[1]
	frame = cv2.flip(frame, 1)
	frame = cv2.resize(frame, (1280, 720))
	cv2.imshow('Background', frame)
cv2.imwrite('background.png', frame)
cv2.destroyAllWindows()
print('\n\n\t\tBackground Image has been saved successfully !!!')

# Step 2: HSV Color Range for Cloak
input('Press Enter to start Calibration: ')
Lower, Upper = Calibration(vc)
print(f'HSV VALUES\n\nL_HUE: {Lower[0]}\nL_SAT: {Lower[1]}\nL_VAL: {Lower[2]}\nU_HUE: {Upper[0]}\nU_SAT: {Upper[1]}\nU_VAL: {Upper[2]}\n')

# Step 3: Real time application
input('Press enter to start Magic :) ')
background = cv2.imread('background.png')
while cv2.waitKey(1) == -1:
	return_value, frame = vc.read()
	frame = cv2.flip(frame, 1)
	frame = cv2.resize(frame, (1280, 720))
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, np.array(Lower), np.array(Upper))
	mask = Transform(mask)
	frame = np.array(frame)
	temp = cv2.bitwise_and(background, background,mask=mask)
	mask = cv2.bitwise_not(mask)
	frame = cv2.bitwise_and(frame, frame, mask=mask)
	frame = cv2.add(frame, temp)
	cv2.imshow('Cloak', frame)

vc.release()
cv2.destroyAllWindows()