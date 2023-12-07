from difficulty import Difficulty
from options.menu import ExitGameException
from state import GameState
from options.game import GameOpt
from utils import clear_screen, remove_accent_marks
from clue_handler import ClueHandler
import random
import getpass

class HangmanGame:

    def __init__(self, difficulty, user_statistics, word_category):
        self.category = word_category
        self.attempts_remaining = difficulty.get_max_attempts()
        self.word, self.clue = difficulty.get_word(word_category)
        self.score = difficulty.get_winning_score()
        self.clue_used = False
        self.letters_to_guess = list(set(filter(lambda x: x != " ", remove_accent_marks(self.word.lower()))))
        self.letters_guessed = []
        self.letters_missed = []
        self.state = GameState.RUNNING
        self.remaining_clues = difficulty.get_clues()
        self.clue_handler = ClueHandler.from_stats(user_statistics)

    def update_stats(self, user_statistics):
        user_statistics.update_from_clues(self.clue_handler)
    
    def update_score(self, user_statistics, difficulty):
        self.state.update_score(user_statistics, difficulty)
        
    def running(self):
        return self.state == GameState.RUNNING
    
    def print_word(self):
        if self.running():
            for letter in self.word:
                if remove_accent_marks(letter.lower()) in self.letters_guessed:
                    print(letter, end=" ")
                elif letter == " ":
                    print(" ", end=" ")
                else:
                    print("_", end=" ")

            return
        
        for letter in self.word:
            print(letter, end=" ")
    
    def print_state(self):
        
        print("=========================================")
        print("Categoria: ", self.category.to_string())
        print("Intentos restantes: ", self.attempts_remaining)
        print("Letras adivinadas: ", self.letters_guessed)
        print("Letras erradas: ", self.letters_missed)
        print("Puntos de ayuda restantes: ", self.remaining_clues)
        print("Pistas de revelacion de letra disponibles: ", self.clue_handler.get_basic_clues())
        print("PUNTAJE: ", self.clue_handler.get_score())
        if self.clue_used:
            print("AYUDA: ", self.clue)

        self.print_word()
        print("\n")
        self.state.print()
        if self.state == GameState.WON:
            print(f"¡Obtuviste {self.score} puntos!")
        print("=========================================")


    def try_to_guess_letter(self,letter):
        if letter in self.letters_guessed:
            print("\nYa adivinaste esta letra, vuelve a intentarlo\n")
            return
        if letter in self.letters_missed:
            print("\nYa intentaste con esta letra, vuelve a intentarlo\n")
            return
        
        if letter in self.letters_to_guess:
            print("\nAdivinaste una letra!\n")   
            self.letters_to_guess.remove(letter)
            self.letters_guessed.append(letter)
            
        else:
            print("\nLetra incorrecta, vuelve a intentarlo\n")
            self.attempts_remaining -= 1
            self.letters_missed.append(letter)

        if len(self.letters_to_guess) == 0:
            self.state = GameState.WON
        if self.attempts_remaining == 0:
            self.state = GameState.LOST
    
    def try_to_guess_word(self, word):
        
        if word == remove_accent_marks(self.word.lower()):
            print("\nAdivinaste la palabra!\n")
            self.state = GameState.WON
            self.letters_guessed += self.letters_to_guess
        else:
            print("\nPalabra incorrecta\n")
            self.attempts_remaining -= 1

        if self.attempts_remaining == 0:
            self.state = GameState.LOST

    def use_clue(self):
        self.clue_handler.use_clue(self.letters_to_guess, self.letters_guessed)

    def buy_clue(self):
        self.clue_handler.buy_clue()

    def give_help(self):
        if self.remaining_clues < 2:
            print("\nNo te quedan suficientes pistas para que te demos una ayuda!\n")
            return

        if self.clue_used:
            print("\nYa te dimos una pista!\n")
            return

        print("\nAyuda obtenida\n")
        self.clue_used = True
        self.remaining_clues -= 2

    def is_abandoned():
        print("\n¿Estas seguro de que deseas abandonar la partida?\n")
        print("0. Si")
        print("1. No\n")
        inp = input("- ")
        if inp == "1":
            return False
        
        return True
        
    def show_options():
        print("0. Abandonar partida")
        print("1. Revelar una letra")
        print("2. Comprar una pista de revelacion de letra")
        print("3. Pedir una pista")
        print("Ingrese una letra para continuar jugando\n")

    def end():

        print("\nPresione ENTER para volver al menu principal\n")
        getpass.getpass(prompt="")


    def try_to_guess(self, inp):
        if len(inp) > 1:
            self.try_to_guess_word(inp)
            return
        self.try_to_guess_letter(inp) 

    def invalid_input(inp):
        return len(inp) == 0    
        # Más adelante seguramente hagamos otras validaciones, por eso la funcion
        # como por ejemplo que no se pueda ingresar un numero distinto de 0, 1 o 2 

    def is_won(self):
        return self.state == GameState.WON

    def play(self):
        while self.running():
            HangmanGame.show_options()
            inp = input("Intento: ").lower().strip()
            clear_screen()
            if HangmanGame.invalid_input(inp):
                print("\nEl caracter ingresado no es válido, vuelve a intentarlo\n")
                continue

            opcion = GameOpt.from_input(inp)
            if opcion == None:
                self.try_to_guess(inp) 
                self.print_state()
                continue
            
            try:
                opcion.execute(self)      
            except ExitGameException:
                return

            self.print_state()
        
        HangmanGame.end()

    # Devuelve el estado final del juego
    def run(self):
        clear_screen()
        print("\nBienvenido al juego del Ahorcado!\n")                                                                        
        self.print_state()
        self.play()

        


