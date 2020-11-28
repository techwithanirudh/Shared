import os

os.chdir(os.path.dirname(__file__))

# from imutils import paths
# import numpy as np
# import cv2

# args = {'watermark': 'pyimagesearch_watermark.png', 'input': './input', 'output': './output'}
# watermark = cv2.imread(args['watermark'], cv2.IMREAD_UNCHANGED)
# (wH, wW) = watermark.shape[:2]

# for imagePath in paths.list_images(args['input']):
# 	image = cv2.imread(imagePath)
# 	(h, w) = image.shape[:2]
# 	image = np.dstack([image, np.ones((h, w), dtype='uint8') * 255])
# 	overlay = np.zeros((h, w, 4), dtype='uint8')
# 	overlay[h - wH - 10:h - 10, w - wW - 10:w - 10] = watermark
# 	output = image.copy()
# 	filename = imagePath[imagePath.rfind(os.path.sep) + 1:]
# 	p = os.path.sep.join((args['output'], filename))
# 	cv2.imwrite(p, output)

from imutils import paths
import moviepy.editor as mp

args = {'watermark': 'watermark.png', 'input': './input', 'output': './output'}
for imagePath in paths.list_files(args['input']):
	video = mp.VideoFileClip(imagePath)
	logo = (mp.ImageClip(args['watermark']).set_duration(video.duration).set_pos(('right', 'bottom')))
	final = mp.CompositeVideoClip([video, logo])
	filename = imagePath[imagePath.rfind(os.path.sep) + 1:]
	p = os.path.sep.join((args['output'], filename))
	final.write_videofile(p, remove_temp=False)