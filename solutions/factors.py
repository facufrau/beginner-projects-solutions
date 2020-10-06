#Beginner project 21 - Factors of a number.

'''
Factors of a Number

    Define a function that creates a list of all the numbers that are factors of the user's number.
    For example, if the function is called factor, factor(36) should return [1, 2, 3, 4, 6, 9, 12, 18, 36].
    The numbers in your list should be sorted from least to greatest, and 1 and the original number should be included.
    Remember to consider negative numbers as well as 0.
    Bonus:
        Have the program print the factors of the users number in a comma separated string,
        without a comma after the last number, and without the brackets of a Python list.
        If the user's number is prime, note it.

'''
def check_prime(num):
    '''
    Checks if a number is prime.
    '''
    num = abs(num)
    if num == 1 or num == 0:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
                break
        else:
            return True

def get_factors(num):
    '''
    Calculates factors of a number.
    Returns a list of factors and True if is prime, False otherwise.
    '''
    num = abs(num)
    factors_p = [] #For storing positive factors.
    factors_n = [] #For storing negative factors.

    for i in range(1, num + 1):
        if num % i == 0:
            factors_p.append(i)
            factors_n.append(-i)

    # Sort both list and merge them.
    # Negative in reverse order for keeping the list in order by ABS value.
    factors_list = sorted(factors_p) + sorted(factors_n, reverse=True)
    return factors_list, check_prime(num)

def print_factors(num):
    '''
    Prints the factors in a comma-separated string, and if the number is prime.
    '''
    factors, prime = get_factors(num)
    print(f'The factors of number {num} are: ')
    string = ""
    for f in factors:
        if f != factors[-1]:
            string += str(f) + ", "
        else:
            string += str(f)
    print(string)
    if prime:
        print(f'The number {num} is prime.')

if __name__ == "__main__":

    while True:
        number = input("Enter number for calculate factors (-1000000 to 1000000): ")
        if not number:
            continue
        try:
            number = int(number)
            if -1000000 <= number <= 1000000:
                break
        except:
            print("Please enter an integer number.")

    print_factors(number)