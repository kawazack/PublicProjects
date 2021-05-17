import mysql.connector

#Conexion

database = mysql.connector.connect(

    host = "localhost",
    user="root",
    passwd="",
    database="master_python"
)

#how to know the connection was correct?

#print(database)

cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

#check databases created inside mysqlfor bd in cursor:
#print(bd)

