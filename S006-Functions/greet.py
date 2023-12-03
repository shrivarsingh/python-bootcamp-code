# # Review: 
# # Create a function called greet(). 
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.

# # Simple function
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
# greet()
# print()

# # Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do? {name}")
#     print("Isn't the weather nice today?")
# greet_with_name("Angela")
# print()

# Functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with(location = "London", name = "Angela")
