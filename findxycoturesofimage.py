import cv2 

# Let's load a simple image with 3 black squares 
image = cv2.imread('D:/Anirudh/pythonprojects/sampleproject1/data/Images/5/scratch1.png') 
# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Find Canny edges 
edged = cv2.Canny(gray, 30, 200) 

# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv2.findContours(edged, 
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

cv2.imshow('Canny Edges After Contouring', edged) 
print("Number of Contours found = " + str(len(contours))) 

# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
for contour in contours:
    x, y, _, _ = cv2.boundingRect(contour)
    print(x, y)
cv2.imshow('Contours', image) 
cv2.waitKey(0) 

