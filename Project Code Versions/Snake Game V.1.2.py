'''
Maths Snake
Jaynik Parsotomo
Version 1.2
'''
from tkinter import *
from tkinter import ttk

def playMenu():

    main = ttk.Frame(root, width=800, height=600, padding=(5,5,5,5))
    main.grid(column=0, row=0, sticky=(N,W,E,S))
    
    title = Label(main, text = "SELECT DIFFICULTY LEVEL:", fg = 'red', compound='center')
    title.grid(column=0, row=0)

    easyButton = Button(main, text = "EASY", fg='white', bg='#00B200', command=easy)
    easyButton.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=2)

    mediumButton = Button(main,text = "MEDIUM", fg='white', bg='orange', command=medium)
    mediumButton.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=2)

    hardButton = Button(main,text = "HARD", fg='white', bg='red',command=hard)
    hardButton.grid(column=0, row=3, sticky =(N,W,E,S), columnspan=2)

    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 600))
    root.mainloop()

def easy():
    
    main = ttk.Frame(root,width=800, height=600, padding=(5,5,5,5))
    main.grid(column=0, row=0, sticky=(N,W,E,S))

    title = Label(main, text = "EASY:", fg = 'red')
    title.grid(column=0, row=0)

    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 600))
    root.mainloop()

def medium():
    
    main = ttk.Frame(root,width=800, height=600, padding=(5,5,5,5))
    main.grid(column=0, row=0, sticky=(N,W,E,S))

    title = Label(main, text = "MEDIUM:", fg = 'red')
    title.grid(column=0, row=0)

    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 600))
    root.mainloop()
    
def hard():
    
    main = ttk.Frame(root, width=800, height=600, padding=(5,5,5,5))
    main.grid(column=0, row=0, sticky=(N,W,E,S))

    title = Label(main, text = "HARD:", fg = 'red')
    title.grid(column=0, row=0)

    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 600))
    root.mainloop()

    
def progress():
    
    main = ttk.Frame(root, width=800, height=600, padding=(5,5,5,5))
    main.grid(column=0, row=0, sticky=(N,W,E,S))

    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(0,weight=1)
    
    title = Label(main, text = "PROGRESS:", fg = 'red')
    title.grid(column=0, row=0)

    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 600))
    root.mainloop()

def howToPlay():
    
    main = ttk.Frame(root, width=800, height=600, padding=(5,5,5,5))
    main.grid(column=0, row=0, sticky=(N,W,E,S))

    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(0,weight=1)
    
    title = Label(main, text = "HOW TO PLAY:", fg = 'red')
    title.grid(column=0, row=0)

    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 600))
    root.mainloop()

def highScore():
    main = ttk.Frame(root, width=800, height=600, padding=(5,5,5,5))
    main.grid(column=0, row=0, sticky=(N,W,E,S))

    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(0,weight=1)
    
    title = Label(main, text = "High Score:", fg = 'red')
    title.grid(column=0, row=0)

    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 600))
    root.mainloop()



root = Tk()
main = ttk.Frame(root, width=800, height=600, padding=(5,5,5,5))
main.grid(column=0, row=0, sticky=(N,W,E,S))

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

title = Label(main,text = "MATH SNAKE", fg = 'red', compound = 'center')
title.grid(column=0, row=0)

playButton = Button(main,text = "PLAY", fg='white', bg='purple1', command=playMenu)
playButton.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=2)

progressButton = Button(main,text = "PROGRESS",fg='white', bg='green3',command=progress)
progressButton.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=2)

howToPlayButton = Button(main,text = "HOW TO PLAY", fg='white', bg='green3',command=howToPlay)
howToPlayButton.grid(column=0, row=3, sticky =(N,W,E,S),columnspan=2 )

highScoreButton = Button(main, text = "HIGH SCORE", fg='white', bg='green3',command=highScore)
highScoreButton.grid(column=0, row=4, sticky =(N,W,E,S),columnspan=2 )

exitButton = Button(main,text = "EXIT",fg='white', bg='red', command=exit)
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
