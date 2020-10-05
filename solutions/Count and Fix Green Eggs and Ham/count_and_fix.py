#Beginner project 19 - Count and fix "Green eggs and ham"
'''
Count and Fix Green Eggs and Ham

Some of you may remember the Dr. Sues story "Green Eggs and Ham".

However, there is a problem with the story I gave you - every time the word I is used, it is lowercase.
Because of this problem, your job is to do the following:

    Copy the story I gave you into a regular text file.
    Create a program that reads through the story and makes the letter i uppercase any time it should be.
        (Make sure to change it when it's used in sam-I-am's name too.)
    Have your program make a new file, and have it write out the story correctly.
    Print out how many errors were corrected.
    When you're finished, you should have corrected this many errors.

'''
import os

def check_word(word):
    '''
    Checks word and replaces the lowecase "i" to uppercase "I"
    '''
    if str(word) == "i":
        return "I", 1
    elif str(word) == "Sam-i-am" or str(word)[:-1] == "Sam-i-am":
        return ("Sam-I-am" + str(word[-1:])), 1
    else:
        return str(word), 0

p = 'ENTER FILEPATH HERE'

text = []
with open(os.path.join(p, 'text_with_errors.txt')) as f:
    count = 0
    lines = f.readlines()

    for line in lines:
        for word in line.split():
            replaced, value = check_word(word)
            text.append(replaced)
            count += value
            text.append(' ')
        text.append('\n')

    with open(os.path.join(p, 'text_corrected.txt'), 'w') as new_file:
        new_file.writelines(text)

print(f'This program made {count} replaces')