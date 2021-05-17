#Ejemplo tablas de multiplicar

randomvar = 5
print("\n ############## Example #################")

numero_usuario= int(input("What number wants the table be calculated?"))

if numero_usuario < 1:
    numero_usuario = 1

print(f"###### Multplication table of number {numero_usuario} #######\n")

for numero_tabla in range(1,11):

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else: 
    print("End of Table.\n")