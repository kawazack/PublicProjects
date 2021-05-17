"""

Ejercicio 9. Do a programm that requests input a number indefinitely
until the user introduces the number 111
"""

input_number = int(input("What is the number that you have in mind?\n"))

while input_number != 111:
    print(f"You have introduced the number {input_number}. Number incorrect. Try again\n")
    input_number = int(input("What is the number that you have in mind?\n"))
else: 
    print("Congratulations!! You guess the magic number :P")
