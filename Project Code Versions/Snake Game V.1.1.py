'''
Maths Snake
Jaynik Parsotomo
Version 1.1
'''
from tkinter import *
from tkinter import ttk

root = Tk()
main = ttk.Frame(root, width=5000, height=5000, padding=(5,5,5,5))
main.grid(column=0, row=0, sticky=(N,W,E,S))

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

title = Label(main,text = "MATH SNAKE", fg = 'red', compound = 'center')
title.grid(column=0, row=0)

playButton = Button(main,text = "PLAY", fg='white', bg='purple')
playButton.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=2)

progressButton = Button(main,text = "PROGRESS",fg='white', bg='green3')
progressButton.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=2)

howToPlayButton = Button(main,text = "HOW TO PLAY", fg='white', bg='green3')
howToPlayButton.grid(column=0, row=3, sticky =(N,W,E,S),columnspan=2 )

highScoreButton = Button(main, text = "HIGH SCORE", fg='white', bg='green3')
highScoreButton.grid(column=0, row=4, sticky =(N,W,E,S),columnspan=2 )

exitButton = Button(main,text = "EXIT",fg='white', bg='red')
exitButton.grid(column=0, row=5,sticky =(N,W,E,S), columnspan=2)

main.grid_columnconfigure(0,weight=1)
main.grid_rowconfigure(0,weight=1)
main.grid_rowconfigure(1,weight=10)
main.grid_rowconfigure(2,weight=10)
main.grid_rowconfigure(3,weight=10)
main.grid_rowconfigure(4,weight=10)

root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 600))
root.mainloop()

