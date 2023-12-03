# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
 
print("   1  2  3")
print("1", end = " ")
print(*row1, sep = " ")
print("2", end = " ")
print(*row2, sep = " ")
print("3", end = " ")
print(*row3, sep = " ")

position = input("Where do you want to put the treasure? XY? ")


horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1
map[vertical][horizontal] = "❌"

print("   1  2  3")
print("1", end = " ")
print(*row1, sep = " ")
print("2", end = " ")
print(*row2, sep = " ")
print("3", end = " ")
print(*row3, sep = " ")

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")