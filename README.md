# Overview

Once ran, this Python script is always active unless you terminate the script or press ```Shift + ESC```.  When ```L CTRL + b``` is pressed, you will empty out the entire chest/shulker box.  When ```L CTRL + ` ```is pressed, you will empty out one line in the chest/shulker box.

I originally had this idea programmed in the LUA scripting language to work with my Logitech G-502 mouse, but I wanted to expand compatibility to my non-Logitech keyboard.

# Modules Used 

- ```mouse```: receives mouse inputs, emulates mouse inputs, receives cursor position, and sets cursor position
- ```keyboard```: receives keyboard inputs and emulates keyboard inputs

Built-in Python Libraries:

- ```time```: suspend script execution

# License

This project uses the MIT license. Please ensure you retain the license notice if you use any part of my program. For more information about the licensing of this project, please see [LICENSE.md](LICENSE.md).