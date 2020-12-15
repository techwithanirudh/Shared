import cv2 

pointsList = []
def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        # if size != 0 and size % 4 != 0:
            # cv2.line(image, tuple(pointsList[round((size-1)/4)*4]),(x,y),(0,0,255),2)
        cv2.circle(image,(x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])

image = cv2.imread('D:/Anirudh/pythonprojects/sampleproject1/testAtoZFine.jpg') 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200) 
contours, hierarchy = cv2.findContours(edged, 
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
cv2.imshow('Canny Edges After Contouring', edged) 
print("Number of Contours found = " + str(len(contours))) 
per = 4
while True:
# cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
    if len(pointsList) % per == 0 and len(pointsList) != 0:
        per += 4
        print(pointsList)
    cv2.setMouseCallback('Contours', mousePoints)    
    cv2.imshow('Contours', image) 
    cv2.waitKey(20) 
# for contour in contours:
#     x, y, h, w = cv2.boundingRect(contour)
#     crop = image.copy()
#     crop = crop[y:y+h + h, x:x+w + w]
#     cv2.imshow('cont1', crop)
#     cv2.waitKey(0)
#     print(x, ',', y, ',', h, ',', w)
