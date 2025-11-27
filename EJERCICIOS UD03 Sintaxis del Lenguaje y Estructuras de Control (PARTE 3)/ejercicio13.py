"""Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
Python3  no  tiene  ninguna  función  predefinida  que  permita  calcular  la  raíz  cúbica,  ¿Cómo  se 
puede calcular?"""
import math

num = int(input("Introduce un número para mostrar su raiz cuadrada y cubica: "))

cuandrada = math.sqrt(num)
cubica = num**(1/3)

print(f"Raíz cuadrada: {cuandrada}\nRaíz cúbica: {cubica}")



