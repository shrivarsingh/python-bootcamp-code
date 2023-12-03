#Write your code below this line 👇
import math


def paint_calc(height, width, cover):
    # 1 can of paint can cover 5 square meters
    number_of_cans = math.ceil(height * width / cover)
    unit = "cans" if number_of_cans > 1 else "can"
    print(f"you will need {number_of_cans} {unit} of paint")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
