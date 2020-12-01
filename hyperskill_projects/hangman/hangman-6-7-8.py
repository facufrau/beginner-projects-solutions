from random import choice
import sys

def play():
    words = ('python', 'kotlin', 'javascript', 'java')
    secret_word = choice(words)
    word_guess = ['-' for _ in range(len(secret_word))]
    letters = set(secret_word)

    lives = 8
    letters_entered = []

    while lives > 0:
        print()
        guessed = "".join(word_guess)
        print(guessed)
        
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("You should input a single letter")
            continue
        else:
            if not guess.isalpha() or guess.isupper():
                print("Please enter a lowercase English letter")
                continue
            else:
                if guess in letters_entered:
                    print("You've already guessed this letter")
                    continue
                else:
                    # Check the letter entered and reduce lives.
                    if guess not in letters:
                        lives -= 1
                        print("That letter doesn't appear in the word")
                    else:
                        if guess not in word_guess:
                            for i in range(len(secret_word)):
                                if guess == secret_word[i]:
                                    word_guess[i] = guess
        
        # Add entered letter to previous tries.
        letters_entered.append(guess)

        # Check if guessed the word.
        if guessed == secret_word:
            break

    if guessed == secret_word:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")
    
print("H A N G M A N")
menu = input('Type "play" to play the game, "exit" to quit: ')
if menu == 'play':
    play()
elif menu == 'exit':
    sys.exit()