from user_statistics import UserStatistics
import random

CLUE_COST = 2

class ClueHandler:
    
    def buy_clue(self, user_statistics):
        if user_statistics.get_score() < CLUE_COST:
            print("\nNo tienes suficientes puntos para comprar una pista\n")
            return
        
        user_statistics.increase_basic_clues()
        user_statistics.decrease_score(CLUE_COST)
        print("\nCompraste una pista!\n")

    def use_clue(self, user_statistics, letters_to_guess, letters_guessed):
        if len(letters_to_guess) <= 1:
            print("\nTe queda solo una letra, no podes usar la pista!\n")
            return

        if user_statistics.get_basic_clues() <= 0:
            print("\nNo tienes pistas para usar\n")
            return

        clue = random.choice(letters_to_guess)
        letters_to_guess.remove(clue)
        letters_guessed.append(clue)
        user_statistics.decrease_basic_clues()

    # def give_clue(self, user_statistics, letters_to_guess, letters_guessed):
    #     if len(letters_to_guess) <= 1:
    #         print("\nTe queda solo una letra, no podes usar la pista!\n")
    #         return

    #     if not self.buy_clue(user_statistics):
    #         return

    #     self.use_clue(user_statistics, letters_to_guess, letters_guessed)
    #     print("\nPista obtenida\n")
            
    