from tkinter import*

combined=Tk()
combined.title("W8 Project")
combined.configure(bg="red")
combined.resizable(height=False,width=False)
heading=Label(combined,text="ALERT: Choose one format:-",width=80,font=("bookman old style",16,"bold", "italic")).grid(row=0,sticky=N,pady=5)
def normal():
    import rps_only
def modified():
    import final

Button(combined,text="CLASSICAL Rock-Paper-Scissor",font=("comicsans",13,"bold"),width=30,command=normal).grid(row=4,padx=5,pady=5,sticky=N)
Button(combined,text="SHELDON COOPER VERSION:Rock-Paper-Scissor-Lizard-Spock",font=("comicsans",13,"bold"),width=55,command=modified).grid(row=2,padx=5,pady=5,sticky=N)
Label(combined, text= 'We strongly suggest you to Play the "SHELDON COOPER VERSION:Rock-Paper-Scissor-Lizard-Spock" first.', font=("bookman old style",13,"bold"), bg="red").grid(row=6,pady=5,sticky=N)
combined.mainloop()