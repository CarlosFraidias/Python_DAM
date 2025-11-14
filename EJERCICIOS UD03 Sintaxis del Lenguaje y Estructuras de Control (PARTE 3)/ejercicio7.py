"""Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas 
horas y minutos corresponde."""

min = int(input("Introduce una cantidad de minutos: "))

horas = 0

while min > 60:
    min -= 60
    horas += 1

print(f"{horas} h, {min} min.")