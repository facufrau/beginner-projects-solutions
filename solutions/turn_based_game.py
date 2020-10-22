#Beginner project 23 - Turn Based Pokemon Style Game.
'''
Write a simple game that allows the user and the computer to take turns selecting moves to use against each other.
Both the computer and the player should start out at the same amount of health (such as 100),
and should be able to choose between the three moves:
    The first move should do moderate damage and has a small range (such as 18-25).
    The second move should have a large range of damage and can deal high or low damage (such as 10-35).
    The third move should heal whoever casts it a moderate amount, similar to the first move.
After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. 
Once the user or the computer's health reaches 0, the game should end.
Subgoals:
    When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
    When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
    Give each move a name.
'''
import random

class Player:
    """ A class for representing a player in a turn based game."""
    def __init__(self, name):
        self.name = name
        self.health = 100

    def __str__(self):
        return f"{self.name} has {self.health} health"

    def show_health(self):
        print(f"-//- {self.name} -- Health: {self.health} -//-")

    def small_hit(self, Player):
        """
        Do moderate damage to another player, with small range (18-25)
        Updates target player.health attribute.
        If the value is <= 0, returns 0 instead.
        """
        damage = random.randint(18,25)
        print(f"{self.name} used Small Hit - Damage: {damage}")
        Player.health -= damage
        if Player.health <= 0:
            Player.health = 0

    def charged_hit(self, Player):
        """
        This moves does more damage and has a wider range(10-35).
        Updates target Player.health attribute.
        If the value is <= 0, returns 0 instead.
        """
        damage = random.randint(10,35)
        print(f"{self.name} used Charged Hit - Damage {damage}")
        Player.health -= damage
        if Player.health <= 0:
            Player.health = 0

    def heal(self):
        """
        This moves heal the player that uses by a moderate amount (14-22).
        Updates self attribute.
        """
        heal = random.randint(14,22)
        print(f"{self.name} used Heal - Recovered: {heal}")
        self.health += heal
        if self.health >= 100:
            self.health = 100

class Computer(Player):
    """
    A class for representing a computer(AI) player.
    The computer will choose random moves with equal probability(33% each), if its health < 35,
    the heal move will have increased probability(30%-30%-40%)
    """
    def play(self, target):
        """Choose a move at random"""
        if self.health < 35:
            move = random.randint(1,10)
        else:
            move = random.randint(1,9)

        if 1 <= move <= 3:
            self.small_hit(target)
        elif 4 <= move <= 6:
            self.charged_hit(target)
        else:
            self.heal()

def ask_move():
    """
    Ask a player which move wants to use, print choices.
    Hands exceptions and checks adequate input (only numbers 1, 2 and 3)
    """
    while True:
        move = input("Choose a move to use (enter 1, 2 or 3)\n1 - Small Hit(18,25)    2 - Charged Hit(10,35)    3 - Heal(14,22)\n")
        try:
            move = int(move)
            if move in [1,2,3]:
                break
        except:
            print("Please enter 1, 2 or 3")
    return move
    
            
def main():
    again = True
    while again:
        """ Main function for the game."""
        print("User vs AI turn based game")
        # Create the instances of Player and Computer objects.
        player_name = input("Enter your name: ")
        ai = Computer('Computer')
        player = Player(player_name)
        # Show starting values.
        player.show_health()
        ai.show_health()

        while True:
        # Ask the player for a move.
            player_move = ask_move()
            if player_move == 1:
                player.small_hit(ai)
            elif player_move == 2:
                player.charged_hit(ai)
            else:
                player.heal()
            # Make AI move.
            ai.play(player)
            # Show status after both players played.
            player.show_health()
            ai.show_health()
            # Check if one of the players health is 0.
            if player.health == 0:
                print(f"The player {player.name} lost - The computer wins")
                break
            elif ai.health == 0:
                print(f"Player {player.name} wins! - The computer lost")

        while True:
            flag = input("Do you want to play again? (y/n):  ")
            if flag.lower() in ['y','yes']:
                break
            elif flag.lower() in ['n', 'no']:
                again = False
                break

if __name__ == '__main__':
    main()