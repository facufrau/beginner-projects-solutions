# Simple banking system - stage 2/4
import random
from sys import exit

def main():
    """Main function for the app."""
    menu = "1. Create an account\n2. Log into account\n0. Exit"
    submenu = "1. Balance\n2. Log out\n0. Exit"

    database = {}
    while True:
        print(menu)
        option = int(input())
        if option == 1:
            card, pin = create_acc()
            database[card] = {'pin': pin, 'balance': 0}
        elif option == 2:
            user_card = input("\nEnter your card number:\n")
            user_pin = input("Enter your PIN:\n")
            check = True
            try:
                database[user_card]['pin'] != user_pin
                check = True
            except KeyError:
                check = False

            if check == False or database[user_card]['pin'] != user_pin:
                print("\nWrong card number or PIN!\n")
            else:
                print("\nYou have successfully logged in!\n")
                print(submenu)
                while True:
                    sub_option = int(input())
                    if sub_option == 1:
                        balance = database[user_card]['balance']
                        print(f"\nBalance: {balance}\n")
                    elif sub_option == 2:
                        print("\nYou have successfully logged out!\n")
                    elif sub_option == 0:
                        print("\nBye!")
                        exit()
        elif option == 0:
            print("\nBye!")
            exit()

def create_acc():
    """ Generates a credit card number and pin """
    IIN = '400000'  # Issuer Identification Number (IIN)
    CAN = str(random.randint(0, 10 ** 9)).zfill(9)  # customer account number
    card = IIN + CAN
    card_num_list = [int(x) for x in card]
    checksum = 0
    for i, n in enumerate(card_num_list):
        if i % 2 == 0:
            current = n * 2
            if current > 9:
                current -= 9
            checksum += current
        else:
            checksum += n
    if checksum % 10 == 0:
        card += str(0)
    else:
        card += str(10 - checksum % 10)
        
    pin = str(random.randint(0, 10000)).zfill(4)  # 4 digit pin (0000-9999)
    print(f"\nYour card has been created")
    print(f"Your card number:\n{card}")
    print(f"Your card PIN:\n{pin}")
    print()

    return card, pin

if __name__ == '__main__':
    main()