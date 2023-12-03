import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  # for char in range(nr_letters):
  #   password_list.append(random.choice(letters))

  # for char in range(nr_symbols):
  #   password_list += random.choice(symbols)

  # for char in range(nr_numbers):
  #   password_list += random.choice(numbers)

  password_list += [random.choice(letters) for _ in range(nr_letters)]
  password_list += [random.choice(symbols) for _ in range(nr_symbols)]
  password_list += [random.choice(numbers) for _ in range(nr_numbers)]


  random.shuffle(password_list)

  # password = ""
  # for char in password_list:
  #   password += char

  password = "".join(password_list)

  # print(f"Your password is: {password}")
  password_entry.delete(0, "end")
  password_entry.insert(0, string=password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    site = website_entry.get()
    name = username_entry.get()
    password = password_entry.get()

    if len(site) == 0 or len(name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty!")
    else:
    # messagebox.showinfo(title="Title", message="Message")
        confirm = messagebox.askokcancel(title=site, message=f"These are the details entered: \nName:{name}\nPassword: {password}\nSave details?")

        if confirm:
            info = f"{site} | {name} | {password}\n"
            with open("data.txt", mode="a") as file:
                file.writelines(info)
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # Starts cursor inside automatically when application is launched

username_label = tk.Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = tk.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "Shrivar Singh")
# Insert(Index, String) Index is where to insert such as END for adding at end of

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = tk.Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(width=36, text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
