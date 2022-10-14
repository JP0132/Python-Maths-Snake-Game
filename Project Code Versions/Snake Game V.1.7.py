'''
Maths Snake
Jaynik Parsotomo
Version 1.7
'''
from tkinter import *
import random
from random import randint

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

    questionTitle = Label(body, text="Question", fg="blue",bg='yellow',font=('Fixedsys',20,'bold'))

    questionTitle.grid(column=0,row=2, sticky=(W,E))

    right = Label(body,text="Right", fg="blue",bg='yellow',font=('Fixedsys',20,'bold'))
    right.config(width=10)
    right.grid(column=1,row=2, sticky=(W,E))

    wrong = Label(body,text="Wrong", fg="blue",bg='yellow',font=('Fixedsys',20,'bold'))
    wrong.config(width=10)
    wrong.grid(column=2,row=2, sticky=(W,E))

    answer = Label(body,text="Answer", fg="blue",bg='yellow',font=('Fixedsys',20,'bold'))
    wrong.config(width=10)
    answer.grid(column=3,row=2, sticky=(W,E))
    
def howToPlay():
    ClearWindow()
    createTitle(title,"How To Play:")

    instructionsTitle = Label(body, text="Instructions",height=1, width=5,fg="blue",bg='gold2',font=('Fixedsys',25,'bold'))
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
    
    control = Label(body, text='Controls',fg='blue',font=('Fixedsys',20,'bold'))
    control.grid(column=0, row=4, sticky =(N,W,E,S))
    
    photo = PhotoImage(file = "arrowkeys.gif")
    label = Label(body,image=photo)
    label.image = photo
    label.grid(column=0, row=5,sticky =(N,W,E,S))
    #image.grid(column=0, row=4)
    #display = PhotoImage(image)
    #control.insert(END, display)

    progressTitle = Label(body, text='Progress',fg='blue',font=('Fixedsys',20,'bold'))
    progressTitle.grid(column=0, row=6, sticky =(N,W,E,S))

    progressInstruc = Text(body,fg="dark green",font=('Fixedsys',14))
    progressInstruc.grid(column=0, row=7, sticky =(N,W,E,S))
    progressInstruc.configure(state='normal')
    howToUse = """
 Within the Progress aection you can access the questions within the game
 and view all the answers to the question. You can see the how many times you got
 an question right or wrong. Now you can see the type of questions you keep getting
 wrong
"""
    
    progressInstruc.insert(END,howToUse)
    progressInstruc.configure(state='disabled')

 


def createPlayMenu():
    ClearWindow()
    createTitle(title,"Select Difficulty:")
    
    easyButton = Button(body, text = "EASY", fg='white', bg='green3', command=easy,font=('Fixedsys',20, 'bold') )
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
    
    playButton = Button(body,text = "PLAY", fg='white', bg='purple', command=createPlayMenu,font=('Fixedsys',20, 'bold'))
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

def life():
    life = 3
    
    
def gameBar():
    lifeTracker = Label(body, text='Life',fg ='yellow3',bg='purple', font=('Fixedsys',20))
    lifeTracker.grid(column=0,row=0,sticky =(N,W,E,S))

    scoreTracker = Label(body, text='Score',width = 21, fg='yellow3',bg='DodgerBlue2', font=('Fixedsys',20))
    scoreTracker.grid(column=2,row=0,sticky =(N,W,E,S))
    
def easy():
    ClearWindow()
    createTitle(title,"Maths Snake (Easy):")
    snakeGamePlay(body)

def medium():
    ClearWindow()
    createTitle(title,"Maths Snake (Medium):")

def hard():
    ClearWindow()
    createTitle(title,"Maths Snake (Hard):")

def snakeGamePlay(body):
    snakeCharacter = 'snake'
    foodCharacter = 'food'
    size = {snakeCharacter: 9, foodCharacter: 10}

    
    class snakeGame(Canvas):
        def __init__(self, master=None):
            super().__init__(master)
            self.configure(width = 450,height =540 , bg='black')
            self.running = False
            self.snake = None
            self.food = None
            self.current = None
            self.direction = None
            #self.score = scores()

        def start(self):
             if self.running == False:
                self.snake = Snake(self)
                self.food = Food(self)
                self.running = True

        def restart(self):
            if self.running == True:
                self.running = False
                self.food.delete()
                for bodyPart in self.snake.body:
                    bodyPart.delete()
            

    class gameCharacters():
        def __init__(self, game, a, b, type):
            self.game = game
            self.x = a
            self.y = b
            self.type = type
            if type == snakeCharacter:
                self.character = Canvas.create_rectangle(self.game,
                                                   a - 9, b - 9,
                                                   a + 9, b + 9,
                                                   fill='green3',
                                                   width=2)
            elif type == foodCharacter:
                self.character = Canvas.create_oval(self.game,
                                              a - 10, b - 10,
                                              a + 9, b + 9,
                                              fill='red',
                                              width=2)
        def modify(self, a, b):
            self.x, self.y = a, b
            self.game.coords(self.character,
                            a - size[self.type], b - size[self.type],
                            a + size[self.type], b + size[self.type])
        def delete(self):
            self.game.delete(self.character)

            
    class Food(gameCharacters):
        def __init__(self, game):
            self.game = game
            position = int(40/2 - 1)
            n, m = randint(0, position), randint(0, position)
            a, b = 10 * (2 * n + 1), 10 * (2 * m + 1)
            while [a, b] in [[bodyPart.x, bodyPart.y] for bodyPart in self.game.snake.body]:
                n, m = randint(0, position), randint(0, position)
                a, b = 10 * (2 * n + 1), 10 * (2 * m + 1)
            super().__init__(game, a, b, foodCharacter)

    class Body(gameCharacters):
        def __init__(self, game, a, y):
            super().__init__(game, a, y, snakeCharacter)

    class Snake():
        def __init__(self, game):
            self.game = game
            a = 10 + 2 * int(40/4) * 10
            self.body = [Body(game, a, a), Body(game, a, a + 20)]

        def move(self, path):
            a = (self.body[-1].x + 20 * path[0]) % 450
            b = (self.body[-1].y + 20 * path[1]) % 540
            if a == self.game.food.x and b == self.game.food.y:
                self.body.append(Body(self.game, a, b))
                self.game.food.delete()
                self.game.food = Food(self.game)

            elif [a, b] in [[bodyPart.x, bodyPart.y] for bodyPart in self.body]:
                print("hi")

            else:
                self.body[1].modify(a, b)
                self.body = self.body[1:]+ [self.body[0]]
            
        


    game = snakeGame(body)
    game.grid(column =1, row=0, sticky ='nsew')

    gameButtons = Frame(body)
    startButton = Button(gameButtons, text='Start',bg='green3',fg='white', command=game.start)
    startButton.grid(column=0, row=0)
    startButton.config(width = 7, height = 1, font=('Fixedsys',20))

    restartButton = Button(gameButtons, text='Restart', bg='red',fg='white', command=game.restart)
    restartButton.grid(column=0, row=1)
    restartButton.config(width = 7, height = 1,font=('Fixedsys',20))

    gameButtons.grid(column=0, row=0)


    

                                                                                                       
     


 
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
