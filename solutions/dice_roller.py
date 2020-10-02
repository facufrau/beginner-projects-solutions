#Beginner project 18 - Dice rolling simulator

'''
Dice Rolling Simulator

By using the random module, Python can do things like pseudo-random number generation.

Allow the user to input the amount of sides on a dice and how many times it should be rolled.
Your program should simulate dice rolls and keep track of how many times each number comes up
(this does not have to be displayed).

Finally, print out how many times each number came up.

Subgoals:
    Adjust your program so that if the user does not type in a number when they need to,
    the program will keep prompting them to type in a real number until they do so.

    Put the program into a loop so that the user can continue to simulate dice rolls without
    having to restart the entire program.

    In addition to printing out how many times each side appeared, also print out the percentage it appeared.
    If you can, round the percentage to 4 digits total OR two decimal places.

Bonus:
    You are about to play a board game, but you realize you don't have any dice. Fortunately you have this program.
        Create a program that opens a new window and draws 2 six-sided dice
        Allow the user to quit, or roll again
    Allow the user to select the number of dice to be drawn on screen(1-4) 2. Add up the total of the dice and display it
'''
import random
again = True
while again:
    results = {}
    while True:
        sides = input("Enter number of sides(2-100): ")
        if not sides:
            continue
        try:
            sides = int(sides)
            if 2 <= sides <= 100:
                break
        except:
            print("Please enter an integer between 2-100")

    while True:
        rolls = input("Enter number of times the dice will be rolled(1-10000): ")
        if not rolls:
            continue
        try:
            rolls = int(rolls)
            if 1 <= rolls <= 10000:
                break
        except:
            print("Please enter an integer between 1-10000")

    for i in range(rolls):
        throw = random.randint(1, sides)
        if throw not in results:
            # First item in list is how many times that number appeared.
            # Second item will be frequency.
            results[throw] = [0, 0]
        results[throw][0] += 1

    # Calculate frequency for each number.
    for count in results.values():
        count[1] = count[0] / rolls

    # Print the results for each number.
    for number in sorted(results.keys()):
        print(f'The number {number} appeared {results[number][0]} times with a frequency of {results[number][1]*100:.2f}%.')

    while True:
        ask = input("Do you want to roll the dice again? (y/n): ")
        if ask.lower() in ['y','yes']:
            break
        elif ask.lower() in ['n', 'no']:
            again = False
            break
        else:
            print("Please enter 'y' or 'n'")