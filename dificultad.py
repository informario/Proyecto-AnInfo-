from enum import Enum
import random
import json

class Dificultad(Enum):
    FACIL = 0,
    NORMAL = 1,
    DIFICIL = 2,

    def __init__(self, palabras, cantidad_intentos, cantidad_pistas):
        self.palabras = palabras
        self.cantidad_intentos = cantidad_intentos
        self.cantidad_pistas = cantidad_pistas

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
    
    def get_palabra(self, path):
        
        with open(path, 'r') as j:
            data = json.load(j)

        match self:
            case Dificultad.FACIL:
                return random.choice(data.get('facil'))
            
            case Dificultad.NORMAL:
                return random.choice(data.get('normal'))
            
            case Dificultad.DIFICIL:
                return random.choice(data.get('dificil'))
        return self.palabras
