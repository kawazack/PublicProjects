texto = "Máster en Python"
texto2 = "conmigo"
numero = 45
decimal = 6.7

print(texto)
print(texto2)
print(numero)
print(decimal)

print("--------------------------------")

#La variable se reasigna

numero = 77

print(numero)

#Concatenación a)

nombre = "Victor"
apellidos = "Robles"
web= "www.victorrobles.es"

print (nombre + " " + apellidos + " - " + web)

#Concatenación b) interpolación (incrustar directamente variables)

print(f"{nombre} {apellidos} - {web}")

#Concatenación c) con método format

print("Hola me llamo {} {} y mi web es. {}".format(nombre, apellidos, web))


