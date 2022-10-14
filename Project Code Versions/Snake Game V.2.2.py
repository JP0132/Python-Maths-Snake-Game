'''
Maths Snake Game
Version 2.2
Jaynik Parsotomo
'''

from tkinter import *
from random import randint
import random
import pickle

easyQuestions = ['10 + 3', '2+2', '14-3','16+2','19-1']
easyAnswers = ['13', '4','11','18','18']

easyIndex = random.choice(range(len(easyQuestions)))
eQ = easyQuestions[easyIndex]
eA = easyAnswers[easyIndex]

print(easyIndex)

rightE = 'rightE2.pk'
wrongE = 'wrongE2.pk'

rightTrackerE = [0,0,0,0,0]
wrongTrackerE = [0,0,0,0,0]

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
                value = rightTrackerE.pop(easyIndex)
                track = value + 1
                rightTrackerE.insert(easyIndex, track)
                print(rightTrackerE)
                with open(rightE, 'wb') as fp:
                    pickle.dump(rightTrackerE, fp)
                
                

            else:
                self.root.destroy()
                value = wrongTrackerE.pop(easyIndex)
                track = value + 1
                wrongTrackerE.insert(easyIndex, track)
                print(wrongTrackerE)
                with open(wrongE, 'wb') as fp:
                    pickle.dump(wrongTrackerE, fp)
            

Question()
with open(rightE, "rb") as fp:
    rightTrackerE = pickle.load(fp)

with open(wrongE, "rb") as fi:
    wrongTrackerE = pickle.load(fi)
