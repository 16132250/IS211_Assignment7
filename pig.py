import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

def dice_roll(Player):
    roll = random.randint(1,6)
    # print(f"{Player.name} rolled a {roll}")

    return int(roll)

def play_or_stay(Player):
    choice = input(f"  Enter 'r' to roll or 'h' to hold: ")
    while choice not in ['r', 'h']:
        print("Invalid input. Please enter 'r' to roll or 'h' to hold.")
        choice = input(f"{Player.name}, enter 'r' to roll or 'h' to hold: ")
    return choice



if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    winner = False

    while not winner:
        for player in [player1, player2]:
            print(f"{player.name}'s turn")
            while True:
                choice = play_or_stay(player)
                if choice == 'h':
                    break
                roll = dice_roll(player)
                if roll == 1:
                    print(f"    {player.name} rolled a 1 and now they\'re done")
                    break
                player.score += roll
                print(f"    You rolled {roll}. Player 1 score: {player1.score} Player 2 score: {player2.score}")
                if player.score >= 30:
                    winner = True
                    print(f"{player.name} is the winner!")
                    break
            if winner:
                break

