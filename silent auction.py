import os

print(r'''
           ___________
           \         /
            )_______(
            |"""""""|_.-._,.---------.,_.-._
            |       | | |               | | ''-.
            |       |_| |_             _| |_..-'
            |_______| '-' `'---------'` '-'
            )"""""""(
           /_________\
           `'-------'`
         .-------------.
     jgs/_______________\
''')


def calculating_bid(bids_dictionary):
    """it takes evry value of the bids entered by the user
    and compare to see which is the max value and who is the winner"""
    winner = ""
    max_value = 0
    for i in bids_dictionary:
        values = bids_dictionary[i]
        if values > max_value:
            max_value = values
            winner = i

    return f"The winner is {winner} with the bid of ${max_value}"


all_bids = {}

while True:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : "))

    all_bids[name] = bid

    cont = input("Are there any other biddders? (y/n)")
    if cont == "y":
        os.system("cls" if os.name == "nt" else "clear")
        continue
    else:
        output = calculating_bid(all_bids)
        print(output)
        break
