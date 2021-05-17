"""

- Imprimir por pantalla los cuadrados de los 60 primeros números naturales
- Resolverlo con bucle for y bucle while

"""
print("\n########## Bucle for ##########\n")

counter = 0

for counter in range(1, 61):
    print(f"The square of the number {counter} is {counter*counter}")
else:
    print("\n>>>>>>>End of the bucle for<<<<<<<\n")

print("######### Bucle while ########\n")

counter = 0

while counter <= 60:
    print(f"The square of the number {counter} is {counter*counter}")
    counter += 1

print(f"\n>>>>>End of the while bucle<<<<<<")