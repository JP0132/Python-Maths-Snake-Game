'''
Maths Snake
Jaynik Parsotomo
Version 2.9
'''
from tkinter import *
import random
from random import randint
import pickle

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

 
def exitGame():
    ClearWindow()
    createTitle(title,"Exit?")

    yes = Button(body,text = "YES", fg='white', bg='red', command=quit, font=('Fixedsys',20, 'bold'))
    yes.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=2)

    no = Button(body,text = "NO", fg='white', bg='#00B200',font=('Fixedsys',20, 'bold'))
    no.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=2)

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

    exitButton = Button(body,text = "EXIT",fg='white', bg='red',command=exitGame,font=('Fixedsys',20, 'bold'))
    exitButton.grid(column=0, row=5,sticky =(N,W,E,S), columnspan=4)

def highScoreList():
    ClearWindow()
    createTitle(title,"High Score List:")

    with open(easyScores, 'rb') as fv:
        easyScoreList = pickle.load(fv)

    sortsE = sorted([(x,i) for (i,x) in enumerate(easyScoreList)], reverse=True)
    valuesE = []
    posE = []

    for x,i in sortsE:
        if x not in valuesE:
            valuesE.append(x)
            posE.append(i)
            if len(valuesE) == 5:
                break
    print(valuesE)

    easyHeading = Label(body, text = 'Easy High Scores')
    easyHeading.grid(row=0, column=0)

    counterE = 1

    while counterE-1 != len(valuesE):
        for item in valuesE:
                items = item
                labels = Label(body,text = items, width=5)
                labels.grid(row = counterE, column = 0)
                counterE = counterE + 1


    with open(mediumScores, 'rb') as fv:
        mediumScoreList = pickle.load(fv)
    sortsM = sorted([(x,i) for (i,x) in enumerate(mediumScoreList)], reverse=True)
    valuesM = []
    posM = []
    for x,i in sortsM:
        if x not in valuesM:
            valuesM.append(x)
            posM.append(i)
            if len(valuesM) == 5:
                break
    print(valuesM)
    mediumHeading = Label(body, text = 'Medium High Scores')
    mediumHeading.grid(row=0, column=1)
    counterM = 1
    while counterM-1 != len(valuesM):
        for item in valuesM:
                items = item
                labels = Label(body,text = items, width=5)
                labels.grid(row = counterM, column = 1)
                counterM = counterM + 1

    with open(hardScores, 'rb') as fs:
        hardScoreList = pickle.load(fs)
    sortsH = sorted([(x,i) for (i,x) in enumerate(hardScoreList)], reverse=True)
    valuesH = []
    posH = []
    for x,i in sortsH:
        if x not in valuesH:
            valuesH.append(x)
            posH.append(i)
            if len(valuesH) == 5:
                break
    print(valuesH)
    hardHeading = Label(body, text = 'Hard High Scores')
    hardHeading.grid(row=0, column=2)
    counterH = 1
    while counterH-1 != len(valuesH):
        for item in valuesH:
                items = item
                labels = Label(body,text = items, width=5)
                labels.grid(row = counterH, column = 2)
                counterH = counterH + 1

    
levelFlag = 0
    
def easy():
    ClearWindow()
    createTitle(title,"Maths Snake (Easy):")
    levelFlag = 0
    snakeGamePlay(body,levelFlag)

def medium():
    ClearWindow()
    createTitle(title,"Maths Snake (Medium):")
    levelFlag = 1
    snakeGamePlay(body, levelFlag)

def hard():
    ClearWindow()
    createTitle(title,"Maths Snake (Hard):")
    levelFlag = 2
    snakeGamePlay(body, levelFlag)
    


easyQuestions = ['10 + 3', '2+2', '14-3','16+2','19-1']
easyAnswers = ['13', '4','11','18','18']

mediumQuestions = ['10*3', '2/2', '14/7','9*2','18/3']
mediumAnswers = ['30', '1','2','18','6']

hardQuestions = ['256/8', '1/2 = ?', '1/4 = ?','576/45','1/10 = ?']
hardAnswers = ['32', '0.5','0.25','12.8','0.1']

easyScores = 'easyScore7.pk'
easyScoreList = []

with open(easyScores, 'rb') as fv:
    easyScoreList = pickle.load(fv)


mediumScores = 'mediumScore7.pk'
mediumScoreList = []

with open(mediumScores, 'rb') as ft:
    mediumScoreList = pickle.load(ft)

hardScores = 'hardScore3.pk'
hardScoreList = []

with open(hardScores, 'rb') as ft:
    hardScoreList = pickle.load(ft)

def snakeGamePlay(body,levelFlag):
    snakeCharacter = 'snake'
    foodCharacter = 'food'
    size = {snakeCharacter: 9, foodCharacter: 10}

    up = 'Up'
    down = 'Down'
    right = 'Right'
    left = 'Left'

    directions  = {up: [0, -1], down: [0, 1], right: [1, 0], left: [-1, 0]}
    axes = {up: 'Vertical', down: 'Vertical', right: 'Horizontal', left: 'Horizontal'}
    

    
    class snakeGame(Canvas):
        def __init__(self, master=None):
            super().__init__(master)
            self.configure(width = 450,height =540 , bg='black')
            self.running = False
            self.snake = None
            self.food = None
            self.current = None
            self.direction = None
            self.score = Scores()

        def start(self):
             if self.running == False:
                self.snake = Snake(self)
                self.food = Food(self)
                self.direction = right
                self.current = Movement(self, right)
                self.current.begin()
                self.running = True

        def restart(self):
            if self.running == True:
                self.score.reset()
                self.current.stop()
                self.running = False
                self.food.delete()
                for bodyPart in self.snake.body:
                    bodyPart.delete()

        def controls(self, event):
             if True == self.running and\
                event.keysym in axes.keys() and\
                axes[event.keysym] != axes[self.direction]:
                    self.current.flag = 0
                    self.direction = event.keysym
                    self.current = Movement(self, event.keysym)  
                    self.current.begin()

    class Scores():
        def __init__(self, master = None):
            self.counter = 0 
            #self.highScore = StringVar(master, '0')
            self.scoreTracker = StringVar(master, '0')

        def increase(self):
            self.counter = int(self.scoreTracker.get()) + 1
            #highScore = max(self.counter, int(self.highScore.get()))
            self.scoreTracker.set(str(self.counter))
            #self.highScore.set(str(highScore))
            
            

        def reset(self):
            if levelFlag == 0:
                easyScoreList.append(self.counter)
                with open(easyScores, 'wb') as fi:
                    pickle.dump(easyScoreList, fi)

            elif levelFlag == 1:
                mediumScoreList.append(self.counter)
                with open(mediumScores, 'wb') as fp:
                    pickle.dump(mediumScoreList, fp)

            elif levelFlag == 2:
                hardScoreList.append(self.counter)
                with open(hardScores, 'wb') as fs:
                    pickle.dump(hardScoreList, fs)

                                
            self.scoreTracker.set(0)
            
                 
                 
            

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
            self.a, self.b = 10 * (2 * n + 1), 10 * (2 * m + 1)
            while [self.a, self.b] in [[bodyPart.x, bodyPart.y] for bodyPart in self.game.snake.body]:
                n, m = randint(0, position), randint(0, position)
                self.a, self.b = 10 * (2 * n + 1), 10 * (2 * m + 1)
            super().__init__(game, self.a, self.b, foodCharacter)

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
                self.game.current.flag = 0
                Question(game)
                #self.body.append(Body(self.game, a, b))
                #self.game.score.increase()
                self.game.food.delete()
                self.game.food = Food(self.game)

            elif [a, b] in [[bodyPart.x, bodyPart.y] for bodyPart in self.body]:
                self.game.restart()

            else:
                self.body[0].modify(a, b)
                self.body = self.body[1:]+ [self.body[0]]

        def growth(self,a,b):
            self.body.append(Body(self.game, a, b))

    class Movement():
        def __init__(self, game, direction):
            self.flag = 1
            self.game =  game
            self.direction = direction

        def begin(self):
            if self.flag > 0:
                self.game.snake.move(directions[self.direction])
            self.game.after(100, self.begin)

        def stop(self):
            self.flag = 0

        def after(self):
            self.game.snake.move(directions[self.direction])

    class Question():
        def __init__(self, game, master=None):

            self.game = game

            self.root2 = Toplevel()
            self.root2.columnconfigure(1, weight=1)
            self.root2.rowconfigure(1, weight=1)

            self.root2.resizable(width=False, height=False)
            self.root2.geometry('{}x{}'.format(400, 300))

            self.easyIndex = random.choice(range(len(easyQuestions)))
            eQ = easyQuestions[self.easyIndex]
            eA = easyAnswers[self.easyIndex]
            print(eQ)

            self.mediumIndex = random.choice(range(len(mediumQuestions)))
            mQ = mediumQuestions[self.mediumIndex]
            mA = mediumAnswers[self.mediumIndex]
            print(mQ)

            self.hardIndex = random.choice(range(len(hardQuestions)))
            hQ = hardQuestions[self.hardIndex]
            hA = hardAnswers[self.hardIndex]
            print(hQ)

            if levelFlag == 0:
                self.q = eQ
                self.v = StringVar(master, 0)
                self.v.set(self.q)
                self.label = Label(self.root2, textvariable=self.v)
                self.label.grid(row = 0, column = 0)
                

            elif levelFlag == 1:
                self.q = mQ
                self.v = StringVar(master, 0)
                self.v.set(self.q)
                self.label = Label(self.root2, textvariable=self.v)
                self.label.grid(row = 0, column = 0)

            elif levelFlag == 2:
                self.q = hQ
                self.v = StringVar(master)
                self.v.set(self.q)
                self.label = Label(self.root2, textvariable=self.v)
                self.label.grid(row = 0, column = 0)


            self.e = Entry(self.root2)
            self.e.grid(row = 1, column=0)

            self.eAnswer = eA
            self.mAnswer = mA
            self.hAnswer = hA
        
            self.submit = Button(self.root2, text="submit", width=10, command = self.save)
            self.submit.grid(row = 2, column = 0)

            

        def save(self):
            if levelFlag == 0:
                if self.e.get() == self.eAnswer:
                    self.root2.destroy()
                    self.game.current.flag = 1
                    self.game.score.increase()
                    self.game.snake.growth(self.game.food.a, self.game.food.b)
                    value = rightTrackerE.pop(self.easyIndex)
                    track = value + 1
                    rightTrackerE.insert(self.easyIndex, track)
                    print(rightTrackerE)
                    with open(rightE, 'wb') as fp:
                        pickle.dump(rightTrackerE, fp)
                else:
                    self.root2.destroy()
                    self.game.current.flag = 1
                    value = wrongTrackerE.pop(self.easyIndex)
                    track = value + 1
                    wrongTrackerE.insert(self.easyIndex, track)
                    print(wrongTrackerE)
                    with open(wrongE, 'wb') as fp:
                        pickle.dump(wrongTrackerE, fp)

            elif levelFlag == 1:
                if self.e.get() == self.mAnswer:
                    self.root2.destroy()
                    self.game.current.flag = 1
                    self.game.score.increase()
                    self.game.snake.growth(self.game.food.a, self.game.food.b)
                    value = rightTrackerM.pop(self.mediumIndex)
                    track = value + 1
                    rightTrackerM.insert(self.mediumIndex, track)
                    print(rightTrackerM)
                    with open(rightM, 'wb') as fp:
                        pickle.dump(rightTrackerM, fp)
                else:
                    self.root2.destroy()
                    self.game.current.flag = 1
                    value = wrongTrackerM.pop(self.mediumIndex)
                    track = value + 1
                    wrongTrackerM.insert(self.mediumIndex, track)
                    print(wrongTrackerM)
                    with open(wrongM, 'wb') as fp:
                        pickle.dump(wrongTrackerM, fp)

            elif levelFlag == 2:
                if self.e.get() == self.hAnswer:
                    self.root2.destroy()
                    self.game.current.flag = 1
                    self.game.score.increase()
                    self.game.snake.growth(self.game.food.a, self.game.food.b)
                    value = rightTrackerH.pop(self.hardIndex)
                    track = value + 1
                    rightTrackerH.insert(self.hardIndex, track)
                    print(rightTrackerH)
                    with open(rightH, 'wb') as fp:
                        pickle.dump(rightTrackerH, fp)
                else:
                    self.root2.destroy()
                    self.game.current.flag = 1
                    value = wrongTrackerH.pop(self.hardIndex)
                    track = value + 1
                    wrongTrackerH.insert(self.hardIndex, track)
                    print(wrongTrackerH)
                    with open(wrongH, 'wb') as fp:
                        pickle.dump(wrongTrackerH, fp)          



            
            
        


    game = snakeGame(body)
    game.grid(column =1, row=0, sticky ='nsew')

    root.bind("<Key>",game.controls)

    gameButtons = Frame(body)
    startButton = Button(gameButtons, text='Start',bg='green3',fg='white', command=game.start)
    startButton.grid(column=0, row=0)
    startButton.config(width = 7, height = 1, font=('Fixedsys',20))

    restartButton = Button(gameButtons, text='Restart', bg='red',fg='white', command=game.restart)
    restartButton.grid(column=0, row=1)
    restartButton.config(width = 7, height = 1,font=('Fixedsys',20))

    gameButtons.grid(column=0, row=0)

    #scoreboard = Frame(body)
    gameScore = Label(gameButtons, text='Game Score',bg='orange',fg='white')
    gameScore.grid(column = 0, row = 2)
    
    currentScore = Label(gameButtons, textvariable=game.score.scoreTracker)
    currentScore.grid(column = 0, row = 3)
    highscore = Label(gameButtons, text='High Score',bg='orange',fg='white')
    highscore.grid(column = 0, row = 4)
    if levelFlag == 0:
        highScoreTracker = Label(gameButtons, textvariable=highScoreE)
        highScoreTracker.grid(column = 0, row = 5)

    elif levelFlag == 1:
         highScoreTracker = Label(gameButtons, textvariable=highScoreM)
         highScoreTracker.grid(column = 0, row = 5)

    elif levelFlag == 2:
         highScoreTracker = Label(gameButtons, textvariable=highScoreH)
         highScoreTracker.grid(column = 0, row = 5)

    #scoreboard.grid(column=0, row=1)

  

rightE = 'rightE.pk'
wrongE = 'wrongE.pk'
rightTrackerE = [0,0,0,0,0]
wrongTrackerE = [0,0,0,0,0]
with open(rightE, "rb") as fp:
    rightTrackerE = pickle.load(fp)

with open(wrongE, "rb") as fi:
    wrongTrackerE = pickle.load(fi)
    
rightM = 'rightM.pk'
wrongM = 'wrongM.pk'
rightTrackerM = [0,0,0,0,0]
wrongTrackerM = [0,0,0,0,0]
with open(rightM, "rb") as fq:
    rightTrackerM = pickle.load(fq)

with open(wrongM, "rb") as ft:
    wrongTrackerM = pickle.load(ft)

rightH = 'rightH.pk'
wrongH = 'wrongH.pk'
rightTrackerH = [0,0,0,0,0]
wrongTrackerH = [0,0,0,0,0]
with open(rightH, "rb") as fy:
    rightTrackerH = pickle.load(fy)
    
with open(wrongH, "rb") as fo:
    wrongTrackerH = pickle.load(fo)

 
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

highestScoreE = max(easyScoreList)
highScoreE = StringVar(root,'0')
highScoreE.set(str(highestScoreE))

highestScoreM = max(mediumScoreList)
highScoreM = StringVar(root,'0')
highScoreM.set(str(highestScoreM))

highestScoreH = max(hardScoreList)
highScoreH = StringVar(root,'0')
highScoreH.set(str(highestScoreH))

createNav(nav)
ChangePage("home")
root.mainloop()







