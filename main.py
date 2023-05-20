#
# Copyright (c) 2023 by Kenner Hartman. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for details.
#

# import modules
import keyboard
import mouse
import time
import pygetwindow as gw

byPassNone = 0
timesToLoop = int(3)

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

    minecraftWindow = gw.getActiveWindowTitle()

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

def changeY(): 
    global timesToLoop
    
    try:
        timesToLoop = int(input('How many lines in the chest/shulker do you want to clear (Default: 3): '))
    except:
        print("\nYou entered a string, not a number! Please try again using 'L Ctrl + L Shift + a'\n")

    if keyboard.is_pressed('left shift') and keyboard.is_pressed('esc'):
        exit()

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

        for i in range(0, timesToLoop):
            clearChest(x, y)
            y += 70

    if keyboard.is_pressed('left shift') and keyboard.is_pressed('`'): 
        x, y = mouse.get_position()

        clearChest(x, y)

if __name__ == "__main__":
    print("The script is currently running.  Press 'Left Shift + ESC' to exit the script.")

    while True:
        checkIsRunning()
        time.sleep(1/1000)

        if keyboard.is_pressed('left shift') and keyboard.is_pressed('esc'):
            break

        # shortcut to change how many lines in a chest/shulker you clear
        # this code is here so it works even if you are outside of Minecraft
        if keyboard.is_pressed('left control') and keyboard.is_pressed('left shift') and keyboard.is_pressed('a'): 
                changeY()

        while(flag == 1): 
            # shortcut to change how many lines in a chest/shulker you clear; 
            # will not work in Minecraft if this is not here
            if keyboard.is_pressed('left control') and keyboard.is_pressed('left shift') and keyboard.is_pressed('a'): 
                changeY()

            # this line of code needs to be here to exit the script while the Minecraft window is active
            if keyboard.is_pressed('left shift') and keyboard.is_pressed('esc'):
                break

            checkIsRunning()
            runScript()