#
# Copyright (c) 2023 by Kenner Hartman. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for details.
#

# import modules
import keyboard
import mouse
import time
import pygetwindow as pg

def checkIsRunning():
    global flag
    
    # figuring out a solution so I can only check for the first word when getActiveWindowTitle() is called
    # change "Minecraft* (version hidden from driver)" according to your needs for the time being
    if (pg.getActiveWindowTitle() == "Minecraft* (version hidden from driver)" or pg.getActiveWindowTitle() == "Minecraft* (version hidden from driver) - Singleplayer"):
        flag = 1
        # print("Window is active")
    else:
        flag = 0
        # print("Window is not active")
        

# emulates shift clicking inventory slots
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
        time.sleep(25/1000) # DO NOT DECREASE VALUE UNLESS YOU WANT TO BREAK YOUR CURSOR AND HAVE YOUR LIFE RUINED!!!
    
def runScript():
    if keyboard.is_pressed('left shift') and keyboard.is_pressed('b'): 
        x, y = mouse.get_position()

        for i in range(0, 3):
            clearChest(x, y)
            y += 70

    if keyboard.is_pressed('left shift') and keyboard.is_pressed('`'): 
        x, y = mouse.get_position()

        clearChest(x, y)

while True:
    checkIsRunning()
    time.sleep(1/1000)

    if keyboard.is_pressed('left shift') and keyboard.is_pressed('esc'):
        break

    while(flag == 1): 
        if keyboard.is_pressed('left shift') and keyboard.is_pressed('esc'):
            break

        checkIsRunning()
        runScript()
