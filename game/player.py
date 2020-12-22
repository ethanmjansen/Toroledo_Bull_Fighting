class Player():
    """Abstract player Class"""
    
    def __init__(self, purse):
        self.purse = purse
        self.win_streak = 0
        self.lose_streak = 0

    def bet(self, amount, bull_name):
        self.purse -= amount
        return f'You bet ${amount} on {bull_name}'

    def win(self, amount, bull_name):
        self.lose_streak = 0
        self.purse += amount
        self.win_streak += 1
        return f'You win ${amount} by betting on {bull_name}.'

    def lose(self, amount, bull_name):
        self.win_streak = 0
        self.purse -= amount
        self.lose_streak -= 1
        return f'You lose ${amount} by betting on {bull_name}.'

    def __str__(self):
        if self.win_streak >= 1:
            return f'You have ${self.purse} and a winning streak of {self.win_streak}.'
        elif self.lose_streak <= -1:
            return f'You have ${self.purse} and a losing streak of {self.lose_streak}.'
        else:
            return f"You have ${self.purse} and haven't bet on any bulls yet."

if __name__ == "__main__":
    """Proof of Concept"""
    player = Player(200)

    print(player)
    print(player.bet(10, 'Lao'))
    print(player.win(100, 'Lao'))
    print(player)
    print(player.win(200, 'T-Bone'))
    print(player)
    print(player.lose(150, 'Chips'))
    print(player)
