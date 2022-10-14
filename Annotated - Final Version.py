'''
Maths Snake
Jaynik Parsotomo
Version 3.1 - Annotated
'''

'''Libraies Imported'''
from tkinter import *
import random
from random import randint
import pickle

'''Create Home Button'''
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

'''Create each Tilte on the sections'''       
def createTitle(frame,title):
    title = Label(frame, text=title, bg='black', fg='red', font=('Fixedsys',20, 'bold'))
    title.grid(column=0, row=0, sticky=(W, E))
'''Function for Progress Section'''

def progress():
    ClearWindow()
    createTitle(title,"Progress:")
    '''Heading of Progress Tabel'''
    questionTitle = Label(body, text="Question", fg="blue",bg='yellow',font=('Fixedsys',20,'bold'))

    questionTitle.grid(column=0,row=0, sticky=(W,E))

    right = Label(body,text="Right", fg="blue",bg='yellow',font=('Fixedsys',20,'bold'))
    right.config(width=10)
    right.grid(column=1,row=0, sticky=(W,E))

    wrong = Label(body,text="Wrong", fg="blue",bg='yellow',font=('Fixedsys',20,'bold'))
    wrong.config(width=10)
    wrong.grid(column=2,row=0, sticky=(W,E))

    answer = Label(body,text="Answer", fg="blue",bg='yellow',font=('Fixedsys',20,'bold'))
    wrong.config(width=10)
    answer.grid(column=3,row=0, sticky=(W,E))

    '''Display the information for the Progress Table'''
    counterQ = 1
    questionList = easyQuestions + mediumQuestions + hardQuestions
    while counterQ-1 != len(questionList):
        for item in questionList:
            items = item
            labels = Label(body,text = items,fg="white",bg='orange',font=('Fixedsys',12,'bold'), width=10)
            labels.grid(row = counterQ, column = 0)
            counterQ = counterQ + 1
            
    counterA = 1
    answerList = easyAnswers + mediumAnswers + hardAnswers
    while counterA -1 != len(answerList):
        for item in answerList:
            items = item
            labels = Label(body,text = items, fg="white",bg='orange',font=('Fixedsys',12,'bold'),width=10)
            labels.grid(row = counterA, column = 3)
            counterA = counterA + 1

    with open(rightM, "rb") as fq:
        rightTrackerM = pickle.load(fq)

    with open(wrongM, "rb") as ft:
        wrongTrackerM = pickle.load(ft)

    with open(rightE, "rb") as fp:
        rightTrackerE = pickle.load(fp)
    with open(wrongE, "rb") as fi:
        wrongTrackerE = pickle.load(fi)

    with open(rightH, "rb") as fy:
        rightTrackerH = pickle.load(fy)

    with open(wrongH, "rb") as fo:
        wrongTrackerH = pickle.load(fo)

    rightList = rightTrackerE + rightTrackerM + rightTrackerH
    counterR = 1
    while counterR -1 != len(rightList):
        for item in rightList:
            items = item
            labels = Label(body,text = items,fg="white",bg='orange',font=('Fixedsys',12,'bold'), width=10)
            labels.grid(row = counterR, column = 1)
            counterR = counterR + 1

    counterW = 1
    wrongList = wrongTrackerE + wrongTrackerM + wrongTrackerH
    while counterW -1 != len(wrongList):
        for item in wrongList:
            items = item
            labels = Label(body,text = items, fg="white",bg='orange',font=('Fixedsys',12,'bold'), width=10)
            labels.grid(row = counterW, column = 2)
            counterW = counterW + 1

'''Create the How to Pay Section'''    
def howToPlay():
    ClearWindow()
    createTitle(title,"How To Play:")

    '''Instructions Section'''
    instructionsTitle = Label(body, text="Instructions",height=1, width=5,fg="blue",bg='gold2',font=('Fixedsys',25,'bold'))
    instructionsTitle.grid(column=0, row=2, sticky =(W,E))

    instructions =  Text(body, height=10, width=5,fg="blue",font=('Fixedsys',12))
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

    '''Disply the image of the Controls'''   
    control = Label(body, text='Controls',fg='blue',font=('Fixedsys',20,'bold'))
    control.grid(column=0, row=4, sticky =(N,W,E,S))
    
    photo = PhotoImage(file = "arrowkeys.gif")
    label = Label(body,image=photo)
    label.image = photo
    label.grid(column=0, row=5,sticky =(N,W,E,S))

    '''How to Use the Progress Table'''
    progressTitle = Label(body, text='Progress',fg='blue',font=('Fixedsys',20,'bold'))
    progressTitle.grid(column=0, row=6, sticky =(N,W,E,S))

    progressInstruc = Text(body,fg="dark green",font=('Fixedsys',12))
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

'''Create the Select Difficulty Level'''
def createPlayMenu():
    ClearWindow()
    createTitle(title,"Select Difficulty:")
    
    easyButton = Button(body, text = "EASY", fg='white', bg='green3', command=easy,font=('Fixedsys',20, 'bold') )
    easyButton.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=2)

    mediumButton = Button(body,text = "MEDIUM", fg='white', bg='orange', command=medium,font=('Fixedsys',20, 'bold'))
    mediumButton.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=2)

    hardButton = Button(body,text = "HARD", fg='white', bg='red', command=hard,font=('Fixedsys',20, 'bold'))
    hardButton.grid(column=0, row=3, sticky =(N,W,E,S), columnspan=2)
    
'''Fucntion to set the Title'''
def setTitle(root, title):
    root.title(title)
    
'''Used to Empty to contents of the Window'''    
def ClearWindow():
     for widget in Frame.winfo_children(body):
          widget.grid_forget()
     for widget in Frame.winfo_children(title):
          widget.grid_forget()
          
'''Creates the Main Menu, wiht the Buttons to be displayed'''        
def createHome(frame):
    
    playButton = Button(body,text = "PLAY", fg='white', bg='purple', command=createPlayMenu,font=('Fixedsys',20, 'bold'))
    playButton.grid(column=0, row=1, sticky =(N,W,E,S), columnspan=4)

    progressButton = Button(body,text = "PROGRESS",fg='white', bg='green3',command=progress,font=('Fixedsys',20, 'bold'))
    progressButton.grid(column=0, row=2, sticky =(N,W,E,S), columnspan=4)

    howToPlayButton = Button(body,text = "HOW TO PLAY", fg='white', bg='green3', command=howToPlay,font=('Fixedsys',20, 'bold'))
    howToPlayButton.grid(column=0, row=3, sticky =(N,W,E,S),columnspan=4)

    highScore = Button(body,text="HIGH SCORE",fg="white",bg="green3", command=highScoreList,font=('Fixedsys',20, 'bold'))
    highScore.grid(column=0, row=4, sticky =(W,E), columnspan=4)

    exitButton = Button(body,text = "EXIT",fg='white', bg='red',command=exitApp,font=('Fixedsys',20, 'bold'))
    exitButton.grid(column=0, row=5,sticky =(N,W,E,S), columnspan=4)

'''Closes the Game'''
def exitApp():
    root.destroy()

'''Contains the Top 5 High Scores for Each Section, displayed in a list'''
def highScoreList():
    ClearWindow()
    createTitle(title,"High Score List:")
    
    '''Sorts the list to get the top 5 high scores for the list'''
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
    '''Displayes the Top 5 scores'''
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

    
levelFlag = 0 #Used to Define which level has been selected
'''Calls the game fucntion to create the game when the level has been selected''' 
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

'''Creates a List of the Questions and Answers for each Level'''
easyQuestions = ['10 + 3', '2+2', '14-3','16+2','19-1']
easyAnswers = ['13', '4','11','18','18']

mediumQuestions = ['10*3', '2/2', '14/7','9*2','18/3']
mediumAnswers = ['30', '1','2','18','6']

hardQuestions = ['256/8', '1/2 = ?', '1/4 = ?','576/45','1/10 = ?']
hardAnswers = ['32', '0.5','0.25','12.8','0.1']

'''Stores the List of scores for each level'''
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

'''Snake Game Fucntion,conrains the Classes used to create the game'''
def snakeGamePlay(body,levelFlag):
#Easy access which character is being called for
    snakeCharacter = 'snake'
    foodCharacter = 'food'

    size = {snakeCharacter: 9, foodCharacter: 10}#An dictionary containing the sizes of the food and snake for easy access

#Define the controls, using Dictionaries'''

    up = 'Up'
    down = 'Down'
    right = 'Right'
    left = 'Left'

    directions  = {up: [0, -1], down: [0, 1], right: [1, 0], left: [-1, 0]}
    axes = {up: 'Vertical', down: 'Vertical', right: 'Horizontal', left: 'Horizontal'}
    

#Main Class containing the Snake Game   
    class snakeGame(Canvas):
        #Defining the attribute
        def __init__(self, master=None):
            super().__init__(master)
            self.configure(width = 450,height =540 , bg='black')
            self.running = False
            self.snake = None
            self.food = None
            self.current = None
            self.direction = None
            self.score = Scores()
        #Defines the Start Button
        def start(self):
             if self.running == False:
                self.snake = Snake(self)
                self.food = Food(self)
                self.direction = right
                self.current = Movement(self, right)
                self.current.begin()
                self.running = True
        #Defines the Restart Button
        def restart(self):
            if self.running == True:
                self.score.reset()
                self.current.stop()
                self.running = False
                self.food.delete()
                for bodyPart in self.snake.body:
                    bodyPart.delete()
        #Method creates the Controls for the Snake
        def controls(self, event):
             if True == self.running and\
                event.keysym in axes.keys() and\
                axes[event.keysym] != axes[self.direction]:
                    self.current.flag = 0
                    self.direction = event.keysym
                    self.current = Movement(self, event.keysym)  
                    self.current.begin()
#Class which creates the Score Tracker
    class Scores():
        def __init__(self, master = None):
            self.counter = 0 
            self.scoreTracker = StringVar(master, '0')

#Method used to increase the score
        def increase(self):
            self.counter = int(self.scoreTracker.get()) + 1            
            self.scoreTracker.set(str(self.counter))
                    
#Method which defines what happens when the game ends with the score
        def reset(self):
         #Save the game score to the appropiate list
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

            #Reset the score tracker back to zero                  
            self.scoreTracker.set(0)
            
                 
                 
            
#Class which creates the shapes for the snake and food 
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
#Used to add the shape onto the canvas
        def modify(self, a, b):
            self.x, self.y = a, b
            self.game.coords(self.character,
                            a - size[self.type], b - size[self.type],
                            a + size[self.type], b + size[self.type])
#Method to delete the tkinter objects
        def delete(self):
            self.game.delete(self.character)

#Deines the charateristic of the food           
    class Food(gameCharacters):
        #Defines random locationo f the food
        def __init__(self, game):
            self.game = game
            position = int(40/2 - 1)
            n, m = randint(0, position), randint(0, position)
            self.a, self.b = 10 * (2 * n + 1), 10 * (2 * m + 1)
            #This checks where the snake is so the food is not created there
            while [self.a, self.b] in [[bodyPart.x, bodyPart.y] for bodyPart in self.game.snake.body]:
                n, m = randint(0, position), randint(0, position)
                self.a, self.b = 10 * (2 * n + 1), 10 * (2 * m + 1)
            super().__init__(game, self.a, self.b, foodCharacter)

#A class to create the body of the snake
    class Body(gameCharacters):
        def __init__(self, game, a, y):
            super().__init__(game, a, y, snakeCharacter)

#Defines the characteristic of the snake
    class Snake():
        def __init__(self, game):
            #Defines the starting position of the snake
            self.game = game
            a = 10 + 2 * int(40/4) * 10
            self.body = [Body(game, a, a), Body(game, a, a + 20)]
#Method which defines what happens each time the snake moves
        def move(self, path):
            #The snake head coordinates and speed each time it moves
            a = (self.body[-1].x + 20 * path[0]) % 450
            b = (self.body[-1].y + 20 * path[1]) % 540
            #Checks if the snake has eaten the food
            if a == self.game.food.x and b == self.game.food.y:
                self.game.current.flag = 0#Stops the gameplay
                Question(game)#Question pops up
                self.game.food.delete()#Deletes the food
                self.game.food = Food(self.game)#Creates a new food
                
            #Checks if the snake head has hit the body
            elif [a, b] in [[bodyPart.x, bodyPart.y] for bodyPart in self.body]:
                self.game.restart()#Ends the game

            #Updates the head coordinates and body
            else:
                self.body[0].modify(a, b)
                self.body = self.body[1:]+ [self.body[0]]
        #A method which grows the snake
        def growth(self,a,b):
            self.body.append(Body(self.game, a, b))
#Defines the movement at certian points of the game
    class Movement():
        def __init__(self, game, direction):
            self.flag = 1
            self.game =  game
            self.direction = direction
#Define what happens at the beginning of the game
        def begin(self):
            if self.flag > 0:
                self.game.snake.move(directions[self.direction])
            self.game.after(100, self.begin)
#Method which stops the game
        def stop(self):
            self.flag = 0
#Method which defines the movement after each move
        def after(self):
            self.game.snake.move(directions[self.direction])

#Creates the Questions
    class Question():
        def __init__(self, game, master=None):

            self.game = game
            #Creates a pop-up
            self.root2 = Toplevel()
            self.root2.columnconfigure(1, weight=1)
            self.root2.rowconfigure(1, weight=1)

            self.root2.resizable(width=False, height=False)
            self.root2.geometry('{}x{}'.format(400, 300))
            #Selectes a random question from the list and the answer to it
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
            
            #Creates the entry box
            self.e = Entry(self.root2)
            self.e.grid(row = 1, column=0)

            self.eAnswer = eA
            self.mAnswer = mA
            self.hAnswer = hA
            
            #creates the button to submit the answer
            self.submit = Button(self.root2, text="submit", width=10, command = self.save)
            self.submit.grid(row = 2, column = 0)

            
#Method to submit the answer
        def save(self):
            #Checks which level it is 
            if levelFlag == 0:
                #Checks if the users answer is right
                if self.e.get() == self.eAnswer:
                    self.root2.destroy()#Closes the pop-up
                    self.game.current.flag = 1#Restarts gameplay
                    self.game.score.increase()#Increases the score
                    self.game.snake.growth(self.game.food.a, self.game.food.b)#Grows the snake
                    #Updates the Right Tracker
                    value = rightTrackerE.pop(self.easyIndex)
                    track = value + 1
                    rightTrackerE.insert(self.easyIndex, track)
                    print(rightTrackerE)
                    with open(rightE, 'wb') as fp:
                        pickle.dump(rightTrackerE, fp)
                else:
                    self.root2.destroy()
                    self.game.current.flag = 1
                    #Updates the wrong tracker
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



            
            
        

#Saves the main snake game class to the varible game, easy access
    game = snakeGame(body)
    game.grid(column =1, row=0, sticky ='nsew')
#Binds the controls keys to the game
    root.bind("<Key>",game.controls)
#Creates the buttons
    gameButtons = Frame(body)
    startButton = Button(gameButtons, text='Start',bg='green3',fg='white', command=game.start)
    startButton.grid(column=0, row=0)
    startButton.config(width = 7, height = 1, font=('Fixedsys',20))

    restartButton = Button(gameButtons, text='Restart', bg='red',fg='white', command=game.restart)
    restartButton.grid(column=0, row=1)
    restartButton.config(width = 7, height = 1,font=('Fixedsys',20))

    gameButtons.grid(column=0, row=0)
    
    gameScore = Label(gameButtons, text='Game Score',bg='orange',fg='white')
    gameScore.grid(column = 0, row = 2)
    #Displays the scores
    currentScore = Label(gameButtons, textvariable=game.score.scoreTracker)
    currentScore.grid(column = 0, row = 3)
    highscore = Label(gameButtons, text='High Score',bg='orange',fg='white')
    highscore.grid(column = 0, row = 4)
    #selects the appropiate high score
    if levelFlag == 0:
        highScoreTracker = Label(gameButtons, textvariable=highScoreE)
        highScoreTracker.grid(column = 0, row = 5)

    elif levelFlag == 1:
         highScoreTracker = Label(gameButtons, textvariable=highScoreM)
         highScoreTracker.grid(column = 0, row = 5)

    elif levelFlag == 2:
         highScoreTracker = Label(gameButtons, textvariable=highScoreH)
         highScoreTracker.grid(column = 0, row = 5)



#Create the right an wrong tracker  
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

#Creates the Tkinter Window 
root = Tk()
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

#Creates the Frame for the home button
nav = Frame(root, borderwidth=2, relief="sunken", bg="white")
nav.grid(column=0, row=0, rowspan = 2, sticky=(N, S))

#Creates the frame for the title
title = Frame(root, borderwidth=2, relief="sunken")
title.grid(column=1, row=0, sticky=(N, E, W))
title.columnconfigure(0, weight=1)

#Holds the main content of the game
body = Frame(root, borderwidth=2, relief="sunken", bg="white")
body.grid(column=1, row=1, sticky=(N, W, E, S))
body.columnconfigure(0, weight=1)

root.resizable(width=False, height=False)
#root.state("zoom")
root.geometry('{}x{}'.format(800, 600))

#Selectes the highest score from the score lists
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








