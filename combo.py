import tkinter as tk
from tkinter import *
from tkinter import messagebox

win=tk.Tk()
win.geometry("500x500")
# lbldata=StringVar()
# label=Label(win,text="Bahvdip",textvariable=lbldata).pack()
# my=Combobox(win,textvariable=lbldata,width=30)
# t1=("a","b")
# my['values']=t1

# my.current(1)
# my.pack()

v1=IntVar()
v2=IntVar()

def btn_click():
    var=''
    if v1.get()==1:
        var+="Bca Check"
    else:
        var+="Bca Uncheck"
    if v2.get()==1:
        var+="It check"
    else:
        var+="It Uncheck"
    messagebox.showinfo(message=var+'\n')

c1=Checkbutton(win,text="Bca",variable=v1)
c2=Checkbutton(win,text="It",variable=v2)

b11=Button(win,text="Click",command=btn_click)

c1.pack()
c2.pack()
b11.pack()
win.mainloop()