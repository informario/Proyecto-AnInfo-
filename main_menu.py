from juego_ahorcado import JuegoAhorcado
from estado_juego import EstadoJuego
from dificultad import Dificultad
from enum import Enum

OPCION_VOLVER_MENU_PRINCIPAL = 0
DIFICULTAD_INICIAL = Dificultad.NORMAL
OPCIONES_SELECCIONAR_DIFICULTAD = ["1", "2", "3", "0"]

class OpcionMenu(Enum):
    EMPEZAR_JUEGO = 1
    SELECCIONAR_DIFICULTAD = 2
    REGLAS = 3
    SALIR = 4
    
    def from_input(input):
        match input:
            case "1":
                return OpcionMenu.EMPEZAR_JUEGO
            case "2":
                return OpcionMenu.SELECCIONAR_DIFICULTAD
            case "3":
                return OpcionMenu.REGLAS
            case "4":
                return OpcionMenu.SALIR
            case _:
                return None

    def ejecutar(self, menu_juego):
        match self:
            case OpcionMenu.EMPEZAR_JUEGO:
                menu_juego.empezar_a_jugar()
            case OpcionMenu.SELECCIONAR_DIFICULTAD:
                menu_juego.seleccionar_dificultad()
            case OpcionMenu.REGLAS:
                print("Reglas")
            case OpcionMenu.SALIR:
                print("¡Gracias por jugar!")
            case _:
                print("Opcion incorrecta")

class MenuJuego:
    def __init__(self):
        self.dificultad = DIFICULTAD_INICIAL
    
    def mostrar_opciones():
        print("Opciones:")
        print("\t1 - Empezar a jugar")
        print("\t2 - Seleccionar dificultad")
        print("\t3 - Reglas")
        print("\t4 - Salir")

    def ejecutar_opciones(self):
        """
        Muestra el menu principal del juego del Ahorcado y maneja las opciones seleccionadas por el usuario.

        El bucle se ejecuta continuamente hasta que el usuario elige salir.

        Entrada:
        - Elige una opción ingresando el número correspondiente.

        Salida:
        - Mensajes de la opcion elegida.
        """    
        while True:
            MenuJuego.mostrar_opciones()
            opcion = input("Elige una opcion: ")
            opcion = OpcionMenu.from_input(opcion)
            if opcion == None:
                print("Opcion incorrecta")
                continue
            opcion.ejecutar(self)
            if opcion == OpcionMenu.SALIR:
                break


    def seleccionar_dificultad(self):
        print("Selecciona una dificultad:")
        print("1. FACIL: 7 intentos, 3 pistas y palabras cortas")
        print("2. NORMAL: 5 intentos, 1 pista y palabras o frases normales")
        print("3. DIFICIL: 3 intentos, sin pistas y palabras o frases largas")
        print("0. Volver al menu principal")
        print("Dificultad actual: ", self.dificultad.to_string())
        print("\n")
        opcion = input("-")
        while opcion not in OPCIONES_SELECCIONAR_DIFICULTAD:
            print("Opcion incorrecta, vuelve a intentarlo")
            opcion = input("-")
            #Esto se puede abstraer a otra función porque lo vamos a usar en varios lugares
        
        if int(opcion) == OPCION_VOLVER_MENU_PRINCIPAL:
            return
        dificultad = Dificultad.from_index(int(opcion))
        if dificultad == None:
            # Esto no deberia pasar nunca
            return
        self.dificultad = dificultad
        print("Dificultad seleccionada: ", self.dificultad.to_string())
        return
        
    def empezar_a_jugar(self):
        juego = JuegoAhorcado(self.dificultad)
        juego.iniciar()

