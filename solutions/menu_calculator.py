#Beginner project 16 - Menu calculator.
'''
Menu Calculator

Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders.
Since your restaurant only sells 9 different items, you assign each one to a number, as shown below.

    1 - Chicken Strips - $3.50
    2 - French Fries - $2.50
    3 - Hamburger - $4.00
    4 - Hotdog - $3.50
    5 - Large Drink - $1.75
    6 - Medium Drink - $1.50
    7 - Milk Shake - $2.25
    8 - Salad - $3.75
    9 - Small Drink - $1.25

To quickly take orders, your program should allow the user to type in a string of numbers.
Then it should calculate the cost of the order.
For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered,
the user should type in 5993348, and the program should say that it costs $19.50.
Also, make sure that the program loops so the user can take multiple orders
without having to restart the program each time.

Subgoals:
If you decide to, print out the items and prices every time before the user types in an order.
Once the user has entered an order, print out how many of each item have been ordered, as well as the total price.
If an item was not ordered at all, then it should not show up.

'''
# List of lists containing menu items and prices.
menu = [[1, "Chicken Strips", 3.50], [2, "French Fries", 2.50], [3, "Hamburger", 4.00],
[4, "Hotdog", 3.50], [5, "Large Drink", 1.75], [6, "Medium Drink", 1.50],
[7, "Milk Shake", 2.25], [8, "Salad", 3.75], [9, "Small Drink", 1.25]]

flag = True
while flag:
    print('*** Welcome to my restaurant ***\n----------MENU----------')
    for item in menu:
        print(f'{item[0]} - {item[1]} - ${item[2]:.2f}')

    while True:
        order = input('Please enter the order numbers with no spaces between: ')
        if not order:
            continue
        try:
            order_list = [int(x) for x in order if int(x) > 0]
            break
        except:
            print('Please enter only numbers in the order.')

    #Initalize variables for printing orders and price.
    total_price = 0.00
    orders = {}
    print('You order has the following items: ')
    for i in order_list:
        # Adds up total price.
        total_price += menu[i-1][2]

        # Stores in a dictionary how many of each item was ordered.
        product = menu[i-1][1]
        if product not in orders:
            orders[product] = 0
        orders[product] += 1

    for item, amount in orders.items():
            print(f'- {amount} -- {item}')
    print(f'The total price is ${total_price:.2f}')

    while True:
        again = input('Do you want to enter another order? y/n ')
        if again.lower() in ['n', 'no']:
            flag = False
            break
        elif again.lower() in ['y', 'yes']:
            break
        else:
            print('Please enter "y" or "n"')
