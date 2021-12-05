import tkinter
win=tkinter.Tk()
win.title("First App")
txt=win.title()
print(txt)
win.resizable(True,True)
w=800
h=650
ws=win.winfo_screenwidth()
hs=win.winfo_screenmmheight()
x=ws/2-w/2
y=hs/2-h/2
win.geometry("%dx%d+%d+%d" %(w,h,x,y))
# win.minsize(100,100)
# win.maxsize(500,500)
# win.attributes('-alpha',0.7)
win.mainloop()

