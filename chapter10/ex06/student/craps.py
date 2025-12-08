import random

class Player:
    def __init__(self):
        self.roll = ""               # Last roll's string representation
        self.rollsCount = 0          # Number of rolls made
        self.atStartup = True        # First roll?
        self.winner = False          # Has the player won?
        self.loser = False           # Has the player lost?
        self.point = 0               # Used after startup roll

    def rollDice(self):
        """Roll dice once, update game state, and return the tuple of dice values."""
        if self.winner or self.loser:
            return None   # Game already over

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        # Save roll info
        self.roll = f"({die1}, {die2}) total = {total}"
        self.rollsCount += 1

        # GAME LOGIC
        if self.atStartup:
            if total in (7, 11):
                self.winner = True
            elif total in (2, 3, 12):
                self.loser = True
            else:
                self.point = total
                self.atStartup = False
        else:
            # Subsequent rolls
            if total == self.point:
                self.winner = True
            elif total == 7:
                self.loser = True

        return (die1, die2)

    def getNumberOfRolls(self):
        return self.rollsCount

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser


# ---------------------------------------------------------------
# Game Driver Functions
# ---------------------------------------------------------------

def playOneGame():
    """Plays one full game interactively roll by roll."""
    player = Player()

    while not (player.isWinner() or player.isLoser()):
        dice = player.rollDice()
        print(player.roll)

    if player.isWinner():
        print("You win!")
    else:
        print("You lose!")

    return player.getNumberOfRolls(), player.isWinner()


def playManyGames(n):
    """Simulates n games without printing individual rolls."""
    wins = 0
    losses = 0
    totalRollsWin = 0
    totalRollsLoss = 0

    for _ in range(n):
        player = Player()

        while not (player.isWinner() or player.isLoser()):
            player.rollDice()

        if player.isWinner():
            wins += 1
            totalRollsWin += player.getNumberOfRolls()
        else:
            losses += 1
            totalRollsLoss += player.getNumberOfRolls()

    print(f"The total number of wins is {wins}")
    print(f"The total number of losses is {losses}")

    if wins > 0:
        print(f"The average number of rolls per win is {totalRollsWin / wins:.2f}")
    else:
        print("No wins recorded.")

    if losses > 0:
        print(f"The average number of rolls per loss is {totalRollsLoss / losses:.2f}")
    else:
        print("No losses recorded.")

    print(f"The winning percentage is {wins / n:.3f}")


# ---------------------------------------------------------------
# Example Execution
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Example: play one interactive game
    playOneGame()

    num = int(input("Enter the number of games: "))
    playManyGames(num)
