import random


def generate_math():
    for i in range(1, 11):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "%", "//", "**"])

        user_input = f"Wie viel ist {a} {operator} {b} ? "

        return {user_input: eval(f"{a}{operator}{b}")}
