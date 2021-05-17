"""Ejercicio 3.

Hay que crear 4 variables; una lista, un string, un número y un booleano
Luego que imprima un mensaje según el tipo de dato de cada variable.
Usar funciones

"""

def translate_type(data_type):
    result = None
    if data_type == list:
        result = "LIST"
    elif data_type == str:
        result  = "STRING"
    elif data_type == int:
        result = "NUMBER"
    elif data_type == bool:
        result = "BOOLEAN"
    return result



def check_type (data, data_type):
    test = isinstance(data, data_type)
    result = ""
    if test:
        result= f"This data is of correct type {translate_type(data_type)}"

    else:
        result = "El tipo de dato no es reconocido"

    return result

my_list= ["stuff", 77]
string= "This is the string"
number= 777
boolean= True

print(check_type(my_list, list))
print(check_type(number, int))
print(check_type(string, str))    
print(check_type(boolean, bool))
print(check_type(None, bool))
