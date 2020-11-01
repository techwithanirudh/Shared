import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np
from keras.models import load_model
import random
import os

os.chdir(os.path.dirname(__file__))

model = load_model('rock-paper-scissors-model.h5')
cap = cv2.VideoCapture(0)
root = tk.Tk()
root.title('Rock Paper Scisscors')
lmain = tk.Label(root)
lmain.pack()

REV_CLASS_MAP = {
    0: 'rock',
    1: 'paper',
    2: 'scissors',
    3: 'none'
}

def mapper(val):
    return REV_CLASS_MAP[val]

def key(key):
    global keyx
    keyx = key

def detect(handimg):
    pred = model.predict(np.array([handimg]))
    move_code = np.argmax(pred[0])
    guess = mapper(move_code)
    print('\nYou guessed', guess)
    choices = ['rock', 'paper', 'scissors']
    computer_guess = random.choice(choices)
    print('\nComputer guessed', computer_guess)
    guess_dict = {'rock': 0, 'paper': 1, 'scissors': 2}
    guess_idx = guess_dict.get(guess, 3)
    computer_idx = guess_dict.get(computer_guess)
    result_matrix = [[0,2,1],
    				 [1,0,2],
    				 [2,1,0],
    				 [3,3,3]]
    result_idx = result_matrix[guess_idx][computer_idx]
    result_messages = ['\nIt is a tie!', '\nYou win!', '\nComputer wins!', '\nError: Invalid Guess']
    result = result_messages[result_idx]
    print(result)

def show_frame():
    global handimg, keyx
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    roi = frame[100:500, 100:500]
    handimg = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    handimg = cv2.resize(handimg, (227, 227))
    if keyx == 'c':
        keyx = ''
        detect(handimg)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def key_pressed(event):
    key(event.char)

keyx = ''
root.bind('<Key>', key_pressed)
show_frame()
root.mainloop()