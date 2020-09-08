#Beginner project 14 - Hangman Game
#Based in Al Sweigart - Invent your own computer games with Python Book.
import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    0   |
        |
        |
       ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
   +---+
    0   |
   /|\  |
        |
       ===''', '''
   +---+
    0   |
   /|\  |
   /    |
       ===''', '''
   +---+
    0   |
   /|\  |
   / \  |
       ===''']

words = 'abeja aguila araña avispa ballena bisonte bufalo burro caballo camello canario cangrejo canguro caracol cebra cerdo chimpance ciervo cisne cocodrilo elefante escarabajo escorpion foca gallina gallo gato golondrina hipopotamo hormiga jabali jirafa leon loro mosca mosquito oso oveja perdiz perro pinguino pollo saltamontes serpiente tigre topo toro tortuga vaca zorro'
words = words.split()

def get_random_word(wordlist):
    '''
    Get a random word from a list and returns it.
    '''
    return random.choice(wordlist)

def print_board(missed_letters, correct_letters, secret_word):
    '''
    Prints the board with guessed letters and chances remaining.
    '''
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks: #Print the secret word with spaces in between letters guessed.
        print(letter, end=' ')
    print()

def get_guess(already_guessed):
    '''
    Returns the letter entered by player, this function checks that the user
    only enters a letter and not other characters.
    '''
    while True:
        guess = input('Guess a letter... ')
        guess = guess.lower()

        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess

def play_again():
    '''
    Returns true if player wants to play again, otherwise
    returns false.
    '''
    print('Do you want to play again (yes or no)')
    return input().lower().startswith('y')

# Main function of the game.
def main():
    #Declare and initalize variables.
    print('Welcome to H A N G M A N game')
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words)
    game_done = False

    #Display the board until word is guessed.
    while True:
        print_board(missed_letters, correct_letters, secret_word)

        #Let player enter a letter.
        guess = get_guess(missed_letters + correct_letters)

        #Check if the letter is in the word.
        if guess in secret_word:
            correct_letters += guess

            found_all = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all = False
                    break

            if found_all:
                print(f'Yes! The secret word is "{secret_word}"! You have won.')
                game_done = True

        else:
            missed_letters += guess

            #Check if the player guessed too many times and lost.
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                print_board(missed_letters, correct_letters, secret_word)
                print(f'You have run out of guesses! \nAfter {str(len(missed_letters))} missed guesses and {str(len(correct_letters))} correct guesses, the word was "{secret_word}".')

                game_done = True

        if game_done:
            if play_again():
                missed_letters = ''
                correct_letters = ''
                game_done = False
                secret_word = get_random_word(words)
            else:
                break

if __name__ == '__main__':
    main()
