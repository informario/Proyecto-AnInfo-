from dificultad import Dificultad

def main():

    dificultad = Dificultad(["a", "b", "c"], 7, 3)

    print(f"Palabras: {dificultad.get_palabras()}")
    print(f"Intentos: {dificultad.get_intentos()}")
    print(f"Pistas: {dificultad.get_pistas()}")

    print(f"Quedan intentos: {dificultad.quedan_intentos()}")
    print(f"Quedan pistas: {dificultad.quedan_pistas()}")

    return 0

main()