"""
Ejercicio 2. 
a) Write a program that adds values to the list while the
list's length is <120.
b) Print the list:

Plus: Do it with while and for

Pro: Request user to enter values to be stored in the list
"""
mylist = []

for i in range(0,120):
    mylist.append(i)
    print(f"Mostrando el elemento {mylist[i]+1}")
else:
    print("\n#######The Bucle has ended ########")

""" Loop requesting user give input with "while" choice:

    while len(mylist)<119:
    request_number=(input('The list is not full. You can add more stuff. What you want to add?: '))
    mylist.append(request_number)
    else:
        print('The list is already full. Next time :P')
"""
""" Loop requesting user give input with "for" choice:
    for i in range(0,120):
        request_number=(input('The list is not full. You can add more stuff. What you want to add?: '))
        mylist.append(request_number)
    else:
        print('The loop has ended. See you next time! :P')
"""

print(mylist)
print(len(mylist))