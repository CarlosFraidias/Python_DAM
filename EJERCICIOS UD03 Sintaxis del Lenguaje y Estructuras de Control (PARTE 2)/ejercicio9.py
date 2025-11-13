"""Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego 
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos. """

contadorNeg = 0
contadorPos = 0

while True:
    num = int(input("Introduce un número pos o neg, 0 si deseas terminar: "))
    if(num == 0):
        break
    elif(num < 0):
        contadorNeg += 1
    else:
        contadorPos += 1

print(f"Negativos: {contadorNeg}, Positivos: {contadorPos}")