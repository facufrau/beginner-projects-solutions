# Beginner project 6 - Coin estimator by weight.

from time import sleep

coins = {
        'penny': {'weight': 2.500, 'fit': 50, 'value': 0.01},
        'nickel': {'weight': 5.000, 'fit': 40, 'value': 0.05},
        'dime': {'weight': 2.268, 'fit': 50, 'value': 0.10},
        'quarter': {'weight': 5.670, 'fit': 40, 'value': 0.25},
        }

# Ask the user for the total weight of each coin type.
# Store the total weight for each coin type in the dictionary.
for k in coins:
    while True:
        coin_weight = input(f'Enter the total weight of {k.capitalize()} in g (grams):\n')
        try:
            coin_weight = float(coin_weight)
            if coin_weight > 0:
                coins[k]['total_weight'] = coin_weight
                break
            else:
                print('That is not a valid weight amount')
        except:
            print('That is not a valid weight amount')

# Calculate total cash, how many coins and wrappers.
# Format and print out the results.
total_cash = 0

for k in coins:
    coins_qty = round(coins[k]['total_weight']/coins[k]['weight'])
    wrappers = round(coins_qty/coins[k]['fit'])
    total_cash += coins_qty * coins[k]['value']
    sleep(1.5)
    print(f'-----{k.upper()}-----')
    print(f'You have {coins_qty} coins and you will need {wrappers} wrapper(s)')
    print('----------------------')

print(f'Your estimated total cash is {round(total_cash, 2)}')
