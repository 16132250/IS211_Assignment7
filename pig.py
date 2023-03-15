import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def dice_roll(self):
        roll = random.randint(1,6)
        print(f"{self.name} rolled a {roll}")
        return roll

if __name__ == "__main__":
    player1 = Player("Player 1")
    rollp1 = player1.dice_roll()
    player2 = Player("Player 2")
    rollp2 = player2.dice_roll()