#
# Copyright (c) 2023 by Kenner Hartman. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for details.
#

import os
import json

class Config:

    # when called, if a 'config.json' file is not present, then one will be created, 
    # with object(s) passed in as a parameter (named data)
    def createConfig(data):
        filename = "json/config.json"
        isFile = os.path.isfile(filename)

        if(not isFile):
            with open(filename, 'w') as f:
                json.dump(data, f, indent = 4)
            print("\nA 'config.json' file has been created. By default, this script will clear 3 lines from the inventory of a chest/shulker.\n"
                "To change this, press 'L CTRL + L SHIFT + a' at the same time.\n")

    # read 'config.json'
    def readConfig():
        with open('json/config.json', 'r') as f:
            settings = json.load(f)
        f.close()

        return settings

    # write/override object data in 'config.json'
    def writeToConfig(settings):
        with open('json/config.json', 'w') as f:
            json.dump(settings, f, indent = 4)
        f.close()