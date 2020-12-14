import cv2 

image = cv2.imread('D:/Anirudh/pythonprojects/sampleproject1/testAtoZ.jpg') 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200) 
contours, hierarchy = cv2.findContours(edged, 
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
cv2.imshow('Canny Edges After Contouring', edged) 
print("Number of Contours found = " + str(len(contours))) 
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
for contour in contours:
    x, y, h, w = cv2.boundingRect(contour)
    crop = image.copy()
    crop = crop[y:y+h, x:x+w]
    cv2.imshow('cont1', crop)
    cv2.waitKey(0)
    print(x, ',', y, ',', h, ',', w)
cv2.imshow('Contours', image) 
cv2.waitKey(0) 
