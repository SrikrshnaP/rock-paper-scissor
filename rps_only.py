#IMPORTING
from tkinter import *
import random

#INITIALIZATION
temp = True #help variable
computerPoints = 0  #counts for points table
playerPoints =0


#MAIN WINDOW / PLAYER WINDOW
playerWindow = Toplevel()
playerWindow.configure(bg='cyan')
playerWindow.geometry('+490+50')
playerWindow.title('player')
playerWindow.resizable(width=False,height=False)

#POINTS TABLE WINDOW
pointsWindow = Toplevel()
pointsWindow.configure(bg='cyan')
pointsWindow.title('points table')
pointsWindow.resizable(width=False,height=False)
pointsWindow.geometry('+40+450')

#COMPUTER WINDOW
computerWindow = Toplevel()
computerWindow.configure(bg='cyan')
computerWindow.geometry('+70+50')
computerWindow.title('rock paper scissor computer')
computerWindow.resizable(width=False,height=False)

#RESULT WINDOW
resultWindow = Toplevel()
resultWindow.configure(bg='cyan')
resultWindow.geometry('+400+400')
resultWindow.title('Result')
resultWindow.resizable(width=False,height=False)

#REPLAYPROMPT WINDOW
replayPromptWindow = Toplevel()
replayPromptWindow.configure(bg='purple')
replayPromptWindow.geometry('+700+400')
replayPromptWindow.title('prompt')
replayPromptWindow.resizable(width=False,height=False)

#POINTS TABLE
def counter(): 
    cScoreLabel=Label(pointsWindow,text='   computer  \nscore',
              font=("Open Sans", 20),fg='red',bg='cyan')
    pScoreLabel=Label(pointsWindow,text='   player  \nscore',
              font=("Open Sans", 20),fg='green',bg='cyan')
    cPointsDisplay=Label(pointsWindow,text=computerPoints,font=("Courier", 100),bg='cyan')
    pPointsDisplay=Label(pointsWindow,text=playerPoints,font=("Courier", 100),bg='cyan')
    
    cScoreLabel.grid(row=0,column=0)
    pScoreLabel.grid(row=0,column=1)
    cPointsDisplay.grid(row=1,column=0)
    pPointsDisplay.grid(row=1,column=1)
counter()

#ASSIGNING VARIABLES TO PHOTOS
rockHandPlayer = PhotoImage(file = 'rockHandPlayer.png')
paperHandPlayer = PhotoImage(file = 'paperHandPlayer.png')
scissorHandPlayer = PhotoImage(file = 'scissorHandPlayer.png')

rockHandComputer = PhotoImage(file = 'rockHandComputer.png')
paperHandComputer = PhotoImage(file = 'paperHandComputer.png')
scissorHandComputer = PhotoImage(file = 'scissorHandComputer.png')
cMessagePhoto = PhotoImage(file = 'cMessage.png')

winPhoto = PhotoImage(file = 'win.png')
loosePhoto = PhotoImage(file = 'loose.png')
tiePhoto = PhotoImage(file = 'tie.png')
resMessagePhoto = PhotoImage(file = 'resMessage.png')


#FUNCTIONS
def windowDesigns():
    global rockHandPlayerButton,paperHandPlayerButton,scissorHandPlayerButton,playerLabel,cMessage,computerLabel,result,prompt,yesButton,noButton,quitMessage,sp
    #PLAYER WINDOW DESIGNING
    rockHandPlayerButton = Button(playerWindow,image = rockHandPlayer,
                                        command = lambda:picked('rock'))
    paperHandPlayerButton = Button(playerWindow,image = paperHandPlayer,
                                        command = lambda:picked('paper'))
    scissorHandPlayerButton = Button(playerWindow,image = scissorHandPlayer,
                                        command = lambda:picked('scissors'))
    playerLabel=Label(playerWindow,text='PLAYER',
                                        font=("Open Sans", 15),bg='cyan',fg='black')
    
    
    playerLabel.grid(row = 0,column = 1)
    rockHandPlayerButton.grid(row = 1,column = 0)
    paperHandPlayerButton.grid(row = 1,column = 1)
    scissorHandPlayerButton.grid(row = 1,column = 2)
    #RESULT WINDOW DESIGNING
    result = Label(resultWindow,image = resMessagePhoto)
    result.grid(row = 0,column = 0)
    #COMPUTER WINDOW DESIGNING
    computerLabel = Label(computerWindow,text='COMPUTER',
                                        font=("Open Sans", 15),bg='cyan',fg='black')
    computerLabel.grid(row = 0,column = 0)
    cMessage = Label(computerWindow,image = cMessagePhoto)
    cMessage.grid(row = 1,column = 0)
    #REPLAYPROMPT WINDOW DESIGNING
    promptMessage = Label(replayPromptWindow,text = 'wanna play again ?',font = ( 'comic sans' , 40),fg = 'white',bg='purple')
    sp = Label(replayPromptWindow,text = '            ',font = ( 'comic sans' , 15),bg='purple')
    yesButton = Button(replayPromptWindow,text = 'YES',font = ( 'comic sans' , 30),bg='lightgreen',command = playagain)
    noButton = Button(replayPromptWindow,text = 'NO',font = ( 'comic sans' , 30),bg='red', command = closeall)
    quitMessage = Label(replayPromptWindow,text = 'will quit program',font = ( 'comic sans' , 15),bg='purple',fg='tomato')
    promptMessage.grid(row = 0,column = 0, columnspan = 5,rowspan = 3)
    sp.grid(row = 3,column = 1)
    yesButton.grid(row = 6,column = 1)
    noButton.grid(row = 6,column = 4)
    quitMessage.grid(row = 7,column = 4)
    
def computerChoice():
    randomPick = random.choice(['rock','paper','scissors'])
    return randomPick

def closeall():
    playerWindow.destroy()
    replayPromptWindow.destroy()
    computerWindow.destroy()
    resultWindow.destroy()
    pointsWindow.destroy()
    exit()

    

def hideReplayPromptWindow():
    replayPromptWindow.withdraw()
hideReplayPromptWindow() #initially replayPrompt window should be hidden

def showreplayPromptWindow():
    replayPromptWindow.update()
    replayPromptWindow.deiconify()

def playagain():
    global temp
    hideReplayPromptWindow()
    temp = True
    #RESETTING PLAYER WINDOW
    playerLabel.grid(row = 0,column = 1)
    playerWindow.geometry('+490+50')
    paperHandPlayerButton.configure(image = paperHandPlayer)
    rockHandPlayerButton.grid(row = 1,column = 0)
    paperHandPlayerButton.grid(row = 1,column = 1)
    scissorHandPlayerButton.grid(row = 1,column = 2)
    #RESETTING RESULT WINDOW
    result.configure(image = resMessagePhoto)
    #RESETTING COMPUTER WINDOW
    cMessage.configure(image = cMessagePhoto)

    
def picked(playerChoice): #CALCULATION
    global temp,computerPoints,playerPoints

    computerPick = computerChoice()

    if temp == True:
        
        #REMOVING UNPICKED SIGNS FROM PLAYER WINDOW
        scissorHandPlayerButton.grid_forget()
        rockHandPlayerButton.grid_forget()
        playerWindow.geometry('+750+50')

        #COMPUTER WINDOW DISPLAY
        if computerPick == 'rock':
            cMessage.configure(image = rockHandComputer)
        elif computerPick == 'scissors':
            cMessage.configure(image = scissorHandComputer)
        else:
            cMessage.configure(image = paperHandComputer)

        #CALCULATING WIN OR LOOSE OR TIE
            
        if playerChoice == 'rock':
            #Middle button turns to picked player choice
            paperHandPlayerButton.configure(image = rockHandPlayer) 
            if computerPick == 'rock':
                #Displaying result photo
                result.configure(image = tiePhoto) #DES
            elif computerPick == 'paper':
                result.configure(image = loosePhoto)
                computerPoints+=1
            else:
                result.configure(image = winPhoto)
                playerPoints+=1

        elif playerChoice == 'paper':
            paperHandPlayerButton.configure(image = paperHandPlayer)
            if computerPick == 'rock':
                result.configure(image = winPhoto)
                playerPoints+=1
            elif computerPick == 'paper':
                result.configure(image = tiePhoto)
            else:
                result.configure(image = loosePhoto)
                computerPoints+=1
                    
        elif playerChoice == 'scissors':
            paperHandPlayerButton.configure(image = scissorHandPlayer)
            if computerPick == 'rock':
                result.configure(image = loosePhoto)
                computerPoints+=1
            elif computerPick == 'paper':
                result.configure(image = winPhoto)
                playerPoints+=1
            else:
                result.configure(image = tiePhoto)
        
        counter() #Updating the counter
        showreplayPromptWindow()
        temp = False

windowDesigns()

computerWindow.mainloop()

