import random

class ManejadorDePistas:
    def dar_pista(self,juego):
        if juego.pistas_restantes == 0:
            print("\nNo te quedan pistas!\n")
            return
        
        if len(juego.letras_por_adivinar) <= 1:
            print("\nTe queda solo una letra, no podes usar la pista!\n")
            return

        pista = random.choice(juego.letras_por_adivinar)
        juego.letras_por_adivinar.remove(pista)
        juego.letras_adivinadas.append(pista)

        juego.pistas_restantes -= 1

    def __init__(self,juego):
        self.dar_pista(juego)