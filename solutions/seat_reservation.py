#Beginner project 17 - Seat Reservation
'''
Seat Reservation

If you've ever been in a concert, you are aware that you buy tickets to be able to reserve a seat inside a stadium.
The seat you will be on will have a specific number or code that would enable you to know exactly how far or how close
you are to the stage.

Note: if you are kind of uncomfortable with lists, here's a reference to get you started.
    Create a simple seat reservation program

    Create a list that would store dashes '-' as a symbol that the seat is still available to take.

    Define a function that would loop over the list and print out the seats horizontally or in a 3 x 3 position.
    Refer to this image for reference.

    Define a second function that would check if the seats are occupied. This should check if the list contains "X"
    in each element, which is the symbol that we will use if the seat is taken that you will store in a variable.

    If the variable is equal to 9 (the total number of seats), return True (and break from the loop), and False if not.
    Create a loop that would have to (1) ask the user for the number of seat he would want to reserve,
    (2) print out the chairs,(3) check if all the seats are occupied and (4) ask the user now if he/she wants to reserve again.

'''
import time
seats = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-'],
        ]

def print_seats(seat_list):
    '''
    Prints the seats in orden and in separate lines.
    '''
    for i in seat_list:
        for j in i:
            print(j, end=' ')
        print('\n')

def check_seats(seat_list):
    '''
    Checks the amount of occupied seats 'X', returns True if all occupied.
    False otherwise.
    '''
    occupied = 0
    for i in seat_list:
        for j in i:
            if j == 'X':
                occupied += 1

    if occupied == 9:
        return True
    else:
        return False

print('Welcome to my theater, this are the seats: ')
flag = True
while flag:
    print_seats(seats)
    while not check_seats(seats):
        while True:
            reserve = input('Which seat do you want to reserve (1-9): ')
            if not reserve:
                continue
            try:
                reserve = int(reserve) - 1
                if 0 <= reserve < 9:
                    break
            except:
                print('Please enter only a number between 1-9: ')

        row = reserve // 3
        col = reserve % 3

        if seats[row][col] == '-':
            print('Seat available, now reserving...')
            time.sleep(1)
            seats[row][col] = 'X'
            print_seats(seats)
            break
        else:
            print('Seat unavailable, please choose another...')
            time.sleep(1)
            continue

    if check_seats(seats):
        print('All seats occupied!')
        break

    while True:
        again = input('Do you want to reserve again? y/n ')
        if again.lower() in ['n', 'no']:
            flag = False
            break
        elif again.lower() in ['y', 'yes']:
            break
        else:
            print('Please enter "y" or "n"')