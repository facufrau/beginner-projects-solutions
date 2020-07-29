# Beginner project 10 - guess_number.py
# Guess the number game.
'''
Create a simple game where the computer randomly selects a number between 1 and 100.
Then the user has to guess what the number is.
After every guess, the computer should tell the user if the guess is higher or lower than the answer.
When the user guesses the correct number, print out a congratulatory message.
Subgoals:
    1-Add an introductory message that explains to the user how to play your game.
    2-In addition to the congratulatory message at the end of the game
    print out how many guesses were taken before the user arrived at the correct answer.
    3-At the end of the game, allow the user to decide if they want to play again (without having to restart the program).
'''
from random import randint

name = input('Hello, what is your name?\n')
while True:
    print(f'Hello {name.capitalize()} in this game you have to guess a number (1-100)')
    secret_number = randint(1, 100)
    guesses_taken = 0

    while True:
        try:
            guess = int(input('Take a guess...  '))
        except:
            print('Please enter a valid number between 1-100')

        if guess > secret_number:
            print('You guess is too high!')
            guesses_taken += 1
        elif guess < secret_number:
            print('You guess is too low!')
            guesses_taken += 1
        elif guess == secret_number:
            print(f'Congratulations, the number I was thinking was {secret_number}')
            guesses_taken += 1
            break

    print(f'You took {guesses_taken} guesses.')
    flag = input('Do you want to play again? y/n\n')
    if flag == 'y':
        continue
    elif flag == 'n':
        break
    else:
        break