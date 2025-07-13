from tkinter import *
import random
import tkinter.messagebox
root=Tk()
root.title("Guessing Game")
root.minsize(350,400)
def okbtn():
    name=entry.get()
    tkinter.messagebox.showinfo("Hello!","Well "+name+" I am thinking of a number between 1 and 20!")
l=Label(root,text="Welcome to our game!")
l.pack()
lb=Label(root,text="What's your name?")
lb.place(x=10,y=100)
entry= Entry(root,width=20)
entry.place(x=150,y=100)
b= Button(root,text="Ok",command=okbtn)
b.place(x=120 ,y=150)

la=Label(root,text="Take a guess!")
la.place(x=10,y=200)
entry1= Entry(root,width=20)
entry1.place(x=150,y=200)
u= Button(root,text="Guess")
u.place(x=110 ,y=250)
root.mainloop()
