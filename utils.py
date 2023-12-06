import os
try:
    from unidecode import unidecode
except ImportError:
    print("El modulo unidecode no esta instalado, por favor instalelo con el comando 'pip install unidecode'")
    exit()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Quitamos las tildes de las vocales y nos quedamos con la ñ
def remove_accent_marks(string):
    result = unidecode(string)
    
    if 'ñ' in string:
        result = result.replace('n', 'ñ', 1)
    return result