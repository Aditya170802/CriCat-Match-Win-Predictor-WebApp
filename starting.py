import tkinter.font as font
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

# this is backend
#this would be the master or the main place of all calculations for the win prediction.
import pandas as pd
import numpy as np
from masterWinCal import Calc



# this is gui part
class One:

    def finder(code,t1,t2,ml,mr,grd):
        
        string = "t20"

        arr = [string,t1.get(1.0, "end-1c"),t2.get(1.0, "end-1c"),grd.get(1.0, "end-1c")]
        x = ml.get(1.0, "end-1c").split(",")
        y = mr.get(1.0, "end-1c").split(",")
        val = Calc.calc(arr,x,y)
        team = val[1]
        prob = val[0]
        messagebox.showinfo("Result",("{} has winning probability of {}".format(team, prob)))


    def testMatch():
        global currentframe
        currentframe.pack_forget()
        currentframe = TMatch
        currentframe.place(anchor='center', relx=0.5, rely=0.5)
        f1 = Frame(currentframe, width=230, height=450,background="light blue")
        f2 = Frame(currentframe, width=230, height=450,background="light blue")

        # Team Textbox
        team1 = Text(f1,width=30,height=2)
        team2 = Text(f2,width=30,height=2)

        # Left Side Player TextBox
        member1L = Text(f1,width=40,height=3)
         
        # Right Side Player TextBox
        member1R = Text(f2,width=40,height=3)


        

        #Find Button
        find = Button(currentframe,width=15,height=3, text="find",command=lambda:One.finder(0,team1,team2,member1L,member1R,ground))
        find.pack(side=BOTTOM,pady=15)
        find['font'] = myFont

        #Ground TextBox
        ground = Text(currentframe,width=20,height=2)
        ground.pack(side=BOTTOM)

        #Heading
        label2 = Label(currentframe,text="Test Match",background="light blue")
        label2.pack(pady=10)
        label2['font'] = textFont

        team1.pack(side=TOP)
        team2.pack(side=TOP)

        #Left Team
        member1L.pack(side=BOTTOM,pady=7)


        #Right Team
        member1R.pack(side=BOTTOM,pady=7)



        f1.pack(side=LEFT,padx=10)
        f2.pack(side=RIGHT)
        currentframe.pack()


    def oneDay():
        global currentframe
        currentframe.pack_forget()
        currentframe = OMatch
        currentframe.place(anchor='center', relx=0.5, rely=0.5)
        f1 = Frame(currentframe, width=230, height=450,background="light blue")
        f2 = Frame(currentframe, width=230, height=450,background="light blue")
        

        team1 = Text(f1,width=30,height=2)
        team2 = Text(f2,width=30,height=2)

        # Left Side Player
        member1L = Text(f1,width=40,height=3)
         
        # Right Side Player
        member1R = Text(f2,width=40,height=3)


        #Find Button
        find = Button(currentframe,width=15,height=3, text="find",command=lambda:One.finder(1,team1,team2,member1L,member1R,ground))
        find.pack(side=BOTTOM,pady=15)
        find['font'] = myFont

        #Ground TextBox
        ground = Text(currentframe,width=20,height=2)
        ground.pack(side=BOTTOM)


        #Heading
        label2 = Label(currentframe,text="OneDay Match",background="light blue")
        label2.pack(pady=10)
        label2['font'] = textFont

        team1.pack(side=TOP)
        team2.pack(side=TOP)

        #Left Team
        member1L.pack(side=BOTTOM,pady=7)

        #Right Team
        member1R.pack(side=BOTTOM,pady=7)


        f1.pack(side=LEFT,padx=10)
        f2.pack(side=RIGHT)
        currentframe.pack()

    def t20():
        global currentframe
        currentframe.pack_forget()
        currentframe = TwMatch
        currentframe.place(anchor='center', relx=0.5, rely=0.5)
        f1 = Frame(currentframe, width=230, height=450,background="light blue")
        f2 = Frame(currentframe, width=230, height=450,background="light blue")
        


        team1 = Text(f1,width=30,height=2)
        team2 = Text(f2,width=30,height=2)

        # Left Side Player
        member1L = Text(f1,width=40,height=3)
         
        # Right Side Player
        member1R = Text(f2,width=40,height=3)


        #Find Button
        find = Button(currentframe,width=15,height=3, text="find",command=lambda:One.finder(2,team1,team2,member1L,member1R,ground))
        find.pack(side=BOTTOM,pady=15)
        find['font'] = myFont

        #Ground TextBox
        ground = Text(currentframe,width=20,height=2)
        ground.pack(side=BOTTOM)


        #Heading
        label2 = Label(currentframe,text="T20 Match",background="light blue")
        label2.pack(pady=10)
        label2['font'] = textFont

        team1.pack(side=TOP)
        team2.pack(side=TOP)

        #Left Team
        member1L.pack(side=BOTTOM,pady=7)

        #Right Team
        member1R.pack(side=BOTTOM,pady=7)


        f1.pack(side=LEFT,padx=10)
        f2.pack(side=RIGHT)
        currentframe.pack()
    


#Root
root = Tk() 
root.title(string="CriCat")
root.geometry("800x550")
root.config(background="light blue")


# Main Frame
landing = Frame(root, width=500, height=450,background="light blue")
landing.place(anchor='center', relx=0.5, rely=0.5)
bottomFrame = Frame(root,background="light blue")
bottomFrame.place(anchor='center', relx=0.5, rely=0.9)

# TestMatch Frame
TMatch = Frame(root, width=500, height=450,background="light blue")
OMatch = Frame(root, width=500, height=450,background="light blue")
TwMatch = Frame(root, width=500, height=450,background="light blue")

currentframe = landing





#Buttons
myFont = font.Font(family='Courier',size=12)

test_match = Button(bottomFrame,width=15,height=3, text="Test", command=One.testMatch)
test_match.pack(side=LEFT,padx=5)


one_day_match = Button(bottomFrame,width=15,height=3, text="odi",command=One.oneDay)
one_day_match.pack(side=LEFT,padx=5)

t20_match = Button(bottomFrame,width=15,height=3, text="T20i",command=One.t20 )
t20_match.pack(side=LEFT,padx=5)

test_match['font'] = myFont
one_day_match['font'] = myFont
t20_match['font'] = myFont


#Text
msg = Label(landing,text="let's find out who wins!",background="light blue")
textFont = font.Font(family='Blackadder ITC',size=20)
msg['font'] = textFont
msg.pack(side=BOTTOM)




# Opening Image and Resizing it
img = (Image.open("./Cricat (1).png"))
resized_image= img.resize((300,205), Image.ANTIALIAS)


# Position image
new_image= ImageTk.PhotoImage(resized_image)
label1 = Label(landing,image=new_image,height=290,width=290,background="light blue")
label1.pack()


landing.pack()


#Main Loop
root.mainloop()