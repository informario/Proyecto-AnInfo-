from dificultad import Dificultad
from estado_juego import EstadoJuego
import random
import os

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
        for letra in self.palabra:
            if letra in self.letras_adivinadas or self.estado == EstadoJuego.PERDIDO:
                print(letra, end=" ")
            elif letra == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
        
    
    def mostrar_estado(self):
        
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

    def intentar_adivinar_letra(self, letra):
        if len(letra) == 0:
            print("\nEl caracter ingresado no es válido, vuelve a intentarlo\n")
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
        
        if palabra == self.palabra:
            self.estado = EstadoJuego.GANADO
            self.letras_adivinadas += self.letras_por_adivinar
        else:
            print("\nPalabra incorrecta\n")
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
            print("0. Abandonar partida")
            print("1. Revelar una letra")
            print("2. Pedir una pista")
            print("Ingrese una letra para continuar jugando\n")

            char = input("Intento: ").lower().strip()   
            # Esto convierte el input a minusculas y elimina los espacios en blanco
            # del principio y del final. Si le pasamos un string con unicamente un espacio en blanco,
            # lo va a dejar vacío
            os.system('clear')

            
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
        
        inp = input("Presione ENTER para continuar\n")
        while inp != "":
            inp = input("")
            continue
        return self.estado