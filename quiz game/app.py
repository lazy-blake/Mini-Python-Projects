import json
from quiz import quiz_questions


with open(
    "C:\\Users\\akash\\OneDrive\\Documents\\Python\\Projects\\quiz game\\quiz.json",
    "r",
) as f:
    data = json.load(f)

score = 0
diff = input("Choose your diffficulty level (easy/medium/hard):").strip()
cat = input("Choose catagory (Science/Math/Art):").strip()


while True:
    quiz_questions(score, data, diff, cat)
    cont = input("Continue playing? (y/n):")
    if cont == "y":
        diff = (
            input("Choose your diffficulty level (easy/medium/hard):").lower().strip()
        )
        cat = input("Choose catagory (Science/Math/Art):").strip()
        continue
    elif cont != "y":
        print("Thanks for playing")
        break
