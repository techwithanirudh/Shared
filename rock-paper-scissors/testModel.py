import os
from keras.models import load_model
import cv2
import numpy as np

filepath = 'D:/Anirudh/pythonprojects/envs/auto-py-to-exe36/rock-paper-scissors-master/modelTest'

REV_CLASS_MAP = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}

def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("rock-paper-scissors-model.h5")
Images = []
Answer = []
good = 0
bad = 0
for val in range(8):
    Images.append('rock' + str(val + 1) + '.jpg') 
    Answer.append('rock')
for val in range(8):
    Images.append('paper' + str(val + 1) + '.jpg') 
    Answer.append('paper')
for val in range(8):
    Images.append('scissors' + str(val + 1) + '.jpg') 
    Answer.append('scissors')
for val in range(24):
    img = cv2.imread(filepath + '/' + Images[val])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (227, 227))
    pred = model.predict(np.array([img]))
    move_code = np.argmax(pred[0])
    move_name = mapper(move_code)
    if move_name == Answer[val]:
        good += 1
    else:
        bad += 1
bad += 1
acc = good / bad
bad -= 1
os.system('cls')
print('good:', good)
print('bad:', bad)
success = False
if good > 18:
    success = True
print('acc:', acc)
print('pass:', success)