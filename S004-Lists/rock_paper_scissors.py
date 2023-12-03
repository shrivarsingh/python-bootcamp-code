import random

rock = '''
ROCK!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

print("\nWelcome to ✊Rock ✋Paper ✌Scissors")
print("\nChoose your destiny:")
choice = int(input("0 for Rock\n1 for Paper\n2 for Scissors\n> ")[0])
computer = random.randint(0, 2)
print(f"\nYou chose:{rps[choice]}\nComputer chose:{rps[computer]}")

# rock rps[0] beats scissors rps[2], scissors rps[2] beats paper rps[1], paper rps[1] beats rock rps[0]
if choice == computer:
    print("It's a Draw.")
elif choice == 0 and not computer == 1:
    print("You win!")
elif choice == 1 and not computer == 2:
    print("You win!")
elif choice == 2 and not computer == 0:
    print("You win!")
else:
    print("You lose.")
