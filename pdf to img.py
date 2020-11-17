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

# imgs = []
# imgsL = 38
# for ind in range(imgsL):
#     imgs.append('files/' + str(ind + 1) + '.jpg')

# imagesL = []
# varImgs = ''
# cnt = 0
# path = 'D:/Anirudh/pythonprojects/sampleproject1'
# for img in imgs:
#     cnt += 1
#     imagesL.append('img' + str(cnt))
#     varImgs += f'{imagesL[cnt - 1]}, '

# varImgs += '= '

# for ind in range(imgsL):
#     if ind != imgsL - 1:
#         varImgs += f'cv2.imread(\'{path}/{imgs[ind]}\'), '
#     else:
#         varImgs += f'cv2.imread(\'{path}/{imgs[ind]}\')'

# imagesL = str(imagesL).replace('\'', '')

# exec(f'''
# import cv2
# {varImgs}
# def vconcat_resize(img_list, interpolation  
#                    = cv2.INTER_CUBIC): 
#     w_min = min(img.shape[1]  
#                 for img in img_list) 

#     im_list_resize = [cv2.resize(img, 
#                       (w_min, int(img.shape[0] * w_min / img.shape[1])), 
#                                  interpolation = interpolation) 
#                       for img in img_list] 
#     return cv2.vconcat(im_list_resize)
# img_v_resize = vconcat_resize({imagesL})
# cv2.imwrite('{path}/data/sea.png', img_v_resize)
# ''')