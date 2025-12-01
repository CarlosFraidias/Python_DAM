"""Algoritmo que pida un número y diga si es positivo, negativo o 0."""

num = int(input("Introduce un número entero: "))

if num<0:
    print("positivo")
elif num>0:
    print("negativo")
else:
    print("cero")