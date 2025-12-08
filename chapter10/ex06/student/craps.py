import random

class Player:
    def __init__(self):
        self.roll = ""               # last roll as a string
        self.numberOfRolls = 0       # <-- test bunu bekliyor
        self.atStartup = True
        self.winner = False
        self.loser = False
        self.point = 0

    def rollDice(self):
        """Roll dice once and update the game state."""
        if self.winner or self.loser:
            return None

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        self.roll = f"({die1}, {die2}) total = {total}"
        self.numberOfRolls += 1      # <-- test bunu kontrol ediyor

        if self.atStartup:
            if total in (7, 11):
                self.winner = True
            elif total in (2, 3, 12):
                self.loser = True
            else:
                self.point = total
                self.atStartup = False
        else:
            if total == self.point:
                self.winner = True
            elif total == 7:
                self.loser = True

        return (die1, die2)

    def getNumberOfRolls(self):
        """Return the number of dice rolls made."""
        return self.numberOfRolls   # <-- test burada hata buluyordu

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser
