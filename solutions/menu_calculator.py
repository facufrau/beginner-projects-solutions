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

print('*** Welcome to my restaurant ***\n----------MENU----------')
for item in menu:
    print(f'{item[0]} - {item[1]} - ${item[2]:.2f}')

while True:
    order = input('Please enter the order numbers with no spaces between: ')
    try:
        order_list = [int(x) for x in order if int(x) > 0]
        break
    except:
        print('Please enter only numbers in the order.')

print(order)
print(order_list)

total_price = 0.00
for i in order_list:
    total_price +=

