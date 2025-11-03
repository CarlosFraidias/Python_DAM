"""Dibuja un ordinograma de un programa que muestre los números pares comprendidos
entre el 1 y el 200. Esta vez utiliza un contador sumando de 1 en 1."""

num = 1
while num <= 200:
    if num % 2 == 0:
        print(num)
    num=num+1
