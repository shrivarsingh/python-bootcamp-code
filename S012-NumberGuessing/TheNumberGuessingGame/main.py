import art
import random


LEVEL = {"easy": 10, "hard": 5}


def app_logo():
    return art.logo + (art.creator)


def intro():
    print(app_logo())
    print("Welcome to the Number Guessing Game!")


def random_number():
    return random.randint(1, 100)


def check_difficulty():
    print("Easy = 10 chances | Hard = 5 chances")
    difficulty = input("Chose a difficulty. Type \"easy\" or \"hard\": ")
    if difficulty[0].lower() == "e":
        print("Easy selected.")
        return LEVEL["easy"]
    elif difficulty[0].lower() == "h":
        print("Hard selected.")
        return LEVEL["hard"]
    else:
        print("Cannot recognize input. Defaulting to easy difficulty.")
        return LEVEL["easy"]


def check_guess(num, chances):
    guess_num = 0
    guessed_numbers = []
    while not guess_num == num and chances > 0:
        ps = "attempts" if chances > 1 else "attempt"
        print(f"\nYou have {chances} {ps} remaining to guess the number.")
        guess_num = int(input("Make a guess: "))
        guessed_numbers.append(str(guess_num))
        print(f"\nNumbers guessed: {(', '.join(guessed_numbers))}", end = "")
        if guess_num < num:
            print(f"\nIt's a number higher than {guess_num}", end = ".")
        elif guess_num > num:
            print(f"\nIt's a number lower than {guess_num}", end = ".")
        chances = chances - 1
    if guess_num == num:
        return f"\nYou got it! I was thinking of {num}. Great minds think alike!"
    else:
        return f"\nYou have run out of chances, the correct number was {num}. You Lose."


def number_guess():
    intro()
    random_num = random_number()
    print("I'm thinking of a number between 1 and 100.")
    # print(f"Pssst! The correct answer is {random_num}")
    num_lives = check_difficulty()
    player_guess = check_guess(num=random_num, chances=num_lives)
    print(player_guess)
    print("GoodBye.\n")


number_guess()
