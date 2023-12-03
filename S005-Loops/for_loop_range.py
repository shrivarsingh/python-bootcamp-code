# For loop with Range

for number in range(1, 11):
    print(number, end = " ")
print()

for number in range(1, 11, 3):
    print(number, end = " ")
print()

# add numbers 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)
