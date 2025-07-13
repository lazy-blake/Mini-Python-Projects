import os


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


while True:
    print(r"""
 _____________________
|  _________________  |
| | CALCULATOR   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|""")

    number = float(input("What's the first number: "))
    while True:
        print("+", "-", "*", "/")
        operation = input("Choose a operation: ")
        number2 = float(input("What's the next number: "))
        if operation == "+":
            output = add(number, number2)
            print(f"{number} + {number2} = {output}")
        elif operation == "-":
            output = sub(number, number2)
            print(f"{number} - {number2} = {output}")
        elif operation == "*":
            output = mul(number, number2)
            print(f"{number} * {number2} = {output}")
        elif operation == "/":
            output = div(number, number2)
            print(f"{number} / {number2} = {output}")

        cont = input(
            f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation:"
        )
        if cont == "y":
            number = output
            continue
        elif cont == "n":
            os.system("cls" if os.name == "nt" else "clear")
            break
