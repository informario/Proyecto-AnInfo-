from enum import Enum
import os
import controller
START_GAME_OPT = "1"
SELECT_DIFFICULTY_OPT = "2"
RULES_OPT = "3"
EXIT_OPT = "4"

class MenuOption(Enum):
    START_GAME = 1
    SELECT_DIFFICULTY = 2
    RULES = 3
    EXIT = 4
    
    def show_incorrect_option_message():
        print("Opcion incorrecta, vuelve a intentarlo\n")

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

    def execute(self, game_controller):
        match self:
            case MenuOption.START_GAME:
                game_controller.play_game()
            case MenuOption.SELECT_DIFFICULTY:
                game_controller.update_difficulty()
            case MenuOption.RULES:
                game_controller.show_rules()
            case MenuOption.EXIT:
                if self.ask_exit_confirmation():
                    print("\n¡Gracias por jugar!\n")
                    raise ExitGameException 
            case _:
                print("Opcion incorrecta")


    def ask_exit_confirmation(self):
        if self == MenuOption.EXIT:
            print("\n")
            os.system('clear')
            while True:
                print("¿Estas seguro de que deseas salir del juego?")
                print("0. Si")
                print("1. No\n")
                inp = input("- ").strip()
                os.system('clear')
                if inp == "0":
                    return True
                if inp == "1":
                    return False
                MenuOption.show_incorrect_option_message()

        return False
    

class ExitGameException(Exception):
    pass