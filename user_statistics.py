INITIAL_SCORE = 0
INITIAL_CLUES = 0
INITIAL_HINT_CLUES = 0
CLUE_COST = 2
HINT_COST = 10

class UserStatistics:

    def __init__(self, score = INITIAL_SCORE, basic_clues = INITIAL_CLUES, hint_clues =  INITIAL_HINT_CLUES):
        self.score = score
        self.basic_clues = basic_clues
        self.hint_clues = hint_clues

    def get_score(self):
        return self.score

    def get_basic_clues(self):
        return self.basic_clues

    def get_hint_clues(self):
        return self.hint_clues

    def increase_score(self, difficulty):
        self.score += difficulty.get_score()

    def decrease_score(self, amount):
        self.score -= amount

    def increase_basic_clues(self):
        self.basic_clues += 1

    def decrease_basic_clues(self):
        self.basic_clues -= 1

    def increase_hint_clues(self):
        self.hint_clues += 1

    def decrease_hint_clues(self):
        self.hint_clues -= 1

    def update_from_clues(self, clue_handler):
        self.basic_clues = clue_handler.get_basic_clues()
        self.score = clue_handler.get_score()
        self.hint_clues = clue_handler.get_hint_clues()

    def buy_basic_clue(self):
        if self.get_score() < CLUE_COST:
            print("\nNo tienes suficientes puntos para comprar una pista\n")
            return
        
        self.increase_basic_clues()
        self.decrease_score(CLUE_COST)
        print("\nCompraste una pista!\n")

    def buy_hint_clue(self):
        if self.get_score() < HINT_COST:
            print("\nNo tienes suficientes puntos para comprar una ayuda de palabra!\n")
            return
        
        self.increase_hint_clues()
        self.decrease_score(HINT_COST)
        print("\nCompraste una ayuda de palabra!\n")

    