#Beginner project 24 - Variant of 21.
'''
A Variation of 21

If you do not know how 21 (AKA Blackjack) is played, reading the first couple of paragraphs of this wikipedia article may be beneficial.

In this project, you will make a game similar to Blackjack. In this version:

    There is only one player.
    There are two types of scores: the game score and the round score.
    The game score will begin at 100, and the game will last for five rounds.
    At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the player's round score.
    From here, the player has two options - draw another card to try to get their round score closer to 21, or they can end the round.
    The player can draw as many cards as they want until they end the round or their round score exceeds 21.
    At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins. After the five rounds, the player is given their total score and the game is over. ---Other Information About The Game---
    Aces are only worth 1.
    If a player busts, 21 is subtracted from their total score.
    All face cards are worth 10.
    So the point of your program is to allow the user to play the game described above.
    Subgoals:
        At the beginning of each round, print the round number (1 to 5).

        Since this is a text base game, tell the user what is happening. For example, tell him/her when he/she draws a card,
        the name of the card, when they bust, etc.

        Create a ranking system at the end of the game and tell the user their rank.
        For example, if the player finishes with less than 50 points they get an F,
        if they get between 50-59 points they get an E, 60-69 is a D, 70-79 is a C,
        80-89 is a B, and 90-100 is an A.

        At the end of each round, print out the user's total score.

        This may be the hardest part of the project, depending on how you wrote it.
        Make sure the deck has 4 of each type of card, and then remove cards as they are drawn.
        At the end of each round, make the deck have all of the cards again.

'''
import random
from time import sleep

#Create a Card and Deck classes.
class Card:
    '''
    A class for representing a single card.
    '''
    def __init__(self, suit, rank, val):
        self.suit = suit
        self.rank = rank
        self.val = val

    def show(self):
        print(f'{self.rank} of {self.suit} - value {self.val}')

class Deck:
    '''
    A class for representing a 52 card Deck.
    '''
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in range(1,14):
                if v < 10:
                    self.cards.append(Card(s, ranks[v-1], v))
                else:
                    # All faces card have a value of 10.
                    value = 10
                    self.cards.append(Card(s, ranks[v-1], value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

def main():
    """Main function for the game."""
    print("Welcome to the 21 variant game.")
    input("Press enter to continue: ")
    # The player starts with 100 points.
    game_score = 100

    # Loop for playing 5 rounds.
    for i in range(5):
        # Initialize and shuffle deck, each round starts with all cards.
        deck = Deck()
        deck.shuffle()

        # Start round and give 2 cards to user, calculate round score.
        print(f"-----------\nRound {i+1}\n-----------")
        player_hand = [deck.draw_card() for i in [1,2]]
        sleep(1)
        print(f"You drew: ")
        sleep(1)
        player_hand[0].show()
        player_hand[1].show()
        round_score = player_hand[0].val + player_hand[1].val

        # Loop for playing the round after starting draw of 2 cards.
        while True:
            print(f"Current score {round_score}")

            # Verify that the user enters allowed inputs.
            options = ['1','2']
            while True:
                choice = input("Enter: 1 - Draw another card   or   2 - End round\n")
                if choice in options:
                    break
                else:
                    print("Please enter only '1' or '2'")

            # Draw a new card.
            if choice == '1':
                card = deck.draw_card()
                sleep(1)
                print(f"You drew ")
                card.show()
                round_score += card.val

                # Check if the score is more than 21 then end round.
                if round_score > 21:
                    lost_points = 21
                    sleep(1)
                    print(f"You busted with a score of {round_score}, you lose 21 points")
                    break

            # End current round.
            elif choice == '2':
                lost_points = 21 - round_score
                sleep(1)
                print(f"Your round score was {round_score} and you lose {lost_points} points")
                break

        game_score -= lost_points
        print(f"Your current game score is {game_score} points.")

    print("------------\nGame ended\n------------")
    print(f"Your final score is {game_score}")
    if game_score >= 90:
        print("Your rank is: A")
    elif game_score >= 80:
        print("Your rank is: B")
    elif game_score >= 70:
        print("Your rank is: C")
    elif game_score >= 60:
        print("Your rank is: D")
    elif game_score >= 50:
        print("Your rank is: E")
    else:
        print("Your rank is F")

if __name__ == '__main__':
    main()