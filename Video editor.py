import moviepy.editor as mp
import os

os.chdir(os.path.dirname(__file__))

filename = './input/rock.mp4'
sec1, sec2 = 5, 8 

myVideo = mp.VideoFileClip(filename)
myVideoEdited = myVideo.subclip(sec1, sec2)
myVideoEdited.write_videofile('test.mp4', codec='libx264', remove_temp=False)