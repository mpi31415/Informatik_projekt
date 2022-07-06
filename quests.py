import random


def generate_quest():
    Haustier = True
    if Haustier:

        choose = []
        while len(choose) < 5:
            x = random.randint(0, 10)
            if x not in choose:
                choose.append(x)
        print(choose)

        quest = ["Wäsche machen", "Mit dem Hund Gassi", "Polizei rufen wegen Nachbarn", "Religion wechseln",
                 "Mit meinem Lieblings Atom Kriegsverbrechen in Yugoslavien begehen", "Mittagsschlaf",
                 "Affen rekrutieren für meine Armee", "Müll sammeln", "Zur Arbeit beim Indischen Call Center gehen",
                 "Fake News im Netz verbreiten", "Wettrennen gegen Steven Hawkins machen"]

        for i in choose:
            print(quest[i])
        else:
            choose = []
        while len(choose) < 5:
            x = random.randint(0, 9)
            if x not in choose:
                choose.append(x)
        print(choose)

        quest = ["Wäsche machen", "Polizei rufen wegen Nachbarn", "Religion wechseln",
                 "Mit meinem Lieblings Atom Kriegsverbrechen in Yugoslavien begehen", "Mittagsschlaf",
                 "Affen rekrutieren für meine Armee", "Müll sammeln", "Zur Arbeit beim Indischen Call Center gehen",
                 "Fake News im Netz verbreiten", "Wettrennen gegen Steven Hawkins machen"]

        for i in choose:
            return quest[i]


