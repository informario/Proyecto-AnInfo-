
from enum import Enum
import collections

class EstadoJuego(Enum):
    EN_CURSO = 1,
    GANADO = 2,
    PERDIDO = 3,
    ABANDONADO = 4,
    
    def print(self):
        match self:
            case EstadoJuego.EN_CURSO:
                print("Juego en curso")
            case EstadoJuego.GANADO:
                print("Felicitaciones, ganaste")
            case EstadoJuego.PERDIDO:
                print("Perdiste")
            case EstadoJuego.ABANDONADO:
                print("Abandonaste el juego")

class Dificultad(Enum):
    FACIL = 1,
    NORMAL = 2,
    DIFICIL = 3,

    # Esta funcion va a leer del .json y devolver alguna palabra de acuerdo a la dificultad
    def obtener_palabra(self):
        match self:
            case Dificultad.FACIL:
                return "casa"
            case Dificultad.NORMAL:
                return "perro"
            case Dificultad.DIFICIL:
                return "murcielago"

    def obtener_intentos_maximos(self):
        match self:
            case Dificultad.FACIL:
                return 0
            case Dificultad.NORMAL:
                return 0
            case Dificultad.DIFICIL:
                return 0
            #actualizar esto

    def obtener_pistas(self):
        match self:
            case Dificultad.FACIL:
                return 0
            case Dificultad.NORMAL:
                return 0
            case Dificultad.DIFICIL:
                return 0

    def to_string(self):
        match self:
            case Dificultad.FACIL:
                return "FACIL"
            case Dificultad.NORMAL:
                return "MEDIA"
            case Dificultad.DIFICIL:
                return "DIFICIl"
            

    def print(self):
        print("Dificultad actual: ", self.to_string())

class JuegoAhorcado:
    def __init__(self, dificultad):
        self.dificultad = dificultad
        self.palabra = dificultad.obtener_palabra()
        self.intentos_restantes = dificultad.obtener_intentos_maximos()
        self.pistas = dificultad.obtener_pistas()
        self.letras_por_adivinar = list(set(self.palabra))
        self.letras_adivinadas = []
        self.letras_erroneas = []
        self.estado = EstadoJuego.EN_CURSO
    
    def en_curso(self):
        return self.estado == EstadoJuego.EN_CURSO
    
    def mostrar_palabra(self):
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
    
    def mostrar_estado(self):
        print("=========================================")
        print("Intentos restantes: x")
        print("Letras adivinadas: x")
        print("Letras erradas: x")
        print("Pistas restantes: x")

        self.dificultad.print()
        self.mostrar_palabra()
        self.estado.print()
        print("=========================================")

    def intentar_adivinar_letra(self, letra):
        if letra in self.letras_por_adivinar:
            self.letras_por_adivinar.remove(letra)
            self.letras_adivinadas.append(letra)
            
        else:
            self.letras_erroneas.append(letra)
            self.intentos_restantes -= 1

        if len(self.letras_por_adivinar) == 0:
            self.estado = EstadoJuego.GANADO
        if self.intentos_restantes == 0:
            self.estado = EstadoJuego.PERDIDO

    def obtener_pista(self):
        if self.pistas == 0:
            return
        # Logica para obtener una pista

    def abandonar(self):
        self.estado = EstadoJuego.ABANDONADO

    # Devuelve el estado final del juego
    def iniciar(self):
        self.mostrar_estado()
        while self.en_curso():
            print("0. Abandonar partida")
            print("1. Pedir pista")
            print("Ingrese una letra para continuar jugando\n")
            char = input("Intento: ")
            if char == "0":
                self.abandonar()
                return
            if char == "1":
                self.obtener_pista()
                continue
            #self.intentar_adivinar_letra(char)
            self.mostrar_estado()
        
        return self.estado

def mostrar_menu_principal():
    print("Bienvenido al juego del ahorcado")
    print("Seleccione una dificultad: ")
    print("1. Comenzar juego")
    print("2. Seleccionar dificultad\n")
        
def main():
    mostrar_menu_principal()
    juego = JuegoAhorcado(Dificultad.FACIL)
    if input("-") == "1":
        juego.iniciar()
        if juego.estado == EstadoJuego.ABANDONADO:
            main()

main()