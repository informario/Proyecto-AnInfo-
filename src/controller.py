from getpass import getpass
from src.game import HangmanGame
from src.menu import GameMenu
from src.state import GameState
from src.difficulty import Difficulty
from enum import Enum
from src.clue_handler import ClueHandler
from options.menu import ExitGameException, MenuOption
from src.user_statistics import UserStatistics

RETURN_TO_MAIN_MENU_OPT = ""
INITIAL_DIFFICULTY = Difficulty.MEDIUM

class GameController:
    def __init__(self, score, basic_clues, bonus_clues):
        self.user_statistics = UserStatistics(score, basic_clues, bonus_clues)
        self.difficulty = INITIAL_DIFFICULTY

    def run(self):
        menu = GameMenu(self)
        while True:
            try: 
                option = menu.request_option()
                option.execute(self)
            except ExitGameException:
                break

    def obtain_user_stats(self):
        return self.user_statistics
    
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
        print("Pistas de revelacion de letra disponibles: ", self.user_statistics.get_basic_clues())
        print("Pistas de ayuda de palabra disponibles:    ", self.user_statistics.get_bonus_clues())
        print("Puntaje:                                   ", self.user_statistics.score)

    def buy_basic_clue(self):
        self.user_statistics.buy_basic_clue()

    def buy_bonus_clue(self):
        self.user_statistics.buy_bonus_clue()
