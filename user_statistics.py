
INITIAL_SCORE = 0

class UserStatistics:

    def __init__(self):
        self.score = INITIAL_SCORE
        self.basic_clues = 0
        self.bonus_clues = 0

    def get_score(self):
        return self.score

    def get_basic_clues(self):
        return self.basic_clues

    def increase_score(self, difficulty):
        self.score += difficulty.get_score()

    def decrease_score(self, amount):
        self.score -= amount

    def increase_basic_clues(self):
        self.basic_clues += 1

    def decrease_basic_clues(self):
        self.basic_clues -= 1
    