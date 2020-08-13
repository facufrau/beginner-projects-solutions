# Beginner project 13 - Base Jumper.
'''
Create a program that converts an integer to the specified base.
Ask for 3 inputs: number, base and goal base.
Accept basis from 2 to 16.
Display result and ask if want to convert again.
Subgoals:
    do not display leading zeros
    validate number for given base.
'''
#Dictionary for referencing numbers.
ref_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def base_10(num_str, base):
    '''
    Converts a string containing a number from given base to base 10.
    '''
    n_base10 = 0
    long = len(num_str)

    for i in range(long):
        digit = ref_digits[num_str[long-1-i]]
        n_base10 += digit * (base ** i)

    return n_base10

def to_base_x(num, base):
    '''
    Converts a number in decimal base to a specified base (2-16)
    '''

    n_base_x = 0

print(base_10('123123', 4))
print(base_10('123AB', 14))
print(base_10('A4FC9', 16))





#Get 3 numbers from user input.
number = input('Enter a positive integer to convert')
while True:
    number_base = input('Enter the number\'s base (2-16)')
    if 2 <= number_base <= 16 :
        break
    else:
        print('The number base is out of range (2-16).')

while True:
    goal_base = input('Enter the base for the conversion (2-16)')
    if 2 <= goal_base <= 16:
        break
    else:
        print('The goal base is out of range (2-16).')