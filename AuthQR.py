# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode

# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
#     for barcode in decode(img):
#         myData = barcode.data.decode('utf-8')
#         pts = np.array([barcode.polygon],np.int32)
#         pts = pts.reshape((-1,1,2))
#         print(myData)

#     cv2.imshow('QR Code Scanner',img)
#     cv2.waitKey(20)

import pyqrcode
import os
import cv2

os.chdir(os.path.dirname(__file__))

Uniform_Resource_Locater_or_Message = pyqrcode.create(input("\n\nEnter Any Uniform Resource Locater or Message:    "))
Uniform_Resource_Locater_or_Message.png('QR_Code.png', scale=8)
code = cv2.imread('QR_Code.png')
cv2.imshow('code', code)
cv2.waitKey(0)