"""Dibuja un ordinograma de un programa que calcule y escriba la suma y el producto de los
10 primeros números naturales."""

suma = 0
prod = 1

for i in range(1,11):
    suma = suma + i
    prod = prod * i

print("Suma:", suma, "Producto:", prod)