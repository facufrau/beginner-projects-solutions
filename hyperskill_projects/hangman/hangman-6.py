from random import choice

print("H A N G M A N")

words = ('python', 'kotlin', 'javascript', 'java')
secret_word = choice(words)
word_guess = ['-' for _ in range(len(secret_word))]
letters = set(secret_word)

lives = 8
while lives > 0:
    print()
    guessed = "".join(word_guess)
    print(guessed)
    guess = input("Input a letter: ")

    # Check the letter entered and reduce lives.
    if guess not in letters:
        lives -= 1
        print("That letter doesn't appear in the word")
    else:
        if guess not in word_guess:
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    word_guess[i] = guess
        else:
            lives -= 1
            print("No improvements")
    
    # Check if guessed the word.
    if guessed == secret_word:
        break

if guessed == secret_word:
    print("You guessed the word!")
    print("You survived!")
else:
    print("You lost!")