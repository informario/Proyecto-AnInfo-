from enum import Enum
import random
import json

PATH = "palabras.json"

class Dificultad(Enum):
    FACIL = 0,
    NORMAL = 1,
    DIFICIL = 2,

    def __init__(self):

        if (self == self.FACIL):
            self.cantidad_intentos = 7
            self.cantidad_pistas = 5
            self.palabras = self.get_palabra()
        elif (self == self.NORMAL):
            self.cantidad_intentos = 5
            self.cantidad_pistas = 3
            self.palabras = self.get_palabra()
        else:
            self.cantidad_intentos = 3
            self.cantidad_pistas = 1
            self.palabras = self.get_palabra()
        
    def decrementar_intentos(self):
        if (self.cantidad_intentos > 0):
            self.cantidad_intentos -= 1

    def decrementar_pistas(self):
        if (self.cantidad_pistas > 0):
            self.cantidad_pistas -= 1

    def quedan_intentos(self):
        return (self.cantidad_intentos > 0)
    
    def quedan_pistas(self):
        return (self.cantidad_pistas > 0)

    def get_intentos(self):
        return self.cantidad_intentos
    
    def get_pistas(self):
        return self.cantidad_pistas
    
    def get_palabra(self):
        
        with open(PATH, 'r') as j:
            data = json.load(j)

        match self:
            case Dificultad.FACIL:
                return random.choice(data.get('facil'))
            
            case Dificultad.NORMAL:
                return random.choice(data.get('normal'))
            
            case Dificultad.DIFICIL:
                return random.choice(data.get('dificil'))
            
        return self.palabras
