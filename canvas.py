from os import extsep, stat
import tkinter as tk
from tkinter import *

win=tk.Tk()
ca=Canvas(win,width=400,height=400,bg='red')
ca.pack()

ca.create_line(100,10,100,10)

card=100,50,40,10
arg=ca.create_arc(card,start=10,extent=150,fill='blue')

win.mainloop()