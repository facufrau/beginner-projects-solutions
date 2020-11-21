import random
import sys
# Write your code here
user = input("Enter your name: ")
print(f"Hello, {user}")
score = 0

with open("rating.txt", "r") as f:
    for line in f.readlines():
        line = line.split()
        name = line[0]
        saved_score = int(line[1])
        
        if name == user:
            score = saved_score
            break
        else:
            score = 0


options_list = input().split(",")
print("Okay, let's start")
if options_list == ['']:
    options_list =  ["rock", "paper", "scissors"]
    
while True:
    user_move = input()
    if user_move == "!exit":
        print("Bye!")
        break
    if user_move == "!rating":
        print(f"Your rating: {score}")
        continue
    if user_move not in options_list:
        print("Invalid input")
        continue
    else:        
        ai_move = random.choice(options_list)
        if user_move == ai_move:
            score += 50
            print(f'There is a draw ({ai_move})')
        else:
            options = len(options_list)
            distance = (options_list.index(ai_move) - options_list.index(user_move)) % options
            
            if distance > options // 2:
                score += 100
                print(f'Well done. The computer chose {ai_move} and failed')
            else:
                print(f'Sorry, but the computer chose {ai_move}')   