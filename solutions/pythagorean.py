# Beginner project 4
# Pythagorean Triples Checker

# Allows the user to input the sides of any triangle in any order.
# Return whether the triangle is a Pythagorean Triple or not.
# Loop the program so the user can use it more than once without having to restart the program.

print("This program checks if the triangle is a Pythagorean Triple or not")

while True:
    sides = []

    # Getting three numbers from user.
    for i in range(3):
        while True:
            number = input(f"Enter {i+1}° number: ")
            
            # Check if number is a positive integer.
            try:
                int(number)
                if int(number) > 0:
                    break
                else:
                    continue
            except ValueError:
                print("That is not an int number.")
        # Append number to the sides list.
        sides.append(int(number))
    
    # Sort list and check Pythagorean triple.
    sides.sort()
    sum_squares = sides[0] ** 2 + sides [1] ** 2
    third_square = sides [2] ** 2
    
    if third_square == sum_squares:
        print(f"The numbers {sides} are a pytheagorean triple")
    else:
        print(f"The numbers {sides} are NOT a pytheagorean triple")
    
    # Ask for quitting.
    q = input("Do you want to try again? yes/no\n")
    if (q.lower() == 'no' or q.lower() == 'n'):
        break
    else:
        continue
        
    
