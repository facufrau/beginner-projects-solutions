# Simple banking system - stage 3/4
import random
from sys import exit
import sqlite3

conn = sqlite3.connect('card.s3db')
# Create table
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS card')
conn.commit()
cur.execute('CREATE TABLE card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
conn.commit()

def main():
    """Main function for the app."""
    menu = "1. Create an account\n2. Log into account\n0. Exit"
    submenu = "1. Balance\n2. Log out\n0. Exit"

    while True:
        print(menu)
        option = int(input())
        id_num = 0
        if option == 1:
            card, pin = create_acc()
            id_num += 1
            row = [id_num, card, pin]
            cur.execute('INSERT INTO card (id, number, pin) VALUES (?,?,?)', row)
            conn.commit()
        elif option == 2:
            user_card = input("\nEnter your card number:\n")
            user_pin = input("Enter your PIN:\n")
            cur.execute("SELECT number, pin, balance FROM card WHERE number=(?)", (user_card,))
            conn.commit()
            response = cur.fetchone()
            
            print(response)
            if not response or response[1] != user_pin:
                print("\nWrong card number or PIN!\n")
            else:
                print("\nYou have successfully logged in!\n")
                while True:
                    print(submenu)
                    sub_option = int(input())
                    if sub_option == 1:
                        balance = response[2]
                        print(f"\nBalance: {balance}\n")
                    elif sub_option == 2:
                        print("\nYou have successfully logged out!\n")
                        break
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