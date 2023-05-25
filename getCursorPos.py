#
# Copyright (c) 2023 by Kenner Hartman. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for details.
#

import keyboard
import mouse

if __name__ == "__main__":
    print("\nThis is not the main script; run 'python main.py' in the root directory of this project. \n")

    print("If you are figuring out the (x, y) coordinates of your cursor position, use 'L Shift +  L Click' to do so; "
          "(x, y) will be printed to the console ('L Shift + ESC' to exit script):")
    
    flag = 0

    while (flag == 0):
        if keyboard.is_pressed('left shift') and keyboard.is_pressed('esc'):
            break
        
        if keyboard.is_pressed('left shift') and mouse.is_pressed('left'):
            print("(x, y): " + str(mouse.get_position()) + "\n")
            break