"""Create a function that depnding of user input, generates
the multiplication table of the user input
"""
#Example 1: Define parameterized function

def showTable (user_number):
    print(f"\n######## This is the table of number {user_number} #######\n")

    for counter in range(11):
        print(f"{user_number}x{counter}={user_number*counter}")

#Example 2: Use a bucle for to be input when the function is called

for number_table in range(1,11):
    showTable(number_table)