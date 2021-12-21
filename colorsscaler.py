
import tkinter as tk
from tkinter import colorchooser

from tkinter import *
from tkinter import messagebox

from matplotlib import colors

win=Tk()
win.geometry('500x500')
sc1=DoubleVar()
sc2=DoubleVar()
sc3=DoubleVar()
def btn_click():
    cc1=colorchooser.askcolor()
        
    
sca1=Scale(win,variable=sc1,from_=0,to=255,showvalue=1,resolution=1)
sca1.pack()
sca2=Scale(win,variable=sc2,from_=0,to=255,showvalue=1,resolution=1)
sca2.pack()
sca3=Scale(win,variable=sc3,from_=0,to=255,showvalue=1,resolution=1)
sca3.pack()

btn=Button(win,text="Click",command=btn_click)

btn.pack()

win.mainloop()