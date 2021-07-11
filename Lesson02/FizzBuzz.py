for number in range(1,100):
    print(number)
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz" + " " + str(number))
    elif number % 3 == 0:
        print("fizz" + " " + str(number))
    elif number % 5 == 0:
        print("buzz" + " " + str(number))

