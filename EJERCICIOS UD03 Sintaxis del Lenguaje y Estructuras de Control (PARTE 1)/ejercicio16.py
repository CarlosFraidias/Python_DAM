"""Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene."""

while True:
    num = int(input("Introduce un número del 0 al 99999: "))
    if 0<=num<=99999:
        break

cifras = 0
while num >= 1:
    num = num/10
    cifras += 1

print("El número introduceido tiene", cifras, "cifras.")