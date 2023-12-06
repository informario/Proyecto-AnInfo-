import json

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
        - Devuelve un string indicando si el usuario fue creado con exito o no.
        """
        
        if user_name not in self.sessions:
            self.sessions[user_name] = INITIAL_SCORE
            return f"Usuario registrado correctamente. Tu puntaje inicial es: {INITIAL_SCORE}."
        else:
            return f"El nombre de usuario ya existe. Por favor, use otro nombre para registrarse."

    def login_session(self, user_name):
        """
        Iniciar sesion.

        Parametros:
        - user_name: Nombre de usuario.

        Retorna:
        - Devuelve un string indicando si el usuario ingreso con exito o no.
        """

        if user_name in self.sessions:
            return f"Bienvenido de nuevo {user_name}. Tu puntaje es: {self.session[user_name]}"
        else:
            return f"Usuario no registrado. Por favor, registrese para continuar."

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
            self.sessions[user_name] += score
            return f"Puntos actualizados correctamente."
        else:
            return f"Usuario no resgistrado."
