# Beginner project 5.
# Rock-paper-scissors game.

from random import randint
import time

print("Rock, paper and scissors game")

# Create a moves list and a score.
moves = ["R","P","S"]
score = {"Player": 0 , "Computer": 0, "Ties": 0}

# Function to evaluate winner and add score.
def play(player, computer):
    """
    Evaluate the winner of the R-P-S game and update score.
    Player wins return 1, computer wins return 2, ties return 3.
    """
    if (player == "R"):
        if (computer == "S"):
            score["Player"] = score["Player"] + 1
            return 1
        elif (computer == "P"):
            score["Computer"] = score["Computer"] + 1
            return 2
        elif (computer == "R"):
            score["Ties"] = score["Ties"] + 1
            return 3

    elif (player == "P"):
        if (computer == "S"):
            score["Computer"] = score["Computer"] + 1
            return 2
        elif (computer == "P"):
            score["Ties"] = score["Ties"] + 1
            return 3
        elif (computer == "R"):
            score["Player"] = score["Player"] + 1
            return 1

    elif (player == "S"):
        if (computer == "S"):
            score["Ties"] = score["Ties"] + 1
            return 3
        elif (computer == "P"):
            score["Player"] = score["Player"] + 1
            return 1
        elif (computer == "R"):
            score["Computer"] = score["Computer"] + 1
            return 2

# Main loop
while True:
    while True:
        player_move = input("Choose your move: (R) Rock, (P) Paper or (S) Scissors\n").upper()
        if (player_move in moves):
            break
    computer_move = moves[randint(0,2)]

    print(f"Your move is {player_move}")
    time.sleep(1)
    print(f"The computer move is {computer_move}")
    time.sleep(1)

    result = play(player_move, computer_move)
    if result == 1:
        print("You won!!")
    elif result == 2:
        print("The computer won")
    elif result == 3:
        print("It is a tie")
    print(f"Scoreboard: \n\tPlayer {score['Player']} \n\tComputer {score['Computer']} \n\tTies {score['Ties']}")

    flag = input("Play again? 'Yes'/'No'\n")
    if flag.upper() == 'YES' or flag.upper() == 'Y':
        continue
    elif flag.upper == 'NO' or flag.upper() == 'N':
        break