from game_data import data
from art import logo
from art import vs
from random import randint
import os # for clear screen


# function to clear terminal
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def select_random_data(lenght_of_data):
    return randint(0, (lenght_of_data-1))

def print_data(data_num):
    if data[data_num]['description'][0].lower() in ['a', 'e', 'i', 'o', 'u']:
        a_an = "an"
    else:
        a_an = "a"
    print(f"{data[data_num]['name']}, {a_an} {data[data_num]['description']}, from {data[data_num]['country']}.")

def followers(data_for_follower):
    return data[data_for_follower]['follower_count']

def higher_lower():
    score = 0
    prompt = ""
    a = select_random_data(len(data))
    while True:
        clear()
        print(logo)
        print(f"{prompt}Score: {score}.\n")
        print("Compare A:", end = " ")
        print_data(a)
        print(followers(a))
        print("\t\t" + vs)
        print("Against B:", end = " ")
        b = select_random_data(len(data))
        while b == a:
            b = select_random_data(len(data))
        print_data(b)
        print(followers(b))
        choices = ["A", "B"]
        c = input("Who has more followers? Type \"A\" or \"B\": ")[0].upper()
        while not c in choices:
            c = input("Cannot recognize choice. Please retype \"A\" or \"B\": ")[0].upper()
        if c == "A":
            if followers(a) > followers(b):
                prompt = "You're right! "
                score  = score + 1
                a = b
            else:
                clear()
                print(logo)
                print(f"Incorrect Answer!\nFinal Score: {score}.")
                return
        elif c == "B":
            if followers(b) > followers(a):
                prompt = "You're right! "
                score  = score + 1
                a = b
            else:
                clear()
                print(logo)
                print(f"Incorrect Answer!\nFinal Score: {score}.")
                return

higher_lower()
