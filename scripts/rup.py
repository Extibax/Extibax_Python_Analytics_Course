#  Script: Remove Useless Packages
# Modules
from colorama import Fore, Back, Style
import pandas as pd
import json


class Rup:
    with open("package.json") as json_file:
        data_frame = json.load(json_file)
        print(json.dumps(data_frame["dependencies"], sort_keys=True, indent=True))


exports = Rup()
