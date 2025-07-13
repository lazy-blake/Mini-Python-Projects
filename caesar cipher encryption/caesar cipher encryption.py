from caesar_art import art
from caesar_art import list1, list2
from encrypt_decrypt import decrypt, encrypt

print(art)

valid_input = ["encode", "decode"]

while True:
    user = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    if user in valid_input:
        if user == "encode":
            msg = input("Type your message: ").upper()
            shift = int(input("Type the shift number: "))

            encrypt(msg, shift, list1, list2)

        elif user == "decode":
            msg = input("Type your message: ").upper()
            shift = int(input("Type the shift number: "))

            decrypt(msg, shift, list1, list2)

        cont = input("Wants to continue? (y/n): ")
        if cont != "y":
            print("Goodbye")
            break

    else:
        print("Invalid Input!! Try again")
        continue
