"""
Ejercicio 6. 
Mostrar todas las tablas de multiplicar del 1 al 10.

Mostrar también el título de la tabla y luego la multiplicación del 1 al 10.
"""

counter_table = 0
counter_number = 0

while counter_table <= 100:   
    print(f"\n############## This is the table of number {counter_table} ##############\n")
    while counter_number <=100:
        print(f"{counter_table} x {counter_number} = {counter_table*counter_number}")
        counter_number+=1
    counter_number=0
    counter_table+=1
else:
    print ("\nEnd of the table's loop")