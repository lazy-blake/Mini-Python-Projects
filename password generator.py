import string
import random


letters_value = string.ascii_letters
symbols_value = string.punctuation
numbers_value = string.digits

while True:
    letters = int(input("How many letters would u like in your password: "))
    symbols = int(input("How many symbols would u like in your password: "))
    numbers = int(input("How many mumbers would u like in your password: "))

    password_list = []
    for i in range(letters):
        password_list.append(random.choice(letters_value))

    for i in range(symbols):
        password_list.append(random.choice(symbols_value))

    for i in range(numbers):
        password_list.append(random.choice(numbers_value))

    random.shuffle(password_list)
    password = "".join(password_list)

    print(password)
    cont = input("Generate another password? (y/n):")
    if cont != "y":
        print("Thank you")
        break
