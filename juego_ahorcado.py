from dificultad import Dificultad
from estado_juego import EstadoJuego
from manejador_de_pistas import ManejadorDePistas

class JuegoAhorcado:

    def __init__(self, dificultad):
        self.intentos_restantes = dificultad.obtener_intentos_maximos()
        self.pistas_restantes = dificultad.obtener_pistas()
        self.palabra = dificultad.obtener_palabra()
        self.letras_por_adivinar = list(set(self.palabra))
        self.letras_adivinadas = []
        self.letras_erradas = []
        
        self.estado = EstadoJuego.EN_CURSO
    
    def en_curso(self):
        return self.estado == EstadoJuego.EN_CURSO
    
    def mostrar_palabra(self):
        print("    ")
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
    
    def mostrar_estado(self):
        print("=========================================")
        print("Intentos restantes: ", self.intentos_restantes)
        print("Letras adivinadas: ", self.letras_adivinadas)
        print("Letras erradas: ", self.letras_erradas)
        print("Pistas restantes: ", self.pistas_restantes)

        self.mostrar_palabra()
        print("\n")
        self.estado.print()
        print("=========================================")

    def intentar_adivinar_letra(self, letra):
        if letra in self.letras_por_adivinar:
            self.letras_por_adivinar.remove(letra)
            self.letras_adivinadas.append(letra)
            
        else:
            self.intentos_restantes -= 1
            self.letras_erradas.append(letra)
            
        if len(self.letras_por_adivinar) == 0:
            self.estado = EstadoJuego.GANADO
        if self.intentos_restantes == 0:
            self.estado = EstadoJuego.PERDIDO

    def obtener_pista(self):
        ManejadorDePistas(self)

    # Devuelve el estado final del juego
    def iniciar(self):
        print("Bienvenido al juego del Ahorcado!")
        self.mostrar_estado()
        while self.en_curso():
            print(f"Letras erradas: {self.letras_erradas}")
            print("0. Abandonar partida")
            print("1. Pedir pista")
            print("Ingrese una letra para continuar jugando\n")
            char = input("Intento: ")
            if char == "0":
                print("¿Estas seguro de que deseas abandonar la partida?")
                print("0. Si")
                print("1. No")
                char = input("-")
                if char == "0":
                    return
                else:
                    continue
            if char == "1":
                self.obtener_pista()
                self.mostrar_estado()
                continue
            self.intentar_adivinar_letra(char)
            self.mostrar_estado()
        
        return self.estado