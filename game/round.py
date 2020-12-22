import random
from bull_pen import make_bulls

def d20():
    # Rolls a D20
    return random.randint(0,20)

def d4():
    # Rolls a D4
    return random.randint(0,4)

class Round():
    """Abstract Round class"""

    def __init__(self, bull_1, bull_2):
        self.bull_1 = bull_1
        self.bull_2 = bull_2

    def initiative(self):
        # Who attacks first
        bull_1_initiative = d20() + self.bull_1.altPSQL[2] + self.bull_1.altPSQL[3]
        bull_2_initiative = d20() + self.bull_2.altPSQL[2] + self.bull_2.altPSQL[3]

        if bull_1_initiative > bull_2_initiative:
            self.attacker = self.bull_1
            self.defender = self.bull_2
        else:
            self.attacker = self.bull_2
            self.defender = self.bull_1

    def attack(self, bull):
        # Attack chance
        offense = d20() + bull.altPSQL[0]
        return offense

    def defend(self, bull):
        # Defense chance
        defense = d20() + bull.altPSQL[1]
        return defense

    def fight(self):
        # If a bull's stamina is already zero
        if self.bull_2.altPSQL[1] < 1:
            self.winner = self.bull_1
            self.loser = self.bull_2
            print(f'{self.bull_2.name} trips on the way to the fight and is hospitalized')
        elif self.bull_1.altPSQL[1] < 1:
            self.winner = self.bull_2
            self.loser = self.bull_1
            print(f'{self.bull_1.name} trips on the way to the fight and is hospitalized')
        
        # Main fight loop
        while self.bull_1.altPSQL[1] > 0 and self.bull_2.altPSQL[1] > 0:

            self.initiative()

            offense = self.attack(self.attacker)
            defense = self.defend(self.defender)
            
            if offense > defense:
                damage = d4()
                self.defender.altPSQL[1] -= damage

            print(f'{self.bull_1.name} health: {self.bull_1.altPSQL[1]}, {self.bull_2.name} health: {self.bull_2.altPSQL[1]}')
        

        # Determine winner after loop

        if self.bull_1.altPSQL[1] > self.bull_2.altPSQL[1]:
            self.winner = self.bull_1
            self.loser = self.bull_2
        else:
            self.winner = self.bull_2
            self.loser = self.bull_1       
        
        return self.winner  

    def __str__(self):
        return f'{self.bull_1},\n{self.bull_2}'

if __name__ == "__main__":
    "Proof of Concept"
    bulls = make_bulls()
    bull_1 = random.choice(list(bulls.values()))
    bull_2 = random.choice(list(bulls.values()))
    match = Round(bull_1, bull_2)
    print(match)
    match.fight()
