import random

count = 0
while True:
    Roll = input("Do you want to roll the dice? (y/n): ")
    if Roll.lower()== "y":
        try:
            roll_length = int(input("How many dices you want to roll? "))
        except ValueError:
            print("Invalid input! Plz enter a valid number")
            continue
        rolled_dice =[]
        for i in range(roll_length):
            rolled_dice.append(random.randint(1,6))
        print(rolled_dice)
        count += 1

    elif Roll.lower() == "n":
        print("Thanks for playing. You have rolled the dices",count,"times")
        break
    else:
        print("Invalid input, Plz enter y or n")
    
    




