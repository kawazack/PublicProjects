"""
El diccionario es un tipo de dato, parecido a un array pero con indice alfanumérico.
No está ordenado
Es decir, es similar a un array asociativo o a un JSOn.
La clave es que indexa por clave: valor

"""

#Diccionario multidimensional

contacts = [
    { 
        'name': 'Gerard',
        'email': 'gerardo@gerardo.com'  
    },
    {
        'name': 'Jorge',
        'email': 'jorge@jorge.com'
    },
    {
        'name': 'Ricardinho',
        'email': 'ricardinho@ricardinho.com'
    }
]

print (contacts[0]['name'])

print(f"List of contacts:")
print("\n-------------------------------------------------------------")
for contact in contacts:
    print(f"The name of contact {contacts.index(contact)+1} is {contact['name']}")
    print(f"The email of contact {contacts.index(contact)+1} is {contact['email']}")
    print("--------------------------------------------------------------")