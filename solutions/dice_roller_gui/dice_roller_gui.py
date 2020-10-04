#Beginner project 18.1 - Dice roller
#Alternative to N°18 - GUI version of dice roller

'''
Dice Rolling Simulator

Bonus:
    You are about to play a board game, but you realize you don't have any dice.
    Fortunately you have this program.
    Create a program that opens a new window and draws 2 six-sided dice
    Allow the user to quit, or roll again
    Allow the user to select the number of dice to be drawn on screen(1-4)
    Add up the total of the dice and display it
'''
import random
import PySimpleGUI as sg

sg.theme("DarkAmber")

#Layout
layout = [ [sg.Text('N° of dice: '), sg.InputText()],
           [sg.Text('Results: '), sg.Text('')],
           [sg.OK(), sg.Cancel()] ]
#Create a window
window = sg.Window('Dice Roller', layout)
#Event loop to process "events"
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    
window.close()

'''
while True:
    ask = input("Do you want to roll the dice again? (y/n): ")
    if ask.lower() in ['y','yes']:
        break
    elif ask.lower() in ['n', 'no']:
        again = False
        break
    else:
        print("Please enter 'y' or 'n'")
'''
