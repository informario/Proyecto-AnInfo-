INITIAL_SCORE = 0
INITIAL_CLUES = 0
INITIAL_BONUS_CLUES = 0
CLUE_COST = 2
HINT_COST = 10

class UserStatistics:

    def __init__(self, score = INITIAL_SCORE, basic_clues = INITIAL_CLUES, bonus_clues =  INITIAL_BONUS_CLUES):
        self.score = score
        self.basic_clues = basic_clues
        self.bonus_clues = bonus_clues

    def get_score(self):
        return self.score

    def get_basic_clues(self):
        return self.basic_clues

    def get_bonus_clues(self):
        return self.bonus_clues

    def increase_score(self, difficulty):
        self.score += difficulty.get_winning_score()

    def decrease_score(self, difficulty):
        self.score -= difficulty.get_losing_score()
        if self.score < 0:
            self.score = 0
    
    def decrease_score_amount(self, amount):
        self.score -= amount
        if self.score < 0:
            self.score = 0

    def increase_basic_clues(self):
        self.basic_clues += 1

    def decrease_basic_clues(self):
        self.basic_clues -= 1

    def increase_bonus_clues(self):
        self.bonus_clues += 1

    def decrease_bonus_clues(self):
        self.bonus_clues -= 1

    def update_from_clues(self, clue_handler):
        self.basic_clues = clue_handler.get_basic_clues()
        self.score = clue_handler.get_score()
        self.bonus_clues = clue_handler.get_bonus_clues()

    def buy_basic_clue(self):
        if self.get_score() < CLUE_COST:
            print("\nNo tienes suficientes puntos para comprar una pista simple!")
            return
        
        self.increase_basic_clues()
        self.decrease_score_amount(CLUE_COST)
        print("\nCompraste una pista simple!\n")

    def buy_bonus_clue(self):
        if self.get_score() < HINT_COST:
            print("\nNo tienes suficientes puntos para comprar una pista bonus!")
            return
        
        self.increase_bonus_clues()
        self.decrease_score_amount(HINT_COST)
        print("\nCompraste una pista bonus!\n")

    