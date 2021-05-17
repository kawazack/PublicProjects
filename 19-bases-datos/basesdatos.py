import sqlite3

conexion = sqlite3.connect('pruebas.db')

#Crear cursor (permite ejecutar consultas)

cursor= conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo varchar(255),
descripcion text,
precio int(255)
)""")

#Save changes
conexion.commit()

#close conexion (needed afte the commands interacting with database)

#Insert data into the database
#cursor.execute("INSERT INTO productos VALUES (null, 'zapatillas', 'esto son zapatillas', '20')")
conexion.commit()

"""
Execute sql registers one by one

conexion.execute("DELETE FROM productos WHERE id=1")
conexion.execute("DELETE FROM productos WHERE id=2")
conexion.execute("DELETE FROM productos WHERE id=3")
conexion.execute("DELETE FROM productos WHERE id=4")
conexion.execute("DELETE FROM productos WHERE id=5")"""

"""Unsolved doubt: How to make for delete registers and reset the id to don't be interrupted?
cursor.execute("DBCC CHECKIDENT ('Productos', RESEED, 0)
GO") """

cursor.execute ("SELECT * FROM productos") 

#print(cursor)

productos = cursor.fetchall()

for producto in productos:
    print(producto)


conexion.close()