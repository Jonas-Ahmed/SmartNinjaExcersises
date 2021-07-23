import datetime
import random
import json

secret_no = random.randint(1, 30)


wrong_guess = []

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())


def play_easy():
    while True:
        name1 = name
        attempts = 0
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret_no:
            score_list.append({"Attempts": attempts, "date": str(datetime.datetime.now()), "name": name1, "Secret_no.": secret_no,
            "wrong_guess": wrong_guess})

            print("You've guessed it - congratulations! It's number " + str(secret_no))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret_no:
            print("Your guess is not correct... try something smaller")
        elif guess < secret_no:
            print("Your guess is not correct... try something bigger")

        wrong_guess.append(guess)


def play_hard():
    while True:
        name1 = name
        attempts = 0
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret_no:
            score_list.append({"Attempts": attempts, "date": str(datetime.datetime.now()), "name": name1, "Secret_no.": secret_no,"wrong_guess": wrong_guess})

            #with open("score_list.json", "w") as score_file:
            #    score_file.write(json.dumps(score_list))

            print(f"you guessed correct, the no. is {secret_no}")
            print(f"You guessed {attempts} times")

            again = input("Would you like to try again y/n ").lower()
            if again == "n":
                break

        elif guess != secret_no:
            print("Wrong guess, try again")

        wrong_guess.append(guess)


def scores():
    print(f"Top point: {score_list}")


def main():
    name = input("What is your name ? ")
    print(f"Hej {name}")
    selection = input("Would you like to A) play the game easy mode, B) play the game hard mode, C) see the scores or D) quit?")

    if selection == "A":
        play_easy()
    elif selection == "B":
        play_hard()
#    elif selection == "C":
        # scores()
    else:
        "Break"

main()
