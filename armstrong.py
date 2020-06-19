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
