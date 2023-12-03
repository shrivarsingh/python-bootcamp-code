from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

main_menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
power_on = True
while power_on:
    choice = input(f"What would you like? {main_menu.get_items()}: ")
    if choice == "report":
        coffee.report()
        money.report()
    elif choice == "off":
        power_on = False
    else:
        selected = main_menu.find_drink(choice)
        if selected is None:
            print()
        elif coffee.is_resource_sufficient(selected):
            if money.make_payment(selected.cost):
                coffee.make_coffee(selected)

# # ANGELA CODE
# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
#
# is_on = True
#
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
#         is_payment_successful = money_machine.make_payment(drink.cost)
#         if is_enough_ingredients and is_payment_successful:
#             coffee_maker.make_coffee(drink)
