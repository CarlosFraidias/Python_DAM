"""Crea un programa que pida al usuario dos números y muestre su división si el segundo no 
es cero, o un mensaje de aviso en caso contrario. """

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

if not n2 == 0:
    print(f"división: {n1/n2}")
else:
    print("No se puede dividir entre cero.")