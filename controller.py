from getpass import getpass
import os
from game import HangmanGame
from menu import GameMenu
from state import GameState
from difficulty import Difficulty
from enum import Enum
from clue_handler import ClueHandler
from options.menu import ExitGameException, MenuOption
from user_statistics import UserStatistics

RETURN_TO_MAIN_MENU_OPT = ""
INITIAL_DIFFICULTY = Difficulty.MEDIUM

class GameController:
    def __init__(self, score, basic_clues, hint_clues):
        self.user_statistics = UserStatistics(score, basic_clues, hint_clues)
        self.difficulty = INITIAL_DIFFICULTY

    def run(self):
        menu = GameMenu(self)
        while True:
            try: 
                option = menu.request_option()
                option.execute(self)
            except ExitGameException:
                break

        return self.user_statistics.get_score(), self.user_statistics.get_basic_clues(), self.user_statistics.get_hint_clues()

    def update_difficulty(self):
        dificulty = GameMenu.request_selected_difficulty()
        if dificulty != None:
            self.difficulty = dificulty

    def play_game(self):
        category = GameMenu.request_word_category()
        game = HangmanGame(self.difficulty, self.user_statistics, category)
        game.run()
        game.update_stats(self.user_statistics)
        game.update_score(self.user_statistics, self.difficulty)
    
    def show_rules(self):
        GameMenu.show_rules()

    def show_game_statistics(self):
        print("\nDificultad actual: ", self.difficulty.to_string())
        print("Puntaje:             ", self.user_statistics.score)

    def buy_basic_clue(self):
        self.user_statistics.buy_basic_clue()

    def buy_hint_clue(self):
        self.user_statistics.buy_hint_clue()

