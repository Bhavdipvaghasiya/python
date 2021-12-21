import tkinter as tk


win=tk.Tk()
win.geometry("500x400")
def test():
    pass
manubar=tk.Menu(win)
filemanu=tk.Menu(manubar)
manubar.add_cascade(label="File", menu=filemanu)
filemanu.add_command(label="Open", command=test)
manubar.add_separator()
win.config(menu=manubar)

win.mainloop()