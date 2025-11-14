"""Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su 
diferencia, de modo que el resultado sea siempre positivo)."""

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

distancia = 0

if num1 < num2:
    for i in range(num1, num2):
        distancia += 1
elif num1 > num2:
    for i in range(num2, num1):
        distancia += 1
else:
    distancia = 0

print(f"La distancia entre {num1} y {num2} es: {distancia}")