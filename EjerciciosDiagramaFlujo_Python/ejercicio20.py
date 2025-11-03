"""Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice 
su factura N! siendo el factorial:
0!=1
1!=1
2!=2*1
…
N!= N*(N-1)*(N-2)*…*1
"""

n = int(input("Introduce un número para realizar su factorial: "))

fact = 1

while n > 0:
    fact = fact * n
    n -= 1

print("Factorial:", fact)