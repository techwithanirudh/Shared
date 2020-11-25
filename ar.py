import cv2
import os
import numpy as np

os.chdir(os.path.dirname(__file__))

# cap = cv2.VideoCapture(0)
imgTarget = cv2.imread('tiger.png')
myVid = cv2.VideoCapture('cup.mp4')
detection = True
frameCounter = 0
# success, imgVideo = myVid.read()
hT, wT, cT = imgTarget.shape
imgAR = cv2.imread('paper.png')
# imgVideo = cv2.resize(imgVideo, (wT, hT))
imgAR = cv2.resize(imgAR, (hT, wT))
orb = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(imgTarget, None)
# imgTarget = cv2.drawKeypoints(imgTarget, kp1, None)

while True:
    # success, imgWebcam = cap.read()
    imgWebcam = cv2.imread('tiger1.png')
    imgAug = imgWebcam.copy()
    kp2, des2 = orb.detectAndCompute(imgWebcam, None)
    # imgWebcam = cv2.drawKeypoints(imgWebcam, kp2, None)

    if frameCounter == myVid.get(cv2.CAP_PROP_FRAME_COUNT):
        myVid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0
    imgVideo = myVid.read()[1]
    imgVideo = cv2.resize(imgVideo, (wT, hT))

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    # print(len(good))
    imgFeatures = cv2.drawMatches(imgTarget, kp1, imgWebcam, kp2, good, None, flags=2)
    if len(good) > 20:
        detection = True
        srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        matrix, mask = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5)
        pts = np.float32([[0, 0], [0, hT], [wT, hT], [wT, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, matrix)
        img2 = imgWebcam.copy()
        cv2.polylines(img2, [np.int32(dst)], True, (255, 0, 255), 3)# img2 = cv2.polylines(imgWebcam, [np.int32(dst)], True, (255, 0, 255), 3)
        # imgAR for img or imgVideo for video
        imgWarp = cv2.warpPerspective(imgVideo, matrix, (imgWebcam.shape[1], imgWebcam.shape[0]))
        maskNew = np.zeros((imgWebcam.shape[0], imgWebcam.shape[1]), np.uint8)
        cv2.fillPoly(maskNew, [np.int32(dst)], (255, 255, 255))
        maskInv = cv2.bitwise_not(maskNew)
        imgAug = cv2.bitwise_and(imgAug, imgAug, mask=maskInv)
        imgAug = cv2.bitwise_or(imgWarp, imgAug)

    cv2.imshow('maskNew', imgAug)
    # cv2.imshow('imgWarp', imgWarp)
    # cv2.imshow('img2', img2)
    # cv2.imshow('imgFeatures', imgFeatures)
    # cv2.imshow('imgTarget', imgTarget)
    # cv2.imshow('myVid', imgVideo)
    cv2.imshow('Webcam', imgWebcam)
    frameCounter += 1
    cv2.waitKey(1)