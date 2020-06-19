# Beginner project 1.

bottles = 99

for i in range(bottles,-1,-1):

    if i >= 2:
        print(f'{i} bottles of beer on the wall, {i} bottles.')

        if i != 2:
            print(f'Take one down, pass it around, {i-1} bottles of beer on the wall...\n')
        else:
            print(f'Take one down, pass it around, {i-1} bottle of beer on the wall...\n')
            
    elif i == 1:
        print(f'{i} bottle of beer on the wall, {i} bottle.')
        print(f'Take one down, pass it around, none bottles of beer on the wall...\n')

    else:
        print('No more bottles of beer on the wall, no more bottles of beer.')
        print(f'Go to the store and buy some more, {bottles} bottles of beer on the wall...\n')
        
        
        
