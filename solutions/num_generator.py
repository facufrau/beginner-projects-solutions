# Generates a 5 digit random number until reach a goal number and count the qty of tries.
from random import randint
from time import sleep

while True:
    goal_num = input('Enter goal number: ')
    try:
        goal_num = int(goal_num)
        if goal_num > 10000 and goal_num < 100000:
            break
        print('Please enter a 5 digit integer number')
    except:
        print('That is not an integer number')

print('This program will generate random numbers until reached the input number.')
for i in [3,2,1]:
    print(f'{i}...')
    sleep(1)

tries = 0
while True:
    tries += 1
    random_num = randint(10000,99999)
    print(random_num)
    if random_num == goal_num:
        print(f'Your goal number was {random_num} and needed {tries} tries.')
        break
