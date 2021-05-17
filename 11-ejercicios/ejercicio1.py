"""
Exercise 1. 
Make a program that has a list of 8 int numbers and do the following:
    - Iterate across the list and show it in screen
    - Sort the list and show it
    - Show the length in the screen
    - Find some element in the list according the user input in keyboard
"""

print("The list for numbers is the following: \n")
my_list = [21, 5, 4, 11, 10, 50, 6, 77]

print(f"\n {my_list} \n")

print("\nThe list have the following list iteration: \n")
for i in my_list:
    print(f"The element n. {my_list.index(i)+1} is {i}")


print("\nThe list ordered from lower to higher is: \n")

my_list.sort()
print(my_list)
print(f"\nThe length of the list is: {len(my_list)}\n")

print("Now is time to look for some number inside the list...\n")

input_number = int(input("What is the number you are looking for?\n"))

check = isinstance(input_number, int)
while not check or input_number <=0:
    input_number = int(input("What is the number you are looking for?\n"))
else:
    if input_number in my_list:
        print ("----------------------------------------")
        print(f"The number {input_number} is in the list")       
    else:
        print ("----------------------------------------") 
        print(f"The number {input_number} is not in the list")

"""Alternative solution to search in list:
Check the values in the list if they have valid index
search = my_list.index(input_number)"""



