from controller import *
from session_handler import *

def main():
    session_handler = SessionHandler()
    user_name, score = session_handler.run()

    if user_name is not None:
        game = GameController(score[INDEX_SCORE])
        final_score = game.run()

        session_handler.update(user_name, final_score, 0) # Hay que implementar la logica para devolver la cantidad de pistas acumuladas

main()