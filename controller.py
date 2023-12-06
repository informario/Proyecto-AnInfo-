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
    def __init__(self):
        self.user_statistics = UserStatistics()
        self.clue_handler = ClueHandler()
        self.difficulty = INITIAL_DIFFICULTY

    def run(self):
        menu = GameMenu(self)
        while True:
            try: 
                option = menu.request_option()
                option.execute(self)
            except ExitGameException:
                break

    def update_difficulty(self):
        dificulty = GameMenu.request_selected_difficulty()
        if dificulty != None:
            self.difficulty = dificulty

    def play_game(self):
        game = HangmanGame(self.difficulty, self)
        game.run()
        game.update_score(self.user_statistics, self.difficulty)
    
    def show_rules(self):
        GameMenu.show_rules()

    def show_game_statistics(self):
        print("\nDificultad actual: ", self.difficulty.to_string())
        print("Puntaje:             ", self.user_statistics.score)

    def buy_clue(self):
        self.clue_handler.buy_clue(self.user_statistics)

    def use_clue(self, letters_to_guess, letters_guessed):
        self.clue_handler.use_clue(self.user_statistics, letters_to_guess, letters_guessed)
