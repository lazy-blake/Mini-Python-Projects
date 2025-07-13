def quiz_questions(score, data, diff, cat):
    for i in data["quiz"]:
        if i["difficulty"] == diff:
            if i["category"] == cat:
                print(
                    f"{i['question']}\n a) {i['options']['a']}\n b) {i['options']['b']}\n c) {i['options']['c']}\n d) {i['options']['d']}\n"
                )

                ans = input("Your answer (a/b/c/d):").lower()
                if ans == i["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct ans is: {i['answer']}")

    print(f"Total score: {score}")
