from enum import Enum
from utils import clear_screen

from options.menu import ExitGameException, MenuOption

ABANDON_GAME_OPT = "0"
USE_BASIC_CLUE_OPT = "1"
BUY_BASIC_CLUE_OPT = "2"
USE_BONUS_CLUE_OPT = "3"
BUY_BONUS_CLUE_OPT = "4"

class GameOpt(Enum):
    ABANDON_GAME_OPT = 1
    USE_BASIC_CLUE = 2
    BUY_BASIC_CLUE = 3
    USE_BONUS_CLUE = 4
    BUY_BONUS_CLUE = 5

    @classmethod
    def from_input(cls, inp):
        if inp == ABANDON_GAME_OPT:
            return GameOpt.ABANDON_GAME_OPT
        elif inp == USE_BASIC_CLUE_OPT:
            return GameOpt.USE_BASIC_CLUE
        elif inp == BUY_BASIC_CLUE_OPT:
            return GameOpt.BUY_BASIC_CLUE
        elif inp == USE_BONUS_CLUE_OPT:
            return GameOpt.USE_BONUS_CLUE
        elif inp == BUY_BONUS_CLUE_OPT:
            return GameOpt.BUY_BONUS_CLUE
        else:
            return None
            
    def execute(self, juego):
        match self:
            case GameOpt.ABANDON_GAME_OPT:
                if self.ask_abandon_confirmation():
                    raise ExitGameException
            case GameOpt.USE_BASIC_CLUE:
                juego.use_basic_clue()
            case GameOpt.BUY_BASIC_CLUE:
                juego.buy_basic_clue()
            case GameOpt.USE_BONUS_CLUE:
                juego.use_bonus_clue()
            case GameOpt.BUY_BONUS_CLUE:
                juego.buy_bonus_clue()

    def ask_abandon_confirmation(self):
        if self == GameOpt.ABANDON_GAME_OPT:
            print("\n")
            while True:
                print("¿Estas seguro de que deseas abandonar la partida?")
                print("0. Si")
                print("1. No\n")
                inp = input("- ").strip()
                clear_screen()
                if inp == "0":
                    return True
                if inp == "1":
                    return False
                MenuOption.show_incorrect_option_message()
