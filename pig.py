import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

def dice_roll(Player):
    roll = random.randint(1,6)
    print(f"{Player.name} rolled a {roll}")

    return int(roll)

def play_or_stay(Player):
    choice = input(f"{Player.name}, enter 'r' to roll or 'h' to hold: ")
    while choice not in ['r', 'h']:
        print("Invalid input. Please enter 'r' to roll or 'h' to hold.")
        choice = input(f"{Player.name}, enter 'r' to roll or 'h' to hold: ")
    return choice



if __name__ == "__main__":
    counter = 0
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    score_p1 = player1.score
    score_p2 = player2.score

    while counter <= 3:

        choice_p1 = play_or_stay(player1)

        roll_p1 = dice_roll(player1)
        score_p1 += roll_p1
        print(f"{player1.name} chose: {choice_p1}")
        print(f'{player1.name} score is now {score_p1}')


        choice_p2 = play_or_stay(player2)

        roll_p2 = dice_roll(player2)
        print(f"{player2.name} chose: {choice_p2}")

        counter += 1
        print(f'counter = {counter}')