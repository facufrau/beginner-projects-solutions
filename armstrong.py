''' Armstrong Number
    Define a function that allows the user to check whether a given number is armstrong number or not.
    Hint: To do this, first determine the number of digits of the given number. Call that n.
    Then take every digit in the number and raise it to the nth power.
    Add them, and if your answer is the original number then it is an Armstrong number.
    Example: Take 1634. Four digits. So, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634.
    So 1634 is an Armstrong number.
    Tip: All single digit numbers are Armstrong numbers.
'''
def armstrong(number):
    '''
    Allows the user to check whether a given number
    is armstrong number or not.
    '''
    n = len(str(number))
    digits = [int(i) for i in str(number)]

    total = 0
    for digit in digits:
        total = total + digit**n

    if total == number:
        print(f'{number} is an Armstrong number.')
        return True
    else:
        print(f'{number} is NOT an Armstrong number.')
        return False

while True:
    num = input('Enter a number: ')

    try:
        num = int(num)
        break

    except ValueError:
        print('That is not a int number.')

armstrong(num)