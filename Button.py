import tkinter as tk
from tkinter import messagebox
win=tk.Tk()
tv=tk.StringVar()
def Click_me():
    msg=messagebox.showinfo("entry Widged","hello"+tv.get())
t1=tk.Entry(win,textvariable=tv)
   # print("I am Click")


btn=tk.Button(win,text='Click', command=Click_me)
btn.pack()
win.mainloop()
