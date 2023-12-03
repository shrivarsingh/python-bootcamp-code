# Debug Exercise

# # Original Code
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# My Solution Code
for number in range(1, 101):
    new_line = "\n" if number % 5 == 0 else "\t"
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz", end = new_line)
    elif number % 3 == 0:
        print("Fizz", end = new_line)
    elif number % 5 == 0:
        print("Buzz", end = new_line)
    else:
        print(number, end = new_line)
