'''
Maths Snake
Jaynik Parsotomo
Version 1.4
'''
from tkinter import *


def createNav(frame):
    def BuildHome():
        ChangePage("home")
    home = Button(frame, text="Home",bg='blue', fg='yellow',command=BuildHome,font=('Fixedsys',15, 'bold') )
    home.config(height=5, width=10)
    home.grid(column=0, row=0, sticky=(W, E))

        
def ChangePage(page):
    if page == "home":
        ClearWindow()
        createTitle(title,"Maths Snake")
        createHome(body)

        
def createTitle(frame,title):
    title = Label(frame, text=title, bg='black', fg='red', font=('Fixedsys',20, 'bold'))
    title.grid(column=0, row=0, sticky=(W, E))

def progress():
    ClearWindow()
    createTitle(title,"Progress:")


def howToPlay():
    ClearWindow()
    createTitle(title,"How To Play:")


def createPlayMenu():
    ClearWindow()
    createTitle(title,"Select Difficulty:")
    
def setTitle(root, title):
    root.title(title)
    
def ClearWindow():
     for widget in Frame.winfo_children(body):
          widget.grid_forget()
     for widget in Frame.winfo_children(title):
          widget.grid_forget()
          
def createHome(frame):
    
    playButton = Button(body,text = "PLAY", fg='white', bg='purple1', command=createPlayMenu,font=('Fixedsys',20, 'bold'))
    playButton.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=4)

    progressButton = Button(body,text = "PROGRESS",fg='white', bg='green3',command=progress,font=('Fixedsys',20, 'bold'))
    progressButton.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=4)

    howToPlayButton = Button(body,text = "HOW TO PLAY", fg='white', bg='green3', command=howToPlay,font=('Fixedsys',20, 'bold'))
    howToPlayButton.grid(column=0, row=3, sticky =(N,W,E,S),columnspan=4)

    highScore = Button(body,text="HIGH SCORE",fg="white",bg="green3", command=highScoreList,font=('Fixedsys',20, 'bold'))
    highScore.grid(column=0, row=4, sticky =(W,E), columnspan=4)

    exitButton = Button(body,text = "EXIT",fg='white', bg='red',command=exit,font=('Fixedsys',20, 'bold'))
    exitButton.grid(column=0, row=5,sticky =(N,W,E,S), columnspan=4)

def highScoreList():
    ClearWindow()
    createTitle(title,"High Score List:")
    
root = Tk()
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

nav = Frame(root, borderwidth=2, relief="sunken", bg="white")
nav.grid(column=0, row=0, rowspan = 2, sticky=(N, S))

title = Frame(root, borderwidth=2, relief="sunken")
title.grid(column=1, row=0, sticky=(N, E, W))
title.columnconfigure(0, weight=1)

body = Frame(root, borderwidth=2, relief="sunken", bg="white")
body.grid(column=1, row=1, sticky=(N, W, E, S))
body.columnconfigure(0, weight=1)

root.resizable(width=False, height=False)
#root.state("zoom")
root.geometry('{}x{}'.format(800, 600))

createNav(nav)
ChangePage("home")
root.mainloop()
