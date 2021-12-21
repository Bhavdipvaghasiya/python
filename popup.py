import tkinter as tk
from tkinter import *
from tkinter import messagebox

win=tk.Tk()
win.geometry("500x500")
label=Label(win,text="Bhavdip",font=("Helvetica",18))
label.pack()
popup=Menu(win,tearoff=0)
popup.add_command(label="New")
popup.add_command(label="Open")
popup.add_separator()
popup.add_command(label="Exit",accelerator='Ctrl+A')

def menu_popup(event):
    try:
        popup.tk_popup(event.x_root,event.y_root,0)
    finally:
        popup.grab_release()
    
click=StringVar()
main_menu=OptionMenu(win,click,"c++","Java",'Python')
main_menu.pack()
def btn_click():
    curindex=l1.curselection()
    for i in curindex:
        mes=messagebox.showinfo("List widget",l1.get(i))

l1=Listbox(win)
l1.insert(1,"Bhavdip")
l1.insert(2,"Kushan")
l1.pack()
win.bind('<Button-3>',menu_popup)

button=Button(win,text="Quick",command=btn_click)
button.pack()
win.mainloop()