import os
from PIL import Image

os.chdir(os.path.dirname(__file__))

fileFormat = '.png'
w, h = 32, 32
imgNames = os.listdir('.')
imgs = []
for imgName in imgNames:
    if imgName.endswith(fileFormat):
        imgs.append(imgName)
ind = 0
for img in imgs:
    img = os.path.dirname(__file__) + '/' + img
    print('Resizing:', img)
    image = Image.open(img)
    image = image.resize((w, h), Image.ANTIALIAS)
    image.save(f'{img}')