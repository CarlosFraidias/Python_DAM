"""Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de 
10."""

num = int(input("Introduce un número"))

if num % 10 == 0:
    print("el número introducido es múltiplo de 10")
else:
    print("el número introducido no es múltiplo de 10")