from enum import Enum

OPCION_ABANDONAR_PARTIDA = "0"
OPCION_PEDIR_PISTA = "1"
OPCION_PEDIR_AYUDA = "2"

class OpcionJuego(Enum):
    ABANDONAR_PARTIDA = 1
    PEDIR_PISTA = 2
    PEDIR_AYUDA = 3

    @classmethod
    def from_input(cls, inp):
        if inp == OPCION_ABANDONAR_PARTIDA:
            return OpcionJuego.ABANDONAR_PARTIDA
        elif inp == OPCION_PEDIR_PISTA:
            return OpcionJuego.PEDIR_PISTA
        elif inp == OPCION_PEDIR_AYUDA:
            return OpcionJuego.PEDIR_AYUDA
        else:
            return None
            
    def ejecutar(self, juego):
        match self:
            case OpcionJuego.ABANDONAR_PARTIDA:
                juego.abandonar_partida()   # No se utiliza
            case OpcionJuego.PEDIR_PISTA:
                juego.dar_pista()
            case OpcionJuego.PEDIR_AYUDA:
                juego.dar_ayuda()

