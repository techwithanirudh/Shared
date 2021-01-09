import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from pickle import load
from keras.applications.xception import Xception
import os
import pyttsx3

os.chdir(os.path.dirname(__file__))

img_path = './images/1.png'

def extract_features(image, model):
    image = image.resize((299,299))
    image = np.array(image)
    # for images that has 4 channels, we convert them into 3 channels
    if image.shape[2] == 4: 
        image = image[..., :3]
    image = np.expand_dims(image, axis=0)
    image = image/127.5
    image = image - 1.0
    feature = model.predict(image)
    return feature

def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def generate_desc(model, tokenizer, photo, max_length):
    in_text = 'start'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        pred = model.predict([photo,sequence], verbose=0)
        pred = np.argmax(pred)
        word = word_for_id(pred, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'end':
            break
    return in_text

max_length = 32
tokenizer = load(open("./tokenizer.p","rb"))
model = load_model('./models/model_9.h5')
xception_model = Xception(include_top=False, pooling="avg")

import cv2

cap = cv2.VideoCapture(0)

print('in')
while True:
    frameOrg = cap.read()[1]
    frame = frameOrg
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(color)
    photo = extract_features(frame, xception_model)
    description = generate_desc(model, tokenizer, photo, max_length)
    print("\n\n")
    print(description)
    text1 = ''

    for word in description.split(' '):
        conds = [word != 'start', word != 'end']
        if all(conds):
            text1 += word + ' '

    pyttsx3.speak(text1)
    cv2.imshow('Live', frameOrg)
    key = cv2.waitKey(20)
    if key == 27:
        break