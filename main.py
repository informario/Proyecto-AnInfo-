from controller import *
from session_handler import SessionHandler

def main():
    session_handler = SessionHandler()
    user_name, score = session_handler.run()

    game = GameController(score)
    final_score = game.run()

    session_handler.update_points(user_name, final_score)

main()