def print_state(water, milk, beans, cups, money):
    """Prints the current state of the machine."""
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")
    print()

def buy():
    """Buys a cup of selected coffee and updates status."""
    global water_stock, milk_stock, beans_stock, cups_stock, money_stock
    choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
    if choice == 1:  # espresso
        water_stock -= 250
        beans_stock -= 16
        cups_stock -= 1
        money_stock += 4
    elif choice == 2:  # latte
        water_stock -= 350
        milk_stock -= 75
        beans_stock -= 20
        cups_stock -= 1
        money_stock += 7
    else:  # capuccino
        water_stock -= 200
        milk_stock -= 100
        beans_stock -= 12
        cups_stock -= 1
        money_stock += 6

def fill():
    """Refills each supply in input amount."""
    global water_stock, milk_stock, beans_stock, cups_stock

    water_add = int(input("Write how many ml of water do you want to add:\n"))
    milk_add = int(input("Write how many ml of milk do you want to add:\n"))
    beans_add = int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups_add = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    
    water_stock += water_add
    milk_stock += milk_add
    beans_stock += beans_add
    cups_stock += cups_add


def take():
    """Takes out the money."""
    global money_stock
    print(f"I gave you ${money_stock}")
    money_stock = 0
    
# Define and initialize stock variables.
water_stock = 400
milk_stock = 540
beans_stock = 120
cups_stock = 9
money_stock = 550
print_state(water_stock, milk_stock, beans_stock, cups_stock, money_stock)
    
action = input("Write action (buy, fill, take):\n")
if action == "buy":
    buy()
    print_state(water_stock, milk_stock, beans_stock, cups_stock, money_stock)
elif action == "fill":
    fill()
    print_state(water_stock, milk_stock, beans_stock, cups_stock, money_stock)
elif action == "take":
    take()
    print_state(water_stock, milk_stock, beans_stock, cups_stock, money_stock)       
