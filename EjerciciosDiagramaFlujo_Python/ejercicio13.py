"""Dibuja un ordinograma de un programa que muestre los números desde el 1 hasta el
número N que se introducirá por teclado."""

n = int(input("Introduce el número hasta el cual quieres que se muestren números"))
for num in range(1,n+1):
    print(num)
