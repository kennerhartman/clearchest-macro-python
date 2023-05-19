# import modules

import keyboard
import mouse
import time
    
def shiftClick():
    keyboard.press('left shift')
    mouse.click("left")
    keyboard.release('left shift')
    mouse.release('left')

def clearChest(x, y):
    for i in range(0, 10):
        shiftClick()
        mouse.move(x, y)
        x += 72
        time.sleep(25/1000) # DO NOT DECREASE VALUE UNLESS YOU WANT TO BREAK YOUR CURSOR!!!
    
while True:
    if keyboard.is_pressed('left ctrl') and keyboard.is_pressed('b'): 
        x, y = mouse.get_position()

        for i in range(0, 3):
            clearChest(x, y)
            y += 70

    if keyboard.is_pressed('left ctrl') and keyboard.is_pressed('`'): 
        x, y = mouse.get_position()

        clearChest(x, y)

    if keyboard.is_pressed('left shift') and keyboard.is_pressed('esc'):
        break
    