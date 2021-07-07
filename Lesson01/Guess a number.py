secret = 9
guess = int(input("Please guess a number between 1-10\n"))
                
if guess != secret:
    print(f"Sorry wrong number, the correct one was {secret}")
else:
    print(f"you are correct the secret number is {secret}")

