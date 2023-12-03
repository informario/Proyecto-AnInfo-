from dificultad import Difficulty
from enum import Enum

class HangmanParts(Enum):
    """
    Enumeración que representa las diferentes partes del ahorcado del ahorcado.

    Attributes:
        HEAD: Representa la cabeza del ahorcado.
        TORSO: Representa el torso del ahorcado.
        LEFT_ARM: Representa el brazo izquierdo del ahorcado.
        RIGHT_ARM: Representa el brazo derecho del ahorcado.
        LEFT_LEG: Representa la pierna izquierda del ahorcado.
        RIGHT_LEG: Representa la pierna derecha del ahorcado.
        SOGA: Representa la soga para colgar al ahorcado.
    """
    HEAD = (0, "0")
    TORSO = (1, "|")
    LEFT_ARM = (2, "/")
    RIGHT_ARM = (3, "\\")
    LEFT_LEG = (4, "/")
    RIGHT_LEG = (5, "\\")
    SOGA = (6, "|")

    def value_int(self):
        """Obtiene el valor entero asociado a la parte del ahorcado."""
        return self.value[0]
    
    def value_str(self):
        """Obtiene el valor en cadena asociado a la parte del ahorcado."""
        return self.value[1]
    
class Hangman():
    """
    Clase que representa el ahorcado.

    Attributes:
        ahorcado (list): Lista que representa el estado actual del ahorcado.
        len_ahorcado (int): Longitud de la lista del ahorcado.
        cuerpo_completo (list): Lista que contiene todas las partes del ahorcado.
    """
    def __init__(self):
        self.hangman = [" ", " ", " ", " ", " ", " ", " "]
        self.len_ahorcado = len(self.hangman)
        self.cuerpo_completo = [HangmanParts.HEAD, HangmanParts.TORSO, HangmanParts.LEFT_ARM, HangmanParts.RIGHT_ARM, HangmanParts.LEFT_LEG, HangmanParts.RIGHT_LEG, HangmanParts.SOGA]
    
    def add_part(self, part: HangmanParts):
        """
        Agrega una parte específica al ahorcado.

        Parameters:
            parte (HangmanParts): La parte del ahorcado a agregar.

        Raises:
            Exception: Si la parte del ahorcado no existe.

        Retorno:
            None
        """
        if part.value_int() > self.len_ahorcado:
            raise Exception("Parte del ahorcado no existe")
        self.hangman[part.value_int()] = part.value_str()

    def add_parts(self, partes: list):
        """
        Agrega varias partes al ahorcado.

        Parameters:
            partes (list): Lista de partes a agregar al ahorcado.

        Retorno:
            None
        """
        for parte in partes:
            self.add_part(parte)
    
    def add_legs(self):
        """Agrega las piernas al ahorcado."""
        self.add_parts([HangmanParts.LEFT_LEG, HangmanParts.RIGHT_LEG])
    
    def add_arms(self):
        """Agrega los brazos al ahorcado."""
        self.add_parts([HangmanParts.LEFT_ARM, HangmanParts.RIGHT_ARM])

    def complete_hangman(self):
        """Completa todo el ahorcado."""
        self.add_parts(self.cuerpo_completo)

    def add_head(self):
        """Agrega la cabeza al ahorcado."""
        self.add_part(HangmanParts.HEAD)

    def add_torso(self):
        """Imprime el estado actual del ahorcado."""
        self.add_part(HangmanParts.TORSO)
    
    def print(self):
        cabeza = self.hangman[HangmanParts.HEAD.value_int()]
        torso = self.hangman[HangmanParts.TORSO.value_int()]
        brazo_izquierdo = self.hangman[HangmanParts.LEFT_ARM.value_int()]
        brazo_derecho = self.hangman[HangmanParts.RIGHT_ARM.value_int()]
        pierna_izquierda = self.hangman[HangmanParts.LEFT_LEG.value_int()]
        pierna_derecha = self.hangman[HangmanParts.RIGHT_LEG.value_int()]
        soga = self.hangman[HangmanParts.SOGA.value_int()]

        print(" _______")
        print(f" |/    {soga}")
        print(f" |     {cabeza}")
        print(f" |    {brazo_izquierdo}{torso}{brazo_derecho}")
        print(f" |    {pierna_izquierda} {pierna_derecha}")
        print(f" |")
        print("_|_")

def add_parts_easy_mode(intentos_fallidos: int, hangman: Hangman):
    """
    Agrega las partes correspondientes al ahorcado del ahorcado en modo fácil.

    Parametros:
        intentos_fallidos (int): La cantidad de intentos fallidos del jugador.
        ahorcado (Hangman): El objeto Hangman al que se le agregarán las partes.

    Retorno:
        None
    """
    partes_a_agregar = [
        HangmanParts.HEAD,
        HangmanParts.TORSO,
        HangmanParts.LEFT_ARM,
        HangmanParts.RIGHT_ARM,
        HangmanParts.LEFT_LEG,
        HangmanParts.RIGHT_LEG,
        HangmanParts.SOGA,
    ]

    partes_agregar = partes_a_agregar[:intentos_fallidos]
    hangman.add_parts(partes_agregar)

def add_parts_normal_mode(intentos_fallitos: int, hangman: Hangman):
    """
    Agrega las partes correspondientes al ahorcado del ahorcado en modo normal.

    Parametros:
        intentos_fallidos (int): La cantidad de intentos fallidos del jugador.
        ahorcado (Hangman): El objeto Hangman al que se le agregarán las partes.

    Retorno:
        None
    """    
    if intentos_fallitos == 0:
        return
    if intentos_fallitos == 5:
        hangman.complete_hangman()
        return
    
    if intentos_fallitos >= 1:
        hangman.add_head()
    if intentos_fallitos >= 2:
        hangman.add_torso()
    if intentos_fallitos >= 3:
        hangman.add_arms()
    if intentos_fallitos >= 4:
        hangman.add_legs()

def add_parts_hard_mode(intentos_fallidos: int, hangman: Hangman):
    """
    Agrega las partes correspondientes al ahorcado del ahorcado en modo difícil.

    Parametros:
        intentos_fallidos (int): La cantidad de intentos fallidos del jugador.
        ahorcado (Hangman): El objeto Hangman al que se le agregarán las partes.

    Retorno:
        None
    """
    if intentos_fallidos == 0:
        return
    if intentos_fallidos == 3:
        hangman.complete_hangman()
        return
    if intentos_fallidos >= 1:
        hangman.add_head()
        hangman.add_torso()
    if intentos_fallidos >= 2:
        hangman.add_arms()
        hangman.add_legs()


def dibujar_ahorcado(intentos_fallidos, dificultad: Difficulty):
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
    if dificultad.get_max_attempts() < intentos_fallidos:
        raise Exception("Intentos fallidos no puede ser mayor a los intentos maximos de la dificultad")
    
    hangman = Hangman()
    if dificultad == Difficulty.EASY:
        add_parts_easy_mode(intentos_fallidos, hangman)
    elif dificultad == Difficulty.MEDIUM:
        add_parts_normal_mode(intentos_fallidos, hangman)
    else:
        add_parts_hard_mode(intentos_fallidos, hangman)

    hangman.print()

# Ejemplo de uso
dibujar_ahorcado(1, Difficulty.EASY)