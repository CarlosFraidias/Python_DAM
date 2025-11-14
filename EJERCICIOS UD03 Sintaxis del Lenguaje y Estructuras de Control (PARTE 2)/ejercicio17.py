"""Programa que suma independientemente los pares y los impares de los números 
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas."""

sumaPares = 0
sumaImpares = 0

for i in range(100, 201):
    
    if i % 2 == 0:
        sumaPares += i
    else:
        sumaImpares += i  

print(f"Suma de los números pares: {sumaPares}, Suma de los números impares: {sumaImpares}")




