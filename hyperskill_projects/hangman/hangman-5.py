from random import choice

print("H A N G M A N")

words = ('python', 'kotlin', 'javascript', 'java')
secret_word = choice(words)
word_guess = ['-' for _ in range(len(secret_word))]
letters = set(secret_word)

lives = 8
while lives > 0:
    print("\n" + "".join(word_guess))
    guess = input("Input a letter: ")
    if guess in letters:
        for i in range(len(secret_word) - 1):
            if guess == secret_word[i]:
                word_guess[i] = guess
    else:
        print("That letter doesn't appear in the word")
    lives -= 1
    
print("\nThanks for playing!\nWe'll see how well you did in the next stage")
