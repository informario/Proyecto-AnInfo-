def hola():
    print("¡Hola mundo!")
    print_status(False, 5, 3, ["a", "e", "i", "o", "u"])


def print_status(adivino: True, intentos: int, pistas: int, letras_adivinadas: list):
    if adivino:
        print("BIEN!")
    else:
        print("MAL AHI")
    print(f"Intentos restantes: {intentos}")
    print(f"Pistas restantes: {pistas}")
    print(f"Letras adivinadas: {letras_adivinadas}")
    print("Printeo el ahorcado") #4

hola()