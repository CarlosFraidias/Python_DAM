"""Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el 
exponente. Pueden ocurrir tres cosas: 
• El exponente sea positivo, sólo tienes que imprimir la potencia. 
• El exponente sea 0, el resultado es 1. 
• El exponente sea negativo, el resultado es 1/potencia con el exponente positivo."""

base = int(input("Introduce la base: "))
expo = int(input("Introduce el exponente: "))

if expo > 0:
    print(f"Resultado: {base**expo}")
elif expo == 0:
    print(f"Resultado: 0")
else:
    expo = expo * (-1)
    print(f"Resultado: {1/(base**expo)}")