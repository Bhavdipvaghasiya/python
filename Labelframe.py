import tkinter as tk

win=tk.Tk()
lf=tk.LabelFrame(win,text="A",padx=10,pady=10)
lf.pack()
btn=tk.Button(lf,text='Click')
btn.pack()
win.mainloop()