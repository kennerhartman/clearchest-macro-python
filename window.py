#
# Copyright (c) 2023 by Kenner Hartman. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for details.
#

import customtkinter as ctk
from mypackages import Config

# window

ctk.set_default_color_theme("themes.json")

window = ctk.CTk()
window.title('Macro Config Settings')
window.geometry('850x500')
window.resizable(0, 0)
window.iconbitmap('assets/icon.ico')

# appearance widgets

# function 'combineFunctions' is from https://www.geeksforgeeks.org/how-to-bind-multiple-commands-to-tkinter-button/; 
# this code is NOT licensed by me
def combineFunctions(*funcs):
    # this function will call the passed functions
    # with the arguments that are passed to the functions
    def inner_combined_func(*args, **kwargs):
        for f in funcs:
  
            # Calling functions with arguments, if any
            f(*args, **kwargs)
  
    # returning the reference of inner_combined_func
    # this reference will have the called result of all
    # the functions that are passed to the combined_funcs
    return inner_combined_func

def changeAppearanceEvent(new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

def rememberAppearance(new_appearance_mode):
        settings = Config.readConfig()
        
        settings['backgroundColor'] = new_appearance_mode
        Config.writeToConfig(settings)

def setAppearance():
    # overwrites "backgroundColor" in 'config.json'
    settings = Config.readConfig()
    settings = settings['backgroundColor']
    ctk.set_appearance_mode(settings)

    # changes what text is shown on the OptionMenu

    appearanceOptionMenu.set(settings) 

appearanceWidgetFrame = ctk.CTkFrame(window, corner_radius=0)

appearanceLabel = ctk.CTkLabel(appearanceWidgetFrame, text = "Appearance Mode:")

appearanceOptionMenu = ctk.CTkOptionMenu(
        appearanceWidgetFrame, 
        values=["Light", "Dark", "System"], 
        command=combineFunctions(changeAppearanceEvent, rememberAppearance)
    )

# set app appearance | grid layout

appearanceWidgetFrame.grid(column=0, sticky="nesw")
appearanceWidgetFrame.grid_rowconfigure((0, 1, 2, 3), weight=1)

appearanceLabel.grid(row=3, sticky="sw", padx=20)
appearanceOptionMenu.grid(row=4, padx=20, pady=10)

# create and run window

setAppearance()

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure((0, 1, 2), weight=0)

window.mainloop()