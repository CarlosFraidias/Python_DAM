"""Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia 
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla. """

a = int(input("Introduce un valor a: "))
b = int(input("Introduce un valor b: "))

potencia = 1

for i in range(b):
    potencia *= a

print(potencia)