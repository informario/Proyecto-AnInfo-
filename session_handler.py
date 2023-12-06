import json
from getpass import getpass
from utils import clear_screen

INITIAL_SCORE = 0

LOGIN_SESSION_OPT = "1"
REGISTER_SESSION_OPT = "2"
EXIT_OPT = "3"

class SessionHandler:
    
    def __init__(self, file_name = "sessions.json"):
        self.file_name = file_name
        self.sessions = self.load_sessions()

    def register_session(self, user_name):
        """
        Registra la sesion de un nuevo usuario.
        Verifica que el usuario no este registrado antes de hacerlo. 
        
        Parametros:
        - user_name: Nombre de usuario a crear.

        Retorna:
        - Devuelve el nombre de usuario y el puntaje si se pudo iniciar sesion correctamente. En caso contrario devuelve None.
        """
        
        if user_name not in self.sessions:
            self.sessions[user_name] = INITIAL_SCORE
            self.save_sessions()
            return (user_name, self.sessions[user_name])
        
        return None, None

    def login_session(self, user_name):
        """
        Iniciar sesion.

        Parametros:
        - user_name: Nombre de usuario.

        Retorna:
        - Devuelve el nombre de usuario y el puntaje si se pudo iniciar sesion correctamente. En caso contrario devuelve None.
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
        
    def update_points(self, user_name, score):
        """
        Actualiza el puntaje de un usuario.

        Parametros:
        - user_name: Nombre de usuario.
        - score: Puntaje.

        Retorna:
        - Devuelve un string indicando si el usuario ingreso con exito o no.
        """

        if user_name in self.sessions:
            self.sessions[user_name] = score
            self.save_sessions()
            return f"Puntos actualizados correctamente."
        else:
            return f"Usuario no resgistrado."

    def run(self):
        clear_screen()

        while True:
            print("Opciones:")
            print("\t1 - Iniciar sesion")
            print("\t2 - Registrarse")
            print("\t3 - Salir")

            inp = input("\nElige una opcion: ").strip()

            if inp == LOGIN_SESSION_OPT:
                user_name, score = self.log_in()

                if user_name is None:
                    clear_screen()
                    continue
                
                return user_name, score

            elif inp == REGISTER_SESSION_OPT:
                self.sign_up()
                clear_screen()
            elif inp == EXIT_OPT:
                return None, None
            else:
                clear_screen()
                print("Opcion incorrecta\n")

    def log_in(self):
        while True:
            clear_screen()
            print("Iniciando sesion")

            inp = input("\nIngrese su nombre de usuario: ").strip()
            user_name, score = self.login_session(inp)
            clear_screen()
        
            if user_name is None:
                print(f"Usuario no registrado. Por favor, registrese para continuar.")
                print("\nPresione ENTER para volver al menu de loggeo")
                getpass(prompt="")
                return user_name, score

            print(f"Bienvenido de nuevo {user_name}. Tu puntaje es: {self.sessions[user_name]}.")
            print("\nPresione ENTER para comenzar el juego")
            getpass(prompt="")
            return user_name, score

    def sign_up(self):
        while True:
            clear_screen()
            print("Registrandose")

            inp = input("\nIngrese su nombre de usuario: ").strip()
            user_name, score = self.register_session(inp)
            clear_screen()
        
            if user_name is None:
                print(f"El nombre de usuario ya existe. Por favor, use otro nombre para registrarse.")
                print("\nPresione ENTER para volver a intentarlo")
                getpass(prompt="")
                continue

            print(f"Usuario registrado correctamente. Tu puntaje inicial es: {INITIAL_SCORE}.")
            print("\nPresione ENTER para volver al menu de loggeo")
            getpass(prompt="")
            return user_name, score

# session_handler = SessionHandler()

# user_name, puntaje = session_handler.run()

# print(f"Nombre de usuario: {user_name} - Puntaje: {puntaje}")