def calculate_love_score(name1, name2):
    name = name1 + name2

    score1 = 0
    for i in name:
        for j in "true":
            if i == j:
                score1 += 1

    score2 = 0
    for i in name:
        for j in "love":
            if i == j:
                score2 += 1

    total1 = str(score1)
    total2 = str(score2)

    total = total1 + total2

    print(total)


calculate_love_score("Kanye West", "Kim Kardashian")

