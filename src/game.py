from src.difficulty import Difficulty
from options.menu import ExitGameException
from src.state import GameState
from options.game import GameOpt
from utils.utilities import clear_screen, normalize, remove_accent_marks, score_padding
from src.clue_handler import ClueHandler
import random
import getpass
import utils.api as api

class HangmanGame:

    def __init__(self, difficulty, user_statistics, word_category):
        self.category = word_category
        self.dificulty = difficulty
        self.attempts_remaining = difficulty.get_max_attempts()
        self.word, self.clue = difficulty.get_word(word_category)
        self.letters_to_guess = normalize(self.word)
        self.letters_guessed = []
        self.letters_missed = []
        self.state = GameState.RUNNING
        self.clue_handler = ClueHandler.from_stats(user_statistics)
        self.stick_man = api.DrawnHangman(difficulty)

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
        print("======================================================")
        print(f"\n----------------| Categoria: {self.category.to_string().upper()} |----------------\n")
        print(f"                  Dificultad: {self.dificulty.to_string()}\n")
        print(f"Intentos restantes: {self.attempts_remaining}    |    Pistas simples: {self.clue_handler.get_basic_clues()}")
        print(f"PUNTAJE:            {self.clue_handler.get_score()}{score_padding(self.clue_handler.get_score())}|    "\
              f"Pistas bonus:   {self.clue_handler.get_bonus_clues()}\n")
        print("Letras adivinadas:  ", list_to_str(self.letters_guessed))
        print("Letras erradas:     ", list_to_str(self.letters_missed))
        if self.clue_handler.was_bonus_clue_used():
            print("Pista bonus: ", self.clue)

        self.stick_man.draw_hangman(self.attempts_remaining)

        self.print_word()
        print("\n\n")
        self.state.print()
        if self.state == GameState.WON:
            print(f"¡Obtuviste {self.dificulty.get_winning_score()} puntos!")
        if self.state == GameState.LOST:
            print(f"Se te descuentan {self.dificulty.get_losing_score()} puntos :(")
        print("\n======================================================")


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

    def use_basic_clue(self):
        self.clue_handler.use_basic_clue(self.letters_to_guess, self.letters_guessed)

    def buy_basic_clue(self):
        self.clue_handler.buy_basic_clue()

    def use_bonus_clue(self):
        self.clue_handler.use_bonus_clue()

    def buy_bonus_clue(self):
        self.clue_handler.buy_bonus_clue()

    def show_options():
        print("\n0. Abandonar partida")
        print("1. Usar pista simple")
        print("2. Usar pista bonus")
        print("3. Comprar pista simple (precio:  2 puntos)")
        print("4. Comprar pista bonus  (precio: 10 puntos)")
        print("\nIngrese una letra para continuar jugando\n")

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

    def is_won(self):
        return self.state == GameState.WON

    def play(self):
        while self.running():
            HangmanGame.show_options()
            inp = input("Intento: ").lower().strip()
            clear_screen()
            if HangmanGame.invalid_input(inp):
                print("\nEl caracter ingresado no es válido, vuelve a intentarlo\n")
                self.print_state()
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
        clear_screen()

    def run(self):
        clear_screen()
        print("\nBienvenido al juego del Ahorcado!\n")                                                                        
        self.print_state()
        self.play()

def list_to_str(list):
    return (" ").join(list)


