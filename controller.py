from getpass import getpass
import os
from game import HangmanGame
from state import GameState
from difficulty import Difficulty
from enum import Enum

from options.menu import MenuOption
from user_statistics import UserStatistics

RETURN_TO_MAIN_MENU_OPT = ""
INITIAL_DIFFICULTY = Difficulty.MEDIUM

class GameController:
    def __init__(self):
        self.user_statistics = UserStatistics()
        self.difficulty = INITIAL_DIFFICULTY

    def run(self):
        while True:
            option = self.request_menu_option()
            option.execute(self)
            if option == MenuOption.EXIT:
                break

    def update_difficulty(self):
        dificulty = GameController.request_difficulty()
        if dificulty != None:
            self.difficulty = dificulty

    def play_game(self):
        game = HangmanGame(self.difficulty)
        game.run()
        game.update_score(self.user_statistics, self.difficulty)

    def request_menu_option(self):
        while True:
            GameController.show_menu_options()
            self.show_game_statistics()
            inp = input("\nElige una opcion: ").strip()
            option = MenuOption.from_input(inp)
            if option != None:
                break
            MenuOption.show_incorrect_option_message()

        return option
    
    def request_difficulty():
        GameController.show_difficulty_options()
        GameController.show_back_to_menu_message()
        option = input("- ").strip()
        difficulty = Difficulty.from_input(option)
        while  difficulty == None:
            if option == RETURN_TO_MAIN_MENU_OPT:
                return None
            MenuOption.show_incorrect_option_message()
            option = input("- ").strip()
            difficulty = Difficulty.from_input(option)

        return difficulty

    def show_game_statistics(self):
        print("\nDificultad actual: ", self.difficulty.to_string())
        print("Puntaje:             ", self.user_statistics.score)

    def show_back_to_menu_message():
        print("\nPresione ENTER para volver al menu principal\n")
    
    def show_rules():
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
        GameController.show_back_to_menu_message()
        getpass(prompt="")

    def show_difficulty_options():
        os.system('clear')
        print("Selecciona una dificultad:")
        print("\t1. FACIL: 7 intentos, 5 pistas y palabras cortas")
        print("\t2. NORMAL: 5 intentos, 3 pistas y palabras o frases normales")
        print("\t3. DIFICIL: 3 intentos, 2 pistas y palabras o frases largas")

    def show_menu_options():
        os.system('clear')
        print("Opciones:")
        print("\t1 - Empezar a jugar")
        print("\t2 - Seleccionar dificultad")
        print("\t3 - Reglas")
        print("\t4 - Salir")



    