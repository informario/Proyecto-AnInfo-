from enum import Enum
import json
import random
PATH = "palabras.json"

class WordCategory (Enum):
    ANINFO = 1,
    OTRA = 2,
    FAMOSOS = 3,    

    def from_input(inp):
        if inp == "1":
            return WordCategory.ANINFO
        elif inp == "2":
            return WordCategory.OTRA
        elif inp == "3":
            return WordCategory.FAMOSOS
        else:
            return None
        
    def to_string(self):
        match self:
            case WordCategory.ANINFO:
                return "aninfo"
            case WordCategory.OTRA:
                return "otra"
            case WordCategory.FAMOSOS:
                return "famosos"
