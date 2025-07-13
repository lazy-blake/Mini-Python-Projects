from art import logo, vs
from game_data import data
import random
import os


def questions():
    """This function takes a python file
    and print its content as questions"""
    random_question_A = random.choice(data)
    print(
        f"Compare A: {random_question_A['name']}, {random_question_A['description']}, from {random_question_A['country']}."
    )
    print(vs)
    random_question_B = random.choice(data)
    print(
        f"Against B: {random_question_B['name']}, {random_question_B['description']}, from {random_question_B['country']}."
    )
    return random_question_A, random_question_B


def compare(question_A, question_B):
    """This function takes two questions as input
    and chech which one has more follower and return True or False"""
    user = input("Who has more followers? Type 'A' or 'B': ").lower()

    if question_A["followers"] > question_B["followers"] and user == "a":
        return True

    elif question_B["followers"] > question_A["followers"] and user == "b":
        return True

    else:
        return False


score = 0
while True:
    print(logo)
    while True:
        A, B = questions()
        if compare(A, B):
            score += 1
            os.system("cls")
            print(logo)
            print(f"You're right! Current score: {score}")
            continue
        else:
            os.system("cls")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

    cont = input("Play again? (y/n): ").lower()
    if cont != "y":
        print("Thanks for playing!!")
        break
