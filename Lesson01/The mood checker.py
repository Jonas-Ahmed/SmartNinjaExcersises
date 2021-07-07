name = input("Hi, what is your name?\n")
print(f"Hi {name}, hope you are well")
print(""" I would like to hear, how you mood is.

Might I give the following suggestions

Happy
Sad
Nervous
Excited
Relaxed
""")

mood = input(f"{name}, would you please inform me of your mood ?\n")


if mood == "Happy":
    print(f"{name}, it is great to see you happy!")
elif mood == "Sad":
    print("That is not good, hope you feel better tomorrow")
elif mood == "Nervous":
    print("Take a deep breath 3 times.")
elif mood == "Relaxed":
    print(f"Good to hear that you are {mood}")
elif mood == "Excited":
    print(f"{name}, don't get to {mood} ;)")
else:
    print("I don't recognize this mood")

