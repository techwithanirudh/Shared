import cv2
import numpy as np

def Transform(mask):
    cv2.imshow('Mask', mask)
    kernel = np.ones((10, 10), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=5)
    mask = cv2.dilate(mask, kernel, iterations=8)
    return mask

def Empty(x):
    pass

def Calibration(vc):
    cv2.namedWindow('Calibrate HSV')
    cv2.createTrackbar('L_HUE', 'Calibrate HSV', 0, 179, Empty)
    cv2.createTrackbar('L_SAT', 'Calibrate HSV', 0, 255, Empty)
    cv2.createTrackbar('L_VAL', 'Calibrate HSV', 0, 255, Empty)
    cv2.createTrackbar('U_HUE', 'Calibrate HSV', 0, 179, Empty)
    cv2.createTrackbar('U_SAT', 'Calibrate HSV', 0, 255, Empty)
    cv2.createTrackbar('U_VAL', 'Calibrate HSV', 0, 255, Empty)
    cv2.setTrackbarPos('U_HUE', 'Calibrate HSV', 179)
    cv2.setTrackbarPos('U_SAT', 'Calibrate HSV', 255)
    cv2.setTrackbarPos('U_VAL', 'Calibrate HSV', 255)

    while cv2.waitKey(2) == -1:
        frame = vc.read()[1]
        frame = np.flip(frame, 1)
        cv2.imshow('Frame', frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        L_HUE = cv2.getTrackbarPos('L_HUE', 'Calibrate HSV')
        L_SAT = cv2.getTrackbarPos('L_SAT', 'Calibrate HSV')
        L_VAL = cv2.getTrackbarPos('L_VAL', 'Calibrate HSV')
        U_HUE = cv2.getTrackbarPos('U_HUE', 'Calibrate HSV')
        U_SAT = cv2.getTrackbarPos('U_SAT', 'Calibrate HSV')
        U_VAL = cv2.getTrackbarPos('U_VAL', 'Calibrate HSV')
        
        Lower = [L_HUE, L_SAT, L_VAL]
        Upper = [U_HUE, U_SAT, U_VAL]
        
        mask = cv2.inRange(hsv, np.array(Lower), np.array(Upper))
        mask = Transform(mask)

        cv2.imshow('Calibrate', mask)

    cv2.destroyAllWindows()
    return Lower, Upper