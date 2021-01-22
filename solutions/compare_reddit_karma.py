#Beginner project 25 - Compare recent reddit karma
'''
Compare Recent reddit Karma

Create a program that gets information about two different users,
and then sees whose most recent post received the most karma.
The program should then print out which user received more karma, and what the difference was.
This is a pretty open project, so I encourage you to take it further by adding more features
if you find it interesting.

Subgoals:
Allow the user to put in the name of two different users when the program first begins.
If one of the names of the users does not exist (because of a spelling error),print out a message saying so.
Allow the user to keep comparing other users until the program is closed.
Display the amount of upvotes and downvotes each user received for their posts.
'''

import json
import requests
from time import sleep

def main():
    flag = True
    while flag:
        print("-------------------------\nReddit karma comparison\n-------------------------")
        # Get the 2 usernames to check karma.
        first_user = input("Enter first reddit username for analysis: ")
        second_user = input("Enter second reddit username for analysis: ")

        # Set headers and ask limit.
        headers = {'User-agent': 'Myscript 0.0.1'}
        while True:
            limit = input("Enter limit of posts/comments to retrieve(25,50,75 or 100): ")
            try:
                limit = int(limit)
                if limit in [25, 50, 75, 100]:
                    break
                else:
                    print("Please enter only 25, 50, 75, 100")
            except ValueError:
                print("Please enter only 25, 50, 75, 100")

        # Get first user data.
        url = f"https://www.reddit.com/user/{first_user}.json?limit={limit}"
        res_first = requests.get(url, headers=headers)
        print(f"Status code for {first_user} : {res_first.status_code}")

        # Pause three seconds between requests
        sleep(3)

        # Get second user data.
        url = f"https://www.reddit.com/user/{second_user}.json?limit={limit}"
        res_second = requests.get(url, headers=headers)
        print(f"Status code for {second_user} : {res_second.status_code}")


        # Verify that both of the usernames exists.
        if res_first.status_code != 200:
            if res_second.status_code != 200:
                print("Both usernames does not exist")
                return 0
            else:
                print("First username does not exist")
                return 1
        elif res_second.status_code != 200:
            print("Second username does not exist")
            return 1

        # Create jsons from the data obtained.
        json_first = res_first.json()
        json_second = res_second.json()
        jsons = {first_user: json_first, second_user:json_second}

        # Create dictionaries for storing karma for each user
        scores_comments = {first_user:[], second_user: []}
        scores_posts = {first_user:[], second_user: []}

        for user, data in jsons.items():
            for item in data["data"]["children"]:
                score = item["data"]["score"]
                data_type = item["kind"]

                if data_type == "t1":  # t1 means comments in reddit user json.
                    scores_comments[user].append(score)
                elif data_type == "t3":  # t3 means posts in reddit user json.
                    scores_posts[user].append(score)

        first_user_total = {'comments': sum(scores_comments[first_user]), 'posts': sum(scores_posts[first_user])}
        second_user_total = {'comments': sum(scores_comments[second_user]), 'posts': sum(scores_posts[second_user])}
        print(f"Post karma: {first_user} {first_user_total['posts']}")
        print(f"Post karma: {second_user} {second_user_total['posts']}")
        print(f"Comment karma: {first_user} {first_user_total['comments']}")
        print(f"Comment karma: {second_user} {second_user_total['comments']}")

        while True:
            ask_again = input("Do you want to start again? yes/no (y/n): ").lower()
            if ask_again in ['yes', 'y', 'no', 'n']:
                break
        if ask_again in ['no', 'n']:
            flag = False

        # Pause by 5 seconds between starting again.
        sleep(5)
if __name__ == '__main__':
    main()