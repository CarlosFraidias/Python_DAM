"""Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un 
mensaje indicando cuántos son positivos y cuantos negativos."""

neg = 0
pos = 0
for i in range(0,100):
    num = int(input("-Introduce un número:"))
    if num < 0:
        neg = True
        
if neg:
    print("Ha habido algún negativo")
else:
    print("No ha habido ningún negativo")