"""
Ejercicio 5. Make an script that shows all numbers in console between
two numbers given by the user

"""

number1 = int(input("What is your first number?\n"))
number2 = int(input("What is your second number?\n"))


if number1 < number2:
    for i in range(number1, (number2+1)):
        print(i)
    else:
        print("\nLoop executed succesfully. End of the loop")
else:
    print("The operation cannot be executed due to upper limit of the interval is lower than the lower limit and this is a logic incongruence")

