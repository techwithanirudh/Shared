# from PIL import Image

# colour = [255, 255, 255]
# img = Image.open('D:/Anirudh/pythonprojects/sampleproject1/data/Images/5/scratch1.png')
# img = img.convert('RGBA')
# datas = img.getdata()
# newData = []
# for item in datas:
#     if item[0] == colour[0] and item[1] == colour[1] and item[2] == colour[2]:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# img.putdata(newData)
# img.save('D:/Anirudh/pythonprojects/sampleproject1/data/Images/5/scratch1rem.png')

path = 'D:/Anirudh/pythonprojects/sampleproject1/data/Images/8/'

from PIL import Image
import os

os.chdir(path)

pngFiles = []
fmat = '.png'
colour = [255, 255, 255]
files = os.listdir(path)
for file in files:
    if file.endswith(fmat):
        pngFiles.append(file)
print(pngFiles)
for file in pngFiles:
    img = Image.open(file)
    img = img.convert('RGBA')
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == colour[0] and item[1] == colour[1] and item[2] == colour[2]:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(file)
