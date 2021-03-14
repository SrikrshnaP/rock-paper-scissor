from tkinter import*
import random
from playsound import playsound
from tkinter import messagebox as m

#window to show Play and Instruction as two Options
root1=Toplevel()
root1.title("Team W8 Project")
root1.configure(bg="pink")
root1.resizable(width=False,height=False)
heading1=Label(root1,text="Rock-Paper-Scissor-Lizard-Spock",width=80, height='2', font=("bookman old style",16,"bold", "italic")).grid(row=0,sticky=N,pady=5)
insp=Label(root1, text="Inspired by: ", font=("bold", 12, "italic"), bg="pink").grid(row=1,sticky=N,pady=0)
tbbt_photo=PhotoImage(file="tbbt2.png")
tbbt_image=tbbt_photo.subsample(2, 2)
Label(root1, image=tbbt_image ).grid(row=2, sticky=N, pady=5)

#Audio Instructions
def audins():
    #Window=Toplevel(root1)
    playsound("rpsls.mp3")
audinst=Button(root1, text="Listen to Sheldon Explain", width="22", font=("bookman old style", 13, "bold"), command=audins).grid(row=5, sticky=N, pady=5)

#Instructions
sheld_photo=PhotoImage(file="sheldon_explains.png")
sheld_image=sheld_photo.subsample(1, 1)
flow_photo=PhotoImage(file="flow.png")
flow_image=flow_photo.subsample(1, 1)
def ins():
    insWindow=Toplevel(root1)
    insWindow.configure(bg="light green")
    insWindow.resizable(width=False,height=False)
    insWindow.title("Instructions/Rules")
    lab1=Label(insWindow, text="Rules/Instructions for Rock-Paper-Scissor-Lizard-Spock", font=("bold", 16), bg="light green")
    lab1.grid(row=0, sticky=N, pady=5)
    Label(insWindow, image=sheld_image).grid(row=2, sticky=N, pady=5)
    lab2=Label(insWindow, text="      For this game, we have taken inspiration from the show, The Big Bng Theory. \nIn it Sheldon Cooper explains to us Rock-Paper-Scissor-Lizard-Spock.\nGo through the picture below for better understanding--", font=("bold", 12), bg="light green")
    lab2.grid(row=3, sticky=N, pady=5)
    Label(insWindow, image=flow_image).grid(row=4, sticky=N, pady=5)
    close=Button(insWindow,text="Close", width="10", font=("bookman old style", 13, "bold"), command=insWindow.destroy).grid(row=6,sticky=N,padx=5,pady=10)
Button(root1, text="Rules", width="10", font=("bookman old style", 13, "bold"), command=ins).grid(row=6, sticky=N, pady=5)

#Play the game
rock_photo=PhotoImage(file="Rock.png")
rock_image=rock_photo.subsample(1, 1)
paper_photo=PhotoImage(file="Paper.png")
paper_image=paper_photo.subsample(1, 1)
scissors_photo=PhotoImage(file="Scissor.png")
scissors_image=scissors_photo.subsample(1, 1)
lizard_photo=PhotoImage(file="Lizard.png")
lizard_image=lizard_photo.subsample(1, 1)
spock_photo=PhotoImage(file="Spock.png")
spock_image=spock_photo.subsample(1, 1)

player_points=0
computer_points=0
c=["Rock","Paper","Scissor", "Lizard", "Spock"]

def play():
    root=Toplevel(root1)
    root.configure(bg="light green")
    root.resizable(width=False,height=False)
    root.title("Rock-Paper-Scissor-Lizard-Spock")
    heading=Label(root,text="Let's play Rock-Paper-Scissor-Lizard-Spock",width=100,font=("bookman old style",16,"bold", "italic"),bg="yellow").grid(row=0,sticky=N,pady=5)
    small_instruction=Label(root,text="Choose your option till the score of one of players becomes 10",font=("calibri",14,"italic"),bg="light green").grid(row=4,sticky=N,pady=20)
    def outcome_function(user_option):
        global player_points
        global computer_points
        computer_option=random.choice(c)
        player_choice.config(fg="red",text="Your choice: "+str(user_option))
        computer_choice.config(fg="green",text="Computer chose: "+str(computer_option))

        if(user_option=="Rock" and computer_option=="Scissor") or (user_option=="Rock" and computer_option=="Lizard") or (user_option=="Paper" and computer_option=="Rock") or (user_option=="Paper" and computer_option=="Spock") or (user_option=="Scissor" and computer_option=="Paper") or (user_option=="Scissor" and computer_option=="Lizard") or (user_option=="Lizard" and computer_option=="Spock") or (user_option=="Lizard" and computer_option=="Paper") or (user_option=="Spock" and computer_option=="Rock") or (user_option=="Spock" and computer_option=="Scissor"):
            player_points=player_points+2
            player_score.config(fg="red",text="Your score: "+str(player_points))
            computer_score.config(fg="green",text="Computer's score: "+str(computer_points))
            result.config(text="Yay! You won this time \n (+2 to you)")
        elif (user_option=="Rock" and computer_option=="Rock") or (user_option=="Paper" and computer_option=="Paper") or (user_option=="Scissor" and computer_option=="Scissor") or (user_option=="Lizard" and computer_option=="Lizard") or (user_option=="Spock" and computer_option=="Spock"):
            player_points=player_points+1
            computer_points=computer_points+1
            player_score.config(fg="red",text="Your score: "+str(player_points))
            computer_score.config(fg="green",text="Computer's score: "+str(computer_points))
            result.config(text="+1/+1 For its a TIE")
        else:
            computer_points=computer_points+2
            player_score.config(fg="red",text="Your score: "+str(player_points))
            computer_score.config(fg="green",text="Computer's score: "+str(computer_points))
            result.config(text="Computer wins this time\n (+2 to the Computer)")
        
            

        if player_points>=10 and computer_points>=10:
            warning.config(fg="green",text="Game Over")
            final_result.config(fg="Green",text="Its a Draw")
            player_points=0
            computer_points=0
        elif player_points>=10:
            warning.config(fg="green",text="Game Over")
            final_result.config(fg="Green",text="You have won!!! I am sure Sheldon would be PROUD!")
            player_points=0
            computer_points=0
        elif computer_points>=10:
            warning.config(fg="green",text="Game Over")
            final_result.config(fg="Green",text="You Loose!!!Better Luck next time, I mean seriously BETTER LUCK")
            player_points=0
            computer_points=0
            
    def quit():
        if m.askyesno("Exit","Do you really want to quit the game"):
            m.showinfo("Response","Goodbye")
            exit()
        elif m.askyesno("Response","Do you want to start a new game"):
            warning.config(text="")
            final_result.config(text="")
            player_choice.config(text="")
            player_score.config(text="")
            computer_choice.config(text="")
            computer_score.config(text="")
            result.config(text="")
        else:
            m.showinfo("Response","Continue with your game")
            warning.config(text="")
            final_result.config(text="")


    #Buttons
    Button1=Button(root,image=rock_image,command=lambda:outcome_function("Rock"),bg="black").grid(row=5,padx=5,pady=5,sticky=W)
    Button2=Button(root,image=paper_image,command=lambda:outcome_function("Paper"),bg="black").grid(row=5,padx=290,pady=5,sticky=W)
    Button3=Button(root,image=scissors_image,command=lambda:outcome_function("Scissor"),bg="black").grid(row=5,padx=5,pady=5,sticky=N)
    Button4=Button(root,image=lizard_image,command=lambda:outcome_function("Lizard"),bg="black").grid(row=5,pady=5,padx=290,sticky=E)
    Button5=Button(root,image=spock_image,command=lambda:outcome_function("Spock"),bg="black").grid(row=5,padx=5,pady=5,sticky=E)

    # Runtime labels
    player_choice=Label(root,font=("calibri",15,"italic"),bg="light green")
    player_choice.grid(row=6,padx=10,pady=8,sticky=W)
    computer_choice=Label(root,font=("calibri",15,"italic"),bg="light green")
    computer_choice.grid(row=6,padx=10,pady=8,sticky=E)

    player_score=Label(root,font=("calibri",15,"italic"),bg="light green")
    player_score.grid(row=7,padx=5,pady=5,sticky=W)
    computer_score=Label(root,font=("calibri",15,"italic"),bg="light green")
    computer_score.grid(row=7,padx=5,pady=5,sticky=E)
    result=Label(root,font=("Times new roman",15,"italic"),bg="light green")
    result.grid(row=7,padx=5,pady=5,sticky=N)

    #Final statements
    warning=Label(root,font=("Algerian",13,"bold","italic"),bg="light green")
    warning.grid(row=8,padx=5,pady=8,sticky=N)
    final_result=Label(root,font=("algerian",13,"italic"),bg="light green")
    final_result.grid(row=10,padx=5,pady=8,sticky=N)

    #Quit button
    leave=Button(root,text="Quit game",width=9,font=("calibri",13,"bold"),bg="light blue",command=quit)
    leave.grid(row=14,padx=5,pady=5,sticky=N)
Button(root1,text="Lets PLay", width=10, font=("bookman old style",12,"bold"), command=play).grid(row=8, sticky=N, pady=0)
Label(root1, text="We suggest you to Listen to Sheldon Explain the Game, if you dont quite understand it, go ahead to the Rules. \n After which you should definitely Play the Game \n.\n.\n.\nAll Hail Sam Kass!!!\n(Internet pioneer and blogger, who invented the game Rock, Paper, Scissors, Lizard, Spock)", font=("bookman old style",12,"bold"), bg="pink").grid(row=11, sticky=N, pady=30)

root1.mainloop()