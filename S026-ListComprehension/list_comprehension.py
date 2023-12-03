# List Comprehension
# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]  # 4 or less characters
print(short_names)
long_names_caps = [name.upper() for name in names if len(name) >= 5]  # 5 characters or more in upper case
print(long_names_caps)
