# Generates a 5 digit random number until reach a goal number and count the qty of tries.
from random import randint
from time import sleep

def countdown():
    '''
    Counts down from 3 and prints to the screen
    '''    
    for i in [3, 2, 1]:
        print(f'{i}...')
        sleep(1)

def ask_number():
    '''
    Prompts the user for a 5 digit number and checks the input.
    '''
    while True:
        goal_num = input('Enter goal number: ')
        
        try:
            goal_num = int(goal_num)
            if goal_num > 10000 and goal_num < 100000:
                return goal_num
            print('Please enter a 5 digit integer number')
            
        except:
            print('That is not an integer number')

def find_number(goal):
    '''
    Generates random number until the goal is generated.
    Count number of tries required.
    '''
    tries = 0
    while True:
        tries += 1
        random_num = randint(10000,99999)
        print(random_num)
        
        if random_num == goal:
            return random_num, tries

def main():

    goal_num = ask_number()
    print('This program will generate random numbers until reached the input number.')

    countdown()

    found_num, tries = find_number(goal_num)
    print(f'Your goal number was {found_num} and needed {tries} tries.')

if __name__ == '__main__':
    main()
