# Beginner project 3.

'''
Magic 8 Ball
Simulate a magic 8-ball.
Allow the user to enter their question.
Display an in progress message(i.e. "thinking").
Create 20 responses, and show a random response.
Allow the user to ask another question or quit.
'''

from time import sleep
from random import choice

answers = [ 'It is certain.', ' It is decidedly so.', 'Without a doubt', 'Yes-definitely',
            'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
            'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
            'Cannot predict now.', 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.',
            'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

def answer():
    ''' Generate the answer for the question made by user.
        Display thinking time and format.
    '''
    question = input('Enter your question:\n')
    sleep(1)
    print('Thinking...')
    sleep(2)
    print(choice(answers))
    return 0

while True:
    answer()
    flag = input('Ask another question Yes/No?\n')
    if flag.lower() == 'Yes' or flag == 'y':
        continue
    else:
        break
