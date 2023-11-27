from juego_ahorcado import JuegoAhorcado
from estado_juego import EstadoJuego
from dificultad import Dificultad

OPCION_VOLVER_MENU_PRINCIPAL = 0
DIFICULTAD_INICIAL = Dificultad.NORMAL
OPCIONES_SELECCIONAR_DIFICULTAD = ["1", "2", "3", "0"]


def seleccionar_dificultad(dificultad):
    print("Selecciona una dificultad:")
    print("1. FACIL: 7 intentos, 3 pistas y palabras cortas")
    print("2. NORMAL: 5 intentos, 1 pista y palabras o frases normales")
    print("3. DIFICIL: 3 intentos, sin pistas y palabras o frases largas")
    print("0. Volver al menu principal")
    print("Dificultad actual: ", dificultad[0].to_string())
    print("\n")
    opcion = input("-")
    while opcion not in OPCIONES_SELECCIONAR_DIFICULTAD:
        print("Opcion incorrecta, vuelve a intentarlo")
        opcion = input("-")
    
    if int(opcion) == OPCION_VOLVER_MENU_PRINCIPAL:
        return
    dificultad[0] = Dificultad.from_index(int(opcion))
    if dificultad[0] == None:
        # Esto no deberia pasar nunca
        dificultad[0] = DIFICULTAD_INICIAL
    print("Dificultad seleccionada: ", dificultad[0].to_string())
    return
        
def empezar_a_jugar(dificultad):
    juego = JuegoAhorcado(dificultad)
    estado = juego.iniciar()
            
def main_menu():
    """
    Muestra el menu principal del juego del Ahorcado y maneja las opciones seleccionadas por el usuario.

    El bucle se ejecuta continuamente hasta que el usuario elige salir.

    Entrada:
    - Elige una opción ingresando el número correspondiente.

    Salida:
    - Mensajes de la opcion elegida.
    """    
    dificultad = DIFICULTAD_INICIAL
    while True:
        mostrar_opciones()
        opcion = input("Elige una opcion: ")
        match opcion:
            case "1": 
                empezar_a_jugar(dificultad)
            case "2":
                seleccionar_dificultad([dificultad])
            case "3":
                print("Reglas")
            case "4":
                print("Salir")
                break
            case _:
                print("Opcion incorrecta")

def mostrar_opciones():
    print("Opciones:")
    print("\t1 - Empezar a jugar")
    print("\t2 - Seleccionar dificultad")
    print("\t3 - Reglas")
    print("\t4 - Salir")