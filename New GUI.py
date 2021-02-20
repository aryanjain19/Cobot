from tkinter import *
from tkinter.ttk import *
base = Tk()
base.title("COBOT")
base.resizable(width = False,height = False)
base.configure(width = 470,height = 550,bg = "#17202A")
head = Label(base,text = "Welcome to CoBot !",font = ("helvetica",15),foreground = "orange",background ="#17202A" )
head.place(x =230,y = 30, anchor= CENTER)
footer = LabelFrame(base,borderwidth= 5,width= 450,height = 50).place(x = 10,y = 480)

send = Button(footer,text="Send",command = None,width = 10)

send.place(x = 380,y = 490)
base.mainloop()
