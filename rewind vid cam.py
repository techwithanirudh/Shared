# ffmpeg -i YouTube_TMP_SND.mp3 -vf reverse -af areverse YouTube_TMP_SND_Reversed.mp3
import time
import cv2
import os
from moviepy.editor import VideoFileClip
# import pygame
# from pygame import mixer

# pygame.init()
os.chdir(os.path.dirname(__file__))

path = './VIDEOS/YouTube.mp4'
# aud = VideoFileClip(path)
# aud = aud.audio
# lenPath = len(path.split('/')) - 1  
# pathAud = path.split('/')[lenPath].replace('.mp4', '')
# pathAud = pathAud + '_TMP_SND.mp3'
# aud.write_audiofile(pathAud)
cap = cv2.VideoCapture(path)
counter = 0
check = True
frame_list = []

# mixer.music.load(pathAud)
# mixer.music.play()

while check:
    check, vid = cap.read()
    frame_list.append(vid)
    counter += 1

frame_list.pop()
frame_list.reverse()
fps = cap.get(cv2.CAP_PROP_FPS)
time_delta = 1.0 / fps
second = 283

for frame in frame_list:
    cv2.imshow("Frame" , frame_list[int(fps * second)])
    time.sleep(time_delta)
    if cv2.waitKey(25) and 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()