"""Escribe un programa que pida un nombre de usuario y una contraseña y si se ha 
introducido "pepe" y "asdasd" se indica "Has entrado al sistema", sino se da un error. """

user = str(input("Introduce tu nombre: "))
password = str(input("Introduce tu contraseña: "))

if user == "pepe" and password == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error")

