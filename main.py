import json
import random
from enum import Enum
import collections

from estado_juego import EstadoJuego
from dificultad import Dificultad
from juego_ahorcado import JuegoAhorcado

def print_status(adivino: True, intentos: int, pistas: int, letras_adivinadas: list):
    if adivino:
        print("BIEN!")
    else:
        print("MAL AHI")
    print(f"Intentos restantes: {intentos}")
    print(f"Pistas restantes: {pistas}")
    print(f"Letras adivinadas: {letras_adivinadas}")
    print("Printeo el ahorcado") #4


# class Dificultad(Enum):
#     FACIL = 1,
#     NORMAL = 2,
#     DIFICIL = 3,

#     # Esta funcion va a leer del .json y devolver alguna palabra de acuerdo a la dificultad
#     def obtener_palabra(self, path):
#         with open(path, 'r') as j:
#             data = json.load(j)

#         match self:
#             case Dificultad.FACIL:
#                 return random.choice(data.get('facil'))
            
#             case Dificultad.NORMAL:
#                 return random.choice(data.get('normal'))
            
#             case Dificultad.DIFICIL:
#                 return random.choice(data.get('dificil'))

#     def obtener_intentos_maximos(self):
#         match self:
#             case Dificultad.FACIL:
#                 return 30 #hardcodeado para testing
#             case Dificultad.NORMAL:
#                 return 0
#             case Dificultad.DIFICIL:
#                 return 0
#             #actualizar esto

#     def obtener_pistas(self):
#         match self:
#             case Dificultad.FACIL:
#                 return 0
#             case Dificultad.NORMAL:
#                 return 0
#             case Dificultad.DIFICIL:
#                 return 0

#     def to_string(self):
#         match self:
#             case Dificultad.FACIL:
#                 return "FACIL"
#             case Dificultad.NORMAL:
#                 return "MEDIA"
#             case Dificultad.DIFICIL:
#                 return "DIFICIl"
            

    def print(self):
        print("Dificultad actual: ", self.to_string())


def mostrar_menu_principal():
    print("Bienvenido al juego del ahorcado")
    print("Seleccione una dificultad: ")
    print("1. Comenzar juego")
    print("2. Seleccionar dificultad\n")
        
def main():
    # mostrar_menu_principal()
    # dificultad = Dificultad(0)
    # juego = JuegoAhorcado(dificultad)

    dificultad = Dificultad(0)
    print(dificultad.cantidad_intentos)

    if input("-") == "1":
        juego.iniciar()
        if juego.estado == EstadoJuego.ABANDONADO:
            main()

main()