#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

p_letters = ""
p_symbols = ""
p_numbers = ""

# OR can create a list and append characters to the end of them


for letter in range(0, nr_letters):
    p_letters += letters[random.randint(0, len(letters) - 1)] # OR random.choice(letters)
for symbol in range(0, nr_symbols):
    p_symbols += symbols[random.randint(0, len(symbols) - 1)] # OR random.choice(symbols)
for number in range(0, nr_numbers):
    p_numbers += numbers[random.randint(0, len(numbers) - 1)] # OR random.choice(numbers)

easy_password = p_letters + p_symbols + p_numbers

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = list(easy_password)
random.shuffle(hard_password)
hard_password = ''.join(hard_password)

print(f"Here is your password {hard_password}")
