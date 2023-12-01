from dificultad import Dificultad
from estado_juego import EstadoJuego
from options.game_options import OpcionJuego
import random
import os
import getpass

class JuegoAhorcado:

    def __init__(self, dificultad):
        self.intentos_restantes = dificultad.obtener_intentos_maximos()
        self.pistas_restantes = dificultad.obtener_pistas()
        self.palabra, self.pista = dificultad.obtener_palabra()
        self.pista_utilizada = False
        self.letras_por_adivinar = list(set(filter(lambda x: x != " ", self.palabra)))
        self.letras_adivinadas = []
        self.letras_erradas = []
        self.estado = EstadoJuego.EN_CURSO
    
    def en_curso(self):
        return self.estado == EstadoJuego.EN_CURSO
    
    def mostrar_palabra(self):
        if self.en_curso():
            for letra in self.palabra:
                if letra in self.letras_adivinadas:
                    print(letra, end=" ")
                elif letra == " ":
                    print(" ", end=" ")
                else:
                    print("_", end=" ")

            return
        
        for letra in self.palabra:
            print(letra, end=" ")
    
    def mostrar_estado(self):
        
        print("=========================================")
        print("Intentos restantes: ", self.intentos_restantes)
        print("Letras adivinadas: ", self.letras_adivinadas)
        print("Letras erradas: ", self.letras_erradas)
        print("Pistas restantes: ", self.pistas_restantes)
        if self.pista_utilizada:
            print("AYUDA: ", self.pista)

        self.mostrar_palabra()
        print("\n")
        self.estado.print()
        print("=========================================")


    def intentar_adivinar_letra(self, letra):
        if letra in self.letras_adivinadas:
            print("\nYa adivinaste esta letra, vuelve a intentarlo\n")
            return
        
        if letra in self.letras_por_adivinar:
            print("\nAdivinaste una letra!\n")   
            self.letras_por_adivinar.remove(letra)
            self.letras_adivinadas.append(letra)
            
        else:
            print("\nLetra incorrecta, vuelve a intentarlo\n")
            self.intentos_restantes -= 1
            self.letras_erradas.append(letra)

        if len(self.letras_por_adivinar) == 0:
            self.estado = EstadoJuego.GANADO
        if self.intentos_restantes == 0:
            self.estado = EstadoJuego.PERDIDO
    
    def intentar_adivinar_palabra(self, palabra):
        
        if palabra == self.palabra:
            print("\nAdivinaste la palabra!\n")
            self.estado = EstadoJuego.GANADO
            self.letras_adivinadas += self.letras_por_adivinar
        else:
            print("\nPalabra incorrecta\n")
            self.intentos_restantes -= 1

        if self.intentos_restantes == 0:
            self.estado = EstadoJuego.PERDIDO


    def dar_pista(self):
        if self.pistas_restantes == 0:
            print("\nNo te quedan pistas!\n")
            return
        
        if len(self.letras_por_adivinar) <= 1:
            print("\nTe queda solo una letra, no podes usar la pista!\n")
            return
    
        print("\nPista obtenida\n") 
        pista = random.choice(self.letras_por_adivinar)
        self.letras_por_adivinar.remove(pista)
        self.letras_adivinadas.append(pista)

        self.pistas_restantes -= 1

    def dar_ayuda(self):
        if self.pistas_restantes < 2:
            print("\nNo te quedan suficientes pistas para que te demos una ayuda!\n")
            return

        if self.pista_utilizada:
            print("\nYa te dimos una pista!\n")
            return

        print("\nAyuda obtenida\n")
        self.pista_utilizada = True
        self.pistas_restantes -= 2

    def partida_abandonada():
        print("¿Estas seguro de que deseas abandonar la partida?")
        print("0. Si")
        print("1. No\n")
        inp = input("- ")
        if inp == "1":
            return False
        
        return True
        
    def mostrar_opciones():
        print("0. Abandonar partida")
        print("1. Revelar una letra")
        print("2. Pedir una pista")
        print("Ingrese una letra para continuar jugando\n")

    def terminar_partida():
        print("\nPresione ENTER para volver al menu principal\n")
        getpass.getpass(prompt="")


    def intentar_adivinar(self, inp):
        if len(inp) > 1:
            self.intentar_adivinar_palabra(inp)
            return
        self.intentar_adivinar_letra(inp) 

    def input_invalido(inp):
        return len(inp) == 0    
        # Más adelante seguramente hagamos otras validaciones, por eso la funcion
        # como por ejemplo que no se pueda ingresar un numero distinto de 0, 1 o 2 


    def jugar_partida(self):
        while self.en_curso():
            JuegoAhorcado.mostrar_opciones()
            inp = input("Intento: ").lower().strip()
            os.system('clear')
            if JuegoAhorcado.input_invalido(inp):
                print("\nEl caracter ingresado no es válido, vuelve a intentarlo\n")
                continue

            opcion = OpcionJuego.from_input(inp)
            if opcion == None:
                self.intentar_adivinar(inp) 
                self.mostrar_estado()
                continue

            if opcion == OpcionJuego.ABANDONAR_PARTIDA:
                if JuegoAhorcado.partida_abandonada():
                    return
                
            opcion.ejecutar(self)            
            self.mostrar_estado()
        
        JuegoAhorcado.terminar_partida()

    # Devuelve el estado final del juego
    def iniciar(self):
        os.system('clear')
        print("\nBienvenido al juego del Ahorcado!\n")                                                                        
        self.mostrar_estado()
        self.jugar_partida()
        
        


