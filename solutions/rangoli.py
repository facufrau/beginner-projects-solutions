# Rangoli generator
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def print_rangoli(size):
    # your code goes here
    # Get substring with letters until selected size.
    letters = alphabet[:size]
    
    # Calculate line length and amount of rows.
    line = 4 * size - 3
    rows = 2 * size - 1
    
    # List for storing each rangoli line str.
    rangoli = []
    counter = -1
    for i in range(rows):
        # Generate first half until central row.
        if i <= (rows // 2):
            # First row only has one letter.
            if counter == -1:
                l = '-'.join(letters[counter:])
            # Generate a symmetric list of letters for joining
            else:
                partia1 = letters[counter::1]
                total = letters[:(-i-1):-1] + partia1
                l = '-'.join(total)
                
            rangoli.append(l.center(line, '-'))
            counter -= 1
        # Repicate with symmetry the remaining lines.
        else:
            index = (rows - 1) - i
            rangoli.append(rangoli[index])
    print('\n'.join(rangoli))
    
    
if __name__ == '__main__':
    while True:
        n = input('Enter Rangoli 0 < n < 27 : ')
        try:
            n = int(n)
            if 0 < n < 27:
                break
            else:
                print("Enter a number n --> 0 < n < 27")
        except:
            print("Please enter only numbers.")
    print_rangoli(n)
