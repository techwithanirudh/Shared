import cv2
import os

os.chdir(os.path.dirname(__file__))

thresh = 200

if (thresh % 2) == 0:
    thresh += 1

thresh = 9001
print(thresh)

def capture_image():
    cap = cv2.VideoCapture(0)

    while True:
        frame = cap.read()[1]
        cv2.imshow('BookPage', frame)
        key = cv2.waitKey(20)
        if key == ord('s'):
            cv2.imwrite('bookpage.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows() 

def main():
    img = cv2.imread('bookpage.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, result = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
    adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, thresh, 4)

    cv2.imshow('Image', img)
    cv2.imshow('Result', result)
    cv2.imshow('Adaptive Result', adaptive)

    cv2.waitKey(0)
    cv2.destroyAllWindows() 

# capture_image()
main()
