from enum import Enum

START_GAME_OPT = "1"
SELECT_DIFFICULTY_OPT = "2"
RULES_OPT = "3"
EXIT_OPT = "4"

class MenuOption(Enum):
    START_GAME = 1
    SELECT_DIFFICULTY = 2
    RULES = 3
    EXIT = 4
    
    def from_input(inp):
        if inp == START_GAME_OPT:
            return MenuOption.START_GAME
        elif inp == SELECT_DIFFICULTY_OPT:
            return MenuOption.SELECT_DIFFICULTY
        elif inp == RULES_OPT:
            return MenuOption.RULES
        elif inp == EXIT_OPT:
            return MenuOption.EXIT
        else:
            return None

    def ejecutar(self, menu_juego):
        match self:
            case MenuOption.START_GAME:
                menu_juego.start_to_play()
            case MenuOption.SELECT_DIFFICULTY:
                menu_juego.select_difficulty()
            case MenuOption.RULES:
                menu_juego.show_rules()
            case MenuOption.EXIT:
                print("¡Gracias por jugar!")
            case _:
                print("Opcion incorrecta")

