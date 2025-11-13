"""Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales. """

suma = 0
prod = 1

for i in range(1,11):
    suma += i
    prod *= i

print(f"Suma: {suma}, Producto: {prod}")