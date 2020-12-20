from bull_pen import make_bulls
import random

class Tournament():
    def __init__(self, bulls):
        self.bulls = bulls

    def make_bracket(self):
        bracket = []

        for bull in bulls.keys():
            bracket.append(bull)

        random.shuffle(bracket)
        self.bracket = bracket[0:8]

        return self.bracket

    def elite_eight(self):
        pass

    def final_four(self):
        pass
    
    def championship(self):
        pass

if __name__ == "__main__":
    bulls = make_bulls()
    tournament = Tournament(bulls)
    print(tournament.make_bracket())

