from enum import Enum

OPCION_EMPEZAR_JUEGO = "1"
OPCION_SELECCIONAR_DIFICULTAD = "2"
OPCION_REGLAS = "3"
OPCION_SALIR = "4"

class OpcionMenu(Enum):
    EMPEZAR_JUEGO = 1
    SELECCIONAR_DIFICULTAD = 2
    REGLAS = 3
    SALIR = 4
    
    def from_input(inp):
        if inp == OPCION_EMPEZAR_JUEGO:
            return OpcionMenu.EMPEZAR_JUEGO
        elif inp == OPCION_SELECCIONAR_DIFICULTAD:
            return OpcionMenu.SELECCIONAR_DIFICULTAD
        elif inp == OPCION_REGLAS:
            return OpcionMenu.REGLAS
        elif inp == OPCION_SALIR:
            return OpcionMenu.SALIR
        else:
            return None

    def ejecutar(self, menu_juego):
        match self:
            case OpcionMenu.EMPEZAR_JUEGO:
                menu_juego.empezar_a_jugar()
            case OpcionMenu.SELECCIONAR_DIFICULTAD:
                menu_juego.seleccionar_dificultad()
            case OpcionMenu.REGLAS:
                menu_juego.mostrar_reglas()
            case OpcionMenu.SALIR:
                print("¡Gracias por jugar!")
            case _:
                print("Opcion incorrecta")

