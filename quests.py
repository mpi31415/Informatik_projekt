import random


def ask_for_int(message: str) -> int:
    number = None
    while type(number) != int:
        try:
            number = int(input(message))
        except ValueError:
            print("Das ist keine Ganzzahl!")
    return number


def generate_math():
    punkte = 0
    combo_true = 1
    combo_false = 1
    for i in range(1, 11):
        print(f"Runde {i}:")
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "%", "//", "**"])

        user_input = ask_for_int(f"Wie viel ist {a} {operator} {b} ? ")

        if user_input == eval(f"{a}{operator}{b}"):
            punkte += i * combo_true ** 2
            combo_true += 100
            combo_false = 1
            print("Korrekt")
        else:
            punkte -= i * combo_false ** 2
            combo_false += 100
            combo_true = 1
            print("Falsch")

        print(f"Punkte: {punkte}\n")
