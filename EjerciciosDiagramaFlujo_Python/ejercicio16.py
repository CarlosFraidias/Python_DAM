"""Dibuja un ordinograma de un programa que lea un número y dice si es positivo o negativo,
consideramos el cero como positivo."""

num = int(input("Introduce un número para ver si es negativo o positivo: "))

if num < 0:
    print("El número introducido es negativo")
else:
    print("El número introducido es positivo")