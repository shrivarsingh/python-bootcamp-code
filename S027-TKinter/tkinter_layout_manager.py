from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("My First Python GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I am a Label.", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="New New Text")
my_label.config(padx=50, pady=50)

# Buttons
button1 = Button(text="Click Me", command=button_clicked)  # Command name of function without parenthesis
button1.grid(column=1, row=1)

# Buttons
button2 = Button(text="Click Me", command=button_clicked)  # Command name of function without parenthesis
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=4, row=3)


window.mainloop()  # Always must be the last line of code
