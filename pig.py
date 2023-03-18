import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--numPlayer", type=int, default=2)
args = parser.parse_args()

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_score = 0

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
    players = [Player(f"Player {i}") for i in range(1, args.numPlayer+1)]
    winning_score = 100
    winner = False

    while not winner:
        for player in players:
            print(f"{player.name}'s turn")
            player.turn_score = 0
            while True:
                choice = play_or_stay(player)
                if choice == 'h':
                    player.score += player.turn_score
                    if player.score >= winning_score:
                        winner = True
                        print(f"{player.name} is the winner!")
                    break
                roll = dice_roll(player)
                if roll == 1:
                    print(f"    {player.name} rolled a 1 and now they\'re done")
                    player.turn_score = 0
                    break
                else:
                    player.turn_score += roll
                    # player.score += roll
                    print(f"    You rolled {roll}. {player.name} score: [{player.score}] "
                          f"Turn score: [{player.turn_score}]")
                    if player.score + player.turn_score >= winning_score:
                        winner = True
                        print(f"{player.name} is the winner!")
                        break
            if winner:
                break

