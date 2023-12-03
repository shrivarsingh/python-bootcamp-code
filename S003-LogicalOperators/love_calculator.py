# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import time

name_check = name1 + " <3 " + name2

print(f"\nChecking...")

for letter in name_check:
    print(letter, end = "")
    time.sleep(0.1)
print("\n")

name_check = name_check.lower()

name_t = name_check.count("t")
name_r = name_check.count("r")
name_u = name_check.count("u")
name_e = name_check.count("e")
name_l = name_check.count("l")
name_o = name_check.count("o")
name_v = name_check.count("v")
name_true = name_t + name_r + name_u + name_e
name_love = name_l + name_o + name_v + name_e
name_true_love = int(str(name_true) + str(name_love))

if name_true_love < 10 or name_true_love > 90:
    print(f"Your score is {name_true_love}, you go together like coke and mentos.")
elif name_true_love > 40 and name_true_love < 50:
    print(f"Your score is {name_true_love}, you are alright together.")
else:
    print(f"Your score is {name_true_love}.")
