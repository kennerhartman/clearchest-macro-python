# Overview

<<<<<<< HEAD
Once ran, this Python script is always active unless you terminate the script or press ```Shift + ESC```.  

- When ```L CTRL + b``` is pressed, you will empty out the entire chest/shulker box.  
- When ```L CTRL + ` ```is pressed, you will empty out one line in the chest/shulker box.
- When ``` L CTRL + L SHIFT + a``` is pressed, you can change how many lines you clear from a chest/shulker.  Default times is 3.  You will need to manually activate the terminal window to type in a value.  If you enter a string, you will be prompted to press ``` L CTRL + L SHIFT + a``` again to change how many lines you clear from a chest/shulker.

    - <span style="color: lightblue">Working on a feature for the script to "remember" your input so when you close the script and later reopen it, it will still use the value you inputted</span>
=======
Once ran, this Python script is always active unless you terminate the script or press ```Shift + ESC```.  When ```Left Shift + b``` is pressed, you will empty out the entire chest/shulker box.  When ```Left Shift + ` ```is pressed, you will empty out one line in the chest/shulker box.
>>>>>>> 45b6ba310dd7c98af207e7ff6f51ce47ed68909c

I originally had this idea programmed in the LUA scripting language to work with my Logitech G-502 mouse, but I wanted to expand compatibility to my non-Logitech keyboard.

# Compatibility

This script works for the following operating system(s):

<img src="https://upload.wikimedia.org/wikipedia/commons/b/b6/Cropped-Windows10-icon.png" width=75px>

# Modules Used 

- [```mouse```](https://pypi.org/project/mouse/): receives mouse inputs, emulates mouse inputs, receives cursor position, and sets cursor position
- [```keyboard```](https://pypi.org/project/keyboard/): receives keyboard inputs and emulates keyboard inputs
- [```pygetwindow```](https://pypi.org/project/PyGetWindow/): for this script, allows the script to access Windows processes and know what Window is active

Built-in Python Libraries:

- ```time```: suspend script execution

# License

This project uses the MIT license. Please ensure you retain the license notice if you use any part of my program. For more information about the licensing of this project, please see [LICENSE.md](LICENSE.md).
