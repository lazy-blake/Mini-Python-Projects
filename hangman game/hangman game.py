from wonderwords import RandomWord
from hangman_art import hangman_stages, hangman_logo

print(hangman_logo)

r = RandomWord()
computer_guess = r.word()

blank = ""
for blanks in range(len(computer_guess)):
    blank += "_"
print(f"Word to guess: {blank}")

correct_letter = []

lives = 6
wrong_guesses = 0
while lives > 0:
    user_guess = input("Guess a letter: ")

    display = ""
    for i in computer_guess:
        if i == user_guess:
            display += i
            correct_letter.append(i)
        elif i in correct_letter:
            display += i
        else:
            display += "_"

    if user_guess in display:
        print(display)
        print(hangman_stages[wrong_guesses])
    elif user_guess in correct_letter:
        print("You have already guessed this letter")
    elif lives == 1:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        wrong_guesses += 1
        print(hangman_stages[wrong_guesses])
        print(
            f"***********************IT WAS {computer_guess}! YOU LOSE**********************"
        )
        break
    else:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        lives -= 1
        wrong_guesses += 1
        print(hangman_stages[wrong_guesses])

        print(
            f"""****************************{lives}/6 LIVES LEFT****************************"""
        )
