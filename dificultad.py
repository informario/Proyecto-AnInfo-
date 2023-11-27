from enum import Enum
import random
import json

PATH = "palabras.json"

class Dificultad(Enum):
    FACIL = 1
    NORMAL = 2
    DIFICIL = 3

    # Esta funcion va a leer del .json y devolver alguna palabra de acuerdo a la dificultad
    def obtener_palabra(self):
        with open(PATH, 'r') as j:
            data = json.load(j)

        match self:
            case Dificultad.FACIL:
                return random.choice(data.get('facil'))
            
            case Dificultad.NORMAL:
                return random.choice(data.get('normal'))
            
            case Dificultad.DIFICIL:
                return random.choice(data.get('dificil'))

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
                return 1

    def to_string(self):
        match self:
            case Dificultad.FACIL:
                return "FACIL"
            case Dificultad.NORMAL:
                return "NORMAL"
            case Dificultad.DIFICIL:
                return "DIFICIL"
                

    def from_index(index):
        match index:
            case Dificultad.FACIL.value:
                return Dificultad.FACIL
            case Dificultad.NORMAL.value:
                return Dificultad.NORMAL
            case Dificultad.DIFICIL.value:
                return Dificultad.DIFICIL
            case _:
                return None
