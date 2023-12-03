from getpass import getpass
import os
from juego_ahorcado import HangmanGame
from estado_juego import GameState
from dificultad import Difficulty
from enum import Enum

from options.menu_options import MenuOption

OPTION_RETURN_TO_MAIN_MENU = "0"
INITIAL_DIFFICULTY = Difficulty.MEDIUM

class MenuGame:
    def __init__(self):
        self.difficulty = INITIAL_DIFFICULTY
    
    def show_options():
        os.system('clear')
        print("Opciones:")
        print("\t1 - Empezar a jugar")
        print("\t2 - Seleccionar dificultad")
        print("\t3 - Reglas")
        print("\t4 - Salir")

    def execute_options(self):
        """
        Muestra el menu principal del juego del Ahorcado y maneja las opciones seleccionadas por el usuario.

        El bucle se ejecuta continuamente hasta que el usuario elige salir.

        Entrada:
        - Elige una opción ingresando el número correspondiente.

        Salida:
        - Mensajes de la opcion elegida.
        """    
        while True:
            MenuGame.show_options()
            options = input("Elige una opcion: ").strip()
            options = MenuOption.from_input(options)
            if options == None:
                print("Opcion incorrecta")
                continue
            options.ejecutar(self)
            if options == MenuOption.EXIT:
                break
    
    def show_rules(self):
        os.system('clear')
        print("Reglas:")
        print("1. El juego consiste en adivinar una palabra o frase oculta")
        print("2. El jugador puede ingresar una letra o una palabra para intentar adivinar")
        print("3. Si la letra ingresada se encuentra en la palabra oculta, esta se revelará y pasará a ser conocida")
        print("4. Si la letra ingresada no se encuentra en la palabra oculta, el jugador pierde un intento")
        print("5. El juego termina cuando el jugador adivina la palabra oculta o se queda sin intentos")
        print("6. El jugador puede pedir pistas para obtener información sobre la palabra oculta")
        print("7. Existen dos tipos de pistas: se puede revelar una letra de la palabra (que gasta una pista), o se puede pedir una definición de la palabra oculta (que gasta dos pistas)")
        print("8. El juego tiene tres niveles de dificultad: FACIL, NORMAL y DIFICIL, al elegir estos cambian las dificultades de las palabras, y cada uno tiene una cantidad de intentos y pistas diferente")
        print("9. El jugador puede cambiar la dificultad del juego en cualquier momento")
        print("10. El jugador puede abandonar la partida en cualquier momento")
        print("\nPresione ENTER para volver al menu principal\n")
        getpass(prompt="")

    def select_difficulty(self):
        os.system('clear')
        print("Selecciona una dificultad:")
        print("1. FACIL: 7 intentos, 5 pistas y palabras cortas")
        print("2. NORMAL: 5 intentos, 3 pistas y palabras o frases normales")
        print("3. DIFICIL: 3 intentos, 2 pistas y palabras o frases largas")
        print("0. Volver al menu principal")
        print("Dificultad actual: ", self.difficulty.to_string())
        print("\n")
        option = input("-").strip()
        difficulty = Difficulty.from_input(option)
        while difficulty == None:
            if option == OPTION_RETURN_TO_MAIN_MENU:
                return
            print("Opcion incorrecta, vuelve a intentarlo")
            option = input("-").strip()
            difficulty = Difficulty.from_input(option)

        self.difficulty = difficulty
        print("Dificultad seleccionada: ", self.difficulty.to_string())
        
    def start_to_play(self):
        game = HangmanGame(self.difficulty)
        game.run()

