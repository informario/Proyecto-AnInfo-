from enum import Enum

ABANDON_GAME_OPT = "0"
ASK_CLUE_OPT = "1"
ASK_HELP_OPT = "2"

class GameOpt(Enum):
    ABANDON_GAME_OPT = 1
    ASK_CLUE = 2
    ASK_HELP = 3

    @classmethod
    def from_input(cls, inp):
        if inp == ABANDON_GAME_OPT:
            return GameOpt.ABANDON_GAME_OPT
        elif inp == ASK_CLUE_OPT:
            return GameOpt.ASK_CLUE
        elif inp == ASK_HELP_OPT:
            return GameOpt.ASK_HELP
        else:
            return None
            
    def execute(self, juego):
        match self:
            case GameOpt.ABANDON_GAME_OPT:
                juego.game_abandoned()   # No se utiliza
            case GameOpt.ASK_CLUE:
                juego.give_clue()
            case GameOpt.ASK_HELP:
                juego.give_help()

