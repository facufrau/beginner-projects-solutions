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

from datetime import datetime
from dateutil import parser, tz
from dateutil.relativedelta import relativedelta

months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
            'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
units = ['year', 'month', 'day', 'hour', 'minutes', 'seconds']

print('------Countdown------')

XMAS = parser.parse("Dec 25, 2020, 0:00 AM")
XMAS = XMAS.replace(tzinfo=tz.gettz("Hora estándar de Argentina"))
now = datetime.now(tz=tz.tzlocal())

countdown = relativedelta(XMAS, now)
output = (t for tu in units if (t := time_amount(tu, countdown)))
print(f"Countdown to XMAS 2020: ", ", ".join(output))