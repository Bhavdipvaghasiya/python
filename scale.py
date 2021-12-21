import tkinter as tk
from tkinter import *
from tkinter import messagebox

win=Tk()
win.geometry('500x500')
sc=DoubleVar()
def btn_click():
    messagebox.showinfo(message=sc.get())
sca1=Scale(win,variable=sc,from_=-100,to=100,showvalue=1,resolution=1)
sca1.pack()

btn=Button(win,text="Click",command=btn_click)
btn.pack()
win.mainloop()