from bull_pen import make_bulls
import random
from round import Round

class Tournament():
    """Abstract Tournament Class"""
    
    def __init__(self, bulls):
        self.bulls = bulls

    def make_bracket(self):
        bracket = []

        for bull in self.bulls.keys():
            bracket.append(bull)

        random.shuffle(bracket)
        self.bracket = bracket[0:8]

        return self.bracket

    def elite_eight(self):
        round_1 = Round(self.bulls[self.bracket[0]], self.bulls[self.bracket[1]])
        round_2 = Round(self.bulls[self.bracket[2]], self.bulls[self.bracket[3]])
        round_3 = Round(self.bulls[self.bracket[4]], self.bulls[self.bracket[5]])
        round_4 = Round(self.bulls[self.bracket[6]], self.bulls[self.bracket[7]])
        
        winner_1 = round_1.fight()
        winner_2 = round_2.fight()
        winner_3 = round_3.fight()
        winner_4 = round_4.fight()

        self.bracket = []
        self.bracket.append(winner_1.name)
        self.bracket.append(winner_2.name)
        self.bracket.append(winner_3.name)
        self.bracket.append(winner_4.name)
        print('\n')
        return self.bracket

    def final_four(self):
        round_1 = Round(self.bulls[self.bracket[0]], self.bulls[self.bracket[1]])
        round_2 = Round(self.bulls[self.bracket[2]], self.bulls[self.bracket[3]])
        
        winner_1 = round_1.fight()
        winner_2 = round_2.fight()

        self.bracket = []
        self.bracket.append(winner_1.name)
        self.bracket.append(winner_2.name)
        print('\n')
        return self.bracket
    
    def championship(self):
        round_1 = Round(self.bulls[self.bracket[0]], self.bulls[self.bracket[1]])
        
        winner_1 = round_1.fight()

        self.bracket = []
        self.bracket.append(winner_1.name)
        print('\n')
        return self.bracket

if __name__ == "__main__":
    bulls = make_bulls()
    tournament = Tournament(bulls)
    print(tournament.make_bracket())
    print(tournament.elite_eight())
    print(tournament.final_four())
    print(tournament.championship())
