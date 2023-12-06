from enum import Enum
import json
import random
PATH = "palabras.json"

class WordCategory (Enum):
    ANINFO = 1,
    FAMOSOS = 2,
    PELICULAS_Y_SERIES = 3,    
    ANIMALES = 4,
    OTROS = 5,

    def from_input(inp):
        if inp == "1":
            return WordCategory.ANINFO
        elif inp == "2":
            return WordCategory.FAMOSOS
        elif inp == "3":
            return WordCategory.PELICULAS_Y_SERIES
        elif inp == "4":
            return WordCategory.ANIMALES
        elif inp == "5":
            return WordCategory.OTROS
        else:
            return None
        
    def to_string(self):
        match self:
            case WordCategory.ANINFO:
                return "aninfo"
            case WordCategory.FAMOSOS:
                return "famosos"
            case WordCategory.PELICULAS_Y_SERIES:
                return "peliculas y series"
            case WordCategory.ANIMALES:
                return "animales"
            case WordCategory.OTROS:
                return "otros"
            
