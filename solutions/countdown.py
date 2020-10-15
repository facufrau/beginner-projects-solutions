#Beginner project 22 - Countdown timer.

'''
Create a program that allows the user to choose a time and date,
and then prints out a message at given intervals (such as every second)
that tells the user how much longer there is until the selected time.
Subgoals:

    If the selected time has already passed, have the program tell the user to start over.

    If your program asks for the year, month, day, hour, etc. separately,
    allow the user to be able to type in either the month name or its number.

    TIP: Making use of built in modules such as time and datetime can change
    this project from a nightmare into a much simpler task
'''

from time import sleep
from datetime import datetime
from dateutil import parser, tz
from dateutil.relativedelta import relativedelta

def time_amount(time_unit: str, countdown: relativedelta) -> str:
    """Return the time amount formatted with unit if not null."""
    t = getattr(countdown, time_unit)
    if t != 0 :
        return f"{t} {time_unit}"
    else:
        return ""

def main():
    """Calculates time delta and prints the countdown every 5 seconds."""

    units = ['years', 'months', 'days', 'hours', 'minutes', 'seconds']

    print('------Countdown------')

    event = input("Enter the name of the event you want to track: \n")
    while True:
        date_input = input("Enter date in format YYYY-MM-DD HH:MM:SS: ")
        try:
            DATE = parser.parse(date_input)
            DATE = DATE.replace(tzinfo=tz.tzlocal())
        except:
            continue
        if DATE > datetime.now(tz=tz.tzlocal()):
            break
        else:
            print("Date already passed, please enter another date.")

    print('Press ctrl + c to stop')
    while True:
        now = datetime.now(tz=tz.tzlocal())
        countdown = relativedelta(DATE, now)
        output = []
        for tu in units:
            t = time_amount(tu, countdown)
            if t:
                output.append(t)
        output_string = ", ".join(output)
        print(f"Countdown to {event}: " + output_string)
        sleep(5)

if __name__ == "__main__":
    main()