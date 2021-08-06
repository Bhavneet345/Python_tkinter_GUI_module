from tkinter import *
root = Tk()
root.geometry("655x333")

l1 = Label(root, text="Username")
l2 = Label(root, text="Password")
l1.grid()
l2.grid(row=1)

userval = StringVar()
passwordval = StringVar()

user_entry = Entry(root, textvariable=userval)
pass_entry = Entry(root, textvariable=passwordval)

user_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)


def submit_button():
    print("Submission Successful")


def get_val():
    print(f"The user value is {user_entry.get()}")
    print(f"The password is {pass_entry.get()}")


submit = Button(root, text="submit", fg="black", command=get_val)
submit.grid(row=2, column=1)
root.mainloop()

