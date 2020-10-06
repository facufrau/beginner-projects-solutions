#Beginner project 20 - What is my number?
'''
What's My Number?

Between 1 and 1000, there is only 1 number that meets the following criteria:

    The number has two or more digits.
    The number is prime.
    The number does NOT contain a 1 or 7 in it.
    The sum of all of the digits is less than or equal to 10.
    The first two digits add up to be odd.
    The second to last digit is even and greater than 1.
    The last digit is equal to how many digits are in the number.

To find out if you have the correct number, click here.
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

def split_digits(num):
    '''
    Takes a number and returs a list of its digits.
    '''
    digits = [int(x) for x in str(num)]
    return digits

def add_digits(number_list):
    '''
    Calculate the sum of a list of numbers.
    '''
    total = 0
    for x in number_list:
        total += x
    return total 

def main():    
    for i in range(1001):
        digits = split_digits(i)
        sum_digits = add_digits(digits)
        if len(digits) >= 2:
            if check_prime(i):
                if (1 not in digits and 7 not in digits):
                    if sum_digits <= 10:
                        if (digits[0] + digits[1]) % 2 != 0:
                            if digits[-2] > 1 and digits[-2] % 2 == 0:
                                if digits[-1] == len(digits):
                                    print(f'Number found! - {i}')
                                    break

if __name__ == "__main__":
    main()
