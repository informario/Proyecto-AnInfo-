import unittest
from unittest.mock import patch, call
from difficulty import Difficulty
from src.menu import GameMenu

from options.menu import MenuOption

class TestGameMenu(unittest.TestCase):
    
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
        from src.controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["1"]
            game_controler = GameController(0, 0, 0)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.START_GAME)

    def test_request_option_select_difficulty(self):
        from src.controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["2"]
            game_controler = GameController(0, 0, 0)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.SELECT_DIFFICULTY)
            
    def test_request_option_buy_basic_clue(self):
        from src.controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["3"]
            game_controler = GameController(0, 0, 0)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.BUY_BASIC_CLUE)

    def test_request_option_buy_hint_clue(self):
        from src.controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["4"]
            game_controler = GameController(0, 0, 0)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.BUY_HINT_CLUE)

    def test_request_option_rules(self):
        from src.controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["5"]
            game_controler = GameController(0, 0, None)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.RULES)

    def test_request_option_exit(self):
        from src.controller import GameController
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["6"]
            game_controler = GameController(0, 0, None)
            game_menu = GameMenu(game_controler)
            option = game_menu.request_option()
            self.assertEqual(option, MenuOption.EXIT)

if __name__ == "__main__":
    unittest.main()