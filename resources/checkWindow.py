import pygetwindow as gw

byPassTypeNone = 0

class ActiveWindow:
    # get active window, change variable 'flag' found in main.py
    def checkActiveWindow():
        global byPassTypeNone

        # these next few lines of code will: 
        # 1(a): get the ActiveWindowTitle, (line 19)
        # 1(b): check if there is no window selected [if there is no window selected and I split an empty string, the script will crash] (line 21)
        # else, change 'byPassTypeNone' to '-1' to stop the script from checking if there is no active window (line 24)
        # 2: put each word of the ActiveWindowTitle into a list, (line 26)
        # 3: store the first index of the list into a string and forget the rest (line 27)
        # 4(a): because my game has an * in its title, I made an 'if statement' to detect if there is one in the list (line 29)
        # 4(b): find the index of the * and remove it (line 30-31)

        minecraftWindow = gw.getActiveWindowTitle()

        if(minecraftWindow is None and byPassTypeNone != -1):
            pass
        elif(minecraftWindow): # I don't even know what is happening at this point, but it works; script will crash if it is an 'else' statement!!!
            byPassTypeNone = -1

            minecraftWindow = minecraftWindow.split()
            minecraftWindow = minecraftWindow[0]

            if("*" in minecraftWindow):
                indexOfChar = minecraftWindow.index("*")
                minecraftWindow = minecraftWindow[:indexOfChar] + minecraftWindow[indexOfChar + 1:]
        
        # check if active window is equal to "Minecraft".  if so, return '1' and 
        # the macro in 'main.py' can run if the right keys are pressed

        if (minecraftWindow == "Minecraft"):
            return 1
            # print("Minecraft window is active")
        else:
            return 0
            # print("Minecraft window is not active")