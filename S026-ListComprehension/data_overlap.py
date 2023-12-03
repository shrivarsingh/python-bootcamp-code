# day-26-3-exercise

with open("file1.txt") as file:
    file1 = file.readlines()
num_file1 = [int(num.strip()) for num in file1]
print(f"\nfile1.txt: {num_file1}")

with open("file2.txt") as file:
    file2 = file.readlines()
num_file2 = [int(num.strip()) for num in file2]
print(f"\nfile2.txt: {num_file2}")

print("\nCommon numbers are:")
if len(num_file1) > len(num_file2):
    result = [num for num in num_file1 if num in num_file2]
else:
    result = [num for num in num_file2 if num in num_file1]

# Write your code above 👆

print(result)


