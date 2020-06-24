# Beginner project 3.
'''
Simulate a magic 8-ball.
Allow the user to enter their question.
Display an in progress message(i.e. "thinking").
Create 20 responses, and show a random response.
Allow the user to ask another question or quit.
Bonus:
    Add a gui.
    It must have box for users to enter the question.
    It must have at least 4 buttons:
        ask
        clear (the text box)
        play again
        quit (this must close the window)
'''
from time import sleep
from random import choice
import tkinter as tk
from tkinter import messagebox

def ask():
    """Ask the question to the magic ball and insert the
    answer into lbl_answer.
    """
    answers = ['It is certain.', ' It is decidedly so.', 'Without a doubt', 'Yes-definitely',
            'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
            'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
            'Cannot predict now.', 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.',
            'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

    question = ent_question.get()
    
    if question:
        lbl_answer["text"] = f'{choice(answers)}'
        btn_ask["state"] = 'disabled'
    else:
        messagebox.showwarning(message="Question field empty!", title="Empty field")

def clear():
    """
    Clear and enable the text box.
    """
    ent_question.delete(0, 'end')

def play_again():
    """
    Clear answer label and enable the ask button to play again.
    """
    lbl_answer["text"] = ''
    btn_ask["state"] =  'normal'

def close():
    """
    Exits the program.
    """
    window.destroy()

window = tk.Tk()
window.title('Magic ball')

# Create a question frame: label and entry
frm_question = tk.Frame(master=window)
ent_question = tk.Entry(master=frm_question,state='normal', width=60)
lbl_question = tk.Label(master=frm_question, text='Your question: ')

# Create buttons frame and organize.
frm_buttons = tk.Frame(master=window)

btn_ask = tk.Button(frm_buttons, state='normal', text='Ask!', command=ask)
btn_clear = tk.Button(frm_buttons, text='Clear text box', command=clear)
btn_again = tk.Button(frm_buttons, text='Play again', command=play_again)
btn_quit = tk.Button(frm_buttons, text='Quit', command=close)

btn_ask.grid(row=0, column=0, padx=20, pady=10)
btn_clear.grid(row=0, column=1, padx=20, pady=10)
btn_again.grid(row=0, column=2, padx=20, pady=10)
btn_quit.grid(row=0, column=3, padx=20, pady=10)

# Create answer label.
lbl_answer = tk.Label(master=window, text='')

# Organize question entry and label, and answer label.
ent_question.grid(row=0, column=1, sticky='w')
lbl_question.grid(row=0, column=0, sticky='e')
lbl_answer.grid(row=1, column=0, padx=10, sticky='nw')

# Organize question and buttons frame.
frm_question.grid(row=0, column=0, padx=10)
frm_buttons.grid(row=2, column=0, padx=10)

# Execute main loop.
window.mainloop()
