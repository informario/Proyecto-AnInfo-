from enum import Enum
import random
import json

PATH = "palabras.json"
OPCION_FACIL = "1"
OPCION_NORMAL = "2"
OPCION_DIFICIL = "3"

class Dificultad(Enum):
    FACIL = 1
    NORMAL = 2
    DIFICIL = 3

    # Esta funcion va a leer del .json y devolver un diccionario con la palabra y su pista de acuerdo a la dificultad
    def obtener_palabra(self):
        with open(PATH, 'r') as j:
            data = json.load(j)

        match self:
            case Dificultad.FACIL:
                return list(random.choice(data.get('facil')).items())[0]
            
            case Dificultad.NORMAL:
                return list(random.choice(data.get('normal')).items())[0]
            
            case Dificultad.DIFICIL:
                return list(random.choice(data.get('dificil')).items())[0]

    def obtener_intentos_maximos(self):
        match self:
            case Dificultad.FACIL:
                return 7 
            case Dificultad.NORMAL:
                return 5
            case Dificultad.DIFICIL:
                return 3

    def obtener_pistas(self):
        match self:
            case Dificultad.FACIL:
                return 5
            case Dificultad.NORMAL:
                return 3
            case Dificultad.DIFICIL:
                return 2

    def to_string(self):
        match self:
            case Dificultad.FACIL:
                return "FACIL"
            case Dificultad.NORMAL:
                return "NORMAL"
            case Dificultad.DIFICIL:
                return "DIFICIL"
                

    
    def from_input(inp):
        if inp == OPCION_FACIL:
            return Dificultad.FACIL
        elif inp == OPCION_NORMAL:
            return Dificultad.NORMAL
        elif inp == OPCION_DIFICIL:
            return Dificultad.DIFICIL
        else:
            return None
    

