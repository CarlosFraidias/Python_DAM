"""Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius."""

fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))

celsius = (fahrenheit - 32) * (5/9)

print(f"{celsius}º Celsius")