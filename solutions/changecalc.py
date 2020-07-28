# Beginner project 8
# Change Calculator
'''
    Imagine that your friend is a cashier, but has a hard time counting back change to customers.
    Create a program that allows him to input a certain amount of change,
    and then print how how many quarters, dimes, nickels, and pennies
    are needed to make up the amount needed. Example: if he inputs 1.47,
    the program will say that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.
    Subgoals:
        So your friend doesn't have to calculate how much change is needed,
        allow him to type in the amount of money given to him and the price of the item.
        The program should then tell him the amount of each coin he needs like usual.
        To make the program even easier to use, loop the program back to the top
        so your friend can continue to use the program without having to close and open
        it every time he needs to count change.
'''
while True:
    try:
        price = float(input('Please enter the price of the object: '))
        if price > 0:
            break
    except:
        print('Enter a valid price (for example 35.66)')

while True:
    try:
        money = float(input('Please enter the money received: '))
        if money > 0:
            break
    except:
        print('Enter a valid amount of money (for example 100.50)')

penny, nickel, dime, quarter = 0, 0, 0, 0
change = round(money - price, 2)
cents = change * 100

while cents > 0:
    if cents % 25 == 0:
        quarter += 1
        cents -= 25
    elif cents % 10 == 0:
        dime += 1
        cents -= 10
    elif cents % 5 == 0:
        nickel += 1
        cents -= 5
    elif cents % 1 == 0:
        penny += 1
        cents -= 1

print(f'The total change is {change}')
print(f'You will need: \n-->{quarter} quarter(s)\n-->{dime} dime(s)\n-->{nickel} nickel(s)\n-->{penny} penny(ies)')