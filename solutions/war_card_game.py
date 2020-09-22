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

play = True
while play:

    # Build a dictionary with a deck of cards.
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = []
    DECK_VALUE = {}
    for s in suits:
        for n in numbers:
            deck.append(n + ' of ' +s)
            DECK_VALUE[n + ' of ' +s] = numbers.index(n) + 1
    random.shuffle(deck)

    print('Welcome to the war-card game.')
    # Get name of the players and initialize player hands.
    while True:
        player_1 = input('Player 1 name: ')
        player_2 = input('Player 2 name: ')

        if player_1 != player_2:
            player_1_cards = []
            player_2_cards = []
            break

    player_1_cards = deck[:len(deck)//2]
    player_2_cards = deck[len(deck)//2:]
    player_1_pile = []
    player_2_pile = []
    round = 1

    while player_1_cards or player_2_cards:
        card_1 = player_1_cards.pop(random.randint(0, len(player_1_cards) - 1))
        card_2 = player_2_cards.pop(random.randint(0, len(player_2_cards) - 1))
        print(card_1)
        print(card_2)

        if DECK_VALUE[card_1] == DECK_VALUE[card_2]:
            player_1_pile.append(card_1)
            try:
                player_1_pile.append(player_1_cards.pop())
            except:
                print(f'{player_1} lost...\n{player_2} wins!!')

            player_2_pile.append(card_2)
            try:
                player_2_pile.append(player_2_cards.pop())
            except:
                print(f'{player_2} lost...\n{player_1} wins!!')

        elif DECK_VALUE[card_1] > DECK_VALUE[card_2]:

            player_1_pile.extend(player_2_pile)
            for c in player_1_pile:
                player_1_cards.insert(0, c)

            player_1_cards.insert(0, card_1)
            player_1_cards.insert(0, card_2)

            player_1_pile = []
            player_2_pile = []

        elif DECK_VALUE[card_1] < DECK_VALUE[card_2]:

            player_2_pile.extend(player_1_pile)
            for c in player_2_pile:
                player_2_cards.insert(0, c)

            player_2_cards.insert(0, card_1)
            player_2_cards.insert(0, card_2)

            player_1_pile = []
            player_2_pile = []

        print(f'Round: {round}')
        print(f'{player_1}: {len(player_1_cards)} cards, {len(player_1_pile)} pile')
        print(f'{player_2}: {len(player_2_cards)} cards, {len(player_2_pile)} pile')
        #input('Press enter to continue round')
        round += 1

        if len(player_1_cards) == 0:
            print(f'{player_1} lost... {player_2} won!!')
            break
        elif len(player_2_cards) == 0:
            print(f'{player_2} lost... {player_1} won!!')
            break
    again = input('Do you want to play again? yes/no:  ')
    if again.lower() in ['no', 'n']:
        play = False