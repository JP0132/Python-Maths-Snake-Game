'''
Maths Snake
Jaynik Parsotomo
Version 1.3
'''

from tkinter import *

def createNav(frame):
    def BuildHome():
        ChangePage("home")
    home = Button(frame, text="Home",bg='blue', fg='yellow',command=BuildHome)
    home.config(height=5, width=10)
    home.grid(column=0, row=0, sticky=(W, E))

        
def ChangePage(page):
    if page == "home":
        ClearWindow()
        createTitle(title,"Maths Snake")
        createMainMenu(body)

        
def createTitle(frame,title):
    title = Label(frame, text=title, bg='black', fg='red', font=('Arial',20, 'bold'))
    title.grid(column=0, row=0, sticky=(W, E))

def setTitle(root, title):
    root.title(title)
    
def ClearWindow():
     for widget in Frame.winfo_children(body):
          widget.grid_forget()
     for widget in Frame.winfo_children(title):
          widget.grid_forget()
          
def createMainMenu(frame):
    
    playButton = Button(body,text = "PLAY", fg='white', bg='#00B200')
    playButton.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=2)

    progressButton = Button(body,text = "PROGRESS",fg='white', bg='#00B200')
    progressButton.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=2)

    howToPlayButton = Button(body,text = "HOW TO PLAY", fg='white', bg='#00B200')
    howToPlayButton.grid(column=0, row=3, sticky =(N,W,E,S),columnspan=2 )

    highScore = Button(body,text="HIGH SCORE",fg="white",bg="#00B200")
    highScore.grid(column=0, row=4, sticky =(W,E), columnspan=4)

    exitButton = Button(body,text = "EXIT",fg='white', bg='red')
    exitButton.grid(column=0, row=5,sticky =(N,W,E,S), columnspan=4)

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
root.geometry('{}x{}'.format(800, 600))

createNav(nav)
ChangePage("home")
root.mainloop()
