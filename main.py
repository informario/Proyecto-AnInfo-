from controller import *
from session_handler import *

def main():
    session_handler = SessionHandler()
    user_name, score, clues = session_handler.run()

    if user_name is not None:
        game = GameController(score, clues)
        final_score, final_basic_clues = game.run()

        session_handler.update(user_name, final_score, final_basic_clues) # Hay que implementar la logica para devolver la cantidad de pistas acumuladas

main()