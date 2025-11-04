"""Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y 
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario 
incorrecto"""

user = "Pepito"
password = "1234"

print("Inicio de sesión")

introducirUsuario = input("Introduce tu nombre de usuario: ")
introducirContrasena = input("Introduce tu contraseña: ")

if introducirUsuario == user and introducirContrasena == password:
    print("Inicio de sesión correcto")
else:
    print("Inicio de sesión incorrecto")