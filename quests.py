import random


def generate_math():
    for i in range(1, 11):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "%", "//", "**"])

        user_input = f"Wie viel ist {a} {operator} {b} ? "

        return {user_input: eval(f"{a}{operator}{b}")}


def generate_quest():
    Quest = ["dance", "catch bugs", "swimming", "train", "sleep"]
    Kek = 4
    Axe = 1
    Rod = 0
    Pet = 0

    if Axe == 1:
        Quest.append("chop trees")
        Kek = Kek + 1
    else:
        None

    if Rod == 1:
        Quest.append("fishing")
        Kek = Kek + 1
    else:
        None

    if Pet == 1:
        Quest.append("train pet")
        Kek = Kek + 1
    else:
        None

    choose = []
    while len(choose) < 2:
        x = random.randint(0, Kek)
        if x not in choose:
            choose.append(x)


    for i in choose:
        return Quest[i]
