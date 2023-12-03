# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper_func(*args):
        func_name = function.__name__
        arguments = args
        print(f"function: {func_name}\nArguments: {arguments}")
    return wrapper_func


# Use the decorator 👇

@logging_decorator
def hello(name, favourite_number):
    print(f"Hello, {name.title()}")
    print(f"Your favourite number is {favourite_number}")


hello('shrivar', 13)
