# Beginner project 12 - Fibonacci.
'''
Define a function that allows the user to find the value of the nth term in the sequence.
To make sure you've written your function correctly, test the first 10 numbers of the sequence.
You can assume either that the first two terms are 0 and 1 or that they are both 1.
There are two methods you can employ to solve the problem.
    One way is to solve it using a loop and the other way is to use recursion.
    Try implementing a solution using both methods.

'''
def fibonacci_loop(n):
    '''
    Calculates and return the nth term in the fibonacci sequence.
    Designed with a for loop.
    '''
    sequence = [0,1]
    if n == 1:
        return sequence[n-1]
    elif n == 2:
        return sequence[n-1]
    else:
        for i in range(1, n+1):
            if i > 2:
                next_term = sequence[i-2] + sequence[i-3]
                sequence.append(next_term)
        return sequence[n-1]

def fibonacci_recursive(n):
    '''
    Calculates and return the nth term in the fibonacci sequence.
    Designed with recursion.
    '''
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print('Solution with loop')
for i in range (1, 16):
    print(f'{i}° term: {fibonacci_loop(i)}')

print('Solution with recursion')
for i in range (1, 16):
    print(f'{i}° term: {fibonacci_recursive(i)}')