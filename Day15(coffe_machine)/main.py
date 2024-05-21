from data import MENU, resources


def is_resource_available(check_ingredient_for_order):
    for item in check_ingredient_for_order:
        if check_ingredient_for_order[item] >= resources[item]:
            print(f"not enough {item}")
            return False
    return True



def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money")
        return False


def make_coffee(drink_name, check_ingredient_for_order):
    for item in check_ingredient_for_order:
        resources[item] -= check_ingredient_for_order[item]
    print(f"here your coffee!!! ☕")





profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso, latte, capuccino): ")
    if choice == "off".lower().strip():
        is_on = False
    elif choice == "report".lower().strip():
        print(f"Water - {resources['water']}ml")
        print(f"Milk - {resources['milk']}ml")
        print(f"Coffee - {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_available(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

