# from replit import clear
# HINT: You can call clear() to clear the output in the console.

from art import logo

# function to clear terminal
import os # for clear screen
def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def add_bid(bid_name, bid_value):
    bids[bid_name] = bid_value


def check_bids(bid_record):
    print(logo)
    highest_bidder = ""
    highest_bid = 0
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            highest_bidder = bidder
    bid_bids = "bids" if num_of_bids > 1 else "bid"
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid} out of {num_of_bids} {bid_bids}")
    

clear()
disp_text = "Welcome to the secret auction program.\n"
bids = {}
num_of_bids = 0
new_bid = True
while new_bid:
    print(logo)
    print(disp_text)
    name = input("What is your name?\n> ")
    bid = int(input("What is your bid?\n> $"))
    add_bid(bid_name=name, bid_value=bid)
    add_new = input("Are there any other bidders? Type \"y\" for yes or \"n\" for no.\n> ").lower()
    new_bid = False if (add_new[0] == "n") else True
    num_of_bids += 1
    disp_text = f"Current active bids: {num_of_bids}\n"
    clear()
check_bids(bid_record=bids)
