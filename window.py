#
# Copyright (c) 2023 by Kenner Hartman. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for details.
#

import time
import customtkinter as ctk

from mypackages import Config


# window

ctk.set_default_color_theme("json/themes.json")

window = ctk.CTk()
window.title('Macro Config Settings')
window.geometry('850x500')
window.resizable(False, False)
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

appearanceWidgetFrame.grid_rowconfigure((0, 1), weight=1)
appearanceWidgetFrame.grid_columnconfigure((0, 1), weight=0)
appearanceWidgetFrame.grid(column=0, sticky="nesw")
appearanceWidgetFrame.grid(row=0, rowspan=2, sticky="nesw")

appearanceOptionMenu.grid(row=2, padx=20, pady=20, sticky="s")
appearanceLabel.grid(row=2, padx=20, pady=50, sticky="sw")

# general widgets

generalWidgetsFrame = ctk.CTkFrame(window, corner_radius=0, width=300)
generalWidgetsFrame.grid_rowconfigure((0, 1), weight=1)
generalWidgetsFrame.grid_columnconfigure((0, 1), weight=0)

entery = ctk.CTkEntry(generalWidgetsFrame, width=230, placeholder_text="Change times to loop through script...")
notANumberLabel = ctk.CTkLabel(generalWidgetsFrame, text="Please enter a number!", text_color="red")
inputTooBigLabel = ctk.CTkLabel(generalWidgetsFrame, text="Needs to be less than 10!", text_color="red")
successLabel = ctk.CTkLabel(generalWidgetsFrame, text="Successfully changed!", text_color="green")

def enter(event):
    inputText = entery.get()
    settings = Config.readConfig()
    
    if(inputText.isnumeric() == True):
        inputText = int(inputText)
        if(inputText > 10):
            notANumberLabel.grid_forget()
            successLabel.grid_forget()

            inputTooBigLabel.grid(column=1, pady=15)
            inputTooBigLabel.after(3500, inputTooBigLabel.grid_forget)
        elif(inputText <= 10):
            notANumberLabel.grid_forget()
            inputTooBigLabel.grid_forget()

            settings['userPref'] = inputText
            Config.writeToConfig(settings)

            successLabel.grid(column=1, pady=15)
            successLabel.after(3500, successLabel.grid_forget)
    else:
        successLabel.grid_forget()
        inputTooBigLabel.grid_forget()

        notANumberLabel.grid(column=1, pady=15)
        notANumberLabel.after(3500, notANumberLabel.grid_forget)
        

    # delete entery and set the focus to the window, not the widget

    inputText = str(inputText)
    for i in inputText:
        entery.delete(0)

    window.focus_set()

entery.bind("<Return>", enter)

generalWidgetsFrame.grid(column=1, sticky="n")
generalWidgetsFrame.grid(row=1)

entery.grid(column=1)

# create and run window

setAppearance()

window.grid_rowconfigure((0, 1), weight=1)
window.grid_columnconfigure((0), weight=0)
window.grid_columnconfigure((1), weight=1)

window.mainloop()