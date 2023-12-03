import time

def scroll_print(text):
    for letter in text:
        print(letter, end = "")
        time.sleep(0.01)
    print()

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
scroll_print("Welcome to Treasure Island.")
scroll_print("Your mission is to find the treasure.")
print()

scroll_print("You're at a cross road. Where do you want to go? \"left\" or \"right\"?")
choice1 = input("> ").lower()

if choice1 == "left":
    print()
    scroll_print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat or \"swim\" to swim across.")
    choice2 = input("> ").lower()
    if choice2 == "wait":
        print()
        scroll_print("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you use?")
        choice3 = input("> ").lower()
        if choice3 == "yellow":
            print()
            scroll_print("O_O You are mesmerized by the amount of treasure before you.")
            print("You win!")
        elif choice3 == "red":
            print()
            scroll_print("Do you also smell the gas?... OH!... BOOM!... You are burned by fire.")
            print("Game Over.")
        else:
            print()
            scroll_print("OMG! You get mauled by beasts.")
            print("Game Over.")
    else:
        print()
        scroll_print("Oh dear! you get attacked by a trout.")
        print("Game Over.")
else:
    print()
    scroll_print("Oh no! You fell into hole!")
    print("Game Over.")
