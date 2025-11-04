"""Dibuja un ordinograma de un programa que lea tres números y nos diga cual es mayor, cual 
menor y cuales son iguales."""

num1 = int(input("Introduce el primer número"))
num2 = int(input("Introduce el segundo número"))
num3 = int(input("Introduce el tercer número"))

mayor = num1
if mayor < num2:
    mayor = num2
    
if mayor < num3:
    mayor = num3
    
menor = num1
if menor > num2:
    menor = num2
if menor > num3:
    menor = num3
    
print("El número mayor es:", mayor)
print("El número menor es:", menor)

if num1 == num2 == num3:
    print("Todos los numeros son iguales.")
elif num1 == num2:
    print("El primer y  segundo número son iguales.")
elif num1 == num3:
    print("El primer y tercer número son iguales.")
elif num2 == num3:
    print("El segundo y tercer número son iguales")
else:
    print("no hay números iguales")