"""
Ejercicio 8.
    - We need to extract the % of a number depending on the inputs of the user;
    - inputs of user: number and %.

"""
number_user = int(input("What is your number?\n"))
percentage_user = int(input("What is the percentage you want to get? \n"))

print(f"The {percentage_user}% of {number_user} is {(number_user*percentage_user)/100}")