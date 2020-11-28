from random import choice

print("H A N G M A N")

words = ('python', 'kotlin', 'javascript', 'java')
secret_word = choice(words)
hint = secret_word[:3] + (len(secret_word) - 3) * '-'

guess = input(f"Guess the word: {hint}")
if guess == secret_word:
    print("You survived!")
else:
    print("You lost!")
