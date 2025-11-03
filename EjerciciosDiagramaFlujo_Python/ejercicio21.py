"""Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un 
mensaje de si ha leído número negativo o no."""


neg = False
for i in range(0,100):
    num = int(input("-Introduce un número:"))
    if num < 0:
        neg = True
        
if neg:
    print("Ha habido algún negativo")
else:
    print("No ha habido ningún negativo")
    