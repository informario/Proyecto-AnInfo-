from dificultad import Dificultad
from estado_juego import EstadoJuego
import random
import os
import getpass

class JuegoAhorcado:

    def __init__(self, dificultad):
        self.intentos_restantes = dificultad.obtener_intentos_maximos()
        self.pistas_restantes = dificultad.obtener_pistas()
        self.palabra, self.pista = dificultad.obtener_palabra()
        self.mostrar_pista = False
        self.letras_por_adivinar = list(set(filter(lambda x: x != " ", self.palabra)))
        self.letras_adivinadas = []
        self.letras_erradas = []
        
        self.estado = EstadoJuego.EN_CURSO
    
    def en_curso(self):
        return self.estado == EstadoJuego.EN_CURSO
    
    def mostrar_palabra(self):
        print("    ")
        
        if self.en_curso():
            for letra in self.palabra:
                if letra in self.letras_adivinadas:
                    print(letra, end=" ")
                elif letra == " ":
                    print(" ", end=" ")
                else:
                    print("_", end=" ")

        else:
            for letra in self.palabra:
                print(letra, end=" ")
    
    def mostrar_estado(self):
        os.system('clear')
        print("=========================================")
        print("Intentos restantes: ", self.intentos_restantes)
        print("Letras adivinadas: ", self.letras_adivinadas)
        print("Letras erradas: ", self.letras_erradas)
        print("Pistas restantes: ", self.pistas_restantes)
        if self.mostrar_pista:
            print("AYUDA: ", self.pista)

        self.mostrar_palabra()
        print("\n")
        self.estado.print()
        print("=========================================")

        if not self.en_curso():
            print("Presione ENTER para volver al menu principal")
            getpass.getpass(prompt="")

    def intentar_adivinar_letra(self, letra):

        if letra.isspace():
            return

        if letra in self.letras_por_adivinar:
            self.letras_por_adivinar.remove(letra)
            self.letras_adivinadas.append(letra)
            
        else:
            self.intentos_restantes -= 1
            self.letras_erradas.append(letra)
            
        if len(self.letras_por_adivinar) == 0:
            self.estado = EstadoJuego.GANADO
        if self.intentos_restantes == 0:
            self.estado = EstadoJuego.PERDIDO
    
    def intentar_adivinar_palabra(self, palabra):

        if palabra.isspace():
            return
        
        if palabra == self.palabra:
            self.estado = EstadoJuego.GANADO
            self.letras_adivinadas += self.letras_por_adivinar
        else:
            self.intentos_restantes -= 1

        if self.intentos_restantes == 0:
            self.estado = EstadoJuego.PERDIDO


    def revelar_letra(self):
        if self.pistas_restantes == 0:
            print("\nNo te quedan pistas!\n")
            return
        
        if len(self.letras_por_adivinar) <= 1:
            print("\nTe queda solo una letra, no podes usar la pista!\n")
            return

        pista = random.choice(self.letras_por_adivinar)
        self.letras_por_adivinar.remove(pista)
        self.letras_adivinadas.append(pista)

        self.pistas_restantes -= 1

    def dar_pista(self):
        if self.pistas_restantes < 2:
            print("\nNo te quedan suficientes pistas para que te demos una ayuda!\n")
            return

        if self.mostrar_pista:
            print("\nYa te dimos una pista!\n")
            return

        self.mostrar_pista = True
        self.pistas_restantes -= 2

    # Devuelve el estado final del juego
    def iniciar(self):
        os.system('clear')
        print("Bienvenido al juego del Ahorcado!")
        self.mostrar_estado()
        while self.en_curso():
            print(f"Letras erradas: {self.letras_erradas}")
            print("0. Abandonar partida")
            print("1. Revelar una letra")
            print("2. Pedir una pista")
            print("Ingrese una letra para continuar jugando\n")
            char = input("Intento: ")
            if char == "0":
                print("¿Estas seguro de que deseas abandonar la partida?")
                print("0. Si")
                print("1. No")
                char = input("-")
                if char == "0":
                    return
                else:
                    continue
            if char == "1":
                self.revelar_letra()
                self.mostrar_estado()
                continue
            if char == "2":
                self.dar_pista()
                self.mostrar_estado()
                continue
            if len(char) > 1:
                self.intentar_adivinar_palabra(char)
            else:
                self.intentar_adivinar_letra(char)
            self.mostrar_estado()
        
        return self.estado