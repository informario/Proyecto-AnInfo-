import unittest
from unittest.mock import patch
from io import StringIO

def print_status(adivino: bool, intentos: int, pistas: int, letras_adivinadas: list):
    """
    Imprime el estado actual del juego, proporcionando información sobre si se adivinó la letra,
    la cantidad de intentos restantes, pistas restantes, letras adivinadas y un mensaje adicional.

    Parametros:
    - adivino (bool): True si se adivinó la letra, False de lo contrario.
    - intentos (int): La cantidad de intentos restantes.
    - pistas (int): La cantidad de pistas restantes.
    - letras_adivinadas (list): Lista de letras que se han adivinado.
    """
    
    if adivino:
        print("BIEN!")
    else:
        print("MAL AHI")
    print(f"Intentos restantes: {intentos}")
    print(f"Pistas restantes: {pistas}")
    print(f"Letras adivinadas: {letras_adivinadas}")
    print("Printeo el ahorcado") #4

class TestPrintStatus(unittest.TestCase):

    def test_print_status_adivino_true(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_status(True, 3, 2, ['a', 'b', 'c'])
            expected_output = "BIEN!\nIntentos restantes: 3\nPistas restantes: 2\nLetras adivinadas: ['a', 'b', 'c']\nPrinteo el ahorcado\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_status_adivino_false(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print_status(False, 1, 0, ['a', 'n', 'i', 'n', 'f', 'o'])
            expected_output = "MAL AHI\nIntentos restantes: 1\nPistas restantes: 0\nLetras adivinadas: ['a', 'n', 'i', 'n', 'f', 'o']\nPrinteo el ahorcado\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
