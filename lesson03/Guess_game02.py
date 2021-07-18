import datetime
import random
import json


name = input("Hej, hvad hedder du ? ")
print(f"Hej {name}")

print("Dette er en gætte leg, gæt et nr. mellem 1 og 30")

secret_no = random.randint(1, 30)

attempts = 0

wrong_guess = []

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print(f"Top point: {score_list}")


while True:
    guess = int(input("Gæt nr. "))
    attempts += 1

    if guess == secret_no:
        score_list.append({"gange": attempts, "dato": str(datetime.datetime.now()), "name": name, "hemmelige_nr.": secret_no, "wrong_guess": wrong_guess})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print(f"Du gættede korrekt, nr. er {secret_no}")
        print(f"Du gættede {attempts} gange")

        again = input("Vil du prøve igen j/n ").lower()
        if again == "n":
            break

    elif guess < secret_no:
        print("Gæt er for lavt, prøv med et højere nr.")
        wrong_guess.append(guess)

    elif guess > secret_no:
        print("Gæt er for højt, prøv med et lavere nr.")
        wrong_guess.append(guess)

print(wrong_guess)
# forsøgt at sortere med disse funktioner uden held :( import collections / import operator og forskellige loops