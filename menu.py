from getpass import getpass
import os
from game import HangmanGame
from game_state import GameState
from difficulty import Difficulty
from enum import Enum

from options.menu import MenuOption
from user_statistics import UserStatistics

OPTION_RETURN_TO_MAIN_MENU = "0"
INITIAL_DIFFICULTY = Difficulty.MEDIUM

class GameMenu:
    def __init__(self):
        self.difficulty = INITIAL_DIFFICULTY
        self.user_statistics = UserStatistics()
    
    def show_options(self):
        os.system('clear')
        print("Opciones:")
        print("\t1 - Empezar a jugar")
        print("\t2 - Seleccionar dificultad")
        print("\t3 - Reglas")
        print("\t4 - Salir")
        print("\tDificultad actual: ", self.difficulty.to_string())    
        print("\tPuntaje actual: ", self.user_statistics.score) 
        

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
            self.show_options()
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
        print("\t1. El juego consiste en adivinar una palabra o frase oculta")
        print("\t2. El jugador puede ingresar una letra o una palabra para intentar adivinar")
        print("\t3. Si la letra ingresada se encuentra en la palabra oculta, esta se revelará y pasará a ser conocida")
        print("\t4. Si la letra ingresada no se encuentra en la palabra oculta, el jugador pierde un intento")
        print("\t5. El juego termina cuando el jugador adivina la palabra oculta o se queda sin intentos")
        print("\t6. El jugador puede pedir pistas para obtener información sobre la palabra oculta")
        print("\t7. Existen dos tipos de pistas: se puede revelar una letra de la palabra (que gasta una pista), o se puede pedir una definición de la palabra oculta (que gasta dos pistas)")
        print("\t8. El juego tiene tres niveles de dificultad: FACIL, NORMAL y DIFICIL, al elegir estos cambian las dificultades de las palabras, y cada uno tiene una cantidad de intentos y pistas diferente")
        print("\t9. El jugador puede cambiar la dificultad del juego en cualquier momento")
        print("\t10. El jugador puede abandonar la partida en cualquier momento")
        print("\nPresione ENTER para volver al menu principal\n")
        getpass(prompt="")

    def select_difficulty(self):
        os.system('clear')
        print("Selecciona una dificultad:")
        print("\t1. FACIL: 7 intentos, 5 pistas y palabras cortas")
        print("\t2. NORMAL: 5 intentos, 3 pistas y palabras o frases normales")
        print("\t3. DIFICIL: 3 intentos, 2 pistas y palabras o frases largas")
        print("Dificultad actual: ", self.difficulty.to_string())
        print("\nPresiona ENTER para volver al menu principal\n")
        option = input("- ").strip()
        difficulty = Difficulty.from_input(option)
        while difficulty == None:
            if len(option) == 0:
                return 
            if option == OPTION_RETURN_TO_MAIN_MENU:
                return
            print("Opcion incorrecta, vuelve a intentarlo")
            option = input("- ").strip()
            difficulty = Difficulty.from_input(option)

        self.difficulty = difficulty
        print("Dificultad seleccionada: ", self.difficulty.to_string())
        
    def start_to_play(self):
        game = HangmanGame(self.difficulty)
        game.run()
        if game.is_won():
            self.user_statistics.increase_score(self.difficulty)




    