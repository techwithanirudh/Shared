from keras.models import load_model
import cv2
import numpy as np
import random
import os

REV_CLASS_MAP = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}

def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("rock-paper-scissors-model.h5")
os.system('cls')
cap = cv2.VideoCapture(0)

while True:
    frame = cap.read()[1]
    cv2.imshow('Live', frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (227, 227))
    pred = model.predict(np.array([frame]))
    move_code = np.argmax(pred[0])
    guess = mapper(move_code)
    key = cv2.waitKey(20)
    if key == 27: # esc key
        break
    if key == ord('c'):
        os.system('cls')
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

cap.release()
cv2.destroyAllWindows()