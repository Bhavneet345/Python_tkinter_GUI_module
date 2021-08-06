from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("800x600")
root.title("Newspaper")

# frame1 for heading
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(fill="x")
l1 = Label(f1, text="NEW24TIMES", fg="black", font=("TimesNewRoman", "15", "bold"))
l1.pack()


# frame2 for Images
f2 = Frame(root, borderwidth=6, relief=SUNKEN)
f2.pack(fill="y",side=LEFT)
l2 = Label(f2, fg="grey", text="Images", font=("TimesNewRoman","15","bold"))
l2.pack()
photo = []
for i in range(1,4):
   img = Image.open(f'img{i}.jpg')
   photo.append(ImageTk.PhotoImage(img))
for i in range(0,3):
    Label(f2,image=photo[i]).pack()

# frame3 for content of the images
f3 = Frame(root, bg="white", borderwidth=6, relief=SUNKEN)
f3.pack(fill="x",anchor="ne")
l3 = Label(f3, text="Headings", borderwidth=6, relief=SUNKEN, fg="black", font=("TimesNewRoma", "15", "bold"))
l3.pack()
content = []
for i in range(1,4):
    with open(f"file{i}") as f:
        text = f.read()
        content.append(text)
    l4 = Label(text=f'{i}.{content[i-1]}\n', font=("TimesNewRoman", "15"), fg="black")
    l4.pack()
root.mainloop()

