def imprimir_victoria():
    ahorcado = [
        "   ___________ ",
        "   |         |",
        "   |         O ",
        "   |        /|\\",
        "   |        / \\",
        "   |           ",
        "   |            ",
        "  _|_   P A L A B R A"
    ]

    for linea in ahorcado:
        print(linea)

    print("")

    mensaje = [
        "  {}{}{}    {}{}{}   {}    {}   {}{}{}   {}{}{}  {}{}{}{}{}  {}{}{}",
        "  {}        {}    {}  {}{}  {}  {}    {}  {}          {}      {}    ",
        "  {}  {}{}  {}{}{}{}  {} {} {}  {}{}{}{}  {}{}{}      {}      {}{}{}",
        "  {}    {}  {}    {}  {}  {}{}  {}    {}      {}      {}      {}    ",
        "    {}{}    {}    {}  {}    {}  {}    {}  {}{}{}      {}      {}{}{}",
    ]

    for linea in mensaje:
        print(linea)

    print("")

    print("  Presione ENTER para volver al menu principal")
    input("  Input: ")

def imprimir_derrota():
    ahorcado = [
        "   ___________ ",
        "   |         |",
        "   |        _O_",
        "   |        /|\\",
        "   |        / \\",
        "   |           ",
        "   |            ",
        "  _|_   P A L A B R A"
    ]

    for linea in ahorcado:
        print(linea)

    print("")

    mensaje = [
        "  {}{}{}   {}{}{}  {}{}{}    {}{}{}    {}  {}{}{}  {}{}{}{}{}  {}{}{}",
        "  {}   {}  {}      {}    {}  {}    {}      {}          {}      {}    ",
        "  {}{}{}   {}{}{}  {}{}{}    {}    {}  {}  {}{}{}      {}      {}{}{}",
        "  {}       {}      {}  {}    {}    {}  {}      {}      {}      {}    ",
        "  {}       {}{}{}  {}   {}   {}{}{}    {}  {}{}{}      {}      {}{}{}"
    ]

    for linea in mensaje:
        print(linea)

    print("")

    print("  Presione ENTER para volver al menu principal")
    input("  Input: ")

def imprimir_1():
    ahorcado = [
        "   ___________ ",
        "   |         |           Dificultad: Facil",
        "   |         O",
        "   |        /|\\",
        "   |        / \\",
        "   |           ",
        "   |            ",
        "  _|_    _ _ _ _ _"
    ]

    for linea in ahorcado:
        print(linea)

    print("")
    print("  Intentos restantes: 3")
    print("  Pistas restantes: 3")
    print("  Letras erroneas ya mencionadas: ...")
    print("")
    print("  0. Volver al menu principal")
    print("  1. Pista")
    print("")
    print("  Ingrese una letra o palabra")
    print("")
    input("  Input: ")

def imprimir_2():
    print("")
    print("  Presione un numero para seleccionar la dificultas o volver al menu principal")
    print("")
    print("  1. Facil:   7 intentos, 3 pistas y palabras cortas")
    print("  2. Medio:   5 intentos, 1 pista y palabras o frases normales")
    print("  3. Dificil: 3 intentos, sin pistas y palabras o frases largas")
    print("  4. Volver al menu principal")
    print("")
    input("  Input: ")

def imprimir_3():
    print("")
    print("  Reglas...")
    print("")
    print("  Presione ENTER para volver al menu principal")
    input("  Input: ")

def imprimir_menu():

    titulo = [
        "   {}{}{}   {}    {}   {}{}   {}{}{}   {}{}{}   {}{}{}   {}{}{}     {}{}",
        "  {}    {}  {}    {}  {}  {}  {}   {}  {}      {}    {}  {}    {}  {}  {}",
        "  {}{}{}{}  {}{}{}{}  {}  {}  {}{}{}   {}      {}{}{}{}  {}    {}  {}  {}",
        "  {}    {}  {}    {}  {}  {}  {}  {}   {}      {}    {}  {}    {}  {}  {}",
        "  {}    {}  {}    {}   {}{}   {}   {}  {}{}{}  {}    {}  {}{}{}     {}{}"
    ]

    print("")

    for linea in titulo:
        print(linea)

    print("")

    ahorcado = [
        "   ___________",
        "   |         |",
        "   |         O",
        "   |        /|\\",
        "   |        / \\",
        "  _|_"
    ]

    for linea in ahorcado:
        print(linea)

    print("")

    print("  1. Empezar partida")
    print("  2. Seleccionar nivel de dificultad")
    print("  3. Reglas del juego")
    print("  4. Salir")
    print("")
    input("  Input: ")

# imprimir_menu()

# imprimir_1()
# imprimir_2()
# imprimir_3()
# imprimir_derrota()
# imprimir_victoria()