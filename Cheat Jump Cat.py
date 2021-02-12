import pyautogui, time
 
pyautogui.keyDown('space')
time.sleep(0.5) 
pyautogui.keyUp('space')
time.sleep(3.3)
points = 10

# Get Up To 64 Score If You Want Unlimited Scores replace for i in range(30) with while True:
for i in range(int(points / 2 - 2)): 
    pyautogui.keyDown('space')
    time.sleep(0.5) 
    pyautogui.keyUp('space')
    time.sleep(1.3) 
