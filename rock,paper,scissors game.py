import random


emoji = {
    "r" : "🪨",
    "p" : "📃",
    "s" : "✂️"
}

win = {
    "r" : "s",
    "p" : "r",
    "s" : "p"
}
your_count = 0
comp_count = 0
draw_count = 0

valid_inputs = ("r","p","s","q")
while True: 

        game = input("Rock , papers or scissors? (r/p/s) or Quit(q):").lower()
        computer_choice = random.choice(("s","r","p"))

        if game not in valid_inputs:
            print("Invalid Input")
            continue
        
        if game.lower() == "q":
            print("You quit the game")
            break
        
        print(f"You chose {emoji[game]}")
        print(f"computer chose {emoji[computer_choice]}")
        
        if computer_choice == game:
            print("Draw")
            draw_count += 1

        elif computer_choice == win[game] :
            print("You win")
            your_count += 1            
            
        else:
            print("You lose")
            comp_count += 1
            
        if your_count  >= 2:
            print(f"You are the winner of the game,you won {your_count} times, you lost {comp_count} times and draw happend {draw_count} times")
            play_again = input("Do you want to continue the game? (y/n):")
            if play_again == "y":
                your_count = 0
                comp_count = 0
                draw_count = 0
                print("Reseting score....Starting new game")
                continue
            else:
                break
            
        elif comp_count  >= 2:
            print(f"Computer is the winner of the game BUT you won {your_count} times, you lost {comp_count} times and draw happend {draw_count} times")
            play_again = input("Do you want to continue the game? (y/n):")
            if play_again == "y":
                your_count = 0
                comp_count = 0
                draw_count = 0
                print("Reseting score....starting new game..")
                continue
            else:
                break
            
        

        cont =  input("You want to continue? (y/n):")
        if cont != "y":
            print("\n🏁 Final Score Summary:")
            print(f"✔ Total Wins: {your_count}")
            print(f"✖ Total Losses: {comp_count}")
            print(f"🤝 Total Draws: {draw_count}")
            print("🫶 Thanks for playing!")
            break            
            
        
        
        
        
