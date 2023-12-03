#Write your code below this row 👇
total = 0
for number in range(2, 101, 2):
    total += number
print(f"The sum of the even numbers from 1 to 100 is {total}")

# OR
tot = 0
for number in range(1, 101):
    if number % 2 ==0:
        tot += number
print(f"The sum of the even numbers from 1 to 100 is {tot}")
