"""
Proyecto de Python y Mysql
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar todas, borrarlas

"""

from users import actions                                                       

print ("""

Actions available:
    - register
    - login
""")
#instance the class
doThe = actions.Actions()

action = input("What you want to do?: ")

if action == "register":
    doThe.register()

elif action == "login":
    doThe.login()
    