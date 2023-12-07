from getpass import getpass
import os
from word_category import WordCategory
from difficulty import Difficulty
from options.menu import MenuOption
from utils import clear_screen
import banners

RETURN_TO_MAIN_MENU_OPT = ""


class GameMenu:

    def __init__(self, game_controller):
        self.game_controller = game_controller

    @staticmethod
    def show_back_to_menu_message():
        print("\nPresione ENTER para volver al menu principal\n")

    @staticmethod
    def show_options():
        clear_screen()

        banners.menu()
        GameMenu._show_options()

    @staticmethod
    def _show_options():
        print("Opciones:")
        print("\t1 - Empezar a jugar")
        print("\t2 - Seleccionar dificultad")
        print("\t3 - Comprar una pista de revelacion de letra (cuesta 2 puntos)")
        print("\t4 - Comprar una pista de ayuda de palabra (cuesta 10 puntos)")
        print("\t5 - Reglas")
        print("\t6 - Salir")

    @staticmethod
    def show_rules():
        clear_screen()
        GameMenu._show_rules()
        GameMenu.show_back_to_menu_message()
        getpass(prompt="")

    @staticmethod
    def _show_rules():
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

    @staticmethod
    def show_difficulty_options():
        clear_screen()
        GameMenu._show_difficulty_options()

    @staticmethod
    def _show_difficulty_options():
        print("Selecciona una dificultad:")
        print("\t1. FACIL: 7 intentos, 5 pistas y palabras cortas")
        print("\t2. NORMAL: 5 intentos, 3 pistas y palabras o frases normales")
        print("\t3. DIFICIL: 3 intentos, 2 pistas y palabras o frases largas")

    def request_selected_difficulty():
        GameMenu.show_difficulty_options()
        GameMenu.show_back_to_menu_message()
        option = input("- ").strip()
        difficulty = Difficulty.from_input(option)
        while  difficulty == None:
            if option == RETURN_TO_MAIN_MENU_OPT:
                return None
            MenuOption.show_incorrect_option_message()
            option = input("- ").strip()
            difficulty = Difficulty.from_input(option)

        return difficulty
    
    def request_option(self):
        while True:
            GameMenu.show_options()
            self.game_controller.show_game_statistics()
            inp = input("\nElige una opcion: ").strip()
            option = MenuOption.from_input(inp)
            if option != None:
                break
            
            MenuOption.show_incorrect_option_message()

        return option

    def show_category_options():
        clear_screen()
        GameMenu._show_category_options()

    @staticmethod
    def _show_category_options():
        print("Selecciona una categoria:")
        print("\t1. Aninfo")
        print("\t2. Famosos")
        print("\t3. Peliculas y series")
        print("\t4. Animales")
        print("\t5. Otros\n")
    
    def request_word_category():
        GameMenu.show_category_options()
        option = input("- ").strip()
        category = WordCategory.from_input(option)
        while category == None:
            MenuOption.show_incorrect_option_message()
            option = input("- ").strip()
            category = WordCategory.from_input(option)

        return category

import unittest
from unittest.mock import patch, call

class TestGameMenu(unittest.TestCase):

    def test_show_back_to_menu_message(self):
        with patch("builtins.print") as mock_print:
            GameMenu.show_back_to_menu_message()
            mock_print.assert_called_with("\nPresione ENTER para volver al menu principal\n")

    def test_show_options(self):
        with patch("builtins.print") as mock_print:
            GameMenu._show_options()

        expected_calls = [
            call("Opciones:"),
            call("\t1 - Empezar a jugar"),
            call("\t2 - Seleccionar dificultad"),
            call("\t3 - Comprar una pista de revelacion de letra (cuesta 2 puntos)"),
            call("\t4 - Comprar una pista de ayuda de palabra (cuesta 10 puntos)"),
            call("\t5 - Reglas"),
            call("\t6 - Salir")
        ]

        mock_print.assert_has_calls(expected_calls, any_order=False)

    
    def test_show_difficulty_options(self):
        with patch("builtins.print") as mock_print:
            GameMenu._show_difficulty_options()

        expected_calls = [
            call("Selecciona una dificultad:"),
            call("\t1. FACIL: 7 intentos, 5 pistas y palabras cortas"),
            call("\t2. NORMAL: 5 intentos, 3 pistas y palabras o frases normales"),
            call("\t3. DIFICIL: 3 intentos, 2 pistas y palabras o frases largas")
        ]

        mock_print.assert_has_calls(expected_calls, any_order=False)

    def test_show_category_options(self):
        with patch("builtins.print") as mock_print:
            GameMenu._show_category_options()

        expected_calls = [
            call("Selecciona una categoria:"),
            call("\t1. Aninfo"),
            call("\t2. Famosos"),
            call("\t3. Peliculas y series"),
            call("\t4. Animales"),
            call("\t5. Otros\n")
        ]

        mock_print.assert_has_calls(expected_calls, any_order=False)

    
    def test_request_selected_difficulty_easy(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["1"]
            difficulty = GameMenu.request_selected_difficulty()
            self.assertEqual(difficulty, Difficulty.EASY)

    def test_request_selected_difficulty_medium(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["2"]
            difficulty = GameMenu.request_selected_difficulty()
            self.assertEqual(difficulty, Difficulty.MEDIUM)

    def test_request_selected_difficulty_hard(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["3"]
            difficulty = GameMenu.request_selected_difficulty()
            self.assertEqual(difficulty, Difficulty.HARD)

    def test_request_selected_difficulty_incorrect_option(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["4", "1"]
            difficulty = GameMenu.request_selected_difficulty()
            self.assertEqual(difficulty, Difficulty.EASY)

    def test_request_option_start_game(self):
        from controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["1"]
            game_controler = GameController(0, 0, 0)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.START_GAME)

    def test_request_option_select_difficulty(self):
        from controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["2"]
            game_controler = GameController(0, 0, 0)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.SELECT_DIFFICULTY)
            
    def test_request_option_buy_basic_clue(self):
        from controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["3"]
            game_controler = GameController(0, 0, 0)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.BUY_BASIC_CLUE)

    def test_request_option_buy_hint_clue(self):
        from controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["4"]
            game_controler = GameController(0, 0, 0)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.BUY_HINT_CLUE)

    def test_request_option_rules(self):
        from controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["5"]
            game_controler = GameController(0, 0, None)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.RULES)

    def test_request_option_exit(self):
        from controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["6"]
            game_controler = GameController(0, 0, None)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.EXIT)

if __name__ == "__main__":
    unittest.main()