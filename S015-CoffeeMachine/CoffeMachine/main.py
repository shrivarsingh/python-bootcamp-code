MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

logo = """
  ______            ______   ______                         __       __          __                         
 /      \\          /      \\ /      \\                       /  \\     /  |        /  |                        
/$$$$$$  | ______ /$$$$$$  /$$$$$$  ______   ______        $$  \\   /$$ | ______ $$ |   __  ______   ______  
$$ |  $$/ /      \\$$ |_ $$/$$ |_ $$/      \\ /      \\       $$$  \\ /$$$ |/      \\$$ |  /  |/      \\ /      \\ 
$$ |     /$$$$$$  $$   |   $$   | /$$$$$$  /$$$$$$  |      $$$$  /$$$$ |$$$$$$  $$ |_/$$//$$$$$$  /$$$$$$  |
$$ |   __$$ |  $$ $$$$/    $$$$/  $$    $$ $$    $$ |      $$ $$ $$/$$ |/    $$ $$   $$< $$    $$ $$ |  $$/ 
$$ \\__/  $$ \\__$$ $$ |     $$ |   $$$$$$$$/$$$$$$$$/       $$ |$$$/ $$ /$$$$$$$ $$$$$$  \\$$$$$$$$/$$ |      
$$    $$/$$    $$/$$ |     $$ |   $$       $$       |      $$ | $/  $$ $$    $$ $$ | $$  $$       $$ |      
 $$$$$$/  $$$$$$/ $$/      $$/     $$$$$$$/ $$$$$$$/       $$/      $$/ $$$$$$$/$$/   $$/ $$$$$$$/$$/       
 """

# TODO: 1. Prompt user input.

# TODO: 2. Turn coffee machine off by using "off".

# TODO: 3. Display current resource values when "resources" is entered.

# TODO: 4. Check sufficient resources to make requested coffee.

# TODO: 5. Process coins inserted.

# TODO: 6. Check correct amount of coins inserted.

# TODO: 7. Make Coffee by using resources required.


def report():
    """Prints the available resources."""

    def border(character):
        for i in range(25):
            print(f"{character}", end="")
        print()

    print()
    border("-")
    print(f"{'{:<18}'.format('Resource')}Amount")
    border("-")
    unit_before = ""
    unit_after = ""
    for resource in resources:
        if resource == "water" or resources == "milk":
            unit_before = ""
            unit_after = " ml"
        elif resource == "coffee":
            unit_before = ""
            unit_after = " g"
        elif resource == "profit":
            unit_before = "$"
            unit_after = ""
        resource_display = '{:<14}'.format(resource.title())
        amount_display = '{:>9}'.format(unit_before + str(resources[resource]) + unit_after)
        print(f" {resource_display}{amount_display}")
    border("-")
    print()


def coffee_choice():
    """Prompts the user and returns a valid input."""
    while True:
        print("What would you like to have?")
        coffee_list = []
        for option in MENU:
            coffee_list.append(option)
            o = '{:<12}'.format(option.title())
            print(f"☕ {(len(coffee_list))}. {o} ${MENU[option]['cost']:.2f}")
        c = input("> ")
        if c == "off":
            return "off"
        elif c == "report":
            report()
        elif c == "1":
            return coffee_list[0]
        elif c == "2":
            return coffee_list[1]
        elif c == "3":
            return coffee_list[2]
        else:
            print("\n⚠ No, we do not make Tea. Please select one of available options displayed. ⚠")


def sufficient_resources(required_ingredients):
    print()
    num_ingredients = len(required_ingredients)
    for required in required_ingredients:
        if required in resources:
            if required_ingredients[required] <= resources[required]:
                print(f"✔ {required.title()} Levels: Sufficient.")
                num_ingredients -= 1
            else:
                print(f"❌ {required.title()} Levels: Insufficient.")
    if num_ingredients == 0:
        return True
    else:
        return False


def process_coins(price):
    print()
    total_credits = 0.00
    coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    for coin in coins:
        print(f"Please pay: ${price:.2f} | Credits: ${total_credits:.2f}")
        num_coins = int(input(f"How many {coin} would you like to insert:\n${coins[coin]:.2f} x "))
        total_credits = total_credits + (coins[coin] * num_coins)
        print()
    print(f"Please pay: ${price:.2f} | Credits: ${total_credits:.2f}\n🔃 Validating...")
    if total_credits == price:
        print(f"Perfect amount. No change required.")
        return True
    elif total_credits > price:
        print(f"\nPlease take your change: ${(total_credits - price):.2f}")
        return True
    else:
        print("⚠ Insufficient Funds. ⚠")
        return False


print(logo)
power_on = True
resources["profit"] = float(0.00)
while power_on:
    coffee = coffee_choice()
    if coffee in MENU:
        coffee_ingredients = MENU[coffee]["ingredients"]
        if sufficient_resources(coffee_ingredients):
            coffee_cost = MENU[coffee]["cost"]
            if process_coins(coffee_cost):
                resources["profit"] = resources["profit"] + coffee_cost
                print(f"🔃 Making {coffee} for ${resources['profit']:.2f}.")
                for coffee_ingredient in coffee_ingredients:
                    resources[coffee_ingredient] = resources[coffee_ingredient] - coffee_ingredients[coffee_ingredient]
                print("✔ Done.")
                print(f"\nHere is your {coffee.title()}. Enjoy!\n")
            else:
                print("\n🔃 Reloading data...\n")
        else:
            print("\n⚠ Oops looks like we lack the resources to make what you require. ⚠\n")
    else:
        power_on = False
        print("\n🔌 Coffee Maker is now shutting down.\n")
