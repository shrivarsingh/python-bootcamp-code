# import another_module
# # import turtle
# from turtle import Turtle, Screen
#
# print(another_module.another_variable)
#
# # Turtle object
# # timmy = turtle.Turtle()  # Construct an object from blueprint and saved into an object called timmy
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("YellowGreen")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
