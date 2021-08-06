from tkinter import *
from win32com.client import Dispatch
root = Tk()


def Hello():
    print("Hello world!!")


def print_name():
    print("Hello my name is Bhavneet")


def speaks():
    speaker = Dispatch("Sapi.SpVoice")
    speaker.Speak("Hello my name is Bhavneet")


root.geometry("600x400")

f1 = Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
f1.pack(side=TOP, fill='x')
b1 = Button(f1, fg="red", text="Print_now", command=Hello)
b1.pack(side=LEFT)
b2 = Button(f1, fg="red", text="Print_now", command=print_name)
b2.pack(side=LEFT)
b3 = Button(f1, fg="red", text="Print_now", command=speaks)
b3.pack(side=LEFT)
root.mainloop()
