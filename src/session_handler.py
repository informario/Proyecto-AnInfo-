import json
from getpass import getpass
from utils.utilities import clear_screen
from src.difficulty import Difficulty

INITIAL_SCORE = 0
INITIAL_BASIC_CLUES = 0
INITIAL_BONUS_CLUES = 0

INDEX_SCORE = 0
INDEX_BASIC_CLUES = 1
INDEX_BONUS_CLUES = 2

LOGIN_SESSION_OPT = "1"
REGISTER_OPT = "2"
EXIT_OPT = "3"
SESSIONS_FILE = "utils/sessions.json"

class SessionHandler:
    
    def __init__(self, file_name = SESSIONS_FILE):
        self.file_name = file_name
        self.sessions = self.load_sessions()

    def register_user(self, user_name):
        """
        Registra un nuevo usuario.
        Verifica que el nombre de usuario no este siendo utilizado. 
        
        Parametros:
        - user_name: Nombre de usuario a crear.

        Retorna:
        - Devuelve una tupla con el nombre de usuario y el puntaje si se pudo registrar correctamente. 
        - En caso de que el nombre de usuario este siendo utilizado devuelve None.
        """
        
        if user_name not in self.sessions:
            self.sessions[user_name] = [INITIAL_SCORE, INITIAL_BASIC_CLUES, INITIAL_BONUS_CLUES]
            self.save_sessions()
            return (user_name, self.sessions[user_name])
        
        return None, None

    def search_user(self, user_name):
        """
        Busca al usuario cuyo nombre se recibe como parametro.

        Parametros:
        - user_name: Nombre de usuario.

        Retorna:
        - Devuelve una tupla con el nombre de usuario y su puntaje si se encontro correctamente.
        - En caso de que el nombre de usuario no se encuentre devuelve None.
        """

        if user_name in self.sessions:
            return (user_name, self.sessions[user_name])
        
        return None, None

    def load_sessions(self):
        """
        Carga las sesiones.
        En caso de no existir el archivo lo crea.

        Parametros:
        - file_name: Nombre del archivo

        Retorna:
        - Devuelve un diccionario que almacena el contenido del archivo.
        """

        try:
            with open(self.file_name, 'r') as f:
                return json.load(f)
            
        except FileNotFoundError:
            self.sessions = {}

            with open(self.file_name, 'w') as f:
                json.dump(self.sessions, f)

            return self.sessions

    def save_sessions(self):
        """
        Guarda las sesiones.
        """

        with open(self.file_name, 'w') as f:
            json.dump(self.sessions, f)
        
    def update(self, user_name, user_stats):
        """
        Actualiza el puntaje de un usuario.

        Parametros:
        - user_name: Nombre de usuario.
        - score: Puntaje.

        Retorna:
        - Devuelve un booleano indicando si los puntos se actualizaron con exito o no.
        """

        if user_name in self.sessions:
            self.sessions[user_name][INDEX_SCORE] = user_stats.score
            self.sessions[user_name][INDEX_BASIC_CLUES] = user_stats.basic_clues
            self.sessions[user_name][INDEX_BONUS_CLUES] = user_stats.bonus_clues
            self.save_sessions()
            return True
        
        return False

    def run(self):
        clear_screen()

        while True:
            print("\nOpciones:\n")
            print("\t1 - Iniciar sesion\n")
            print("\t2 - Registrarse\n")
            print("\t3 - Salir\n")

            inp = input("\nElige una opcion: ").strip()

            if inp == LOGIN_SESSION_OPT:
                user_name, user_info = self.login_menu()

                if user_name is None:
                    clear_screen()
                    continue
                
                clear_screen()
                return user_name, user_info[INDEX_SCORE], user_info[INDEX_BASIC_CLUES], user_info[INDEX_BONUS_CLUES]
            elif inp == REGISTER_OPT:
                user_name, user_info = self.reg_menu()

                if user_name is None:
                    clear_screen()
                    continue
            
                clear_screen()
                return user_name, user_info[INDEX_SCORE], user_info[INDEX_BASIC_CLUES], user_info[INDEX_BONUS_CLUES]
            
            elif inp == EXIT_OPT:
                return None, None
            
            else:
                clear_screen()
                print("Opcion incorrecta\n")
            


    def welcome_user_print(self,user_name, user_info):
        clear_screen()
        print(f"\n¡Bienvenido {user_name}!\n")
        print("__________________________________________________________________________________")
        print(f"Tu puntaje es: {user_info[INDEX_SCORE]}")
        print(f"Tu cantidad de pistas simples: {user_info[INDEX_BASIC_CLUES]}")
        print(f"Tu cantidad de pistas bonus:   {user_info[INDEX_BONUS_CLUES]}")
        print("__________________________________________________________________________________")
        print("\nPresione ENTER para comenzar el juego")
        getpass(prompt="")

    def login_menu(self):
        clear_screen()
        print("\n")
        while True:
            print("\nINICIAR SESION")
            print("--------------\n")

            print("Ingrese su nombre de usuario " \
            "o presione ENTER si desea volver al menu principal")
            print("\n")
            inp = input("username: ").strip()
            if inp == "":
                return None, None
            
            user_name, user_info = self.search_user(inp)

            if user_name is None:
                clear_screen()
                print("Nombre de usuario no registrado. Por favor intente de nuevo o regístrese.")
                print("__________________________________________________________________________________")
                continue
            else:
                print("\n") 
                break

        self.welcome_user_print(user_name, user_info)
        
        return user_name, user_info
    
    def reg_menu(self):
        clear_screen()
        print("\n")

        
        while True:
            print("\nREGISTRARSE")
            print("-----------\n")  
            print("Ingrese un nombre de usuario para registrarse "\
            "o presione ENTER si desea volver al menu principal")
            print("\n")
            new_user_name = input("username: ").strip()
            if new_user_name == "":
                return None, None
            
            user_name, user_info = self.register_user(new_user_name)
            if user_name == None:
                clear_screen()
                print("El nombre de usuario ingresado ya está en uso. Por favor intente de nuevo.")
                print("__________________________________________________________________________________")
                continue
            else:
                print("\n")
                break
                
        self.welcome_user_print(user_name, user_info)
        return user_name, user_info
        
            
