# START

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np
from keras.models import load_model
import random

path = 'D:/Anirudh/pythonprojects/envs/auto-py-to-exe36/rock-paper-scissors-master/'
model = load_model('rock-paper-scissors-model.h5')
cap = cv2.VideoCapture(0)
root = tk.Tk()
root.title('Rock Paper Scisscors')
lblAction = tk.Label(root) 
lblAction.config(font=('Courier', 14), text='You Guessed: none') 
lblAction.place(x=230, y=10) 
lblComputerG = tk.Label(root) 
lblComputerG.config(font=('Courier', 14), text='Computer Guessed: none') 
lblComputerG.place(x=850, y=10) 
lblWinnner = tk.Label(root) 
lblWinnner.config(font=('Courier', 14), text='Winner: none') 
lblWinnner.place(x=650, y=670) 
lmain = tk.Label(root)
lmain.place(x=-1, y=40)
pathimg = path + 'images/'

REV_CLASS_MAP = {
    0: 'rock',
    1: 'paper',
    2: 'scissors',
    3: 'none'
}

def mapper(val):
    return REV_CLASS_MAP[val]

def display_move(computer_guess):
    global diagrams, logolbl
    diagrams = tk.PhotoImage(file=pathimg + computer_guess + '.png')
    logolbl = tk.Label(root, image=diagrams, width=540)
    logolbl.place(x=700, y=50)

def detect(handimg):
    pred = model.predict(np.array([handimg]))
    move_code = np.argmax(pred[0])
    guess = mapper(move_code)
    lblAction.config(font=('Courier', 14), text='You Guessed: ' + guess) 
    lblAction.place(x=230, y=10)
    choices = ['rock', 'paper', 'scissors']
    computer_guess = random.choice(choices)
    display_move(computer_guess)
    lblComputerG.config(font=('Courier', 14), text='Computer Guessed: ' + computer_guess) 
    lblComputerG.place(x=850, y=10) 
    guess_dict = {'rock': 0, 'paper': 1, 'scissors': 2}
    guess_idx = guess_dict.get(guess, 3)
    computer_idx = guess_dict.get(computer_guess)
    result_matrix = [[0,2,1],
    				 [1,0,2],
    				 [2,1,0],
    				 [3,3,3]]
    result_idx = result_matrix[guess_idx][computer_idx]
    result_messages = ['Tie', 'You', 'Computer', 'Invalid Guess']
    result = result_messages[result_idx]
    lblWinnner.config(font=('Courier', 14), text='Winner: ' + result) 
    lblWinnner.place(x=650, y=670) 

def show_frame():
    global handimg, key
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    roi = frame[100:500, 100:500]
    handimg = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    handimg = cv2.resize(handimg, (227, 227))
    if key == 'c':
        key = ''
        detect(handimg)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def key_pressed(event):
    global key
    key = event.char

key = ''
root.bind('<Key>', key_pressed)
root.geometry('1600x900')
show_frame()
root.mainloop()

# END