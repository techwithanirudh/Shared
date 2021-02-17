import screen_brightness_control as sbc 
import keyboard, time

change = 70

while True: 
    if keyboard.is_pressed('b'): 
        change = 100
        sbc.fade_brightness(change)
    if keyboard.is_pressed('d'): 
        change = 30
        sbc.fade_brightness(change)
    time.sleep(0.05)
