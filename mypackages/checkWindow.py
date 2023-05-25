#
# Copyright (c) 2023 by Kenner Hartman. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for details.
#

import pygetwindow as gw
import re

byPassTypeNone = 0

class ActiveWindow:
    # get active window, change variable 'flag' found in main.py
    def checkActiveWindow(title):

        global byPassTypeNone

        # these next few lines of code will: 

        # 1(a): get the ActiveWindowTitle, 
        # 1(b): check if there is no window selected [if there is no window selected and I split an empty string, the script will crash] 
        # else, change 'byPassTypeNone' to '-1' to stop the script from checking if there is no active window 
        # 2: put each word of the ActiveWindowTitle into a list, 
        # 3: store the first index of the list into a string and forget the rest 
        # 4(a): because my game has an * in its title, I made an 'if statement' to detect if there is one in the list 
        # 4(b): find the index of the * and remove it 

        windowTitle = gw.getActiveWindowTitle()

        if(windowTitle is None and byPassTypeNone != -1):
            pass
        elif(windowTitle): # I don't even know what is happening at this point, but it works; script will crash if it is an 'else' statement!!!
            byPassTypeNone = -1

            # search name of ActiveWindow
            if(re.search(title, windowTitle)):
                windowTitle = re.findall(title, windowTitle)[0]

                if("*" in windowTitle):
                    indexOfChar = windowTitle.index("*")
                    windowTitle = windowTitle[:indexOfChar] + windowTitle[indexOfChar + 1:]

                # if ActiveWindow is "Minecraft"
                if(windowTitle == "Minecraft"):
                    return "Minecraft"
                
                # if I need to check for any Windows besides "Minecraft", manually append the following code:
                    # if(windowTitle == "[window name]"):
                        # return [value]
                
