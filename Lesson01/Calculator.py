print("Hi, this is a small simple calculator, please type in 2 values and choose an arithmetic operator")

value1 = float(input("Type value 1 here "))
value2 = float(input("Type value 2 here "))
print("""The arithmetic options are

addition (+),
subtraction (-),
multiplication (*),
and division (/).
""")
arithmetic = input("Arithmetic please ")

print(f"{value1} {arithmetic} {value2}, which is")

if arithmetic == "+":
    print(value1 + value2)
elif arithmetic == "-":
    print(value1 - value2 )
elif arithmetic == "/":
    print(value1 / value2)
elif arithmetic == "*":
    print(value1 * value2)
else:
    print("sorry, don't know this value")
