programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    }

# list[0] vs dictionary[key]

print()
print(programming_dictionary["Bug"])
programming_dictionary["Programming"] = "Programming is the process of creating a set of instructions that tell a computer how to perform a task."

print()
print(programming_dictionary)
print()

empty_list = []

# Creates an empty dictionary or wipes a dictionary
empty_dictionary = {}

print(programming_dictionary["Bug"])
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])
print()


# Loop through a dictionary
for thing in programming_dictionary:
    print(thing) # prints key
    print(programming_dictionary[thing])
