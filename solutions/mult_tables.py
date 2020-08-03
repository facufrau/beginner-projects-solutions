# Beginner project 11 - Multiplication tables.
# Make a multiplication table and show them to the user.
from time import sleep

# Receiving input from the user, for the size of the table.
while True:
    try:
        size = int(input('Enter multiplication table size (1-20): '))
        if 1 <= size <= 20:
            break
    except:
        print('Please enter a integer number between 1 and 20.')

# Calculating max length of numbers for formatting.
max_length = len(str(size ** 2)) + 2

# First loop that print headers / first row.
for i in range (1, size + 1):
    if i == 1:
        if size < 4:
            print('---', end='')
        elif size < 10:
            print('----',end='')
        else:
            print('-----',end='')
    print(str(i).center(max_length,'-'),end='')
print('\n')
sleep(1)

# Second loop that prints columns first item and complete row.
for i in range (1, size + 1):
    for j in range (1, size + 1):
        if j == 1:
            print(str(i).ljust(max_length,'-'),end='')
        print(str(i*j).center(max_length,'-'),end='')
    print('\n')
    sleep(1)