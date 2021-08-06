from tkinter import *
root = Tk()
root.geometry("600x400")

intro = Label(root, text="WELCOME TO THE DANCE CLASSES", font=("TimesNewRoman", "15", "bold"), bg="Red", fg="black")
intro.grid(padx=150)
name = Label(root, text="NAME", font=("TimesNewRoman", 10, "bold"))
name.grid(row=3, column=0)

age = Label(root, text="AGE", font=("TimesNewRoman", 10, "bold"))
age.grid(row=4, column=0)

dance_classes_type = Label(root, text="DANCE TYPE", font=("TimesNewRoman", 10, "bold"))
dance_classes_type.grid(row=5, column=0)

name = StringVar()
age = IntVar()
dance_classes_type = StringVar()

name_entry = Entry(root, textvariable=name)
name_entry.grid(row=3, column=1)
age_entry = Entry(root, textvariable=age)
age_entry.grid(row=4, column=1)
dance_entry = Entry(root, textvariable=dance_classes_type)
dance_entry.grid(row=5, column=1)


def get_results():
    print(f"NAME IS : {name_entry.get()}")
    print(f"AGE IS : {age_entry.get()}")
    print(f"DANCE-TYPE IS : {dance_entry.get()}")


submit = Button(root, text="Submit", fg="black", command=get_results)
submit.grid(row=6,column=1)

root.mainloop()
