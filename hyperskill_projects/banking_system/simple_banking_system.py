# Simple banking system - stage 3/4
import random
from sys import exit
import sqlite3

conn = sqlite3.connect('card.s3db')
# Create table
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
conn.commit()


def main():
    """Main function for the app."""
    menu = ["1. Create an account", "2. Log into account", "0. Exit"]

    submenu = ["1. Balance", "2. Add income", "3. Do transfer",
               "4. Close account", "5. Log out", "0. Exit"]

    while True:
        print('\n'.join(menu))
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

            if not response or response[1] != user_pin:
                print("\nWrong card number or PIN!\n")
            else:
                print("\nYou have successfully logged in!\n")
                while True:
                    cur.execute("SELECT balance FROM card WHERE number=(?)", (user_card,))
                    conn.commit()
                    balance = cur.fetchone()[0]

                    print('\n'.join(submenu))
                    sub_option = int(input())
                    
                    # Check balance option
                    if sub_option == 1:
                        print(f"\nBalance: {balance}\n")
                    
                    # Add cash to account
                    elif sub_option == 2:
                        cash = int(input("\nEnter income:\n"))
                        cash = cash + balance
                        cur.execute("UPDATE card SET balance=(?) WHERE number=(?)", (cash, user_card))
                        conn.commit()
                        print("Income was added!\n")

                    # Transfer to another account.
                    elif sub_option == 3:
                        print("\nTransfer")
                        destination_card = input("Enter card number:\n")
                        if not checksum(destination_card):
                            print("Probably you made a mistake in the card number. Please try again!\n")
                        else:
                            cur.execute("SELECT balance FROM card WHERE number=(?)", (destination_card,))
                            conn.commit()
                            if not cur.fetchone():
                                print("Such a card does not exist.\n")
                            else:
                                cur.execute("SELECT balance FROM card WHERE number=(?)", (destination_card,))
                                conn.commit()
                                dest_balance = cur.fetchone()[0]
                                transfer = int(input("Enter how much money you want to transfer:\n"))
                                if transfer > balance:
                                    print("Not enough money!\n")
                                else:
                                    sender = balance - transfer
                                    receiver = dest_balance + transfer
                                    cur.execute("UPDATE card SET balance=(?) WHERE number=(?)", (sender, user_card))
                                    cur.execute("UPDATE card SET balance=(?) WHERE number=(?)", (receiver, destination_card))
                                    conn.commit()
                                    print("Success!\n")

                    # Close account and delete from database.
                    elif sub_option == 4:
                        cur.execute("DELETE FROM card WHERE number=(?)", (user_card,))
                        conn.commit()
                        print("\nThe account has been closed!\n")
                        break

                    # Log out
                    elif sub_option == 5:
                        print("\nYou have successfully logged out!\n")
                        break

                    # Exit program
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


def checksum(ccnumber):
    """ Checks the validity of a card"""
    card_num_list = [int(x) for x in ccnumber]
    check = 0
    for i, n in enumerate(card_num_list):
        if i % 2 == 0:
            current = n * 2
            if current > 9:
                current -= 9
            check += current
        else:
            check += n
    return (check % 10) == 0


if __name__ == '__main__':
    main()
