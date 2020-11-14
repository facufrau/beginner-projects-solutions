import sys

class CoffeeMachine:
    def __init__(self):
        # Define and initialize stock variables.
        self.stock = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550} 
    
    def main(self):
        while True:
            print()
            print('Write action (buy, fill, take, remaining, exit):')
            user_input = input()
            self.action(user_input)
            print()
    
    def print_state(self):
        """Prints the current state of the machine."""
        print()
        print("The coffee machine has:")
        print(f"{self.stock['water']} of water")
        print(f"{self.stock['milk']} of milk")
        print(f"{self.stock['beans']} of coffee beans")
        print(f"{self.stock['cups']} of disposable cups")
        print(f"{self.stock['money']} of money")
        print()

    def buy(self):
        """Buys a cup of selected coffee and updates status."""
        self.supplies = {
                    1: {'water': 250, 'milk': 0, 'beans': 16, 'cups': 1, 'money': -4},
                    2: {'water': 350, 'milk': 75, 'beans': 20, 'cups': 1, 'money': -7},
                    3: {'water': 200, 'milk': 100, 'beans': 12, 'cups': 1, 'money': -6}
                    }
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == "back":
            pass
        else:
            choice = int(choice)
            for key, value in self.supplies[choice].items():
                if self.stock[key] - value < 0:
                    print(f"Sorry, not enough {key}!")
                    return None
                else:
                    self.stock[key] -= value
            print("I have enough resources, making you a coffee!")


    def fill(self):
        """Refills each supply in input amount."""
        water_add = int(input("Write how many ml of water do you want to add:\n"))
        milk_add = int(input("Write how many ml of milk do you want to add:\n"))
        beans_add = int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups_add = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        
        self.stock['water'] += water_add
        self.stock['milk'] += milk_add
        self.stock['beans'] += beans_add
        self.stock['cups'] += cups_add


    def take(self):
        """Takes out the money."""
        print(f"I gave you ${self.stock['money']}")
        self.stock['money'] = 0

    def action(self, u_input):
        if u_input == "buy":
            self.buy()
        elif u_input == "fill":
            self.fill()
        elif u_input == "take":
            self.take()    
        elif u_input == "remaining":
            self.print_state()
        elif u_input == "exit":
            sys.exit()


coffee = CoffeeMachine()
coffee.main()
