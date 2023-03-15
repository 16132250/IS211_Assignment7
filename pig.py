import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

def dice_roll(Player):
    roll = random.randint(1,6)
    print(f"{Player.name} rolled a {roll}")
    return roll

def play_or_stay(Player):
    choice = input(f"{Player.name} choose 1 to roll, 0 to stay")
    return choice



if __name__ == "__main__":
    player1 = Player("Player 1")
    rollp1 = dice_roll(player1)
    choicep1 = play_or_stay(player1)
    print(f"{player1.name} chose: {choicep1}")

    player2 = Player("Player 2")
    rollp2 = dice_roll(player2)
    choicep2 = play_or_stay(player2)
    print(f"{player2.name} chose: {choicep2}")