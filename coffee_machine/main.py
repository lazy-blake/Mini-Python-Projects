from coffee_data import Menu, resources


def bill_calculator(user):
    """This takes the input of which type of coffee the user want
    and according to that it asks for coins
    and calculate how much money it needs to buy the coffee"""
    if user in Menu:
        print("Please insert a coin")
        coin1 = int(input("How many 5?: "))
        coin2 = int(input("How many 10?: "))
        coin3 = int(input("How many 20?: "))

        coins = 5 * (coin1) + 10 * (coin2) + 20 * (coin3)

        if coins > Menu[user]["cost"]:
            bill = coins - Menu[user]["cost"]
            print(f"Here is {bill} rs in change")
            return True, user

        elif coins < Menu[user]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False, None

        else:
            return True, user
    else:
        print("Invalid Input!!")
        return False, None


def report():
    """It prints the amount of resources remaining at that moment,
    it can be before making the coffee or after"""
    print(
        f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['Money']} rs"
    )


def compare_resources(user_coffee):
    """It takes the coffee name as input
    and calculate if the machine has enough resources to make it"""
    if user_coffee in Menu:
        for i in resources:
            for j in Menu[user_coffee]["ingredients"]:
                if resources[i] >= Menu[user_coffee]["ingredients"][j]:
                    return True, None
                else:
                    print(f"Sorry there is not enough {i}.")
                    return False, i
            return
    else:
        return False, None


def resource_calculator(coffee):
    """It takes the coffe name as input
    and calculate how much ingredients it have to deduct to make that coffee"""
    resources["water"] -= Menu[coffee]["ingredients"]["water"]
    resources["milk"] -= Menu[coffee]["ingredients"]["milk"]
    resources["coffee"] -= Menu[coffee]["ingredients"]["coffee"]


while True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "report":
        report()
        continue
    elif prompt == "shutdown":
        print("Shutting Down.......")
        break
    executing, unavailable = compare_resources(prompt)
    if executing:
        success, coffee_type = bill_calculator(prompt)
        if success:
            resources["Money"] += Menu[coffee_type]["cost"]
            print(f"Here is your {coffee_type}🍵 enjoy!!")
            resource_calculator(coffee_type)
        else:
            continue
    else:
        if unavailable:
            continue
        else:
            print("Invalid Input!!!")
            continue
