print("Hi, this is a small kg/miles converter, below please type in a value and to what it should be converted")

again = True

while again == True:
    value = float(input("Please type in the value, you want converted\n"))
    measure = input("kg or miles ? \n")
    measure1 = measure.lower()
    if measure1 == "kg":
        print("Is" + " " + str(value*1.609344) + " " + "kg")
        repeat = input("would you like to try again ? y/n ")
        if repeat == "n":
            print("Goodbye, have a nice day")
            again = False
        else:
            continue

    elif measure1 == "miles":
        print("Is" + " " + str(value*0.62137) + " " + "miles")
        repeat = input("would you like to try again ? y/n ")
        if repeat == "n":
            print("Goodbye, have a nice day")
            again = False
        else:
            continue

    else:
        print("Sorry this converter is only for kg or miles")
        repeat = input("would you like to try again ? y/n ")
        if repeat == "n":
            print("Goodbye, have a nice day")
            again = False
        else:
            continue





