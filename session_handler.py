import json
from getpass import getpass
from utils import clear_screen
from difficulty import Difficulty

INITIAL_SCORE = 0
INITIAL_CLUE = 0

INDEX_SCORE = 0
INDEX_CLUE = 1

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
            self.sessions[user_name] = [INITIAL_SCORE, INITIAL_CLUE]
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
        
    def update(self, user_name, score, clue):
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
            self.sessions[user_name][INDEX_CLUE] = clue
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
                user_name, score = self.login_menu()

                if user_name is None:
                    clear_screen()
                    continue
                
                return user_name, score
            
            elif inp == EXIT_OPT:
                return None, None
            
            else:
                clear_screen()
                print("Opcion incorrecta\n")

    def login_menu(self):
        clear_screen()
        print("Iniciando sesion")

        inp = input("\nIngrese su nombre de usuario: ").strip()
        user_name, score = self.search_user(inp)

        if user_name is None:
            user_name, score = self.register_user(inp)
    
        clear_screen()
        print(f"Bienvenido {user_name}.")
        print(f"Tu puntaje es: {self.sessions[user_name][INDEX_SCORE]}.")
        print(f"Tu cantidad de pistas es: {self.sessions[user_name][INDEX_CLUE]}. ")
        print("\nPresione ENTER para comenzar el juego")
        getpass(prompt="")
        return user_name, score
    
    def get_score(self, user_name):
        """
        Obtiene el puntaje asociado a un usuario en la sesión actual.

        Parametros:
        - user_name (str): El nombre del usuario.

        Retorna:
        - int: El puntaje actual del usuario.
        """
        return self.sessions[user_name][INDEX_SCORE]

    def deduct_score_on_loss(self, user_name, difficulty: Difficulty):
        """
        Reduce el puntaje del usuario en función de la dificultad proporcionada, en caso de pérdida en la partida.

        Parametros:
        - user_name (str): El nombre del usuario al que se le va a deducir el puntaje.
        - difficulty (Difficulty): La dificultad de la partida, que determina la cantidad de puntos a deducir.
        """
        score = self.get_score(user_name)
        deduction_points = difficulty.get_deduction_points()
        current_score = score - deduction_points
        if current_score < 0:
            current_score = 0
        self.update(user_name, current_score, self.sessions[user_name][INDEX_CLUE])
