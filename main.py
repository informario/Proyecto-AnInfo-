from src.controller import *
from src.session_handler import *

def main():
    session_handler = SessionHandler()
    user_name, score, basic_clues, bonus_clues = session_handler.run()

    if user_name is not None:
        game = GameController(score, basic_clues, bonus_clues)
        game.run()
        user_stats = game.obtain_user_stats()

        session_handler.update(user_name, user_stats) # Hay que implementar la logica para devolver la cantidad de pistas acumuladas

main()