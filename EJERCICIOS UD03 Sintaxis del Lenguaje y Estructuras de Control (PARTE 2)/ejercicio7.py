"""Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún
número negativo o no."""

neg = False

for i in range(1, 101):
    num = int(input("Introudce un número: "))
    if num  < 0:
        neg = True

if neg:
    print("Ha habido algun negativo")
else:
    print("No han habido negativos")