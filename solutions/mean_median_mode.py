# Beginner project 9
# Mean, median and mode.
'''
Create three functions that allow the user to find the mean, median, and mode of a list of numbers.
If you have access or know of functions that already complete these tasks, do not use them.
Subgoals
    In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
    If there is an even number of numbers in the list, return both numbers that could be considered the median.
    If there are multiple modes, return all of them.
'''

def mean(numbers, decimals):
    '''
    Calculate the mean of a list of numbers.
    User can pass the decimals for rounding the answer.
    '''
    total_sum = 0
    for n in numbers:
        total_sum += n
    avg = round(total_sum/len(numbers), decimals)
    return avg

def median(numbers, decimals):
    '''
    Calculate the median of a list of numbers.
    If even number of numbers, return the mean between both middle values.
    '''
    numbers.sort() # sorting in ascending way for calculations.
    length = len(numbers)
    if length % 2 == 0:
        med1 = numbers[length // 2 - 1]
        med2 = numbers[length // 2]
        med = (med1 + med2) / 2
        return round(med, decimals)
    else:
        med = numbers[length // 2]
        return round(med, decimals)

def mode(numbers):
    '''
    Calculate the mode of a list of numbers.
    If there are multiple, return a list of modes.
    '''
    numbers.sort() #Sorting in ascending way for calculations.
    num_dict = {}
    for n in numbers:
        if n in num_dict:
            num_dict[n] += 1
        else:
            num_dict[n] = 1

    #Find the maximum value in dictionary of numbers and repetitions.
    max_value = max(num_dict.values())

    #Create a list with the keys(numbers) that have the value equal as the maximum value.
    #This numbers are the mode or modes.
    modes = [key for key, value in num_dict.items() if value == max_value]
    return modes

if __name__ == '__main__':
    while True:
        number_type = input('Enter "f" to work with float numbers or "i" for integers: \n')
        if number_type == 'i':
            nums = []
            decs = 0
            while True:
                n = input('Enter an integer number or "q" to stop: \n')
                if n == 'q':
                    break
                try:
                    nums.append(int(n))
                except:
                    continue
            print(f'You entered this numbers: {nums}')

            while True:
                d = input('Enter the number of decimals for calculations(0-9): \n')
                try:
                    decs = int(d)
                    if decs >= 0 and decs <=9:
                        break
                except:
                    continue
            print(f'You chose {decs} decimals.')
            print(f'The mean is {mean(nums, decs)}.\nThe median is {median(nums, decs)}.\nThe mode(s) is(are) {mode(nums)}.')
            break
        elif number_type == 'f':
            nums = []
            decs = 0
            while True:
                n = input('Enter a float number or "q" to stop: \n')
                if n == 'q':
                    break
                try:
                    nums.append(float(n))
                except:
                    continue
            print(f'You entered this numbers: {nums}')

            while True:
                d = input('Enter the number of decimals for calculations(0-9): \n')
                try:
                    decs = int(d)
                    if decs >= 0 and decs <=9:
                        break
                except:
                    continue
            print(f'You chose {decs} decimals.')
            print(f'The mean is {mean(nums, decs)}.\nThe median is {median(nums, decs)}.\nThe mode(s) is(are) {mode(nums)}.')
            break