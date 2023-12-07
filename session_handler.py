import json
from getpass import getpass
from utils import clear_screen

INITIAL_SCORE = 0
INITIAL_CLUES = 0
INITIAL_HINTS = 0

INDEX_SCORE = 0
INDEX_CLUES = 1
INDEX_HINTS = 2

LOGIN_SESSION_OPT = "1"
EXIT_OPT = "2"

class SessionHandler:
    
    def __init__(self, file_name = "sessions.json"):
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
            self.sessions[user_name] = [INITIAL_SCORE, INITIAL_CLUES, INITIAL_HINTS]
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
        
    def update(self, user_name, score, basic_clues, hint_clues):
        """
        Actualiza el puntaje de un usuario.

        Parametros:
        - user_name: Nombre de usuario.
        - score: Puntaje.

        Retorna:
        - Devuelve un booleano indicando si los puntos se actualizaron con exito o no.
        """

        if user_name in self.sessions:
            self.sessions[user_name][INDEX_SCORE] = score
            self.sessions[user_name][INDEX_CLUES] = basic_clues
            self.sessions[user_name][INDEX_HINTS] = hint_clues
            self.save_sessions()
            return True
        
        return False

    def run(self):
        clear_screen()

        while True:
            print("Opciones:")
            print("\t1 - Iniciar sesion")
            print("\t2 - Salir")

            inp = input("\nElige una opcion: ").strip()

            if inp == LOGIN_SESSION_OPT:
                user_name, user_info = self.login_menu()

                if user_name is None:
                    clear_screen()
                    continue
                
                return user_name, user_info[INDEX_SCORE], user_info[INDEX_CLUES], user_info[INDEX_HINTS]
            
            elif inp == EXIT_OPT:
                return None, None
            
            else:
                clear_screen()
                print("Opcion incorrecta\n")

    def login_menu(self):
        clear_screen()
        print("Iniciando sesion")

        inp = input("\nIngrese su nombre de usuario: ").strip()
        user_name, user_info = self.search_user(inp)

        if user_name is None:
            user_name, user_info = self.register_user(inp)
    
        clear_screen()
        print(f"Bienvenido {user_name}.")
        print(f"Tu puntaje es: {user_info[INDEX_SCORE]}.")
        print(f"Tu cantidad de pistas de revelacion de letra es: {user_info[INDEX_CLUES]}. ")
        print(f"Tu cantidad de pistas de ayuda de palabra es: {user_info[INDEX_HINTS]}. ")
        print("\nPresione ENTER para comenzar el juego")
        getpass(prompt="")
        return user_name, user_info
