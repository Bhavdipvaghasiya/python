import tkinter as tk
from  tkinter import Button
topwin=tk.Tk()
btn=Button(topwin,text="Click Me", width=4, height=3,activebackground="red",activeforeground="yellow",bg="white")
btn.place(x=50,y=30)

topwin.mainloop()
