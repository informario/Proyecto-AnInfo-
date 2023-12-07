from enum import Enum
from utils import clear_screen

from options.menu import ExitGameException, MenuOption

ABANDON_GAME_OPT = "0"
USE_CLUE_OPT = "1"
BUY_CLUE_OPT = "2"
USE_HINT_OPT = "3"
BUY_HINT_OPT = "4"

class GameOpt(Enum):
    ABANDON_GAME_OPT = 1
    USE_CLUE = 2
    BUY_CLUE = 3
    USE_HINT = 4
    BUY_HINT = 5

    @classmethod
    def from_input(cls, inp):
        if inp == ABANDON_GAME_OPT:
            return GameOpt.ABANDON_GAME_OPT
        elif inp == USE_CLUE_OPT:
            return GameOpt.USE_CLUE
        elif inp == BUY_CLUE_OPT:
            return GameOpt.BUY_CLUE
        elif inp == USE_HINT_OPT:
            return GameOpt.USE_HINT
        elif inp == BUY_HINT_OPT:
            return GameOpt.BUY_HINT
        else:
            return None
            
    def execute(self, juego):
        match self:
            case GameOpt.ABANDON_GAME_OPT:
                if self.ask_abandon_confirmation():
                    raise ExitGameException
            case GameOpt.USE_CLUE:
                juego.use_basic_clue()
            case GameOpt.BUY_CLUE:
                juego.buy_basic_clue()
            case GameOpt.USE_HINT:
                juego.use_hint_clue()
            case GameOpt.BUY_HINT:
                juego.buy_hint_clue()

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
