#Beginner project 23 - Turn Based Pokemon Style Game.
'''
Write a simple game that allows the user and the computer to take turns selecting moves to use against each other.
Both the computer and the player should start out at the same amount of health (such as 100),
and should be able to choose between the three moves:
    The first move should do moderate damage and has a small range (such as 18-25).
    The second move should have a large range of damage and can deal high or low damage (such as 10-35).
    The third move should heal whoever casts it a moderate amount, similar to the first move.
After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. Once the user or the computer's health reaches 0, the game should end.
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
        print(f"{self.name} health: {self.health}")

    def small_hit(self, Player):
        """
        Do moderate damage to another player, with small range (18-25)
        Updates target player.health attribute.
        If the value is <= 0, returns 0 instead.
        """
        Player.health -= random.randint(18,25)
        if Player.health <= 0:
            Player.health = 0

    def charged_hit(self, Player):
        """
        This moves does more damage and has a wider range.
        Updates target Player.health attribute.
        If the value is <= 0, returns 0 instead.
        """
        Player.health -= random.randint(10,35)
        if Player.health <= 0:
            Player.health = 0

    def heal(self):
        """
        This moves heal the player that uses by a moderate amount (14-22).
        Updates self attribute.
        """
        self.health += random.randint(14,22)
        if self.health >= 100:
            self.health = 100

class computer(Player):


p1 = Player('Facu')
p2 = Player('ai')


