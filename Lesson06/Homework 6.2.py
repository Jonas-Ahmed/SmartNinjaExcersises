import datetime
import random
import json

secret_no = random.randint(1, 30)


wrong_guess = []

class results():
    def __init__(self, score, name, date):
        self.score = score
        self.name = name
        self.date = date

def play_easy():
    name = input("What is your name ? ")
    print(f"Hi {name}")
    score = 0

    while True:

        guess = int(input("Guess the secret number (between 1 and 30): "))
        score += 1

        if guess == secret_no:
            goal = results(score=score, name=name,date=str(datetime.datetime.now()))

            with open("results.json", "w") as score_list:
                score_list.write(str(goal.__dict__))

            print("You've guessed it - congratulations! It's number " + str(secret_no))
            print("Attempts needed: " + str(score))

            again = input("Would you like to try again y/n ").lower()
            if again == "n":
                break

        elif guess > secret_no:
            print("Your guess is not correct... try something smaller")
        elif guess < secret_no:
            print("Your guess is not correct... try something bigger")

        wrong_guess.append(guess)


def play_hard():
    name = input("What is your name ? ")
    print(f"Hi {name}")
    score = 0

    while True:

        guess = int(input("Guess the secret number (between 1 and 30): "))
        score += 1

        if guess == secret_no:
            goal = results(score=score, name=name, date=str(datetime.datetime.now()))

            with open("results.json", "w") as score_list:
                score_list.write(str(goal.__dict__))

            print("You've guessed it - congratulations! It's number " + str(secret_no))
            print("Attempts needed: " + str(score))

            again = input("Would you like to try again y/n ").lower()
            if again == "n":
                break

        elif guess != secret_no:
            print("Wrong guess, try again")

        wrong_guess.append(guess)


def scores():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def top_score():
    score_list = scores()
    new_score_list = sorted(score_list, key=lambda k: k["score"])[:3]
    return new_score_list




selection = input("Would you like to A) play the game easy mode, B) play the game hard mode, C) see the scores or type anything else to quit?")

while True:
    if selection.upper() == "A":
        play_easy()
    elif selection.upper() == "B":
        play_hard()
    elif selection.upper() == "C":
        for x in top_score():
            print(str(x["score"]) + " attempts and date " + str(x["date"]))
    else:
        break

