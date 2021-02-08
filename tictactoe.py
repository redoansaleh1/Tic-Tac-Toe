"""
Hello freinds Today you will make a Tic-Tac-Toe;
Language:Python;
library:Tkinter;
Let's start...
"""
#First import everything from Tkinter. 
from tkinter import *
"""
Now You are import messegabox from tkinter.
The messageboxes is used when any user is win
or
draw.
"""
from tkinter import messagebox 
"""
rooms variable is used to understand the 9 boxes of the board of Tic-Tac-Toe.
9 boxes info are store as the data type of python array.
"""
rooms=[]
"""
Turn variable is store a string.
The string data determine that which player's turn now.
By default the string is "x" because on tic-tac-toe "x" turn is first than "o".
when "x" is clicked than turn="o".
"""
turn="x"
"""
x win and o_win store a integer number.
The integer numbers is default is 0.
when x win then x_win+=1
And
when o win then o_win+=1. 
"""
x_win=0
o_win=0
"""
The started variable store that game is started or not if started than started=True otherwise False.
By default it is False because the first the game is not start.
"""
started=False
"""
This is a function named make_all_none.
this function make all the boxes "  ".
It's vary important to restart.
"""
def make_all_none():
        if len(rooms)==0:
            for i in range(9):
                    rooms.append("  ")
        else:
            for i in range(9):
                    rooms[i]="  "                
            button_0['text']=rooms[0]          
            button_1['text']=rooms[1]
            button_2['text']=rooms[2]
            button_3['text']=rooms[3]
            button_4['text']=rooms[4]
            button_5['text']=rooms[5]
            button_6['text']=rooms[6]
            button_7['text']=rooms[7]
            button_8['text']=rooms[8]       
#this function determine the result.               
def result():
    if(rooms[0]=="o" and rooms[1]=="o" and rooms[2]=="o") or (rooms[0]=="o" and rooms[4]=="o" and rooms[8]=="o") or (rooms[0]=="o" and rooms[3]=="o" and rooms[6]=="o") or (rooms[2]=="o" and rooms[4]=="o" and rooms[6]=="o") or (rooms[2]=="o" and rooms[5]=="o" and rooms[8]=="o") or (rooms[0]=="o" and rooms[1]=="o" and rooms[2]=="o") or (rooms[1]=="o" and rooms[4]=="o" and rooms[7]=="o") or (rooms[3]=="o" and rooms[4]=="o" and rooms[5]=="o") or (rooms[6]=="o" and rooms[7]=="o" and rooms[8]=="o"):
        return "o"
    elif(rooms[0]=="x" and rooms[1]=="x" and rooms[2]=="x") or (rooms[0]=="x" and rooms[4]=="x" and rooms[8]=="x") or (rooms[0]=="x" and rooms[3]=="x" and rooms[6]=="x") or (rooms[2]=="x" and rooms[4]=="x" and rooms[6]=="x") or (rooms[2]=="x" and rooms[5]=="x" and rooms[8]=="x") or (rooms[0]=="x" and rooms[1]=="x" and rooms[2]=="x")  or (rooms[1]=="x" and rooms[4]=="x" and rooms[7]=="x") or (rooms[3]=="x" and rooms[4]=="x" and rooms[5]=="x")  or (rooms[6]=="x" and rooms[7]=="x" and rooms[8]=="x"):
        return "x"
    else:
        for i in range(9):
            if rooms[i]!="  ":
                draw=True 
            else:
                draw=False
                break;
        if draw==True:
            return "draw"
        else:
            return "NULL"                                                  
#if anybody click on any box then this function set what we should do.                    
def click(i,room):
        global started,turn,rooms,o_win,x_win,o_score,x_score
        if room['text']=="  ":
            if turn=="x":
                rooms[i]=turn
                room['text']=rooms[i]
                room['fg']="red"
                turn="o"
                if result()=="NULL":
                    pass
                elif result()=="draw":
                    started=False   
                    messagebox.showinfo("draw", "This game is draw") 
                    x_score['text']="x_{}".format(x_win) 
                    o_score['text']="o_{}".format(o_win) 
                    make_all_none()
                    turn="x"
                elif result()=="x":
                    started=False  
                    messagebox.showinfo("congrats", "x win") 
                    x_win+=1      
                    x_score['text']="x_{}".format(x_win)
                    make_all_none()  
                    turn="x"
            else:
                rooms[i]=turn       
                room['text']=rooms[i]
                turn="x"   
                if result()=="o":
                    started=False  
                    messagebox.showinfo("congrats", "o win") 
                    o_win+=1
                    o_score['text']="o_{}".format(o_win)
                    make_all_none()      
                    turn="x"
                elif result()=="draw":
                    started=False   
                    messagebox.showinfo("draw", "This game is draw") 
                    x_score['text']="x_{}".format(x_win) 
                    o_score['text']="o_{}".format(o_win) 
                    make_all_none()
                    turn="x"
        started=True      
#creating window.        
root=Tk()
#setting title.
root.title("Tic-Tac-Toe")
#if game is not start make all "  ".
if started==False:
    make_all_none()    
#creating score board.    
x_score=Label(root,text="x_{}".format(x_win),bg="green")
o_score=Label(root,text="o_{}".format(o_win),bg="green")
#creating button.
button_0=Button(root,text=rooms[0],bg="lightgreen",command=lambda:click(0,button_0),width=4,height=4)
button_1=Button(root,text=rooms[1],bg="lightgreen",command=lambda:click(1,button_1),width=4,height=4)
button_2=Button(root,text=rooms[2],bg="lightgreen",command=lambda:click(2,button_2),width=4,height=4)
button_3=Button(root,text=rooms[3],bg="lightgreen",command=lambda:click(3,button_3),width=4,height=4)
button_4=Button(root,text=rooms[4],bg="lightgreen",command=lambda:click(4,button_4),width=4,height=4)
button_5=Button(root,text=rooms[5],bg="lightgreen",command=lambda:click(5,button_5),width=4,height=4)
button_6=Button(root,text=rooms[6],bg="lightgreen",command=lambda:click(6,button_6),width=4,height=4)
button_7=Button(root,text=rooms[7],bg="lightgreen",command=lambda:click(7,button_7),width=4,height=4)
button_8=Button(root,text=rooms[8],bg="lightgreen",command=lambda:click(8,button_8),width=4,height=4)
#display score board on window.
x_score.grid(row=0,column=0)
o_score.grid(row=0,column=2) 
#display button on window.
button_0.grid(row=1,column=0)        
button_1.grid(row=1,column=1)
button_2.grid(row=1,column=2)
button_3.grid(row=2,column=0)
button_4.grid(row=2,column=1)
button_5.grid(row=2,column=2)
button_6.grid(row=3,column=0)
button_7.grid(row=3,column=1)
button_8.grid(row=3,column=2)
#score board size.
x_score.config(font=("Courier",10))
o_score.config(font=("Courier",10))
#button size.
button_0.config(font=("Courier",8))
button_1.config(font=("Courier",8))
button_2.config(font=("Courier",8))
button_3.config(font=("Courier",8))
button_4.config(font=("Courier",8))
button_5.config(font=("Courier",8))
button_6.config(font=("Courier",8))
button_7.config(font=("Courier",8))
button_8.config(font=("Courier",8))
#change the background color.
root.config(background="green")
#runing the loop of the window.
root.mainloop()