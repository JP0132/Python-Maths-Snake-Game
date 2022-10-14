'''
Maths Snake Game
Version 2.1
Jaynik Parsotomo
'''

from tkinter import *
from random import randint
import random

easyQuestions = ['10 + 3', '2+2', '14-3','16+2','19-1']
easyAnswers = ['13', '4','11','18','18']

easyIndex = random.choice(range(len(easyQuestions)))
eQ = easyQuestions[easyIndex]
eA = easyAnswers[easyIndex]

class Question():
    def __init__(self, master=None):
        
        self.root = Tk()
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)

        self.v = StringVar(master, 0)
        self.v.set(eQ)

        self.root.resizable(width=False, height=False)
        self.root.geometry('{}x{}'.format(400, 300))

        self.label = Label(self.root, textvariable=self.v)
        self.label.grid(row = 0, column = 0)

        self.e = Entry(self.root)
        self.e.grid(row = 1, column=0)

        self.answer = eA
    
        self.submit = Button(self.root, text="submit", width=10, command = self.save)
        self.submit.grid(row = 2, column = 0)

    def save(self):
            if self.e.get() == self.answer:
                self.root.destroy()

            else:
                self.root.destroy()

Question()
