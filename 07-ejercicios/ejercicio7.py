"""
Exercise 7. Print all non odd numbers between two numbers given by the user
"""
lower_limit= int(input("What is your first number?: "))
upper_limit= int(input("\nWhat is your second number?: "))

if lower_limit < upper_limit:
    for i in range(lower_limit, upper_limit+1):
        if i%2 == 0:
            print(f"{i} is an EVEN number")
        else:
            print(f"{i} is an ODD number")

else:
    print("\nInvalid input. This operation cannot be made")