"""

Pedir 2 números al usuario
Hacer todas las operaciones básicas de una calculadora y mostrarlo en pantalla

"""

number1= int (input("Introduce the first number: "))
number2 = int(input("Introduce the second number: "))

addition = number1 + number2
substraction = number1 - number2
multiplication = number1*number2
division= number1/number2
rest = number1%number2

print(f"\nThe addition of number1 and number2 is {addition}\n")
print(f"The substraction of number1 and number2 is {substraction}\n")
print(f"The multiplication of number1 and number2 is {multiplication}\n")
print(f"The division of number1 and number2 is {division}\n")
print(f"The rest of number1 and number2 is {rest}\n")
