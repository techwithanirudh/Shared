# Shared
# My Projects
# YoutubeVideoDownloader Is Password Protected


code watermark Concat.py

import moviepy.editor as mp
import os

os.chdir(os.path.dirname(__file__))

clips = ['test.mp4', 'test1.mp4']
clipsL = []
ind = 0
for clip in clips:
    clipsL.append(mp.VideoFileClip(clips[ind]))
    ind += 1

mp.concatenate_videoclips(clipsL)
