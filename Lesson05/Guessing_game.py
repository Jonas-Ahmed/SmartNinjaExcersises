import datetime
import random
import json

secret_no = random.randint(1, 30)


wrong_guess = []

def play_easy(name):
    while True:
        attempts = 0
        score_list = scores()
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret_no:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": name, "Secret_no.": secret_no,
            "wrong_guess": wrong_guess})

            print("You've guessed it - congratulations! It's number " + str(secret_no))
            print("Attempts needed: " + str(attempts))

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            again = input("Would you like to try again y/n ").lower()
            if again == "n":
                break

        elif guess > secret_no:
            print("Your guess is not correct... try something smaller")
        elif guess < secret_no:
            print("Your guess is not correct... try something bigger")

        wrong_guess.append(guess)


def play_hard(name):
    while True:
        attempts = 0
        score_list = scores()
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret_no:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": name, "Secret_no.": secret_no,"wrong_guess": wrong_guess})

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print(f"you guessed correct, the no. is {secret_no}")
            print(f"You guessed {attempts} times")

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
    new_score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return new_score_list



name = input("What is your name ? ")
print(f"Hej {name}")
selection = input("Would you like to A) play the game easy mode, B) play the game hard mode, C) see the scores or type anything else to quit?")

while True:
    if selection.upper() == "A":
        play_easy(name)
    elif selection.upper() == "B":
        play_hard(name)
    elif selection.upper() == "C":
        for x in top_score():
            print(str(x["attempts"]) + " attempts and date " + str(x["date"]))
    else:
        break

