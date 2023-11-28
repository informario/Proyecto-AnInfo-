from enum import Enum
import random
import json

PATH = "palabras.json"

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
        match inp:
            case "1":
                return Dificultad.FACIL
            case "2":
                return Dificultad.NORMAL
            case "3":
                return Dificultad.DIFICIL
            case _:
                return None

