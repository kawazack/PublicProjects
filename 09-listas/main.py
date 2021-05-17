#Create an Unidimensional list with variable = [0,1,2,3]
#Create a multidimensional list and practice with bucles


contacts = [

    [
        'Antonio',
        'antonio@antonio.com'

    ],
    [ 
        'Luis',
        'luis@luis.com'
    ],
    [
        'Rigoberto',
        'rigoberto@rigoberto.com'
    ]
]

print(contacts[0][0])

for contact in contacts:
    print(f"{contacts.index(contact)+1} - {contact}")


for contact in contacts:
    print(f"Details of the contact: {contacts.index(contact)+1}\n")
    for element in contact:
        if contact.index(element) == 0:
            print(f"Name: {element}")
        else:
            print(f"Email: {element}")
    print(f"\n")


#sort

musicians = ['Mt85', 'FMA Orchestra', 'J. Balvin', 'Robbie Williams']
numbers = [1,6,7,3,7,15,10,2]

def sort_function (e):
    return len(e)

print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
musicians.sort(key=sort_function, reverse=True)
print(musicians)


#Delete elements

#Buscar

#Cuantas veces aparece un elemento

print(numbers.count(7))