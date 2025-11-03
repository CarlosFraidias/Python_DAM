"""Dibuja un ordinograma de un programa que lea dos números y nos diga cual es mayor o si 
son iguales."""

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if num1>num2:
    print("El numero", num1, "es el mayor")
elif(num1==num2):
    print("Ambos números son iguales")
else:
    print("El numero", num2, "es el mayor")