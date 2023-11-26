from main_menu import *
from estado_juego import EstadoJuego
from dificultad import Dificultad
from juego_ahorcado import JuegoAhorcado

def main():
    juego = JuegoAhorcado(Dificultad.FACIL)

    if input("-") == "1":
        juego.iniciar()
        if juego.estado == EstadoJuego.ABANDONADO:
            main()

main()
