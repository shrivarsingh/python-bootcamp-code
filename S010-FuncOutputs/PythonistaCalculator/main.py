# Calculator

import click # auto enter for operation symbol
import os # for clear screen
from art import logo

# function to clear terminal for PC
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    clear()
    print(logo)
    num1 = float(input("What's the first number?\n> "))
    ops = "   "
    for operation in operations:
        ops = ops + operation + "  "
    calculation = True
    while calculation:
        # operation_symbol = input("Pick an operation: ")
        print(ops)
        click.echo("Pick an operation:\n> ", nl=False)
        operation_symbol = click.getchar()
        print(operation_symbol)
        num2 = float(input("What's the next number?\n> "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        clear()
        print(logo)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calculation = input(f"Type \"y\" to continue calculating with {answer}, or type \"n\" to restart.\n> ")
        if continue_calculation == "y":
            num1 = answer
            print(f"> {num1}")
        elif continue_calculation == "n":
            calculation = False
            calculator() # Recursion
        else:
            return
            
calculator()
clear()
print(logo)
print("Goodbye.\n")
