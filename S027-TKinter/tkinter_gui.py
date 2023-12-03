import tkinter

window = tkinter.Tk()
window.title("My First Python GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label.", font=("Arial", 24, "bold"))
# my_label.pack(expand=True)
# my_label.pack(side="bottom")
my_label.pack()
# Label - can change text in the following ways
my_label["text"] = "New Text"
my_label.config(text="New New Text")

# Buttons
def button_clicked():
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)  # Command name of function without parenthesis
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()


window.mainloop()  # Always must be the last line of code
