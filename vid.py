import cv2 
import moviepy.editor as mp
import pygame
import os

pygame.init()
os.chdir(os.path.dirname(__file__))

filename = 'D:/Anirudh/pythonprojects/sampleproject1/VIDEOS/cup.mp4'
cap = cv2.VideoCapture(filename) 
video = mp.VideoFileClip(filename)
audio = video.audio
try:
    filenameL = len(filename.split('/'))
    fname = filename.split('/')[filenameL - 1].split('.')[0] + '.mp3'
    audio.write_audiofile(fname)
except IndexError:
    fname = filename.split('.')[0] + '.mp3'
    audio.write_audiofile(fname)

pygame.mixer.music.load(os.path.dirname(__file__) + '/' + fname)
pygame.mixer.music.play()
wait = False
while True: 
    if not wait:
        running, frame = cap.read()
        if not running:
            break 
        cv2.imshow('Frame', frame) 
        cv2.waitKey(20)

cap.release() 
cv2.destroyAllWindows() 