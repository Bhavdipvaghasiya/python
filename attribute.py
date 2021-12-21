import tkinter as tk
from tkinter.constants import CENTER

win=tk.Tk()
#win.attributes('-topmost',1)
win.title("My First Program")
win.geometry('200x300+50+50')
#win.iconbitmap()
btn=tk.Button(win,text="Click")
#btn.pack()
#btn.grid(column=4,row=1)
btn.place(x=40,y=40)
# win2=tk.Tk()
# #win2.lift()
# win2.title("My Second Program")
# win2.geometry('200x300+75+75')

# win3=tk.Tk()
# win.lift()
# win3.lower()
# win3.title("My Third Program")
# win3.geometry('200x300+100+100')


win.mainloop()
