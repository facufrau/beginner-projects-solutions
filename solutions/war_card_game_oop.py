#Beginner project 15 - War card game.
'''
War (also known as Battle in the United Kingdom) is a card game typically played by two players.
It uses a standard playing card deck. The objective of the game is to win all of the cards.

The deck is divided evenly among the players, giving each a down stack.
In unison, each player reveals the top card of their deck—this is a "battle"—and
the player with the higher card takes both of the cards played and moves them to their stack.
Aces are high, and suits are ignored.

If the two cards played are of equal value, then there is a "war".
Both players place the next card of their pile face down (some variants have three face down cards)
and then another card face-up. The owner of the higher face-up card wins the war and adds all the
cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle
repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.

Finally, Those who collect the 52 cards at first is declared as the winner !!!

Subgoals:
    Create a "Replay" option.
'''
import random
from time import sleep
import more_itertools as mit
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
                self.cards.append(Card(s, ranks[v-1], v))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player():
    '''
    A class for representing players in card game.
    '''
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    def play_card(self):
        ''' Plays the first card in hand list.'''
        if not self.hand:
            return None
        else:
            amount = len(self.hand) - 1
            return self.hand.pop(random.randint(0, amount))


print("--------Welcome to the war game--------")

# Create objects for the game and initialize values.
player1 = Player(input("Enter the 1st player name: "))
player2 = Player(input("Enter the 2nd player name: "))
deck = Deck()
deck.shuffle()

# Divide half of the cards for each player.
for i in range(len(deck.cards)):
    if i % 2 == 0:
        player1.draw(deck)
    else:
        player2.draw(deck)

# Create a list with 2 sublists, for each player to store played cards.
board_cards = [[],[]]

def append_cards(player_name, board):
    '''Append all cards to the player who wins the round.'''
    for sublist in board:
        for c in sublist:
            player_name.hand.append(c)

# Each player plays one card and check the value.
def play_round():
    sleep(0.001)
    global board_cards
    board_cards[0].append(player1.play_card())
    board_cards[1].append(player2.play_card())

    if mit.last(board_cards[0]).val > mit.last(board_cards[1]).val:
        cards_qty = len(board_cards[0]) + len(board_cards[1])
        print(f'{player1.name} wins this round and take {cards_qty} cards')
        append_cards(player1, board_cards)
        board_cards = [[],[]]

    elif mit.last(board_cards[0]).val < mit.last(board_cards[1]).val:
        cards_qty = len(board_cards[0]) + len(board_cards[1])
        print(f'{player2.name} wins this round and take {cards_qty} cards')
        append_cards(player2, board_cards)
        board_cards = [[],[]]
    else:
        print(f'The round ended in tie, each player plays 2 more cards:\none facing up and one facing down')
        board_cards[0].append(player1.play_card())
        board_cards[1].append(player2.play_card())
        play_round()

#Loop until one of each player has all the cards.
while True:
    play_round()
    print(f'{player1.name} has {len(player1.hand)} cards')
    print(f'{player2.name} has {len(player2.hand)} cards')

    if len(player1.hand) == 52 and len(player2.hand) == 0:
        print(f'Congratulations {player1.name}! You won the game!\nSorry, {player2.name} you lost the game...')
        break

    elif len(player2.hand) == 52 and len(player1.hand) == 0:
        print(f'Congratulations {player2.name}! You won the game!\nSorry, {player1.name} you lost the game...')
        break