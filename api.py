from dificultad import Dificultad
from enum import Enum

class PartesAhorcado(Enum):
    """
    Enumeración que representa las diferentes partes del ahorcado del ahorcado.

    Attributes:
        CABEZA: Representa la cabeza del ahorcado.
        TORSO: Representa el torso del ahorcado.
        BRAZO_IZQUIERDO: Representa el brazo izquierdo del ahorcado.
        BRAZO_DERECHO: Representa el brazo derecho del ahorcado.
        PIERNA_IZQUIERDA: Representa la pierna izquierda del ahorcado.
        PIERNA_DERECHA: Representa la pierna derecha del ahorcado.
        SOGA: Representa la soga para colgar al ahorcado.
    """
    CABEZA = (0, "0")
    TORSO = (1, "|")
    BRAZO_IZQUIERDO = (2, "/")
    BRAZO_DERECHO = (3, "\\")
    PIERNA_IZQUIERDA = (4, "/")
    PIERNA_DERECHA = (5, "\\")
    SOGA = (6, "|")

    def value_int(self):
        """Obtiene el valor entero asociado a la parte del ahorcado."""
        return self.value[0]
    
    def value_str(self):
        """Obtiene el valor en cadena asociado a la parte del ahorcado."""
        return self.value[1]
    
class Ahorcado():
    """
    Clase que representa el ahorcado.

    Attributes:
        ahorcado (list): Lista que representa el estado actual del ahorcado.
        len_ahorcado (int): Longitud de la lista del ahorcado.
        cuerpo_completo (list): Lista que contiene todas las partes del ahorcado.
    """
    def __init__(self):
        self.ahorcado = [" ", " ", " ", " ", " ", " ", " "]
        self.len_ahorcado = len(self.ahorcado)
        self.cuerpo_completo = [PartesAhorcado.CABEZA, PartesAhorcado.TORSO, PartesAhorcado.BRAZO_IZQUIERDO, PartesAhorcado.BRAZO_DERECHO, PartesAhorcado.PIERNA_IZQUIERDA, PartesAhorcado.PIERNA_DERECHA, PartesAhorcado.SOGA]
    
    def agregar_parte(self, parte: PartesAhorcado):
        """
        Agrega una parte específica al ahorcado.

        Parameters:
            parte (PartesAhorcado): La parte del ahorcado a agregar.

        Raises:
            Exception: Si la parte del ahorcado no existe.

        Retorno:
            None
        """
        if parte.value_int() > self.len_ahorcado:
            raise Exception("Parte del ahorcado no existe")
        self.ahorcado[parte.value_int()] = parte.value_str()

    def agregar_partes(self, partes: list):
        """
        Agrega varias partes al ahorcado.

        Parameters:
            partes (list): Lista de partes a agregar al ahorcado.

        Retorno:
            None
        """
        for parte in partes:
            self.agregar_parte(parte)
    
    def agregar_piernas(self):
        """Agrega las piernas al ahorcado."""
        self.agregar_partes([PartesAhorcado.PIERNA_IZQUIERDA, PartesAhorcado.PIERNA_DERECHA])
    
    def agregar_brazos(self):
        """Agrega los brazos al ahorcado."""
        self.agregar_partes([PartesAhorcado.BRAZO_IZQUIERDO, PartesAhorcado.BRAZO_DERECHO])

    def completar_ahorcado(self):
        """Completa todo el ahorcado."""
        self.agregar_partes(self.cuerpo_completo)

    def agregar_cabeza(self):
        """Agrega la cabeza al ahorcado."""
        self.agregar_parte(PartesAhorcado.CABEZA)

    def agregar_torso(self):
        """Imprime el estado actual del ahorcado."""
        self.agregar_parte(PartesAhorcado.TORSO)
    
    def print(self):
        cabeza = self.ahorcado[PartesAhorcado.CABEZA.value_int()]
        torso = self.ahorcado[PartesAhorcado.TORSO.value_int()]
        brazo_izquierdo = self.ahorcado[PartesAhorcado.BRAZO_IZQUIERDO.value_int()]
        brazo_derecho = self.ahorcado[PartesAhorcado.BRAZO_DERECHO.value_int()]
        pierna_izquierda = self.ahorcado[PartesAhorcado.PIERNA_IZQUIERDA.value_int()]
        pierna_derecha = self.ahorcado[PartesAhorcado.PIERNA_DERECHA.value_int()]
        soga = self.ahorcado[PartesAhorcado.SOGA.value_int()]

        print(" _______")
        print(f" |/    {soga}")
        print(f" |     {cabeza}")
        print(f" |    {brazo_izquierdo}{torso}{brazo_derecho}")
        print(f" |    {pierna_izquierda} {pierna_derecha}")
        print(f" |")
        print("_|_")

def agregar_partes_modo_facil(intentos_fallidos: int, ahorcado: Ahorcado):
    """
    Agrega las partes correspondientes al ahorcado del ahorcado en modo fácil.

    Parametros:
        intentos_fallidos (int): La cantidad de intentos fallidos del jugador.
        ahorcado (Ahorcado): El objeto Ahorcado al que se le agregarán las partes.

    Retorno:
        None
    """
    partes_a_agregar = [
        PartesAhorcado.CABEZA,
        PartesAhorcado.TORSO,
        PartesAhorcado.BRAZO_IZQUIERDO,
        PartesAhorcado.BRAZO_DERECHO,
        PartesAhorcado.PIERNA_IZQUIERDA,
        PartesAhorcado.PIERNA_DERECHA,
        PartesAhorcado.SOGA,
    ]

    partes_agregar = partes_a_agregar[:intentos_fallidos]
    ahorcado.agregar_partes(partes_agregar)

def agregar_partes_modo_normal(intentos_fallitos: int, ahorcado: Ahorcado):
    """
    Agrega las partes correspondientes al ahorcado del ahorcado en modo normal.

    Parametros:
        intentos_fallidos (int): La cantidad de intentos fallidos del jugador.
        ahorcado (Ahorcado): El objeto Ahorcado al que se le agregarán las partes.

    Retorno:
        None
    """    
    if intentos_fallitos == 0:
        return
    if intentos_fallitos == 5:
        ahorcado.completar_ahorcado()
        return
    
    if intentos_fallitos >= 1:
        ahorcado.agregar_cabeza()
    if intentos_fallitos >= 2:
        ahorcado.agregar_torso()
    if intentos_fallitos >= 3:
        ahorcado.agregar_brazos()
    if intentos_fallitos >= 4:
        ahorcado.agregar_piernas()

def agregar_partes_modo_dificil(intentos_fallidos: int, ahorcado: Ahorcado):
    """
    Agrega las partes correspondientes al ahorcado del ahorcado en modo difícil.

    Parametros:
        intentos_fallidos (int): La cantidad de intentos fallidos del jugador.
        ahorcado (Ahorcado): El objeto Ahorcado al que se le agregarán las partes.

    Retorno:
        None
    """
    if intentos_fallidos == 0:
        return
    if intentos_fallidos == 3:
        ahorcado.completar_ahorcado()
        return
    if intentos_fallidos >= 1:
        ahorcado.agregar_cabeza()
        ahorcado.agregar_torso()
    if intentos_fallidos >= 2:
        ahorcado.agregar_brazos()
        ahorcado.agregar_piernas()


def dibujar_ahorcardo(intentos_fallidos, dificultad: Dificultad):
    """
    Dibuja el ahorcado del ahorcado de acuerdo a los intentos fallidos y la dificultad.

    Parametros:
        intentos_fallidos (int): La cantidad de intentos fallidos del jugador.
        dificultad (Dificultad): La dificultad del juego.

    Raises:
        Exception: Si los intentos fallidos son mayores a los intentos máximos de la dificultad.

    Retorno:
        None
    """
    if dificultad.obtener_intentos_maximos() < intentos_fallidos:
        raise Exception("Intentos fallidos no puede ser mayor a los intentos maximos de la dificultad")
    
    ahorcado = Ahorcado()
    if dificultad == Dificultad.FACIL:
        agregar_partes_modo_facil(intentos_fallidos, ahorcado)
    elif dificultad == Dificultad.NORMAL:
        agregar_partes_modo_normal(intentos_fallidos, ahorcado)
    else:
        agregar_partes_modo_dificil(intentos_fallidos, ahorcado)

    ahorcado.print()

# Ejemplo de uso
dibujar_ahorcardo(5, Dificultad.NORMAL)