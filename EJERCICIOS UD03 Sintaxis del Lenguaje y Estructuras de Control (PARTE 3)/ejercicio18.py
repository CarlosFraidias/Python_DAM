"""Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales. Mostramos las 
Iniciales en Mayúsculas sí o sí. """

nombre = str(input("Introduce tu nombre: "))
apellido1 = str(input("Introduce tu primer apellido: "))
apellido2 = str(input("Introduce tu segundo apellido: "))

print(f"Iniciales: {nombre[0].upper()}{apellido1[0].upper()}{apellido2[0].upper()}")