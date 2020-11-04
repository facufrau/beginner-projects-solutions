def print_state(stock):
    """Prints the current state of the machine."""
    print()
    print("The coffee machine has:")
    print(f"{stock['water']} of water")
    print(f"{stock['milk']} of milk")
    print(f"{stock['beans']} of coffee beans")
    print(f"{stock['cups']} of disposable cups")
    print(f"{stock['money']} of money")
    print()

def buy(stock):
    """Buys a cup of selected coffee and updates status."""
    supplies = {
                1: {'water': 250, 'milk': 0, 'beans': 16, 'cups': 1, 'money': -4},
                2: {'water': 350, 'milk': 75, 'beans': 20, 'cups': 1, 'money': -7},
                3: {'water': 200, 'milk': 100, 'beans': 12, 'cups': 1, 'money': -6}
                }
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if choice == "back":
        pass
    else:
        choice = int(choice)
        for key, value in supplies[choice].items():
            if stock[key] - value < 0:
                print(f"Sorry, not enough {key}!")
                return None
            else:
                stock[key] -= value
        print("I have enough resources, making you a coffee!")


def fill(stock):
    """Refills each supply in input amount."""
    water_add = int(input("Write how many ml of water do you want to add:\n"))
    milk_add = int(input("Write how many ml of milk do you want to add:\n"))
    beans_add = int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups_add = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    
    stock['water'] += water_add
    stock['milk'] += milk_add
    stock['beans'] += beans_add
    stock['cups'] += cups_add


def take(stock):
    """Takes out the money."""
    print(f"I gave you ${stock['money']}")
    stock['money'] = 0

    
# Define and initialize stock variables.
stock = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}

while True:    
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "buy":
        buy(stock)
    elif action == "fill":
        fill(stock)
    elif action == "take":
        take(stock)    
    elif action == "remaining":
        print_state(stock)
    elif action == "exit":
        break