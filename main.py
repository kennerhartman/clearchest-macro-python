#
# Copyright (c) 2023 by Kenner Hartman. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for details.
#

# import modules
import keyboard
import mouse
import time
import pygetwindow as pg

time.sleep(3)

byPassNone = 0

def checkIsRunning():
    global flag
    global byPassNone

    # these next few lines of code will: 
    # 1(a): get the ActiveWindowTitle, (line 29)
    # 1(b): check if there is no window selected [if there is no window selected and I split an empty string, the script will crash] (line 31)
    # else, change 'byPassNone' to '-1' to stop the script from checking if there is no active window (line 34)
    # 2: put each word of the ActiveWindowTitle into a list, (line 36)
    # 3: store the first index of the list into a string and forget the rest (line 37)
    # 4(a): because my game has an * in its title, I made an 'if statement' to detect if there is one (line 39)
    # 4(b): find the index of the * and remove it (line 40-41)

    minecraftWindow = pg.getActiveWindowTitle()

    if(minecraftWindow is None and byPassNone != -1):
        pass
    elif(minecraftWindow): # I don't even know what is happening at this point, but it works; script will crash if it is an 'else' statement!!!
        byPassNone = -1

        minecraftWindow = minecraftWindow.split()
        minecraftWindow = minecraftWindow[0]

        if("*" in minecraftWindow):
            indexOfChar = minecraftWindow.index("*")
            minecraftWindow = minecraftWindow[:indexOfChar] + minecraftWindow[indexOfChar + 1:]
    
    # check if active window is equal to "Minecraft".  if so, 'flag' is set to '1' and the macro can run if the right keys are pressed

    if (minecraftWindow == "Minecraft"):
        flag = 1
        # print("Minecraft window is active")
    else:
        flag = 0
        # print("Minecraft window is not active")
        
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

if __name__ == "__main__":
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
