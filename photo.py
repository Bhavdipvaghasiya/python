import tkinter as tk
from tkinter import Button, IntVar, PhotoImage
win=tk.Tk()
img=PhotoImage(file='C:\\Windows\\Web\\Wallpaper\\Characters\\img20.png')
bt=Button(win,text='Bhavip',image=img,height=20,width=100)
bt.pack()
win.mainloop()