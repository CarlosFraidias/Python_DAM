"""Programa que lea un número positivo N y calcule y visualice su factorial N! Siendo el
factorial:
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2* 1
N! = N * (N-1) * (N-2) * … * ."""

n = int(input("Introduce un número para hacerle el factorial: "))

fact = 1
for i in range(1,n+1):
    fact *= i

print(fact)