
menu = {
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

profit = 0
espresso_change = 0
latte_change = 0
cappuccino_change = 0
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
again = True

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def espresso_changes():
    """This function makes changes to the resources as an espresso is made."""
    resources["water"] -= menu["espresso"]["ingredients"]["water"]
    resources["coffee"] -= menu["espresso"]["ingredients"]["coffee"]
    resources["milk"] -= 0
    return resources

def latte_changes():
    """This function makes changes to the resources as a latte is made."""
    resources["water"] -= menu["latte"]["ingredients"]["water"]
    resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
    resources["milk"] -= menu["latte"]["ingredients"]["milk"]
    return resources

def cappuccino_changes():
    """This function makes changes to the resources as a cappuccino is made."""
    resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
    resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
    resources["milk"] -= menu["cappuccino"]["ingredients"]["milk"]
    return resources

def check_enough_resources_espresso():
    if resources["water"] >= menu["espresso"]["ingredients"]["water"] and resources["coffee"] >= menu["espresso"]["ingredients"]["coffee"]:
        check_enough_money_espresso()
    else:
        print("The espresso cannot be made. Insufficient resources.")
        global again
        again = False
    
def check_enough_resources_latte():    
    if resources["coffee"] >= menu["latte"]["ingredients"]["coffee"] and resources["milk"] >= menu["latte"]["ingredients"]["milk"] and resources["water"] >= menu["latte"]["ingredients"]["water"]:
        check_enough_money_latte()
    else:
        print("The latte cannot be made. Insufficient resources.")
        global again
        again = False

def check_enough_resources_cappuccino():
    if resources["milk"] >= menu["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= menu["cappuccino"]["ingredients"]["coffee"] and resources["water"] >= menu["cappuccino"]["ingredients"]["water"]:
        check_enough_money_cappuccino()
    else:
        print("The cappuccino cannot be made. Insufficient resources.")
        global again
        again = False

def make_espresso():
    espresso_changes()
    print(f"Here is your change: ${round(espresso_change, 2)}")
    print("Enjoy your espresso!")
    start()

def make_latte():
    latte_changes()
    print(f"Here is your change: ${round(latte_change, 2)}")
    print("Enjoy your latte!")
    start()

def make_cappuccino():
    cappuccino_changes()
    print(f"Here is your change: ${round(cappuccino_change, 2)}")
    print("Enjoy your cappuccino!")
    start()

def check_enough_money_espresso():
    user_money = money_calculation()
    if user_money >= menu["espresso"]["cost"]:
        global profit 
        global espresso_change
        profit += menu["espresso"]["cost"]
        espresso_change = user_money - menu["espresso"]["cost"]
        make_espresso()
    else:
        print("Sorry there isn't enough money. Money refunded.")

def check_enough_money_latte():
    user_money = money_calculation()
    if user_money >= menu["latte"]["cost"]:
        global profit 
        global latte_change
        profit += menu["latte"]["cost"]
        latte_change = (user_money - menu["espresso"]["cost"])
        make_latte()
    else:
        print("Sorry there isn't enough money. Money refunded.")

def check_enough_money_cappuccino():
    user_money = money_calculation()
    if user_money >= menu["cappuccino"]["cost"]:
        global profit 
        global cappuccino_change
        profit += menu["cappuccino"]["cost"]
        cappuccino_change = (user_money - menu["cappuccino"]["cost"])
        make_cappuccino()
    else:
        print("Sorry there isn't enough money. Money refunded.")

def money_calculation(): # This calculates the total money the user inputs into the coffee machine.
    user_input_quarter = int(input("How many quarters?: "))
    user_input_dime = int(input("How many dimes?: "))
    user_input_nickel = int(input("How many nickels?: "))
    user_input_penny = int(input("How many pennies?: "))
    user_money_total = (user_input_penny * penny) + (user_input_nickel * nickel) + (user_input_dime * dime) + (user_input_quarter * quarter)
    return user_money_total

def start():
    global again
    while again:
        user_input = input("What would you like? (espresso, latte, cappucino, or type 'off' to turn off the machine): ")

        if user_input == "espresso":
            check_enough_resources_espresso()

        elif user_input == "latte":
            check_enough_resources_latte()

        elif user_input == "cappuccino":
            check_enough_resources_cappuccino()

        elif user_input == "report":
            report()

        elif user_input == "off":
            print("Goodbye!")
            again = False
        else:
            start()
start()
