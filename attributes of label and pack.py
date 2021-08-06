from tkinter import *
root = Tk()
root.geometry("800x400")
root.title("My first GUI!!HELLO WORLD")

# important label options
# text = add_the_text
# bd = background
# fg = foreground
# font = set_the_font
# pad_x = x_padding
# pad_y = y_padding
# relief = border_styling = SUNKEN,RAISED,GROOVE,RIDGE

text_label = Label(text="machine learning is a method of data analysis that automates analytical model building. "
                        "\nIt is a branch of artificial intelligence based on the idea "
                        "\nthat systems can learn from data, identify patterns and make decisions "
                        "\nwith minimal human intervention.", bg="blue", fg="black", padx=44, pady=44,
                   font=("TimesNewRoman", 10))

# important pack options
# anchor =  "sw","nw","ne","se"  -> directions
# side = BOTTOM,TOP,left,right
# fill = x,y
# pad_x = 
# pad_y =
text_label.pack(anchor="nw", fill="y", side="left")

root.mainloop()
