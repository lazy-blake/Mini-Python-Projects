import random

lvl = {
    "easy": 10,
    "medium": 7,
    "hard": 5,
}
print(r"""
                    ___.                                              .__                                               
  ____  __ __  _____\_ |__   ___________     ____  __ __  ______ _____|__| ____    ____      _________    _____   ____  
 /    \|  |  \/     \| __ \_/ __ \_  __ \   / ___\|  |  \/  ___//  ___/  |/    \  / ___\    / ___\__  \  /     \_/ __ \ 
|   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/  / /_/  >  |  /\___ \ \___ \|  |   |  \/ /_/  >  / /_/  > __ \|  Y Y  \  ___/ 
|___|  /____/|__|_|  /___  /\___  >__|     \___  /|____//____  >____  >__|___|  /\___  /   \___  (____  /__|_|  /\___  >
     \/            \/    \/     \/        /_____/            \/     \/        \//_____/   /_____/     \/      \/     \/ 
""")

a = int(input("Enter the minimum value to guess:"))
b = int(input("Enter the maximum value to guess:"))
attemts = input("Choose a difficulty (easy/medium/hard): ")
print(f"You have {lvl[attemts]} moves")
rand_value = random.randint(a, b)
for i in lvl:
    if i == attemts:
        move = lvl[i]

for i in range(move):
    try:
        guess = input(f"Enter your guess from {a} to {b} or QUIT(Q)= ")
        if guess == "q":
            print("You quit the game")
            break
        guess = int(guess)
        if (move - (i + 1)) == 0:
            print("you are out of attemts, the number was = ", rand_value)
        else:
            if guess > rand_value:
                print(
                    f"NO! You are worng,Guess a smaller number.Remaining attemts = {move - (i + 1)}"
                )
            elif guess < rand_value:
                print(
                    f"NO! You are worng,Guess a larger number.Remaining attemts = {move - (i + 1)}"
                )
            else:
                print("You guessed it right.", "The number is =", rand_value)
                print("-------GAME OVER---------")
                print(f"------Best Score: {i} attemts")
                break

    except ValueError:
        print("Invalid input! Plz enter a valid number")
