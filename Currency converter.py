

valid_input = ["USD","JPY","INR"]

store = []

while True:
    try:
        amount = float(input("Enter your amount:"))
        source = input("Source currency (USD/JPY/INR):").upper()
        target = input("Target Currency (USD/JPY/INR):").upper()

        key = (source,target)


        currency = {
            ("USD","INR") : amount * 86.05,
            ("INR","USD") : amount/86.05,
            ("USD","JPY") : amount * 145.76,
            ("JPY","USD") : amount/145.76,
            ("JPY","INR") : amount * 0.59,
            ("INR","JPY") : amount/0.59

        }

        if source not in valid_input or target not in valid_input:
            print("Invalid input")
            continue
        else:
            if key in currency:
                data =f"{amount} {source} is equal to {currency[key]} {target}"
                print(data)
                store.append(data)


        cont = input("Want to convert more? (y/n) : ")
        if cont != "y":
            print("Thanks for using our service")
            print(f"Conversion History : {store}")
            break
            

    except ValueError:
        print("Enter a valid input")

