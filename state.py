from enum import Enum
from difficulty import Difficulty

class GameState(Enum):
    RUNNING = 1
    WON = 2
    LOST = 3

    def print(self):
        match self:
            case GameState.RUNNING:
                print("Juego en curso")
            case GameState.WON:
                print("Felicitaciones!! Ganaste la partida")
            case GameState.LOST:
                print("Perdiste, no te quedan intentos")

    def update_score(self, user_statistics, difficulty: Difficulty):
        match self:
            case GameState.WON:
                user_statistics.increase_score(difficulty)
            case GameState.LOST:
                user_statistics.decrease_score(difficulty)
            case _:
                pass