"""Dibuja un ordinograma de un programa que suma independientemente los pares y los 
impares de los números comprendidos entre 100 y 200, y luego muestre por pantalla ambas 
sumas."""

pares = 0
impares = 0

for i in range(100, 201):
    if i % 2 == 0:
        pares = pares + i
    else:
        impares = impares + i

print("Suma de pares:", pares, "\nSuma de impares:", impares)
