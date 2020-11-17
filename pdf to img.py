from pdf2image import convert_from_path 
import os
from PIL import Image

os.chdir(os.path.dirname(__file__))

images = convert_from_path('*.pdf', poppler_path='/poppler-20.11.0/bin') 
num = 1
for img in images: 
    img.save(f'data\{num}.jpg', 'JPEG')
    num += 1



# list_im = []
# for ind in range(38):
#     list_im.append('files/' + str(ind + 1) + '.jpg')

# images = [Image.open(x) for x in list_im]
# widths, heights = zip(*(i.size for i in images))

# total_width = sum(widths)
# max_height = max(heights)

# new_im = Image.new('RGB', (total_width, max_height))

# x_offset = 0
# for im in images:
#   new_im.paste(im, (x_offset,0))
#   x_offset += im.size[0]

# new_im.save('data/test.jpg')


# file_name = 'data/image-1-compressed.jpg'
# picture = Image.open('data/test.jpg')
# dim = picture.size
# print(f"This is the current width and height of the image: {dim}")
# picture.save(file_name, optimize=True, quality=1) 