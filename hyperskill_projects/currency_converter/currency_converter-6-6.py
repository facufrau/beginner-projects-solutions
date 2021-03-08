import requests
import json

# Get input currency from user.
current_code = input().lower()

# Create a cache dictionary for used rates.
cache = {'usd': 0, 'eur': 0}

# Loop for continue checking.
while True:
    target_code = input().lower()
    if not target_code:
        break
    money = int(input())

    # Get currency rates from server.
    response = requests.get(f"http://www.floatrates.com/daily/{current_code}.json")
    json_str = response.content.decode('utf-8')
    rates_json = json.loads(json_str)

    # Cache desired results
    rates = ['usd', 'eur']
    for r in rates:
        try:
            cache[r] = rates_json[r]['rate']
        except KeyError:
            continue

    # Convert money and print result.
    print("Checking the cache...")
    if target_code in cache:
        print("Oh! It is in the cache!")
        rate = cache[target_code]
    else:
        print("Sorry, but it is not in the cache!")
        # Update cache with new code retrieved.
        rate = rates_json[target_code]['rate']
        cache[target_code] = rate
        
    conv_money = round(money * rate, 2)
    print(f"You received {conv_money} {target_code.upper()}.")



