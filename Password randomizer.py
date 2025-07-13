import random
import string

values = string.ascii_letters + string.digits + string.punctuation
while True:
    password_length = int(input("Enter the length of password: "))

    password = ""
    for i in range(len(values)):
        if len(password) == password_length:
            break
        else:
            password += random.choice(values)

    print("Your password is: ", password)

    cont = input("Generate another password? (y/n):")
    if cont != "y":
        print("Thank you")
        break
