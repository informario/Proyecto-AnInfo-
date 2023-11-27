from enum import Enum

class EstadoJuego(Enum):
    EN_CURSO = 1
    GANADO = 2
    PERDIDO = 3
    
    def print(self):
        match self:
            case EstadoJuego.EN_CURSO:
                print("Juego en curso")
            case EstadoJuego.GANADO:
                print("Felicitaciones, ganaste")
            case EstadoJuego.PERDIDO:
                print("Perdiste")
