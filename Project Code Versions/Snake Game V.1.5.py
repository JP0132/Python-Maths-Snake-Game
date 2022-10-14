'''
Maths Snake
Jaynik Parsotomo
02/11/18
Version 1.5
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

    instructionsTitle = Label(body, text="Instructions",height=1, width=5,fg="blue",bg='yellow',font=('Fixedsys',25,'bold'))
    instructionsTitle.grid(column=0, row=2, sticky =(W,E))

    '''
    instructionsTitle.configure(state='normal')
    instructionsTitle.insert(END,"Instructions:")
    instructionsTitle.configure(state='disabled')
    '''
    instructions =  Text(body, height=10, width=5,fg="blue",font=('Fixedsys',14))
    instructions.grid(column=0, row=3, sticky =(N,W,E,S))
    instructions.configure(state='normal')
    introGame = """
 The aim of the game is to control the snake to the correct answer to the question,
 gaining points if the answer was right. You have 3 lives, and you lose a life
 everytime you get a answer wrong or eat yourself.
    
 It is game over once you have lost all your lives!

 You can access the questions within Progress on the homepage.
    """
    instructions.insert(END,introGame)
    instructions.configure(state='disabled')

    '''
    scroll = Scrollbar(body, orient="vertical",command=instructions.yview)
    scroll.grid(column=1, row=3, sticky='nw')
    instructions.configure(yscrollcommand=scroll.set)
    '''
    
    #control = Text(body, height=5, width=5)
    #control.grid(column=0,row=4,sticky='nw')
    photo = PhotoImage(file = "arrowkeys.gif")
    label = Label(body,image=photo)
    label.image = photo
    label.grid(column=0, row=4)
    #image.grid(column=0, row=4)
    #display = PhotoImage(image)
    #control.insert(END, display)

 
def exitGame():
    ClearWindow()
    createTitle(title,"Exit?")

    yes = Button(body,text = "YES", fg='white', bg='red', command=quit, font=('Fixedsys',20, 'bold'))
    yes.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=2)

    no = Button(body,text = "NO", fg='white', bg='#00B200',font=('Fixedsys',20, 'bold'))
    no.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=2)

def selectDifficulty():
    ClearWindow()
    createTitle(title,"Select Difficulty:")
    
    easyButton = Button(body, text = "EASY", fg='white', bg='#00B200', command=easy,font=('Fixedsys',20, 'bold') )
    easyButton.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=2)

    mediumButton = Button(body,text = "MEDIUM", fg='white', bg='orange', command=medium,font=('Fixedsys',20, 'bold'))
    mediumButton.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=2)

    hardButton = Button(body,text = "HARD", fg='white', bg='red', command=hard,font=('Fixedsys',20, 'bold'))
    hardButton.grid(column=0, row=3, sticky =(N,W,E,S), columnspan=2)
    
def setTitle(root, title):
    root.title(title)
    
def ClearWindow():
     for widget in Frame.winfo_children(body):
          widget.grid_forget()
     for widget in Frame.winfo_children(title):
          widget.grid_forget()
          
def createHome(frame):
    
    playButton = Button(body,text = "PLAY", fg='white', bg='purple', command=selectDifficulty,font=('Fixedsys',20, 'bold'))
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

def easy():
    ClearWindow()
    createTitle(title,"Maths Snake (Easy):")

def medium():
    ClearWindow()
    createTitle(title,"Maths Snake (Medium):")

def hard():
    ClearWindow()
    createTitle(title,"Maths Snake (Hard):")
 


 
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
