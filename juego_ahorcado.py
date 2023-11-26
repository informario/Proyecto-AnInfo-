from dificultad import Dificultad

class JuegoAhorcado:

    def __init__(self, dificultad):
        self.dificultad = dificultad

        self.letras_por_adivinar = list(set(self.palabra))
        self.letras_adivinadas = []
        self.letras_dichas = []
        self.estado = EstadoJuego.EN_CURSO
    
    def en_curso(self):
        return self.estado == EstadoJuego.EN_CURSO
    
    def mostrar_palabra(self):
        for letra in self.dificultad.palabra:
            if letra in self.letras_adivinadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
    
    def mostrar_estado(self):
        print("=========================================")
        print("Intentos restantes: x")
        print("Letras adivinadas: x")
        print("Letras erradas: x")
        print("Pistas restantes: x")

        self.dificultad.print()
        self.mostrar_palabra()
        self.estado.print()
        print("=========================================")

    def intentar_adivinar_letra(self, letra):
        if letra in self.letras_por_adivinar:
            self.letras_por_adivinar.remove(letra)
            self.letras_adivinadas.append(letra)
            
        else:
            self.intentos_restantes -= 1

        if letra not in self.letras_dichas:
            self.letras_dichas.append(letra)

        if len(self.letras_por_adivinar) == 0:
            self.estado = EstadoJuego.GANADO
        if self.intentos_restantes == 0:
            self.estado = EstadoJuego.PERDIDO

    def obtener_pista(self):
        if self.pistas == 0:
            return
        # Logica para obtener una pista

    def abandonar(self):
        self.estado = EstadoJuego.ABANDONADO

    # Devuelve el estado final del juego
    def iniciar(self):
        self.mostrar_estado()
        while self.en_curso():
            print(f"Letras dichas: {self.letras_dichas}")
            print("0. Abandonar partida")
            print("1. Pedir pista")
            print("Ingrese una letra para continuar jugando\n")
            char = input("Intento: ")
            if char == "0":
                self.abandonar()
                return
            if char == "1":
                self.obtener_pista()
                continue
            self.intentar_adivinar_letra(char)
            self.mostrar_estado()
        
        return self.estado