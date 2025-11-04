"""Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta
que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y
cuantos negativos."""

print("Introduce una secuencia de números no nulos\nEscribe 0 cuando quieras parar\nAl final se mostraran cuantos positivos o negativos se escribieron")

num = int(input("Introduce un número: "))

pos = 0
neg = 0

while num != 0:
    if num < 0:
        neg+=1
    else:
        pos+=1
    num = int(input("Introduce un número: "))

print("Positivos:", pos, "\nNegativos:", neg)

print("Fin del programa")