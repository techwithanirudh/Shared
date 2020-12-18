import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
color_lower = np.array([22, 93, 0])
color_upper = np.array([45, 255, 255])
prev_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, color_lower, color_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 300: 
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if prev_y - y > 10:
                pyautogui.press('down')
                # print('moving down')
            prev_y = y
            # print(area)
            # cv2.drawContours(frame, c, -1, (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    key = cv2.waitKey(20)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
