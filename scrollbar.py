import tkinter as tk
from tkinter import *

win=Tk()
win.geometry('300x400')
s_bar=Scrollbar(win)
s_bar.pack(side=RIGHT,fill=Y)

l_box=Listbox(win,yscrollcommand=s_bar.set)
for i in range(100):
    l_box.insert(i,"Bhavdip Vaghasiya"+str(i))
l_box.pack(side=RIGHT,fill=BOTH)
#s_bar.config(command=l_box)
win.mainloop()
