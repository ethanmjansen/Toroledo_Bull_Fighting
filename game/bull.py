import random

class Bull():
    """Abstract Bull Class"""
    
    def __init__(self, name=None, P=None, S=None, Q=None, L=None):
        self.name = name
        
        # Stats
        self.PSQL = [P, S, Q, L]
        self.altPSQL = [P, S, Q, L]

        # Statuses
        self.statuses = ['great', 'good', 'mild_good', 'mild_bad', 'bad', 'worst']
        self.great = ['Excellent', 'Healthy', 'Sound', 'Grade A', 'Strong']
        self.good = ['Robust', 'Rested', 'Fit', 'Virile', 'Ready']
        self.mild_good = ['Agile', 'Kosher', 'Secure']
        self.mild_bad = ['So-so',  'Capable', 'Normal']
        self.bad = ['Ailing', 'Listless', 'Serious', 'Shaky', 'Frail']
        self.worst = ['Sickly', 'Ragged', 'Gloomy', 'Drowsy', 'Feeble']

    def pick_status(self):
        """Pick a status and modify PSQL"""
        # Make a choice
        choice = random.choice(self.statuses)
        # Update status and give PSQL modifiers
        if choice == self.statuses[0]:
            self.altPSQL = [i + 3 for i in self.PSQL]
            self.status = random.choice(self.great)
        elif choice == self.statuses[1]:
            self.altPSQL = [i + 2 for i in self.PSQL]
            self.status = random.choice(self.good)
        elif choice == self.statuses[2]:
            self.altPSQL = [i + 1 for i in self.PSQL]
            self.status = random.choice(self.mild_good)
        elif choice == self.statuses[3]:
            self.altPSQL = [i - 1 for i in self.PSQL]
            self.status = random.choice(self.mild_bad)
        elif choice == self.statuses[4]:
            self.altPSQL = [i - 2 for i in self.PSQL]
            self.status = random.choice(self.bad)
        else:
            self.altPSQL = [i - 3 for i in self.PSQL]
            self.status = random.choice(self.worst)
        
        return self.PSQL, self.altPSQL

    def __str__(self):
        """Proof of Concept function"""
        return f"Bull Name: {self.name},\nPSQL: {self.PSQL},\nStatus: {self.status},\naltPSQL: {self.altPSQL}"


if __name__ == "__main__":
    """Proof of Concept"""
    bull = Bull('Lao', 9, 8, 9, 8)
    bull.pick_status()
    print(bull)
