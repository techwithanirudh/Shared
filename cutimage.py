#!/usr/local/bin/python3
import numpy as np
from PIL import Image, ImageDraw

# Open the input image as numpy array, convert to RGB
img=Image.open("D:/Anirudh/pythonprojects/sampleproject1/data/Images/5/scratch4.png").convert("RGB")
npImage=np.array(img)
h, w=img.size

# Create same size alpha layer with circle
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([9, 16, h - 8, w - 8],0,360,fill=255)

# Convert alpha Image to numpy array
npAlpha=np.array(alpha)

# Add alpha layer to RGB
npImage=np.dstack((npImage,npAlpha))

# Save with alpha
Image.fromarray(npImage).save('D:/Anirudh/pythonprojects/sampleproject1/data/Images/5/scratch1dup.png')
