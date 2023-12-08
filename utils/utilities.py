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

def normalize(word):
    return list(set(filter(lambda x: x != " ", remove_accent_marks(word.lower()))))

def score_padding(score):
    if score < 10:
        return "    "
    elif score < 100:
        return "   "
    elif score < 1000:
        return "  "
    elif score < 10000:
        return " "
    else:
        return ""
    
def difficulty_padding(difficulty):
    if difficulty == "FACIL":
        return "  "
    elif difficulty == "MEDIA":
        return "  "
    elif difficulty == "DIFICIL":
        return " "
    else:
        return "   "