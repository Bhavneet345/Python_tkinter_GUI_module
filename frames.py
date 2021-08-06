from tkinter import *
root = Tk()
root.geometry("600x400")
f1 = Frame(root, bg="black", borderwidth=5)
f1.pack(side=TOP)
label = Label(f1, text="FRAME1",bg="red")
label.pack()
root.mainloop()
