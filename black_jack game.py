import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def compare(sum1, sum2):
    if sum2 > 21:
        print("Dealer went over. You win!!")
    elif sum2 < sum1 <= 21:
        print("You win!!!")
    elif sum1 < sum2 <= 21:
        print("Dealer wins!! you lose 😭!!!")
    else:
        print("It's a draw!")


while True:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == "y":
        print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/
    """)
        user = [random.choice(cards), random.choice(cards)]
        computer = [random.choice(cards)]
        while True:
            sum1 = 0
            for i in user:
                sum1 += i
            print(f"Your cards: {user}, current score: {sum1}")
            print(f"Computer's first card: {computer}")

            if sum1 == 21 and len(user) == 2:
                print("Blackjack!! Game ended")
                break
            elif 11 in user and sum1 > 21:
                user.remove(11)
                user.append(1)

            cont = input("Type 'y' to get another card, type 'n' to pass: ")
            if cont == "y":
                user.append(random.choice(cards))
                sum1 = sum(user)
                if sum1 > 21:
                    print(f"Your cards: {user}, current score: {sum1}")
                    print("You went over. You lose 😭")
                    break
                elif 11 in user and sum1 > 21:
                    user.remove(11)
                    user.append(1)
                    sum1 = sum(user)

            else:
                print(f"Your final hand: {user}, final score: {sum1}")
                sum2 = sum(computer)
                while sum2 < 17:
                    computer.append(random.choice(cards))
                    sum2 = sum(computer)

                    if sum2 == 21 and len(computer) == 2:
                        print("Dealer got Blackjack!! Game ended")
                        break

                print(f"Computer's final hand: {computer}, final score: {sum2}")
                compare(sum1, sum2)
                break

    else:
        print("Thanks for playing")
        break
