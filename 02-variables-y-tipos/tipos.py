#tipo de dato

nada = None
cadena = "Hola soy Víctor Robles WEB"
cadena = "Desarrollador web"
booleano = True
lista = [10, 20, 30, 40, 50]
listaString = [44, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre": "Victor Robles",
    "apellido": "Robles",
    "curso": "Master en Python",
}

rango = range(9)
dato_byte= b"Probando"

#imprimir la variable
print(cadena)
print(booleano)
print(lista)
print(listaString)
print(tuplaNoCambia)
print(diccionario)
print(rango)

for i in rango:

    print(i)

print(dato_byte)

#imprimir tipo de dato
print(type(cadena))
print(type(booleano))
print(type(lista))
print(type(listaString))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

#convertir tipo de dato a otro

texto = "Soy el texto"
numero = str(777)
print(texto + " " + numero)