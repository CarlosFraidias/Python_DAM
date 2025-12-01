"""Programa que lea una cadena por teclado y compruebe si es una letra mayúscula."""

mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

cad = str(input("Introduce una cadena de texto: "))

hayMayus = False

for i in cad:
    if i in mayus:
        hayMayus = True
        
if hayMayus:
    print("Hay mayúsculas.")
else:
    print("No hay mayúsculas.")
    