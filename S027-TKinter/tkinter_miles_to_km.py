from tkinter import *


def convert():
    mile_value = float(miles.get())
    km_value = mile_value * 1.609
    km.config(text=str(round(km_value, 2)))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Miles
miles = Entry(width=7)
miles.grid(column=1, row=0)

# Miles Unit Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# is equals to Label
is_equals_to = Label(text="is equals to")
is_equals_to.grid(column=0,row=1)

# Km Converted Label
km = Label(text="")
km.grid(column=1,row=1)

# Km Units Label
km_label = Label(text="Km")
km_label.grid(column=2,row=1)

# Convert Button
convert = Button(text="Calculate", command=convert)
convert.grid(column=1,row=3)

window.mainloop()
