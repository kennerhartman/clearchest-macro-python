#
# Copyright (c) 2023 by Kenner Hartman. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for details.
#

# import modules
import keyboard
import mouse
import time
import subprocess

from mypackages import Config
from mypackages import ActiveWindow

# config file related code

data = {"userPref": 3, "CLI": True, "backgroundColor": "System"}
Config.createConfig(data)
settings = Config.readConfig()

# main part of the script

# default times to loop through 'clearChest()' is 3; 
# will change to whatever is in the 'config.json' 'userPref'
timesToLoop = 3

def changeY(): 
    global timesToLoop

    if(settings['CLI'] == True):
        try:
            timesToLoop = int(input('How many lines in the chest/shulker do you want to clear (Default: 3, unless changed): '))
        except:
            print("\nYou entered a string, not a number! Please try again using 'L Ctrl + L Shift + a'\n")
        
        if(timesToLoop > 10 or timesToLoop < 0):
            print("\nPlease enter a number less than or equal to 10!\n")
        else:
            settings['userPref'] = timesToLoop
            Config.writeToConfig(settings)

    elif(settings['CLI'] == False):
        subprocess.call("window.py", shell=True)

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
    print("The script is currently running.  Press 'Left Shift + ESC' to exit the script.\n")

    while True:  
        time.sleep(1/1000)

        ActiveWindow.checkActiveWindow("Discord")

        if keyboard.is_pressed('left shift') and keyboard.is_pressed('esc'):
            break

        # shortcut to change how many lines in a chest/shulker you clear
        # this code is here so it works even if you are outside of MinecraftB
        if keyboard.is_pressed('left control') and keyboard.is_pressed('left shift') and keyboard.is_pressed('a'): 
                changeY()

        while(ActiveWindow.checkActiveWindow("Minecraft")): 
            # shortcut to change how many lines in a chest/shulker you clear; 
            # will not work in Minecraft if this is not here

            if keyboard.is_pressed('left control') and keyboard.is_pressed('left shift') and keyboard.is_pressed('a'): 
                changeY()

            # this line of code needs to be here to exit the script while the Minecraft window is active
            if keyboard.is_pressed('left shift') and keyboard.is_pressed('esc'):
                break

            runScript()