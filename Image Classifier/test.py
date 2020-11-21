import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, models
import os
from tkinter import filedialog

os.chdir(os.path.dirname(__file__))

openWin = filedialog.Tk()
openWin.withdraw()
imgname = filedialog.askopenfilename(filetypes=[('PNG', '*.png')])
if not imgname.endswith('.png'):
    imgname = imgname + '.png'
(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
training_images, testing_images = training_images / 255, testing_images / 255
class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
training_images = training_images[:20000]
training_labels = training_labels[:20000]
testing_images = testing_images[:4000]
testing_labels = testing_labels[:4000]
model = models.load_model('image_classifier.model')
if imgname != '':
    img = cv.imread(imgname)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img, cmap=plt.cm.binary)
    predection = model.predict(np.array([img]) / 255)
    index = np.argmax(predection)
    plt.xlabel(class_names[index], fontdict={'Courier New': 24})
    plt.show()
    print(f'Prediction Is: {class_names[index]}')